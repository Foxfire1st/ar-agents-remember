# mcp/src/agents_remember/application/worktree_status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/application/worktree_status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-13T11:43+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00 |
| governingOverview      | `overview.md`                              |

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

## Docs References

No Domain Documentation source is configured for this memory root.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Status observes the stable sync journal before contract parsing and threads it through all result branches. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:65-151 |
| The journal observer returns a typed projection without reading task or queue state. | `observe_sync_operation` | mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385 |
| `SyncOperationProjection` is an explicit optional field on the context-facing worktree model. | `SyncOperationProjection` | mcp/src/agents_remember/models/worktree.py:127-140 |
| Worktree lifecycle status and next hints are composed by the worktree manager. | "def lifecycle_guidance("; "def next_guidance(" | mcp/src/agents_remember/worktrees/modules/guidance.py:128-134; mcp/src/agents_remember/worktrees/modules/guidance.py:215-215; mcp/src/agents_remember/worktrees/modules/guidance.py:225-225 |
| Worktree summary model constrains the context-facing shape, including the optional series activation fact. | "class WorktreeSummary" | mcp/src/agents_remember/models/worktree.py:219-273 |
| Context packet assembly consumes this read-only worktree projection — assigned directly, no longer `model_validate`d. | "worktree=worktree_status_packet" | mcp/src/agents_remember/application/context_packet.py:96-96 |
| `WorktreeStatusPayload` (the `TypedDict` this projection consumes) and the phase/next-move vocabularies it is checked against (declared in `models/worktree.py` since L9). | "class WorktreeStatusPayload"; "NextOperation = Literal[" | mcp/src/agents_remember/models/worktree.py:50-50; mcp/src/agents_remember/worktrees/modules/guidance.py:124-124 |
| `_vocabulary_cell` substitutes unknown vocabulary tokens and `WorktreeContract.unknown_cells` retains the raw diagnostics. | "def _vocabulary_cell[Cell: str]("; "unknown_cells: tuple[str" | mcp/src/agents_remember/worktrees/worktree_contract.py:104-104; mcp/src/agents_remember/worktrees/worktree_contract.py:108-108; mcp/src/agents_remember/worktrees/worktree_contract.py:281-281; mcp/src/agents_remember/worktrees/worktree_contract.py:283-283; mcp/src/agents_remember/worktrees/worktree_contract.py:286-286 |
| The summary maps unknown_contract_cells and the optional atomic-series activation fact onto the typed response. | `_summary_from_status_payload` | mcp/src/agents_remember/application/worktree_status.py:217-277 |
| The public status projection, including the terminal archive-ready branch whose next move is now enforced downstream. | `_project_terminal_contract_status` | mcp/src/agents_remember/application/worktree_status.py:463-505 |
| The envelope that declares the three keys this projector writes, and the `PUBLIC_TOOLS` membership validator that now refuses an out-of-roster next move. | "# The next-move triple, declared here so the worktree surface's guidance is part of"; "def _require_registered_public_next_tool" | mcp/src/agents_remember/models/worktree.py:323-323; mcp/src/agents_remember/models/worktree.py:355-364 |
| The suite that reaches the archive-ready state through this module's real `worktree_status_payload` call and pins the emitted next move against the real tool signatures. | `test_archive_ready_status_names_the_accepted_cleanup_operation` | mcp/tests/test_worktree_status_terminal_next_tool.py:192-219 |
| `ContractBoundaryTests` pins the omitted next-move keys and the whole projection against the contracts on disk. | "class ContractBoundaryTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:28-28 |

## Cross-Repo References

No meaningful cross-repository reference applies to this repository-owned status projection.

| Finding | Anchor | Source |
| --- | --- | --- |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The current module exposes `worktree_status_packet` at this ownership boundary. | `worktree_status_packet` | mcp/src/agents_remember/application/worktree_status.py:46-128 |

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
  cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:323-323), and
  `WorktreeStatusResponse` inherits them. Before this leaf the envelope resolved to
  `FlexibleResponseModel` (`extra="allow"`) and declared none of them, so the triple rode through as
  an unchecked extra: `worktree_abandon` reached the wire without ever being a `NextTool` member, and
  `model_validate({"ok": True, "nextTool": "not_a_tool"})` succeeded.
- `WorktreeCommandResponse._require_registered_public_next_tool`
  cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:353-364) now refuses any
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

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: "class WorktreeStatusPayload"; "NextOperation = Literal[" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:124-124; mcp/src/agents_remember/models/worktree.py:50-50. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_project_terminal_contract_status` repointed to mcp/src/agents_remember/application/worktree_status.py:463-505. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_project_terminal_contract_status` repointed to mcp/src/agents_remember/application/worktree_status.py:463-505. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "class WorktreeStatusPayload"; "NextOperation = Literal[" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:124-124; mcp/src/agents_remember/models/worktree.py:50-50. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `next_guidance` in the row 117 of this card from mcp/src/agents_remember/worktrees/modules/guidance.py:225-225 to mcp/src/agents_remember/worktrees/modules/guidance.py:128, the extent of the construct the claim is about (the checker named line(s) [128] as its live location); re-pointed `unknown_cells: tuple[str` in the row 121 of this card from mcp/src/agents_remember/worktrees/worktree_contract.py:104-104 to mcp/src/agents_remember/worktrees/worktree_contract.py:281, the extent of the construct the claim is about (the checker named line(s) [281] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `next_guidance` in the row 117 of this card from mcp/src/agents_remember/worktrees/modules/guidance.py:215-216 to mcp/src/agents_remember/worktrees/modules/guidance.py:128-134, the extent of the construct the claim is about (the checker named line(s) [128] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `lifecycle_guidance` in the row 117 of this card from mcp/src/agents_remember/worktrees/modules/guidance.py:128-134 to mcp/src/agents_remember/worktrees/modules/guidance.py:215-216, the extent of the construct the claim is about (the checker named line(s) [215] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `lifecycle_guidance` in the row 117 of this card from mcp/src/agents_remember/worktrees/modules/guidance.py:130-130 to mcp/src/agents_remember/worktrees/modules/guidance.py:215-216, the extent of the construct the claim is about (the checker named line(s) [215] as its live location); re-pointed `next_guidance` in the row 117 of this card from mcp/src/agents_remember/worktrees/modules/guidance.py:215-216 to mcp/src/agents_remember/worktrees/modules/guidance.py:128-134, the extent of the construct the claim is about (the checker named line(s) [128] as its live location)
- 2026-09-13T14:32+02:00 — Curator citation repoint after the contract-scoped atomic-series activation re-keying shrank `models/worktree.py`: the next-move triple comment now resolves at `models/worktree.py:322-322` and `_require_registered_public_next_tool` at `models/worktree.py:355-364`, so the envelope/validator row was rebound to those ranges. Claim wording unchanged.
- 2026-09-13T12:29:52+00:00: Generated citation repair: "class WorktreeStatusPayload"; "NextOperation = Literal[" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:126-126; mcp/src/agents_remember/models/worktree.py:50-50. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T12:29:52+00:00: Generated citation repair: "# The next-move triple, declared here so the worktree surface's guidance is part of" repointed to mcp/src/agents_remember/models/worktree.py:322-322. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T12:29:52+00:00: Generated citation repair: `_require_registered_public_next_tool` repointed to mcp/src/agents_remember/models/worktree.py:353-364. No content impact: mechanical anchor-range projection bound to citation source snapshot 608ec827a174d194b141ff2daa61dd8e3b6b44611d03fb561dc0b7bb0223223f; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-13T09:43+00:00 -- 260831-LOCR-L34 curator citation review: every claim this card carries was re-read against its cited range in the code worktree; anchors were rebound to the exact literal bytes at the cited location, ranges stale by a line shift were repaired, and claims the generated projection left unsupported were re-cited or re-worded. No verification stamp advanced.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: recorded that this module's terminal-status next
  move (`nextAction` / `nextTool` / `nextArgs` from `_project_terminal_contract_status`) is now typed
  and enforced downstream — declared on `WorktreeCommandResponse` and refused by its
  `PUBLIC_TOOLS` membership validator (`_require_registered_public_next_tool`) — and stated explicitly
  that this route's own
  projection behavior is unchanged by the leaf and that the emitted guidance was always correct. Added
  a per-surface note (`task_doc` may name the non-public `session_retire`; do not widen
  `PUBLIC_TOOLS`) and three reference rows, including the new suite that exercises this module's real
  `worktree_status_payload`. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "class WorktreeStatusPayload"; "NextOperation = Literal[" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:126-126; mcp/src/agents_remember/models/worktree.py:51-51. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: `SyncOperationProjection` repointed to mcp/src/agents_remember/models/worktree.py:127-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:06:15+00:00: Generated citation repair: "class WorktreeStatusPayload"; "NextOperation = Literal[" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:126-126; mcp/src/agents_remember/models/worktree.py:50-50. No content impact: mechanical anchor-range projection bound to citation source snapshot 1740540b8733028dd833a3538d739271e8925ea5f51911a0f8dcd8c49e7e1c13; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: "def _vocabulary_cell[Cell: str](", "unknown_cells: tuple[str" repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:104-104, mcp/src/agents_remember/worktrees/worktree_contract.py:283-283. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `observe_sync_operation` repointed to mcp/src/agents_remember/worktrees/sync_transaction_state.py:369-385. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-10T15:06+02:00 — No content impact: mechanical citation re-derivation after the closeout auto-carry change shifted lines in `sync_transaction.py` / `sync_transaction_state.py`; the cited symbols and their meanings are unchanged.
- 2026-09-08T16:24:06+02:00 — CCR-L38 preparation range refresh: repointed the existing `NextOperation` source coordinate after the frozen model additions. This is a mechanical source-range correction; verification metadata remains closeout-owned.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: documented the read-only `atomicSeriesActivation` status fact and its typed summary mapping from the frozen L38 source. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: "class ContractBoundaryTests(unittest.TestCase):" repointed to mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:28-28. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: "class WorktreeSummary" repointed to mcp/src/agents_remember/models/worktree.py:151-151. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-05T06:24:16+00:00: Generated citation repair: "class WorktreeStatusPayload"; "NextOperation = Literal[" repointed to mcp/src/agents_remember/worktrees/modules/guidance.py:126-126; mcp/src/agents_remember/models/worktree.py:39-39. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for the changed
  status projection card.

- 2026-08-26T03:37+02:00 — Added stable enclosure-root sync-operation projection to every
  locator-established status path, including missing/unreadable contracts. Recorded that journal
  observation is independent of task and queue state. Verification remains
  post-Dagger/closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-13T09:05+02:00 — L23 curator: recorded the operation-projection import move and confirmed
  the status/result contract is otherwise unchanged; final provenance remains closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: recorded strict lineage projection into worktree summaries; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-04T02:20:03+02:00 — 260731-EFA-L6 S18-B06 curator delta: repaired the scoped citations against the frozen source snapshot; generated ranges were inspected and the managed index remained warm/frozen with zero source reads, tokenization, parsing, and build.

- 2026-08-04T01:24:49+02:00 — 260731-EFA-L6 S18-SR2-B06 worker: source-first separated the
  contract reader's unknown-cell definition/retention from this application's actual camel-case
  projection at `_summary_from_status_payload`. Preserved both generated definition ranges and
  added one honest `:1-1` mapping binding; no citation mechanics ran.
- 2026-08-04T00:28:23+02:00 — 260731-EFA-L6 S18-B06 curator: repaired the scoped worktree-status citation claims; final exact frozen-snapshot check is clean.
- 2026-08-03T02:54:53+02:00 — W3-B04 curator: curated 5 table citations (5 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/worktrees/status.py` became `mcp/src/agents_remember/application/worktree_status.py`, so this sidecar moved with it; path metadata, the Purpose file name and `governingOverview` (now the `application/` route overview) follow. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:24+02:00 — 260731-EFA-L4 curator: the card described a projection that "maps the
  result into the compact context-facing worktree shape" and said nothing about what it returns —
  which is now the whole point. `worktree_status_packet` is typed `-> WorktreeSummary` and all four
  returns construct the model (it imports `agents_remember.models.worktree.WorktreeSummary` and no
  longer imports `Any`); `controllers/context_packet.py` assigns it directly and calls no
  `model_validate` on it, unlike every sibling summary on that packet. `_packet_from_status_payload`
  is renamed `_summary_from_status_payload` and signed on `guidance.WorktreeStatusPayload`.
  Recorded the wire change I verified line by line in the projection body: `nextTool`, `nextArgs`
  and `nextRequiredArgs` are now `payload.get(...)` with **no** default where they were
  `.get(..., "")` / `.get(..., {})` / `.get(..., [])`, so with `exclude_none` the keys are omitted
  instead of carrying a value no producer declares; and the new
  `unknownContractCells=payload.get("unknown_contract_cells")` field. Also recorded that the
  `invalidContract` branch narrowed in meaning without its code changing — an off-vocabulary cell
  now degrades in the reader instead of landing here. Added the two invariants that protect both,
  plus three reference rows. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: status packets now include `enclosurePath`, `leafId`, and `kind`, and missing/invalid contract states mirror the explicit enclosure path in their payloads. Verification metadata pinned until closeout stamps the code commit.
- 2026-05-28T19:52+02:00: Updated after context worktree status moved to explicit `WorktreeSummary` fields without raw-status passthrough.
- 2026-05-24T05:03+02:00: Created onboarding after context-packet worktree status projection adopted typed MCP next hints.
