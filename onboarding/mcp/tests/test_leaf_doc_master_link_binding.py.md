# mcp/tests/test_leaf_doc_master_link_binding.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Proves, on real repositories, that a leaf task document authored **before** its master's series contract
exists acquires its derived master link when the leaf is started — and that the authoring plane refuses
the one case nothing would ever repair.

Planning a master necessarily authors its leaf documents before the master's first `worktree_start`
bootstraps the series contract. At authoring time `task_doc` cannot stamp the two derived fields
(`seriesContractPath`, `enclosures[]`), so start is the only place they can ever be bound. This module
pins both halves of that fix together: the bind-at-start half and the fail-closed half, because either
alone is wrong — binding without the refusal leaves an unrepairable silent drop, and refusing without the
binding makes the normal planning flow impossible.

The restamp's own decision table is covered on the unit population in
`test_task_document_application_1.py` (`LeafDocMasterLinkBindingTests`); this module is the end-to-end
proof over a real coordination root, code repository and Git-backed memory repository.

## Code Commentary

### Logic

One scratch coordination root, one code repository and one external memory repository per case, built in
`setUp` (`:45-66`) from `init_repo`, `initialized_memory_repo` and a real `McpRuntimeConfig`. The task root
is `tasks/repo-a/260624_master/`.

`_author_master` (`:78-93`) and `_author_leaf` (`:95-108`) author both documents through the real
`task_doc_tool`; `_write_leaf_document` (`:110-141`) instead authors the pre-contract document state
directly, giving the master its live row for the leaf first (that row is what start proves leaf identity
against) while deliberately withholding the series contract and the two derived fields. `_start_leaf`
(`:143-159`) drives the real public `worktree_manager.start_result` with `skip_provider_setup=True` and
`memory_mode="disabled"`.

The four cases:

- `test_leaf_authored_before_its_series_contract_gets_its_link_at_start` (`:163-195`) is the exact sequence
  that produced this master's own first leaf with `seriesContractPath: None`. It asserts the precondition
  rather than assuming it — `series_contract_path(task_root).exists()` is false and the authored document
  carries `seriesContractPath is None` and `enclosures == []` — then starts the leaf and asserts the
  document now carries the series contract path, the one `enclosures[]` ref naming the real enclosure
  contract, and the stamped `lifecycleId`.
- `test_an_existing_damaged_document_is_repaired_by_its_next_start` (`:197-233`) is the already-damaged
  case: the document exists with `lifecycleId="LC-OLD"` and no link, and its authored content (title,
  objective, requirements, steps) must survive the repair. Start binds the link, follows the fresh
  lifecycle `LC-REPAIR`, and changes nothing else — asserted field by field.
- `test_authoring_a_leaf_with_no_master_document_is_refused_with_its_remedy` (`:235-250`) is the fail-closed
  half: with no series contract and no master document in the task root, authoring the leaf raises
  `TaskDocError` whose message names `seriesContractPath`, the exact missing master `task.json` path and the
  remedy, and no leaf document is written.
- `test_authoring_a_master_and_its_leaves_before_any_start_still_succeeds` (`:252-268`) is the counter-case
  that keeps the planning flow usable: master first, then two leaves, no start anywhere. Both leaves are
  still unstamped (`seriesContractPath` `None`, `enclosures` empty, `lifecycleId` `None`) — the documented,
  repairable state the first case proves start binds — and both master rows exist.

### Conventions

The module authors documents through the real `task_doc` plane wherever the plane is the subject, and only
falls back to `write_task_doc` for the pre-contract state the plane is forbidden to produce. `LEAF_ID`
(`15_leaf`) is the enclosure leaf id and `LEAF_DOC_ID` (`15`) the authored document id, which keeps the
case-insensitive lookup path in play rather than accidentally matching on identical strings.

The module is a registered consumer of `mcp/tests/closeout_input_test_support.py` and
`mcp/tests/curator_coherence_test_support.py` in `mcp/tests/evidence-lifecycle.toml` (consumer rows `:315`
and `:373`), both reached transitively through `test_worktree_support`'s `initialized_memory_repo`, which
imports both. Consumer declarations are ownership accounting only; they are not execution or acceptance
evidence. The module is registered in the **integration** lane of `mcp/tests/test-evidence-lanes.toml`
(entry row `:152`) by the same change set that created it: it drives a real worktree start over real
temporary Git repositories, so that is its behaviour-preserving lane.

### Invariants And Boundaries

- The precondition assertions are load-bearing, not decoration: without them the case would still pass if
  authoring quietly started stamping the fields, and the module would stop proving anything about start.
- The repair is asserted to be **additive**: fresh lifecycle yes, but objective, requirements, steps and
  title must be unchanged, so a repair that rewrote the authored document would fail here.
- The refusal case asserts the message's substance (the missing link's field names, the exact master path,
  the remedy) and that nothing was written, rather than matching one phrasing verbatim.
- These are focused development cases over disposable repositories. They are behavior evidence for one
  route, not full-suite certification or independent review, and this card records source inspection, not a
  test run.

### Todos

None recorded. The module deliberately does **not** cover the false premise that survived in
`restamp_leaf_doc_lifecycle`'s docstring — that function has no caller in `mcp/src` at all (see the
`tasks/leaf_doc.py` card), so there is no route to exercise; the live publisher is covered through start.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; the proving evidence is this
repository's own source, the real `task_doc` plane and real Git objects.

No external source is required for this repository-owned binding proof.

### Repo-Internal References

- The pre-contract authoring path and the exact sequence that lost the master link: master and leaf authored through `task_doc` with no series contract, then started. [1]
- The repair path for an already-damaged document, asserted additive (authored content unchanged). [2]
- The fail-closed half: a leaf under a task root with no master document is refused with its remedy and writes nothing. [3]
- The counter-case that keeps planning usable: master plus two leaves before any start, still unstamped. [4]
- The refusal this module asserts, with its remedy text. [5]
- The start publisher that binds the missing link, entered from the real start path. [6]
- The worktree-side wrapper that resolves the canonical parent row and delegates to the task-domain planner. [7]
- The task-domain planner that decides whether the derived master link is bound. [8]
- The focused restamp decision-table class in the sibling module, which this module's docstring points at. [9]
- The two artifact rows that declare this module as an exact consumer, both through `test_worktree_support`. [10]
- The transitive importer that makes the module a consumer of both supports. [11]
- The integration lane row the fail-closed manifest requires. [12]
- The transitive importer that makes the module a consumer of both supports. [13]
- The integration lane row the fail-closed manifest requires. [14]

### Cross-Repo References

Each case builds both repositories it spans — a code repository and an external memory repository — as real
temporary Git repositories, which is what lets `worktree_start` run at all. No production
cross-repository authority is claimed by this focused module.

- The external-memory side of each case is a real second repository created by the fixture, not a mock. [15]
