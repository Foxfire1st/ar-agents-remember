# mcp/src/agents_remember/application/next_step.py

| Field                  | Value                                                  |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/application/next_step.py`     |
| doc_type               | `file-level-onboarding`                                |
| lastUpdated            | 2026-08-01T01:15+02:00 |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`             |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                          |

## Governing Overview

Nearest route overview: [overview.md](agents-remember/mcp/src/agents_remember/application/overview.md).

## Purpose

The lifecycle next-step engine (task 27). Computes the single `NextStep` hint
attached to EVERY MCP tool response at the `mcp/tools/base.py::_tool_payload`
choke point, so an agent mid-thread always knows the one next move. It folds the
pre-lifecycle worktree-guidance system into the whole lifecycle spine across two
regimes — a prose-guided non-linear FRONT HALF and a per-tool LINEAR HALF — and
makes a terminal `lifecycle_end` loop back rather than dead-end. Task 28 makes
**NOTIFY-AND-CONTINUE** the ACTIVE turn-end model: at every former gate moment the
ACTIVE hints (the `decide` phase, the `_gate_after` closeout/integration/cleanup
overlays, and the `FRONT_HALF_RUNDOWN`/`_FRONT_HALF_SUMMARY` pointers) now point
the agent at `lifecycle_turn_end_notification` — notify the developer and stop, no
wait — and a new `awaiting-developer` branch returns a no-`nextTool` stop hint
while the lifecycle is parked there. The `lifecycle_gate`/blocked path is PARKED:
still valid if a gate is raised, its `_AWAIT_GATE` await-the-developer pointer at
`lifecycle_resume` stays intact (carrying the chain THROUGH the open gate: raise →
blocked/await → resume → continue), it is simply no longer the hinted route. The
structure mirrors the leaf-26 Lifecycle Flow tab (`dashboard/src/panels/FlowTab.tsx`)
RUNDOWN/LINEAR spec. The hint engine only *advises*; it never fires
`lifecycle_turn_end_notification` or `lifecycle_gate` itself — the agent acts on
the hint.

## Code Commentary

### Logic

Pure core: `compute_next_step(state, contract, tool_name, *, guidance)` →
`NextStep | None`. All inputs are pre-resolved; it does no I/O.

Since 260731-EFA-L2 `compute_next_step` is a four-line dispatcher over one named helper per regime —
`_terminal_step(tool_name)`, `_parked_step(state)`, `_front_half_step(state)`,
`_linear_half_step(tool_name, contract, guidance)` — each carrying the explanatory comment that used
to sit inline. The branch order, the conditions and every returned hint are unchanged; the
descriptions below still hold, they simply live one function down.

Branching:

- `state is None or state.is_terminal` → no active lifecycle. If the just-completed
  `tool_name == "lifecycle_end"`, return the module-level `_LOOP_BACK` constant
  (start fresh with `lifecycle_start`, or `worktree_attach`); otherwise `None`
  (a lifecycle-less response is left unchanged).
- `state.state == "blocked"` → an open gate (the PARKED path). A raised
  `lifecycle_gate` calls `amb.block()` (state → "blocked"), so the only correct
  move is to await the developer's decision and then resume: return the
  module-level `_AWAIT_GATE` constant (`nextTool="lifecycle_resume"`). Checked
  BEFORE the front-half/linear branches — independent of phase/contract since a
  gate can open anywhere — so the open gate is never jumped by the post-gate
  operational step. Task 28 keeps this branch valid but no longer routes the
  active flow through it.
- `state.state == "awaiting-developer"` → the task-28 NOTIFY-AND-CONTINUE turn end
  (the `lifecycle_turn_end_notification` response itself, before the next call
  auto-resumes). Return the module-level `_TURN_HANDED_TO_DEVELOPER` constant —
  `summary` only, **`nextTool=None`** — so the agent stops at its own turn end
  rather than pushing past it. Checked right after the blocked branch.
- `contract is None` → FRONT HALF. Phase `decide` returns a hard-coded hint to
  verify `worktree_start --dry-run` then notify via `lifecycle_turn_end_notification`
  (`nextTool="lifecycle_turn_end_notification"`,
  `nextArgs={"summary":"Ready to open the worktree — your call."}`) and stop. Every
  other front-half phase returns the stable `_FRONT_HALF_SUMMARY` pointer at the
  one-time `FRONT_HALF_RUNDOWN`, now with `nextTool="lifecycle_turn_end_notification"`,
  `nextArgs={"summary":"Plan ready for your review."}`. Task 28 repointed both off
  the parked `lifecycle_gate` (`worktree-intent` / `plan-approval`) hand-offs. Prose
  rather than per-tool because research tools (`read_ar_files`/`grepai`/`cgc`)
  fire unpredictably and `task-file-exists?` is a routing decision, not a tool
  (developer S5 resolution: ride the turn-end notification).
- contract present → LINEAR HALF. First try the `_gate_after` overlay; if it
  returns a hint, use it; otherwise, if `guidance` was supplied, adapt it via
  `_from_guidance`; else `None`.

`_gate_after(tool_name, contract)` is the turn-end overlay at the three former
gate moments, keyed on the just-completed tool + contract sub-state:
`worktree_closeout_preview` && `not approved_for_commit` (commit approval);
`worktree_integrate` && `closeout_status=="completed"` && `integration_status!="completed"`
(integration); `lifecycle_finalize_task` && `integration_status=="completed"`
&& `cleanup!="completed"` (cleanup). At each, task 28 returns a
`lifecycle_turn_end_notification` hint (`nextTool="lifecycle_turn_end_notification"` +
a context `summary`) — notify and stop, no gate, no wait — replacing the prior
`closeout-approval`/`integration-approval`/`cleanup-approval` gate raises. Closeout
uses distinct preview/apply tools, but integrate/finalize reuse one tool with a
`dry_run` arg — so the not-yet-applied contract state (not the args) distinguishes
dry-run from apply.

`_from_guidance(dict)` maps the `lifecycle_guidance` dict onto the shared
`NextStep` shape, defensively coercing types: `summary` via `str(...)`,
`nextOperation`/`nextTool` via `_opt_str` (non-empty `str` else `None`),
`nextArgs` only if it `isinstance(dict)`, `nextRequiredArgs` only if a `list`.

Edge / I/O layer: `next_step_for(amb, tool_name)` cit:([`next_step_for`], mcp/src/agents_remember/application/next_step.py:260-281) → `NextStep | None`.
Reads `amb.current` (the live `LifecycleState`), loads the contract via
`_load_contract`, runs guidance via `_guidance_for`, and **returns
`compute_next_step(...)` directly**. The WHOLE body is wrapped in
`try/except Exception: return None` — `_tool_payload` must never raise into a
tool call, so any failure simply drops the hint.

**Since 260731-EFA-L4 this edge returns the MODEL, not a dump of it.** It used to
end with `step.model_dump(mode="json", exclude_none=True) if step is not None
else None`. The hint is a declared field of the response envelope
(`models.base.ResponseModel.nextStep` / `FlexibleResponseEnvelope.nextStep`), so
serializing it belongs to the choke point's single `model_dump` — dumping it here
is what made the hint a key *written into an already-dumped, already-token-counted
dict*, which is how the advertised token count came to under-report every
in-lifecycle response. `_tool_payload` now assigns `response.nextStep =
next_step_for(amb, tool_name)` and dumps once afterwards. The hint's rendered JSON
is unchanged: the envelope is dumped with the same `mode="json", exclude_none=True`.

cit:([`_load_contract`], mcp/src/agents_remember/application/next_step.py:297-314) looks-before-leaping: `not state.enclosure` →
`None`; `enclosure` path not a file → `None` (the `worktree_start --dry-run`
window where a promoted lifecycle has no contract on disk yet — an EXPECTED state,
front-half fallback); the narrow `try/except` around `load_contract` then catches
only a genuinely torn/unparseable contract (e.g. a racing closeout rewrite) →
`None`.

cit:([`_guidance_for`], mcp/src/agents_remember/application/next_step.py:284-294) returns `None` for `contract is None`, else
`dict(lifecycle_guidance(contract))` with its own `try/except → None`, so a
guidance failure still lets the (contract-independent) `_gate_after` overlay fire.
The `dict(...)` is a deliberate widening (260731-EFA-L4): this hint layer reads
guidance defensively by key (`_from_guidance` coerces every field it takes) and
never re-emits its vocabulary, so it takes the plain payload rather than the
producer's narrower typed shape.

### Conventions

- Pure-core / impure-edge split: `compute_next_step` and helpers `_gate_after`,
  `_from_guidance`, `_opt_str` are pure; `next_step_for`, `_guidance_for`,
  `_load_contract` do I/O at the boundary.
- The active turn-end hint is encoded as
  `nextTool="lifecycle_turn_end_notification"` + `nextArgs={"summary":…}`; the
  parked gate junction is `nextTool="lifecycle_gate"` + `nextArgs={"kind":…}` —
  both reuse the shared `NextStep` vocabulary, not a bespoke field.
- Roadmap strings live as module constants (`FRONT_HALF_RUNDOWN`,
  `_FRONT_HALF_SUMMARY`, `_LOOP_BACK`, `_AWAIT_GATE`, and the task-28
  `_TURN_HANDED_TO_DEVELOPER`) so the front-half, gate-await, and turn-end
  pointers are stable.

### Invariants And Boundaries

- `next_step_for` must NEVER raise into the tool path; broad containment here plus
  narrow containment in the helpers guarantees a failure degrades to "no hint."
- **This edge does not serialize.** `next_step_for` returns `NextStep | None`; the
  one `model_dump` lives at the `_tool_payload` choke point, after the hint has
  been set on the envelope. Do not re-add a `model_dump` here — a separately
  dumped hint is a key outside the response model and outside
  `finalize_payload_tokens`, which is exactly the token under-count 260731-EFA-L4
  removed.
- The engine only HINTS; it must not call `lifecycle_turn_end_notification` or
  `lifecycle_gate`. Human approval moments
  (`closeout`/`integration`/`cleanup`/`plan`/`worktree-intent`) stay
  developer-driven — the agent acts on the hint.
- `state` is threaded through even when `None`/terminal so a terminal
  `lifecycle_end` can still emit `_LOOP_BACK` — the lifecycle is a loop, not a wall.
- An `awaiting-developer` lifecycle (task 28) always yields
  `_TURN_HANDED_TO_DEVELOPER` (`nextTool=None`) — the agent stops at its own turn
  end; the `_tool_payload` choke point auto-resumes on the next AR tool call.
- A `blocked` lifecycle (open gate, parked path) always yields `_AWAIT_GATE` →
  `lifecycle_resume`, never the post-gate operational step — the hint chain runs
  THROUGH the gate (raise → blocked/await → resume → continue), so the gate is
  never silently jumped. Task 28 keeps this valid but un-hinted in the active flow.
- `contract is None` is the canonical FRONT-HALF signal; the dry-run window and a
  torn contract both collapse to it deliberately (never a hard error).
- `NextStep` is a strict model; only `summary` is required, matching the
  prose-only front half.

### Todos

None.

## Docs References

| Source | Relevance |
| --- | --- |
No relevant documentation found after checking live sources.

## Repo-Internal References

`compute_next_step` is invoked from the `_tool_payload` choke point and depends on
the `NextStep` model, the worktree guidance state machine, the contract loader,
and the ambient lifecycle / phase definitions.

| Finding | Anchor | Source |
| --- | --- | --- |
| Choke point that calls `next_step_for` and now SETS `nextStep` on the response model before the single dump, rather than stamping it onto a dumped dict. | `_attach_lifecycle_tail`; `_tool_payload` | mcp/src/agents_remember/application/tool_response.py:34-50; mcp/src/agents_remember/mcp/tools/base.py:77-79 |
| `NextStep` model + the `nextStep` field on the response envelopes — the declaration that makes setting it at the choke point legal. | `NextStep`, `ResponseModel`, `FlexibleResponseEnvelope` | mcp/src/agents_remember/models/base.py:47-63; mcp/src/agents_remember/models/base.py:66-88; mcp/src/agents_remember/models/base.py:97-114 |
| `lifecycle_guidance` state machine delegated to in the linear half; `_guidance_for` widens its payload with `dict(...)`. | `lifecycle_guidance` | mcp/src/agents_remember/worktrees/modules/guidance.py:216-226 |
| `load_contract` / `WorktreeContract` (sub-state fields read by `_gate_after`). | `load_contract`, `WorktreeContract` | mcp/src/agents_remember/worktrees/worktree_contract.py:230-285; mcp/src/agents_remember/worktrees/worktree_contract.py:436-469 |
| `amb.current` — the live `LifecycleState` resolved at the edge. | `AmbientLifecycle` | mcp/src/agents_remember/observer/ambient.py:90-594 |
| `LifecycleState` (`enclosure`, `is_terminal`) + `Phase` literals (`decide`, …) and the `awaiting-developer` state the parked branch reads (state/phase vocabulary in `models/lifecycle.py` since L9). | `LifecycleState`; "LiveState = Literal["; "Phase = Literal[" | mcp/src/agents_remember/models/lifecycles/responses.py:16-16; mcp/src/agents_remember/models/lifecycles/responses.py:20-20; mcp/src/agents_remember/observer/lifecycle_state.py:156-179 |
| Engine tests. | `test_tool_payload_attaches_next_step_and_lifecycle_start_emits_rundown`, `test_advertised_token_count_covers_the_attached_next_step` | mcp/tests/test_next_step.py:298-303; mcp/tests/test_next_step.py:305-317 |

As of HFX-L6, the FRONT_HALF_RUNDOWN reframe bullet names the architect lifecycle explicitly
(`l-01-agent-lifecycles` `roles/architect.md`); the rundown's flow semantics are unchanged — the
front half it describes is now the architect lifecycle's front half, since spawned backend roles
do not own the developer-facing front half.

As of the 260703-L8 remediation the FRONT_HALF_RUNDOWN speaks the event-loop vocabulary: the third item routes the event (no doc → design one; approved + code change → build; no code change → research-only exit; triage may route/spawn/escalate) instead of the retired job-selection table, and the task-file item states the ladder explicitly (task doc → branch → worktree, worktree_start only after the plan gate).

As of cycle 5 the front-half summary speaks event-routing (the last job-selection remnant is gone).

## Cross-Repo References

No meaningful cross-repo references found.

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: source moved from
  `mcp/tools/next_step.py` to `application/next_step.py`; this card moved with
  it, path metadata and the governing-overview link follow. The body already
  tracked the application-source behavior; no content claim changed.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-08-02T23:59:26+02:00 — L6 Wave 2 duplicate-range correction: removed 2 repeated path:start-end Citation objects from 1 same-claim citation group(s) at card line(s) 202; retained the first occurrence/order, all non-repeated anchor coverage and source ranges; scoped non-fixing result 0.
- 2026-08-02T21:10:52+02:00 — 260731-EFA-L6 curator W2-B10: repaired 13 citation findings (5 reference rows and 3 prose pointers); scoped recheck clean.

- 2026-08-01T01:15+02:00 — 260731-EFA-L4 curator: the Logic section said the edge returns "JSON dict
  or `None`" via `step.model_dump(mode="json", exclude_none=True)`. Verified against the diff and
  the current source: cit:([`next_step_for`], mcp/src/agents_remember/application/next_step.py:260-281) is now typed `-> NextStep | None` and returns
  `compute_next_step(...)` directly. Corrected the claim and recorded why it matters — the hint is a
  declared field of the response envelope, so dumping it here is what made it a key written into an
  already-dumped, already-token-counted dict at the `_tool_payload` choke point; the rendered JSON
  is unchanged because the envelope is dumped with the same options. Also recorded the second
  change: cit:([`_guidance_for`], mcp/src/agents_remember/application/next_step.py:284-294) now returns `dict(lifecycle_guidance(contract))`, a
  deliberate widening for a layer that reads guidance defensively by key and never re-emits its
  vocabulary. Added an invariant that this edge does not serialize, line ranges for
  `next_step_for`/`_guidance_for`/`_load_contract`, and citations across the reference table
  (whose header was two columns and is now three).
- 2026-07-31T15:31+02:00 — 260731-EFA-L2: `compute_next_step`'s inline branches were extracted into
  `_terminal_step` / `_parked_step` / `_front_half_step` / `_linear_half_step` to bring the function
  under the now-armed complexity rules. No hint, condition or ordering changed. Verification
  metadata pinned until closeout stamps the L2 code commit.
- 2026-07-07T21:00+02:00 — 260707-HFX-L6 architect/orchestrator split: updated the
  front-half rundown reframe pointer from the orchestrator lifecycle to the architect lifecycle
  (`roles/architect.md`). Verification metadata pinned until closeout stamps the HFX-L6 commit.

- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): front-half summary vocabulary aligned. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T16:30+02:00 - L8 seam-ruling remediation (cycle 4): rundown re-worded to the event-loop + ladder vocabulary (AR-13). Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:32+02:00 - L9 lifecycle convergence: the FRONT_HALF_RUNDOWN reframe bullet now names the orchestrator lifecycle explicitly (l-01-agent-lifecycles roles/orchestrator.md); flow semantics unchanged. Verification metadata pinned until closeout stamps the L9 commit.
- 2026-06-27T22:00+02:00 — Task 28 (NOTIFY-AND-CONTINUE active turn end): repointed every ACTIVE hint off `lifecycle_gate` onto `lifecycle_turn_end_notification` — the front-half `decide` hint, the generic `_FRONT_HALF_SUMMARY`/`FRONT_HALF_RUNDOWN` closing step, and the three `_gate_after` closeout/integration/cleanup overlays now all carry `nextTool="lifecycle_turn_end_notification"` + a context `summary` (notify and stop, no gate, no wait). Added the `_TURN_HANDED_TO_DEVELOPER` constant and a `state.state == "awaiting-developer"` branch (checked right after `blocked`) returning a `nextTool=None` stop hint. The `_AWAIT_GATE` + `blocked` branch is left intact — the parked gate path stays valid but un-hinted. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-27T20:16+02:00 — Gate-await hint. Added the `_AWAIT_GATE` module constant and a `state.state == "blocked"` branch in `compute_next_step`, checked right after the terminal check and before the front-half/linear branches. A raised `lifecycle_gate` calls `amb.block()` (state → "blocked"), so the hint now points at `lifecycle_resume` (await the developer's decision) instead of the post-gate operational step — carrying the chain through the open gate (raise → blocked → resume → continue), independent of phase/contract.
- 2026-06-27T18:43+02:00 — Added. New module: the task-27 lifecycle next-step engine — pure `compute_next_step` (front-half rundown pointer / `decide` worktree-intent gate vs linear-half `_gate_after` overlay + `lifecycle_guidance` delegation, plus the terminal `_LOOP_BACK`) and the exception-contained edge `next_step_for` with look-before-leaping `_load_contract`/`_guidance_for`.
