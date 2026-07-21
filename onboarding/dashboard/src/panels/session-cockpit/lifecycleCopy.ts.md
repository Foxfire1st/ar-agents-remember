# dashboard/src/panels/session-cockpit/lifecycleCopy.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/lifecycleCopy.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-21T05:30+02:00                           |
| lastVerifiedCommitHash | `1119b64ff1564c5fc76fd518f88e529535c04b34`       |
| lastVerifiedCommitDate | 2026-07-21T08:14:40+02:00|
| governingOverview      | `overview.md`                                   |

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

- **`terminateConfirmCopy`** (L13-L21): `end <label> · leaf <id> · state <word> — kills the tmux
  session; transcripts are kept` — the grammar's state word via `seatVisualState`, the leaf via
  `leafIdFromKey`. **R1 dash-collision fix (260718-CHATS-L5P):** an UNCLASSIFIED seat's state word is
  itself an em-dash (`—`), which placed next to the copy's `— kills` consequence dash printed a bare
  `state — —`. The `· state <word>` clause is now DROPPED entirely when the state is `—`, so the two
  dashes never collide (`end <label> · leaf <id> — kills …`).
- **Residual copy** (L20-L32): `terminateResidualCopy` / `retireResidualCopy` — both
  `<label> terminated|retired · control-stop note (informational): <detail>`; the detail is the
  server's verbatim words.
- **`cleanupOutcomeCopy`** (L34-L47): the landed-cleanup route's OWN outcome —
  `ended N · skipped M (session: reason, …)`; skips never dropped.
- **`STOP_TURN_DISABLED_REASON`** (L51-L52): the UA-7 gap named honestly (no cancel-turn route
  exists on the control bridge yet).
- **InteractionBar copy** (L54-L71): `INTERACTION_HONESTY_HINT` (terminal text becomes a queued
  message, not an answer), `INTERACTION_ANSWERING`, `INTERACTION_ANSWERED` (poll-bounded,
  ≤ ~2.5 s named), `INTERACTION_COMPOSER_MODE` (gate channel, not the terminal),
  `INTERACTION_NO_PROMPT_TEXT` (raw payload in the inspector).
- **PTY archetypes (R1)** (L73-L84): `isControlledSession` — `controlState` present and
  ≠ `"unsupported"` (the server's `ControlState` literal, never a heuristic);
  `paneArchetypeCopy` names both archetypes honestly.
- **`paneAccessibleName`** (L86-L90, R2): `terminal: <label> · <harness> · <state>` — every
  pane's `role="group"` name.
- **`SCREEN_READER_MODE_NOTE`** (L92-L94, R2): the toggle's honest cost note (xterm's a11y tree
  costs rendering performance — hence opt-in).

### Invariants And Boundaries

- New lifecycle/interaction strings belong HERE — surfaces import, never inline.
- Residual copy must keep "(informational)" and must never contain "fail" (test-asserted).
- `isControlledSession` is the ONE archetype predicate — PtySurface, SeatInspector, and any
  future surface must share it.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Every exported string/predicate. | L1-L94 | [lifecycleCopy.ts](lifecycleCopy.ts) |
| The grammar state word the confirm/name builders consume. | L44-L106 | [../../data/stateGrammar.ts](../../data/stateGrammar.ts) |
| The rail consuming confirm + cleanup-outcome copy. | L548-L614, L755-L770 | [SessionRail.tsx](SessionRail.tsx) |
| The stage notes consuming residual copy. | L45-L70 | [StopResidualNotes.tsx](StopResidualNotes.tsx) |
| The bar consuming the interaction constants. | L12-L18, L257-L290 | [InteractionBar.tsx](InteractionBar.tsx) |
| The surface consuming archetype/name/toggle copy. | L9-L14, L172-L245 | [PtySurface.tsx](PtySurface.tsx) |
| The inspector consuming archetype + retire-residual copy. | L5, L71, L105-L111 | [SeatInspector.tsx](SeatInspector.tsx) |
| The server literal the archetype predicate mirrors. | — | [../../types/terminalCatalog.ts](../../types/terminalCatalog.ts) |

## FEUI-L8 Reviewed Candidate Delta

Adds exact unavailable-cleanup copy listing intended labels and ids. This wording preserves unknown authority honestly rather than classifying the operation as success or failure.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the R1 dash-collision fix in
  `terminateConfirmCopy` — the `· state <word>` clause is dropped when the state word is the em-dash
  sentinel, so an unclassified seat no longer renders `state — —`. All other copy/predicates unchanged.
  Verification pinned to the leaf base (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R5 (+R1/R2/R4/R6 copy): the ONE
  centralized copy module — naming terminate confirms, informational terminate/retire residuals,
  the honest cleanup outcome with skips, the UA-7 stop reason, the InteractionBar's
  honesty/round-trip strings, the `isControlledSession` archetype predicate + pane copy, the
  accessible pane name, and the screen-reader cost note. Verification metadata pinned to the
  leaf base until closeout stamps the L6 code commit.
