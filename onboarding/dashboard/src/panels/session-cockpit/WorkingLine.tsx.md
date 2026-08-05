# dashboard/src/panels/session-cockpit/WorkingLine.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/WorkingLine.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`       |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                    |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

The **WorkingLine** (260715-FEUI-L6 R6, spec §1.2-2, design §9.7): the SINGLE home of turn
theater. Renders ONLY while the focused seat's grammar state is `working`
(`seatVisualState().key`), mounted by SessionsView into SessionStage's reserved slot directly
under the HeaderStrip. Anatomy, fixed: `◐ <activity form | "working"> · ~elapsed · ⏹ stop`. Turn
theater NEVER renders per rail row.

## Code Commentary

### Logic

- **Render gate** (cit:(["if (!working) return null;"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:122-122)): the render returns null when `working` is false.
- **Activity form seam** (cit:(["export function workingActivityForm(session: OpenSession): string | undefined {"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:93-93)): `workingActivityForm` is the typed activity-form helper.
- **~elapsed** (cit:(["export function formatApproxElapsed(elapsedMs: number): string {"; "now?: number;"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:80-80; dashboard/src/panels/session-cockpit/WorkingLine.tsx:107-107)): the elapsed formatter and optional `now` input are declared here.
- **Stop action (UA-7)** (cit:(["interrupt === undefined ? null"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:148-148)): the stop-control render branches when `interrupt` is undefined.
- **Spinner** (cit:([`PULSE_ANIMATION`], dashboard/src/data/stateGrammar.ts:14-14)): `stateGrammar` defines `PULSE_ANIMATION`.

### Invariants And Boundaries

- This line is the ONLY turn-theater surface; the rail renders none of it (the rail's L6 gains
  are bell markers + tooltip hints only).
- The activity form must stay real-or-plain — a decorative gerund is a ruled violation.
- The pulse literal must track the grammar's ruled string; drift surfaces via the test's
  constant pin.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The WorkingLine component, elapsed formatter, and interrupt seam. | "export function WorkingLine({"; "export function formatApproxElapsed(elapsedMs: number): string {"; "interrupt === undefined ? null" | dashboard/src/panels/session-cockpit/WorkingLine.tsx:80-80; dashboard/src/panels/session-cockpit/WorkingLine.tsx:98-98; dashboard/src/panels/session-cockpit/WorkingLine.tsx:148-148 |
| The grammar predicate + the ruled pulse literal. | `seatVisualState`; `PULSE_ANIMATION` | dashboard/src/data/stateGrammar.ts:14-14; dashboard/src/data/stateGrammar.ts:101-125 |
| The cockpit-store shape contains `workingSince`. | `workingSince` | dashboard/src/data/sessionCockpitStore.ts:139-139 |
| The UA-7 reason copy. | `STOP_TURN_DISABLED_REASON` | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:66-67 |
| The reserved stage slot renders `ConversationWorkingLine` or `WorkingLine`. | "<ConversationWorkingLine sessionId={focused.id} />"; "<WorkingLine" | dashboard/src/panels/session-cockpit/SessionsView.tsx:1216-1216; dashboard/src/panels/session-cockpit/SessionsView.tsx:1218-1218 |
| SessionsView registers the `conversation.stop` command used by the working-line stage. | "id: \"conversation.stop\""; "title: \"Stop turn\""; "keywords: [\"stop\", \"interrupt\", \"cancel\", \"turn\", \"abort\"]"; "when: () => chatsInterruptRef.current.available"; "run: () => chatsInterruptRef.current.onStop?.()" | dashboard/src/panels/session-cockpit/SessionsView.tsx:582-584; dashboard/src/panels/session-cockpit/SessionsView.tsx:586-587 |

## 260718-CHATS-L4 Reviewed Candidate Delta

An optional `interrupt` prop (the `ConversationInterrupt` from `useConversationControls`) is added,
backward-compatible: absent (the pre-L4 tests, RailChat) → the existing disabled placeholder with
`STOP_TURN_DISABLED_REASON`; present → an actionable stop gated on real turn + capability evidence.
The enabled control carries `aria-keyshortcuts` DERIVED from the effective keymap (review F25), rests at
demoted destructive weight (muted border, amber only on hover/focus — A6), and its tooltip is an honest
action tooltip (`Stop the current turn · <effective chord>`) — the known-stale L1 capability reason is
never surfaced (F24). The not-working / catalog-lag placeholder falls back to the honest pre-L4 constant
rather than the stale L1 text. The welded ⏹ position and the working-only render gate are unchanged.

The reviewed candidate is uncommitted; existing verification hash/date remain pinned; closeout owns
commit stamping.

## Current L5I Maintenance

This is the catalog-driven working fallback for raw terminals and the temporary SSE connect/reconnect
window. It renders no stop at all when no interrupt is wired, because controlled seats own Stop beside
Send; a raw terminal can still receive the line-hosted evidence-gated control.

## Update History

- 2026-08-04T11:43:39+02:00 — 260731-EFA-L6 S18-B03 curator: replaced stale WorkingLine ranges with exact
  gate/action/grammar anchors, bound the dependent full conversation.stop registration, narrowed
  declaration-only claims, and rewrote the old welded-stop claim around the interrupt branch.

- 2026-07-24T13:17:17Z — Curator: corrected fallback-source and stop-control ownership semantics;
  verification fields remain pre-commit.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: recorded the optional `interrupt` prop — absent
  keeps the pre-L4 disabled placeholder (existing tests unchanged); present renders an evidence-gated
  actionable stop with keymap-derived `aria-keyshortcuts` (F25), demoted weight (A6), and an honest
  action tooltip that never leaks the stale L1 reason (F24). Verification metadata remains pinned to the
  leaf base until closeout stamps the L4 commit.
- 2026-07-17T04:20+02:00 — Created for 260715-FEUI-L6 R6: the single-home turn theater in L2's
  reserved stage slot — grammar-gated render (the same predicate as the `turn.stop` palette
  command after review finding 3), real-or-plain activity form (typed seam, never whimsy),
  ~-labeled sweep-bounded tabular elapsed omitted when unobserved, the welded UA-7-gated
  disabled stop naming the gap, and the ruled slow-pulse ◐ glyph frozen under
  `data-effects="off"`. Verification metadata pinned to the leaf base until closeout stamps the
  L6 code commit.
