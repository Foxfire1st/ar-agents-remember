# mcp/src/agents_remember/serving/conversation/control/previews.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/control/previews.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T15:45+02:00 |
| lastVerifiedCommitHash |  `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`|
| lastVerifiedCommitDate |  2026-08-14T14:36:50+02:00|
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

## Docs References

No Domain Documentation source is configured; the transform is repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The redaction policy is the repository tool-report helper; the asset reference type and the
authority's digest construction are the parity targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| The repository `redact_secrets` policy applied to every preview. | `redact_secrets` | mcp/src/agents_remember/kernel/primitives/tool_reports.py:72-79 |
| The `AssetReference` type covered by the asset-form digest. | `AssetReference` | mcp/src/agents_remember/models/conversations/control_wire.py:154-162 |
| The submission authority's payload-digest construction this mirrors byte-for-byte. | `_payload_digest` | mcp/src/agents_remember/serving/harness_submission_authority.py:987-1008 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-03T03:56+02:00 — 260731-EFA-L6 W3-B10 curator: repaired 1 prose citation and 1 table citation; no unresolved Tier-3 claims.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that ran past
  the end of `mcp/src/agents_remember/kernel/primitives/tool_reports.py` (cited L1-L80; the file is 79 lines).
  Replaced the whole-file range with the two spans the claim actually rests on: `_SECRET_PATTERN`
  at L25-L27 and the recursive `redact_secrets` at L72-L79.

- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: created the sidecar for the deterministic
  preview/digest transforms — control-char strip, whitespace collapse, secret redaction, the 96
  grapheme-ish cluster bound that never splits a cluster, and the authority-parity payload digest.
  Verification is blank because the new source file is uncommitted; closeout owns its first source
  stamp.
