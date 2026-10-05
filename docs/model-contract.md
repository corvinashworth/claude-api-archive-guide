# Claude Opus 5 model contract

This table is intentionally short. Update it only after checking the live [Argolink model page](https://argolink.io/gh-claude-api-archive-guide).

- Model ID: `claude-opus-5`
- Argolink model page: `https://argolink.io/gh-claude-api-archive-guide` (tracked shortlink; destination is the model page)
- Endpoint family: `/v1/messages`
- Context: `1,000,000` tokens; max output: `128000` tokens.
- Reasoning efforts: `low, medium, high, xhigh, max`; default: `high`.
- Listed token rates: input `$5` / output `$25` per million tokens; cached input `$0.5` when listed.

## Request boundary

- Authentication: `Authorization: Bearer $ARGOLINK_API_KEY`.
- Base URL: `https://api.argolink.io`.
- Model ID: `claude-opus-5`.
- Endpoint: `/v1/messages`.
- For media jobs, save the returned task identifier, poll the documented task endpoint, and download the final URL before its retention window ends.

Do not copy prices or limits from third-party lists into this file; the model page and catalog are the current source of truth.
