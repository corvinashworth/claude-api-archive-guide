# Chat request boundary

`claude-opus-5` uses `/v1/messages`. Keep the request small enough to debug and record the returned request ID.

- Authentication: `Authorization: Bearer $ARGOLINK_API_KEY`
- Model: `claude-opus-5`
- Base URL: `https://api.argolink.io`
- Reasoning choices currently listed for this model: `low, medium, high, xhigh, max`.

Do not silently translate a timeout into a second submission. When a tool call or structured response is required, keep the response envelope and error body in the redacted diagnostic record.
