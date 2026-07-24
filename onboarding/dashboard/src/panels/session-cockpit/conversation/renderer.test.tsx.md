# dashboard/src/panels/session-cockpit/conversation/renderer.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/renderer.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-24T13:17:17Z |
| lastVerifiedCommitHash | `842b487b854503d95c9c2d9dce1841198ba93c7d` |
| lastVerifiedCommitDate | 2026-07-24T17:08:25+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation overview](overview.md)

## Purpose

The rendered-grammar negative-proof suite (R3/R5/R7). It pins the feed ARIA honesty, image-reference
alt/provenance without a fabricated fetch URL, the real clamp button with an exact hidden-line count,
the source badge rule, the default-closed diagnostics drawer, and a structural axe pass over the
grammar.

## Code Commentary

### Logic

- **jsdom geometry shim** (L8-L12): jsdom has no layout engine, so `offsetHeight`/`offsetWidth` are
  stubbed (600/800) for this file so `@tanstack/react-virtual` measures a non-zero viewport and
  actually renders feed rows for the semantics assertions.
- **`ConversationTimeline` — role=feed (R5)** (L33-L68): a `role="feed"` exists; each `article`'s
  `aria-posinset` equals the server `globalOrdinal` (7/8, NEVER the array index), `aria-setsize` is
  present only when `totalItems` is known, and streaming articles carry `aria-live="off"`. The second
  case proves `aria-setsize` is OMITTED and the pager reads `total unknown` when the total is not
  honestly known.
- **`MessageItem` — grammar/images/clamp (R3)** (L70-L118): an `image-ref` renders a non-empty
  accessible alt + provenance and NO `<img>` (no invented `/api/assets` URL — F11); a long completed
  assistant message clamps behind a real `<button aria-expanded>` whose label carries an exact
  `+N lines` count; an agent-bus delivery is source-badged (`agent bus`) while an ordinary operator
  message is not (badge only when origin changes interpretation).
- **`TerminalDiagnosticsDrawer` — default off (R2/R7)** (L120-L130): closed by default →
  `data-open="false"`, `aria-hidden="true"`, `inert`, and NO PTY frame mounted (the R7 negative proof).
- **`ConversationTimeline` — 10k tool-heavy DOM/interaction baseline (R5.2/R5.10, L4.4)** (added by
  260718-CHATS-L5, L132-L217): mounts 10,000 rotating message/thinking/tool-call/tool-result items
  through the landed L4 renderer + `@tanstack/react-virtual`. The load-bearing invariant is that the
  mounted DOM is virtualized by stable item and stays BOUNDED regardless of history depth — the
  standing tripwire asserts the `[data-conversation-item]` count `> 0`, `< 80`, AND `< total/100`, so
  the feed can never degrade into a 10k-node tree; `aria-posinset` still rides the 1-based server
  `globalOrdinal` (never the array index), `aria-setsize="10000"` is the honest total, and
  `aria-live="off"` rides the row. A generous `mount < 3000 ms` ceiling is an interaction tripwire
  for shared-runner jitter (recorded 260718-CHATS-L5: 10 mounted articles / ~42–55 ms). A second
  `it` runs `axe.run` over the 10k feed (contrast/region disabled) and asserts zero violations at
  depth. This is the L4.4 artifact L4 explicitly deferred ("the measured DOM/interaction baseline is
  an L5 artifact").
- **axe** (final describe): `axe.run` over a small feed + closed drawer with `color-contrast`/`region`
  disabled (jsdom has no rendered geometry) asserts zero structural violations.

### Invariants And Boundaries

- `aria-posinset` is the server ordinal, not the array index; `aria-setsize` appears only with an
  honest total; the clamp count is exact — these are the R5 honesty assertions.
- The diagnostics drawer mounts NO content when closed — the R7 default-off proof.
- The 10k baseline's guarded invariant is DOM-boundedness (mounted `< 80` AND `< total/100`), not the
  ms figure; degrading virtualization fails it loudly. The `mount < 3000 ms` ceiling and the recorded
  ~42–55 ms are jsdom tripwires only, not a hardware ranking — a real-layout supersede is a recorded
  second-half item (L5.R4).
- The axe pass is structural only (contrast/region disabled) because jsdom cannot lay out geometry.

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
| The virtualized feed under test (posinset/setsize/live). | L15 | [ConversationTimeline.tsx](ConversationTimeline.tsx) |
| The message item under test (image ref, clamp, source badge). | L16 | [MessageItem.tsx](MessageItem.tsx) |
| The default-off diagnostics drawer under test. | L17 | [TerminalDiagnosticsDrawer.tsx](TerminalDiagnosticsDrawer.tsx) |
| The item wire type the fixtures build. | L14 | [../../../data/conversation/types.ts](../../../data/conversation/types.ts) |
| The axe-core dev dependency this suite requires (added by the leaf). | L1 | [../../../../package.json](../../../../package.json) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Current L5I Maintenance

The renderer suite gained the browser-sensitive regression matrix for scroll memory: middle/top and
bottom restoration, later inflow at bottom, geometry settling, hidden collapse clamps, trusted-user
override, virtual measurement shifts, and the persistent latest control. It also retains focused
renderer/a11y coverage for the conversation grammar.

## Update History

- 2026-07-24T13:17:17Z — Curator: recorded the scroll-restoration regression matrix and latest-chip
  behavior; verification fields remain pre-commit.

- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: recorded the 10k tool-heavy DOM/interaction
  baseline + axe tripwire this leaf added (the L4.4 artifact L4 deferred) — the bounded-mounted-DOM
  invariant (`< 80` and `< total/100`), the honest 1-based posinset / `aria-setsize="10000"` /
  `aria-live="off"`, the `mount < 3000 ms` jsdom interaction ceiling, and axe-clean at depth;
  recorded baseline 10 mounted rows / ~42–55 ms. Verification stays pinned at the leaf base
  (`9e6c15d`) because the L5 change to this file is uncommitted; closeout owns its source stamp.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the rendered-grammar
  negative-proof suite — feed posinset=server-ordinal / honest setsize / `total unknown`, image
  alt+provenance with no fabricated fetch URL (F11), exact-count clamp button, source-badge rule,
  default-off/inert diagnostics (R7), and the structural axe pass. Verification is pinned to the leaf
  base (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
