# mcp/src/agents_remember/worktrees/status.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/worktrees/status.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:24+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`status.py` projects an optional `c-09-git-worktree-manager` skill worktree contract into the read-only
worktree summary used by context packets.

## Code Commentary

`worktree_status_packet()` returns inactive, missing-contract, or invalid-contract
states without mutating Git. For valid contracts it delegates to
`git_worktree_manager.status_payload()` and maps the result into the compact
context-facing worktree shape. The projection no longer preserves the full
manager payload as `rawStatus`; `WorktreeSummary` owns the explicit context
fields.

### 260731-EFA-L4: the projection *returns* the model instead of a dict to validate

`worktree_status_packet(contract_path) -> WorktreeSummary`. It used to return
`dict[str, Any]` for `controllers/context_packet.py` to `model_validate`, and that `Any` is what
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
- Context packets expose typed lifecycle and next-operation hints, not shell
  command strings or raw manager payloads.
- **Build the model here; do not hand the caller a dict to validate.** The whole point of the
  return type is that a producer/model mismatch is a pyright error at this seam rather than a
  `ValidationError` at packet-build time, in a handler with no `except`.
- Absent next-move keys stay absent. Do not reintroduce a `""` / `{}` / `[]` default for
  `nextTool` / `nextArgs` / `nextRequiredArgs` — a value this projection invents is by definition
  one no producer declares.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree lifecycle status and next hints are composed by the worktree manager. | [git_worktree_manager.py](agents-remember/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Worktree summary model constrains the context-facing shape. | [worktree.py](agents-remember/mcp/src/agents_remember/models/worktree.py) |
| Context packet assembly consumes this read-only worktree projection — assigned directly, no longer `model_validate`d. | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |
| `WorktreeStatusPayload` (the `TypedDict` this projection consumes) and the phase/next-move vocabularies it is checked against. | [modules/guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py) |
| `_vocabulary_cell` and `WorktreeContract.unknown_cells`, the source of `unknownContractCells`. | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py) |
| `ContractBoundaryTests` pins the omitted next-move keys and the whole projection against the contracts on disk. | [test_wire_vocabulary_exhaustiveness.py](agents-remember/mcp/tests/test_wire_vocabulary_exhaustiveness.py) |

## Series-Contract Notes

Status packets mirror the leaf enclosure identity fields from `guidance.status_payload`, including `enclosurePath`, `leafId`, and `kind`.

## Update History

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
