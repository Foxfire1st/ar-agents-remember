# mcp/tests/test_knowledge_diff_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_diff_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| lastVerifiedCommitDate | 2026-09-18T09:42:44+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation entries are configured in this memory root. The statements below are grounded in
repository source and package-local evidence only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The integration marker, the fixture, the request builder and the public-seam driver. | `pytestmark`; `fixture`; `request_for`; `run_diff` | mcp/tests/test_knowledge_diff_boundaries.py:51-51; mcp/tests/test_knowledge_diff_boundaries.py:68-73; mcp/tests/test_knowledge_diff_boundaries.py:76-106; mcp/tests/test_knowledge_diff_boundaries.py:109-122 |
| The two readers that let a case name a record rather than a position. | `items_of`; `item_for` | mcp/tests/test_knowledge_diff_boundaries.py:125-139 |
| **The expansion naming both requested trees and every path they differ at, with the reproducing command and no `HEAD`.** | "test_the_expansion_names_both_requested_trees_and_every_path_they_differ_at" | mcp/tests/test_knowledge_diff_boundaries.py:145-182 |
| **The changed path no recorded realization attributes, listed as a visible gap that survives a filter.** | "test_a_changed_path_no_recorded_realization_attributes_is_listed_as_a_visible_gap" | mcp/tests/test_knowledge_diff_boundaries.py:185-218 |
| The moved obligation's source observed on the side that claims it. | "test_the_attributed_source_of_a_moved_obligation_is_observed_on_the_side_that_claims_it" | mcp/tests/test_knowledge_diff_boundaries.py:221-251 |
| **A small display budget paging the comparison without shrinking its totals.** | "test_a_small_display_budget_pages_the_comparison_without_shrinking_its_totals" | mcp/tests/test_knowledge_diff_boundaries.py:257-297 |
| **A missing side refusing and substituting no other snapshot.** | "test_a_missing_side_refuses_and_substitutes_no_other_snapshot" | mcp/tests/test_knowledge_diff_boundaries.py:303-322 |
| **The real candidate write that moves the logical digest and refuses the continuation, and the helper that makes the write through the public store.** | "test_a_candidate_that_changed_after_a_continuation_refuses_the_continuation"; `add_unrelated_revision` | mcp/tests/test_knowledge_diff_boundaries.py:325-363; mcp/tests/test_knowledge_diff_boundaries.py:366-405 |
| **A continuation against another selector refusing and returning no page.** | "test_a_continuation_presented_against_another_selector_refuses_and_returns_no_page" | mcp/tests/test_knowledge_diff_boundaries.py:408-435 |
| **A side naming another snapshot of its own file refused before any page — the node the review's `R22` form kills.** | "test_a_side_naming_another_snapshot_of_its_own_file_refuses_before_any_page" | mcp/tests/test_knowledge_diff_boundaries.py:438-475 |
| **The forbidden-overreach case: nine verdict words searched over the serialized response, with a positive control.** | "test_no_field_of_a_comparison_can_carry_a_strengthening_or_harmlessness_verdict" | mcp/tests/test_knowledge_diff_boundaries.py:481-507 |
| **The two change statements kept apart, and the record comparison reporting exactly the field that changed.** | "test_the_two_change_statements_are_separate_fields_and_neither_implies_the_other"; "test_the_record_comparison_reports_exactly_the_payload_field_that_changed" | mcp/tests/test_knowledge_diff_boundaries.py:510-540; mcp/tests/test_knowledge_diff_boundaries.py:543-597 |
| The input-substitution and scope-rewording helpers the last group of cases uses. | `_substitute`; `_substituting`; `selected_scopes`; `_rewording` | mcp/tests/test_knowledge_diff_boundaries.py:616-634; mcp/tests/test_knowledge_diff_boundaries.py:637-684; mcp/tests/test_knowledge_diff_boundaries.py:687-705 |
| **A page of a selection being what the comparison displays and not what it selected.** | "test_a_page_of_a_selection_is_what_the_comparison_displays_not_what_it_selected" | mcp/tests/test_knowledge_diff_boundaries.py:708-749 |
| The two non-claims: no mounted UI and no approval, and an unavailable observation never reported as a change set. | "test_a_comparison_names_no_mounted_ui_and_no_approval_it_cannot_make"; "test_an_unavailable_observation_is_reported_as_unavailable_and_never_as_a_change_set" | mcp/tests/test_knowledge_diff_boundaries.py:752-771; mcp/tests/test_knowledge_diff_boundaries.py:774-814 |
| **The probe that measured the trees being what makes a gap visible.** | "test_a_probe_that_measured_the_trees_is_what_makes_a_gap_visible" | mcp/tests/test_knowledge_diff_boundaries.py:817-840 |
| The production probe these cases drive rather than substitute. | `git_tree_difference_probe` | mcp/src/agents_remember/application/knowledge_diff.py:162-196 |
|The fixture these cases run on, and the governed contract it is registered under.|`build_diff_fixture`; `knowledge-diff-cases`| mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/evidence-lifecycle.toml:1256-1277; mcp/tests/evidence-lifecycle.toml:1262-1262 |
|**The integration-lane row this module occupies, and the read-scope artifact whose consumer list it joined.**|"integration = ["; "owner = \"knowledge-read-scope-cases\""| mcp/tests/evidence-lifecycle.toml:1299-1299; mcp/tests/test-evidence-lanes.toml:168-168 |
| The fixture these cases run on, and the governed contract it is registered under. | `build_diff_fixture`; `knowledge-diff-cases` | mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/evidence-lifecycle.toml:1198-1202 |
| **The integration-lane row this module occupies, and the read-scope artifact whose consumer list it joined.** | "integration = ["; "owner = \"knowledge-read-scope-cases\"" | mcp/tests/evidence-lifecycle.toml:1299-1299; mcp/tests/test-evidence-lanes.toml:168-168 |

## Cross-Repo References

The module commits two real temporary Git repositories and points one at the other's object store, all
under `tmp_path`. No configured remote, protected branch or sibling repository is touched.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured cross-repository evidence is claimed. | — | — |
| The fixture these cases run on, and the governed contract it is registered under. | `build_diff_fixture`; `knowledge-diff-cases` | mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/evidence-lifecycle.toml:1198-1202; mcp/tests/evidence-lifecycle.toml:1262-1262 |
| **The integration-lane row this module occupies, and the read-scope artifact whose consumer list it joined.** | "integration = ["; "owner = \"knowledge-read-scope-cases\"" | mcp/tests/evidence-lifecycle.toml:1299-1299; mcp/tests/test-evidence-lanes.toml:168-168 |

## Update History
- 2026-09-18T07:21:19+00:00: Generated citation repair: "integration = ["; "owner = \"knowledge-read-scope-cases\"" repointed to mcp/tests/test-evidence-lanes.toml:168-168; mcp/tests/evidence-lifecycle.toml:1299-1299. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "integration = ["; "owner = \"knowledge-read-scope-cases\"" repointed to mcp/tests/test-evidence-lanes.toml:168-168; mcp/tests/evidence-lifecycle.toml:1299-1299. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "integration = ["; "owner = \"knowledge-read-scope-cases\"" repointed to mcp/tests/test-evidence-lanes.toml:168-168; mcp/tests/evidence-lifecycle.toml:1299-1299. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 7 generated projection bullet(s) by hand while resolving the memory sync** — `integration = [`, `owner = \`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand** — `integration = [`, `owner = \`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"integration = ["; "owner = \"knowledge-read-scope-cases\""` → `mcp/tests/test-evidence-lanes.toml:162-162; mcp/tests/evidence-lifecycle.toml:1285-1285`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:1285-1285; mcp/tests/test-evidence-lanes.toml:160-160` -> `mcp/tests/evidence-lifecycle.toml:1286-1286; mcp/tests/test-evidence-lanes.toml:161-161`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T01:15:00+00:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): created this one-to-one card for the comparison's integration population (fifteen cases, integration lane row `:159`, 840 lines — under the 1 200-line rail). It records the six groups of properties the module owns and why each needs a real boundary: the two **real** Git trees and the production probe, the **real** candidate write that moves the logical digest and refuses the continuation, the paging arithmetic through the seam, the four refusal-without-substitution cases (one of which the review's `R22` form kills), and the response's honesty cases — including the forbidden-overreach node, which searches **nine verdict words over the serialized payload with a positive control** rather than over the model's declared attributes. It states the two properties that make the module's lane membership behaviour-preserving (real repositories and a real curated database under `tmp_path`; the production Git probe driven rather than substituted), that nothing was skipped, xfailed, deselected or widened, and that the **16 `reportArgumentType` pyright findings belong to the sibling scope module and not here** — pre-existing, byte-identical across the leaf's fix rounds, outside the published seven-module scope, and carried to `KS-R09`/`L9` to confirm or disposition. It closes by recording that the leaf's carried debt is report text rather than this module's cases: the final verification round reproduced every taxonomy verdict on the frozen bytes with its own instrument (39 applications, 126 scored node runs, 41 assertion kills, 1 exception death, 0 broken mutations, 0 refusals). Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
