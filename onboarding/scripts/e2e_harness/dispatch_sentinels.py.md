# dispatch_sentinels.py

| Field | Value |
|---|---|
| repository | agents-remember |
| path | `scripts/e2e_harness/dispatch_sentinels.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T22:29:54+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate |  2026-08-31T15:32:32+02:00|
| governingOverview | `scripts/e2e_harness/overview.md` |

## Governing Overview

[Ambient Role-Chat E2E Harness](overview.md)

## Purpose

Builds controlled malformed variants from the dispatch advertisement observed by real Codex and
proves each variant is rejected by the canonical product validator at its expected boundary.

## Code Commentary

### Logic

`dispatch_rejection_sentinels` accepts the live tool identity, description, and input schema. It
deep-copies the schema before removing `brief`, separately removes the required `ambient`
caller-boundary term, and sends both variants through `validate_dispatch_advertisement`. A sentinel
passes only when `PublicSurfaceViolation` carries the expected diagnostic; acceptance or rejection
at another boundary fails the scenario.

### Conventions

Sentinel names are stable evidence identities. The returned record names expected failure, actual
failure, and the canonical validator as owner; it does not claim that malformed input was a real
Codex advertisement.

### Invariants And Boundaries

- The unmodified live advertisement is validated by `responses_server.py` before these mutations.
- Input schemas are copied before mutation; no live request object is modified.
- Every sentinel must fail at the exact canonical product boundary and expected reason.
- No local schema vocabulary or compatibility validator is maintained here.

### Todos

None.

## Docs References

No Domain Documentation source is configured. The observed real-Codex advertisement and canonical
repository validator are the authorities.

| Finding | Anchor | Source |
| --- | --- | --- |
| The sentinel corpus is derived from the exact live description and schema. | `dispatch_rejection_sentinels` | scripts/e2e_harness/dispatch_sentinels.py:23-48 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Each malformed candidate must fail through the canonical validator with its expected diagnostic. | `_prove_rejection` | scripts/e2e_harness/dispatch_sentinels.py:60-95 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module imports the candidate repository's canonical validator directly. | "from agents_remember.mcp.public_surface import (" | scripts/e2e_harness/dispatch_sentinels.py:9-12 |

## Update History

- 2026-08-30T22:29:54+02:00 — 260821-ARSPAWN-L5 replaced repeated imported-name
  anchors with the unique proving symbol and exact import literal.

- 2026-08-30T22:20:19+02:00 — 260821-ARSPAWN-L5 converted source references to the
  canonical anchored citation format. Verification metadata remains closeout-owned.

- 2026-08-30T22:11:35+02:00 — 260821-ARSPAWN-L5 created onboarding for canonical
  negative-advertisement proofs. Verification metadata remains closeout-owned.
