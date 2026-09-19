# mcp/tests/test_knowledge_citation_boundaries.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_citation_boundaries.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](../overview.md)

## Purpose

The citation-binding boundary cases: 15 cases that drive a **real** memory repository, a real
SQLite store at generation 5 and a real Git object store, because each of them exists to catch a
fallback that only a real store can expose.

## Code Commentary

### Logic

`_MemoryRepository` builds a real Git repository holding the corpus documents the cases bind against;
`_BindingCase` builds a real knowledge store at the required generation and authors a real terminology
facet to bind to, so every binding in this module points at a record that exists rather than at a
fixture identity. That last detail is load-bearing: the envelope's `knowledge_record` is a different
identity space from generation 1's revision tables, and a case that bound to an invariant revision id
was correctly refused with `missing_expected_row`.

The cases divide into three groups.

**The resolution cases.** `test_a_binding_recorded_against_a_real_document_revision_resolves_to_it`
binds against a measured corpus key and asserts the whole item travels — kind, lifecycle, authority
home. `test_an_owner_revision_the_object_store_cannot_obtain_is_reported_as_unavailable` is the
fallback catcher: the document **is** on disk at the recorded path and the resolver still reports
unavailable, so a working-tree fallback would fail the case.
`test_a_rewritten_document_leaves_the_binding_stale_and_never_re_bound` really rewrites the document
and asserts the binding still reports the *recorded* revision, with `counts.stale == 1`.

**The write-boundary cases.** A wrong-kind target is refused with `invalid_reference`, the expected and
observed kinds named, and **nothing written**; a target the namespace does not hold is refused; a
dangling governing route is refused while an ungoverned binding stores and is reported as `None`; two
bindings claiming one key in one owner revision are refused by the store itself; and a generation-4
dataset is refused the binding table rather than widened.

**The retention cases.** Publication is proven to read back `matched` against the real file, `missing`
against a removed one and `mismatched` against an altered one, with the destination asserted outside
the enclosure and the archive by construction — `../escape.md`, `sub/dir.md`, `..`, `""` and
`a\b.md` are all rejected.

### Invariants And Boundaries

- Every case opens a real store and most of them build a real Git repository, so the module is
  registered in the **integration** lane. `_uncovered_key_case` writes the complete row pair (envelope,
  sealed revision, binding row) rather than the binding row alone, because a binding whose sealed
  revision is missing is a store defect that raises — reporting it as "the target is missing" would
  answer a question about the store with a claim about the binding.
- The module-local helpers are test source and are deliberately **not** registered in the governed
  test-input inventory.
- The corpus keys the cases quote are quoted as corpus data. Quoting a real path in a test is a
  dependency edge in two registries — the evidence census and the selection graph — which is why this
  module's path literals are registrations rather than decoration.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The real Git memory repository the resolution cases bind against, and the real store the write cases run on, each cited at its own declaration.** | `_MemoryRepository`; `_BindingCase` | mcp/tests/test_knowledge_citation_boundaries.py:83-160; mcp/tests/test_knowledge_citation_boundaries.py:161-230 |
| **A binding against a real measured corpus revision, with kind, lifecycle and authority home travelling with the item.** | `test_a_binding_recorded_against_a_real_document_revision_resolves_to_it` | mcp/tests/test_knowledge_citation_boundaries.py:205-245 |
| **The rewritten-document case: the binding keeps its recorded revision and is never silently re-bound, with the stale count measured.** | `test_a_rewritten_document_leaves_the_binding_stale_and_never_re_bound` | mcp/tests/test_knowledge_citation_boundaries.py:248-305 |
| **The fallback catcher: the document is on disk at the recorded path and the resolver still reports unavailable.** | `test_an_owner_revision_the_object_store_cannot_obtain_is_reported_as_unavailable` | mcp/tests/test_knowledge_citation_boundaries.py:353-394 |
| The write refusals: a wrong-kind target with the kinds named and nothing written, a target the namespace does not hold, and a dangling governing route beside an accepted ungoverned binding. | `test_a_wrong_kind_target_is_refused_at_the_write_boundary`; `test_a_target_record_the_namespace_does_not_hold_is_refused`; `test_a_dangling_governing_route_is_refused_and_an_ungoverned_binding_is_not` | mcp/tests/test_knowledge_citation_boundaries.py:425-456; mcp/tests/test_knowledge_citation_boundaries.py:458-481; mcp/tests/test_knowledge_citation_boundaries.py:483-538; mcp/tests/test_knowledge_citation_boundaries.py:401-431 |
| **The store itself refusing two bindings that claim one key in one owner revision.** | `test_two_bindings_claiming_one_key_in_one_owner_revision_are_refused_by_the_store` | mcp/tests/test_knowledge_citation_boundaries.py:516-543 |
| The dataset's own declared tables holding the binding rows, and a generation-4 dataset refused the binding table rather than widened. | `test_the_binding_rows_live_in_the_datasets_own_declared_tables`; `test_a_generation_4_dataset_is_refused_the_binding_table_rather_than_widened` | mcp/tests/test_knowledge_citation_boundaries.py:574-611; mcp/tests/test_knowledge_citation_boundaries.py:613-648; mcp/tests/test_knowledge_citation_boundaries.py:550-595 |
| **The retention cases: a published artifact reads back matched, a missing destination is blocked, changed bytes are mismatched, and the destination is outside the enclosure and the archive by construction.** | `test_a_published_artifact_reads_back_with_its_published_digest`; `test_the_destination_is_outside_the_enclosure_and_the_archive_by_construction`; `test_a_missing_durable_destination_reads_back_as_a_blocked_state`; `test_a_destination_whose_bytes_changed_reads_back_as_mismatched` | mcp/tests/test_knowledge_citation_boundaries.py:635-665; mcp/tests/test_knowledge_citation_boundaries.py:667-685; mcp/tests/test_knowledge_citation_boundaries.py:687-707; mcp/tests/test_knowledge_citation_boundaries.py:709-727 |
| **The uncovered form produced on a real store by a directly written row pair, counted in a denominator of two and asserted distinct from the recorded-blob mismatch.** | `test_an_uncovered_key_form_is_counted_and_reported_on_a_real_store` | mcp/tests/test_knowledge_citation_boundaries.py:714-822 |
| The integration lane row this module occupies. | "mcp/tests/test_knowledge_citation_boundaries.py" | mcp/tests/test-evidence-lanes.toml:192-193; mcp/tests/evidence-lifecycle.toml:953-957; mcp/tests/test-evidence-lanes.toml:196-196; mcp/tests/evidence-lifecycle.toml:197-197; mcp/tests/test-evidence-lanes.toml:197-202 |
| **The ambient-runner artifact's consumer list, which gained this module's path literal.** | "mcp/tests/test_knowledge_citation_boundaries.py" | mcp/tests/evidence-lifecycle.toml:820-820; mcp/tests/evidence-lifecycle.toml:950-957; mcp/tests/evidence-lifecycle.toml:961-965 |
| **The knowledge contract's consumer list, which gained the same path literal.** | "mcp/tests/test_knowledge_citation_boundaries.py" | mcp/tests/evidence-lifecycle.toml:1198-1198; mcp/tests/evidence-lifecycle.toml:820-820; mcp/tests/evidence-lifecycle.toml:950-957; mcp/tests/evidence-lifecycle.toml:961-965 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. The memory repository the cases build is a
temporary Git repository local to each case.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T19:54:57+02:00 — 260915-KS-L23 residue clearance, seat B (uncommitted change set on `ar/260915-ks-l23`, memory base `59eab7a0`): **cleared the three enforced `citation_anchor_absent_from_range` rows in this document** (three table rows, the module's own path literal in each). The lane row's last range stopped at `197` (`public-contract = [`) instead of reaching the integration lane entry at `202`; it was widened to `197-202`. Both consumer-list rows stopped at `961-961` while the entry that actually carries the path sits at `965`; each was widened to `961-965`. Claims, anchors and the other ranges are unchanged. No claim was re-worded, no anchor or range was dropped to silence a row, and no verification stamp advanced: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_a_binding_recorded_against_a_real_document_revision_resolves_to_it` repointed to mcp/tests/test_knowledge_citation_boundaries.py:205-245. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_a_rewritten_document_leaves_the_binding_stale_and_never_re_bound` repointed to mcp/tests/test_knowledge_citation_boundaries.py:248-305. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_an_owner_revision_the_object_store_cannot_obtain_is_reported_as_unavailable` repointed to mcp/tests/test_knowledge_citation_boundaries.py:353-394. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_two_bindings_claiming_one_key_in_one_owner_revision_are_refused_by_the_store` repointed to mcp/tests/test_knowledge_citation_boundaries.py:516-543. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_an_uncovered_key_form_is_counted_and_reported_on_a_real_store` repointed to mcp/tests/test_knowledge_citation_boundaries.py:714-822. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:06:32+00:00: Generated citation repair: "mcp/tests/test_knowledge_citation_boundaries.py" repointed to mcp/tests/test-evidence-lanes.toml:167-167. No content impact: mechanical anchor-range projection bound to citation source snapshot ff98360f8649d71f1a69cbfa94559ed9eed708a54fcd5378afa764553cd788b4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:45+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `a0665505`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the range recorded in the row above is the one that now holds its anchor. The anchors concerned: `mcp/tests/test_knowledge_citation_boundaries.py`. No claim wording changed, and the verification metadata advances to the landed base because the claims were re-read against the current source.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the leaf's boundary case module (15 cases, integration lane). The card records why each group exists rather than what it does. The resolution cases are **fallback catchers**: the unavailable case has the document present on disk at its recorded path and still demands `recorded_object_unavailable`, so a working-tree fallback fails the case rather than passing quietly. The write cases measure refusal *and* its consequence — a wrong-kind target is refused with the kinds named and nothing written — and one of them is the store's own `UNIQUE` constraint refusing a second claim of one key. The retention cases measure the read-back in both directions rather than inspecting the code that writes the file. The card also records the two facts a future editor must not undo: the cases write the **complete** row pair because a binding whose sealed revision is missing is a store defect, and quoting a real path in a test is a dependency edge in two registries, which is why the module's path literals are registrations rather than decoration. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
