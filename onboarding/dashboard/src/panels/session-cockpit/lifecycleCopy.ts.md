# dashboard/src/panels/session-cockpit/lifecycleCopy.ts

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/lifecycleCopy.ts` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `7c56c11d651972515723b4090b8174087eb5236f`       |
| lastVerifiedCommitDate | 2026-08-07T20:50:27+02:00|
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

- **`terminateConfirmCopy`** (cit:([`terminateConfirmCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:14-23)): `end <label> · leaf <id> · state <word> — kills the tmux
  session; transcripts are kept` — the grammar's state word via `seatVisualState`, the leaf via
  `leafIdFromKey`. **R1 dash-collision fix (260718-CHATS-L5P):** an UNCLASSIFIED seat's state word is
  itself an em-dash (`—`), which placed next to the copy's `— kills` consequence dash printed a bare
  `state — —`. The `· state <word>` clause is now DROPPED entirely when the state is `—`, so the two
  dashes never collide (`end <label> · leaf <id> — kills …`).
- **Residual copy** (cit:([`terminateResidualCopy`, `retireResidualCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:30-32; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:35-37)): `terminateResidualCopy` / `retireResidualCopy` — both
  `<label> terminated|retired · control-stop note (informational): <detail>`; the detail is the
  server's verbatim words.
- **`cleanupOutcomeCopy`** (cit:([`cleanupOutcomeCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:40-52)): the landed-cleanup route's OWN outcome —
  `ended N · skipped M (session: reason, …)`; skips never dropped.
- **`STOP_TURN_DISABLED_REASON`** (cit:([`STOP_TURN_DISABLED_REASON`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:66-67)): the UA-7 gap named honestly (no cancel-turn route
  exists on the control bridge yet).
- **InteractionBar copy** (cit:([`INTERACTION_HONESTY_HINT`, `INTERACTION_ANSWERING`, `INTERACTION_ANSWERED`, `INTERACTION_COMPOSER_MODE`, `INTERACTION_NO_PROMPT_TEXT`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:72-73; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:75-75; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:78-79; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:82-83; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:85-86)): `INTERACTION_HONESTY_HINT` (terminal text becomes a queued
  message, not an answer), `INTERACTION_ANSWERING`, `INTERACTION_ANSWERED` (poll-bounded,
  ≤ ~2.5 s named), `INTERACTION_COMPOSER_MODE` (gate channel, not the terminal),
  `INTERACTION_NO_PROMPT_TEXT` (raw payload in the inspector).
- **PTY archetypes (R1)** (cit:([`isControlledSession`, `paneArchetypeCopy`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:109-115; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:117-123)): `isControlledSession` — `controlState` present and
  ≠ `"unsupported"` (the server's `ControlState` literal, never a heuristic);
  `paneArchetypeCopy` names both archetypes honestly.
- **`paneAccessibleName`** (cit:([`paneAccessibleName`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:126-129), R2): `terminal: <label> · <harness> · <state>` — every
  pane's `role="group"` name.
- **`SCREEN_READER_MODE_NOTE`** (cit:([`SCREEN_READER_MODE_NOTE`], dashboard/src/panels/session-cockpit/lifecycleCopy.ts:132-133), R2): the toggle's honest cost note (xterm's a11y tree
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Every exported string/predicate. | `terminateConfirmCopy`; `cleanupOutcomeCopy`; `STOP_TURN_DISABLED_REASON`; `isControlledSession` | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:14-23; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:40-52; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:66-67; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:109-115 |
| The grammar state word the confirm/name builders consume. | `seatVisualState` | dashboard/src/data/stateGrammar.ts:101-125 |
| The rail consuming confirm copy, and the landed-cleanup notice consuming cleanup-outcome copy. | `terminateConfirmCopy`; `cleanupOutcomeCopy` | dashboard/src/panels/session-cockpit/LandedCleanupNotice.tsx:96-96; dashboard/src/panels/session-cockpit/lifecycleCopy.ts:14-23 |
| The stage notes consuming residual copy. | `terminateResidualCopy`; `retireResidualCopy` | dashboard/src/panels/session-cockpit/StopResidualNotes.tsx:3-3; dashboard/src/panels/session-cockpit/StopResidualNotes.tsx:56-57 |
| The bar consuming the interaction constants. | "  INTERACTION_HONESTY_HINT,"; "  INTERACTION_COMPOSER_MODE,"; "  INTERACTION_ANSWERING,"; "  INTERACTION_ANSWERED,"; "  INTERACTION_NO_PROMPT_TEXT," | dashboard/src/panels/session-cockpit/interactionParts.tsx:13-13; dashboard/src/panels/session-cockpit/interactionParts.tsx:12-12; dashboard/src/panels/session-cockpit/interactionParts.tsx:11-11; dashboard/src/panels/session-cockpit/interactionParts.tsx:10-10; dashboard/src/panels/session-cockpit/interactionParts.tsx:16-16 |
| The surface consuming archetype/name/toggle copy. | "isControlledSession,"; "paneAccessibleName,"; "paneArchetypeCopy,"; "SCREEN_READER_MODE_NOTE," | dashboard/src/panels/session-cockpit/PtySurface.tsx:14-17; dashboard/src/panels/session-cockpit/PtySurface.tsx:211-211; dashboard/src/panels/session-cockpit/PtySurface.tsx:230-230; dashboard/src/panels/session-cockpit/PtySurface.tsx:305-305 |
| The inspector's evidence pane consuming archetype + retire-residual copy. | "paneArchetypeCopy,"; "retireResidualCopy," | dashboard/src/panels/session-cockpit/EvidencePane.tsx:19-20; dashboard/src/panels/session-cockpit/EvidencePane.tsx:111-111; dashboard/src/panels/session-cockpit/EvidencePane.tsx:199-199; dashboard/src/panels/session-cockpit/EvidencePane.tsx:213-213 |
| The server literal the archetype predicate mirrors. | `HarnessControlState` | dashboard/src/types/terminalCatalog.ts:9-9 |

## FEUI-L8 Reviewed Candidate Delta

Adds exact unavailable-cleanup copy listing intended labels and ids. This wording preserves unknown authority honestly rather than classifying the operation as success or failure.

The reviewed candidate is still uncommitted. Existing verification hash/date remain pinned to the
leaf base; closeout owns commit stamping.

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Current L5I Maintenance

Centralized interaction copy now includes multi-question progress, multi-select guidance/confirm
labels, and recorded-answer feedback. These strings describe the direct route's all-or-nothing
contract and keep structured interaction wording consistent across the composer-stage UI.

## Update History

- 2026-08-04T18:03+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 8 citation rows with exact anchors and ledger-verified ranges (whole export surface, seatVisualState, SessionRail confirm + LandedCleanupNotice outcome consumers, StopResidualNotes, InteractionBar import/usages, PtySurface, EvidencePane — replacing the consumer-less SeatInspector citation — and the HarnessControlState literal); converted the 8 Logic-bullet line references to cit form with re-derived ranges after the module grew. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T17:48+02:00 — 260731-EFA-L2 curator: re-derived the stale `STOP_TURN_DISABLED_REASON`
  self-citation — the constant now sits at L66-L67 (was L51-L52) after the cleanup-failure copy was
  added above it. The string itself is unchanged.

- 2026-07-24T13:17:17Z — Curator: documented structured-question copy ownership and all-or-nothing
  wording; verification fields remain pre-commit.

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
