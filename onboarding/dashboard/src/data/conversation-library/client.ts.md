# dashboard/src/data/conversation-library/client.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/conversation-library/client.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-20T22:30+02:00 |
| lastVerifiedCommitHash | `9e6c15d2b2bb663fcd10e26d77d0e4d2795829bd` |
| lastVerifiedCommitDate | 2026-07-20T22:32:02+02:00|
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

- **`libraryBase`** (L18-L20): builds the per-harness route root with an encoded `harnessId`.
- **`fetchLibraryList`** (L36-L54): `GET` the scoped list with optional `cwd`/`cursor`/`limit`;
  returns the `ConversationLibraryPage` or `null` on a non-OK response or transport throw.
- **`fetchLibraryRead`** (L56-L76): `GET` one conversation's read-only historical page with optional
  `before`/`limit`; returns the `HistoricalConversationPage` or `null`.
- **`parseOpen`** (L82-L97): the discriminator — a body carrying both `outcome` and `phase` is the
  typed operation (`ok:true`); anything else is parsed into a typed `LibraryRouteError` (`ok:false`),
  defaulting `status:"transport"` and `detail:"HTTP <n>"`. A refusal is NEVER guessed into success.
- **`postOpen`** (L106-L125): the shared `POST` for `open`/`open-status`/`open-reconcile`; a network
  throw returns a `transport`/`network`/`httpStatus:0` typed error (still `ok:false`, never a fake row).
- **`openConversation`/`openStatus`/`openReconcile`** (L127-L155): the three exact-open verbs.
  `openConversation` carries the full `OpenRequestBody` (`requestId`, `expectedIdentityDigest`, optional
  `cwd`/`launchContext`); status/reconcile carry only `{ requestId }` — the caller-stable id is the
  correlation key.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | `system/sources.md` checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The `FetchLike` injection type reused from the active-side client. | L6 | [../conversation/client.ts](../conversation/client.ts) |
| The wire types this client returns (page/read/open/error). | L8-L16 | [types.ts](types.ts) |
| The store orchestrating list/preview/open over this client. | — | [store.ts](store.ts) |
| The landed native-library routes this client talks to. | — | [library/api.py](agents-remember/mcp/src/agents_remember/serving/conversation/library/api.py) |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No applicable cross-repository source was found. | Import and task-boundary review | — |

## Update History

- 2026-07-20T22:30+02:00 — 260718-CHATS-L4 curator: created the sidecar for the native-library HTTP
  client — or-null list/read, the typed open/open-status/open-reconcile verbs behind one caller-stable
  requestId, and the `parseOpen` discriminator that never guesses a refusal into success. Verification
  is pinned to the leaf base (`0be0099`) because the new source file is uncommitted; closeout owns its
  first source stamp.
