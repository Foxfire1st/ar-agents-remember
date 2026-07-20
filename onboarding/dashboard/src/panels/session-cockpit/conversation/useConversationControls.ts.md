# dashboard/src/panels/session-cockpit/conversation/useConversationControls.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/useConversationControls.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The exact-turn **interrupt wiring** (design §9.5, R6; L4-facing ruling 3 + register L3.5). It reads the
live turn + capability from the active-conversation projection, dispatches interrupt with a
caller-stable requestId (reconciled under the SAME id — invariant 27), and reports acknowledgement vs.
settlement as distinct announcer-keyed transitions (ack is never voiced as interrupted). It is the
production embodiment of the leaf's central rulings: attempt-and-reflect capability gating, item-evidence
turn-id correlation, and the never-surface-the-stale-L1-reason discipline.

## Code Commentary

### Logic

- **`resolveWorkingTurnId`** (L61-L78, F1 / register L4.R1): prefers the canonical `status.turn.turnId`;
  when the wire omits it during a working turn (the hosted-codex topology carries no `turnId`),
  correlates from the newest streaming/pending item's `turnId` (falling back to the newest item that
  carries one — codex `native_parent_id`; pi the AR operation id per ruling 3). Returns `null` only when
  genuinely unresolvable.
- **`useConversationInterrupt`** (L88-L170): resolves `turnId`, `turnState`, and `capability` from the
  projection. `keyshortcut` (L92-L97, F25) is DERIVED from the effective keymap —
  `ariaKeyshortcuts(bindingFor(useEffectiveKeymap(), "conversation.stop")?.chord ?? DEFAULT_STOP_CHORD)`
  — so a rebind through `cockpit.sessions.keymap.v1` keeps the AT advertisement truthful, never a
  hardcoded constant.
- **Dispatch** (L134-L144): `onStop` uses a per-turn requestId (`requestIdByTurn`); the FIRST dispatch is
  `requestInterrupt`, a later one is `interruptReconcile` under the SAME id (never a fresh id). `applyResult`
  (L115-L132) announces ack (`interrupt <acknowledgement>`) and, separately, settlement (`turn <settlement>`)
  — ack is never voiced as interrupted; `pending` tracks in-flight.
- **Availability + honest reason** (L146-L169): `available = working && turnId !== null && !hardUnavailable
  && !refusedThisTurn`. Reason copy is ONLY the honest, current signal — an enabled control carries NO
  reason (F24); a hard `unavailable` capability shows its reason; a typed refusal (scoped to its turn,
  L99/L119/L127, F5) shows the exact server detail until the turn changes; an unresolvable working turn
  shows `turn identity unavailable on this wire` (never the stale L1 text).

### Conventions

Capability gating is **attempt-and-reflect** (L4.1/L3.5): the active page's `capabilities.controls` is
the KNOWN-STALE L1 view (`unverified` for all three harnesses) and no GET exposes the true control
capability, so the stop enables on a working+resolvable turn unless the capability is a hard
`unavailable`, and reflects the server's typed refusal reactively. This is the honest wire maximum;
a clean proactive gate awaits a control-capabilities GET or an L1-view refresh.

### Invariants And Boundaries

- The KNOWN-STALE L1 `unverified` `capability.reason` is NEVER surfaced as control copy — it once leaked
  onto the enabled tooltip and the catalog-lag placeholder (F24); the enabled control shows no reason.
- A working turn's id resolves from item evidence when status omits it; a genuinely unresolvable id
  disables with an honest reason, never the stale capability text.
- The requestId is caller-stable and reconciled under the same id; a lost response is reconciled, never
  re-dispatched fresh (invariant 27).
- `aria-keyshortcuts` mirrors the EFFECTIVE keymap assignment (F25), so a rebind stays truthful; the
  attribute appears only on an enabled control (no phantom shortcut, F2).
- Acknowledgement is never settlement — the two announce on distinct keys.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Turn-id correlation, attempt-and-reflect gating, honest reason, ack≠settlement announcing. | L61-L170 | [useConversationControls.ts](useConversationControls.ts) |
| The interrupt request/status/reconcile client + typed `ControlResult` (a refusal never guessed into success). | — | [../../../data/conversation/client.ts](../../../data/conversation/client.ts) |
| The projection this hook reads (`status.turn.turnId`, item `turnId`, `capabilities.controls`). | — | [../../../data/conversation/reducer.ts](../../../data/conversation/reducer.ts) · [../../../data/conversation/store.ts](../../../data/conversation/store.ts) |
| The `ariaKeyshortcuts` helper + `conversation.stop` binding lookup (F25). | — | [../../../data/keymap/preferences.ts](../../../data/keymap/preferences.ts) |
| The shared polite announcer for ack/settlement transitions. | — | [../../../data/announcer.ts](../../../data/announcer.ts) |
| The WorkingLine host that renders the enabled/disabled stop from this hook. | — | [../WorkingLine.tsx](../WorkingLine.tsx) |
| The interrupt hook suite (enable/unresolvable/refusal regression). | — | [useConversationControls.test.tsx](useConversationControls.test.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the exact-turn interrupt
  hook — `resolveWorkingTurnId` item-evidence correlation (F1/L4.R1), attempt-and-reflect capability
  gating on the L3 evidence (L4.1/L3.5), turn-scoped typed-refusal disable (F5), the never-surface-the-
  stale-L1-reason rule (F24), keymap-derived `aria-keyshortcuts` (F25), and ack≠settlement announcing.
  Verification is pinned to the leaf base (`0be0099`) because the new source file is uncommitted;
  closeout owns its first source stamp.
