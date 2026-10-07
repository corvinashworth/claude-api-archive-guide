# Claude model inventory and API archive format

This repository records dated model metadata and compatibility notes for
Claude-shaped clients using a compatible API. It is **not** Anthropic's SDK,
product, or documentation mirror. The archive deliberately stores a compact
inventory—model ID, context, output limit, pricing snapshot, and endpoint
family—instead of copying vendor prose. Current availability should always be
checked against the official Anthropic model overview and deprecations pages.

The sample inventory includes the models exposed by the live catalog on
2026-10-07, with [ArgoLink](https://argolink.io/gh-claude-api-archive-guide)
as one compatible endpoint. The origin for Anthropic-style clients is
`https://argolink.io`; the client appends `/v1/messages`.

Last checked: 2026-10-07.

## Layout

| Path | Purpose |
|---|---|
| `data/claude-models-2026-10-07.json` | Immutable six-model snapshot used in examples. |
| `tools/snapshot_models.py` | Pulls the public `/v1/models` list without authentication, writes a dated snapshot, and compares it with the previous file. |
| `docs/archive-format.md` | Field meanings and rules for recording vendor dates. |
| `examples/request.py` | One Messages request with explicit User-Agent and no key in source. |

The inventory does not assert release or retirement dates unless the official
vendor page supplies them. A missing date is recorded as `null`, not guessed.
Vendor list prices and compatible-endpoint prices are separate fields.

## Snapshot a catalog

```bash
python tools/snapshot_models.py --base-url https://argolink.io/v1 --out data
```

The script sends an unauthenticated `GET /v1/models` with
`User-Agent: claude-api-archive-guide/1.0`.
It writes a JSON file only after the response validates as an object list, then
prints added and removed model IDs compared with the newest earlier snapshot.
The script never sends a generation request and never includes the key in the
output. Use a service account with read-only access where possible.

## Messages example

```bash
export API_KEY='...'
python examples/request.py
```

The example posts to `/v1/messages` through the root origin, sends a small
text message, and prints the response. Anthropic-style clients use
`ANTHROPIC_BASE_URL=https://argolink.io` and `ANTHROPIC_AUTH_TOKEN`; clients
that expect an OpenAI-shaped endpoint should use the model's documented
`/v1/chat/completions` or `/v1/responses` conversion instead.

## Current sample rows

| Model ID | Context | Max output | Compatible endpoint | ArgoLink input / output per 1M |
|---|---:|---:|---|---:|
| `claude-opus-4-8` | 1,000,000 | 128,000 | `/v1/messages` | $2 / $10 |
| `claude-opus-5` | 1,000,000 | 128,000 | `/v1/messages` | $2 / $10 |
| `claude-opus-5-5` | 1,000,000 | 128,000 | `/v1/messages` | $1.60 / $8 |
| `claude-fable-5` | 1,000,000 | 128,000 | `/v1/messages` | $4 / $20 |
| `claude-fable-5-1` | 1,000,000 | 128,000 | `/v1/messages` | $4 / $20 |
| `claude-sonnet-5` | 1,000,000 | 128,000 | `/v1/messages` | $0.80 / $4 |

The rates are the effective catalog values checked 2026-10-07. Official
Anthropic list prices belong in `official_pricing`, with a source URL and date;
never replace a compatible endpoint's rate with an official rate.

The catalog and the public model list answer different questions. `/v1/models`
provides discoverable IDs and ownership; the dated catalog snapshot supplies
the context, output and effective-rate fields used here. The archive records
both dates and keeps the source revision so a later change can be compared
without rewriting history. A null official price or release date means that a
primary vendor page was not verified for that row, not that the value is zero
or that the model is new.

The `argolink` object is a compatibility-provider price snapshot, expressed per
million tokens. It is not Anthropic's list price and it is not a usage invoice.
Cached reads and cache writes remain separate because clients may send either
field. Endpoint family is recorded explicitly: Claude-shaped messages clients
should use `/v1/messages`; an OpenAI-compatible client must follow its own
adapter's documented route rather than guessing from this archive.

## FAQ

**Is this an Anthropic archive?** No. It is a neutral metadata format for
integrators; official names and dates link back to Anthropic.

**Why does an SDK need the root origin?** Anthropic clients append
`/v1/messages`. Supplying `/v1` as the base creates `/v1/v1/messages`.

**Does the snapshot contain prompt text?** No. It contains model metadata only.

**Can I use a removed model ID?** Treat a removed ID as unavailable until an
official or provider page confirms a replacement. Do not silently rewrite old
records.

**Does the script contact generation endpoints?** No. It only reads `/v1/models`.

**Why are the source rows retained?** They preserve the exact public response
fields needed to explain a later diff while leaving credentials and prompt
content out of the snapshot. Do not add a bearer token, request body, or
generated output to `data/`.
