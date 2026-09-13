# mcp/tests/evidence-lifecycle.toml

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/evidence-lifecycle.toml` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash | `9c8a7a42a3d761b13c462874c7b312313a11c0ae` |
| lastVerifiedCommitDate | 2026-09-13T19:56:50+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Declares the current 42 shared-support/fixture artifacts and four executable replacement contracts. The catalog preserves authority, fidelity, lifetime and exact source-observed consumers for the reduced suite; deleted artifacts and their old consumer populations are no longer active declarations.

## Code Commentary

### Logic

Contract rows bind a production owner to a retained executable evidence node. Artifact rows state
category, authority, fidelity, cadence, provenance, permanence/expiry rationale, replacement
contract and consumers. The public validator checks observed consumers against declarations;
keeping a stale consumer merely because an older suite used it is not valid ownership.

The store harness now points to retained provider process-race evidence. Generic synthetic evidence
uses the retained dependency-ownership test as its replacement node. Shared profile/certification
support retains exact consumers without claiming that synthetic fixture bytes are installed-executor
proof. The closeout-input and curator-coherence support rows now declare the registered activation
admission fixture and the route-review transport fixture as exact consumers; the current validator
result is a registry consistency check, not execution or acceptance evidence. `large_fixture_bytes=25000`
controls discovery of unknown non-source suffixes; the catalog is a policy input excluded from its
own artifact population.

### Invariants And Boundaries

- Missing, stale, contradictory or consumer-incomplete declarations refuse.
- Fidelity and permanence are independent of evidence-lane labels.
- Exact source-observed ownership includes transitive consumers where declared; no old count is authoritative.
- The catalog remains a global pytest policy input; that is distinct from broadening an individual helper’s ownership.
- Removing unused scaffolding does not authorize unowned new evidence or a second fixture catalog.

## Docs References

No external Domain Documentation source is configured; these are repository-owned implementation facts.

## Repo-Internal References

The exact source declarations below establish the current behavior; this inventory is not execution evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Catalog schema and large-fixture discovery threshold | `schema_version` | mcp/tests/evidence-lifecycle.toml:1-2 |
| Durable-store replacement contract declares its exact process-race evidence node. | "mcp/tests/test_provider_store_durability.py::ProviderStoreDurabilityTests::test_no_record_is_lost_when_an_append_races_a_compaction" | mcp/tests/evidence-lifecycle.toml:4-7 |
| Actual process-race support and two consumers | "mcp/tests/_store_durability.py" | mcp/tests/evidence-lifecycle.toml:44-61 |
| Retained registry fixture ownership and current consumer declarations | "mcp/tests/certification_registry_test_support.py" | mcp/tests/evidence-lifecycle.toml:493-510 |
| Profile support and current consumer declarations | "repository-certification-profile-test-port" | mcp/tests/evidence-lifecycle.toml:512-548 |
| Closeout-input support declares the activation/admission and route-review registered consumers. | "mcp/tests/closeout_input_test_support.py" | mcp/tests/evidence-lifecycle.toml:283-283 |
| Curator-coherence support declares the activation/admission and route-review registered consumers. | "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:338-338 |
| The enclosure/worktree fixture composition the L32 suite imports; the artifact's `path` cell is the unique anchor because the bare quoted path also appears in consumer lists. | "path = \"mcp/tests/lifecycle_enclosure_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:448-448 |
| The L32 suite is a registered consumer in both shared-support artifacts. | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:282-336; mcp/tests/evidence-lifecycle.toml:338-392 |
| The L34 boundary suite is a registered consumer in both shared-support artifacts. | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:282-336; mcp/tests/evidence-lifecycle.toml:338-392 |
| The L37 pause boundary suite is a registered consumer in both shared-support artifacts (its consumer entries are at `:319` and `:375`); the leaf's AST-only architecture guard consumes neither. | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:282-336; mcp/tests/evidence-lifecycle.toml:338-392 |
| The seal-removal change set's ordered playthrough is a registered consumer in both shared-support artifacts (its consumer entries are at `:316` and `:372`), reached transitively through the same `QueueFixture` composition. | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:316-316; mcp/tests/evidence-lifecycle.toml:372-372 |

## Cross-Repo References

No separate cross-repository authority is established by this file.

## CCR-L42 current candidate

The evidence registry now records the atomic-master review public and scope tests as exact consumers of existing shared support artifacts; the additions refine ownership accounting and do not claim test execution or certification.

## 260831-LOCR-L32 Three Consumer Rows

The leaf's new `mcp/tests/test_worktree_status_terminal_next_tool.py` was added as an exact
consumer of three existing shared-support artifacts — no artifact row was added, removed or
re-categorised, so the catalog's population is unchanged:

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:330` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:383` |
| `mcp/tests/lifecycle_enclosure_test_support.py` | `publish_test_enclosure` — the suite's terminal-archive fixture is a real published enclosure | `mcp/tests/evidence-lifecycle.toml:461` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.

## 260831-LOCR-L34 Two More Consumer Rows

The leaf's new `mcp/tests/test_checkpoint_landing_end_to_end.py` was added as an exact consumer of the
same two shared-support artifacts the L32 suite consumes, again through `QueueFixture`'s transitive
composition. No artifact row was added, removed or re-categorised, so the declared population is
unchanged; the insertion did shift the later consumer rows, which are re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:304` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:357` |

Consumer declarations are ownership accounting only; they are not execution or acceptance evidence.
The three L32 rows moved with the insertion (`closeout_input_test_support.py` 329 → 330,
`curator_coherence_test_support.py` 381 → 383, the `lifecycle_enclosure_test_support.py` artifact row
442 → 444 with the L32 suite's consumer entry at 457 → 461) and this card's references now name the
current lines.

## 260831-LOCR-L37 Two More Consumer Rows

The leaf's new `mcp/tests/test_pause_stop_only_end_to_end.py` was added as an exact consumer of the
same two shared-support artifacts every other `QueueFixture`-based boundary suite consumes, reached
transitively through that fixture's composition. No artifact row was added, removed or re-categorised,
so the declared population is unchanged; the insertion did shift the later consumer rows, which are
re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:318` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:373` |

The leaf's other new module, `mcp/tests/test_pause_is_not_publication.py`, is deliberately **not** a
consumer of any artifact here: it parses the source tree with `ast` and resolves module paths, so it
composes no fixture and installs no support. Consumer declarations are ownership accounting only; they
are not execution or acceptance evidence.

The L36 rows moved with the insertions (`closeout_input_test_support.py` artifact row resolves at
`:283` unchanged, `curator_coherence_test_support.py` at `:339`, the
`lifecycle_enclosure_test_support.py` artifact row at `:450` with the L32 suite's consumer entry at
`:465`), and this card's references now name the current lines.

## 260831-LOCR Seal Removal — Two More Consumer Rows

The change set's new `mcp/tests/test_lifecycle_playthrough_end_to_end.py` was added as an exact
consumer of the same two shared-support artifacts every other `QueueFixture`-based boundary suite
consumes, reached transitively through that fixture's composition. No artifact row was added, removed
or re-categorised, so the declared population is unchanged; the insertion did shift the later consumer
rows, which are re-derived below.

| Artifact | Why the suite consumes it | Consumer row |
| --- | --- | --- |
| `mcp/tests/closeout_input_test_support.py` | transitive typed closeout-input/repository-authority composition the worktree-service fixture relies on | `mcp/tests/evidence-lifecycle.toml:316` |
| `mcp/tests/curator_coherence_test_support.py` | transitive typed task-topology/attestation fixture composition, same route | `mcp/tests/evidence-lifecycle.toml:372` |

The L37 rows moved with the insertion (`closeout_input_test_support.py` artifact row resolves at `:283`
unchanged with the pause suite's consumer entry at `:318` → `:319`, `curator_coherence_test_support.py`
at `:338` → `:339` with the pause entry at `:373` → `:374`, the
`lifecycle_enclosure_test_support.py` artifact row at `:449` → `:450` with the L32 suite's consumer
entry at `:464` → `:465`), and this card's references now name the current lines. Consumer
declarations are ownership accounting only; they are not execution or acceptance evidence.

## Update History
- 2026-09-13T20:42+02:00 — Child-admission seal removal (uncommitted change set on
  `ar/260831_lifecycle-owned-completion-relay`): registered the new
  `mcp/tests/test_lifecycle_playthrough_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 316) and `curator_coherence_test_support.py` (row 372), both
  reached transitively through `QueueFixture`. No artifact row was added or re-categorised, so the
  declared population is unchanged; re-derived every shifted consumer row this card cites (the pause
  suite's entries 318 → 319 and 373 → 374, `curator_coherence_test_support.py` path 338 → 339,
  `lifecycle_enclosure_test_support.py` path 449 → 450 with the L32 entry 464 → 465) and corrected the
  three shared artifact-block ranges in the reference table to `282-336` and `338-392`. Verification
  metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-13T19:02+02:00 — 260831-LOCR-L37: registered the new boundary suite
  `mcp/tests/test_pause_stop_only_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 318) and `curator_coherence_test_support.py` (row 373), reached
  transitively through `QueueFixture`, and recorded that the leaf's other new module
  (`test_pause_is_not_publication.py`) consumes no artifact because it is AST-only. No artifact row was
  added or re-categorised, so the declared population is unchanged; re-derived the shifted consumer
  rows (`curator_coherence_test_support.py` 338, `lifecycle_enclosure_test_support.py` 448, L32 entry
  463). Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-13T18:09+02:00 — 260831-LOCR-L36: rebound two citation ranges shifted by this leaf's two
  additions to the manifest (`mcp/tests/test_cross_master_concurrency.py` in both consumer lists): the
  curator-coherence support artifact resolves at `:337` and the enclosure/worktree fixture's `path`
  cell at `:446`. Ranges only; the artifact and consumer claims are unchanged and no verification
  stamp advanced.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-13T09:12+00:00 — 260831-LOCR-L34 curator: recorded
  `mcp/tests/test_checkpoint_landing_end_to_end.py` as an exact consumer of
  `closeout_input_test_support.py` (row 304) and `curator_coherence_test_support.py` (row 357), both
  reached transitively through `QueueFixture`. No artifact row was added or re-categorised, so the
  declared population is unchanged; the insertion shifted three later consumer rows, which are
  re-derived and re-cited here (330, 383, 459). Verification metadata remains closeout-owned; no
  acceptance claim.
- 2026-09-13T08:49:05+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:336-336. No content impact: mechanical anchor-range projection bound to citation source snapshot 498749c8248ef2a3c982edf27ca50b4962c9d2c9f9bdc470553967a3be375341; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: recorded the new
  `mcp/tests/test_worktree_status_terminal_next_tool.py` as an exact consumer of three existing
  shared-support artifacts (`closeout_input_test_support.py` at row 329,
  `curator_coherence_test_support.py` at row 381, and `lifecycle_enclosure_test_support.py` at row 457,
  the last because the suite publishes a real enclosure through `publish_test_enclosure`). No artifact
  row was added or re-categorised, so the declared population is unchanged; added three reference rows
  and a section naming each artifact's reason for the edge. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:335-335. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "mcp/tests/closeout_input_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:283-283. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "mcp/tests/curator_coherence_test_support.py" repointed to mcp/tests/evidence-lifecycle.toml:334-334. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T00:20:36+02:00 — CCR-L42 current candidate reconciliation: The evidence registry now records the atomic-master review public and scope tests as exact consumers of existing shared support artifacts; the additions refine ownership accounting and do not claim test execution or certification.

- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ02 preparation recorded the exact two R25/R26 consumers added to both shared support rows. Registry SHA `15bea1c01f402c382dad1667dec601313bb8aabfc511bb8cedac66076287606a1` and validator PASS42 are preserved as source/diagnostic evidence only; the source is uncommitted and no acceptance claim is made.
- 2026-09-06T21:51:32+00:00 — Reconciled the retained IAS implementation and diagnostic testing policy with current source citations; prior verification provenance is retained and no new test or review result is claimed.

- 2026-09-06T00:23:26+00:00 — L30 recovery: Reverified retained source or route ownership against actual candidate commit 97e8ed2e1fae21756c3ad995c30613d4fbfcc503; replaced the superseded private-candidate stamp.

- 2026-09-06T00:17+02:00 — Registered the extracted gate fixture and publication-suite consumers in durable memory; reconciled exact-source runner ownership with the distinct pytest closure.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for
  6f10c24d72db6171c0d434b307e6806996e2f11d (CCR-R21@v2/L21): recorded the L21 registration of
  `test_gate_certificate_authority.py` as an exact consumer of the shared certification and
  closeout-input support rows whose builders its forcing suite imports. Verification is pinned
  to the owning commit.

- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 expanded the certification shared-support row to
  the complete five-consumer set exposed by the source graph. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Registered the portable certification composition owner with its two
  exact focused-suite consumers. Verification remains closeout-owned.

- 2026-08-31T12:39+02:00 — Added `test_dispatch_agent_ambient_reviewer.py` to both exact transitive
  consumer sets after the L5 closeout fast hook identified the previously undeclared ownership
  edges.

- 2026-08-30T16:32+02:00 — Added `test_public_surface_conformance.py` to both exact transitive
  consumer sets after the L4 staged fast hook exposed the source-derived ownership edges; the
  focused lifecycle validator passes with 35 governed artifacts.

- 2026-08-29T23:04+02:00 — Added `test_memory_candidate_pair.py` to the exact source-derived
  consumer sets for the closeout-input and curator-coherence test composition roots after the
  A002 lifecycle fast hook exposed both missing edges.

- 2026-08-29T12:27+02:00 — Reconciled the curator-coherence helper's declared consumers with the
  source-derived transitive ownership graph after generation 7 rejected the direct-import-only
  catalog row. Verification remains closeout-owned.

- 2026-08-29T12:10+02:00 — Registered the shared curator-coherence fixture-input owner and its
  three exact importers after the generation-6 fast hook rejected the uncatalogued helper.
  Verification remains closeout-owned.

- 2026-08-29T09:58+02:00 — Added the curator-coherence suite to the exact source-derived consumer
  set for the shared closeout-input test support after the targeted closeout gate exposed the
  missing edge.
- 2026-08-28T05:10+02:00 — Recorded the operational unknown-suffix threshold and the lifecycle
  catalog's explicit policy-input/non-artifact boundary after Q5 v19 forced the self-reference case.
- 2026-08-27T13:32+02:00 — Registered the split Ruff support and its exact consumers. Verification
  remains closeout-owned.
