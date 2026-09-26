# dashboard/src/panels/review/ReviewOutcome.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewOutcome.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The review surface's **non-payload outcomes, in one place**: the loading state, the known-empty note,
and the one refusal/failure block every read that is not a review renders through. It is the new owner
ICR-R16 created for the rendering half, and it exists because the surface used to hold those states
inline — a `RefusalBlock`, a generic `review-error` paragraph and a `payload`/`refusal`/`error` triple
of `useState` values — which meant a transport-level failure and a typed refusal reached a reader as
the same sentence and a thrown message.

What a reader is owed **distinctly** is the module's own vocabulary, and each member names where it
comes from: `loading` (the read is in flight; nothing is claimed about the answer yet), `known-empty`
(the read *answered* and there is nothing to show — a measured inventory of zero paths, no knowledge
comparison and no recorded evidence or assessment, never rendered as a failure and never produced by
one), `not-initialized` (`candidate_dataset_absent`), `unavailable-history` (`candidate_not_live`,
`candidate_unresolved`, `review_adapter_unavailable`, the route's own unwired answer), `validation`
(`bad-request`), `authority` (`bad-path`), `domain-refused` (a subject- or comparison-level refusal
carried by its own code), `network` (no HTTP response at all) and `unreadable` (an HTTP response that is
not this route's answer).

Its boundary is the mirror of the transport owner's: **nothing here invents a recovery route, retries
automatically, or renders an absent answer as an empty review.** Every block prints the owner's own
words — its code, its reason, the offending input it named and the next action it published — and the
one control beside a refusal is the task's own source change inventory, offered only for a refusal that
answers for the *intent* half alone and only as a separate question the reader asks.

## Code Commentary

### Logic

ReviewProblemBlock leads with a compact unavailable label and preserves code, reason, offending input and recovery inside Reason and recovery. Network retry and the explicit source-review action keep their existing eligibility rules. Refusal, transport failure, loading and measured empty remain distinct.

**`ReviewRead` is the read's four phases, and the three that are not panes are rendered here.** The
union is `{phase:"loading"} | {phase:"reviewed", payload} | {phase:"refused", problem} |
{phase:"failed", problem}` — one value rather than three parallel `useState`s, which is what makes "a
refusal and a stale payload can never both be the read" a property of the type instead of a rule two
assignment sites have to keep.

**`readFrom(result)` is the one place a typed result becomes a phase, and an unadmitted answer can
never become a review.** `state === "review"` **with a payload** is `reviewed`; `state === "refused"`
is `refused`, carrying `reviewProblemFromRefusal(result.refusal)` or, when a refused body published no
refusal at all, `unreadableAnswer("refused")`; and everything else is a `failed` phase carrying
`unreadableAnswer(result.state)`. So a body claiming a state this client does not declare is reported,
and a `candidate_dataset_absent` refusal is never read as a review of an empty candidate.

**`shownPayload(read, lastCoherent)` is the one answer to "what should the panes render".** `reviewed`
returns its own payload; `failed` returns the last coherent payload the surface really read; `refused`
returns `null`. The refusal case is deliberate and asymmetric: a typed refusal is the owner's answer
about the leaf's current state, so it **replaces** the panes rather than sitting beside a comparison the
server has just declined to stand behind — while a transport failure is not an answer about the
comparison at all, so the comparison the surface already had stays on screen.

**`problemOf(read)` is the one accessor for the failure a phase carries**, so no caller re-derives which
phases have one.

**`knownEmpty(payload)` is a measurement, not a mood.** It requires all four facts at once:
`source.inventory.state === "measured"`, `listed_total === 0`, `comparison === undefined`, and empty
`evidence.evidence_links` and `evidence.assessments`. Anything unmeasured, or any recorded knowledge,
evidence or assessment, is not this state.

**`ReviewProblemBlock` is the one renderer for a `ReviewFailure`, and it prints every field the owner
published.** It carries `data-review-state={problem.token}` and `data-review-code={problem.code}` on the
root, names the subject that could not be opened (`subject`, defaulting to `the review`; the expansion
pane passes `this entry's content`), and distinguishes its two origins only by test id
(`review-refusal` for the route's typed refusal, `review-failure` for a transport-level body) so a test
or a reader can tell the shapes apart while both travel one renderer. It renders the offending input and
the next action **or an explicit sentence saying the server published none** — never a silent gap — and
it adds exactly two conditional controls: a retry only when `problem.token === "network"` (the one state
with no owner-published recovery route), and the source-inventory offer only when the caller supplied
one and `intentOnlyRefusal(problem.code)` holds.

**`TaskContextInsteadNote` keeps the refusal visible after the reader asks the different question.**
It prints the refused code, reason, offending input and the refusal's own still-standing `nextAction`
above the inventory the reader asked for, because what is shown instead is an answer to a second,
explicitly asked question and never a silent substitution.

**`RetainedGenerationNote` labels a comparison that survived a failed read, and its closing sentence is
chosen by what the retained payload actually is.** A real comparison is one the surface will not let a
failed read deny; a retained **measured-empty** generation is an earlier read's own measured answer, so
it is stated as the known-empty result it is rather than denied.

**`ReviewOutcomeRegion` is the one place those notes are decided, and the two statements about a shown
payload are mutually exclusive there.** It renders the loading line for `loading`; the one problem block
for a carried problem, with `origin` chosen from the phase; the instead-note when a refusal was answered
by the inventory and the read has since come back `reviewed`; `KnownEmptyNote` when the shown payload is
measured-empty; and `RetainedGenerationNote` only when there is a `lastCoherent` payload that is **not**
measured-empty. A retained known-empty is therefore stated once, as the measured result it is, and never
also denied — which is exactly the contradiction the fix round removed (a payload measuring nothing used
to print both sentences in one DOM).

### Conventions

The module imports its types and its three projection functions from `../../data/review` — the review
client's public entry, which re-exports them from `data/reviewTransport.ts` — and declares no client, no
store and no CSS module. One `mutedStyle` constant carries the secondary-line styling the cockpit
panels use inline. Exported names are the phases and the renderers (`ReviewRead`, `readFrom`,
`shownPayload`, `problemOf`, `ReviewLoading`, `knownEmpty`, `KnownEmptyNote`, `ReviewProblemBlock`,
`TaskContextInsteadNote`, `RetainedGenerationNote`, `ReviewOutcomeRegion`); every rendered fact carries a
`data-testid` (`review-loading`, `review-known-empty`, `review-refusal`, `review-failure`,
`review-offending-input`, `review-no-offending-input`, `review-next-action`, `review-no-next-action`,
`review-retry`, `review-source-instead`, `review-source-instead-note`, `review-retained-generation`) or a
data attribute (`data-review-state`, `data-review-code`).

### Invariants And Boundaries

- **An unadmitted state is never a review.** `readFrom` requires `state === "review"` **and** a payload;
  everything else it does not recognize becomes a `failed` phase that names the state.
- **A failure is never known-empty, and known-empty is never a failure.** `knownEmpty` is reachable only
  from a `reviewed` payload, and its four conditions are all measurements.
- **A typed refusal replaces the panes; a transport failure does not erase them.** That asymmetry lives
  in `shownPayload`, in one place.
- **Exactly one renderer for a `ReviewFailure`.** There is one `ReviewProblemBlock` definition, and both
  the surface's outcome region and the expansion pane render it — the expansion pane imports it rather
  than re-implementing a block for the same shape. Two *condensed* lines remain by design (the entry bar
  and the instead-note), and both take the same `ReviewFailure` the one classification produced.
- **Retry only for `network`.** Every other token carries the owner's own next action, and offering a
  retry beside it would imply the reader can clear a state only the owner can clear.
- **The source-inventory offer is a question, never a substitution.** It is offered only for an
  intent-only refusal and only as a labelled button; the client still names no dataset.
- **Design boundary — "exactly one statement" is a calling convention, not a structural property.**
  `shown` and `lastCoherent` are two independent props, so the region prints both notes if a caller ever
  passes a measured-empty `shown` together with a non-empty `lastCoherent`; the surface always passes the
  same object for both (or `null`), so no reachable state is affected. Measured (independent
  re-verification's region matrix): every consistent combination totals 0 or 1 statement, and the
  inconsistent combination is unreachable from the surface. Deriving `lastCoherent` from `shown`, or
  taking one prop, would make the invariant structural rather than conventional.
- **Boundary.** This module owns the *rendering* of every state that is not a review. Which state a
  response is belongs to `data/reviewTransport.ts`; which question was asked, what is retained and when
  the panes mount belong to `ReviewSurface.tsx`.

### Todos

None recorded. One routed item is recorded rather than fixed:

- **The browser-class A01/A13 journeys are not verified by this leaf.** No served dashboard bundle and
  no real browser were driven here, so nothing on this card is a claim about the real page: the
  refusal-visibility half is proven at the mounted-component level plus real HTTP through the real
  client, and the whole journeys — every modified/added diff opening and the retry-vs-target race —
  belong to **R25 (assembled acceptance) with R24 (usable review navigation) and R17 (coherent live
  refresh)**.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and phase
vocabulary, the two projections that decide what is rendered, the one failure renderer and its two
controls, the region that decides the notes, the two consumers that render through it, and the case
modules that drive the mounted surface and the expansion pane. Every anchor in a row occurs inside the
range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own vocabulary of the states a reader is owed distinctly, and its statement that nothing here invents a recovery route or renders an absent answer as an empty review.** | `known-empty`; `not-initialized`; `unavailable-history`; `validation`; `authority`; `domain-refused`; `network`; `unreadable` | dashboard/src/panels/review/ReviewOutcome.tsx:1-25 |
| The one projection and the one accessor this module imports, from the review client's public entry. | `intentOnlyRefusal`; `reviewProblemFromRefusal`; `unreadableAnswer` | dashboard/src/panels/review/ReviewOutcome.tsx:27-32 |
| **The read's four phases as one value, so a refusal and a payload can never both be the read.** | `ReviewRead` | dashboard/src/panels/review/ReviewOutcome.tsx:33-37 |
| **The one place a typed result becomes a phase: an unadmitted or payload-less answer is a failure, never an empty review.** | `readFrom` | dashboard/src/panels/review/ReviewOutcome.tsx:42-55 |
| **What the panes render: the answer, or — for a read that never answered — the last comparison the surface really read, while a typed refusal replaces the panes rather than sitting beside a comparison the server declined to stand behind.** | `shownPayload` | dashboard/src/panels/review/ReviewOutcome.tsx:61-68 |
| The one accessor for the failure a phase carries. | `problemOf` | dashboard/src/panels/review/ReviewOutcome.tsx:70-71 |
| **The in-flight state as its own rendering, so "nothing has answered yet" is distinguishable from "the answer was empty" and from every refusal.** | `ReviewLoading` | dashboard/src/panels/review/ReviewOutcome.tsx:75-81 |
| **Known-empty as a measurement of four facts, never a mood.** | `knownEmpty`; `KnownEmptyNote` | dashboard/src/panels/review/ReviewOutcome.tsx:86-94; dashboard/src/panels/review/ReviewOutcome.tsx:96-108 |
| **The one renderer for a `ReviewFailure`: every published field printed, an explicit sentence where the server published none, two test ids for the two refusal shapes, and the two conditional controls.** | `ReviewProblemBlock`; `review-offending-input`; `review-next-action`; `review-retry` | dashboard/src/panels/review/ReviewOutcome.tsx:115-177 |
| **The note that keeps a refusal visible beside the inventory the reader asked for instead.** | `TaskContextInsteadNote` | dashboard/src/panels/review/ReviewOutcome.tsx:183-195 |
| **The retained-generation label whose closing sentence is chosen by what the retained payload actually is.** | `RetainedGenerationNote` | dashboard/src/panels/review/ReviewOutcome.tsx:201-213 |
| **The one place the notes are decided, where the known-empty statement and the retained-generation label are mutually exclusive.** | `ReviewOutcomeRegion`; `measuredNothing`; `retainedIsReal` | dashboard/src/panels/review/ReviewOutcome.tsx:226-260 |
| The surface wires the outcome region to the target-bound read and appropriate retry/source actions. | `useSurface`; `ReviewSurface` | dashboard/src/panels/review/ReviewSurface.tsx:778-854; dashboard/src/panels/review/ReviewSurface.tsx:856-928 |
| SourceContent consumes the shared problem renderer for transported failures. | `SourceContent` | dashboard/src/panels/review/SourceContent.tsx:167-227 |
| **The mounted cases that pin each state and the retained-generation rules, including the F3 region cases.** | "shows a never-initialized refusal with its reason, offending input and next action"; "keeps source inspection reachable when only intent is unavailable, on request"; "says known empty for a measured empty answer and never for a failure"; "offers an explicit retry for a network failure, and the retry renders the answer"; "never renders a previous target's comparison under a new target's header"; "states a retained known-empty once, as the measured result it is, and never denies it" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:266-283; dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:284-313; dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:314-325; dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:357-376; dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:416-457; dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:481-491 |
| The expansion pane's transport-level cases, which render through this module's one block. | "carries the code, reason, offending input and next action of an unwired adapter" | dashboard/src/panels/review/SourceContentRefusal.test.tsx:52-78 |

| `ReviewProblemBlock` owns the behavior described above. | `ReviewProblemBlock` | dashboard/src/panels/review/ReviewOutcome.tsx:115-117 |
| `ReviewOutcomeRegion` owns the behavior described above. | `ReviewOutcomeRegion` | dashboard/src/panels/review/ReviewOutcome.tsx:226-228 |
| `knownEmpty` owns the behavior described above. | `knownEmpty` | dashboard/src/panels/review/ReviewOutcome.tsx:86-88 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The module renders one repository namespace's
records and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T21:09:39+00:00: Generated citation repair: `ReviewRead` repointed to dashboard/src/panels/review/ReviewOutcome.tsx:33-37. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:09:39+00:00: Generated citation repair: `readFrom` repointed to dashboard/src/panels/review/ReviewOutcome.tsx:42-55. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:09:39+00:00: Generated citation repair: `problemOf` repointed to dashboard/src/panels/review/ReviewOutcome.tsx:70-71. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T19:49:05Z — Reconciled the changed ownership and current behavior with the source.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **four enforced citation rows re-cited to the constructs they name, wording unchanged.** This leaf shortened `ReviewSurface.tsx` (995 → 910 lines) by moving the complete source change explorer into its own module, which moved every construct this row cites: the region's mount is now `888-895` (carrying `ReviewOutcomeRegion`, `retryFor` and `insteadFor` at their call sites, which also clears the range's out-of-bounds end) and the two helpers' own declaration extents are `458-459` (`retryFor`) and `463-472` (`insteadFor`). The row's `targetKeyOf` range `22-22` is kept verbatim and no claim was reworded or dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **created.** The module is new in this leaf and this is its one-to-one card. It records what the renderer is *for*: one value carrying the read's four phases instead of three parallel outcome states; the two projections that decide what the panes render (`shownPayload`'s deliberate asymmetry — a typed refusal replaces the panes, a transport failure does not erase them — and `readFrom`'s refusal to read an unadmitted or payload-less answer as a review); `knownEmpty` as four simultaneous measurements; the **one** `ReviewProblemBlock` both the surface and R03's expansion pane render, printing every published field and an explicit sentence where the server published none; the two conditional controls (retry for `network` only, the source-inventory offer for an intent-only refusal only); and `ReviewOutcomeRegion` as the one place the known-empty statement and the retained-generation label are decided. The card also records the measured **design boundary** the independent re-verification found: "exactly one statement" is a property of the surface's calling convention rather than of the region's two independent props — the inconsistent combination is unreachable from the surface, and deriving `lastCoherent` from `shown` would make it structural. Finally it records the routed item: the browser-class A01/A13 journeys are **not verified by this leaf** and belong to R25 with R24/R17. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate at that base. Nothing in this leaf is committed, so no commit contains the bytes a stamp would claim to have verified; closeout owns the stamp.
