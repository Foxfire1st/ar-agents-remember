# mcp/tests/test_master_net_generation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_master_net_generation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T05:30:43+00:00 |
| lastVerifiedCommitHash | `55c62237132eaa56b0df28ae5a8420a8dc05303d` |
| lastVerifiedCommitDate | 2026-09-28T16:17:26+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **production-composition evidence for `ICR-R13@v1`**: the master NET comparison is
endpoint-correct and bound to a generation, measured through the operations the dashboard
really calls. Every case builds a real series contract on disk, real leaf enclosure contracts,
real code and memory repositories with real branches, and the real `master_changeset` /
`master_file_diff` resolution plus the HTTP routes that serve them. Nothing here injects a
preconstructed payload or a hand-built comparison — which is what the packet's own evidence
class requires, since "tests that merely mirror implementation or assert returned prebuilt
payloads are insufficient for production-composition claims".

## Code Commentary

### Logic

Nine cases, one load-bearing property each (the module's own docstring lists seven; the
route case and the F1 diff-failure case complete the nine):

- `test_two_leaves_that_add_then_remove_a_file_net_to_exactly_zero` — the packet's
  conforming example and the falsifier for its non-conforming one: two leaves add then
  remove one file, the net is exactly `[]` with zero counters while both leaf counters stay
  nonzero. cit:([`test_two_leaves_that_add_then_remove_a_file_net_to_exactly_zero`], mcp/tests/test_master_net_generation.py:237-265)
- `test_a_net_zero_source_result_still_reports_memory_effects` — the packet's boundary:
  net-zero source with a one-line `memory.md` effect reports `code: []` + `memory:
  [memory.md]`. cit:([`test_a_net_zero_source_result_still_reports_memory_effects`], mcp/tests/test_master_net_generation.py:267-283)
- `test_a_pinned_generation_reopens_after_the_branch_advances` — the completed master's
  recorded result: a pinned generation reopens byte-identically after the branch advances
  (`superseded`) while the live view moves on (`current`, new digest). cit:([`test_a_pinned_generation_reopens_after_the_branch_advances`], mcp/tests/test_master_net_generation.py:285-309)
- `test_an_opened_file_stays_bound_to_the_listed_generation` — a pinned file expansion
  returns the recorded bytes while the live expansion returns `after: None`.
  cit:([`test_an_opened_file_stays_bound_to_the_listed_generation`], mcp/tests/test_master_net_generation.py:311-343)
- `test_an_unreadable_child_never_invalidates_the_net` — a garbage leaf contract plus an
  unresolvable leaf commit leave the net matching the live integrated result.
  cit:([`test_an_unreadable_child_never_invalidates_the_net`], mcp/tests/test_master_net_generation.py:345-363)
- `test_a_missing_code_endpoint_is_refused_never_substituted` — a missing endpoint is
  refused by name (`not-recorded` / `unresolvable`), never substituted with a later tip;
  an unknown master keeps degrading to empty. cit:([`test_a_missing_code_endpoint_is_refused_never_substituted`], mcp/tests/test_master_net_generation.py:365-397)
- `test_a_live_leaf_is_labelled_working_and_its_draft_stays_out_of_the_net` — a live leaf
  row reads `working` beside the integrated net and its uncommitted delta never leaks in.
  cit:([`test_a_live_leaf_is_labelled_working_and_its_draft_stays_out_of_the_net`], mcp/tests/test_master_net_generation.py:399-441)
- `test_the_master_routes_carry_the_generation_and_its_named_refusal` — the served routes:
  the list publishes `generation` + `currentness` + `scope`, and the shared 400/404 mapping
  carries the named refusal. cit:([`test_the_master_routes_carry_the_generation_and_its_named_refusal`], mcp/tests/test_master_net_generation.py:443-470)
- `test_a_diff_failure_after_validation_is_refused_never_reported_as_zero` — the F1 fix:
  a diff that fails *after* endpoint validation (monkeypatched
  `changed_files_with_counts` raising) is refused with `kind == "unresolvable"`, never
  reported as an empty net. cit:([`test_a_diff_failure_after_validation_is_refused_never_reported_as_zero`], mcp/tests/test_master_net_generation.py:472-488)

The shared world is `MasterFixture` with its `master_fixture(tmp_path)` builder — a
master-shaped fixture (series contract + two leaf contracts + real code/memory repos) that
leaf one adds `src/feature.py` into and leaf two removes. cit:([`MasterFixture`], mcp/tests/test_master_net_generation.py:110-229) cit:([`master_fixture`], mcp/tests/test_master_net_generation.py:241-245)
`pytestmark = pytest.mark.evidence_unit` declares the evidence lane; the lane row that makes
these cases run at all is `mcp/tests/test-evidence-lanes.toml:113`.

### Conventions

Real-Git fixture module in the `test_knowledge_review_source_endpoints.py` idiom: real
contracts on disk, real branches, the real resolution plus the real HTTP routes. Case names
state the property as a sentence. The F1 case pins the exact refusal kind and the
refused-not-empty wording.

### Invariants And Boundaries

- No preconstructed resolutions, fake indexes or hand-built payloads anywhere.
- R24 navigation is explicitly not claimed here; mounted-browser observation of the
  generation caption belongs to R24/R25 assembly (jsdom proves URLs + caption render).
- The module registers no contract and no artifact and consumes no catalog-registered
  support module, so `mcp/tests/evidence-lifecycle.toml` is untouched and
  `LIFECYCLE_CATALOG_SHA256` is not re-pinned.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The evidence lane the module runs in. | `pytestmark` | mcp/tests/test_master_net_generation.py:67-67 |
| The shared master-shaped world (series + two leaf contracts, real code/memory repos) and its builder. | `MasterFixture`; `master_fixture` | mcp/tests/test_master_net_generation.py:110-229; mcp/tests/test_master_net_generation.py:231-235; mcp/tests/test_master_net_generation.py:242-242 |
| The conforming add-then-remove case and the F1 diff-failure refusal case. | `test_two_leaves_that_add_then_remove_a_file_net_to_exactly_zero`; `test_a_diff_failure_after_validation_is_refused_never_reported_as_zero` | mcp/tests/test_master_net_generation.py:237-265; mcp/tests/test_master_net_generation.py:472-488 |
| The lane row that makes these cases run. | `test_master_net_generation` | mcp/tests/test-evidence-lanes.toml:131-131 |
| The selection under test (endpoint binding, digest, currentness, refusal) and the thin entry that publishes it. | `select_master_net`; `master_changeset` | mcp/src/agents_remember/serving/master_net_generation.py:171-200; mcp/src/agents_remember/serving/changeset.py:247-323 |

## Cross-Repo References

This card maps a repository-local agents-remember test module. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.

- 2026-09-27T05:30:43+00:00 — Authored scoped citation maintenance for 1 L41 source-range projection(s) resolved by the frozen source index. Only changed-source ranges were adopted from the preview; unrelated ranges, generated history and verification stamps are preserved.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `pytestmark` repointed to mcp/tests/test_master_net_generation.py:67-67. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `test_master_net_generation` repointed to mcp/tests/test-evidence-lanes.toml:123-123. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-25T22:19:46+00:00: Generated citation repair: `master_fixture` repointed to mcp/tests/test_master_net_generation.py:241-245. No content impact: mechanical anchor-range projection bound to citation source snapshot 387c4db0e7315fbee092befda9bc6a3baaa4f61fe1047d8e9d84107b1952fdc6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **body update — four cases for the NUL-safe path family (D02, including the no-escape-rewrite proof F4 asked for).** The fixture carries eight names, a tab, a newline and a literal backslash on each side (tracked and untracked); restoring the old `\` → `/` rewrite makes two of the cases fail. **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T11:39:00+02:00 — 260921-ICR-L13 curator, **sync follow-up: lane row (`:113` → `:114`) and verification pair re-derived to the merged production line.** ICR-L7 inserted its revision-selection row above. The module, cases and boundaries are unchanged. No verification stamp was advanced.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **created.** The module is new in this leaf and this is its one-to-one card. It records the nine measured properties (eight plus the F1 diff-failure refusal), the shared `MasterFixture` world, the `evidence_unit` lane with its `:114` row (`:113` before the ICR-L7 sync), and the no-catalog-touch boundary. The F1 case (monkeypatched diff raising after validation, `kind == "unresolvable"`) is part of what this card documents. **Stamp accounting:** the verification pair names the **production line at this leaf's base** `6695a2a12961ef340c8864d56f0a1ce12b51b3c5` (2026-09-22T09:38:24+02:00) while what was actually read is this leaf's uncommitted working tree — this leaf's **uncommitted** candidate, the only tree containing this module. Closeout owns the stamp.
