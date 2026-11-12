# dashboard/src/panels/review/ReviewSurface.memoryWatch.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Check the mounted review and intent-entry consumers of synthetic memory-watch events, including readiness reconciliation, selection isolation and coherent recovery from late or failed reads.

## Code Commentary

`FakeSource` supplies named SSE callbacks; capture-backed review bodies and a controlled fetch stub supply HTTP responses. The first three paired mounts pass a fixture-backed native `TaskEntry` to `DocChangeSetBar`; the response helper returns actual `Response` objects for the conditional-read client. These are the admitted composition adapters, not a second lifecycle-derived task model or evidence of native filesystem delivery.

- The first readiness baseline reconciles an explicit selected subject and entry count that were read before watch arming. One intervening synthetic edit is enough; duplicate and other-target events do not repeat the reads.
- Switching subjects and publishing a matching edit refreshes the actual selected answer and mounted entry. Opening the previous family afterwards does not resurrect its superseded answer. The test distinguishes a readiness refresh on the same comparison from a changed comparison that renews the catalogue.
- Controlled initial responses arriving after readiness cannot replace the reconciled visible generation or entry count.
- Two held edit responses resolved newest-first cannot let the older response replace the newer visible answer; repeating the same revision does not add a read.
- A failed memory-triggered read retains the explicitly labelled coherent generation. A subsequent synthetic edit can recover it and clear the failure.

`deferredSurface` controls request completion and `changedBody` makes an explicit synthetic display/binding perturbation. Test cleanup disposes the test connection and restores globals; it is not an assertion of native filesystem-watch reclamation.

## Evidence Boundary

There are five declared cases. This card records their current assertion bodies, not a fresh Vitest run, native producer timing, live API capture or installed-browser acceptance. The retained capture inputs remain historical fixtures rather than current project knowledge. Returning real `Response` instances does not by itself prove the 304-response path is exercised.

## Evidence

### Repo-Internal References


- Three paired mounts use fixture-backed native task identity, and stubbed fetch replies are real Response instances. [1]


- Initial readiness reconciles the selected answer and entry after one pre-arm synthetic edit, while duplicate and unrelated events are silent.


- A matching edit refreshes the actual selected subject and entry without restoring an old subject answer; catalogue renewal follows changed comparison identity.


- Initial responses arriving after the reconciled generation cannot replace its answer or count. [4]


- Deferred fetch responses and explicit synthetic capture perturbations control the late/failure cases. [5]


- Newest response wins; failed edits retain the labelled coherent generation and a later edit recovers it.

- Retired at the fifth freeze d59c3493: dashboard/src/panels/review/ReviewSurface.memoryWatch.test.tsx:32-78 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 10e466b17feee2530c06b2670fef496c6c9e755f; dashboard/src/panels/review/ReviewSurface.memoryWatch.test.tsx:80-119 - the region it cited is not in the file at the candidate and no re-point was possible; it was removed in commit 20624f979e2b89067a3e42019c9611a8e18ff848; dashboard/src/panels/review/ReviewSurface.memoryWatch.test.tsx:185-222 - the region it cited is not in the file at the candidate and no re-point was possible. Retired means the anchor no longer stands, not that the cited subject was deleted.
