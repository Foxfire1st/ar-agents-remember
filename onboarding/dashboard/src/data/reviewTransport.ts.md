# dashboard/src/data/reviewTransport.ts

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The one transport decode of the review reads. A review route answers with its typed result whatever the
HTTP status, so this module reads the body once and classifies it: a body with a `state` is the route's
answer, and anything else is a named failure that keeps the owner's code, reason, offending input and
next action. It selects, ranks and substitutes nothing.

## Code Commentary

- `getReviewJson<T>(url, signal?)` makes the one GET. A request that fails to reach the server throws
  `ReviewTransportError` with the token `network`. A body that carries a string `state` is returned as
  the answer, also on a non-2xx status. Any other response throws with the failure built from the body's
  `status`, or as `unreadable` when the body has none.
- When a caller passes `signal`, it is handed to `fetch`. Aborting it cancels the request itself; the
  server sees a disconnect and stops the work it was doing for that request. Without a signal `fetch` is
  called with the URL alone.
- `ReviewFailureToken` is the set of states a reader is shown for an answer that is not a review:
  `not-initialized`, `unavailable-history`, `validation`, `authority`, `not-found`, `domain-refused`,
  `network` and `unreadable`.
- `TOKEN_BY_CODE` maps the route's status strings and refusal codes to a token.
  `candidate_dataset_absent` is `not-initialized`. `candidate_not_live`, `candidate_unresolved`,
  `review_adapter_unavailable`, `reviewer_busy`, `inputs_changing` and `unavailable` are
  `unavailable-history`. `bad-request` is `validation`, `bad-path` is `authority`, `not-found` is
  `not-found`. `reviewFailureToken` gives every other non-empty code `domain-refused`, with the code kept,
  and an empty code `unreadable`.
- `reviewer_busy` and `inputs_changing` are answered only by the leaf-wide tree view. Both are transient;
  the reader of that view retries them (`reviewTrees.ts`).
- `intentOnlyRefusal(code)` is true for `candidate_dataset_absent`, `comparison_refused` and
  `subject_unresolved`: refusals of the intent half alone, after which a caller may offer the source
  inventory as a separately asked question.
- `ReviewTransportError` extends `FilesApiError` and carries the whole `ReviewFailure`.
- `reviewProblemFromRefusal` turns a typed refusal into a failure with its fields unchanged;
  `unreadableAnswer` names a `state` this client does not admit; `reviewProblemFromCause` turns any thrown
  cause into a failure.

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

2. **A retry is offered for `network` only.** That is a rule, not a gap: every other token has an
   owner-published `nextAction`, and offering a retry beside it would suggest the caller can clear a
   state only the owner can clear.

## Evidence

- The module comment: one decode per read, and nothing is selected or substituted. [21]
- The tokens a reader can be shown. [22]
- The codes and their tokens, with the two transient codes of the leaf-wide view. [23]
- The refusals of the intent half alone. [24]
- The error a review read throws. [25]
- The one GET: the optional abort signal, the body read whatever the status, and the two failures. [26]
- A typed refusal becomes a failure with its fields unchanged. [27]
- A superseded request's signal is aborted. [28]

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header, the failure
vocabulary and the one code→state table, the single GET, the three projections, the shared client whose
behaviour this module deliberately does not change, the client that delegates here, the two renderers
that consume the one failure shape, and the case module that drives the whole thing over real HTTP
bodies. Every anchor in a row occurs inside the range that row cites.

- **The header's own record of the defect this module exists for, and of its two boundaries: the body is the answer whatever the status, and the shared client keeps throwing for the routes that use it.** [29]
- **The shared client whose throw-on-non-2xx idiom is right for the other serving routes and dropped this route's typed refusal whole: the behaviour this module deliberately does not change.** [30]
- **The failure vocabulary: one token per answer that is not a review, including the two honest fallbacks, and the explicit statement that `loading`/`known-empty` are not members.** [31]
- **One failure in the owner's own terms, with `code` never re-spelled and `httpStatus` present only when a response carried it.** [32]
- The typed refusal's wire fields, declared structurally so the import runs one way only. [33]
- **The only code→state table in the dashboard, and the classifier that carries an unknown code verbatim rather than guessing it into a state.** [34]
- **The refusals that answer for the intent half alone, which is what licenses offering the task's source inventory as a separate question.** [35]
- The one error, staying a `FilesApiError` for existing catchers while carrying the whole failure. [36]
- **The single transport-level classification: the body's own `status`, the optional fields read only where published, and `path` accepted as the port's own spelling of the offending input.** [37]
- **A failure with no HTTP response is its own token and carries no status.** [38]
- **The one GET: the body is read whatever the status, and a body carrying this route's `state` IS the answer.** [39]
- **A typed refusal projected through the same classifier, so the entry and the surface cannot disagree about a code.** [40]
- An answer whose `state` this client does not admit is named, never rendered as a review. [41]
- Any thrown cause as a failure: the transport error's own, anything else as the network failure it must be. [42]
- The three public client reads use the shared review transport. [43]
- **The rendered counterpart of this module's classification: one region for every state that is not a review, and one block carrying every field the owner published.** [44]
- The task entry's brief word for the same tokens (`briefProblem`), shown on a control that never disappears, with the owner's full sentence in the disclosure beside it (`problemSentence`, since `260921-ICR-L47`). [45]
- The change-set client and the route the routed debt belongs to — a different client, a different route and a different owner from the review transport, which is why this leaf leaves it untouched. [46]
- **The cases that drive the real client functions against the measured route bodies, including the pair that shows `getJson` dropping the identical body this decode preserves.** [47]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The module talks to its own origin and names
one repository namespace in the query string.

No meaningful cross-repo references found.
