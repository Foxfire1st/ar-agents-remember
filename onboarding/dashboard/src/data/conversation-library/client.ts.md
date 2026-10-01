# dashboard/src/data/conversation-library/client.ts

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

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The `FetchLike` injection type reused from the active-side client. [1]
- The wire types this client returns (page/read/open/error). [2]
- The store orchestrating list/preview/open over this client. [3]
- The landed native-library routes this client talks to. [4]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
