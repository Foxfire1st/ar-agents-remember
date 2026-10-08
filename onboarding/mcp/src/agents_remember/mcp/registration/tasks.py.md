# mcp/src/agents_remember/mcp/registration/tasks.py

## Governing Overview

[registration route overview](overview.md)

## 260731-EFA-L8 Change

The tool-registration functions gained bare-`*` keyword-only signatures (the 19
PLR0917 fixes across `mcp/registration/*.py`); the rule stays enabled and call sites
already pass keywords. Registered tools are unchanged.

## Purpose

`register_task_tools(server, config)` declares the task-document authoring tool plus the two
task-state transitions: `task_reopen`, `lifecycle_finalize_task`, `task_doc`.

## Code Commentary

### Logic

`task_doc` is the JSON-primary authoring tool and carries the longest docstring on the surface,
because the operation vocabulary is not in the types: `create` | `replace` | `set_status` |
`set_step` | `add_step` | `remove_step` | `skip_step` | `read_steps` | `set_subtask` |
`remove_subtask` | `set_section` | `append_decision` |
`record_route_review` | `author_execution_graph` | `attach_master` | `detach_master` | `retire_master` |
`linkage_report` | `set_field` |
`get` (`migrate_execution_topology` was removed in 260815-DAG-L13). The JSON document is the source of truth; `task.md` / `<slug>.md` is a generated render that
is never parsed back. Everything mutates except `operation='get'`, and `dry_run=true` builds and
validates and returns `rendered`/`diff`/`wouldLose` **without** writing — the preview before
adopting a hand-written `.md`. Master (`kind:"master"`) documents use `set_subtask` /
`remove_subtask` / `set_section`; `remove_subtask` also deletes the leaf doc (json+md) unless
`subtask.keep_file`; every step operation is leaf-only. Since 260831-LOCR-L33 the description spells
the **step plane** out by intent, because `operation` is a plain `str` and the vocabulary is the only
place the split exists: `set_step` updates exactly one existing unit and never creates; `add_step`
creates exactly one and requires `{id, title}`, refusing an id that already exists in its scope;
`remove_step` deletes exactly one and requires a nonblank `step.reason`, records a decision entry, and
**may** remove a `done` unit or operate on a `Completed` document once that reason is given;
`read_steps` is the read-only focused checklist read; and all of them address one exact existing unit
by `step={id, parent?}`, where `parent` selects the namespace. `skip_step` takes an exact existing step and a nonblank
reason, marks only that unit done, records intentional-skip provenance, and does not cascade; an
explicit status clears an earlier skip disposition cit:(["operation: 'create'", "exact existing step", "sets only that unit done", "records intentional-skip provenance without cascading", "A nonblank reason is required.", "explicit status clears an earlier skip disposition"], mcp/src/agents_remember/mcp/registration/tasks.py:121-121; mcp/src/agents_remember/mcp/registration/tasks.py:137-137; mcp/src/agents_remember/mcp/registration/tasks.py:143-144).

Since 260815-DAG-L11 the docstring also spells out the graph operation:
`author_execution_graph` applies one
validated atomic batch of typed mutations (`add_node`/`remove_node`/`add_edge`/`remove_edge`/
`move_leaf`/`set_nature`) to a sprint's `executionGraph` — segment-addressed by sampling
leaf ids, with judgment-bearing mutations requiring a `judgmentId` row in the sprint's Judgment
Register (the mechanism never invents one), typed refusals for segment-on-atomic and incomplete
partitions, and unplaced-leaf placements plus numbering inversions reported as facts. Since
260815-DAG-L13 the first `add_node` batch on a graph-less sprint bootstraps the graph (the result
reports `bootstrapped: true`), sprint creation scaffolds the empty canonical Judgment and Priority
Register sections, and a `set_section` carrying a canonical register heading must keep the exact
register table shape (write-time validation). Since 260815-DAG-L14 the docstring also spells
out the sprint linkage operations: `attach_master` writes the typed `masterRef` row, the
`orchestrates` slug, and — only on a graphed sprint — the lump graph node as one validated atomic
batch (a nature-less master requires `executionNature` + a `judgmentId` from the sprint Judgment
Register; graph-less sprints report `graphNode: deferred-no-graph-default`); `detach_master`
removes the typed row, membership slug, and graph node, refusing while any edge touches the node
and never deleting files; `linkage_report` surfaces seat-doc rows, slug-only membership,
row/membership mismatches, and uncommanded masters as facts, and `get` on a sprint carries the
same `linkageFacts`. The description also lists `retire_master` and states its contract in plain words:
it is the only route that archives a master, with or without a sprint, and finalizing a master never archives
it. `fields={masterRef, reason, removeEdges?}`. Called on a sprint it removes the master's membership, graph
nodes and touching edges, keeps a plain abandoned row with a typed proof (reason, time, recovery data), then
archives the folder and runs the review-artifact archive hook; outgoing edges to unfinished successors need
their exact endpoints in `removeEdges`. Called on a master that no sprint commands (`masterRef` is that master and
there is no `removeEdges`), it edits no sprint, writes its proof to `notes/reports/master-retirement.json` and moves
the folder under `0_archive/`. Open enclosures and unfinished operations refuse with their cleanup route; a sprint's
only graphed master cannot be retired because a graph cannot be empty; a master nested inside another task's folder
is refused because only root task folders have a `0_archive/<name>` location. `dry_run` previews each change and the
hook's effect, repeating the same request resumes after an interruption, and when the hook failed in part
(`ok=false`, `state: retired-with-hook-failures`) the repeat retries the cleanup only. The description also says an
`abandoned` row never blocks a master's closeout, and that a finalized master a sprint commands stays in place with
its sprint row `Completed`.

The body splits that into two objects: `TaskDocTarget(repo_id, task_name, contract_path, slug)` —
which document to edit — and `TaskDocEdit(fields, step, decision, subtask, section)` — what the edit
is. `operation` and `dry_run` stay separate arguments; since 260815-DAG-L16 the registered `task_doc`
also exposes `branch_addressed` (policy-gated direct-execution opt-in for `record_route_review`,
bound to the task-root series contract — L16-R6). A read (`operation='get'`) leaves every edit
slot unset.

`lifecycle_finalize_task` packs its three document arguments into `FinalizeTaskDocs(task_doc_path,
master_doc_path, subtask_number)` and keeps `dry_run` and `teardown_providers` separate. Its
docstring states the terminal semantics: the task's landed commit must be reachable from the
contract's local target/source branch — a PR-gated flow must complete the merge and pull first, so
the proof is structurally identical to a non-PR edge — and no squash-merge equivalence is attempted.
Since 260928-MIK-L38 (MIK-R38; ruling 2026-09-30T12:33:07 Q3) the docstring also says the finalizer
derives and reconciles the leaf's exact row when the leaf declares an existing immediate parent "or names
none and its folder's task.json master lists it", and (review R1 note 5, ruling 13:11:32) that "a sub-task
naming none whose folder task.json is not a master is refused". The refusal names a sub-task, not a leaf,
by ruling 14:12:52 (review R2's wording note): a `light` task that is its own `task.json` finalizes
standalone and is not covered by it. The same clauses are in `docs/reference/mcp-tools.md` and the c-09
skill. No argument, schema or response model changed.

`task_reopen(contract_path, dry_run)` is a state reset, not a worktree creator: it returns the
enclosure contract's review/closeout/integration state to virgin and the leaf's task document to
planning, under the **exact same leaf id** (no `-rN` suffix). It refuses masters, in-flight leaves,
and leaves whose worktrees still exist; afterwards the normal `worktree_start` with the same leaf id
recreates everything.

### Invariants And Boundaries

- Flat signature; `TaskDocTarget` / `TaskDocEdit` / `FinalizeTaskDocs` are built in the body.
- `task_doc` is mutating except `get`, and registers `dry_run=False`.
- **The operation vocabulary lives only in the description text.** `operation` is a plain `str`, not
  an enum and not a schema member, so adding or changing an operation is a description edit and
  nothing else — the 260831-LOCR-L33 step-plane change touched this module's description only, with
  no schema, `PUBLIC_TOOLS`, or response-model change. A reader looking for the operation set in the
  types will not find it here.
- Document schema validation, master/leaf rules, and the reopen refusals live in
  `application/task_doc_tools.py` and `application/worktree_tools.py`.

## Evidence

### Repo-Internal References

- The `task_doc` / `task_reopen` payload builders. [1]
- The finalize description: the folder-master row and the sub-task refusal (MIK-R38). [2]
- The finalize builder. [3]
- `FinalizeTaskDocs`. [4]

- The `task_doc` description names `retire_master` as the only route that archives a master and states its two forms, its refusals and its retry rule. [5]

## Historical 260815-DAG-L3 Queue Registration (Superseded)

L3 originally registered a mutable durable queue with blocker, claim, certification, and lane-owner
state. CLIVE final retired that command model. The surviving `closeout_queue` registration is strict
status/rebuild over a disposable projection; canonical intent lives in `closeout_door`, and claimed
operation state lives in the lifecycle journal. Caller authorization remains explicit but cannot
turn a projection row into lifecycle authority.

## 260815-DAG Master Full-Gate Repair

The `task_doc` tool's long docstring moved to the module-level `_TASK_DOC_TOOL_DESCRIPTION` constant, passed through `@server.tool(description=...)` (wire-contract conformance); the import of `task_doc_tools` follows the move to `application/task_docs/`. The registered tool surface is unchanged.

## 260821-CLIVE Door, Projection, And Discard Registration

This registrar exposes `closeout_door` as the canonical declare/status/defer/resume/withdraw/
update-provenance surface and describes `closeout_queue` as status/rebuild for a disposable
waiting-door projection only. Successful door publication refreshes projections after the short
task CAS is released; waiting-to-claimed transfer remains owned by closeout apply. `task_doc`
documents `discard-unstarted` as a reasoned, evidence-gated planning discard that atomically removes
child JSON/Markdown and retains a typed parent audit; started or ambiguous evidence routes to the
real lifecycle action rather than pretending completion.

## MCAR-L02 Curator-Coherence Registration

`register_task_tools` now advertises one nested-request `curator_coherence` tool with
`status`/`prepare`/`publish`/`validate` actions. Its contract makes the structured stable manifest
canonical, keeps semantic revision/attempt/digest identities separate, requires explicit
`code:`/`memory:`/`task:` evidence references for exact candidate judgments, and names the shared
validator used by memory and closeout. It explicitly forbids historical-filename fallback.

**The description now names every field `publish` requires (260918-TSIP-L3, `T50`).** The enforced
validator (`models/lifecycles/curator_coherence.py:294-328` `_action_has_one_input_shape`) needs
**nine** non-null fields: `semantic_requirement_revision`, `delivery_attempt`,
`expected_predecessor_digest`, `expected_code_candidate_tree`, `expected_memory_candidate_tree`,
`expected_task_topology_fingerprint`, `expected_task_intent`, `expected_attestation_sha256` and
`caller`. The published text named the identity classes `prepare` returns and never marked
`semantic_requirement_revision` or `delivery_attempt` as required, so a caller could satisfy
everything the registered contract named and still be refused. The text now names all nine, says
`status`/`prepare`/`validate` forbid them, and the refusal names the absent ones — **the description
is load-bearing here because the JSON schema cannot carry the constraint**: the request model marks
only `action` and `contract_path` required, since the requirement is conditional on
`action == "publish"`. Pinned in `mcp/tests/test_tools.py` (`CuratorCoherencePublishContractTests`)
against both surfaces at once.

## 260918-TSIP-L4 — The `task_doc` Description Stops Advertising `'light'` (`T43`)

The `_TASK_DOC_TOOL_DESCRIPTION` constant's `kind` clause now reads
`kind ['subTask'|'master'] (the former 'light' kind is refused)` (**`:126-127`**), replacing the
stale `kind ['light'|'subTask'|'master']`. Net `+1` from the old `:127`, so every line at or below
the old `:127` moved `+1` (the `skip_step` vocabulary citation into this file moved
`:119-141 → :119-142` and was re-derived in the same pass).

The tool itself had refused `light` since the light-task removal; only the *published* description
still advertised it, so the surface and the behaviour disagreed in the direction this master
exists to find — a capability refused by a surface that still advertises it (`D13`'s class,
reversed). The pin is taken from the **registered** FastMCP surface
(`TOOL_REGISTRARS` → the real `task_doc` description), not from this constant, by
`mcp/tests/test_tool_response_conformance.py::test_task_doc_description_and_refusal_name_the_same_kind_vocabulary`.
