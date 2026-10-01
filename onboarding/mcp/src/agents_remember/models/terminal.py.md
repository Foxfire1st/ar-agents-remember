# mcp/src/agents_remember/models/terminal.py

## Governing Overview

[models overview](overview.md)

## Purpose

`terminal.py` defines strict Pydantic response contracts for MCP tools that expose dashboard
terminal-session catalog operations. It models the hosted-chat/terminal task-assignment tool and
the internal `spawn_agent_session` primitive used beneath the one public `dispatch_agent` surface;
the response model does not make that primitive a caller-facing tool.

## Code Commentary

### 260714-ACPUI-L2 Launch Response Contract

`SpawnAgentSessionStatus` adds `launch-selection-invalid` for an incomplete settings-resolved
native launch. `resolvedModel` and `resolvedEffort` continue to expose the resolved selection in
the response and catalog provenance. The free-form `sessionCommands` field now explicitly means
user-authored launch configuration only: the dispatch path never synthesizes normalized
model/effort into it. Dynamic catalog failures after the structural preflight remain control-runner
failure evidence rather than additional pre-spawn enum values.

### 260707-HFX2-L17 Response Contract

Attach responses add `role-required`, `seatRole`, and `previousSeatRole`; spawn responses add
`seatRole`. The existing `role` field remains the transport kind (`chat`/`terminal`) for
compatibility and must not be confused with orchestration binding identity.

### Logic

**260707-HFX2-L15 response provenance.** `SpawnAgentSessionResponse` now exposes
`replacementForLeaf`, `resolvedModel`, `resolvedEffort`, `sessionLogEntryId`, and
`sessionLogPath`. `contextDelivered` means the id-bearing user record exists in the bound harness
log; `sessionCommandsDelivered` means command record plus non-error stdout, not pane rendering.

cit:([`TaskAssignmentStatus`], mcp/src/agents_remember/models/terminal.py:22-31) is the closed response vocabulary for document-owned seat assignment attempts: `attached`, `seat-taken`, `unknown-session`, `role-required`, and explicit task-binding/document validation refusals. The operation accepts structural document-and-role intent; it does not expose a leaf-key or occupant-id address.
cit:([`AttachTerminalSessionToTaskResponse`], mcp/src/agents_remember/models/terminal.py:34-46) is a strict `ToolResponse` with operation `attach_terminal_session_to_task`, the requested session and `taskDocumentRef`, the optional previous document binding and seat role, an optional conflict owner for administrative diagnostics, and optional refusal detail.

cit:([`SpawnAgentSessionStatus`], mcp/src/agents_remember/models/terminal.py:53-89) is the L2 vocabulary: `spawned-unbriefed` (the only `ok: true`
case — the seat exists and is bound, and its brief is a separate delivery),
`brief-delivery-separate` (the refusal of the retired one-call brief contract, raised before any
settings, catalog or spawn work when the caller passed `context` or `submit=true`), `leaf-taken`
(the server-arbitrated refusal, never overridden), and the pre-spawn validation refusals
`spend-override-unsupported` (HFX2-L10 — a caller supplied legacy spend fields, direct
launch/session controls, namespaced spawn model/effort env, or a maintained harness-native spend env
key), `harness-unknown` / `harness-not-detected` / `effort-invalid` (under L16, effort outside the
resolved harness's vocabulary, or any effort for a mapping-less settings-defined harness) /
`model-invalid` (under L16, a model knob for a settings-defined harness with no modelFlag) /
`level-invalid` (under L16, a dispatch level outside leaf|master|portfolio) / `bad-kind`. The HFX-L4
leaf-ref refusals are also modeled for spawn because a bad leaf key is refused before tmux or
catalog mutation — and, like `LeafAssignmentStatus`, they arrive as the imported `LeafRefStatus`
alias rather than as two more hand-typed strings.

**`capsule-unavailable` (260915-CAPS-L15)** is the vocabulary's newest member, and it is the
instruction-delivery half of the launch: the seat **is** role-configured and its capsule could not be
supplied — no compilable capsule for the role, no verified instruction channel on the harness the
launch resolved, or a process composed without a compiler. It is refused before any host side effect,
with the exact stage and role named in the detail, because a session that would run without
instructions is never started. It joins the pre-spawn validation refusals above: like them it is a
*decision* the launch point makes, not a failure of the process it was about to start. No member was
removed or re-spelled to make room for it.
cit:([`SpawnAgentSessionResponse`], mcp/src/agents_remember/models/terminal.py:98-157) is a strict
`ToolResponse` with operation `spawn_agent_session`, the `session`, optional `harness`/`kind`/`leafKey`/
`label`/`cwd`/`tmuxName`, the spawned-by provenance (`spawnedBySession` + `spawnedByLifecycle`, and — since
260821-ARSPAWN-L1 — `spawnedByKind`: `Literal["plane","ambient","unattributed"] | None`, the
caller-kind provenance the public `dispatch_agent` sets by caller kind) recorded
on the catalog row for the dashboard orchestration tree, the reviewer ownership pair
`structuralParentTaskDocumentRef` + `structuralParentRole` (the plane-owned parent address, distinct
from occupant ancestry), the optional `spawnRole` (under L14, the
`AR_SPAWN_ROLE` persisted on the row, the Chats command-tree grouping key), the L16 level provenance
(`spawnLevel` + `spawnLevelSource` — the resolved dispatch level and whether it was explicit or
defaulted), the L16 free-form spawn provenance as recorded on the row (`launchArgs` verbatim argv,
`promptKeywords` prepended to the brief, `sessionCommands` — the RESOLVED post-launch paste list —
plus `sessionCommandsDelivered`, whether every session command was capture-verified AND submitted),
the `ownerSession` set on `leaf-taken`, the context-delivery outcome (`contextDelivered` /
`submitted` — `contextDelivered` is true ONLY after a pane capture proves the payload landed, the
260707-HFX-L3 contract; the SF-1 blind seat was a `true` here over a clean-booted pane), the
`deliveryCapture` loud-failure evidence (the final pane capture, attached whenever any delivery
outcome reports `False`; absent on full success — a blind seat is diagnosed from the payload
itself, never trusted from a bare boolean), and a `detail` for the refusals.

**Seat lifecycle (260707-HFX-L8)** adds two new strict response contracts. `SessionRetireStatus`
(cit:([`SessionRetireStatus`], mcp/src/agents_remember/models/terminal.py:176-182)) `= Literal["retired","already-retired","unknown-session","unknown-actor","retire-refused"]`;
cit:([`SessionRetireResponse`], mcp/src/agents_remember/models/terminal.py:179-195) models `session_retire` (issue #12): `operation: Literal["session_retire"]`,
`status`, `session`, and the four retirement provenance fields
`retiredAt`/`retiredBySession`/`retiredReason`/`retiredEdge` (all `None`-default, populated on
success/already-retired), plus `detail` (populated on `retire-refused`, naming the exact
authority-policy clause `check_retire_authority` raised). `ok` is true for `retired`/
`already-retired` (idempotent), false for every refusal status — and that rule lives in ONE place,
cit:([`_RETIRE_OK_STATUSES`], mcp/src/agents_remember/application/terminal_tools.py:1005-1005), so a refusal status added later cannot
arrive as `ok=True` from a call site that forgot it. cit:([`SessionRenameStatus`], mcp/src/agents_remember/models/terminal.py:217-217) `=
Literal["renamed","unknown-session"]`; `SessionRenameResponse` models `session_rename` (issue #4):
cit:([`SessionRenameResponse`], mcp/src/agents_remember/models/terminal.py:224-235)
`operation: Literal["session_rename"]`, `status`, `session`, `label`/`spawnedLabel` (`None`-default).
Identity text only — `spawn_role` (the L6 role-seat-immutability field) never appears in this
response because a rename never touches it.

### Conventions

**The status vocabularies are declared HERE, and the tool imports them — the ownership direction
is inverted on purpose**. Everywhere else in the
package a wire model imports its producer's alias; here that would close an import cycle,
because `mcp.tools.base` → `models.tools.tool_registry` → `models.terminal` is an existing edge and a
`models.terminal` → `mcp.tools.terminal` import would complete the loop. The invariant the fix is
actually for is ONE declaration, not a particular module owning it, so the aliases stay in this
file and application producers annotate their status seams with them: `spawn_refusal(status:
SpawnAgentSessionStatus, …)` now lives in `terminal_spawn_results.py`, while `_retire_payload(status: SessionRetireStatus, …)`, the rename
payload, and the spawn preflight check table. cit:(["def spawn_refusal("], mcp/src/agents_remember/application/terminal_spawn_results.py:13-31) cit:([`_retire_payload`, `_RETIRE_OK_STATUSES`, `_rename_payload`], mcp/src/agents_remember/application/terminal_tools.py:1005-1005; mcp/src/agents_remember/application/terminal_tools.py:1008-1043; mcp/src/agents_remember/application/terminal_tools.py:1190-1211) cit:([`session_rename_payload`, `spawn_agent_session_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:47-64; mcp/src/agents_remember/mcp/tools/terminal.py:87-96) A refusal status
the tool invents is therefore a pyright error at the tool rather than a `ValidationError`
escaping the MCP handler.

The task-assignment contract is declared independently from the legacy leaf-ref refusal alias: cit:([`TaskAssignmentStatus`, `SpawnAgentSessionStatus`], mcp/src/agents_remember/models/terminal.py:22-31; mcp/src/agents_remember/models/terminal.py:49-80). Document assignment failures name task-document validation; spawn retains its own broader refusal vocabulary.

Each of the three tool-facing vocabularies also publishes its runtime half, derived from the
alias by `get_args` rather than retyped beside it: cit:([`VALID_SPAWN_AGENT_SESSION_STATUSES`], mcp/src/agents_remember/models/terminal.py:93-95),
cit:([`VALID_SESSION_RETIRE_STATUSES`], mcp/src/agents_remember/models/terminal.py:182-184), cit:([`VALID_SESSION_RENAME_STATUSES`], mcp/src/agents_remember/models/terminal.py:219-221).
`test_wire_vocabulary_exhaustiveness` asserts, per tool, that the set of statuses the tool can
actually return *equals* the declared set — a measurement in the other direction too, catching a
member no writer can emit.

This module still does not import the serving helper; the response-model layer stays independent
of serving implementation code.

### Invariants And Boundaries

- This is an AR-owned response shape and should stay strict.
- **One declaration per status vocabulary.** These aliases live here and
  `mcp/tools/terminal.py` imports them; do not re-type a status literal at the payload builder,
  and do not "fix" the direction by importing the tool from this module — that closes the
`mcp.tools.base` → `models.tools.tool_registry` → `models.terminal` cycle.
- `LeafRefStatus` belongs to `worktrees.leaf_refs`; its two members are folded in by reference,
  never copied. `Literal` flattens nested aliases, so folding changes nothing on the wire.
- The `VALID_*` frozensets must stay derived by `get_args` from their alias, never listed
  separately.
- Nullable fields default to `None` so `_tool_payload(..., exclude_none=True)` can omit absent
  previous-owner/conflict data without failing validation.
- `ok` and token metadata come from the inherited `ToolResponse` envelope.
- **The per-run instruction mode is recorded, never inferred from an absent field.** `instructionMode`
  (`dict[str, Any] | None`) carries the launch gate's own compact report — `capsule` with the compiled
  digest, instruction count and byte size, or `legacy` with the named decision — so "ran without
  instructions" is legible on the wire instead of being indistinguishable from "ran correctly". It is
  additive and nullable for the same reason every other optional field here is: an older caller's
  payload is unchanged, and the key is omitted rather than nulled.

### Todos

No known follow-up in this file.

## Evidence

### Docs References

No relevant external/domain documentation found; this is an internal response contract.

- The response fields are defined by the document-and-role assignment contract. [1]

### Repo-Internal References

- The administrative attach payload builder returns the exact task-document-and-role fields modeled here. [2]
- Application producers import and annotate the terminal aliases across the centralized spawn-refusal builder, knob-refusal check, retire result, and rename result seams. [3]
- The MCP tool wrappers import the modeled spawn, retire, and rename payload aliases. [4]
- `LeafRefStatus` declares the two leaf-ref refusal members; `LeafRefResolutionError` produces those statuses, and `VALID_LEAF_REF_STATUSES` derives the runtime set from the alias. [5]
- The response registry maps `attach_terminal_session_to_task` and `spawn_agent_session` to these strict models. [6]
- The declared attach response owns its wire fields; removed conformance fixtures do not establish a current validation pass. [7]
- `session_retire_payload`/`session_rename_payload` return the exact fields modeled by `SessionRetireResponse`/`SessionRenameResponse`, including the `already-retired` idempotent fast-path and the `retire-refused` authority-policy detail. [8]
- The response registry maps `session_retire`/`session_rename` to these strict models. [9]
- The three `VALID_*` sets this module declares are no longer pinned by a produced == declared case: `d3610903` removed the per-set `ProducedLiteralTests` cases when coverage became diagnostic, and `mcp/tests/test_wire_vocabulary_exhaustiveness.py` now keeps only its module docstring and helpers. [10]

### Cross-Repo References

No meaningful cross-repo references found.

The model validates a local MCP response and has no external boundary.

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## L23 Source-Lineage Refusals

Assignment and spawn response models now admit the two fail-closed lineage
statuses and carry the strict projection that explains them. The projection is
optional because ordinary task-binding, launch-selection, and seat outcomes do
not manufacture ancestry evidence.

## 260918-TSIP-L4 — The Stranded-Row Report Declared (`T16`)

`SessionRetireResponse` now declares the three keys the retire payload already emitted:
`strandedRowIds: list[str]` (**`:211`**), `strandedRowCount: int` (**`:212`**) and
`surfacedRowId: str | None` (**`:213`**), with `detail` following at `:214`. The
`from pydantic import Field` import and its blank line at **`:7-8`** move the whole file `+2` from
the old `:6`, and the nine-line comment-and-declaration block at **`:205-213`** moves everything
from the old `:203` by a further `+9` (`SessionRetireResponse` `187 → 189`,
`VALID_SESSION_RENAME_STATUSES` `208 → 219`, `SessionRenameResponse` `213 → 224`; file
**224 → 235 lines**).

`_retire_payload` (`application/terminal_tools.py:1038-1042`) adds them on the success path
whenever `_surface_stranded_rows` surfaced a pending operator-inbox row addressed to the retiring
seat or its lifecycle. They are set *after* the seat is already terminated and the row is already
posted, so without the declaration the caller lost the only report of that row — and a retry
answers `already-retired` and carries none of them. Pinned by
`mcp/tests/test_tool_response_conformance.py::test_session_retire_reports_the_stranded_row_after_the_seat_is_gone`.
