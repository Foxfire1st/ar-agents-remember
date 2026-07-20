# mcp/src/agents_remember/serving/conversation/control/previews.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/previews.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `0be0099744bf1287805acf0b95072127b70f7104`|
| lastVerifiedCommitDate |  2026-07-20T15:34:11+02:00|
| governingOverview | `overview.md` |

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

`payload_digest` (L28) is the authority-parity digest, `sha256:`-prefixed: text-only is
byte-identical to the authority's construction; canonical asset identity is covered only when assets
are present. `redacted_preview` (L51) strips control characters, collapses whitespace, applies
`redact_secrets`, and bounds via `_clusters` (L65) to `MAX_PREVIEW_CLUSTERS = 96` (L22), returning
`(preview, truncated)`. `_clusters` approximates grapheme clusters with stdlib only — base characters
plus combining marks, `_VARIATION_SELECTORS` (L25), and `_ZWJ` (L24) continuations — so it never
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

## Docs References

No Domain Documentation source is configured; the transform is repository-owned.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The redaction policy is the repository tool-report helper; the asset reference type and the
authority's digest construction are the parity targets.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The repository `redact_secrets` policy applied to every preview. | L1-L80 | [tool_reports.py](agents-remember/mcp/src/agents_remember/mcp/tool_reports.py) |
| The `AssetReference` type covered by the asset-form digest. | L1-L120 | [harness_control_models.py](agents-remember/mcp/src/agents_remember/serving/harness_control_models.py) |
| The submission authority's payload-digest construction this mirrors byte-for-byte. | L1-L120 | [harness_submission_authority.py](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the deterministic
  preview/digest transforms — control-char strip, whitespace collapse, secret redaction, the 96
  grapheme-ish cluster bound that never splits a cluster, and the authority-parity payload digest.
  Verification is blank because the new source file is uncommitted; closeout owns its first source
  stamp.
