# dashboard/src/data/reviewTransport.test.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewTransport.test.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c` |
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The transport contract case module for ICR-R16, at the review client's HTTP boundary: **the route's
typed refusal is read out of a non-2xx response, and everything that is not that answer is named.**

It exists to pin one measured defect and the ten states that replace it. The real client functions
(`intentReview`, `intentReviewEntries`, `reviewSourceContent`) and the real shared decode
(`data/reviewTransport.ts`) are exercised; only `fetch` is stubbed, so the URL, the status and the body
all travel the way the browser's do. The first two cases are the defect as a pair over **one identical
response** — read through the review client it resolves with the refusal intact; read through `getJson`
it still throws and still drops the body — which is what makes "unrelated clients' semantics are
unchanged" an assertion about behaviour rather than a claim about a diff.

Its refusal bodies are not authored fixtures. Every one is the measured output of the REAL route over
REAL HTTP in this leaf's evidence run (`ar-coordination/temp/icr/evidence-l16-refusals.txt`,
`probe-l16-real-route.py`): the production ports inside `cli.dashboard.create_app`, driven against a
real never-initialized leaf enclosure built by the shipped test support. The module header records that
provenance and the `sha256-normalized` digest of each body it copied, so a reader can re-measure the
fixture rather than trust it.

## Code Commentary

### Logic

**The five measured bodies are declared once, with their digests in the comments above them.** The
subject review's `404` (`candidate_dataset_absent`, digest `834c79f4…`), the entry read's `404` for the
same task (`fdbabc97…`), the route's `400` for a selector it does not admit (`bad-request`), its `503`
for a process composed without an adapter (`unavailable`) and its `400` for a refused authority
(`bad-path`) — plus the expansion read's `400` (`source_content_unresolved`). **The expansion refusal was
re-measured by MIK-L31** (ICR-L43 review R2 O2, routed to MIK-R31 rule 6): the pre-L43 text ("is not one of the 6
changed path(s) …; an entry is expanded from the inventory's own measurement …") was stale after ICR-L43 added the
attributed-unchanged admission, so the body is now the real route's answer on MIK-L31's converted scratch leaf with
the leaf's own code (`capture_refusal.py`; repository id and scratch paths normalized; sha256 of the normalized body
`56cd4625…`): 1 changed path measured, "no realization recorded in the comparison's knowledge links it" with both
snapshots' answers, and the next action naming "one a realization of this comparison records". The worker's script
check found the detail and next action byte-equal to the measured body. A fixture carrying a
digest is a fixture a reader can check, which is the point: the packet explicitly refuses
"tests that merely mirror implementation or assert returned prebuilt payloads".

**`serving(status, body, statusText)` is the one stub, and it is a fetch stub rather than a client
stub.** It replaces the global `fetch` with a function returning a real-shaped `Response` carrying the
given status, status text and JSON body, so the status, the body and the decode all travel the real
path. **`failureOf(call)` is the one way a failure is read**: it awaits the call, converts a thrown
cause through `reviewProblemFromCause`, and throws an explicit `the read resolved; a failure was
expected` if the call succeeds — so a case cannot silently pass on a resolution that should have been
a failure.

**`describe("the review route's typed answer, whatever the status")` pins the four answers that are
the route's own.** A `404` typed refusal resolves through `intentReview` with its refusal intact; the
**identical** body through `getJson` still throws `FilesApiError` and the refusal is unreachable (the
control for the whole module); the entry read's and the expansion read's typed refusals resolve the
same way through their own client functions, so the one decode is proven to serve all three reads; and
an ordinary `200` typed answer still resolves as itself — the fix did not turn success into a special
case.

**`describe("what is not this route's typed answer")` pins each distinct failure, one token at a
time.** `bad-request` becomes `validation` with the owner's `detail`, `offendingInput`, `expected` and
`nextAction` all carried; the `503` unwired body becomes `unavailable-history` with the action that
wires the adapter; `bad-path` becomes `authority` and is asserted **not** to be a network or review
failure; a `502` HTML proxy page becomes `unreadable` with the HTTP status as its code and a detail
saying no refusal body was published; and a `fetch` that throws becomes `network` with **no**
`httpStatus` and **no** `nextAction`, because nothing in that path invents a recovery route. The last
case asserts the thrown error is a `ReviewTransportError` **and** a `FilesApiError`, with the older
`<status> <code>` message idiom intact, so a catcher written before this leaf keeps working.

### Conventions

The module imports the three real client functions and the transport error from the public entries
(`./review`, `./reviewTransport`) and `FilesApiError`/`getJson` from `./files` — it declares no
production behaviour of its own. Constants are upper-case (`REPO`, `MASTER`, `LEAF`, `SUBJECT`, the
five bodies); `intentUrl` is the one spelled URL and is the literal the route serves. Helpers are
lower-case plain functions and every case is an `async` `it` inside one of two `describe` blocks, with
`afterEach(() => vi.unstubAllGlobals())` restoring the global fetch. Assertions read the returned
typed result or the carried `ReviewFailure`'s own fields rather than any re-derived local value.

### Invariants And Boundaries

- **The bodies are measured, not authored.** Each fixture's digest is the evidence run's
  `sha256-normalized` value, quoted in the module header and above the fixture.
- **Only `fetch` is stubbed.** The client functions, the shared decode and the URL construction are the
  real ones, so the assertions are about the shipped path.
- **The `getJson` control asserts a negative.** The case that proves unrelated clients are unchanged
  asserts the throw and the dropped body, not merely their absence.
- **Every failure token is pinned by a case that names it.** `validation`, `unavailable-history`,
  `authority`, `unreadable` and `network` each have a case; no token is asserted only in prose.
- **`network` carries no recovery route.** The case asserts `httpStatus` and `nextAction` are
  `undefined`, so a retry offered for a socket failure stays the surface's decision rather than
  something the transport fabricated.
- **Boundary.** It pins the transport contract of the review reads. It does not drive the surface (that
  is `ReviewSurface.outcomes.test.tsx`), the entry bar (`reviewEntryRefusal.test.tsx`) or the expansion
  pane (`SourceContentRefusal.test.tsx`), and it does not re-measure the route itself (that is the
  Python transport module and this leaf's evidence run).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own provenance header, the
five measured bodies with their digests, the two helpers, and the ten cases that pin the typed answer
and every non-answer. Every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own provenance: the real client functions and the real decode, with only `fetch` stubbed, and each body's measured digest.** | `intentReview`; `intentReviewEntries`; `reviewSourceContent`; `getJson` | dashboard/src/data/reviewTransport.test.ts:1-28 |
| The three real client functions and the error type under test, imported from the public entries. | `intentReview`; `intentReviewEntries`; `reviewSourceContent`; `ReviewTransportError` | dashboard/src/data/reviewTransport.test.ts:25-28 |
| **The measured bodies, each carrying the digest of the run that produced it.** | `DATASET_ABSENT`; `ENTRIES_DATASET_ABSENT`; `BAD_REQUEST`; `UNWIRED`; `BAD_PATH`; `SOURCE_CONTENT_REFUSED` | dashboard/src/data/reviewTransport.test.ts:37-50; dashboard/src/data/reviewTransport.test.ts:54-73; dashboard/src/data/reviewTransport.test.ts:78-88; dashboard/src/data/reviewTransport.test.ts:93-99; dashboard/src/data/reviewTransport.test.ts:104-110; dashboard/src/data/reviewTransport.test.ts:117-135 |
| The expansion refusal re-measured by MIK-L31 on its converted scratch leaf, with its normalized digest. | "re-measured by MIK-L31"; `SOURCE_CONTENT_REFUSED` | dashboard/src/data/reviewTransport.test.ts:112-135 |
| The one spelled URL, which is the literal the route serves. | `intentUrl` | dashboard/src/data/reviewTransport.test.ts:137-137 |
| **The one stub, replacing the global `fetch` with a real-shaped response so status, body and decode all travel the real path.** | `serving` | dashboard/src/data/reviewTransport.test.ts:139-146 |
| **The one way a failure is read, which fails loudly if the read resolves instead.** | `failureOf` | dashboard/src/data/reviewTransport.test.ts:148-155 |
| The restore of the global fetch between cases. | `afterEach` | dashboard/src/data/reviewTransport.test.ts:22-28; dashboard/src/data/reviewTransport.test.ts:152-155 |
| **The defect as a pair over one identical response: the review client resolves with the refusal intact, and `getJson` still throws with the body dropped.** | "resolves a 404 typed refusal through the review client, refusal intact"; "drops the same body through getJson: the shared client's semantics are unchanged" | dashboard/src/data/reviewTransport.test.ts:156-186 |
| **One decode serving all three reads: the entry and expansion typed refusals resolve the same way, and an ordinary 200 answer still resolves as itself.** | "resolves the entry read's and the expansion read's typed refusals the same way"; "still resolves an ordinary 200 typed answer" | dashboard/src/data/reviewTransport.test.ts:187-215 |
| **The transport-level body carried whole: token, code, status, reason, offending input, expected and next action.** | "carries a transport-level refusal body's reason, offending input and next action" | dashboard/src/data/reviewTransport.test.ts:217-235 |
| The unwired adapter as unavailable history, with the action that wires it. | "names an unwired adapter as unavailable history, with the action that wires it" | dashboard/src/data/reviewTransport.test.ts:242-252 |
| **A refused authority as its own state rather than as a network or review failure.** | "names a refused authority as its own state, not as a network or review failure" | dashboard/src/data/reviewTransport.test.ts:254-263 |
| **A response this route did not produce is `unreadable`, with the HTTP status as its code and a detail saying no reason was published.** | "names an HTTP response this route did not produce as unreadable" | dashboard/src/data/reviewTransport.test.ts:265-280 |
| **A socket that never answered is `network`, carrying no status and no invented next action.** | "names a socket that never answered as a network failure" | dashboard/src/data/reviewTransport.test.ts:282-298 |
| **The thrown error stays a `FilesApiError` with the older message idiom, so an existing catcher keeps working.** | "throws the review transport error, which stays a FilesApiError for existing catchers" | dashboard/src/data/reviewTransport.test.ts:295-304 |
| The decode these cases pin, and the error whose type the existing catchers keep. | `getReviewJson`; `ReviewTransportError` | dashboard/src/data/reviewTransport.ts:102-107; dashboard/src/data/reviewTransport.ts:161-171 |
| **The shared client the control case proves unchanged: it still reads only `body.status` and still throws on a non-2xx.** | `getJson`; `FilesApiError` | dashboard/src/data/files.ts:76-84; dashboard/src/data/files.ts:95-102 |
| **The mounted counterpart that consumes the same classification, so the transport contract and the rendered states are pinned against one table.** | `ReviewOutcomeRegion`; `ReviewProblemBlock` | dashboard/src/panels/review/ReviewOutcome.tsx:115-177; dashboard/src/panels/review/ReviewOutcome.tsx:247-278 |

## Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed
same-origin `fetch` and names one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Logic records the expansion refusal re-measured on the real route by MIK-L31 (MIK-R31 rule 6, ICR-L43 review R2 O2: the stale pre-L43 text refreshed, digest `56cd4625…`); one row added.
- 2026-09-30T07:50:00+00:00: Generated citation repair: `intentUrl` repointed to dashboard/src/data/reviewTransport.test.ts:137-137. No content impact: mechanical anchor-range projection bound to citation source snapshot ec86d6994b129f2dd70f55d74cafd3553485138e204193855095f327a179d4d0; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **created.** The module is new in this leaf and this is its one-to-one card. It records what the cases are *for* — one measured defect (the typed refusal in the body of a non-2xx response was unreachable through `getJson`) and the ten states that replace it — and, more usefully for a later reader, the module's own evidentiary discipline: every refusal body is the measured output of the real route over real HTTP in this leaf's evidence run with its `sha256-normalized` digest quoted in the source, only `fetch` is stubbed, and the "unrelated clients unchanged" claim is asserted as a negative over the **identical** response rather than inferred from a diff. The card also names the deliberate holes: `network` is asserted to carry no `httpStatus` and no invented `nextAction`, and the thrown error is asserted to remain a `FilesApiError`. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate at that base. Nothing in this leaf is committed, so no commit contains the bytes a stamp would claim to have verified; closeout owns the stamp.
