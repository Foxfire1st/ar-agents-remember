# mcp/src/agents_remember/mcp/tools/base.py

| Field                  | Value                                          |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                             |
| path                   | `mcp/src/agents_remember/mcp/tools/base.py`    |
| doc_type               | `file-level-onboarding`                        |
| lastUpdated |  2026-09-18T14:55+02:00 |
| lastVerifiedCommitHash | `0dd04d6adbca3e8ba61849b605ece3137005829e` |
| lastVerifiedCommitDate | 2026-09-18T15:05:30+02:00|
| governingOverview      | `overview.md`                                  |

## Governing Overview

[MCP tools overview](overview.md)

## Purpose

Owns the one shared response-finalization adapter, and **re-exports** the advertised MCP tool-name
tuple from its single definition in `models`.

## Code Commentary

The module is 24 lines. It declares `TRANSPORT`, an empty `RESERVED_TOOLS`, `__all__`, and
`_tool_payload` — and defines nothing else. `PUBLIC_TOOLS` is imported at L14 and declared as an
export by `__all__` at L19.

### Logic

**`PUBLIC_TOOLS` is no longer defined here (260831-LOCR-L32).** The exact ordered tuple now
lives at `mcp/src/agents_remember/models/tools/public_roster.py` — 62 names at L32, **63** since
260831-LOCR-L37 added `worktree_pause`, extent `L22-L86`; L14 imports it and L19's
`__all__` declares the re-export, because this is not an `__init__.py` (where ruff exempts the `X as
X` idiom) and a bare import would otherwise read as unused. The object is identical — same tuple,
same order, and 62 unique names at the time of the move — so
`agents_remember.mcp.tools.base.PUBLIC_TOOLS` still resolves the same object and every existing
consumer is unchanged. The later membership change (63 names) was made in the roster leaf and the
worktree registrar together.

The relocation is what made the roster readable from `models`: a `models → mcp` import is a
`layers.toml` violation (models = 2, mcp = 22; the `mcp` charter forbids any import from below), a
function-local import trips `ruff PLC0415` with suppressions forbidden in this repository, and
module-level imports in either direction are circular. `models/worktree.py` now reads the roster to
enforce the worktree surface's next-move vocabulary; the roster's own card records why.

Structural agent operations are
`dispatch_agent`, `retire_child`, `rename_child`, `rename_self`, `message_parent`, and
`message_child`; structural gate names remain `lifecycle_gate`, `gate_decide`, and `gate_list`.
Removed exact-id/leaf-address agent tools are absent. `_tool_payload`
cit:([`_tool_payload`], mcp/src/agents_remember/mcp/tools/base.py:22-24) passes every
application result through `application/tool_response.py::complete_tool_response`.

### Conventions

Live registration and the public response-model registry must match the advertised tuple exactly.
Order is part of the advertisement contract; set-only parity is insufficient. A change to the roster
is a change to `models/tools/public_roster.py`, never a second tuple here.

### Invariants And Boundaries

- **This module re-exports the roster; it does not own it.** Do not re-declare `PUBLIC_TOOLS` here,
  and do not add a derived copy — the single definition is what keeps `mcp.tools.base.PUBLIC_TOOLS`
  and the model-layer reader the same object.
- Public tool names cannot restore session/lifecycle/inbox/gate-id cognition.
- Structural operations use document+role vocabulary.
- Every public result passes the common response finalizer.
- Reserved tools are empty.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The advertised tuple names the structural public surface, and is now defined in the `models` leaf. | `PUBLIC_TOOLS` | mcp/src/agents_remember/models/tools/public_roster.py:22-85 |
| The adapter re-exports the roster through `__all__` instead of declaring its own copy. | "__all__ = [\"PUBLIC_TOOLS\", \"RESERVED_TOOLS\", \"TRANSPORT\"]" | mcp/src/agents_remember/mcp/tools/base.py:19-19 |
| The live registration is compared to this tuple, in order, by the inventory suite. | `PublicSurfaceInventoryTests` | mcp/tests/test_tools.py:222-283 |
| The shared adapter finalizes one application result. | `_tool_payload` | mcp/src/agents_remember/mcp/tools/base.py:22-24 |
| Registrars are the only published declaration family. | `TOOL_REGISTRARS` | mcp/src/agents_remember/mcp/registration/__init__.py:36-49 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## 260815-DAG-L3 Public Tool Census

`closeout_queue` is now part of `PUBLIC_TOOLS`, so registry parity, response conformance, and common
envelope/next-step behavior treat it as a real public MCP surface rather than an internal helper.

## 260821-CLIVE-L2 Current Contract

The current source seams include the module-level vocabulary. The public schema/composition layer exposes task-addressed controls plus explicit legacy and enclosure-adoption routes without private operation ids. Registration and payload building do not own journal state or compatibility decisions.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared protocol vocabulary declares stdio transport. | "TRANSPORT =" | mcp/src/agents_remember/mcp/tools/base.py:16-16 |
| The public tool-name tuple's one definition, moved out of this adapter by 260831-LOCR-L32. | "PUBLIC_TOOLS = (" | mcp/src/agents_remember/models/tools/public_roster.py:22-22 |
| The reserved-tool tuple is explicitly empty. | "RESERVED_TOOLS: tuple[str, ...] = ()" | mcp/src/agents_remember/mcp/tools/base.py:17-17 |
| The protocol adapter delegates response completion to the application boundary. | "def _tool_payload(" | mcp/src/agents_remember/mcp/tools/base.py:22-22 |

## 260821-CLIVE Public Tool Census

`closeout_door` joins the canonical public tool-name set used by response-envelope validation.
This is an additive public surface with its own strict response model; it is not an internal
compatibility name and does not change token/envelope finalization for existing tools.

## MCAR-L02 Public Tool Inventory

`PUBLIC_TOOLS` includes exactly one `curator_coherence` name. Status, preparation, publication, and
validation remain actions of that tool rather than four overlapping public tools.

## 260831-CCR-L15 Status-Wait Public Tool

The public tool census `PUBLIC_TOOLS` adds `worktree_status_wait`, so the
read-only lifecycle status-change wait is part of the public tool inventory enforced by the
conformance suite.

## 260831-LOCR-L29 Public-Inventory Repair — The Self-Referential Test

`PUBLIC_TOOLS` gained `worktree_record_landing` immediately after `worktree_integrate`, so the tuple
again named every tool the server advertises and held 61 entries at that leaf (62 since
260831-LOCR-L30 added the checkpoint landing route).

The gap was not cosmetic. `mcp/registration/closeout.py` registered the tool and FastMCP published
it, while this tuple and `models/tools/tool_registry.py` both omitted it — and
`finalize_tool_response` indexes that registry by tool name, so the advertised tool raised instead
of returning a payload. Nothing exercised the invariant this card states. `mcp/public_surface.py`
compares a live `list_tools()` result against this tuple, and `mcp/registration/__init__.py`
documents that FastMCP publishes in registration order, but the only test comparing them built its
list FROM `PUBLIC_TOOLS`: `server_info` reports `list(PUBLIC_TOOLS)` (`mcp/tools/core.py`), so the
comparison was self-referential and a registered-but-unlisted tool was invisible to a fully green
suite.

`PublicSurfaceInventoryTests` (`mcp/tests/test_tools.py`) closes the hole. It registers every entry
in `TOOL_REGISTRARS` against a probe `FastMCP` and asserts the live `list_tools()` names equal this
tuple in order, then asserts the advertised names have validating response models. Order is part of
the comparison because publication follows registration order, so a misplaced row is a reordering
bug rather than a missing one. Do not replace this with an assertion against `server_info`: that
payload is this tuple, and comparing a tuple to itself is the failure mode the repair removed.

## 260831-LOCR-L30 Checkpoint Landing Joins The Census

`PUBLIC_TOOLS` gained `worktree_checkpoint_landing` immediately after `worktree_integrate`, so the
tuple again names every tool the server advertises and holds **62** entries. The same change register
the name in `mcp/registration/closeout.py`, in `models/tools/tool_registry.py::TOOL_RESPONSE_MODELS`,
and in `models/worktree.py::WorktreeCheckpointLandingResponse`.

This is the three-registry rule the L29 repair established, exercised a second time by construction
rather than by repair: a public tool needs the advertised tuple, the by-name response-model registry,
**and** its envelope model, and missing any one of them leaves the tool published but unable to
answer. `mcp/tests/test_tools.py::PublicSurfaceInventoryTests` now drives a validating
`finalize_tool_response` call for the checkpoint name as well, because the set comparison alone
cannot tell the two landing tools apart — they sit next to each other in the registry and their
payloads differ only in the operation literal, so a swap would still pass a set check.

## 260831-LOCR-L32 The Roster Moves To `models` — This Card Is Now A Re-Export

`PUBLIC_TOOLS` left this module. The 62-name tuple's one definition is now
`mcp/src/agents_remember/models/tools/public_roster.py:22-85`, a zero-import `models` leaf; this
module imports it at L14 and declares the re-export through `__all__` at L19, so
`mcp.tools.base.PUBLIC_TOOLS` resolves the same object and every consumer, the `public_surface` pin,
and `PUBLIC_TOOL_RESPONSE_MODELS` are unchanged. This file shrank from 79 lines to **24**:
`TRANSPORT` moved L9 → L16, `RESERVED_TOOLS` L74 → L17, and `_tool_payload` L77-L79 → L22-L24.

**Why it moved — this is the point of the change, not a tidy-up.** The roster living in `mcp` is
precisely why the worktree next-move vocabulary could not be enforced at the model boundary.
`application/worktree_status.py::_project_terminal_contract_status` writes `nextAction` / `nextTool` /
`nextArgs` into the payload validated once against `WorktreeStatusResponse`, whose envelope declared
none of them under `extra="allow"`, so the values crossed the wire verbatim and unchecked. Enforcing
that vocabulary requires `models/worktree.py` to read `PUBLIC_TOOLS`, and from `mcp` that read is
unwritable: `models → mcp` is a `layers.toml` violation (models = 2, mcp = 22; the `mcp` charter
forbids any import from below), a function-local import trips `ruff PLC0415` and suppressions are
forbidden here, and module-level imports in either direction are circular. Moving the tuple to a
zero-import `models` leaf makes the check *expressible* instead of special-cased, and matches
`layers.toml`'s own doctrine that wire vocabulary is defined in `models` and imported by the decider.
The layering checker returned to its exact baseline of 16 violations, with no `models → mcp` edge and
no new cycle.

**The dated entries below describe the tuple at their own leaf.** They remain accurate history — the
names, counts and registry rules they record still hold — but the roster's *location* in each of them
is `mcp/tools/base.py`. Read them as history; read the roster's current home from
`models/tools/public_roster.py`. Where one of them says the `base.py` tuple "is the authority on the
advertised name set", that now means the re-exported object, which is the same object.

## Update History
- 2026-09-18T14:55+02:00 — 260918-TSIP-L3 curator (citation repair, `ar/260918-tsip-l3-ar`, base `a12c511f`): `PublicSurfaceInventoryTests` was repointed `:220-281 → :222-283`. The claim's wording was re-read against the new bytes and is unchanged — only the range moved, because this leaf's edit to `mcp/tests/test_tools.py` inserted lines above it. `lastUpdated` advances with this repair; `lastVerifiedCommitHash` is deliberately unchanged because the candidate is uncommitted and the governed closeout owns the real code commit.
- 2026-09-12T22:55+02:00 — 260831-LOCR-L32 curator: **`PUBLIC_TOOLS` moved out of this module.** The
  tuple's one definition is now `models/tools/public_roster.py:22-85`; this card's Purpose, Code
  Commentary, Conventions, invariants and reference rows are rewritten to describe a 24-line
  re-export (L14 import, L19 `__all__`) instead of the definition site, this file's `TRANSPORT`,
  `RESERVED_TOOLS` and `_tool_payload` ranges are re-derived to L16 / L17 / L22-L24, and the new
  section records why the move was needed (the `models → mcp` layering violation, the unwritable
  `PLC0415` local import, and the circular module-level imports that blocked the worktree next-move
  check). Also removed a stale Code Commentary sentence that claimed L23 exported
  `worktree_operation_cancel` as a public tool: L23 is now the body of `_tool_payload`, and that name
  is not in the roster. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T20:53:11+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:22-24. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "RESERVED_TOOLS: tuple[str, ...] = ()" repointed to mcp/src/agents_remember/mcp/tools/base.py:17-17. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T20:53:11+00:00: Generated citation repair: "def _tool_payload(" repointed to mcp/src/agents_remember/mcp/tools/base.py:22-22. No content impact: mechanical anchor-range projection bound to citation source snapshot cbb452b5d35b5c1c088ad26c07bb5da009aa64032684a124b62b2b598ff0be0a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: `PUBLIC_TOOLS` grew to 62 with
  `worktree_checkpoint_landing` immediately after `worktree_integrate`, and recorded the
  three-registry requirement plus the new per-tool response-model case. Re-derived this card's
  reference ranges. Verification metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T23:44:56+00:00: Generated citation repair: "RESERVED_TOOLS: tuple[str, ...] = ()" repointed to mcp/src/agents_remember/mcp/tools/base.py:73-73. No content impact: mechanical anchor-range projection bound to citation source snapshot fc36bf81fd36002f552f72a34a44e9713fa47fc86ced6632de3215e5011793d3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:44:56+00:00: Generated citation repair: "def _tool_payload(" repointed to mcp/src/agents_remember/mcp/tools/base.py:76-76. No content impact: mechanical anchor-range projection bound to citation source snapshot fc36bf81fd36002f552f72a34a44e9713fa47fc86ced6632de3215e5011793d3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T01:41:08+02:00 — 260831-LOCR-L29 public-surface repair: added `worktree_record_landing`
  to the advertised tuple immediately after `worktree_integrate`, corrected the census prose from
  the stale 63-name claim to the measured 61 names, recorded why the missing row was invisible
  (`server_info` reports `PUBLIC_TOOLS` itself, so the only comparison was self-referential), and
  added the reference row for the inventory suite that now executes the invariant. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:75-77. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "RESERVED_TOOLS: tuple[str, ...] = ()" repointed to mcp/src/agents_remember/mcp/tools/base.py:72-72. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "def _tool_payload(" repointed to mcp/src/agents_remember/mcp/tools/base.py:75-75. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-05T08:46+02:00 — L31 scoped MCP curator: reviewed 1 declined citation claim against frozen code `ea35964985f30080488270e71ac81657ac40682b`. Separated constant vocabulary from the response-finalization function, including the moved reserved tuple. Existing verification hash/date are retained; this scoped source read and citation repair do not certify the entire card or a gate.
- 2026-09-05T06:24:16+00:00: Generated citation repair: `_tool_payload` repointed to mcp/src/agents_remember/mcp/tools/base.py:79-81. No content impact: mechanical anchor-range projection bound to citation source snapshot ad34c1284f637cc2e60117d5a156ddfdd2236402d2c1332758dd691c2cbef881; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec (lifecycle status-change waiting): recorded `worktree_status_wait` in the `PUBLIC_TOOLS` census.
- 2026-08-30T15:15:36+02:00 — 260821-ARSPAWN-L4: corrected the current public census to 63 and
  recorded exact-order parity as the permanent advertisement contract. Verification remains
  closeout-owned.

- 2026-08-29T08:52+02:00 — Added the one curator-coherence tool name to the public inventory.
  Verification remains closeout-owned.

- 2026-08-24T15:04+02:00 — Cumulative CLIVE curation: added the canonical closeout-door name to the documented public census. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16: `PUBLIC_TOOLS` advertises `direct_landing` (59 names);
  `_tool_payload` behavior unchanged. Verified at code commit a9d50e08.


- 2026-08-15T09:10+02:00 — L3 content update: added closeout_queue to the canonical public tool
  census; verification remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator body review: reconciled this card with the exact current source delta described above; verification provenance remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current MCP-tool card for `base.py` with structural tool exposure and control-plane ownership boundaries.
- 2026-08-04T11:34:10+02:00 — 260731-EFA-L6 S18-B12 curator: split the base-tool ownership record across the payload entry point, response finalizer/lifecycle tail, envelope models, registrar loop/tuple, and supervisor-banner root; the scoped fixer will generate citation ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: `base.py` itself is unchanged by this leaf, but two
  of its claims pointed at `server.py` for tool registration, which moved wholesale to
  `mcp/registration/`. Repointed the `PUBLIC_TOOLS` invariant and the reference row; nothing else
  touched.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep, R5, issue #15): `_tool_payload` now
  attaches `finalized["supervisorBanner"]` when the supervisor heartbeat has gone stale past
  `DEFAULT_SUPERVISOR_STALE_CUTOFF_SECONDS`, via `supervisor_heartbeat.agent_notifier_staleness_banner`
  and `amb.root`; exception-contained at the call site, silent when the supervisor has never ticked.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-08T02:43+02:00 — 260707-HFX-L8: `PUBLIC_TOOLS` now advertises `session_retire` and
  `session_rename` right after `spawn_agent_session`; `_tool_payload` behavior is unchanged.
  Verification metadata pinned until closeout stamps the HFX-L8 commit.
- 2026-07-04T12:31+02:00 - L3: `PUBLIC_TOOLS` now advertises
  `orchestration_nudge_manager`; `_tool_payload` behavior is unchanged.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-07-04T11:10+02:00 — L2: `PUBLIC_TOOLS` now advertises `spawn_agent_session` (the agent-facing
  dispatch tool) right after `attach_terminal_session_to_leaf`; `_tool_payload` behavior is unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-03T00:30+02:00 — L11 advertises `task_reopen` in PUBLIC_TOOLS next to `task_doc`.
- 2026-07-02T17:04+02:00 — L9: `PUBLIC_TOOLS` now advertises
  `attach_terminal_session_to_leaf`, the agent-facing hosted chat/terminal leaf reassignment tool.
  `_tool_payload` behavior is unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE turn end): `PUBLIC_TOOLS` grew to 51 with `lifecycle_turn_end_notification`, and `_tool_payload` gained the awaiting-developer auto-dismiss — after `emit_tool`, when `amb.current.state == "awaiting-developer"` and `tool_name != "lifecycle_turn_end_notification"`, it calls `amb.resume_from_await()` so the next AR tool call resumes the parked lifecycle to `running` (notification = stop, not stall). The tool-name guard is load-bearing: the notification flows through the same choke point in the call that parked the lifecycle, so without it the notification would self-dismiss. The auto-dismiss runs between `emit_tool` and the task-27 next-step attachment. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T18:43+02:00 — Task 27: after `amb.emit_tool(...)`, `_tool_payload` now attaches `finalized["nextStep"] = next_step_for(amb, tool_name)` (new top-level `from .next_step import next_step_for`) when non-`None`, so the single response choke point carries both the slice-2b emission hook and an engine-computed next-step hint for every in-lifecycle tool, with no per-tool wiring. `next_step_for` is exception-contained. New collaborator `mcp/src/agents_remember/mcp/tools/next_step.py`.
- 2026-06-26T14:16+02:00 — Task 25: `PUBLIC_TOOLS` now advertises `lifecycle_gate` and no longer advertises `lifecycle_block`, `gate_create`, `gate_wait`, or `gate_response_wait`; `_tool_payload` validates against `TOOL_RESPONSE_MODELS` so retained compatibility builders still keep strict response contracts.
- 2026-06-25T07:17+02:00 — Task 19: `PUBLIC_TOOLS` grew to 52 with `gate_response_wait`; `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the task-19 code commit.
- 2026-06-23T22:50+02:00 — Dashboard task 14: `PUBLIC_TOOLS` grew to 51 with `lifecycle_finalize_task`; `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the source commit.
- 2026-06-23T13:44+02:00 — Task 10 backend inbox: `PUBLIC_TOOLS` grew to 50 with `operator_inbox_post`, `operator_inbox_poll`, and `operator_inbox_consume`; `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the task-10 code commit.
- 2026-06-18T01:05+02:00 — Task 6 slice 6a: `PUBLIC_TOOLS` grew to 47 with the control-plane gate tools (`gate_create`/`gate_decide`/`gate_wait`/`gate_list`); `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the 6a code commit.
- 2026-06-13T22:34 — Slice 3c commit 1: `PUBLIC_TOOLS` grew to 43 with the `task_doc` authoring tool; `_tool_payload` is unchanged. Verification metadata pinned until closeout stamps the 3c commit-1 code commit.
- 2026-06-13T16:41+02:00 — Slice 2b: `PUBLIC_TOOLS` grew to 42 with the six `lifecycle_*` signal tools, and `_tool_payload` now calls `ambient().emit_tool(...)` so every tool call is attributed to the active lifecycle by construction. Verification metadata pinned until closeout stamps the 2b code commit.
- 2026-06-11T06:47+02:00 — Removed `direct_closeout_preview`/`direct_closeout_apply` from `PUBLIC_TOOLS` (issue #62 worktree-only closeout); tuple is now 36 names (the earlier "37" count was itself stale — the tuple held 38 before this removal).
- 2026-06-10T09:56+02:00 — Registered `worktree_sync` in `PUBLIC_TOOLS` (GitHub #54 sub-task D); tuple is now 37 names.
- 2026-06-01T20:45+02:00 — Registered `worktree_abandon` in `PUBLIC_TOOLS` so its response is validated like every other public tool.
- 2026-05-30T22:29+02:00: Documented that `_tool_payload` now finalizes token-accounting metadata via `finalize_payload_tokens` (S6 wiring), making it the single point that populates `tokens`/`tokenizer`/`tokenCountExact` on every MCP response. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-29T18:35+02:00: Created when `mcp/tools.py` was split into the `mcp/tools/` package (commit `01f503d`); holds the `_tool_payload`/`PUBLIC_TOOLS` contract previously documented in `tools.py.md`.
