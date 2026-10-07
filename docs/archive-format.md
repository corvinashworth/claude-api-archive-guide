# Archive format

`checked_at` is the date of the provider response. `source` is the exact
metadata endpoint. `official_source` is a vendor page used for dates and list
prices. A model row has a stable ID, context and output limits, endpoint family,
and separate effective and official price objects. Release and retirement dates
remain `null` until a primary vendor page is checked.

This format intentionally excludes prompts, user data, access tokens, and
copied vendor documentation. A new snapshot is additive: do not rewrite old
files when a provider changes a model's limits.
