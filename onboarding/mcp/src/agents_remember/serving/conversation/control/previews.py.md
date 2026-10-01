# mcp/src/agents_remember/serving/conversation/control/previews.py

## Governing Overview

[Structured conversation control overview](overview.md)

## Purpose

The deterministic public preview transform and the authority-parity content digest. The queue
projection's `redactedPreview` is identification copy for the authenticated caller's own cockpit row
(never recovery authority): strip control characters, collapse whitespace, apply the repository
secret-redaction policy, and return at most 96 grapheme-ish clusters plus `previewTruncated`. The
digest mirrors the submission authority's exact payload-digest construction so the daemon-held digest
and the authority's idempotence digest always agree for the same content.

## Code Commentary

### Logic

cit:([`payload_digest`], mcp/src/agents_remember/serving/conversation/control/previews.py:28-48) is the authority-parity digest, `sha256:`-prefixed: text-only is
byte-identical to the authority's construction; canonical asset identity is covered only when assets
are present. cit:([`redacted_preview`], mcp/src/agents_remember/serving/conversation/control/previews.py:51-62) strips control characters, collapses whitespace, applies
`redact_secrets`, and bounds via cit:([`_clusters`], mcp/src/agents_remember/serving/conversation/control/previews.py:65-91) to cit:([`MAX_PREVIEW_CLUSTERS`], mcp/src/agents_remember/serving/conversation/control/previews.py:24-24), returning
`(preview, truncated)`. `_clusters` approximates grapheme clusters with stdlib only — base characters
plus combining marks, cit:([`_VARIATION_SELECTORS`], mcp/src/agents_remember/serving/conversation/control/previews.py:27-27), and cit:([`_ZWJ`], mcp/src/agents_remember/serving/conversation/control/previews.py:26-26) continuations — so it never
splits a cluster at the cut edge (proven over ZWJ chains) and only ever conservatively merges two.

### Conventions

The preview is identification copy, not recovery — it may lose information; the digest is exact and
must match the authority byte-for-byte. `regex` is not a declared dependency (only transitive via
tiktoken), so the cluster bound is a documented stdlib approximation.

### Invariants And Boundaries

- The preview never splits a grapheme cluster at the 96-cluster cut edge; it only conservatively
  merges (documented approximation).
- The digest is byte-identical to the submission authority's payload digest for the same content
  (text-only and asset-covering forms).
- Control characters and repository secrets never survive into a preview.

### Todos

None.

## Evidence

### Docs References

No Domain Documentation source is configured; the transform is repository-owned.

No configured domain documentation was available.

### Repo-Internal References

The redaction policy is the repository tool-report helper; the asset reference type and the
authority's digest construction are the parity targets.

- The repository `redact_secrets` policy applied to every preview. [1]
- The `AssetReference` type covered by the asset-form digest. [2]
- The submission authority's payload-digest construction this mirrors byte-for-byte. [3]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
