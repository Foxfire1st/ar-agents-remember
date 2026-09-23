# dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T06:50:00+02:00 |
| lastVerifiedCommitHash | `4c000b11c5243e4a8e77c08e87984fff00c1d94b` |
| lastVerifiedCommitDate | 2026-09-23T20:33:15+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The mounted-surface half of ICR-R16: the **real `ReviewSurface` over the real review client, for every
state that is not a plain success.** Fifteen cases in two `describe` blocks (twelve mounted, three
region-level).

Its evidentiary claim is narrow and stated in the module header: `ReviewSurface` is the real component
and `intentReview` the real client; **only `fetch` is stubbed**, so each response travels the way the
browser's does — status, body, the shared decode in `data/reviewTransport.ts`, the component tree — and
**no assertion reads a prop this test itself passed**: every case asserts what the rendered DOM
contains. The refusal bodies are the measured output of the real route over real HTTP in this leaf's
evidence run, each carrying the `sha256-normalized` digest of the body it copied.

The defect these cases catch is stated in the header too, because a reader of a negative control needs
to know what it controls for: the surface used to catch the client's throw and print
`the review read failed: 404 Not Found`, so the route's typed refusal — code, reason, offending input,
the action that initializes the dataset — was dropped, **and** a failed re-read erased the comparison
already on screen. Every refusal case below fails against that surface, and so does the
retained-generation case.

## Code Commentary

### Logic

**The measured bodies are declared once, with their digests.** `DATASET_ABSENT` is the real `404` for a
never-initialized subject review (`sha256-normalized 834c79f4…`) with its reason, its next action and
`offending_input: knowledge-candidate.sqlite`; `BAD_REQUEST` is the real `400` for a selector the route
does not admit (`8a45fcd3…`) including `expected: "invariant, family, or no selector at all"`;
`UNWIRED` is the real `503` for a process composed without the adapter (`c55ee098…`); `BAD_PATH` is the
real `400` for a refused authority (`3f8a79a5…`). None of the last three carries a repository id, so
their raw and normalized digests coincide — a fact the source states rather than leaves for a reader to
wonder about.

**The payload fixtures are labelled as reduced, not as measured bytes.** `taskContextPayload()` builds
the task-context answer whose inventory rows, counts and wording are the six paths the same run
measured, and `emptyPayload()` reduces it to a **measured** empty result: zero entries,
`listed_total: 0` and a detail saying the bound pair differs at no path. That distinction is
load-bearing — `emptyPayload` is the only thing in the module that may reach the known-empty statement,
and `reviewed(payload)` wraps a payload in the `state: "review"` envelope so a successful answer is
built the way the route builds one.

**The stubs are response-shaped, not client-shaped.** `response(status, body, statusText)` returns
`{ ok, status, statusText, json }` for the given values, and `serving` installs it as the global
`fetch`. `mount()` renders the surface for the task context and `mountSubject()` for one recorded
invariant, so the two calling conventions the surface really has are the two the cases use.
`afterEach` cleans up and restores the global fetch.

**`describe("the review surface's read states")` walks the distinct outcomes in the order a reader meets
them.** The in-flight state renders as itself before any answer arrives; a never-initialized refusal
renders with its reason, offending input and next action; source inspection stays reachable on request
when only intent is unavailable (the second, explicitly asked read with no selector); known empty is
said for a measured empty answer **and never for a failure**; the unavailable-adapter, validation and
authority states are asserted apart in sequence; a network failure offers an explicit retry and the
retry renders the answer; a subject-level refusal stays distinct under its own code; and an answer whose
`state` this client does not admit is named rather than rendered as a review.

**The F4 case is the cross-target prohibition, and it is mounted rather than asserted at the region.**
"never renders a previous target's comparison under a new target's header" reads a real comparison for
one subject, then re-renders the surface for a **different** subject whose read fails, and asserts the
new header carries no `review-inventory`, no `review-retained-generation` and no `data-comparison` — so
a payload read for another question cannot appear under this one.

**`describe("the outcome region's two statements about a measured-empty payload")` pins the rule where
it lives, and says why there.** The comment above it records the measured reachability fact: the state
the two statements must not both appear in — a failed read over a **retained** known-empty generation —
needs a same-target re-read, which the shipped props cannot produce because Cockpit remounts the
takeover per target. So the region is where the rule is pinned: a retained known-empty prints the
known-empty statement once and is never denied; a retained real comparison prints the retained label and
denies no emptiness for it; and a written review prints neither, while an empty *answer* prints only the
known-empty statement.

### Conventions

The module imports its types from `../../data/review`, the region and its phase type from
`./ReviewOutcome`, and the surface from `./ReviewSurface` — it exercises the shipped tree rather than
re-declaring any of it. Fixtures are upper-case where they are constant bodies and lower-case functions
where they are built (`taskContextPayload`, `emptyPayload`); helpers are plain lower-case functions; and
the region block declares its own `failure`, `region(...)` renderer and `statements(view)` reader inside
the `describe`, so the three region cases share one construction. Each case is an `async` `it` that
awaits the DOM via `findBy*`/`waitFor` rather than asserting synchronously.

### Invariants And Boundaries

- **Only `fetch` is stubbed.** The URL, the status, the body, the shared decode and the component tree
  are all the real ones.
- **Every assertion reads rendered output.** No case asserts a prop it passed or a value it computed;
  each reads `data-review-state`, `data-review-code`, a `data-testid` or `textContent` from the DOM.
- **The bodies are measured, and their digests are quoted.** A case that fails can be re-measured
  against this leaf's evidence run rather than argued about.
- **Known-empty is a measured result.** It is reachable only from `emptyPayload`, whose inventory is
  `measured` with `listed_total: 0`.
- **The retained generation belongs to the question it was read for.** The F4 case asserts the
  prohibition, and the region cases assert the two notes are mutually exclusive.
- **The region cases are region-level on purpose.** The comment states the measured reason (the
  same-target re-read is not reachable through today's props) instead of implying the mounted surface
  proves the same thing.
- **Boundary.** This module pins the mounted surface and the outcome region. It does not drive the entry
  bar (`reviewEntryRefusal.test.tsx`), the expansion pane (`SourceContentRefusal.test.tsx`) or the
  transport contract (`data/reviewTransport.test.ts`), and it makes **no** browser-level claim: the
  A01/A13 journeys over a served dashboard belong to R25 with R24/R17.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own provenance and defect
statement, the measured bodies with their digests, the reduced payload builders, the two stubs, and the
fifteen cases grouped by what they pin. Every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own provenance — the real component and client with only `fetch` stubbed, DOM-only assertions, measured bodies with digests — and its statement of the defect these cases control for.** | `ReviewSurface`; `intentReview` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:1-29 |
| The real component, the real region and the real types under test. | `ReviewOutcomeRegion`; `ReviewSurface`; `ReviewRead` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:25-29 |
| **The measured refusal bodies, each carrying the digest of the run that produced it, and the reduced task-context fixture labelled as reduced.** | `DATASET_ABSENT`; `BAD_REQUEST`; `UNWIRED`; `BAD_PATH`; `INVENTORY_DETAIL` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:31-92 |
| **The two payload builders: the task-context answer, and the measured empty one that is the only route to the known-empty statement.** | `taskContextPayload`; `emptyPayload` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:94-215 |
| A successful answer wrapped the way the route wraps one. | `reviewed` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:192-197 |
| **The two stubs: a response-shaped object and the global `fetch` that serves it, so the status, body and decode all travel the real path.** | `response`; `serving` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:217-230 |
| The two calling conventions the surface really has: the task context and one recorded subject. | `mount`; `mountSubject` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:232-244 |
| The cleanup and global-fetch restore between cases. | `afterEach` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:25-29; dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:246-249 |
| **The in-flight state rendered as itself before any answer arrives.** | "shows the read as in flight before any answer arrives" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:251-265 |
| **The conforming example the packet names, mounted: a never-initialized refusal with its reason, offending input and next action.** | "shows a never-initialized refusal with its reason, offending input and next action" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:266-283 |
| **Source inspection stays reachable when only intent is unavailable, as a second question the reader asks.** | "keeps source inspection reachable when only intent is unavailable, on request" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:284-313 |
| **Known empty said for a measured empty answer and never for a failure.** | "says known empty for a measured empty answer and never for a failure" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:314-325 |
| **The three distinct failure states asserted apart in sequence.** | "keeps the unavailable-adapter, validation and authority states apart" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:326-356 |
| **The retry offered for a network failure, and the retry rendering the answer.** | "offers an explicit retry for a network failure, and the retry renders the answer" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:357-376 |
| A subject-level refusal distinct under its own code. | "keeps a subject-level refusal distinct, under its own code" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:377-402 |
| **An answer whose state this client does not admit is named, never rendered as a review.** | "names an answer whose state it does not admit, instead of rendering it as a review" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:403-415 |
| **The cross-target prohibition, mounted: nothing read for one subject may appear under another's header.** | "never renders a previous target's comparison under a new target's header" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:416-457 |
| **The region-level rule and its stated reachability reason, with the three constructions the three cases share.** | `failure`; `region`; `statements` | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:458-479 |
| **The three region cases: retained known-empty stated once and never denied, retained real labelled with no emptiness denied, and a written review printing neither.** | "states a retained known-empty once, as the measured result it is, and never denies it"; "labels a retained real comparison and denies no emptiness for it"; "says nothing of either kind for a written review, and only known-empty for an empty answer" | dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx:481-513 |
| **The surface the cases mount, and the one region that decides the notes they assert.** | `ReviewOutcomeRegion`; `shownPayload`; `knownEmpty`; `RetainedGenerationNote` | dashboard/src/panels/review/ReviewOutcome.tsx:59-70; dashboard/src/panels/review/ReviewOutcome.tsx:85-106; dashboard/src/panels/review/ReviewOutcome.tsx:188-204; dashboard/src/panels/review/ReviewOutcome.tsx:206-251 |
| The surface composition these cases drive: the four-phase read and the target-keyed retained generation. | `ReviewSurface`; `targetKeyOf` | dashboard/src/panels/review/ReviewSurface.tsx:606-946; dashboard/src/panels/review/ReviewSurface.tsx:539-539 |
## Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed
same-origin `fetch` and names one repository namespace.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **created.** The module is new in this leaf and this is its one-to-one card. It records what the fifteen cases are *for* — the mounted surface for every state that is not a plain success, and the outcome region for the two statements about a measured-empty payload — plus the module's own evidentiary discipline and its two deliberate limits. The discipline: only `fetch` is stubbed, every assertion reads the DOM rather than a prop the test passed, and each refusal body is the real route's measured answer with its `sha256-normalized` digest quoted in the source. The limits: the region cases are region-level **because** the same-target re-read that would reach the retained-known-empty state mounted is not reachable through today's props (the module says so in its own comment), and the module makes **no browser-level claim** — the A01/A13 journeys over a served dashboard belong to R25 with R24/R17. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00) — the line this candidate now sits on after the leaf's pair sync — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate at that base. Nothing in this leaf is committed, so no commit contains the bytes a stamp would claim to have verified; closeout owns the stamp.

## 260921-ICR-L17 The Refresh Path, The Carried Identity And The Read Race

`260921-ICR-L17` (`ICR-R17@v1`) adds a third `describe` block — sixteen cases become twenty-two — and
extends the import list with `act`, which is what lets a case put two React updates in one flush.

**What the new block measures.** `describe("the review surface's refresh control and read race
(ICR-R17)")` drives the real surface over the real client with only `fetch` stubbed, and its six cases
pin one property each:

- **the refresh path end to end** — the read carries the identity on screen, the notice names both
  digests, the panes hold the current comparison, and the sentence is asserted to agree with the pane's
  own `data-comparison`, so wording and DOM cannot drift apart;
- **a failed refresh** — the labelled old comparison and its error stay on screen and **no** generation
  claim is rendered, because a read that never reached the server has answered nothing;
- **the read race** — a slow earlier subject's answer that lands after the newer selection cannot
  replace it, neither its comparison nor its header;
- **the same-flush interleaving** (`L17-R2-F1`) — the subject change and the refresh click inside one
  `act` produce exactly two reads, the second carrying nothing, and no notice at all;
- **the two single-question cases** (`L17-F1`) — a different subject, and the same subject read from the
  leaf's record, each carry nothing, and neither leaves a generation claim or a `review-stale` block
  behind.

**Why the flush cases matter.** They are the only cases that can reach the defects the two fix rounds
closed: a read-number-only guard and a sticky carried identity are both invisible to a case that lets
React settle between the two updates.


## Update History
- 2026-09-23T06:50:00+02:00 — 260921-ICR-L17 curator (candidate `ar/260921-icr-l17`, uncommitted; production line at this leaf's base `c422dc00273d4ae7a5d8c9c8db97365b8c85d640`, confirmed from the enclosure contract): **the refresh path, the carried identity and the read race are measured (`ICR-R17@v1`).** A third `describe` block adds six cases over the real surface and client — the end-to-end refresh, the failed refresh that renders no claim, the superseded-answer race, the same-flush interleaving (`L17-R2-F1`), and the two single-question cases (`L17-F1`) — and the module grows from sixteen to twenty-two cases. **Stamp accounting:** the verification pair names this leaf's base — the last real commit the reading was taken against — because the new cases exist only in this leaf's uncommitted working tree; closeout owns the stamp once the code commit exists.

## 260921-ICR-L23 The Boundary'S Own Sentence, And What It Must Not Read As

One case joins the module — `renders the boundary's own sentence when it could not compare the
declared identities (L23)` (`:885-914`). It mounts the subject with a `not-measured` staleness
whose statement names the uncompared channel, then asserts the three things the state exists for:
the boundary's sentence is rendered through `review-staleness-unmeasured`; no previous input and
no "current comparison" wording appears; and `review-stale` is absent, so the unmeasured state
never borrows the stale rendering.

## Update History
- 2026-09-23T20:30:00+02:00 — 260921-ICR-L23 curator (memory worktree only; no code changed, no commits; leaf base `473ad8242bb4c22bdabed5d5253767350381eb3e` plus the working-tree delta): **the module gained the case that pins the unmeasured line, and this card's body now states what it asserts.** `renders the boundary's own sentence when it could not compare the declared identities (L23)` (`:885-914`) mounts a `not-measured` payload and asserts the boundary's sentence is rendered, that no previous input or current-comparison wording appears, and that `review-stale` is absent. The new section above is the durable statement. **No verification stamp was advanced**: the candidate is uncommitted, so no commit holds the content a stamp would claim to have verified, and the governed closeout owns the real code and memory commits.
