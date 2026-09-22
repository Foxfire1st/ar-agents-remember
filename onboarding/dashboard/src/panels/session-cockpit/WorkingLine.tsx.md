# dashboard/src/panels/session-cockpit/WorkingLine.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/WorkingLine.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`       |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The WorkingLine component, elapsed formatter, and interrupt seam. | "export function WorkingLine({"; "export function formatApproxElapsed(elapsedMs: number): string {"; "interrupt === undefined ? null" | dashboard/src/panels/session-cockpit/WorkingLine.tsx:80-80; dashboard/src/panels/session-cockpit/WorkingLine.tsx:133-133; dashboard/src/panels/session-cockpit/WorkingLine.tsx:183-183 |
| The grammar predicate + the ruled pulse literal. | `seatVisualState`; `PULSE_ANIMATION` | dashboard/src/data/stateGrammar.ts:14-14; dashboard/src/data/stateGrammar.ts:101-125 |
| The cockpit-store shape contains `workingSince`. | `workingSince` | dashboard/src/data/sessionCockpitStore.ts:139-139 |
| The UA-7 reason copy. | `STOP_TURN_DISABLED_REASON` | dashboard/src/panels/session-cockpit/lifecycleCopy.ts:65-66 |
| The reserved stage slot renders `ConversationWorkingLine` or `WorkingLine`. | "<ConversationWorkingLine sessionId={focused.id} />"; "<WorkingLine session={focused}" | dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:195-195; dashboard/src/panels/session-cockpit/sessions-view/sessionsViewBody.tsx:197-198 |
| SessionsView registers the `conversation.stop` command used by the working-line stage. | "id: \"conversation.stop\""; "title: \"Stop turn\""; "keywords: [\"stop\", \"interrupt\", \"cancel\", \"turn\", \"abort\"]"; "when: () => deps.chatsInterruptRef.current.available"; "run: () => deps.chatsInterruptRef.current.onStop?.()" | dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:125-131; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:3-3; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:9-9; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:11-11; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:18-18; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:22-22; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:25-25; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:26-26; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:27-27; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:28-28; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:29-29; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:33-33; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:42-42; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:43-43; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:56-56; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:72-72; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:74-74; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:75-75; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:76-76; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:83-83; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:84-84; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:85-85; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:86-86; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:87-87; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:88-88; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:98-98; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:132-132; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:134-134; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:135-135; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:136-136; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:147-147; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:149-149; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:150-150; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:151-151; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:153-153; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:160-160; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:162-162; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:169-169; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:172-172; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:204-204; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:205-205; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:208-208; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:212-212; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:221-221; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:224-224; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:232-232; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:234-234; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:236-236; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:237-237; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:238-238; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:259-259; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:260-260; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:261-261; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:262-262; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:263-263; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:264-264; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:265-265; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:266-266; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:267-267; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:268-268; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:269-269; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:270-270; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:271-271; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:272-272; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:273-273; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:274-274; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:277-277; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:280-280; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:292-292; dashboard/src/panels/session-cockpit/sessions-view/useSessionsPaletteCommands.tsx:304-304 |

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
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

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
