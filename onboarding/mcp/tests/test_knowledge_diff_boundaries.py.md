# mcp/tests/test_knowledge_diff_boundaries.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Pins the bounded comparison response, independent record/source changes and honest unavailable observations.

The sizes and catalog line addresses in the following original account are historical observations, not measurements of the present source tip.

**The comparison's integration population: fifteen cases over a real committed Git pair, a real
curated candidate database and the real application seam**, marked `pytestmark = pytest.mark.integration`
and registered in the **integration** lane at `mcp/tests/test-evidence-lanes.toml:159`. It is the largest
new test module of the leaf at **840 lines** and still under the 1 200-line rail.

The module owns the parts of the contract a hermetic unit case cannot honestly measure: what two **real**
code trees differ at, what a **real** write to the candidate does to a continuation, and what the
**serialized** response can and cannot carry.

## Code Commentary


The source declares fifteen test functions. They cover requested-tree expansion, visible unattributed gaps, side-specific realization evidence, display paging with whole-union totals, missing or changed snapshot/selector refusals, payload-field comparisons and separation of record changes from source observations. A read page is not reused as the comparison scope.

Serialized response checks exclude strengthening/harmlessness verdicts, mounted UI state, approval and severity. Paired unavailable/available probe substitutions distinguish an unmade observation from a measured gap. Index-shaped fixtures use test-only RowStore/revision helpers; payload substitution isolates the comparison projection and is not evidence of canonical writer duplicate_identity admission.

The continuation-mutation helper creates a new invariant with its single revision.
A text record cannot hold a second retained revision of one identity. The new record
moves the candidate snapshot bound by the cursor; the refusal remains
`continuation_binding_mismatch` with no partial page. The before/after counters
account for one new invariant and revision and require all other tables unchanged.

The old InventoryFixture/build_inventory_fixture six-case inventory population was removed. No current inventory-walk coverage or production store authoring is attributed to it.

### Logic

`request_for(fixture, …)` builds the typed request per case and `run_diff` drives
`application.knowledge_diff.diff_knowledge_scope`, so the cases exercise the seam a caller uses.
`run_diff` (`:116`–`:129`) supplies no probe override, and the application selects
`git_tree_difference_probe` by default. Source inspection identifies twelve test functions
using that driver, ten with positive-page assertions; two additional functions substitute
the probe explicitly and one compares selected scopes directly. This is default-route
and assertion census, not a new reached-probe execution count. Real Git-pair fixtures
and default production observation support the integration classification.

**What each group of cases protects:**

| Group | Nodes | The property |
| --- | --- | --- |
| the expansion and the visible gap | `:152`, `:198` | Both requested tree ids and both roots; the reproducing command carrying the two tree ids and no `HEAD`; the three authored changed paths are a subset of attributed paths, the attributed/unattributed lists are disjoint, and the unattributed list is exactly the singleton gap; this node does not assert attributed-set equality or exclude extra attributed paths; and the unattributed path listed, counted with its reason and surviving a display filter |
| attributed source on the side that claims it | `:234` | A moved obligation's source is observed against **its own** side's tree — the candidate's new claim at `exact_recorded_blob`, the baseline's removed claim from the baseline |
| paging and the display budget | `:270`, `:738` | A small budget pages the comparison without shrinking its totals, and a page of a selection is what the comparison **displays**, not what it **selected** — R07's byte-budget page is not reused as the comparison's scope |
| refusal without substitution | `:316`, `:338`, `:438`, `:468` | A missing side refuses and substitutes no other snapshot; a real write to the candidate moves its logical digest and refuses the continuation with `continuation_binding_mismatch` and `detail` ending *"it binds another snapshot pair"*; a continuation presented against another selector refuses and returns **no page**; and a side naming another snapshot of its own file is refused by the per-side digest verification **before any page** |
| the response's honesty | `:511`, `:540`, `:573` | Nine verdict words searched over the whole **serialized** response with a positive control; the two change statements as separate fields where neither implies the other; and the record comparison reporting exactly the payload field that changed |
| the expansion's honesty | `:782`, `:804`, `:863` | No mounted UI and no approval the comparison cannot make; an unavailable observation reported as unavailable and **never** as a change set; and a probe that measured the trees being what makes a gap visible |

**The verdict-word case is the packet's *Forbidden Overreach* measured rather than asserted.** It searches
the serialized response's **field names and values** for nine verdict words and includes a positive
control, so the absence it proves is an absence in the payload a client actually receives — not merely in
the model's declared attributes.

**The three local helpers are deliberate.** `_substitute`/`_substituting` rewrite one field of one
already-built request so a case measures the *comparison's* answer to a mutated input rather than a
different request; `selected_scopes`/`_rewording` build the two `SelectedScope`s and a reworded variant
directly from the fixture, for the case that compares at the storage layer rather than through the seam.

### Conventions

- The module asserts against `DiffFixture`'s named identities through `item_for`/`items_of`, never against
  a stream position.

- `run_diff` is re-declared here rather than imported from the scope module: the boundary module builds
  its own request per case, and the two modules are separate populations with separate lane rows.

### Invariants And Boundaries

- **Integration by behaviour, not by preference.** The module creates two real Git repositories under
  `tmp_path`, commits both trees and borrows one object store from the other. Its
  candidate index is built independently by `build_read_scope_fixture` over a text tree
  with the revised statement, retired claim omitted and successor claim added; it is not
  a copy of a closed baseline database. The test-only `RowStore` mutation helpers change
  that text tree and rebuild its index, then reopen the connection. Default production
  probing observes the real Git pair; these fixture helpers are not the canonical writer
  or its public admission plane.

The sizes and catalog line addresses in the following original account are historical observations, not measurements of the present source tip.

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

- A new invariant and its one revision move the snapshot; refusal leaves every other row counter unchanged. [51]


### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `test_a_small_display_budget_pages_the_comparison_without_shrinking_its_totals` supplies the current fixture or assertion described above. [26]
- `test_the_record_comparison_reports_exactly_the_payload_field_that_changed` supplies the current fixture or assertion described above. [27]
- `test_a_page_of_a_selection_is_what_the_comparison_displays_not_what_it_selected` supplies the current fixture or assertion described above. [28]
- `test_an_unavailable_observation_is_reported_as_unavailable_and_never_as_a_change_set` supplies the current fixture or assertion described above. [29]
- `test_a_probe_that_measured_the_trees_is_what_makes_a_gap_visible` supplies the current fixture or assertion described above. [30]
- Fixture construction imports test-only row constructors; it does not call the retired canonical writer. [31]



- The test-only RowStore changes its text tree, rebuilds the index and reopens the read connection; candidate construction is independent, not a closed-database copy. [32]



### Docs References

No Domain Documentation entries are configured in this memory root. The statements below are grounded in
repository source and package-local evidence only.

No configured domain documentation could be checked.


- The integration marker, the fixture, the request builder and the public-seam driver. [33]


- The two readers that let a case name a record rather than a position. [34]



- Expansion asserts requested trees/roots and delimiter-safe command without HEAD; authored changed paths are an attributed subset, disjoint from the singleton unattributed gap, not an exact attributed-set census. [35]


- **The changed path no recorded realization attributes, listed as a visible gap that survives a filter.** [36]
- The moved obligation's source observed on the side that claims it. [37]
- **A small display budget paging the comparison without shrinking its totals.** [38]
- **A missing side refusing and substituting no other snapshot.** [39]


- The continuation-mutation helper adds an invariant and one revision through test-only text mutation/index rebuild; the continuation then refuses the changed snapshot. No public canonical-store admission is claimed. [40]


- **A continuation against another selector refusing and returning no page.** [41]
- **A side naming another snapshot of its own file refused before any page — the node the review's `R22` form kills.** [42]
- **The forbidden-overreach case: nine verdict words searched over the serialized response, with a positive control.** [43]

- The two change statements kept apart, and the record comparison reporting exactly the field that changed. [44]


- The input-substitution and scope-rewording helpers the last group of cases uses. [45]

- **A page of a selection being what the comparison displays and not what it selected.** [46]

- The two non-claims: no mounted UI and no approval, and an unavailable observation never reported as a change set — now with the partition asserted too (no total at all, empty third list, the undetermined limit declared and no counted omission). [47]

- **The probe that measured the trees being what makes a gap visible.** [48]

- run_diff omits a probe override, and the application defaults to git_tree_difference_probe; this source-described route is not a fresh execution count. [49]









> Retained earlier citation wording: - The module is registered in the integration lane and the current support-artifact consumer lists; catalog declaration is not execution evidence.






### Cross-Repo References

The module commits two real temporary Git repositories and points one at the other's object store, all
under `tmp_path`. No configured remote, protected branch or sibling repository is touched.

No configured cross-repository evidence is claimed.







- The module is registered in the integration lane and the current support-artifact consumer lists; catalog declaration is not execution evidence.

- The module is registered in the integration lane and the current support-artifact consumer lists; catalog declaration is not execution evidence. [50]

## Retirements

- Retired at the fifth freeze d59c3493: mcp/tests/evidence-lifecycle.toml:353-353 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:801-801 - the bytes it recorded now occur 5 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:1203-1203 - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2030-2030 - the bytes it recorded now occur 4 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2741-2741 - the bytes it recorded now occur 92 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2784-2784 - the bytes it recorded now occur 7 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:624-624 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:1937-1937 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:1981-1981 - the bytes it recorded now occur 3 times in the file, so no single home can be named and it is not given to the likelier one; mcp/tests/evidence-lifecycle.toml:2336-2336 - the bytes it recorded now occur 2 times in the file, so no single home can be named and it is not given to the likelier one. Retired means the anchor no longer stands, not that the cited subject was deleted.
