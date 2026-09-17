# mcp/tests/test_dependency_ownership_ast_helpers.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_dependency_ownership_ast_helpers.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `c22beb0121946c0637e113ec4cf29da29fd4aec7` |
| lastVerifiedCommitDate | 2026-09-17T03:29:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
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
is a **hard failure** rather than a silent inventory drift. `260915-KS-L8` moved all three in the same change as
the catalog edit: **11 contracts, 52 artifacts, digest
`4cf81f10dbbd6b941c50887dca45154612e5e46b7135465823af3e6604db3747`** (from `4 / 45 / 293a187f…`, through the
`KS-L1`–`KS-L8` registrations, and from L7's `10 / 51 / 461121ca…`). The comment above the constants says what
the pin is for and names the digest it supersedes; **a future catalog change must re-pin deliberately, in the
same change**, and the counts must move with the blocks they count. The pin's own verification is the module's
`_assert_the_catalog_kept_its_bytes_and_identities`, which recomputes the file's sha256 and counts both block
kinds before comparing them to the three constants.

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
| Repository inputs reach their supported consumers. | `test_repository_inputs_reach_their_supported_consumers` | mcp/tests/test_dependency_ownership_ast_helpers.py:72-91 |
| **The evidence catalog's pinned shape and bytes, and the deliberate re-pin this leaf made in the same change as its catalog rows.** | `LIFECYCLE_CONTRACT_COUNT`; `LIFECYCLE_ARTIFACT_COUNT`; `LIFECYCLE_CATALOG_SHA256` | mcp/tests/test_dependency_ownership_ast_helpers.py:43-65 |
| **The check that makes the pin real: the file's bytes recomputed and both block kinds counted before either is compared.** | `_assert_the_catalog_kept_its_bytes_and_identities` | mcp/tests/test_dependency_ownership_ast_helpers.py:162-178 |
| The closure check over the governed inventory, and the lane-membership check. | `_assert_the_governed_inventory_is_closed`; `_assert_the_proof_is_selected_by_the_lane_manifest` | mcp/tests/test_dependency_ownership_ast_helpers.py:142-159; mcp/tests/test_dependency_ownership_ast_helpers.py:129-139 |
| **The contract and artifact blocks the pin counts, added by this leaf, and the consumer list its sibling artifact gained.** | "knowledge-diff-cases" | mcp/tests/evidence-lifecycle.toml:1199-1199; mcp/tests/evidence-lifecycle.toml:1209-1209; mcp/tests/evidence-lifecycle.toml:1220-1220; mcp/tests/evidence-lifecycle.toml:1242-1242 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): recorded the **second deliberate re-pin of the evidence-catalog identity** and re-derived the card's citations against the new bytes — `LIFECYCLE_CONTRACT_COUNT` 10 → **11**, `LIFECYCLE_ARTIFACT_COUNT` 51 → **52**, and `LIFECYCLE_CATALOG_SHA256` `461121ca…` → **`4cf81f10dbbd6b941c50887dca45154612e5e46b7135465823af3e6604db3747`** (measured on the frozen candidate by counting the blocks and hashing the file). The card now names the check that makes the pin real — `_assert_the_catalog_kept_its_bytes_and_identities`, which recomputes the file's digest and counts both block kinds before comparing them to the constants — and records that this leaf's catalog change is a **new contract/artifact pair** (`knowledge-diff-cases` for `mcp/tests/diff_scope_test_support.py`) **plus** two consumer rows added to the existing read-scope artifact. It also keeps the rule the L7 entry stated, in the form a successor needs: **a catalog change must re-pin deliberately in the same change, with the counts moving with the blocks they count.** Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
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
