# dashboard/src/data/reviewTransport.ts

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

## Evidence

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

- **The header's own record of the defect this module exists for, and of its two boundaries: the body is the answer whatever the status, and the shared client keeps throwing for the routes that use it.** [1]
- **The shared client whose throw-on-non-2xx idiom is right for the other serving routes and dropped this route's typed refusal whole: the behaviour this module deliberately does not change.** [2]
- **The failure vocabulary: one token per answer that is not a review, including the two honest fallbacks, and the explicit statement that `loading`/`known-empty` are not members.** [3]
- **One failure in the owner's own terms, with `code` never re-spelled and `httpStatus` present only when a response carried it.** [4]
- The typed refusal's wire fields, declared structurally so the import runs one way only. [5]
- **The only code→state table in the dashboard, and the classifier that carries an unknown code verbatim rather than guessing it into a state.** [6]
- **The refusals that answer for the intent half alone, which is what licenses offering the task's source inventory as a separate question.** [7]
- The one error, staying a `FilesApiError` for existing catchers while carrying the whole failure. [8]
- **The single transport-level classification: the body's own `status`, the optional fields read only where published, and `path` accepted as the port's own spelling of the offending input.** [9]
- **A failure with no HTTP response is its own token and carries no status.** [10]
- **The one GET: the body is read whatever the status, and a body carrying this route's `state` IS the answer.** [11]
- **A typed refusal projected through the same classifier, so the entry and the surface cannot disagree about a code.** [12]
- An answer whose `state` this client does not admit is named, never rendered as a review. [13]
- Any thrown cause as a failure: the transport error's own, anything else as the network failure it must be. [14]
- The three public client reads use the shared review transport. [15]
- **The rendered counterpart of this module's classification: one region for every state that is not a review, and one block carrying every field the owner published.** [16]
- The task entry's brief word for the same tokens (`briefProblem`), shown on a control that never disappears, with the owner's full sentence in the disclosure beside it (`problemSentence`, since `260921-ICR-L47`). [17]
- **The routed debt this card records and does not fix: the counter read's own rejection handler drops the reason instead of carrying it.** [18]
- The change-set client and the route the routed debt belongs to — a different client, a different route and a different owner from the review transport, which is why this leaf leaves it untouched. [19]
- **The cases that drive the real client functions against the measured route bodies, including the pair that shows `getJson` dropping the identical body this decode preserves.** [20]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The module talks to its own origin and names
one repository namespace in the query string.

No meaningful cross-repo references found.
