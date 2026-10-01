# mcp/src/agents_remember/application/next_step.py

## Governing Overview

Nearest route overview: [application overview](overview.md).

## Purpose

The lifecycle next-step engine (task 27). Computes the single `NextStep` hint
available to the `mcp/tools/base.py::_tool_payload` response boundary. With an ambient
lifecycle, enrichment uses this computed hint when the producer did not already supply one;
an operation's explicit recovery hint takes precedence and contradictory task addresses are omitted. It folds the
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

The two integration-status conditions bracket a checkpointed series correctly and were **reviewed and
deliberately left unchanged** by 260831-LOCR-L30:
`worktree_integrate` && `integration_status != "completed"` still fires for a checkpointed series
cit:(["and contract.integration_status != \"completed\""], mcp/src/agents_remember/application/next_step.py:217-217),
so it gets "Integration dry-run verified — ready to integrate" — right, because it integrates again
when it completes; and `lifecycle_finalize_task` && `integration_status == "completed"` does **not**
fire for one cit:(["and contract.integration_status == \"completed\""], mcp/src/agents_remember/application/next_step.py:229-229),
so it gets no "stop before reclaiming the worktrees" hint — also right, because a checkpointed series
is not terminal. Do not widen either to include `checkpointed`.

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
in-lifecycle response. `_tool_payload` delegates to `complete_tool_response`, whose enrichment preserves an
explicit producer hint or calls `next_step_for`, applies `bound_next_step`, and sets
`response.nextStep` before the one final dump. The hint's rendered JSON
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
  removed. The application enrichment boundary preserves an explicit producer `nextStep`
  and otherwise calls this engine; `bound_next_step` drops a hint whose address contradicts
  the response's exact contract/enclosure address.
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

## Evidence

### Docs References

No Domain Documentation source is configured for this memory root.

No configured domain documentation governs this repository-local hint engine.

### Repo-Internal References

`compute_next_step` is invoked from the `_tool_payload` choke point and depends on
the `NextStep` model, the worktree guidance state machine, the contract loader,
and the ambient lifecycle / phase definitions.

- The response boundary preserves an explicit producer hint or computes one, rejects contradictory task addresses, and enriches the validated model before final serialization. [1]
- `NextStep` model + the `nextStep` field on the response envelopes — the declaration that makes setting it at the choke point legal. [2]
- `lifecycle_guidance` state machine delegated to in the linear half; `_guidance_for` widens its payload with `dict(...)`. [3]
- `load_contract` / `WorktreeContract` (sub-state fields read by `_gate_after`). [4]
- `amb.current` — the live `LifecycleState` resolved at the edge. [5]
- `LifecycleState` (`enclosure`, `is_terminal`) + `Phase` literals (`decide`, …) and the `awaiting-developer` state the parked branch reads (state/phase vocabulary in `models/lifecycle.py` since L9). [6]
- The next-step entry point derives guidance from the current lifecycle and tool; this source citation does not establish response token-count coverage. [7]

As of HFX-L6, the FRONT_HALF_RUNDOWN reframe bullet names the architect lifecycle explicitly
(`l-01-agent-lifecycles` `roles/architect.md`); the rundown's flow semantics are unchanged — the
front half it describes is now the architect lifecycle's front half, since spawned backend roles
do not own the developer-facing front half.

As of the 260703-L8 remediation the FRONT_HALF_RUNDOWN speaks the event-loop vocabulary: the third item routes the event (no doc → design one; approved + code change → build; no code change → research-only exit; triage may route/spawn/escalate) instead of the retired job-selection table, and the task-file item states the ladder explicitly (task doc → branch → worktree, worktree_start only after the plan gate).

As of cycle 5 the front-half summary speaks event-routing (the last job-selection remnant is gone).

### Cross-Repo References

No meaningful cross-repo references found.

The reviewed response-hint boundary is internal to this repository.
