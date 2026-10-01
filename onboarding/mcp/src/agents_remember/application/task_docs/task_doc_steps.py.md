# mcp/src/agents_remember/application/task_docs/task_doc_steps.py

## Governing Overview

[application/task_docs route overview](overview.md)

## Purpose

The task-document **step plane**: it owns the addressing rule and the four step operations
(`set_step`, `add_step`, `remove_step`, `skip_step`) plus the focused `read_steps` projection. It
exists as a separate module because keeping the plane inline pushed `task_doc_tools.py` to 1,243
lines, over the armed 1,200-line hard limit — the same decomposition pattern as
`task_doc_discard`, `task_doc_route_review`, and `task_sprint_linkage`. `task_doc_tools.py`
registers the operations and delegates through thin `_apply_*` adapters; this module owns the
behaviour.

## Code Commentary

### Logic

The module's single contract is **one exact addressing rule**, shared by every operation:
`parent` selects the namespace (absent = top level, present = that parent's `substeps`), and zero or
multiple matches refuse. `exact_step_target` implements it for the operations that act on one
existing unit; `_step_container` implements it for the create-only path. `_one_exact_match` is the
only place a "not found" / "ambiguous" refusal is raised, so no operation can silently collapse or
guess. `parent` is never reinterpreted as a top-level id.

The four operations are deliberately split by intent:

- `set_step` — **update-only**. It never creates. It writes only the keys in `_STEP_UPDATE_KEYS`
  (`title`, `status`, `note`) and clears an earlier `disposition` when an explicit `status` arrives
  (the status edit records executed/reworked state, not the old skip decision).
- `add_step` — **create-only**. It requires both `id` and `title` and refuses an id that already
  exists in its scope ("use `set_step` to update it").
- `remove_step` — **delete-only**. It requires a nonblank `step.reason` and appends a decision entry
  (`Removed step <qualified id>.` with that rationale) in the exact shape `skip_step` uses, so the
  audit entry substitutes for the lost step history.
- `skip_step` — **keep and resolve**. Moved here verbatim from the tools module: it marks the one
  unit `done`, records an `intentionalSkip` disposition (`recordedVia: task_doc.skip_step`, plus the
  lifecycle id), appends its decision, and does not cascade. It refuses a target that is already
  `done`.

`_step_miss_hint` is the defect guard. For a bare id that actually belongs to a substep it names the
parent ("did you mean parent 'S1'?"), and for a `<parent>.<child>` id whose child lives under that
parent it names both halves. `skip_step` deliberately keeps its original miss wording (it never
acquired the bare-id defect); `set_step` and `remove_step` pass `hint=True`.

`step_payloads` / `_substep_payload` are the read projection behind the `read_steps` operation:
`id`, `title`, `status`, `note`, and nested `substeps` — never the whole authored document.

`step_reason` is shared with the tools module: `task_doc_tools._enforce_terminal_status` calls it to
recognize a reasoned removal before the Completion guard.

### Conventions

- Module-level definitions follow the package conventions; names prefixed with `_` are private.
- Refusals are typed `TaskDocError`s imported from the sibling `task_doc_route_review` module, the
  package's existing error home.
- Operation names appear in the refusal text (``f"{operation}: ..."``), so one addressing rule can
  serve four operations without losing which call failed.

### Invariants And Boundaries

- **One addressing rule, no namespace guessing.** `parent` present selects that parent's substeps;
  `parent` absent selects top level. A bare id is never matched at both levels, and an ambiguous id
  refuses rather than picking the first.
- **`set_step` never creates and `add_step` never updates.** The two intents are not interchangeable;
  neither is a fallback for the other.
- **`remove_step` and `skip_step` are distinct and must not be documented as interchangeable.**
  `remove_step` means "this step should never have existed" and deletes the unit;
  `skip_step` means "this planned unit was deliberately not done" and keeps and resolves it. Both
  require a nonblank reason and both append a decision.
- **A reasoned removal is the terminal-status exception.** Per developer ruling, `remove_step` may
  remove a unit whose status is already `done` and may operate on a document whose status is
  `Completed`, provided the nonblank reason is given. The reason substitutes for the refusal and the
  decision entry substitutes for the lost history. The second is *required* rather than merely
  permitted: the motivating repair removed four spurious top-level steps from an
  already-`Completed` leaf document, and gating on document status would have forced a full-document
  `replace` that was correctly refused as too destructive. The ruling is enforced in
  `task_doc_tools._enforce_terminal_status`, which consults `step_reason` here.
- `_STEP_UPDATE_KEYS` omits nothing the caller may restate, but a caller cannot write arbitrary
  keys through this path: only those three are copied onto the target.
- The module carries no write of its own — it mutates the `model_dump(by_alias=True)` dict the tools
  module hands it; validation and persistence stay with `task_doc_tools.py` and the publication
  boundary.

### Todos

None.

## Evidence

### Docs References

No configured external Domain Documentation source applies; this is a repository-internal
application module.

No relevant external documentation was found after checking the configured source registry.

### Repo-Internal References

- The fields a caller may restate on an existing step; `note` is here for both levels because the top-level key set used to omit it. [1]
- The shared nonblank-reason reader, also consumed by the tools module's terminal-status exemption. [2]
- The single addressing rule every step operation shares, including the parent-naming miss hint. [3]
- The create-only operation requires a title and refuses an existing id in its scope. [4]
- The delete-only operation requires a reason and appends the removal decision. [5]
- The update-only operation and the fields it may copy. [6]
- `skip_step` moved here verbatim: keep the unit, mark it done, record `intentionalSkip`, do not cascade. [7]
- The focused checklist read behind the `read_steps` special operation. [8]
- The dispatcher that registers the operations and delegates through thin `_apply_*` adapters. [9]
- The terminal-status guard that admits a reasoned `remove_step` on a `Completed` document. [10]
- The schema field that made a top-level `note` storable at all. [11]
- The executor that pins the addressing, create/delete, note-persistence, rendering, and Completed-document behaviours. [12]

### Cross-Repo References

No meaningful cross-repository boundary is owned by this file.

No cross-repository protocol or external system is involved.
