# dashboard/src/panels/session-cockpit/SessionRail.tsx

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `dashboard/src/panels/session-cockpit/SessionRail.tsx` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated | 2026-08-11T09:45+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914`       |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[panels/session-cockpit overview](overview.md)

## Purpose

Renders the canonical Chats seat rail from the structural rail model, including stable sprint,
master, leaf, and role rows whose live occupant may be replaced.

## Code Commentary

### Logic

`SessionRail` consumes the task-projected model, maintains local tree expansion, focus, attention,
and bulk controls, and delegates the row layout to `sessionRailParts.tsx`. Focus remains a runtime
session choice; hierarchy and row identity come from the structural model.

### Conventions

The rail is a view over the model, not an alternate hierarchy builder. Runtime ancestry is available
only through the separate diagnostic projection.

### Invariants And Boundaries

- Replacement preserves the structural row and changes only its current occupant.
- Tree nesting follows sprint/master/leaf containment.
- Long live labels must remain on one line.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The component renders the structural rail model and focus behavior. | `SessionRail` | dashboard/src/panels/session-cockpit/SessionRail.tsx:160-241 |
| Row and tree composition is delegated to the shared rail body. | `RailBody` | dashboard/src/panels/session-cockpit/sessionRailParts.tsx:751-961 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-08-11T19:58+02:00 — Aligned the current dashboard card for `SessionRail.tsx` with its task-document, seat-state, and lifecycle interaction boundaries.
- 2026-08-10T04:39+02:00 — 260713-TES-L6: documented sprint-group rendering and the non-authoritative
  legacy bucket. Verification metadata remains pinned until closeout stamps the code commit.
- 2026-08-08T23:15+02:00 — 260713-TES-L1 completion round 3 (curator): body refreshed for the supervisor -> agent-notifier rename (citation ranges and/or rename wording); verification metadata pinned until closeout stamps the 260713-TES-L1 commit.

- 2026-08-07T08:19Z — 260731-EFA-L8 curator: recorded the sessionRailParts/sessionRailStyles extraction. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the superseded `(L…)`
  prose citations and the `n/a` rows with exact anchors and fixer-generated ranges; exact
  non-fixing check returns zero findings.

- 2026-07-26T15:40+0200 — 260718-CHATS-L7 curator: recorded the review-N1 tooltip asker fix — the
  `input?` chip's prompt preview now reads `sessionPendingInteractionPayload(session)` (parent's
  singular slot first, else the first multiplexed sub-agent entry) and prefixes the adapter-bound
  agent label (`<agentLabel>: <prompt>`) so the tooltip never implies the parent is asking. Also
  refreshed the self-reference range to the current 1115-line source. Source uncommitted;
  closeout re-stamps verification.

- 2026-07-24T13:17:17Z — Curator: corrected single-end behavior, narrowed poll subscriptions, and
  removed duplicated rail-bus chrome; verification fields remain pre-commit.

- 2026-07-21T05:30+02:00 — 260718-CHATS-L5P curator: recorded the responsive rail-row redesign (RV-2) —
  the `rowShell` is now a `flex-wrap:wrap` LABEL-group + ACTION-group layout where the action group
  wraps whole to a second line and stays single-line/reachable at 1440/1100/900/min-rail (4-width
  `cockpit.spec.ts` geometry pin); the `rowTitle` min-width floor was removed so it truly absorbs; the
  status chip elides and is DROPPED while armed (confirm copy carries the state). Also: R9 End demotion
  (muted→alarm on hover/focus/selected) + row hover feedback; R1/V12 nowrap on confirm/cancel/toggle;
  R8 `⇄ role view / ⇄ tree view` toggle affordance; R5/RV-4 humanized + `inbox clear` bus footer; V26
  end-truncated `leafCaption`. No model/effort leakage introduced. Verification pinned to the leaf base
  (`352d5cd`) until closeout stamps the candidate commit.
- 2026-07-18T07:22+02:00 — Curated the final same-reviewer-PASS FEUI-L8 behavior above using direct
  source/test/task evidence; no Domain Documentation source is configured.

- 2026-07-17T23:54+02:00 — 260715-FEUI-L7 aligned the rail's set-attention contract with the
  explicit `mark seen` action now shared by Evidence and background outcomes. Viewing/focusing
  stays non-acknowledging. Verification metadata remains pinned to the leaf base until closeout.
- 2026-07-17T08:33+02:00 — 260715-FEUI-L4 R6/R8 filled the reserved attention slot with the
  worded `set!` marker for unacknowledged evidence and named every rail dot `state: <word>` for
  assistive technology. The rail remains model/effort-value-free and never acknowledges on its
  own. Verification metadata is pinned to the contract base pending code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 (R5/R7; review finding 4 fixed in-leaf): single End
  now arms an inline honest confirm naming session · leaf · state and executes through
  `endSessionDetailed` (`endSession` signature: id → `OpenSession`; rail-only caller); a failed
  terminate POST renders verbatim with retry/dismiss as a `role="alert"` row; bulk end routes
  through `endLandedDetailed` and the route's own closed+skipped outcome renders as a
  dismissable note; legacy-raw bell markers (text-equivalent, cleared on focus) and labeled
  title/turn-hint tooltip parts joined the rows — the grammar dot stays pure.
- 2026-07-17T02:30+02:00 — Created for 260715-FEUI-L2 S4 (R5/R6/R8/R12/R13/R15/R16/R17, incl. fix
  round 1 findings 3 + 5): the ruled-hierarchy rail renderer — anatomy-exact rows with
  tooltip-backed truncation, hairline leaf clusters, collapsed completed folders, master+sprint
  bulk end with naming previews, the zero-state-suppressed attention strip with live-derived
  highlight expiry, gate/brief markers in the reserved slot, the poll-stale banner, the anchored
  bus footer, and the provenance-only spawn-tree toggle. Verification metadata pinned to the leaf
  base until closeout stamps the L2 code commit.
