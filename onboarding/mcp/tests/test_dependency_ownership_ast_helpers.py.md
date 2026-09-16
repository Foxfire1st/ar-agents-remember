# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `1ff1893f44d875073d58af863238501a6be35288` |
| lastVerifiedCommitDate | 2026-09-16T23:58:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Repository-input ownership discovery without broadening test selection.

## Code Commentary

### Logic

An explicitly supported input with no consumers remains complete with a verified no-consumer decision. Unknown input is incomplete. A declared consumer is selected without global invalidation and carries the declared-consumer reason.

**The module also carries the evidence catalog's pinned identity, and that pin is a deliberate one.** The three
constants `LIFECYCLE_CONTRACT_COUNT`, `LIFECYCLE_ARTIFACT_COUNT` and `LIFECYCLE_CATALOG_SHA256` state the
catalog's declared shape and its exact bytes, so a change to `mcp/tests/evidence-lifecycle.toml` that nobody meant
is a **hard failure** rather than a silent inventory drift. `260915-KS-L7` moved all three in the same change as
the catalog edit: **10 contracts, 51 artifacts, digest
`461121ca16567ab056938b710b19bddb98867581dd4fe3cf7ee2645111d54369`** (from `4 / 45 / 293a187f…`, through the
`KS-L1`–`KS-L7` registrations). The comment above the constants says what the pin is for and names the digest it
supersedes; **a future catalog change must re-pin deliberately, in the same change**, and the counts must move with
the blocks they count.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

No inferred full-suite population repairs an ownership gap. This retained test does not separately exercise every old pytest-plugin AST form.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Repository inputs reach their supported consumers. | `test_repository_inputs_reach_their_supported_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:74-94 |
| **The evidence catalog's pinned shape and bytes, and the deliberate re-pin this leaf made in the same change as its catalog row.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-68 |
| **The contract and artifact blocks the pin counts, added by this leaf.** | "contract:knowledge-read-scope-cases" | mcp/tests/evidence-lifecycle.toml:1198-1221 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): recorded the **evidence-catalog pin** this module carries and the deliberate re-pin this leaf made alongside its own catalog row — `LIFECYCLE_CONTRACT_COUNT` 4 → **10**, `LIFECYCLE_ARTIFACT_COUNT` 45 → **51**, and `LIFECYCLE_CATALOG_SHA256` `293a187f…` → **`461121ca16567ab056938b710b19bddb98867581dd4fe3cf7ee2645111d54369`**. The card states why the pin exists in the form a successor needs: any change to `mcp/tests/evidence-lifecycle.toml` that nobody meant becomes a hard failure, and **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count**. It also records that the pin's comment names the digest it supersedes, so the history of the freeze is auditable from the source rather than only from this card. Verification metadata remains empty until closeout stamps the code commit.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Recorded the exact sixteen-consumer runner regression and explicit no-global-invalidation assertions; repaired shifted layer-contract citation and reference buckets.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  db57101a9001ede8c681ff9de4eb0147d8b636bc (CCR-R19@v2/L19): recorded the L19 ownership-vocabulary
  change — `fresh_rerun_reason` assertions became `unresolved_inputs` assertions and incomplete
  ownership now resolves to an empty test population rather than a safe-full expansion.
  Verification is pinned to the owning commit.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added the exact `layers.toml` ownership forcing
  case and confirmed the composed declaration matches all five literal readers without safe-full
  selection. Verification remains closeout-owned.

- 2026-08-30T22:33:39+02:00 — 260821-ARSPAWN-L5 added the source-observed exact
  `.codex/config.toml` consumer proof; an unobserved declaration cannot claim complete ownership.

- 2026-08-28T06:28+02:00 — PDLS wave 005 curator: expanded the memory contract to recursive static
  pytest-plugin closure, dynamic-plugin fail-closed behavior, literal module consumers, and
  path-loaded owner reachability.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
