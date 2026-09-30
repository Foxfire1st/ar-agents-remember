# dashboard/src/panels/review/ReviewReadCycle.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewReadCycle.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T14:22:59+02:00 |
| lastVerifiedCommitHash | `59daf5055eb1ceffba89170be64ac85cabf860f4` |
| lastVerifiedCommitDate | 2026-09-30T15:02:26+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review surface's read cycle: **one question, one in-flight read, and no superseded answer ever
writing the panes** (`ICR-R17@v1`). The module owns three things `ReviewSurface.tsx` used to keep
inline — the question's own identity (`targetKeyOf`), the read started for it (`askReview` through
`startRead`), and the state a reader's refresh needs (`useReviewReadCycle`, which returns the read,
the retained comparison, the carried binding identity and the `refresh` callback). It exists because
`ReviewSurface.tsx` is over the repository's file-size rail and the component was over the
per-function rail, and because the read cycle is a responsibility of its own: it owns a request
sequence, a retained generation and a refresh. The outcome states stay in
[`ReviewOutcome.tsx`](ReviewOutcome.tsx.md), the refresh control and its notice in
[`ReviewRefresh.tsx`](ReviewRefresh.tsx.md), and — since `260921-ICR-L48` — the admitted roster-walk
merge in [`familyWalkMerge.ts`](familyWalkMerge.ts.md) and the kept answers in
[`ReviewReadCache.ts`](ReviewReadCache.ts.md): one owner each, so there is no second copy of any.

**An answer is bound to its question, and the surface keeps a frame (L48, `ICR-R24@v3`).** The read state
is a `KeyedRead` (`{key, read}`), and the surface is handed a read only for the question on screen: until
the new question's answer (or its kept copy) exists, the read is `loading` *for that question* — never the
previous subject's payload, even for the render between a selection and the effect that starts the new
read. Separately the hook returns `frame`, the last payload **admitted** for this task context (repo,
master, leaf and record), whichever subject it answered; the surface keeps its shell mounted over it while
another subject is pending, failed or refused, and never renders it as that subject's reading.

**A whole subject is read once per comparison (L48).** An admitted whole-subject answer that carried no
refresh identity is kept in the surface's `ReviewReadCache` under its target key; returning to that
question renders the kept answer without a request. Paged questions are never kept, a refresh forgets
the question it re-asks, and an answer from another comparison generation empties the cache.

**A read is asked for a question, and the question has an identity.** `targetKeyOf` composes
`repo/master/leaf`, the record the read is addressed to (`history`, or `live`), the question itself
(the selector, or the task context when the surface is answering a refusal with the task's own source
inventory) and the page position. A comparison is only ever shown under the header it was read for,
so that key is what a retained generation is stored with and checked against, and changing any part
of it re-asks the question.

**The newest read wins, and a superseded one is dropped silently.** Every read takes the next
sequence number out of a `useRef` counter and only the newest may write the read state. A slow answer
for the subject or task selected *before* the current one therefore lands with a smaller number and is
dropped — it cannot replace the comparison on screen, and the failure it might have reported is not
reported either. The effect's own cleanup flag covers unmount; the sequence covers the case that flag
cannot see, which is the same mounted surface with two requests in flight.

**A validated family continuation enriches one existing walk.** A cursor-free question key binds the repository, task, history and selected subject while the request key retains its page position. The read cycle keeps the coherent reading path mounted during a continuation, then merges only one compatible family-side-revision walk. It preserves earlier exact content, deduplicates sources by claim identity and does not reset another walk when the server repeats that walk's first page. The latest response remains authoritative for the primary statement, inventory, evidence and assessment.

**A refresh replaces, it does not patch.** The reader's control re-asks the *same* question carrying
the identity of the comparison they are looking at, read from the payload the panes actually render —
never from a request or a response that arrived for something else. The answer replaces the read state
whole and the server's own staleness answer, compared against the identity that was carried, is what
tells the reader whether it is still the same generation.

**The carried identity belongs to exactly one read.** It is the previous input of the comparison that
was *displayed*, so it travels on the single read the refresh asked for and on no other:
`{readNumber, key, digest}` is captured together in `refresh`, and `startRead` sends the digest only
when that read IS the one the refresh asked for. A different subject, a different leaf, the same
subject read from the leaf's record instead (`history="recorded"`), or a later read of the same
question all carry nothing — otherwise the server would answer `stale` against an identity that read
never replaced, and the notice would announce a candidate publication that never happened. Clearing
the identity when the question key changes is deliberately **not** the rule: switching away from a
question and back again restores the key, and the stale identity with it.

**What it does not do.** No timer, no retry ladder, no polling: a read happens when the question
changes (and has no kept answer) or when the reader asks. A read that fails leaves the last coherent payload retained and lets
the outcome region state the failure beside it, which is the packet's "a failed refresh retains the
labeled old generation with its error".

## Code Commentary

### Logic

**The module header states the read-cycle rules, and it is the contract a later reader should hold.**
The first four bullets state the preserved rules: one read per question, the newest read wins, a refresh
replaces rather than patches, and the carried identity belongs to one read. L48 added two: an answer is
bound to its question, and a whole subject is read once per comparison. The explicit family-continuation admission below adds bounded enrichment without changing those replacement rules. The
`WHY THIS IS ITS OWN MODULE` paragraph names the file-size rail and the per-function rail as the
reason it is not inline, and points at `ReviewOutcome.tsx`, `ReviewRefresh.tsx`, `familyWalkMerge.ts`
and `ReviewReadCache.ts` for the neighbours that own the rest, so the boundary is stated where a reader
meets it.

**`targetKeyOf` is the question's identity, and the page is part of the question.** It returns
`` `${repo}/${master}/${leaf}/${history ?? "live"}/${question}/${position}` `` where `question` is
`task-context` when the surface is answering a refusal with the task's own inventory and
`${selectorKind}:${selectorId}` otherwise, and `position` is `whole` for an unpaged read or
`` `${page.of}:${continuation-or-first}` `` for a paged one. The comment above `position` states why:
page 3 of one collection is a different answer from page 1 of it, and a retained page must never be
rendered under another page's header.

**`ReviewPageRequest` is exported from here now, and it gained the `size` axis.** It was private to
`ReviewSurface.tsx` as `{ of; continuation? }`; the module's copy declares
`{ of: ReviewPagedCollection; continuation?: string | null; size?: number }` and is imported back by
the surface, because the page request participates in the target key and the surface is no longer
where the key is computed. The surface still owns the `selection` state; this module only reads it.

**The collection is the server's own union, not a narrowed copy of it (ICR-R31@v1).** `of` is typed
`ReviewPagedCollection` — `"knowledge" | "records" | "family_members"` — rather than the
`"knowledge" | "records"` pair it used to spell, because a request naming `family_members` must be
representable: that is how a family's truncated roster is continued, with the cursor that family
context published. Which collections the surface **offers** with no cursor is a separate decision and
is not made by this type: it is `REVIEW_WALKABLE_COLLECTIONS`, whose two members are the ones whose
first page exists.

**`askReview` performs exactly one read and writes no state itself.** It builds the client call,
forwards the nine arguments `intentReview` takes — the ninth being the previous binding identity, or
`undefined` — and hands one `ReviewRead` outcome to the caller's `apply` callback. On a throw it applies `{ phase: "failed", problem:
reviewProblemFromCause(cause) }` with no payload, which is how a transport failure stays distinct from
a typed refusal. Because it never calls a setter, there is exactly one place where a read reaches the
surface (`startRead`'s `apply`) and exactly one place where it is dropped.

**`startRead` is the one read path, and it decides both reasons an answer may be dropped.** It takes
the next sequence number (`++reads.current`), computes `current()` as "not superseded and still the
newest", decides which identity the refresh may carry, and retains the mounted payload only for a same-question family continuation. Other questions use replacement semantics. Since L48 it first asks the cache: for a whole-subject read that carries no identity, a kept answer is admitted at once and no request is made (the read number is still consumed, so a later read of that question cannot pose as a refresh). Otherwise it sets the keyed read to `loading` for its own key (or keeps a continued walk on screen), and on an admitted answer either keeps it (whole, no identity) or only lets the cache observe its generation (paged or refresh answers), then `admit`s it — which writes the keyed read, the retained generation and the `frame` together. A failure or refusal writes only the keyed read, so the frame survives it (L48-R1-F1). It then applies one admitted read outcome:

- **the carried identity is sent only when the read IS the one the refresh asked for** — the same
  question key *and* the read number `refresh` captured. Every other read replaces nothing, and a
  carried identity there would make the server answer `stale` about a comparison nobody replaced;
- **the answer is applied only through `current()`**, so the cleanup flag (unmount) and the sequence
  (a newer read) are the two reasons a late answer is dropped, and both are decided in the hook's own
  frame rather than distributed across the component.

**`CarriedBinding` is three fields because an identity alone cannot answer the question the guard
asks.** `readNumber` says which read was asked to replace the display, `key` says which display the
identity came from, and `digest` is the identity itself. The interface's own comment records the
defect the pairing closes: "an identity carried into a read that replaces nothing is what made the
server report a moved comparison for a subject the reader had merely selected."

**`useReviewReadCycle` holds the state, the refs and the one effect, and returns five values** (`read`,
`retained`, `carried`, `refresh`, `frame`). The keyed `answer` and `retained` are `useState`, and the
returned `read` is derived per render by `readOnScreen`: the keyed answer when its key is the target key;
else, in the same pass as the selection, a continued walk of the same question or the cache's kept answer
(so neither a roster page nor a return to a subject flashes a pending state); else `loading` for this
question. `frame` comes from `useFrame`, which files each admitted payload with its task context and
returns it only for the same context. The hook requires the surface's `cache`; `carried` is the `CarriedBinding`; `refreshNonce` is what makes
a reader's click re-run the effect without changing the question. `asked` is `useMemo`-ised on its own
values so the effect's dependency array names the fields it really reads and no lint suppression is
needed to say so — the module says that in the comment above it. `retainedRef` and `carriedRef` are
mirrors so the `refresh` callback can read the displayed payload and the carried identity without
restarting a read; the effect is the single place a read starts.

**`refresh` files the identity with the question it was displayed for and the read that will replace
it.** It reads `retainedRef.current`, takes `payload.comparison?.binding_digest`, and — only when a
payload with a binding is actually displayed — sets `{readNumber: reads.current + 1, key: shown.key,
digest: shownBinding}` before incrementing `refreshNonce` in the same update, so the read the identity
names is the one the effect starts next. A refresh with nothing displayed sets no identity at all.

**The value the notice may describe is computed from all three conjuncts, and the key is not
redundant with the read number.** `carriedHere` holds only when `carried.readNumber === reads.current`
**and** `carried.key === targetKey`. The comment records the defect that made the second conjunct
load-bearing: when the subject change and the reader's refresh land in the same React flush, the
refresh captures the *previous* subject's identity while the one effect run that follows asks for the
new subject and consumes exactly that read number — so a read-number check alone would describe
another subject's identity, and the surface would announce a candidate publication the request never
carried and the server never answered. `startRead` checks the same pair before sending, so the value
described and the value sent cannot disagree. Because the returned `carried` is `carriedHere`, the
identity reaching the notice has an answer behind it by construction.

**Failed admission preserves the coherent display and states failure.** `familyContinuationRead` accepts a continuation only after comparison, candidate, primary revision selection, cursor, family selection, side/revision, guarantee digest, page scope and immutable member/claim checks agree. A structured page refusal keeps its owner's code and recovery text; another incompatibility becomes `comparison_page_unreadable`. The raw rejected response never becomes a successful replacement. Whole-review refusals retain their existing suppression semantics, and newest-read guards still drop late responses.

**Loaded state is local presentation, not a second knowledge authority.** `mergeMember` preserves recorded content while adding exact claims; `mergeFamilySide` preserves independent progress and admits identical replay; `mergeFamilyContinuation` overlays only family context onto the latest owner response. Completeness requires completed recorded sides with all measured member contexts and recorded content; explicit not-recorded sides remain absence.

**The first read can be held (`260921-ICR-L47`).** `ReviewReadQuestion` gained an optional `hold`, and
`useReviewReadCycle` takes `hold = false`: while `hold` is true the read effect returns without starting a
read (and `readOnScreen` serves nothing from the cache), so the surface does not ask for a question it is about to replace. `ReviewSurface.tsx` passes
`hold: navigation.settling`, which is true only while the reviewer was opened with no subject, the catalogue
has not answered, and the bounded `SUBJECT_HOLD_MS` (750 ms) has not expired (`ReviewNavigation.tsx`). The
two display refs are now kept by a small `useLatest` helper (a ref updated every render), extracted to keep
the hook under the per-function line rail; it changes no read rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| The optional hold on the question. | `ReviewReadQuestion`; `hold?: boolean` | dashboard/src/panels/review/ReviewReadCycle.ts:303-317 |
| The latest-value ref helper. | `useLatest` | dashboard/src/panels/review/ReviewReadCycle.ts:352-356 |
| No read starts while held. | `useReviewReadCycle`; "if (hold) return undefined" | dashboard/src/panels/review/ReviewReadCycle.ts:358-471 |

### Conventions

One hook owns the read sequence and retained presentation. Module-private functions separate request, continuation admission (`familyContinuationRead`), the read on screen (`readOnScreen`) and the frame (`useFrame`); exact member merging and independent side-walk composition moved unchanged to `familyWalkMerge.ts` in L48; private interfaces keep each retained read and request together. Everything crossing the
module boundary is either an exported name (`ReviewPageRequest`, `targetKeyOf`, `ReviewReadCycle`,
`useReviewReadCycle`) or an imported shipped type — the review wire types and the client from
`../../data/review`, the read state and its mapper (`ReviewRead`, `readFrom`) from `./ReviewOutcome`,
the cache type from `./ReviewReadCache` and `mergeFamilyContinuation` from `./familyWalkMerge`.
React state is read through `useState` and mutated only through the setters the hook passes down;
`useRef` carries the three values that must not restart a read (the sequence counter and the two
mirrors). The inline `style`/`data-*` idiom lives in the renderers, not here: this module renders
nothing. Comments state the reason a rule exists rather than restating the code, and each
defect-bearing decision names the leaf that closed it (`L17-F1`, `L17-R2-F1`, `L17-F2`).

### Invariants And Boundaries

- **One read path.** Every read goes through `startRead` → `askReview`; the `refresh` callback only
  asks the effect to run again, so a click cannot become a second way of composing the request.
- **One question per read, and the answer is retained under the key it was asked for.** A payload
  read for another subject, task or history is dropped when that question is asked. A family continuation retains its same-question context under the active page key only through the continuation admission path.
- **The newest read wins.** Only the read whose sequence number is still `reads.current` may write the
  read state, and a dropped answer reports nothing — not even a failure.
- **The carried identity is sent and described under the same two-part condition.** The question key
  and the read number are checked at both sites (`startRead` before sending, `carriedHere` before
  describing), so the identity the notice describes is exactly the identity the request carried.
- **The carried identity belongs to one question.** It is never sent on a different subject, a
  different leaf, a recorded read of the same subject, or a later read of the same question.
- **A failed read keeps the last coherent comparison, and the failure is stated beside it.** `retained`
  is not erased by a failing read; only a read for a different question drops it.
- **The surface is handed a read only for the question on screen (L48).** `readOnScreen` never returns an
  answer keyed to another question, so a previous subject's payload cannot be shown under the new
  subject's header (`ICR-R26` isolation under a retained shell).
- **The frame is set only from admitted payloads and survives a failure or refusal (L48-R1-F1).** It is
  scoped to one task context and record, so a payload admitted for another leaf or for the live
  comparison is never the recorded comparison's shell.
- **Only whole, identity-free answers are kept.** Paged and refresh answers are observed for their
  generation but never kept, so a refresh's staleness answer is shown once, for that refresh, and never
  re-rendered as a later plain answer (the fix the worker's E1b event recorded). A superseded answer is
  dropped before it reaches the read state or the cache.
- **Cached returns do not re-validate a moving live candidate** (review observation O-R1-1, by design):
  toggling between two already-read subjects makes no request and each view stays labelled with its own
  trees; the reader's refresh always re-asks, and any answer from another generation empties the cache.
  Making a selection double as a live check would be a new decision, not a repair.
- **The module renders nothing and owns no styling.** It exports values and one callback; the rendering
  of the generation claim belongs to `ReviewRefresh.tsx` and the outcomes to `ReviewOutcome.tsx`.
- **No timer, no retry ladder, no polling.** A read happens on a question change or on the reader's own
  request, and nothing in this module schedules work.
- **Boundary.** This module owns the request sequence and the retained/carried values. It does not
  decide what a state looks like, does not classify a refusal (that is `data/review.ts` and
  `data/reviewTransport.ts`), and does not compare the carried identity against the answer — the
  server answers `stale`/`current` and `generationOf` reads it.
- **The page request carries the server's whole collection union.** `ReviewPageRequest.of` is
  `ReviewPagedCollection`, so a request that continues a family roster is representable; which
  collections may be named with no cursor is `REVIEW_WALKABLE_COLLECTIONS`' decision, not this type's.

### Todos

None recorded. One honest limit belongs to the surface above this module and is recorded rather than
closed here: the carried identity is what makes the *client* able to describe a movement, and the
notice it feeds is a restatement of the server's own comparison, not an independent measurement — the
server's `staleness.state` remains the authority, and a read that never reaches the server produces no
claim at all.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and the four
rules it states, the public read-cycle types and private continuation owners, the two call sites in
`ReviewSurface.tsx`, the client argument the read threads, and the two test cases that measure the
identity's single-read rule. Every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of why it exists (the file-size rail and the per-function rail), the rules it enforces (including L48's keyed answer and once-per-comparison rules), the carried-identity rule, and the explicit "what it does not do" — no timer, no retry ladder, no polling.** | "THE THREE RULES THIS MODULE ENFORCES"; "AN ANSWER IS BOUND TO ITS QUESTION"; "A WHOLE SUBJECT IS READ ONCE PER COMPARISON" | dashboard/src/panels/review/ReviewReadCycle.ts:1-50 |
| The module's imports: the review wire types and the client, and the read state with its mapper. | `intentReview`; `readFrom` | dashboard/src/panels/review/ReviewReadCycle.ts:52-64 |
| **The page request, exported from here rather than declared in the surface, with the collection, the cursor and the size axis the target key consumes.** | `ReviewPageRequest` | dashboard/src/panels/review/ReviewReadCycle.ts:73-77 |
| **The question's identity: task, record, question and page position, with the page's own reason for participating.** | `targetKeyOf` | dashboard/src/panels/review/ReviewReadCycle.ts:82-100 |
| **The one read: the nine-argument client call, the previous identity passed as the ninth, and the answer handed to the caller's callback rather than written to state.** | `askReview`; `intentReview`; `reviewProblemFromCause` | dashboard/src/panels/review/ReviewReadCycle.ts:105-136 |
| **The one read path: the sequence number, the superseded flag, the drop of a payload read for another key, the two-part condition under which the carried identity may be sent, and (L48) the kept-answer short cut and the keep-or-observe decision.** | `startRead`; `keepReview`; `observe` | dashboard/src/panels/review/ReviewReadCycle.ts:163-217 |
| **Admission writes the keyed read, the retained generation and the frame together.** | `admit`; `setFrame` | dashboard/src/panels/review/ReviewReadCycle.ts:219-223 |
| **The read for the question on screen, derived per render.** | `readOnScreen`; `KeyedRead` | dashboard/src/panels/review/ReviewReadCycle.ts:228-231; dashboard/src/panels/review/ReviewReadCycle.ts:319-337 |
| **The frame: the last admitted payload of one task context.** | `useFrame` | dashboard/src/panels/review/ReviewReadCycle.ts:341-348 |
| **The identity paired with the one read it belongs to — the read number, the question key and the digest — and the defect the pairing closes.** | `CarriedBinding` | dashboard/src/panels/review/ReviewReadCycle.ts:277-281 |
| **The hook's contract: the read, the retained generation and its key, the identity described for the question on screen now, and the reader's own refresh.** | `ReviewReadCycle`; `frame` | dashboard/src/panels/review/ReviewReadCycle.ts:283-301 |
| **The hook itself: the four pieces of state, the memoised request fields, the sequence counter, the two refs and the single effect that starts a read.** | `useReviewReadCycle`; `reads`; `carriedRef` | dashboard/src/panels/review/ReviewReadCycle.ts:358-471 |
| **`refresh` files the identity with the question it was displayed for and the read number that will replace it, and asks the effect to run again — a refresh with nothing displayed carries nothing.** | `refresh`; `refreshNonce`; `forgetReview` | dashboard/src/panels/review/ReviewReadCycle.ts:377-377; dashboard/src/panels/review/ReviewReadCycle.ts:423-439 |
| **All three conjuncts of the described identity, and the same-flush defect that makes the question key non-redundant with the read number.** | `carriedHere` | dashboard/src/panels/review/ReviewReadCycle.ts:451-454 |
| **The read state and its mapper: the four phases this module sets, and the client's typed answer projected into them.** | `ReviewRead`; `readFrom` | dashboard/src/panels/review/ReviewOutcome.tsx:33-37; dashboard/src/panels/review/ReviewOutcome.tsx:42-55 |
| **The client's ninth argument and the one query string it is assembled into, with the empty/undefined spellings collapsed once.** | `intentReview`; `reviewQuery` | dashboard/src/data/review.ts:558-574; dashboard/src/data/review.ts:580-611 |
| **The one spelling of the query parameter the server admits, named once so a call site cannot silently stop carrying the identity.** | `PREVIOUS_BINDING_QUERY` | dashboard/src/data/review.ts:674-674 |
| The surface calls the shared read cycle, checks its retained target key, and supplies the resulting generation to refresh. | `useSurface`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:453-532; dashboard/src/panels/review/ReviewSurface.tsx:534-598 |
| **The generation claim that consumes `carried`: it renders nothing unless the read that carried the identity has answered.** | `generationOf` | dashboard/src/panels/review/ReviewRefresh.tsx:113-127 |
| **The cases that measure the identity's single-read rule through the real surface: a different subject carries nothing, a recorded read carries nothing, and a same-flush subject change plus refresh carries nothing.** | "carries the identity into a read that replaces it, and into no other question (L17-F1)"; "never carries a live identity into a recorded read, nor a recorded one into a live read (L17-F1)"; "renders no generation claim when the subject change and the refresh land in one flush (L17-R2-F1)" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:707-898 |
| **The case that measures the sequence guard: a slow earlier subject's answer cannot replace the subject selected now.** | "never renders a slow earlier subject's answer over the subject selected now" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:654-705 |
| Rejected continuation becomes a failed read without installing the raw response. | `familyContinuationRead` | dashboard/src/panels/review/ReviewReadCycle.ts:249-270 |
| Sparse updates preserve exact content and claim identity within independent walks (moved unchanged to `familyWalkMerge.ts` by L48). | `mergeMember`; `mergeFamilySide` | dashboard/src/panels/review/familyWalkMerge.ts:13-33; dashboard/src/panels/review/familyWalkMerge.ts:35-58 |
| Only the bound comparison and exact family-side-revision walk are composed. | `sameFamilyWalk`; `admittedFamilyContinuation`; `mergeFamilyContinuation` | dashboard/src/panels/review/familyWalkMerge.ts:60-72; dashboard/src/panels/review/familyWalkMerge.ts:74-100; dashboard/src/panels/review/familyWalkMerge.ts:104-157 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every read names one repository namespace
and one leaf id and is served by the same-origin dashboard route.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T14:22:59+02:00 — 260928-MIK-L32 curator (staged change set on `ar/260928-mik-l32`, code base `07d6584afba8a9504e4a3cf2e80eac41f68b28a9`): No content impact: this card's own source is unchanged. MIK-R32 moved lines in `dashboard/src/panels/review/ReviewSurface.tsx`, so the citation rows into them that moved were re-pointed by the installed fixer (run once; its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; every re-pointed row was byte-identical to memory HEAD beforehand and was checked to hold its anchors in the new range. The fixer's normalisation also re-measured passing rows into files this leaf did not change (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/ReviewReadCycle.ts`, `dashboard/src/panels/review/ReviewRefresh.tsx`, `dashboard/src/panels/review/familyWalkMerge.ts`); no claim changed. No verification stamp was advanced.
- 2026-09-28T21:45:24+02:00 — 260921-ICR-L48 curator (uncommitted candidate tree `ac73216e2a763b72844a63b8c36c81f9a8b5f0e8` over code base `cb1b942af60a7ed5006ac992075d2bf96aeb9fa7`): **body update — keyed reads, a per-comparison cache and a task-context frame (`ICR-R24@v3`; L48-R1-F1; L47-R1-F5 file budget; `ICR-R17`/`ICR-R10`/`ICR-R26` preserved).** The read state became a `KeyedRead` and the returned `read` is derived by `readOnScreen`, so the surface only ever sees a read for the question on screen; `startRead` serves and keeps whole-subject answers through the surface's `ReviewReadCache` and `admit` also sets `frame` (via `useFrame`), which a failure or refusal no longer clears. The roster-walk merge moved unchanged to `familyWalkMerge.ts` (539 → 471 lines). The card **extends** its read-cycle contract with these rules and **preserves** the four L17 rules, the continuation admission and the hold; its statements that the hook returns four values and that `read` is plain state are **superseded**. Review observation O-R1-1 (cached returns do not re-validate a moving live candidate) is recorded as the stated design rule, not a defect. The five reopened claims were re-read; every row re-derived, four rows added. No stamp advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`dashboard/src/data/review.ts`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:11:24+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): **body update — the read cycle can hold its first read (`ICR-R24@v3`).** Records `hold` on the question and in the effect, and the `useLatest` extraction for the two display refs; the read rules above are unchanged. Displaced rows were re-pointed from the base-to-candidate line mapping. No stamp advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): No content impact: citation ranges into files this leaf changed (`dashboard/src/data/review.ts`, `dashboard/src/panels/review/SourceContent.test.tsx`, `mcp/tests/test-evidence-lanes.toml`, `mcp/tests/evidence-lifecycle.toml`, `mcp/tests/test_knowledge_review_source_content.py`) were re-pointed to where the same anchors now sit, each row checked valid at the base, invalid at the candidate, and valid after the base-to-candidate line mapping; claim wording unchanged. No stamp advanced.

- 2026-09-27T01:16:27+00:00 — Re-resolved import, hook, refresh and continuation references against their actual constructs. Ambiguous name-only repairs were not accepted: imports remain cited at the import block, and hook/refresh claims at their own definitions. No verification stamp was advanced.

- 2026-09-27T00:59:43+00:00 — Curated same-question bounded family accumulation and explicit rejection. Compatible sparse updates retain exact content, claim identity and independent walk progress; rejected pages fail visibly with coherent retention, while refresh/history/subject changes keep replacement semantics. Primary statement, source, evidence and assessment owners are preserved.
- 2026-09-26T21:09:43+00:00: Generated citation repair: `PREVIOUS_BINDING_QUERY` repointed to dashboard/src/data/review.ts:659-659. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed, no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **body refresh for the widened page-request union, plus the citation repair of this card's 10 unsatisfied rows.** `ReviewPageRequest.of` is now the server's own `ReviewPagedCollection` (`"knowledge" | "records" | "family_members"`) rather than the narrowed `"knowledge" | "records"` pair, so a request that continues a family's truncated roster with the cursor its family context published is representable; which collections the surface offers with **no** cursor is `REVIEW_WALKABLE_COLLECTIONS`' separate decision, and the card now says so in Logic and in Invariants. **Citation repair:** the `citation_claim_reopened` row for `ReviewPageRequest` was re-pointed at the range the declaration occupies now (`62-66`), because the declaration line had fallen outside every cited range; the nine `citation_anchor_absent_from_range`/`citation_range_out_of_bounds` findings were cleared the same way — the import block → `43-53`, the one read (`askReview`/`intentReview`/`reviewProblemFromCause`) → `94-125`, `intentReview`/`reviewQuery` → `dashboard/src/data/review.ts:533-549`/`555-586`, and the surface's use of this module → `ReviewSurface.tsx:55-56`, `844-853`, `854`, `884`, which also retires the two ranges that ran past the end of `ReviewSurface.tsx` (`920-935`, `955-966`). Every target range was verified with `sed -n 'START,ENDp'` over the frozen candidate before it was written; no row was dropped and no claim was re-worded. Two further rows whose constructs this leaf's own insertions moved — `CarriedBinding` → `187-191` and `carriedHere` → `286-291` — were re-pointed in the same pass. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **created.** This module is new in this leaf and this is its one-to-one card. It records the three rules the module's own header states (one read per question, the newest read wins, a refresh replaces rather than patches), why it exists as its own module (the file-size rail plus the per-function rail, with the outcome states and the refresh control left to their own owners), and the rule that carries the leaf's two fix rounds: the carried binding identity is `{readNumber, key, digest}` and is both **sent** and **described** only when the read number and the question key agree, so the identity the notice describes is exactly the identity the request carried. Both fix rounds are recorded where the source records them — `L17-F1` (the identity is not sticky; a different subject, a different leaf, a recorded read and a later read of the same question all carry nothing) and `L17-R2-F1` (the question key is not redundant with the read number, because a subject change and a refresh in one React flush would otherwise describe another subject's identity). The module's one honest limit is recorded rather than closed: the notice this value feeds is a restatement of the server's own comparison, not an independent measurement. **Stamp accounting:** the verification pair names the **production line at this leaf's base** `c422dc00273d4ae7a5d8c9c8db97365b8c85d640` (2026-09-23T05:16:40+02:00); everything this card describes is **uncommitted** working-tree bytes in the `ar/260921-icr-l17` worktree composed on top of that base, so no commit contains the code a stamp would claim to have verified. What was actually read is that working tree, and the governed closeout owns the real stamp.
