# mcp/src/agents_remember/application/worktree_status.py

## Governing Overview

[application overview](overview.md)

## Purpose

`worktree_status.py` projects an optional `c-09-git-worktree-manager` worktree contract and its
stable enclosure-root sync journal into the read-only worktree summary used by context packets.

## Code Commentary

`worktree_status_packet()` returns inactive, missing-contract, or invalid-contract
states without mutating Git. For valid contracts it delegates to
`git_worktree_manager.status_payload()` and maps the result into the compact
context-facing worktree shape. The projection no longer preserves the full
manager payload as `rawStatus`; `WorktreeSummary` owns the explicit context
fields.

After the canonical lifecycle locator resolves, the packet observes
`.lifecycle/sync-operation.json` from the locator's stable `worktree_group` **before** reading the
contract. The resulting typed `SyncOperationProjection` is preserved in valid-contract packets,
locator decisions, unreadable-contract decisions, and missing/invalid-contract packets. A broken or
deleted task contract therefore cannot erase retained conflict, continuation/cancellation, terminal,
or quarantine evidence. Observation is read-only and contract-addressed; this route does not inspect
task prose or closeout queue rows to reconstruct sync state.

### 260731-EFA-L4: the projection *returns* the model instead of a dict to validate

`worktree_status_packet(contract_path) -> WorktreeSummary`. It used to return
`dict[str, Any]` for `application/context_packet.py` to `model_validate`, and that `Any` is what
let a value the state machine emits and the model rejects survive every type check right up to
packet construction — where the resulting pydantic `ValidationError` escaped the
`@server.tool()` handler, because nothing on the path catches one. All four returns are now
`WorktreeSummary(...)` constructor calls (`inactive`, `missingContract`, `invalidContract`, and the
`active` projection), and `context_packet.py` assigns `worktree=worktree_status_packet(...)`
directly with a comment saying why it is not `model_validate`d — every other summary on that packet
still is.

`_packet_from_status_payload` is renamed **`_summary_from_status_payload`** and typed
`(payload: WorktreeStatusPayload) -> WorktreeSummary`, importing the `TypedDict` from
`modules.guidance`. Field by field it assigns from a producer that declares the same vocabulary the
field does, so the checker now sits on the seam.

**Three keys are now omitted rather than defaulted, and this is a deliberate wire change.**
`nextTool`, `nextArgs` and `nextRequiredArgs` are read with plain `.get(...)` — no default — because
`next_guidance` writes each key only when there is something to say, and the `done` phases have no
next tool at all. The old projection substituted `""` / `{}` / `[]`, which invented a `nextTool`
value no producer declares and the wire vocabulary rejects. The model fields are optional and the
packet is dumped with `exclude_none`, so absence is the shape. An absent `nextRequiredArgs` means
exactly what `[]` meant — the next call needs nothing beyond `nextArgs` — and there is no third
state to confuse it with. `test_wire_vocabulary_exhaustiveness.py::ContractBoundaryTests` pins the
omission so it cannot move again unannounced.

`unknownContractCells` is the one new field: `payload.get("unknown_contract_cells")`, present only
when `worktree_contract._vocabulary_cell` had to substitute for a token the file carried that its
vocabulary does not hold.

CCR-R25 extends only the read-only series status projection. After the lifecycle locator and
contract have been read, a series contract is passed to `atomic_series_status_projection` and
validated as `AtomicSeriesActivationFact`; leaf packets retain the existing null field. The
projection reports the address, source-pair fingerprint, selected record, state, and read error
facts without publishing, repairing, or selecting activation state. `_summary_from_status_payload`
threads that typed fact into `WorktreeSummary` alongside the stable sync and lifecycle projections.

**`invalidContract` narrowed in meaning without its code changing.** The `except ContractError`
branch now catches only documents that are not contracts at all — no front matter, an unrecognised
schema, a missing required field, an external-memory contract with no memory repository. A cell
whose *value* is off-vocabulary no longer reaches it: the reader substitutes the declared fallback
and reports the raw token through `unknownContractCells`. Refusing those here would have made the
packet honest about a task that `worktree_closeout_apply`, `worktree_integrate`,
`worktree_cleanup`, `worktree_sync` and `worktree_abandon` had all simultaneously stopped being
able to touch.

## Invariants And Boundaries

- This module is read-only; it must not create, close out, integrate, or clean
  worktrees.
- Contract parsing failures should become structured packet state rather than
  escaping context packet construction.
- Stable sync-operation evidence must survive contract read failure and remain present on every
  summary path once the lifecycle locator establishes the enclosure root.
- Context packets expose typed lifecycle and next-operation hints, not shell
  command strings or raw manager payloads.
- **Build the model here; do not hand the caller a dict to validate.** The whole point of the
  return type is that a producer/model mismatch is a pyright error at this seam rather than a
  `ValidationError` at packet-build time, in a handler with no `except`.
- Absent next-move keys stay absent. Do not reintroduce a `""` / `{}` / `[]` default for
  `nextTool` / `nextArgs` / `nextRequiredArgs` — a value this projection invents is by definition
  one no producer declares.

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

### Repo-Internal References

- Status observes the stable sync journal before contract parsing and threads it through all result branches. [1]
- The journal observer returns a typed projection without reading task or queue state. [2]
- `SyncOperationProjection` is an explicit optional field on the context-facing worktree model. [3]
- Worktree lifecycle status and next hints are composed by the worktree manager. [4]
- Worktree summary model constrains the context-facing shape, including the optional series activation fact. [5]
- Worktree summary model constrains the context-facing shape, including the optional series activation fact. [6]
- Context packet assembly consumes this read-only worktree projection — assigned directly, no longer `model_validate`d. [7]
- `WorktreeStatusPayload` (the `TypedDict` this projection consumes) and the phase/next-move vocabularies it is checked against (declared in `models/worktree.py` since L9). [8]
- `_vocabulary_cell` substitutes unknown vocabulary tokens and `WorktreeContract.unknown_cells` retains the raw diagnostics. [9]
- The summary maps unknown_contract_cells and the optional atomic-series activation fact onto the typed response. [10]
- The public status projection, including the terminal archive-ready branch whose next move is now enforced downstream. [11]
- The envelope that declares the three keys this projector writes, and the `PUBLIC_TOOLS` membership validator that now refuses an out-of-roster next move. [12]
- The suite that reaches the archive-ready state through this module's real `worktree_status_payload` call and pins the emitted next move against the real tool signatures. [13]
- `ContractBoundaryTests` pins the omitted next-move keys and the whole projection against the contracts on disk. [14]

### Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned status projection.

## Series-Contract Notes

Status packets mirror the leaf enclosure identity fields from `guidance.status_payload`, including `enclosurePath`, `leafId`, and `kind`.

## L23 Lineage In Context Packets

`_summary_from_status_payload` validates optional snake-case lineage facts into
`SourceLineageProjection`. Context packets therefore expose the same strict
ancestry evidence as status rather than copying or re-deriving Git state.

## L23 Lifecycle Model Package Review

`LifecycleOperationProjection` now comes from `models.lifecycles.operation`, the dedicated owner
created by the model package split. Status construction and source-lineage projection semantics are
unchanged.

## 260821-CLIVE-L2 Current Contract

The current source seams include `worktree_status_packet`. Status locates normal lifecycle state through locator -> immutable root manifest -> journal and projects legal controls. Its degraded unreadable/pre-adoption decisions are explicit read-only behavior, not a fallback mutation reader.

### Reconciled Source Evidence

- The current module exposes `worktree_status_packet` at this ownership boundary. [15]

## Current Landed Composition

`project_contract_status` also owns the public status projection. A proven terminal archive projects cleanup-completed or archive-ready with exact accepted cleanup arguments and no live operation rows; malformed terminal-archive evidence returns its typed refusal. Other paths resolve caller authority, project readable or unreadable lifecycle evidence, and replace the plural operation list. This remains read-only.

## 260831-LOCR-L32 The Terminal Next Move Is Enforced Downstream

`_project_terminal_contract_status`
cit:([`_project_terminal_contract_status`], mcp/src/agents_remember/application/worktree_status.py:463-505) writes a next-move triple into the `worktree_status`
payload: `nextAction`, `nextTool` (from `TerminalCleanupOperation`, i.e. `worktree_cleanup` or
`worktree_abandon`) and `nextArgs` (the accepted cleanup arguments plus `contract_path` and
`dry_run`). **That write is now typed and enforced**, at the single validation point every public tool
response crosses — `TOOL_RESPONSE_MODELS["worktree_status"].model_validate(payload)`.

- `models/worktree.py::WorktreeCommandResponse` declares the three keys
  cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400), and
  cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-400), and
  `WorktreeStatusResponse` inherits them. Before this leaf the envelope resolved to
  `FlexibleResponseModel` (`extra="allow"`) and declared none of them, so the triple rode through as
  an unchecked extra: `worktree_abandon` reached the wire without ever being a `NextTool` member, and
  `model_validate({"ok": True, "nextTool": "not_a_tool"})` succeeded.
- `WorktreeCommandResponse._require_registered_public_next_tool`
  cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442) now refuses any
  cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442) now refuses any
  `nextTool` outside `PUBLIC_TOOLS` with `nextTool must name a registered public tool`.

Two things are worth stating plainly, because earlier accounts of this seam got them wrong and one
may still be found elsewhere:

1. **The emitted guidance was always correct.** The args the projector writes match the real tool
   signatures, so retrying the named tool was — and is — the right resume action. The defect was
   missing typing and missing enforcement, not wrong guidance. Nothing in this module's projection
   behavior changed for this leaf: **this route is unchanged by 260831-LOCR-L32**; the change is
   entirely in the model it validates into.
2. **`WorktreeSummary` is never on this path.** It is constructed only here, in
   `worktree_status_packet`'s own helpers for the `context_packet` surface, so its single-value
   `nextAction: Literal["developer-decision"] | None` stays honest and must not be widened.

**The rule is per surface.** The worktree surface's next move must name a registered *public* tool;
the `task_doc` surface may name a non-public one (`session_retire`). That is why the invariant lives on
`WorktreeCommandResponse` and not on the shared flexible envelope, and why widening `PUBLIC_TOOLS` would
be the wrong fix. `mcp/tests/test_worktree_status_terminal_next_tool.py` drives this module's real
`worktree_status_payload` into the archive-ready state for both cleanup verbs and pins all of it.
