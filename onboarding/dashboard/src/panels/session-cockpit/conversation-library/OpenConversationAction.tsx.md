# dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

`Open as new chat` — the SOLE resume action (design §4.4, §9.4, R4). It mints a caller-stable
`requestId`, sends the opaque conversation key + expected identity digest + cwd + a typed launch
context carrying the task-document reference and optional seat role through the library store's
open flow, and reflects the exact open operation's phase/outcome/rollback.
It NEVER focuses anything itself; the parent focuses the new rail row only after the store reports
`openedForFocus` (`phase="opened" && outcome="opened"`) with catalog proof. Every other outcome leaves
the current chat, draft, focus, and scroll untouched.

## Code Commentary

### Logic

- **`newRequestId`**: an `open-…` id backed by `crypto.randomUUID` when available and by a
  `Date.now`/`Math.random` fallback otherwise, generated once per open
  attempt and then reused across reconciliation (caller-stable — §9.4/invariant 27; cit:([`newRequestId`], dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx:41-47)).
- **`busy` / `reconcilable`** (L92-L102, F6): `busy` runs from dispatch (`dispatching === true`)
  through non-terminal polling but NOT while exhausted or errored; `reconcilable` is the re-drivable
  state left by a transport failure (`error`) or a spent poll budget (`pollsExhausted`). The button
  disables while busy so a double-click cannot mint a second open into the L2.3 TOCTOU window.
- **`label`**: `Open as new chat` / `opening…` / `Reconcile open` / `… — unavailable` (cit:([`label`], dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx:98-101)).
- **Focus-only-on-proof** (L112-L120, R4): the effect calls `onOpened(arSessionId)` ONLY when
  `open.openedForFocus` and an `arSessionId` is present — the exact opened catalog proof, §9.4 step 6.
- **`start`**: when `reconcilable`, it re-drives via `reconcileOpen` under the SAME
  `requestId` (F6a/F6b — a lost response is reconciled, never re-minted); otherwise `beginOpen` with a
  fresh id, the row's `identityDigest`, and the launch context (cit:([`start`], dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx:122-137)).
- **`outcomeCopy`**: honest per-outcome copy for `pending`/`timeout-unknown`/`opened`/
  `unsupported`/`stale-identity`/`launch-failed`/`identity-mismatch`/`request-conflict`; the exhausted
  state prints `outcome unknown — reconcile under the same request`; a non-`not-needed` rollback is
  surfaced in alarm (cit:([`outcomeCopy`], dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx:49-70)).

### Invariants And Boundaries

- Resume is the only mutation this component can cause, and it only focuses the new session on exact
  `opened` catalog proof (R4). Any non-opened outcome is surfaced *in place* and leaves the current
  chat/draft/focus/scroll intact — this is the R4 focus-discipline contract.
- The minted `requestId` is retained across transport-failure/poll-exhaustion retries and reconciled
  under the same id (never a fresh id), and `dispatching` blocks a double-open (F6).
- A hard-`unavailable` resume capability disables the button and shows `resume.reason`.

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The library store open flow (`beginOpen`/`reconcileOpen`, `openedForFocus`, `dispatching`, `pollsExhausted`). | `OpenTracker`, `beginOpen`, `reconcileOpen` | dashboard/src/data/conversation-library/store.ts:51-63; dashboard/src/data/conversation-library/store.ts:229-263; dashboard/src/data/conversation-library/store.ts:269-291 |
| The row wire type carrying `identityDigest`/`capabilities.resume`. | `ConversationLibraryRow`, `HistoryCapabilities` | dashboard/src/data/conversation-library/types.ts:18-24; dashboard/src/data/conversation-library/types.ts:26-36 |
| The surface declares `onOpened`, mounts this action for the selected row, and forwards the callback. | `ConversationLibrarySurface` | dashboard/src/panels/session-cockpit/conversation-library/ConversationLibrarySurface.tsx:75-171 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Clarified that conversation resume forwards canonical task-document
  identity and optional seat role, not leaf-key addressing.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this sidecar against the frontend-rail change set (strict-target lint remediation: complexity, max-lines-per-function, react-hooks, jsx-a11y, and import-cycle fixes). No content impact: behavior-preserving refactor; the file's responsibilities and the claims in this card remain current. Verification metadata stays pinned until closeout stamps the code commit.

- 2026-08-04T03:21:00+02:00 — S18-SR3-B05 curator: regenerated the assigned whole-claim binding with the locked scoped fixer and inspected the generated extent against the approved claim; no approved semantic claim changes.
- 2026-08-04T03:03:32+02:00 — S18-SR3-B05 worker: selected the surface function as the whole-claim anchor and returned its declaration, mount, and callback-forwarding binding to provisional fixer input.
- 2026-08-04T02:35:12+02:00 — S18-B05 curator delta: resolved provisional source-local citation bindings with fixer-generated current-source ranges; no approved semantic claim changes.
- 2026-08-04T01:28:33+02:00 — S18-SR2-B05 worker: documented the request-id fallback as well as `crypto.randomUUID`, and added a provisional binding for the surface's actual action mount/callback forwarding.
- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the sole resume action
  — caller-stable requestId reconciled under the same id (F6), focus a new rail row only on exact
  `opened` catalog proof (R4) with every other outcome surfaced in place, and the `dispatching`
  double-open guard. Verification is pinned to the leaf base (`0be0099`) because the new source file
  is uncommitted; closeout owns its first source stamp.
