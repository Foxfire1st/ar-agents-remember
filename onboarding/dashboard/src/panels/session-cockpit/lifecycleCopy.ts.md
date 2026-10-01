# dashboard/src/panels/session-cockpit/lifecycleCopy.ts

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

**THE lifecycle/interaction copy module** (260715-FEUI-L6 R5 — "copy centralized"): every
confirm, residual, and round-trip string the terminate/retire/interaction surfaces render comes
from here, so the honesty rules live in ONE place: confirms NAME the object (session · leaf ·
state — never a bare "are you sure"); stop residuals are INFORMATIONAL lines on an already
successfully terminated/retired row (the words "termination failed" must never appear for them);
the InteractionBar's copy states the real answer channel and the real PTY truth.

## Code Commentary

### Logic

- **`terminateConfirmCopy`** (cit:([`terminateConfirmCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:13-22)): `end <label> · leaf <id> · state <word> — kills the tmux
  session; transcripts are kept` — the grammar's state word via `seatVisualState`, the leaf via
  `leafIdFromKey`. **R1 dash-collision fix (260718-CHATS-L5P):** an UNCLASSIFIED seat's state word is
  itself an em-dash (`—`), which placed next to the copy's `— kills` consequence dash printed a bare
  `state — —`. The `· state <word>` clause is now DROPPED entirely when the state is `—`, so the two
  dashes never collide (`end <label> · leaf <id> — kills …`).
- **Residual copy** (cit:([`terminateResidualCopy`, `retireResidualCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:29-31; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:34-36)): `terminateResidualCopy` / `retireResidualCopy` — both
  `<label> terminated|retired · control-stop note (informational): <detail>`; the detail is the
  server's verbatim words.
- **`cleanupOutcomeCopy`** (cit:([`cleanupOutcomeCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:39-51)): the landed-cleanup route's OWN outcome —
  `ended N · skipped M (session: reason, …)`; skips never dropped.
- **`STOP_TURN_DISABLED_REASON`** (cit:([`STOP_TURN_DISABLED_REASON`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:65-66)): the UA-7 gap named honestly (no cancel-turn route
  exists on the control bridge yet).
- **InteractionBar copy** (cit:([`INTERACTION_HONESTY_HINT`, `INTERACTION_ANSWERING`, `INTERACTION_ANSWERED`, `INTERACTION_COMPOSER_MODE`, `INTERACTION_NO_PROMPT_TEXT`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:71-72; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:74-74; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:77-78; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:81-82; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:84-85)): `INTERACTION_HONESTY_HINT` (terminal text becomes a queued
  message, not an answer), `INTERACTION_ANSWERING`, `INTERACTION_ANSWERED` (poll-bounded,
  ≤ ~2.5 s named), `INTERACTION_COMPOSER_MODE` (direct agent-session route, not the terminal),
  `INTERACTION_NO_PROMPT_TEXT` (raw payload in the inspector).
- **PTY archetypes (R1)** (cit:([`isControlledSession`, `paneArchetypeCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:108-114; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:116-122)): `isControlledSession` — `controlState` present and
  ≠ `"unsupported"` (the server's `ControlState` literal, never a heuristic);
  `paneArchetypeCopy` names both archetypes honestly.
- **`paneAccessibleName`** (cit:([`paneAccessibleName`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:125-128), R2): `terminal: <label> · <harness> · <state>` — every
  pane's `role="group"` name.
- **`SCREEN_READER_MODE_NOTE`** (cit:([`SCREEN_READER_MODE_NOTE`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:131-132), R2): the toggle's honest cost note (xterm's a11y tree
  costs rendering performance — hence opt-in).

### Invariants And Boundaries

- New lifecycle/interaction strings belong HERE — surfaces import, never inline.
- Residual copy must keep "(informational)" and must never contain "fail" (test-asserted).
- `isControlledSession` is the ONE archetype predicate — PtySurface, SeatInspector, and any
  future surface must share it.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Every exported string/predicate. [1]
- The grammar state word the confirm/name builders consume. [2]
- The rail consumes confirm copy, and the landed-cleanup notice consumes cleanup-outcome copy. [3]
- The stage notes consuming residual copy. [4]
- The bar consuming the interaction constants. [5]
- The surface consuming archetype/name/toggle copy. [6]
- The inspector's evidence pane consumes archetype and retire-residual copy at its rendering sites. [7]
- The server literal the archetype predicate mirrors. [8]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.

## FEUI-L8 Reviewed Candidate Delta

Adds exact unavailable-cleanup copy listing intended labels and ids. This wording preserves unknown authority honestly rather than classifying the operation as success or failure.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Current L5I Maintenance

Centralized interaction copy now includes multi-question progress, multi-select guidance/confirm
labels, and recorded-answer feedback. These strings describe the direct route's all-or-nothing
contract and keep structured interaction wording consistent across the composer-stage UI.
