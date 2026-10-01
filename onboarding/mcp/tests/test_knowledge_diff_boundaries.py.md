# mcp/tests/test_knowledge_diff_boundaries.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

**The comparison's integration population: fifteen cases over a real committed Git pair, a real
curated candidate database and the real application seam**, marked `pytestmark = pytest.mark.integration`
and registered in the **integration** lane at `mcp/tests/test-evidence-lanes.toml:159`. It is the largest
new test module of the leaf at **840 lines** and still under the 1 200-line rail.

The module owns the parts of the contract a hermetic unit case cannot honestly measure: what two **real**
code trees differ at, what a **real** write to the candidate does to a continuation, and what the
**serialized** response can and cannot carry.

## Code Commentary

### Logic

`request_for(fixture, …)` builds the typed request per case and `run_diff` drives
`application.knowledge_diff.diff_knowledge_scope`, so the cases exercise the seam a caller uses. Three
cases drive the **production Git probe** rather than a substituted one, which is why the module is in the
integration lane.

**What each group of cases protects:**

| Group | Nodes | The property |
| --- | --- | --- |
| the expansion and the visible gap | `:145`, `:185` | Both requested tree ids and both roots; the reproducing command carrying the two tree ids and no `HEAD`; the four changed paths classified exactly once across the attributed/unattributed lists; and the unattributed path listed, counted with its reason and surviving a display filter |
| attributed source on the side that claims it | `:221` | A moved obligation's source is observed against **its own** side's tree — the candidate's new claim at `exact_recorded_blob`, the baseline's removed claim from the baseline |
| paging and the display budget | `:257`, `:708` | A small budget pages the comparison without shrinking its totals, and a page of a selection is what the comparison **displays**, not what it **selected** — R07's byte-budget page is not reused as the comparison's scope |
| refusal without substitution | `:303`, `:325`, `:408`, `:438` | A missing side refuses and substitutes no other snapshot; a real write to the candidate moves its logical digest and refuses the continuation with `continuation_binding_mismatch` and `detail` ending *"it binds another snapshot pair"*; a continuation presented against another selector refuses and returns **no page**; and a side naming another snapshot of its own file is refused by the per-side digest verification **before any page** |
| the response's honesty | `:481`, `:510`, `:543` | Nine verdict words searched over the whole **serialized** response with a positive control; the two change statements as separate fields where neither implies the other; and the record comparison reporting exactly the payload field that changed |
| the expansion's honesty | `:752`, `:774`, `:817` | No mounted UI and no approval the comparison cannot make; an unavailable observation reported as unavailable and **never** as a change set; and a probe that measured the trees being what makes a gap visible |

**The verdict-word case is the packet's *Forbidden Overreach* measured rather than asserted.** It searches
the serialized response's **field names and values** for nine verdict words and includes a positive
control, so the absence it proves is an absence in the payload a client actually receives — not merely in
the model's declared attributes.

**The three local helpers are deliberate.** `_substitute`/`_substituting` rewrite one field of one
already-built request so a case measures the *comparison's* answer to a mutated input rather than a
different request; `selected_scopes`/`_rewording` build the two `SelectedScope`s and a reworded variant
directly from the fixture, for the case that compares at the storage layer rather than through the seam.


**This leaf added the real-Git half of the module: six cases over one fixture that builds a repository whose base commit and candidate tree carry every change class at once.** `InventoryFixture` and `build_inventory_fixture` write an edit, a deletion, an addition, a name containing a tab **and** a newline, a binary file, a moved symlink target, a mode-only change, a file→symlink type change and a submodule pointer change, and expose `.sides()` so a case hands the observation one pair rather than five hand-built ones. The cases assert the inventory against an **independent** `git diff --name-status -z` observation read through `mcp/tests/diff_scope_test_support.py::independent_changed_records` (a different Git question, so agreement is an observation about the two trees rather than a restatement of one implementation): population and per-path status equality; the tab/newline name surviving as the address it expands by, with the removed line-oriented command's output shown *not* to contain it; binary, symlink, submodule and mode-only entries each listed with their own kind and none dropped; a withheld tree reported `unavailable` with a reason and never as a measured empty set, with the identical-trees control reported `measured` with zero entries; and the non-UTF-8 boundary, where the observation stays available **and partial**, the path is carried by its byte form and the renderable remainder is still listed in full.

### Conventions

- The module asserts against `DiffFixture`'s named identities through `item_for`/`items_of`, never against
  a stream position.
- A real write used to stale a candidate goes through the **public store operations**
  (`add_unrelated_revision`), so the digest that moves is a digest the package produced.
- `run_diff` is re-declared here rather than imported from the scope module: the boundary module builds
  its own request per case, and the two modules are separate populations with separate lane rows.

### Invariants And Boundaries

- **Integration by behaviour, not by preference.** The module creates two real Git repositories under
  `tmp_path`, commits both trees, borrows one object store from the other, copies a closed database and
  curates it through the store, and drives the production Git probe — so its lane membership is its
  behaviour-preserving classification.
- **Nothing weakened.** No `skip`, `xfail`, `deselect`, per-file ignore or widened limit; fifteen cases,
  and the module is under the 1 200-line rail at 840.
- **The large-pyright residue is pre-existing and outside this module.** `pyright` reports **16
  `reportArgumentType` findings** on the **scope** module at `KnowledgeDiffResult(**base)` in its local
  `build(**overrides: object)` helper — byte-identical across the leaf's own fix rounds and outside the
  seven-module pyright scope the leaf published. It is carried to `KS-R09`/`L9` to confirm or disposition,
  and it is **not** a finding of this module.
- **Boundary.** This module measures the comparison through the seam and the production probe. It does not
  re-implement selection or display, and it asserts nothing about an outcome the seam cannot produce.

### Todos

None recorded. The leaf's carried documentation debt (four evidence items; ledger **A9**) concerns
`notes/reports/**` artifacts and not this module's cases: **every verdict of the corrected mutation
taxonomy reproduced on the frozen bytes** under the final verification round's own instrument (39
mutation applications, 126 scored node runs, 41 assertion kills, 1 exception death, 0 broken mutations,
0 refusals), and the residue was four line numbers and three strings in report text.

## Evidence

### Docs References

No Domain Documentation entries are configured in this memory root. The statements below are grounded in
repository source and package-local evidence only.

No configured domain documentation could be checked.

### Repo-Internal References

- The integration marker, the fixture, the request builder and the public-seam driver. [1]
- The two readers that let a case name a record rather than a position. [2]
- **The expansion naming both requested trees and every path they differ at, with the reproducing command and no `HEAD`.** [3]
- **The changed path no recorded realization attributes, listed as a visible gap that survives a filter.** [4]
- The moved obligation's source observed on the side that claims it. [5]
- **A small display budget paging the comparison without shrinking its totals.** [6]
- **A missing side refusing and substituting no other snapshot.** [7]
- **The real candidate write that moves the logical digest and refuses the continuation, and the helper that makes the write through the public store.** [8]
- **A continuation against another selector refusing and returning no page.** [9]
- **A side naming another snapshot of its own file refused before any page — the node the review's `R22` form kills.** [10]
- **The forbidden-overreach case: nine verdict words searched over the serialized response, with a positive control.** [11]
- **The two change statements kept apart, and the record comparison reporting exactly the field that changed.** [12]
- The input-substitution and scope-rewording helpers the last group of cases uses. [13]
- **A page of a selection being what the comparison displays and not what it selected.** [14]
- The two non-claims: no mounted UI and no approval, and an unavailable observation never reported as a change set — now with the partition asserted too (no total at all, empty third list, the undetermined limit declared and no counted omission). [15]
- **The probe that measured the trees being what makes a gap visible.** [16]
- The production probe these cases drive rather than substitute. [17]
- The fixture these cases run on, and the governed contract it is registered under. [18]
- **The integration-lane row this module occupies, and the read-scope artifact whose consumer list it joined.** [19]
- **The integration-lane row this module occupies, and the read-scope artifact whose consumer list it joined.** [20]
- The fixture these cases run on, and the governed contract it is registered under. [21]
- **The integration-lane row this module occupies, and the read-scope artifact whose consumer list it joined.** [22]
- **The integration-lane row this module occupies, and the read-scope artifact whose consumer list it joined.** [23]

### Cross-Repo References

The module commits two real temporary Git repositories and points one at the other's object store, all
under `tmp_path`. No configured remote, protected branch or sibling repository is touched.

No configured cross-repository evidence is claimed.
- The fixture these cases run on, and the governed contract it is registered under. [24]
- **The integration-lane row this module occupies, and the read-scope artifact whose consumer list it joined.** [25]
