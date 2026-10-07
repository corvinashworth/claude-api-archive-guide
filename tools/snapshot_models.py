#!/usr/bin/env python3
"""Save a dated, read-only Claude model-list snapshot and report ID changes."""
import argparse
import datetime as dt
import json
import pathlib
import urllib.request

USER_AGENT = "claude-api-archive-guide/1.0"


def fetch(url: str) -> list[dict]:
    request = urllib.request.Request(url.rstrip("/") + "/models", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(request, timeout=30) as response:
        raw = json.load(response)
    data = raw.get("data", raw) if isinstance(raw, dict) else raw
    if not isinstance(data, list) or not all(isinstance(row, dict) and row.get("id") for row in data):
        raise ValueError("unexpected model-list response")
    return data


def main(argv=None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-url", default="https://argolink.io/v1")
    parser.add_argument("--out", default="data")
    args = parser.parse_args(argv)
    data = fetch(args.base_url)
    models = []
    for row in data:
        if row["id"].startswith("claude-"):
            models.append({"id": row["id"], "owned_by": row.get("owned_by"),
                           "endpoint": "/v1/messages", "argolink": None,
                           "official_pricing": None, "release_date": None,
                           "retirement_date": None, "source_row": row})
    out = pathlib.Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    today = dt.date.today().isoformat()
    target = out / f"claude-models-{today}.json"
    previous = sorted(out.glob("claude-models-*.json"))
    old_ids = set()
    if previous:
        try:
            old_ids = {row["id"] for row in json.loads(previous[-1].read_text(encoding="utf-8")).get("models", [])}
        except (OSError, ValueError, KeyError, TypeError):
            pass
    payload = {"checked_at": today, "source": args.base_url.rstrip("/") + "/models", "models": models}
    target.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
    new_ids = {row["id"] for row in models}
    print(json.dumps({"file": str(target), "added": sorted(new_ids - old_ids), "removed": sorted(old_ids - new_ids)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
