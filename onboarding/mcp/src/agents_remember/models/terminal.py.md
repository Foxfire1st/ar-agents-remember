# mcp/src/agents_remember/models/terminal.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/models/terminal.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-08-01T09:48+02:00 |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`|
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[models overview](overview.md)

## Purpose

`terminal.py` defines strict Pydantic response contracts for MCP tools that expose dashboard
terminal-session catalog operations. It models the hosted-chat/terminal leaf reassignment tool from L9 and
— since L2 — the agent-facing `spawn_agent_session` dispatch tool.

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

cit:([`TaskAssignmentStatus`], mcp/src/agents_remember/models/terminal.py:20-29) is the closed response vocabulary for document-owned seat assignment attempts: `attached`, `seat-taken`, `unknown-session`, `role-required`, and explicit task-binding/document validation refusals. The operation accepts structural document-and-role intent; it does not expose a leaf-key or occupant-id address.
cit:([`AttachTerminalSessionToTaskResponse`], mcp/src/agents_remember/models/terminal.py:32-44) is a strict `ToolResponse` with operation `attach_terminal_session_to_task`, the requested session and `taskDocumentRef`, the optional previous document binding and seat role, an optional conflict owner for administrative diagnostics, and optional refusal detail.

cit:([`SpawnAgentSessionStatus`], mcp/src/agents_remember/models/terminal.py:43-69) is the L2 vocabulary: `spawned-unbriefed` (the only `ok: true`
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
cit:([`SpawnAgentSessionResponse`], mcp/src/agents_remember/models/terminal.py:78-120) is a strict
`ToolResponse` with operation `spawn_agent_session`, the `session`, optional `harness`/`kind`/`leafKey`/
`label`/`cwd`/`tmuxName`, the spawned-by provenance (`spawnedBySession` + `spawnedByLifecycle`) recorded
on the catalog row for the dashboard orchestration tree, the optional `spawnRole` (under L14, the
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
(cit:([`SessionRetireStatus`], mcp/src/agents_remember/models/terminal.py:149-155)) `= Literal["retired","already-retired","unknown-session","unknown-actor","retire-refused"]`;
cit:([`SessionRetireResponse`], mcp/src/agents_remember/models/terminal.py:160-176) models `session_retire` (issue #12): `operation: Literal["session_retire"]`,
`status`, `session`, and the four retirement provenance fields
`retiredAt`/`retiredBySession`/`retiredReason`/`retiredEdge` (all `None`-default, populated on
success/already-retired), plus `detail` (populated on `retire-refused`, naming the exact
authority-policy clause `check_retire_authority` raised). `ok` is true for `retired`/
`already-retired` (idempotent), false for every refusal status — and that rule lives in ONE place,
cit:([`_RETIRE_OK_STATUSES`], mcp/src/agents_remember/application/terminal_tools.py:977-977), so a refusal status added later cannot
arrive as `ok=True` from a call site that forgot it. cit:([`SessionRenameStatus`], mcp/src/agents_remember/models/terminal.py:186-186) `=
Literal["renamed","unknown-session"]`; `SessionRenameResponse` models `session_rename` (issue #4):
cit:([`SessionRenameResponse`], mcp/src/agents_remember/models/terminal.py:186-197)
`operation: Literal["session_rename"]`, `status`, `session`, `label`/`spawnedLabel` (`None`-default).
Identity text only — `spawn_role` (the L6 role-seat-immutability field) never appears in this
response because a rename never touches it.

### Conventions

**The status vocabularies are declared HERE, and the tool imports them — the ownership direction
is inverted on purpose**. Everywhere else in the
package a wire model imports its producer's alias; here that would close an import cycle,
because `mcp.tools.base` → `models.tool_registry` → `models.terminal` is an existing edge and a
`models.terminal` → `mcp.tools.terminal` import would complete the loop. The invariant the fix is
actually for is ONE declaration, not a particular module owning it, so the aliases stay in this
file and `mcp/tools/terminal.py` annotates its status seams with them: `_spawn_refusal(status:
SpawnAgentSessionStatus, …)`, `_retire_payload(status: SessionRetireStatus, …)`, the rename
payload, and the spawn preflight check table. cit:([`_spawn_refusal`, `_retire_payload`, `_RETIRE_OK_STATUSES`], mcp/src/agents_remember/application/terminal_tools.py:928-953; mcp/src/agents_remember/application/terminal_tools.py:970-970; mcp/src/agents_remember/application/terminal_tools.py:973-1008) cit:([`session_rename_payload`, `spawn_agent_session_payload`], mcp/src/agents_remember/mcp/tools/terminal.py:46-63; mcp/src/agents_remember/mcp/tools/terminal.py:86-95) A refusal status
the tool invents is therefore a pyright error at the tool rather than a `ValidationError`
escaping the MCP handler.

The task-assignment contract is declared independently from the legacy leaf-ref refusal alias: cit:([`TaskAssignmentStatus`, `SpawnAgentSessionStatus`], mcp/src/agents_remember/models/terminal.py:20-29; mcp/src/agents_remember/models/terminal.py:47-78). Document assignment failures name task-document validation; spawn retains its own broader refusal vocabulary.

Each of the three tool-facing vocabularies also publishes its runtime half, derived from the
alias by `get_args` rather than retyped beside it: cit:([`VALID_SPAWN_AGENT_SESSION_STATUSES`], mcp/src/agents_remember/models/terminal.py:80-82),
cit:([`VALID_SESSION_RETIRE_STATUSES`], mcp/src/agents_remember/models/terminal.py:161-163), cit:([`VALID_SESSION_RENAME_STATUSES`], mcp/src/agents_remember/models/terminal.py:187-189).
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
  `mcp.tools.base` → `models.tool_registry` → `models.terminal` cycle.
- `LeafRefStatus` belongs to `worktrees.leaf_refs`; its two members are folded in by reference,
  never copied. `Literal` flattens nested aliases, so folding changes nothing on the wire.
- The `VALID_*` frozensets must stay derived by `get_args` from their alias, never listed
  separately.
- Nullable fields default to `None` so `_tool_payload(..., exclude_none=True)` can omit absent
  previous-owner/conflict data without failing validation.
- `ok` and token metadata come from the inherited `ToolResponse` envelope.

### Todos

No known follow-up in this file.

## Docs References

No relevant external/domain documentation found; this is an internal response contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| The response fields are defined by the document-and-role assignment contract. | `TaskAssignmentStatus`; `AttachTerminalSessionToTaskResponse` | mcp/src/agents_remember/models/terminal.py:20-29; mcp/src/agents_remember/models/terminal.py:32-44 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The administrative attach payload builder returns the exact task-document-and-role fields modeled here. | `attach_terminal_session_to_task_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:27-44 |
| The application tool imports and annotates the terminal aliases across spawn, refusal, retire, rename, and status seams. | `_knob_refusal`; `_spawn_refusal`; `_RETIRE_OK_STATUSES`; `_retire_payload`; `_rename_payload` | mcp/src/agents_remember/application/terminal_tools.py:452-470; mcp/src/agents_remember/application/terminal_tools.py:928-953; mcp/src/agents_remember/application/terminal_tools.py:970-970; mcp/src/agents_remember/application/terminal_tools.py:973-1008; mcp/src/agents_remember/application/terminal_tools.py:1145-1166 |
| The MCP tool wrappers import the modeled spawn, retire, and rename payload aliases. | `spawn_agent_session_payload`; `session_retire_payload`; `session_rename_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:46-63; mcp/src/agents_remember/mcp/tools/terminal.py:66-83; mcp/src/agents_remember/mcp/tools/terminal.py:86-95 |
| `LeafRefStatus` declares the two leaf-ref refusal members; `LeafRefResolutionError` produces those statuses, and `VALID_LEAF_REF_STATUSES` derives the runtime set from the alias. | "LeafRefStatus = Literal["; "class LeafRefResolutionError"; "VALID_LEAF_REF_STATUSES" | mcp/src/agents_remember/models/terminal.py:18-18; mcp/src/agents_remember/worktrees/leaf_refs.py:26-26; mcp/src/agents_remember/worktrees/leaf_refs.py:39-39 |
| The response registry maps `attach_terminal_session_to_task` and `spawn_agent_session` to these strict models. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:140-212 |
| Conformance coverage includes a representative missing-session (attach) and legacy-caller-harness (spawn) refusal payload for the models. | `ToolResponseConformanceTests` | mcp/tests/test_tool_response_conformance.py:639-734 |
| `session_retire_payload`/`session_rename_payload` return the exact fields modeled by `SessionRetireResponse`/`SessionRenameResponse`, including the `already-retired` idempotent fast-path and the `retire-refused` authority-policy detail. | `session_retire_tool`; `session_rename_tool` | mcp/src/agents_remember/application/terminal_tools.py:1011-1080; mcp/src/agents_remember/application/terminal_tools.py:1169-1183 |
| The response registry maps `session_retire`/`session_rename` to these strict models. | `TOOL_RESPONSE_MODELS` | mcp/src/agents_remember/models/tool_registry.py:116-179 |
| `test_every_spawn_status_the_tool_can_return_validates` / `..._retire_status_...` / `..._rename_status_...` assert produced == declared for each of the three `VALID_*` sets. | `ProducedLiteralTests` | mcp/tests/test_wire_vocabulary_exhaustiveness.py:632-817 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| The model validates a local MCP response and has no external boundary. | - | - |

## 260712-TRH-L4 Final Candidate

This sidecar was reviewed against the final uncommitted L4 candidate. The source now participates in the explicit spawned-unbriefed → harness-ready → briefed flow; dispatch proof remains exact-session, copy-mode-aware, harness-log-confirmed, and pending without respawn when proof is absent. Catalog writers are fully serialized across one read/body/write transaction while atomic readers remain lock-free.

### 260713-PHA-L5 Reviewed Hosted Cutover Impact

Reviewed this file against the accepted hosted-session cutover and PASS verdict. Its relevant
contract now follows exact adapter evidence for readiness, delivery, liveness, or interactions;
legacy/custom sessions are unsupported, pane/log classifiers are diagnostics-only, and durable
inbox acceptance remains distinct from explicit consumption where applicable.

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.
- 2026-08-04T13:25:51+02:00 — 260731-EFA-L6 S18-B01 same-reviewer semantic-binding repair: bound the leaf-ref alias, producer, and derived runtime set to their owning source under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-08-02T16:44:03+02:00 — W1-B07 curator: repaired 16 repository-reference citations (16/16 anchored and sourced; scoped citation check clean).

- 2026-08-01T09:48+02:00 — 260731-EFA-L4 curator: body corrected. The Conventions section said
  "the model duplicates the status literal locally rather than importing the serving helper" —
  true as far as the serving helper goes, but it framed local declaration as the whole convention,
  and this file is now the one place in the package where the vocabulary-ownership direction is
  deliberately INVERTED: the aliases stay here and `mcp/tools/terminal.py` imports them because
  `mcp.tools.base` → `models.tool_registry` → `models.terminal` is an existing
  import edge and the natural direction would close a cycle. Recorded that, the tool-side seams
  now annotated with the aliases (`_spawn_refusal`, `_retire_payload`, rename,
  preflight table), the three derived `VALID_*` frozensets
  and the exhaustiveness assertions over them, plus the `_RETIRE_OK_STATUSES` L834 single-place
  `ok` rule. `LeafRefStatus` is now imported from `worktrees.leaf_refs` and folded into
  the historical leaf-assignment and spawn vocabularies instead of the two members
  being typed out in both. L19 later replaced that assignment surface with the structural
  `TaskAssignmentStatus` document contract while spawn retained its own vocabulary.
  cit:(["TaskAssignmentStatus = Literal[", "SpawnAgentSessionStatus = Literal["], mcp/src/agents_remember/models/terminal.py:20-29; mcp/src/agents_remember/models/terminal.py:47-78)
  Two pre-existing body errors found while checking the historical vocabularies against the
  source and fixed: the assignment enumeration omitted `role-required` (added in
  HFX2-L17, described later in this same card), and `SpawnAgentSessionStatus` was described as
  having `spawned` as "the only `ok: true` case" — the success status is `spawned-unbriefed`
  (`_spawned_payload` L768-L773 there, the only `ok: True`), while `brief-delivery-separate` is a
  refusal of the retired one-call brief contract. Added four invariants. Citations: two stale
  ranges repaired — the registry row read L82-L88; L111-L114 and the rows are at L121/L122 and
  L124/L125; the conformance row read L88-L107 and the representative attach/spawn payloads are
  at the corrected payload ranges (the former range is now `_write_json`/`_run_git`/`_write_leaf_task`). The self-citation
  row was re-pointed to `LeafAssignmentStatus` / `AttachTerminalSessionToLeafResponse`, every
  status alias and response class gained a range, and rows were added for `leaf_refs.py`, the
  tool-side seams, and the exhaustiveness suite. Verification
  metadata pinned until closeout stamps the L4 commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented the additive
  `launch-selection-invalid` status, resolved-selection provenance, and the user-authored-only
  `sessionCommands` boundary. Verification metadata remains pinned until closeout stamps the L2
  code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed hosted cutover impact and refreshed the body.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: modeled current/previous seat identity and the
  role-required attach refusal without overloading the transport-role compatibility field.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: added replacement-leaf, resolved-knob, and bound-log
  provenance fields and corrected delivery field semantics to log evidence. Verification metadata
  remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-09T12:04+02:00 — 260707-HFX2-L10 (spawn settings authority):
  `SpawnAgentSessionStatus` gained `spend-override-unsupported`, the pre-spawn refusal for legacy
  caller spend fields and maintained harness-native spend env keys. Response shape otherwise stays
  additive/strict. Verification metadata pinned until closeout stamps the 260707-HFX2-L10 commit.

- 2026-07-08T02:43+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state):
  added `SessionRetireStatus`/`SessionRetireResponse` (issue #12) and `SessionRenameStatus`/
  `SessionRenameResponse` (issue #4) — both strict `ToolResponse` subclasses following the existing
  local-status-literal convention. `SessionRetireResponse` carries the four retirement provenance
  fields (`retiredAt`/`retiredBySession`/`retiredReason`/`retiredEdge`) plus `detail` for the
  authority-refusal case; `SessionRenameResponse` carries `label`/`spawnedLabel` only — identity
  text, never `spawn_role`. Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-07T22:15+02:00 — 260707-HFX-L3 (capture-verified delivery): `SpawnAgentSessionResponse`
  gained `deliveryCapture` (`str | None = None`) — the final pane capture attached whenever any
  delivery outcome reports `False`, absent on full success — and the delivery-field comments now
  state the capture-verified contract. Additive; omitted when `None`. Verification metadata pinned
  until closeout stamps the HFX-L3 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: terminal response models gained the strict leaf-ref refusal
  statuses (`leaf-ref-not-found` / `leaf-ref-ambiguous`), and attach responses gained optional `detail`
  for resolver errors. Verification metadata pinned until closeout stamps the 260707-HFX-L4 commit.
- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): `SpawnAgentSessionStatus` gained the
  pre-spawn refusals `effort-invalid` / `model-invalid` / `level-invalid`;
  `SpawnAgentSessionResponse` gained the free-form spawn provenance (`launchArgs` /
  `promptKeywords` / `sessionCommands` / `sessionCommandsDelivered`) and the level provenance
  (`spawnLevel` / `spawnLevelSource`) — all additive `None`-default fields omitted when absent.
  Verification metadata pinned until closeout stamps the L16 commit.

- 2026-07-06T23:58:30+02:00 — 260703-L14 (visual hierarchy + chat grouping): `SpawnAgentSessionResponse`
  gained the optional `spawnRole` field (`str | None = None`) mirroring the new catalog column —
  additive, omitted from payloads when the spawn carried no AR_SPAWN_ROLE.
  Verification metadata pinned until closeout stamps the L14 commit.
- 2026-07-04T11:10+02:00 — L2: added `SpawnAgentSessionStatus` + the strict `SpawnAgentSessionResponse`
  contract for the agent-facing `spawn_agent_session` dispatch tool (spawned-by provenance,
  context-delivery outcome, and the server-arbitrated `leaf-taken` / pre-spawn refusal statuses). Follows
  the existing strict `ToolResponse` pattern. Verification metadata pinned until closeout stamps the L2
  commit.
- 2026-07-02T17:04+02:00 — L9: created the strict `AttachTerminalSessionToLeafResponse` contract for
  the agent-facing terminal leaf reassignment tool. Verification metadata pinned to the task base until
  closeout stamps the L9 commit.
