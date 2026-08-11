# dashboard/src/data/conversation-library/client.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation-library/client.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[data/conversation-library overview](overview.md)

## Purpose

The HTTP client for the landed native-library routes (`serving/conversation/library/api.py`) under
`/api/harnesses/{harnessId}/conversations`. List and read are "or-null" reads (any failure collapses
to `null`, distinct from an empty success); open/open-status/open-reconcile return a typed
`OpenConversationOperation` as evidence. `fetch` is injected (`FetchLike`) so the store's suite drives
it without a network (design §9.4, §11.2).

## Code Commentary

### Logic

- **`libraryBase`** — builds the per-harness route root with an encoded `harnessId`. cit:([`libraryBase`], dashboard/src/data/conversation-library/client.ts:18-20)
- **`fetchLibraryList`** — `GET` the scoped list with optional `cwd`/`cursor`/`limit`;
  returns the `ConversationLibraryPage` or `null` on a non-OK response or transport throw. cit:([`fetchLibraryList`], dashboard/src/data/conversation-library/client.ts:36-54)
- **`fetchLibraryRead`** — `GET` one conversation's read-only historical page with optional
  `before`/`limit`; returns the `HistoricalConversationPage` or `null`. cit:([`fetchLibraryRead`], dashboard/src/data/conversation-library/client.ts:56-76)
- **`parseOpen`** — the discriminator — a body carrying both `outcome` and `phase` is the
  typed operation (`ok:true`); anything else is parsed into a typed `LibraryRouteError` (`ok:false`),
  defaulting `status:"transport"` and `detail:"HTTP <n>"`. A refusal is NEVER guessed into success. cit:([`parseOpen`], dashboard/src/data/conversation-library/client.ts:82-97)
- **`postOpen`** — the shared `POST` for `open`/`open-status`/`open-reconcile`; a network
  throw returns a `transport`/`network`/`httpStatus:0` typed error (still `ok:false`, never a fake row).
- **`openConversation`/`openStatus`/`openReconcile`** — the three exact-open verbs. cit:([`postOpen`], dashboard/src/data/conversation-library/client.ts:106-125)
  cit:([`openConversation`, `openStatus`, `openReconcile`], dashboard/src/data/conversation-library/client.ts:127-135; dashboard/src/data/conversation-library/client.ts:137-145; dashboard/src/data/conversation-library/client.ts:147-155)
  `openConversation` carries the full `OpenRequestBody` (`requestId`, `expectedIdentityDigest`, optional
  `cwd`/`launchContext`); launch context is a canonical `TaskDocumentRef` plus optional seat role,
  never a leaf-key address. Status/reconcile carry only `{ requestId }` — the caller-stable id is
  the correlation key.

### Invariants And Boundaries

- **Caller-stable requestId across the whole open lifecycle.** The id minted for `open` is reused
  verbatim by `open-status` and `open-reconcile`; a lost response is reconciled under the SAME id,
  never retried under a fresh one (§9.4, invariant 27). This client does not mint ids — the store owns
  that and threads it through.
- **List/read are honestly or-null**: a `null` return means "unavailable", NOT "empty" — the store
  renders `history unavailable for this harness` for `null` and an empty-scope copy for empty rows.
- **A refusal stays typed.** `parseOpen` never coerces a non-operation body into an operation, so an
  `unsupported`/`stale-identity`/`request-conflict` outcome reaches the UI as itself, without focusing
  or fabricating an opened session.

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
| The `FetchLike` injection type reused from the active-side client. | `FetchLike` | dashboard/src/data/conversation/client.ts:17-17 |
| The wire types this client returns (page/read/open/error). | `ConversationLibraryPage` | dashboard/src/data/conversation-library/types.ts:52-59 |
| The store orchestrating list/preview/open over this client. | `conversationLibraryStore` | dashboard/src/data/conversation-library/store.ts:77-84 |
| The landed native-library routes this client talks to. | `api_library_list` | mcp/src/agents_remember/serving/conversation/library/api.py:109-130 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History

- 2026-08-11T19:58+02:00 — Replaced the obsolete leaf-key launch-context implication with the
  current canonical task-document reference and optional seat-role contract.
- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 12 initial citation findings (3 anchor, 6 prose, 3 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the native-library HTTP
  client — or-null list/read, the typed open/open-status/open-reconcile verbs behind one caller-stable
  requestId, and the `parseOpen` discriminator that never guesses a refusal into success. Verification
  is pinned to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its
  first source stamp.
