# dashboard/src/data/ — Cockpit State And Authority Overview

## Governing Overview
[dashboard/src overview](../overview.md)

## Purpose

This route owns retained dashboard projection state, task/document identity and transport clients for review, change sets, requirements, notes, files, Knowledge and developer grants. Browser state consumes server facts rather than creating a second canonical task, lifecycle, delivery or knowledge authority. The removed terminal catalogue, session/seat store, submit/answer/launch transport and conversation/composer data routes are not current owners.

## Hot Path Summary

1. store.ts and selectors.ts retain and derive served native TaskEntry facts without reconstructing a lifecycle/series hierarchy. taskReference.ts spells repository-qualified document and opaque entry selection keys; taskIdentity.ts compares exact references and names the document-backed role-chat leaf. The removed taskHierarchy.ts is not a current client authority.
2. stream.ts consumes projection snapshots/deltas; streamLiveness.ts, screenWakeLock.ts, fetchWithTimeout.ts and inflight.ts coordinate browser transport timing and ownership.
3. Review entry/summary/catalogue and comparison transports carry selected server identity and typed answer/refusal states. Tree and lane clients are used only where a comparison exists; transport acceptance is not complete schema decoding or dataset truth.
4. Task-document body, artifacts, reports, notes, files and requirements use their dedicated readers. Knowledge selections and hash navigation remain separate from task projection.
5. actions.ts retains attention dismissal only; directExecutionGrant.ts carries explicit Give/Revoke to server-owned grant authority. Neither creates local approval or a hosted session.
6. Current asynchronous generation ownership prevents retired reads from replacing successor surfaces. Retained development reset/fixture evidence is not product execution.

## Construction And Ownership

`store.ts` constructs the bounded-read owners for the dashboard store: `TaskDocumentResources` for task bodies, and three `ConditionalReads` instances for change-set lists (`changeSets`, capacity 256), file diffs (`changeSetFiles`, capacity 64 and 16 MiB byte bound) and intent summaries (`intentSummaries`, capacity 128). Clients consume these store resources rather than keeping an independent mounted-reader cache.

The route has a child review-keymap overview and separate panel/view owners. Keymaps retain browser-forbidden validation and chrome/review routing, not composer profiles or PTY interception. React consumers own rendering; Python applications and configured serving ports own canonical authority and answer classification.

The bound reviewer expression-card store retains answers and shares in-flight reads across pending-center remounts, keyed on the complete comparison and invariant set. Selection prefetches a changed set in parallel with its subject answer. This is separate from the retained selected-subject/walk stores and does not mix incompatible questions or infer empty unavailable data.

reviewTrees.ts carries the four code/memory trees and pinning refs, knowledge and index degradation, reopened code-side state, currentness, worklist/history linkage, supplied implementation facts and realization/proof entries on both code sides. The leaf-wide result no longer carries an aggregate memory diff grouped by record/source; standalone knowledge-tree comparison is a separate owner. Its vocabulary is snake_case. Requests address live, recorded or numbered comparisons and optionally invariants, not arbitrary paths/tree IDs. Trees, not-converted and refused are distinct answers. The card-entry hook shares in-flight reads and suppresses callbacks after unmount without aborting the shared acquisition; the leaf-wide hook aborts superseded reads and uses sequence guards and retries only reviewer_busy/inputs_changing, up to seven retries after the initial read with delays 1500, 2000, 3000, 4000, 5000, 6000 and 8000 ms. Loading remains until the final outcome, and abort ends the wait. Claims that the server stops work on disconnect require server-path evidence beyond the client abort itself.

## Invariants And Boundaries

Missing/unavailable/refused answers stay distinguishable from empty data. A declared client type is not a runtime validation guarantee. Source inspection, inherited fixtures and citation renewal provide no new UI, host, test or whole-build acceptance.

## Historical And Verification Limits

Earlier terminal/session/conversation and hosted-delivery accounts are withdrawn as current route facts. Historical producer lists and independent CODE verdicts remain their own bounded evidence, not a new grade from this overview.

## Retained Route And Coverage Metadata

These inherited tables are retained verbatim for navigation and custody. Their status/coverage cells are not a new lifecycle, test, or acceptance verdict.

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| sourceRoute            | `dashboard/src/data/`                            |

| Responsibility | File onboarding |
| --- | --- |
| Runtime bundle identity | [buildIdentity.ts](buildIdentity.ts.md) |
| Bounded boot transport and single-flight ownership | [fetchWithTimeout.ts](fetchWithTimeout.ts.md) · [inflight.ts](inflight.ts.md) |
| Stream liveness and visible-tab wake policy | [streamLiveness.ts](streamLiveness.ts.md) · [screenWakeLock.ts](screenWakeLock.ts.md) |
| Review client family mirror | [reviewFamily.ts](reviewFamily.ts.md) |

## Grant mutation adapter

directExecutionGrant.ts posts Give/Revoke to the developer endpoint and preserves typed refusal. The adapter shapes transport only; product grant and ordinary-start authority remain server-owned.


## Current Behavior

the store's three `ConditionalReads` resources now own reference-counted pending fetches: a same-facts joiner receives its own wait over one fetch, a leaving owner cannot abort a live joiner, and the last waiter removes the entry before aborting. `TaskDocumentResources` uses the same waiter rule and `abortableRead.ts` supplies `abortedRead`/`isAbortedRead`/`withAbort`. The task entry's change-set bar, summary and body abort their own reads on a selection change, and an aborted read is not rendered as a failure. The capacity/byte limits and the 256/64/128 resource capacities are unchanged. Earlier sentences that describe a different-facts read as simply aborting the older controller are historical; the waiter count is now part of the contract.

## Evidence
- The store owns task-document resources and separate bounded conditional-read caches for change-set lists, files and intent summaries. [108]

- The mirrored change types and the entry's optional facts. [1]
- One file's classification as a single read; a transport failure is `unavailable`. [2]
- The scope that keeps it per surface, only for a tree comparison. [3]
- The adapter's own statement: the server classifies once and this file only carries the answer. [4]
- The lane hook and the per-file single read share the classification transport; a dataset review names no tree comparison. [5]
- The summary carries the lane's count on both answered states. [6]
- The shareable hash, read and written. [7]
- A typed answer returned whatever its status; only transport failures throw. [8]
- The selection block every answer carries. [9]
- The three locator declarations. [15]
- The member source carrying them. [16]
- `useReviewCatalogue` owns the behavior described above. [17]
- The entry's summary read and its re-validation generation. [18]


- The server builds one native task forest from declared child rows; the browser no longer runs the removed creation-order hierarchy helper. [24]
- The one full scenario-store reset restores every projected collection, including `closeoutQueues`, in one transaction and is invoked by the development scenario player. [25]
- The route's read-only client and its comparison call. [29]
- **The entry call: the task context alone, because a selector is what it is being asked for.** [30]
- **The reviewed subject as the server's catalogue lists it — presence beside the label, the count field deleted (`ICR-R09@v1`), still the entry's only legitimate selector source, with no path field on purpose.** [31]
- **The entry read's typed envelope, whose refused form carries a refusal and no entries rather than throwing, and whose answered form carries the labelled totals of the whole catalogue.** [32]
- The endpoint the comparison call reaches, with no path among its parameters. [33]
- The closed selector union, the two kinds the server admits. [34]
- The no-store-mutation boundary, stated in the module header. [35]
- The typed result the client returns unchanged. [36]

- The TypeScript interfaces declare a client display projection, not a field-for-field Python mirror: ReviewSourcePane omits relationships, unknown_attribution_changed_paths and attribution; ReviewMovement is a common displayed subset. This is not a claim of runtime field loss. [37]

- **The inventory's wire types, including the byte form of a name this surface cannot print.** [38]
- **The comparison identity that states whether knowledge was compared, and the staleness union that gained the task-context state.** [39]
- The payload whose comparison may be absent, and the pane that says which question was answered. [40]
- **The request that omits the selector when there is none — the task-context entry.** [41]
- Changed-file navigation belongs to the comparison page ChangeList; SourceContent renders the selected source operands. The retired SourceExplorer is not a current owner. [42]

- **The six-member state literal and optional-text side mirror preserve the server contract. This interface is not a discriminated text/state validator and shared transport does not enforce a complete payload guarantee.** [43]

- **The expansion value: both sides, both generation ids, the three-member currentness, and the `path_bound` that says which measured change set admitted the path.** [44]
- **The source-content envelope whose two states are the two answers this route gives, a refusal being a normal one.** [45]

- **Source-content uses the same shared `getReviewJson` status-bearing decoder as the other review reads; the retired direct-fetch exception is historical, not current transport ownership.** [46]

- **The generation as an input: the caller's two published tree ids, echoed back in the spelling the route binds.** [47]

- ExpressionCards.FullFile forwards inventory before/after tree IDs to SourceContent; without both it renders the explicit generation-unavailable message. [48]
- The leaf-wide tree answer carries optional currentness, worklist, implementation facts and focused entries, not an aggregate memory-diff field. [109]

- The renderer the expansion's fields feed, and its three state-decided branches. [49]
- **The generation pins, the published generation identity, and the pins threaded through both master reads.** [54]
- **The new family mirror module, and the re-export that keeps `data/review.ts` the route's one public entry.** [55]
- **The bounded-collection union that lists `family_members` because the server accepts it, and the mirror that never narrows it.** [56]
- **The set a request may name with no cursor, and the reason `family_members` is not in it.** [57]
- **The optional family context whose absence says the body did not come from this route.** [58]
- An incoming link may carry the record its history-row source is about. [59]
- A superseded request is aborted and only the newer answer is shown. [71]
- Loading stays shown during the retries. [72]
- Unavailable is shown only after the bounded number of retries. [73]
- No camelCase key in the real body. [74]
- The module comment: one decode per read, nothing selected or substituted, and getJson unchanged. [75]
- The tokens a reader can be shown. [76]
- The codes and their tokens, with the two transient codes of the leaf-wide view. [77]
- An unknown code is carried as domain-refused. [78]
- The one GET: the optional abort signal, the body read whatever the status, and the two failures. [79]
- The review client imports and re-exports the transport surface. [80]
- A 404 typed refusal resolves through the review client with the refusal intact. [81]
- The same body is dropped by getJson: the shared client's semantics are unchanged. [82]
- selectors.ts changes only the memory-mirror comment from drift_check to drift reporting. driftSegments still uses projec — source ownership, not executed visual proof. [83] [84]

- Review reads share shallow state-bearing-body transport recognition across HTTP statuses. [86]
- Present paging excludes records and allows only knowledge without a cursor. [87]
- Entry catalogue refusal does not remove task-context review reachability. [88]
- Refresh empty-string normalization is specific, rather than universal query normalization. [89]
- Catalogue history/generation keying does not transmit those values; entries/totals can be locally defaulted, and incompatible semantic fields are quarantined. [90]
- Change-set refusal reasons are carried by the current decoder. [91]
- Requirement reads forward context and a path; registered address resolution is listing-based. [92]
- Artifact reader targets also include task reports and decisions. [93]
- Reader transport uses a 120-second bound and accepts a string-state body across statuses. [98]
- Reader hash writer omits empty subject keys while preserving explicit repository/commit. [99]
- Lane missing values become unavailable; undefined comparison suppresses the lane hook's request, while the marker client remains promise-based. [100]
- Entry intent counts and attribution share one response with distinct counted/partial/unavailable states. [101]
- Family change facts and source locator meanings are mirrored rather than recomputed. [102]


- Browser selection keys carry the server entry key verbatim, rather than reconstructing a hierarchy or partially stamped creation ordering. [104]

- Volatile-age equality includes elapsedSeconds. [105]
- Full scenario reset increments generation once and clears closeout queues. [106]
- Drift display consumes reporting counts while provider selector definitions remain. [107]

- The review wire mirror transports recorded meaning steps with their own attempts/revisions and distinguishes readable none from unavailable. [85]



- The served TaskEntry mirror carries optional document reference, identity, state, parent/children and counts; the old separate series-child consumer union is not the native entry model. [26]



- Membership links each child to one deterministic parent and rejects a cycle; the removed series creation-sort builder is not the current producer. [27]
- The generated projection mirror this route's suites build fixtures from, the manual sample used for coverage, and the fixture/projection stale gates. [28]
- The module comment: what the adapter carries and the three answers it keeps apart. [60]
- The answer of the route. [61]
- One entry on both code sides. [62]
- The request, addressed by number, recorded or invariants, with the optional signal. [63]
- The transient codes and the retry delays. [64]
- The bounded retry of a transient refusal. [65]
- One answer as a read state. [66]
- The comparison a payload names; without it no tree read is made. [67]

- The entries hook shares cached/in-flight card reads, suppresses unmounted retell callbacks without aborting the shared read, and returns null without a comparison or invariant set.  Anchor: `useReviewTreeEntries` [68]

- The leaf-wide hook: abort on cleanup, sequence number, retry, and the enabled flag. [69]
- The workspace enables the leaf-wide read only for a tree comparison and pins it to the payload's number. [70]

- Leaf-wide tree retry is bounded and its hook aborts/sequence-guards superseded reads; the card-entry hook shares in-flight acquisitions without aborting them, suppresses callbacks after cleanup and returns only its current question's cached answer. [103]