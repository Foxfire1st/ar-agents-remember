# dashboard/src/panels/session-cockpit/conversation/renderer.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation/renderer.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
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
- **axe** (L132-L152): `axe.run` over a small feed + closed drawer with `color-contrast`/`region`
  disabled (jsdom has no rendered geometry) asserts zero structural violations.

### Invariants And Boundaries

- `aria-posinset` is the server ordinal, not the array index; `aria-setsize` appears only with an
  honest total; the clamp count is exact — these are the R5 honesty assertions.
- The diagnostics drawer mounts NO content when closed — the R7 default-off proof.
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

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the rendered-grammar
  negative-proof suite — feed posinset=server-ordinal / honest setsize / `total unknown`, image
  alt+provenance with no fabricated fetch URL (F11), exact-count clamp button, source-badge rule,
  default-off/inert diagnostics (R7), and the structural axe pass. Verification is pinned to the leaf
  base (`0be0099`) because the new source file is uncommitted; closeout owns its first source stamp.
