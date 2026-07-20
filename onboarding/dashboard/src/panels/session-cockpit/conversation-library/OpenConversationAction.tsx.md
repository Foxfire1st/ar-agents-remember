# dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/session-cockpit/conversation-library/OpenConversationAction.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[session-cockpit/conversation-library overview](overview.md)

## Purpose

`Open as new chat` — the SOLE resume action (design §4.4, §9.4, R4). It mints a caller-stable
`requestId`, sends the opaque conversation key + expected identity digest + cwd + launch context
through the library store's open flow, and reflects the exact open operation's phase/outcome/rollback.
It NEVER focuses anything itself; the parent focuses the new rail row only after the store reports
`openedForFocus` (`phase="opened" && outcome="opened"`) with catalog proof. Every other outcome leaves
the current chat, draft, focus, and scroll untouched.

## Code Commentary

### Logic

- **`newRequestId`** (L41-L47): a `crypto.randomUUID`-backed `open-…` id, generated once per open
  attempt and then reused across reconciliation (caller-stable — §9.4/invariant 27).
- **`busy` / `reconcilable`** (L92-L102, F6): `busy` runs from dispatch (`dispatching === true`)
  through non-terminal polling but NOT while exhausted or errored; `reconcilable` is the re-drivable
  state left by a transport failure (`error`) or a spent poll budget (`pollsExhausted`). The button
  disables while busy so a double-click cannot mint a second open into the L2.3 TOCTOU window.
- **`label`** (L104-L109): `Open as new chat` / `opening…` / `Reconcile open` / `… — unavailable`.
- **Focus-only-on-proof** (L112-L120, R4): the effect calls `onOpened(arSessionId)` ONLY when
  `open.openedForFocus` and an `arSessionId` is present — the exact opened catalog proof, §9.4 step 6.
- **`start`** (L122-L137): when `reconcilable`, it re-drives via `reconcileOpen` under the SAME
  `requestId` (F6a/F6b — a lost response is reconciled, never re-minted); otherwise `beginOpen` with a
  fresh id, the row's `identityDigest`, and the launch context.
- **`outcomeCopy`** (L49-L70): honest per-outcome copy for `pending`/`timeout-unknown`/`opened`/
  `unsupported`/`stale-identity`/`launch-failed`/`identity-mismatch`/`request-conflict`; the exhausted
  state prints `outcome unknown — reconcile under the same request`; a non-`not-needed` rollback is
  surfaced in alarm.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The library store open flow (`beginOpen`/`reconcileOpen`, `openedForFocus`, `dispatching`, `pollsExhausted`). | L11-L16 | [../../../data/conversation-library/store.ts](../../../data/conversation-library/store.ts) |
| The row wire type carrying `identityDigest`/`capabilities.resume`. | L17 | [../../../data/conversation-library/types.ts](../../../data/conversation-library/types.ts) |
| The surface that mounts this action for the selected row and receives `onOpened`. | L153-L162 | [ConversationLibrarySurface.tsx](ConversationLibrarySurface.tsx) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the sole resume action
  — caller-stable requestId reconciled under the same id (F6), focus a new rail row only on exact
  `opened` catalog proof (R4) with every other outcome surfaced in place, and the `dispatching`
  double-open guard. Verification is pinned to the leaf base (`0be0099`) because the new source file
  is uncommitted; closeout owns its first source stamp.
