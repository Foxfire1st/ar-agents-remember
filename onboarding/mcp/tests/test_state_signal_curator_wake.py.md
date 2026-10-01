# mcp/tests/test_state_signal_curator_wake.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins `LOCR-R07@v1`: a curator seat's own canonical terminal turn wakes the **current** manager of the
curator's master, through the same shared role predicate and action-time owner routing the worker seat
already uses, without the curator hand-authoring a completion post. A curator's durable output is its
structured coherence authority rather than a chat message, so the wake is a relay of terminal truth,
not a request that the seat announce itself.

The module starts where production starts — the adapter's own evidence frames — and lets the real
`TerminalCatalogLivenessSweeper` derive the catalog turn truth before the real agent-notifier sweep
relays it. No row in any scenario is written with a turn claim, a terminal outcome or an evidence
identity; no terminal-session GET is issued; and no curator-authored completion row exists in any
world. Five cases. It is deliberately separate from
[test_state_signal_relay.py](test_state_signal_relay.py.md), which owns action-time current-manager
replacement and per-subject topology refusal for the seat-generic relay, from
[test_state_signal_boundary_delivery.py](test_state_signal_boundary_delivery.py.md), which owns the
persist-before-marker order and the held-`working`-target boundary, and from
[test_state_signal_restart_recovery.py](test_state_signal_restart_recovery.py.md), which owns the
durable order across a crash, a failed marker write and a same-seat rebind.

## Code Commentary

### Logic

1. `test_a_completed_curator_turn_wakes_the_current_manager_with_one_durable_signal` — the premise
   asserts the registered row is registration only (`turn_state`, `terminal_outcome` and
   `terminal_evidence_id` all `None`); the two sweeps then produce `turn-ended` / `completed` /
   `turn-41`, and one notifier sweep lands exactly one durable state signal addressed to the
   manager named by the curator's own master. The payload carries `recipientRole="manager"`, the
   master as `taskDocumentRef`, the leaf as `subjectTaskDocumentRef`, `subjectAgentId` = the curator
   session, `seatRole="curator"`, and both outcome and evidence id in `ask` and `response`; the row
   is `state_signal_landed` and `deliveredToSession` is the manager. Two absences are asserted as
   hard facts, not inferred from a green run: the inbox holds no row whose `senderRole` is
   `curator`, and re-running the notifier sweep mints no second signal — the seat's
   `state_signal_emitted_for` is stamped `turn-41` and the signal id list is unchanged.
2. `test_an_interrupted_curator_turn_wakes_the_manager_with_interruption_truth` — a native
   `turn/completed` envelope carrying `status="interrupted"` (sequence 77, with the seat row's
   interrupt provenance set to `developer`). One observation sweep produces `turn-ended` /
   `interrupted` / `turn-77`, and the single signal's `ask` names the interruption — asserting
   `interrupted`, asserting `turn-77`, and asserting `"completed"` is **absent** — while `response`
   carries `outcome interrupted` and `interrupted_by=developer`. The re-emission guard is asserted
   on this path too: a second sweep yields the same single row id and the marker is stamped
   `turn-77`.
3. `test_a_failed_curator_turn_never_wakes_the_manager` — the negative control that keeps the
   two-outcome boundary honest *from the outside*. `LOCR-R07@v1` scopes the wake to `completed` and
   `interrupted`, and the canonical outcome vocabulary is closed: a `failed` native status is a real
   outcome the projector maps, so the seat genuinely reaches `turn-ended` / `failed` / `turn-91` and
   the relay still emits nothing. The case also asserts the seat is *not consumed* — the marker
   stays unset — so a later canonical outcome can still wake rather than the seat being silently
   spent by an outcome it never relayed.
4. `test_the_curator_wake_neither_validates_nor_declares_curator_coherence` — the wake appends no
   verdict. The signal's `ask` and `response` are asserted **equal** to the canonical
   `state_signal_ask(observed, "turn-41")` and `state_signal_response(observed)` derivations, so any
   appended clause fails; none of the acceptance vocabulary (`ready`, `coherence`, `closeout`)
   appears in either text; and `consumedAt` is `None`, because the manager — not the relay — owns
   consumption. The "no coherence artifact was written" claim is read **after** the sweep and
   through the *same* helper as its premise (`coordination_root_entries`), so both sides are one
   population: the root starts as `["logs", "tasks"]` and is asserted to still be exactly that once
   the relay has run. A relay that wrote its own coherence or readiness artifact would show up there
   and nowhere else.
5. `test_a_curator_seat_without_a_current_manager_fails_closed_without_global_routing` — the world
   registers no manager for the curator's own master while a *different* master's manager is live
   and current, so a global owner search would have somewhere to route. The premise asserts both
   halves (`manager_for(OTHER_MASTER)` is not `None`, `manager_for(MASTER)` is `None`) before the
   sweeps, the seat still reaches `completed`, and the assertion is deliberately **one reachable
   check rather than two**: `addressed_to(OTHER_MANAGER_ID)` must be `[]`. That single call fails on
   a state signal anywhere in the inbox *or* on any row naming the live other-master manager as
   owner or delivery target, so splitting it into separate assertions would leave the second half
   shadowed by the first in exactly the scenario the case exists for. The seat is left eligible —
   the marker stays unset — so this is fail-closed, not consume.

### Conventions

One `_CuratorRelayWorld` per case over a temporary coordination root that writes a real task
topology (one sprint orchestrating two masters, each with its own leaves) before the sweep resolves
structural owners. `_CuratorEvidence` is the adapter's own evidence surface: the first read of the
curator row hands back the native `turn/completed` envelope and every later read hands back the
consumed tail, exactly as the daemon's deque does once the cursor has advanced, while every other
row reads an empty page so the curator's evidence cannot leak into another seat. `_AliveHost` and
`_AcceptedPaster` keep delivery off a real process, and `_SUBMIT` is patched to return an accepted
`SubmissionReceipt`. `observe_adapter_evidence` and `settle` are two real sweeps of the production
`TerminalCatalogLivenessSweeper`, the second one past
`DEFAULT_LIVENESS_HYSTERESIS.sweep_interval_seconds` so it is a real second observation rather than a
rate-limited no-op. `notifier` builds a real `AgentNotifierContext` over temporary stores and calls
the real `run_agent_notifier_sweep`. Cases assert through `_single_signal`, `rows`, `signals` and
`addressed_to` rather than reaching into private helpers.

### Invariants And Boundaries

- The wake is **terminal-truth relay only**. It neither validates nor declares curator coherence,
  memory readiness or closeout acceptance; the manager opens and validates the canonical curator
  authority itself. `accepted` is a transport fact here, not a verdict about the curator's memory —
  which is why the acceptance vocabulary is asserted absent rather than present.
- One durable signal per exact seat plus `terminal_evidence_id`, on both the `completed` and the
  `interrupted` path, and never a second one on re-observation.
- `failed` is not a manager wake and does not consume the seat: terminal truth is reached, nothing is
  emitted, and the marker stays unset so a later canonical outcome can still relay.
- Ownership is resolved from the task hierarchy at action time. A curator seat whose own master has
  no current manager fails closed; it never routes to another master's manager. The stale
  spawn-ancestry address registered on the curator row (`STALE_SPAWNER_ID`) is asserted never to be
  selected — the cases assert the manager the topology names, not the session the seat was spawned
  from.
- The relay writes no governed artifact of its own; the coordination root read after the sweep is
  compared against the premise through one reader.
- This card records source inspection. It does not claim acceptance, certification, execution or an
  independent review result. The module is ordinary version-controlled test source: it holds no
  governed evidence registration, and the promotion hold point is the
  `test-evidence-lanes.toml` `unit-regression` row, not a record created here.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own fixtures
and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

- A completed curator turn wakes the current manager of its own master with exactly one durable signal, no curator-authored row, and no second signal on re-observation. [1]
- An interrupted curator turn wakes the manager with interruption truth and is re-emission-guarded on that path. [2]
- A failed curator turn reaches terminal truth, emits nothing, and leaves the seat eligible rather than consumed. [3]
- The payload is the canonical terminal-truth derivation with no verdict appended, and the post-sweep coordination root equals the premise. [4]
- A curator seat with no current manager fails closed instead of routing to another master's live manager, asserted as one reachable check. [5]
- One disposable production wiring per case: task topology, catalog, bridges, inbox, and the two real sweeps. [6]
- The two real liveness observations; the second is past the sweeper's own full-sweep rate limit. [7]
- One real notifier sweep under a bridge that accepts whatever it is handed, over temporary stores. [8]
- Every row addressed to, delivered to, or itself a state signal, in one reachable read whose failure modes cannot shadow each other. [9]
- One reader for both the pre-sweep premise and the post-sweep claim, so "the relay wrote no governed artifact" is a statement about one population. [10]
- The adapter's own evidence surface: the native envelope on the first read, the consumed tail thereafter, empty pages for every other seat. [11]
- One native codex `turn/completed` envelope, mapped by the real vendor projector rather than pre-digested into a turn claim. [12]
- The production task-document tree the routing resolves structural owners from: one sprint, the curator's master, and a second master. [13]
- The stale spawn-ancestry address that routing must never select, because ownership comes from the task hierarchy. [14]
- The acceptance vocabulary deliberately asserted absent: delivery words are transport facts, not memory verdicts. [15]
- The single-signal reader every wake case asserts through. [16]
- The temporary-world context manager, including the no-master-manager variant the fail-closed case uses. [17]
- The shared manager-routing predicate the curator seat must reach exactly as the worker seat does. [18]
- The two sweeps whose composition produces the asserted turn truth and signal. [19]
- The canonical payload builders the signal text is asserted equal to. [20]
- The durable marker the re-emission guard reads and the landed-row predicate the wake asserts. [21]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
