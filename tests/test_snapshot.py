import json
from pathlib import Path

def test_snapshot_is_dated_and_separates_prices():
    data=json.loads((Path(__file__).parents[1]/"data/claude-models-2026-10-07.json").read_text())
    assert data["checked_at"] == "2026-10-07"
    assert all("argolink" in m and "official_pricing" in m for m in data["models"])
