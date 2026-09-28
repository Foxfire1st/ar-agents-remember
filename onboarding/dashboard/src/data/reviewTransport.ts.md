# dashboard/src/data/reviewTransport.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/reviewTransport.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The review reads' **one** transport decode: this route's typed answer whatever the HTTP status, or a
named failure that still carries the owner's own words. It is the new owner ICR-R16 created, and it
exists because of one measured, pre-existing defect rather than for symmetry: the review routes answer
with their typed result and map a refusal onto the change-set routes' `400`/`404`/`503` idiom
(`mcp/src/agents_remember/serving/review.py`), so a refusal arrives as a **non-2xx response whose body
is still this route's typed answer**. `getJson` — the shared client for the other serving routes — reads
only `body.status` and throws, which is right for those routes and dropped every typed review refusal
before a reader could see it: a reader saw `404 Not Found` where the route had published a missing
dataset, its reason and the initialization action.

Two boundaries decide its shape. It is **one decode per review read** — one GET, one body read, one
classification — and it **selects, ranks, computes and substitutes nothing**: a body that is not this
route's answer is reported as the failure it is (`unreadable`), never as an empty review, and a refusal
keeps the code, reason, offending input and next action the owner published. Unrelated clients'
semantics are untouched, and that is asserted rather than asserted-about: `getJson` keeps throwing on a
non-2xx for the routes that use it, which is why `data/changeset.ts` — a different route, a different
client and a different owner — is unchanged by this module (see the routed-debt row below).

## Code Commentary

### Logic

**`ReviewFailureToken` is the closed set of answers that are not a review, and it is wider than the
six states the packet names — deliberately.** `not-initialized`, `unavailable-history`, `validation`,
`authority` and `network` are the route's own vocabulary; `not-found` and `domain-refused` carry the
remaining codes verbatim rather than guessing them into a state; and the last two are the honest
fallbacks, because "an HTTP response that is not this route's answer" (`unreadable`) and "no HTTP
response at all" (`network`) are not the same failure and neither of them is a review. The surface's
`loading` and `known-empty` states are deliberately **not** members: they are not failures and are
rendered as themselves.

**`TOKEN_BY_CODE` is the only code→state table in the dashboard, and a code it does not know is never
guessed into a state.** The map is a `Record<string, ReviewFailureToken>` with
`reviewFailureToken(code)` returning `TOKEN_BY_CODE[code] ?? (code === "" ? "unreadable" :
"domain-refused")`. So an unrecognized refusal code keeps its own identity and is shown as a domain
refusal, and an empty code — a body that named no status at all — is `unreadable`. Both the entry bar
and the surface classify through this one function, which is what makes it impossible for the two to
come to disagree about what a code means.

**`ReviewFailure` is one failure in the owner's own terms.** `code` is the owner's identity for it and
is never re-spelled; `detail` is always present because a failure with no published reason is given the
one honest sentence this module can write (`the review route answered <status> with no refusal body, so
no reason was published`); `httpStatus` is present exactly when an HTTP response carried it. `expected`
and `offendingInput` are optional because the owner may not have published them, and `nextAction` is
optional because a `network` failure has no owner to publish one.

**`ReviewRefusalFacts` is declared structurally rather than imported, and that is what keeps the client
acyclic.** The typed refusal's wire fields (`code`, `detail`, `next_action`, optional
`offending_input`/`expected`, snake_case because that is what the model serializes) are re-declared here
so the import runs one way only: `data/review.ts` → here. A second import direction would make the pair
a cycle, because `review.ts` is the review client's public entry and this module is imported by it.

**`getReviewJson` is the one GET, and the body is read whatever the status.** It `fetch`es once; a
thrown `fetch` becomes `networkFailure(cause)` inside a `ReviewTransportError`; otherwise the body is
parsed with `response.json().catch(() => null)` and **a body whose `state` is a string is returned as
the answer** (`return body as T`). Everything else — including a 200 whose body carries no `state`, a
proxy page, an empty body — falls through to `failureFromBody`. The last case is load-bearing: a 200
with no `state` used to render a blank surface, and it is now a stated failure, so an unadmitted answer
can never be read as a review of an empty candidate.

**`namedFailure` is the single transport-level classification, and it is what makes an unrecognized
body honest.** `failureFromBody` reads the body's own `status` string and hands it to `namedFailure`,
which builds the status text (`<status> <statusText>`), takes the token from `reviewFailureToken`, and
fills `detail`/`offendingInput`/`expected`/`nextAction` from the body **only where the body published
them** — `offendingInput` also accepting the port's own `path` field, which is the spelling
`FileNotFoundError`'s body uses. A body with no `status` is `unreadable` with the HTTP status as its
code.

**`networkFailure` is a distinct type of failure, not a variant of the others.** It has no
`httpStatus`, its `code` is the literal `network`, and its detail names the cause
(`the review read could not reach the server: <message>`). That is the only token for which a retry is
offered anywhere on the surface, because it is the only one whose recovery route is not the owner's own
published next action.

**`intentOnlyRefusal` names the refusals that answer for the intent half alone.** The set is
`candidate_dataset_absent`, `comparison_refused` and `subject_unresolved`, and it exists because the
task's own source change inventory is measured from its two recorded Git trees and needs no dataset at
all. It is used to decide whether the surface may offer that inventory **as a separately asked
question** — never as an automatic substitution and never with a dataset this client chose.

**Three projections turn a refusal, an unadmitted answer or any thrown cause into the one `ReviewFailure`
shape the renderers take, and none of them invents anything.**
`reviewProblemFromRefusal(refusal)` re-uses the same `reviewFailureToken` classification so a typed
refusal and a transport body cannot disagree; it carries `httpStatus: undefined` because a typed refusal
is the route's answer rather than a status. `unreadableAnswer(state)` names the state it does not admit
in its own detail, with the state as its code. `reviewProblemFromCause(cause)` returns a
`ReviewTransportError`'s own `failure` and degrades anything else to `networkFailure` — the honest
reading of "something reached the caller instead of a response".

**`ReviewTransportError` stays a `FilesApiError` so an existing catcher keeps working, and it carries
the whole failure.** `super(failure.httpStatus ?? 0, failure.code)` keeps the older message idiom
(`<status> <code>`) and the older `instanceof` test intact; the added `readonly failure` is what lets a
caller render the refusal instead of only its status line.

### Conventions

The module imports exactly one thing — `FilesApiError` from `./files` — and declares everything else
itself. Its two non-exported helpers (`failureFromBody`, `namedFailure`) and its two exported
projections are plain functions; the one class is the error. Exported names are the vocabulary a
consumer needs (`ReviewFailureToken`, `ReviewFailure`, `ReviewRefusalFacts`, `ReviewTransportError`,
`getReviewJson`, `intentOnlyRefusal`, `reviewFailureToken`, `reviewProblemFromRefusal`,
`unreadableAnswer`, `reviewProblemFromCause`) and every one of them is re-exported from
`data/review.ts`, so `panels/review/*` and `panels/detail-panel/changeSetBar.tsx` keep importing one
public entry and no existing importer changed its import path. The `Review*` prefix keeps a review
display value distinguishable from the change-set client's own types, matching `data/review.ts`.

### Invariants And Boundaries

- **One decode per review read.** One GET, one body read, one classification; the only code→state table
  in `dashboard/src` is this module's `TOKEN_BY_CODE`, and the only review-route URL literals live in
  `data/review.ts`.
- **The body is the answer, whatever the status.** A body carrying this route's `state` is returned as
  the typed result — payload, subject list or refusal — and a 200 without one is a failure, never a
  successful empty answer.
- **Nothing is invented.** No recovery route, no dataset, no empty review: a failure the module cannot
  classify becomes `unreadable`, and a refusal keeps exactly the fields its owner published.
- **Unrelated clients' semantics are unchanged.** `data/files.ts` is untouched; `getJson` still throws
  on a non-2xx and still drops the body for the routes that use it.
- **A refusal's token is the same classification every other answer goes through.** `reviewFailureToken`
  is called from `namedFailure` and from `reviewProblemFromRefusal`, so the entry and the surface cannot
  classify one code two ways.
- **Boundary.** It owns the review route's *transport* — request shape, body admission and failure
  classification. It owns no rendered state (that is `panels/review/ReviewOutcome.tsx`), no route-side
  status mapping (that is `serving/review.py`'s `_status_for`) and no client request contract (that is
  `data/review.ts`).

### Todos

None recorded. Two facts this card records as routed rather than fixed, because they are other owners'
and outside this leaf's packet:

1. **The change-set client still swallows its own refusal detail, and that is a different route,
   client and owner.** `changeSetBar.tsx`'s live-leaf `committed`/`working` counter reads
   `data/changeset.ts` → `/api/changeset/task` through `getJson` and its rejection handler is
   `() => live && setCounters(null)`, so the counter simply disappears with no reason. That is the
   change-set client, not the review transport, and it is **routed to R12 (historical committed-leaf
   review) / R24 (usable review navigation)**. Measured in this leaf; not fixed here, to keep the blast
   radius to the review route.
2. **A retry is offered for `network` only.** That is a rule, not a gap: every other token has an
   owner-published `nextAction`, and offering a retry beside it would suggest the caller can clear a
   state only the owner can clear.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header, the failure
vocabulary and the one code→state table, the single GET, the three projections, the shared client whose
behaviour this module deliberately does not change, the client that delegates here, the two renderers
that consume the one failure shape, and the case module that drives the whole thing over real HTTP
bodies. Every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own record of the defect this module exists for, and of its two boundaries: the body is the answer whatever the status, and the shared client keeps throwing for the routes that use it.** | `getReviewJson` | dashboard/src/data/reviewTransport.ts:1-16; dashboard/src/data/reviewTransport.ts:161-171 |
| **The shared client whose throw-on-non-2xx idiom is right for the other serving routes and dropped this route's typed refusal whole: the behaviour this module deliberately does not change.** | `getJson`; `FilesApiError` | dashboard/src/data/files.ts:76-84; dashboard/src/data/files.ts:95-102 |
| **The failure vocabulary: one token per answer that is not a review, including the two honest fallbacks, and the explicit statement that `loading`/`known-empty` are not members.** | `ReviewFailureToken` | dashboard/src/data/reviewTransport.ts:27-45 |
| **One failure in the owner's own terms, with `code` never re-spelled and `httpStatus` present only when a response carried it.** | `ReviewFailure` | dashboard/src/data/reviewTransport.ts:49-57 |
| The typed refusal's wire fields, declared structurally so the import runs one way only. | `ReviewRefusalFacts` | dashboard/src/data/reviewTransport.ts:62-68 |
| **The only code→state table in the dashboard, and the classifier that carries an unknown code verbatim rather than guessing it into a state.** | `TOKEN_BY_CODE`; `reviewFailureToken` | dashboard/src/data/reviewTransport.ts:73-82; dashboard/src/data/reviewTransport.ts:97-98 |
| **The refusals that answer for the intent half alone, which is what licenses offering the task's source inventory as a separate question.** | `INTENT_ONLY_CODES`; `intentOnlyRefusal` | dashboard/src/data/reviewTransport.ts:89-93; dashboard/src/data/reviewTransport.ts:95-95 |
| The one error, staying a `FilesApiError` for existing catchers while carrying the whole failure. | `ReviewTransportError` | dashboard/src/data/reviewTransport.ts:102-107 |
| **The single transport-level classification: the body's own `status`, the optional fields read only where published, and `path` accepted as the port's own spelling of the offending input.** | `ReviewBody`; `namedFailure`; `failureFromBody` | dashboard/src/data/reviewTransport.ts:109-117; dashboard/src/data/reviewTransport.ts:125-127; dashboard/src/data/reviewTransport.ts:129-146 |
| **A failure with no HTTP response is its own token and carries no status.** | `networkFailure` | dashboard/src/data/reviewTransport.ts:148-156 |
| **The one GET: the body is read whatever the status, and a body carrying this route's `state` IS the answer.** | `getReviewJson` | dashboard/src/data/reviewTransport.ts:161-171 |
| **A typed refusal projected through the same classifier, so the entry and the surface cannot disagree about a code.** | `reviewProblemFromRefusal` | dashboard/src/data/reviewTransport.ts:176-183 |
| An answer whose `state` this client does not admit is named, never rendered as a review. | `unreadableAnswer` | dashboard/src/data/reviewTransport.ts:187-191 |
| Any thrown cause as a failure: the transport error's own, anything else as the network failure it must be. | `reviewProblemFromCause` | dashboard/src/data/reviewTransport.ts:195-196 |
| The three public client reads use the shared review transport. | `intentReview`; `intentReviewEntries`; `reviewSourceContent` | dashboard/src/data/review.ts:555-571; dashboard/src/data/review.ts:721-727; dashboard/src/data/review.ts:739-757 |
| **The rendered counterpart of this module's classification: one region for every state that is not a review, and one block carrying every field the owner published.** | `ReviewOutcomeRegion`; `ReviewProblemBlock` | dashboard/src/panels/review/ReviewOutcome.tsx:115-177; dashboard/src/panels/review/ReviewOutcome.tsx:226-260 |
| The task entry's brief word for the same tokens (`briefProblem`), shown on a control that never disappears, with the owner's full sentence in the disclosure beside it (`problemSentence`, since `260921-ICR-L47`). | `briefProblem`; `problemSentence`; `problem.token` | dashboard/src/panels/detail-panel/entryState.tsx:35-60 |
| **The routed debt this card records and does not fix: the counter read's own rejection handler drops the reason instead of carrying it.** | `setCounters`; `leafChangeset` | dashboard/src/panels/detail-panel/changeSetBar.tsx:12-104; dashboard/src/panels/detail-panel/changeSetBar.tsx:12-114 |
| The change-set client and the route the routed debt belongs to — a different client, a different route and a different owner from the review transport, which is why this leaf leaves it untouched. | `getJson`; `taskChangeset` | dashboard/src/data/changeset.ts:1-10; dashboard/src/data/changeset.ts:144-149; dashboard/src/data/changeset.ts:167-168; dashboard/src/data/changeset.ts:224-234 |
| **The cases that drive the real client functions against the measured route bodies, including the pair that shows `getJson` dropping the identical body this decode preserves.** | "resolves a 404 typed refusal through the review client, refusal intact"; "drops the same body through getJson: the shared client's semantics are unchanged"; "carries a transport-level refusal body's reason, offending input and next action"; "offers an explicit retry for a network failure, and the retry renders the answer" | dashboard/src/data/reviewTransport.test.ts:156-186; dashboard/src/data/reviewTransport.test.ts:217-236; dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:357-376 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The module talks to its own origin and names
one repository namespace in the query string.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T17:04:44+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **claim re-read and corrected.** The row about the entry bar's classification named `ReviewEntryState`, which L47 deleted; the entry now shows `briefProblem`'s word keyed on the same shared token and puts `problemSentence` in a disclosure. Reworded and re-cited to `panels/detail-panel/entryState.tsx`. This transport module is unchanged. No stamp advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Repointed shared catalogue/grouping ownership to the extracted source; source-review entry remains available independently of knowledge.
- 2026-09-25T23:58+02:00 — 260921-ICR-L25 curator, round 2 (uncommitted change set on `ar/260921-icr-l25-ar`, code base `d9e7e6e79ce532d16c689435ae95a63aab430f94` plus the working-tree delta, memory base `39adea206651654dbfacf2ee1bb4e2f3763b515b`; round-2 report `report-l25-round2.md` = `9446232d…`): **citation repair only; no claim about this module changed.** The row that names this file's own subject by contrast — the change-set client and the route the D01 debt belonged to — cited `data/changeset.ts` by four stale coordinates. They are re-derived against this tip: the file's header contract (`:1-10`), the `getChangeSetJson` reader the client's refusal idiom lives in (`:144-149`), and the two leaf helpers (`:167`, `:224-234`). The sentence's meaning is unchanged: this is a different client, route and owner from the review transport, and it is where D01 was carried and closed. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, so the governed closeout owns the real stamp. No commit was made.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **four enforced citation rows re-cited to the constructs they name, wording unchanged.** The public-entry row's four ranges were re-derived one per anchor against the current `data/review.ts`: `reviewSourceContent` `717-735`, `intentReview` `533-549`, `ReviewTransportError`'s re-export line `24-24` (the export block shifted by one), and `intentReviewEntries` `699-705` — each verified with `sed -n 'START,ENDp'` to carry the anchor it is cited for. No claim was reworded or dropped and no contributing range was removed. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **created.** The module is new in this leaf and this is its one-to-one card. It records what the decode is *for* rather than where its lines are: the measured pre-existing defect (the review route publishes its typed refusal in the body of a non-2xx response, and `getJson` read only `body.status` and threw, so the refusal was unreachable and a reader saw `404 Not Found`); the one GET whose body is the answer whatever the status, with a 200 that carries no `state` classified as a failure rather than as an empty review; the code→state table as the **only** one in `dashboard/src`, with an unknown code carried as `domain-refused` rather than guessed into a state; the two honest fallbacks (`unreadable` for a response this route did not produce, `network` for no response at all) and the statement that `loading`/`known-empty` are not failure members; the three projections that give every consumer one `ReviewFailure` shape; and the boundary that unrelated clients' semantics are untouched, which the case module asserts against the identical response. It also records, as **routed rather than fixed**, the change-set client's own swallowed refusal detail (`data/changeset.ts` → `getJson` → `/api/changeset/task`) to R12/R24 — a different route, client and owner, outside this packet's scope. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate at that base. Nothing in this leaf is committed, so no commit contains the bytes a stamp would claim to have verified; the `the recorded working candidate` row is the honest record and closeout owns the stamp.
