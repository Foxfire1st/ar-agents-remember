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

## Evidence

- The module comment: one decode per read, and nothing is selected or substituted. [21]
- The tokens a reader can be shown. [22]
- The codes and their tokens, with the two transient codes of the leaf-wide view. [23]
- The refusals of the intent half alone. [24]
- The error a review read throws. [25]
- The one GET: the optional abort signal, the body read whatever the status, and the two failures. [26]
- A typed refusal becomes a failure with its fields unchanged. [27]
- A superseded request's signal is aborted. [28]
