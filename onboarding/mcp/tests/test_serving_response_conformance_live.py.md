# mcp/tests/test_serving_response_conformance_live.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_serving_response_conformance_live.py`                                            |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-09-04T01:06+02:00 |
| lastVerifiedCommitHash | `1993dd25bdf8331a2c1e28171dff2bf92ea090e2` |
| lastVerifiedCommitDate | 2026-09-04T00:57:29+02:00 |
| governingOverview      | `overview.md`                                          |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Part of the 260731-EFA-L7 in-place split family for `test_serving_response_conformance_live.py`'s source module; covers the behaviours named by its test classes.

## Code Commentary

- `ConversationSuccessConformanceTests`
- `ConversationCompositionRefusalTests`
- `StreamContractTests`
- `_grouped`
- `_driven_pairs`
- `DeclaredSurfaceCoverageTests`

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/tests/test_serving_response_conformance_live.py`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |


## 260831-CCR-L23 Declared-Surface Ledger

L23 advanced the live declared-surface ledger for the two new requirement routes:
292 declared pairs (was 286), 139 driven against a real body (was 133), 153
declared-and-undriven with a reason each, and the weaker claim now reads "every one of
the 63 routes is driven on at least one status" (was 61).

## 260821-CLIVE-L2 Live Readiness Reuse

The live stream contract reuses the same bounded projector-readiness helper before deriving the
ETag for its conditional request. This is an explicit startup boundary, not a silent fallback or a
relaxation of response conformance.

| Finding | Anchor | Source |
| --- | --- | --- |
| The live ETag test requires a ready 200 response before asserting the cached 304. | `test_the_304_branch_declares_a_body_less_response` | mcp/tests/test_serving_response_conformance_live.py:379-390 |

## PDLS Wave 005 Current Delta

The success-conformance case now injects an explicit native `HarnessControlError` before asserting
the declared 422 body. The shared fake no longer recreates lower-level refusal behavior, so this
test owns the scenario while production remains the sole refusal translator.

| Finding | Anchor | Source |
| --- | --- | --- |
| The declared 422 operation body is driven by an explicit native refusal at the scenario boundary. | `ConversationSuccessConformanceTests` | mcp/tests/test_serving_response_conformance_live.py:50-300 |

## Update History

- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 memory pass: recorded the declared/driven ledger advance (292/139, 63 routes) for the requirement endpoints in the live surface-coverage suite.

- 2026-08-28T06:40+02:00 — Replaced fake-owned implicit refusal behavior with explicit
  scenario-local native-error injection for the 422 conformance case.
- 2026-08-24T00:51+02:00 — 260821-CLIVE-L2: reconciled the L2 test boundary represented by the changed source. Verified at code commit `1d446724`.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
