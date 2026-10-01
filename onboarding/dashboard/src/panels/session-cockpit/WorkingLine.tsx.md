# dashboard/src/panels/session-cockpit/WorkingLine.tsx

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

- **Render gate** (cit:(["if (!working) return null;"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:157-157)): the render returns null when `working` is false.
- **Activity form seam** (cit:(["export function workingActivityForm(session: OpenSession): string | undefined {"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:93-93)): `workingActivityForm` is the typed activity-form helper.
- **~elapsed** (cit:(["export function formatApproxElapsed(elapsedMs: number): string {"; "now?: number;"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:80-80; dashboard/src/panels/session-cockpit/WorkingLine.tsx:142-142)): the elapsed formatter and optional `now` input are declared here.
- **Stop action (UA-7)** (cit:(["interrupt === undefined ? null"], dashboard/src/panels/session-cockpit/WorkingLine.tsx:183-183)): the stop-control render branches when `interrupt` is undefined.
- **Spinner** (cit:([`PULSE_ANIMATION`], dashboard/src/data/stateGrammar.ts:14-14)): `stateGrammar` defines `PULSE_ANIMATION`.

### Invariants And Boundaries

- This line is the ONLY turn-theater surface; the rail renders none of it (the rail's L6 gains
  are bell markers + tooltip hints only).
- The activity form must stay real-or-plain — a decorative gerund is a ruled violation.
- The pulse literal must track the grammar's ruled string; drift surfaces via the test's
  constant pin.

## Evidence

### Repo-Internal References

- The WorkingLine component, elapsed formatter, and interrupt seam. [1]
- The grammar predicate + the ruled pulse literal. [2]
- The cockpit-store shape contains `workingSince`. [3]
- The UA-7 reason copy. [4]
- The reserved stage slot renders `ConversationWorkingLine` or `WorkingLine`. [5]
- SessionsView registers the `conversation.stop` command used by the working-line stage. [6]

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
