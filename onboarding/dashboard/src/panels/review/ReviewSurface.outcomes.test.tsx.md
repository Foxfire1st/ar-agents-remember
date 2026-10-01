# dashboard/src/panels/review/ReviewSurface.outcomes.test.tsx

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

The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.

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
new header carries no `review-retained-generation` and no `data-comparison` — so a payload read for
another question cannot appear under this one.

**Since `260921-ICR-L48` the same case also pins what stays.** The Architect's L48-R1 ruling keeps the
workspace mounted when a newly selected subject's read fails, so the case now asserts that the failure is
stated in the reading area labelled with the requested subject (`review-reading-problem` with
`data-problem-subject="invariant:a-different-subject"`), that the task's own source inventory
(`review-inventory`, six changed files) **stays**, and that no `review-center` (A's reading) is rendered.
The earlier assertion that `review-inventory` disappears was **superseded** by that ruling, not weakened:
the inventory belongs to the task, not to either subject, and R26 isolation is still asserted on the
subject-bound parts.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own provenance and defect
statement, the measured bodies with their digests, the reduced payload builders, the two stubs, and the
fifteen cases grouped by what they pin. Every anchor in a row occurs inside the range that row cites.

- **The header's own provenance — the real component and client with only `fetch` stubbed, DOM-only assertions, measured bodies with digests — and its statement of the defect these cases control for.** [1]
- The real component, the real region and the real types under test. [2]
- **The measured refusal bodies, each carrying the digest of the run that produced it, and the reduced task-context fixture labelled as reduced.** [3]
- **The two payload builders: the task-context answer, and the measured empty one that is the only route to the known-empty statement.** [4]
- A successful answer wrapped the way the route wraps one. [5]
- **The two stubs: a response-shaped object and the global `fetch` that serves it, so the status, body and decode all travel the real path.** [6]
- The two calling conventions the surface really has: the task context and one recorded subject. [7]
- The cleanup and global-fetch restore between cases. [8]
- **The in-flight state rendered as itself before any answer arrives.** [9]
- **The conforming example the packet names, mounted: a never-initialized refusal with its reason, offending input and next action.** [10]
- **Source inspection stays reachable when only intent is unavailable, as a second question the reader asks.** [11]
- **Known empty said for a measured empty answer and never for a failure.** [12]
- **The three distinct failure states asserted apart in sequence.** [13]
- **The retry offered for a network failure, and the retry rendering the answer.** [14]
- A subject-level refusal distinct under its own code. [15]
- **An answer whose state this client does not admit is named, never rendered as a review.** [16]
- **The cross-target prohibition, mounted: nothing read for one subject may appear under another's header.** [17]
- **The region-level rule and its stated reachability reason, with the three constructions the three cases share.** [18]
- **The three region cases: retained known-empty stated once and never denied, retained real labelled with no emptiness denied, and a written review printing neither.** [19]
- **The surface the cases mount, and the one region that decides the notes they assert.** [20]
- The real surface composes the target-bound read and retained comparison that these cases exercise. [21]
### Cross-Repo References

No cross-repository behavior is exercised in this file. Every response is served by a stubbed
same-origin `fetch` and names one repository namespace.

No meaningful cross-repo references found.

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


## 260921-ICR-L23 The Boundary'S Own Sentence, And What It Must Not Read As

One case joins the module — `renders the boundary's own sentence when it could not compare the
declared identities (L23)` (`:885-914`). It mounts the subject with a `not-measured` staleness
whose statement names the uncompared channel, then asserts the three things the state exists for:
the boundary's sentence is rendered through `review-staleness-unmeasured`; no previous input and
no "current comparison" wording appears; and `review-stale` is absent, so the unmeasured state
never borrows the stale rendering.
