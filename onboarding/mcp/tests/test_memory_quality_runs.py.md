# mcp/tests/test_memory_quality_runs.py

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
this card records — most recently the one named in the recorded working candidate above. Historical
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
resolves to nothing,
(since MIK-R08 the census is handed over as `prepared=controller._PreparedInputs(census=...)`, the bundle
that also carries the leaf's worklist, left `None` here), and asserts the finding arrives in the checklist the curator's completion loop
gates on — the row is filtered to the
`integrity.governing_overview_resolution` check, its code is asserted to be exactly
`["governing-overview-link-unresolved"]`, and the published `unresolvedLinkCount` is asserted
alongside it. The module's own docstring states why the count assertion is the weaker of the two: a
count cannot show that both declaration forms were reported, so the corpus-side case beside it asserts
the identity of the finding set instead.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

No configured domain evidence applies to the file-local claims above.

### Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

- Start poll completed failed and unknown. [1]
- Launch failure rolls back the admitted slot. [2]
- Wrong repository poll never discloses any run state. [3]
- Pair change during derived evidence refuses before curator publication. [4]
- The dead-governing-overview case hands the census to `_attach_curator_checklist` through the prepared-inputs bundle. [5]

### Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

Fixture repositories and protocol doubles do not establish a live external integration.

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
