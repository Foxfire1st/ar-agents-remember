# mcp/tests/test_retired_door_publication_fields.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_retired_door_publication_fields.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Tests the existing narrow read rule for persisted door-publication evidence that contains three
retired contract-byte digest fields, while keeping other unknown fields invalid.

## Code Commentary

### Logic

`_door_generation` builds the current typed fixture without ledger provenance. The legacy-payload
helper adds exactly the retired before/published/observed contract digest names. The model case
checks that these names are accepted on read and absent when reserialized, while an unrelated
`unexpectedField` still fails with `extra_forbidden`.

The persisted-record case creates a disposable closed external-memory leaf, injects those fields
into its stored publication, and reads through the strict operation store. It then invokes the
terminal-archive boundary and checks that the canonical operation record appears in the proven
archive. This tests the specific historical field migration already owned by the model; it does
not introduce a general compatibility reader or ledger-cache fallback.

### Conventions

The fixture's current generation omits retired ledger provenance, but the intentional three-field
historical payload remains. All record/archive writes are within temporary test repositories and
coordination roots.

### Invariants And Boundaries

- Only the explicitly retired contract-byte names are tolerated by this case.
- Unknown unrelated fields remain rejected.
- Current generation construction has no ledger-provenance input.
- Successful fixture archive proof is not evidence of live cleanup or permission to bypass its boundary.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The current generation and explicit retired digest names define the test input. | n/a | [mcp/tests/test_retired_door_publication_fields.py](mcp/tests/test_retired_door_publication_fields.py) |
| The model read drops only the named retired fields and still rejects unknown fields. | n/a | [mcp/tests/test_retired_door_publication_fields.py](mcp/tests/test_retired_door_publication_fields.py) |
| Store and terminal-archive reads exercise the persisted legacy record. | n/a | [mcp/tests/test_retired_door_publication_fields.py](mcp/tests/test_retired_door_publication_fields.py) |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History

- 2026-09-15T01:02 UTC — Created the missing paired sidecar for the retained retired-field tests; documented the narrow existing read rule, current generation fixture without ledger provenance, and real temporary store/archive coverage. Working candidate verified by source inspection; commit metadata records real committed history only.
