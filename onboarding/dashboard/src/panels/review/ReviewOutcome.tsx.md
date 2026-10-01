# dashboard/src/panels/review/ReviewOutcome.tsx

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

**Since `260921-ICR-L48`, `shownPayload` decides the subject's reading, not whether the shell stays.** It
is still keyed to the question on screen, so a newly selected subject that fails or is refused has no
shown payload. What the surface keeps around it is the read cycle's `frame` (the task context's last
admitted payload): when a frame exists, the workspace, navigation and source explorer stay mounted and the
requested subject's pending state, failure or refusal is stated **in the reading area**, labelled with that
subject, through this module's own `ReviewProblemBlock` (the surface passes it the subject label). Only a
read with no frame at all — the reviewer's first read — still renders its loading line or problem block
here at the surface level, as before.

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
payload are mutually exclusive there.** It renders the loading line for `loading` (`loadingLine`); the one
problem block for a carried problem, with `origin` chosen from the phase (`problemLine`) — both suppressed
when the surface passes `readingInWorkspace`, because the workspace then states that read in its reading
area, labelled with the requested subject, and a surface-level line would be a second, subject-less
statement of the same read (L48); the instead-note when a refusal was answered
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
- **A typed refusal replaces the subject's reading; a transport failure does not erase a retained
  comparison of the same question.** That asymmetry lives in `shownPayload`, in one place. Since L48 a
  refusal no longer replaces the *shell*: when the task context has a frame, the workspace stays mounted
  and the refusal is stated once, in the reading area, for the requested subject (Architect ruling on
  L48-R1). The superseded wording "a typed refusal replaces the panes" held only while every refusal
  unmounted the workspace.
- **One statement per read.** A read is stated either by this region at the surface level or by the
  workspace's reading area (`readingInWorkspace`), never both.
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and phase
vocabulary, the two projections that decide what is rendered, the one failure renderer and its two
controls, the region that decides the notes, the two consumers that render through it, and the case
modules that drive the mounted surface and the expansion pane. Every anchor in a row occurs inside the
range that row cites.

- **The header's own vocabulary of the states a reader is owed distinctly, and its statement that nothing here invents a recovery route or renders an absent answer as an empty review.** [1]
- The one projection and the one accessor this module imports, from the review client's public entry. [2]
- **The read's four phases as one value, so a refusal and a payload can never both be the read.** [3]
- **The one place a typed result becomes a phase: an unadmitted or payload-less answer is a failure, never an empty review.** [4]
- **What the panes render: the answer, or — for a read that never answered — the last comparison the surface really read, while a typed refusal replaces the panes rather than sitting beside a comparison the server declined to stand behind.** [5]
- The one accessor for the failure a phase carries. [6]
- **The in-flight state as its own rendering, so "nothing has answered yet" is distinguishable from "the answer was empty" and from every refusal.** [7]
- **Known-empty as a measurement of four facts, never a mood.** [8]
- **The one renderer for a `ReviewFailure`: every published field printed, an explicit sentence where the server published none, two test ids for the two refusal shapes, and the two conditional controls.** [9]
- **The note that keeps a refusal visible beside the inventory the reader asked for instead.** [10]
- **The retained-generation label whose closing sentence is chosen by what the retained payload actually is.** [11]
- **The one place the notes are decided, where the known-empty statement and the retained-generation label are mutually exclusive.** [12]
- The surface wires the outcome region to the target-bound read and appropriate retry/source actions. [13]
- SourceContent consumes the shared problem renderer for transported failures. [14]
- **The mounted cases that pin each state and the retained-generation rules, including the F3 region cases.** [15]
- The expansion pane's transport-level cases, which render through this module's one block. [16]

| `ReviewProblemBlock` owns the behavior described above. | `ReviewProblemBlock` | dashboard/src/panels/review/ReviewOutcome.tsx:115-117 |
| `ReviewOutcomeRegion` owns the behavior described above. | `ReviewOutcomeRegion` | dashboard/src/panels/review/ReviewOutcome.tsx:247-249 |
| `knownEmpty` owns the behavior described above. | `knownEmpty` | dashboard/src/panels/review/ReviewOutcome.tsx:86-88 |

### Cross-Repo References

No cross-repository behavior is implemented in this file. The module renders one repository namespace's
records and carries no identity that ranges beyond it.

No meaningful cross-repo references found.
