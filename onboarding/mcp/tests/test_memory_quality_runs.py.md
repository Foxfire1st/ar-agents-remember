# mcp/tests/test_memory_quality_runs.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_quality_runs.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-09-18T19:30+02:00 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312` |
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Bounded memory-quality run state and pair-currentness refusal.

## Code Commentary

### Logic

Registry cases retain completed/failed outcomes, unknown-run absence, launch rollback and repository-scoped polling privacy. A controller case changes the code/memory pair while deriving evidence and requires scope-refused with no curator publication.

`260915-KS-L23` added two classes at the end of the module, stated in the section below:
`MeasuringBuildStampTests` (`:626-696`) and `CloseoutOwnedProvenanceRoutingTests` (`:699-731`).

### Conventions

This card's body describes the source as it stood at IAS `d3610903` **plus** the later working candidates
this card records — most recently the one named in the `reviewedWorkingCandidate` row above. Historical
entries below record earlier test populations; they do not require restoring removed cases. Source
inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

A scan result cannot publish against a moved pair. Registry state is operational polling data, not a semantic acceptance certificate.

### Todos

No file-local implementation change is requested by this reconciliation.

### 260915-CAPS-L20 The Wiring Half Is The Defect

`test_a_dead_governing_overview_reaches_the_gated_repair_set` pins the half of `D3`/`D16` that a
checker test cannot: a correct checker whose findings never reach `repair_findings` still produces a
clean `curatorActionableCount`, which is exactly how 41 dead declarations passed every gate.

It drives `_attach_curator_checklist` with a real onboarding tree holding one card whose body link
resolves to nothing, and asserts the finding arrives in the checklist the curator's completion loop
gates on — the row is filtered to the
`integrity.governing_overview_resolution` check, its code is asserted to be exactly
`["governing-overview-link-unresolved"]`, and the published `unresolvedLinkCount` is asserted
alongside it. The module's own docstring states why the count assertion is the weaker of the two: a
count cannot show that both declaration forms were reported, so the corpus-side case beside it asserts
the identity of the finding set instead.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Start poll completed failed and unknown. | `test_start_poll_completed_failed_and_unknown` | mcp/tests/test_memory_quality_runs.py:131-146 |
| Launch failure rolls back the admitted slot. | `test_launch_failure_rolls_back_the_admitted_slot` | mcp/tests/test_memory_quality_runs.py:155-161 |
| Wrong repository poll never discloses any run state. | `test_wrong_repository_poll_never_discloses_any_run_state` | mcp/tests/test_memory_quality_runs.py:156-168 |
| Pair change during derived evidence refuses before curator publication. | `test_pair_change_during_derived_evidence_refuses_before_curator_publication` | mcp/tests/test_memory_quality_runs.py:205-261 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## KS-R23@v1 The Ruler Stamp, And The Closeout-Owned Bucket's Wire

Two classes were added to the end of the module; this card previously described neither.

`MeasuringBuildStampTests` (`:626-696`) carries item 26 (D-33) with three cases:

- `test_every_memory_quality_entry_point_stamps_the_serving_build` (`:636-659`) — drives all three public
  entry points with their bodies patched out and asserts each returns the **process's resolved** commit
  and source digest. Red if a wrapper is dropped, if a mode returns its body's payload unwrapped, or if
  the stamp stops being the resolved identity: an unstamped envelope is exactly the state D-33 recorded,
  where a count cannot be attributed to a ruler.
- `test_the_stamp_is_declared_on_the_responses_that_carry_it` (`:661-674`) — the field is in
  `MemoryQualityCheckResponse.model_fields`, and the stamp validates as the shared `ServingBuildPayload`.
  Red if the declaration is removed, because `FlexibleToolResponse` sets `extra="allow"`, so an
  undeclared key would validate while staying invisible in the tool's own schema.
- `test_the_citation_repair_response_names_its_ruler` (`:676-696`) — drives `citation_fix_tool` with its
  scope, its `_citation_trees` and the fixer doubled, and asserts the returned `servingBuild` is the
  resolved one. Red if the tool's return stops including the stamp.

`CloseoutOwnedProvenanceRoutingTests` (`:699-731`) carries item 17 half (b). Its single case,
`test_the_checklists_commit_owned_set_collects_the_checks_own_bucket` (`:719-731`), drives the real
`controller._checklist_finding_sets` with a check result that declares a `closeoutOwnedFindings` row and
asserts the row lands in the closeout-owned half — and that an absent or non-mapping `checks` payload
yields empty sets rather than raising. Red if the collection stops reading the bucket: those rows would
then be in neither the repairable set nor the closeout-owned section, which is the silence the
disposition rules forbid.

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_launch_failure_rolls_back_the_admitted_slot` repointed to mcp/tests/test_memory_quality_runs.py:155-161. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:30+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **recorded the two classes this leaf added, which this card did not mention.** `MeasuringBuildStampTests` (`:626-696`) is item 26 (D-33): all three memory-quality entry points return the process's resolved `servingBuild`, the field is declared on `MemoryQualityCheckResponse` rather than tolerated by the flexible envelope, and `citation_fix_tool`'s response names its ruler too. `CloseoutOwnedProvenanceRoutingTests` (`:699-731`) is item 17 half (b): `controller._checklist_finding_sets` collects a check's own `closeoutOwnedFindings` bucket into the closeout-owned set, and empty sets are returned for an absent or non-mapping `checks` payload. The `### Logic` and `### Conventions` sections now say the body covers this leaf's working candidate, and the stale `reviewedWorkingCandidate` row (`ar/260915-caps-l20-ar`) names this leaf's. Read against the delivered but **uncommitted** working tree, so the verification stamp is not advanced: no commit carries these bytes and closeout owns the real code commit; the reference rows are left to the citation-range repair pass that owns them.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: recorded this leaf's added case — the wiring that carries a dead governing-overview finding into the gated curator repair set, with the finding's code and the published `unresolvedLinkCount` asserted together. The module counted 11 cases before this leaf and 12 after. Verification metadata advanced to this leaf's frozen code base.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `test_start_poll_completed_failed_and_unknown` repointed to mcp/tests/test_memory_quality_runs.py:131-146. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `test_launch_failure_rolls_back_the_admitted_slot` repointed to mcp/tests/test_memory_quality_runs.py:148-154. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `test_wrong_repository_poll_never_discloses_any_run_state` repointed to mcp/tests/test_memory_quality_runs.py:156-168. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `test_pair_change_during_derived_evidence_refuses_before_curator_publication` repointed to mcp/tests/test_memory_quality_runs.py:205-261. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card purpose, logic, invariants, and cited route against the frozen candidate source; no content or route change was required, and the existing claim bytes remain accurate. source-sha256=d4111c853b47eda1fe5a6c3ff364e5de2b402c2e2f053ce0bd6c171bce159954; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-09-04T01:48+02:00 — 260831-CCR-L08 Gate-5 memory pass: re-anchored the controller-under-test row (48-144 to exact spans) shifted by the CCR-R08 +57-line controller insertion. Citation-only re-anchor; no content impact.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the candidate-tree capture mock in the curator-publication controller case; prior registry, capacity, and pair-forcing prose preserved.

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: expanded total controller proof for async
  pair refusal, stale candidate polling, official running/failed polling, final publication
  identity, and pair revalidation. The derived-evidence race now mocks its unrelated Git-owned
  classifier so it reaches the intended third revalidation seam.

- 2026-08-29T21:46+02:00 — MCAR-L03: added exact-pair async start/poll/race/refusal coverage.
  Dagger verification remains closeout-owned.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the memory-quality controller/run package extraction; concurrency, saturation, polling, and result-identity behavior are unchanged.
- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: rebuilt the focused registry/controller tests around typed identity, hard live capacity, terminal-only pruning, and nondisclosing poll ownership. Verification metadata remains pinned until architect-owned closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: added the never-settles registry
  regression and made the wrapper start/poll case deterministically observe the running envelope
  before completion. Verified at code commit e5cb139f.

- 2026-08-20T21:30+02:00 — Created for 260815-DAG-L15-R7: the run-registry forcing suite
  (start/poll/completed/failed/single-flight/boundedness/TTL eviction) plus the application-wrapper
  tests covering the started/run-not-found/running/failed envelope branches and the key-scoping
  branches (extended in the gate-repair rounds). Verified at code commit de3a0fd9.