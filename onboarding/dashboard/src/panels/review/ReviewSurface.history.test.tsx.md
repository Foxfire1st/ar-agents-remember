# dashboard/src/panels/review/ReviewSurface.history.test.tsx

## Governing Overview

[panels route overview](../overview.md)

## Purpose

**The mounted cases that measure `ICR-R12@v1` at the browser surface**: the entry's historical target
reaches the server as the record the reader asked for, and the surface *states* which record it is
reading. `ReviewSurface` is the real component and `intentReview` the real client, so the query string
asserted below is the one the browser builds, and the provenance line is read out of the rendered DOM
rather than from a prop this test passed itself. Only `fetch` is stubbed.

The defect these two cases catch is the packet's own: a closed leaf's review used to be offered only
while the enclosure was live, and the surface had no way to name the record it wanted, so a leaf whose
worktree cleanup had removed the enclosure could not be reviewed at all. The historical target is what
the entry now carries, and the provenance line is what tells a reader the panes are the **recorded
comparison** rather than whatever the repository holds now.

The two cases are deliberately a pair, because one of them alone would leave the other failure open:

- **the recorded read**: the caller passes the record the entry carried, and the case asserts the
  request URL contains `history=recorded` **and** the subject, that the provenance line is mounted with
  its sentence, that `data-review-history` reads `recorded`, and that the refusal the recorded read
  earned still reaches the reader with its action — so a leaf that recorded nothing is a stated state
  rather than a missing entry;
- **the live read**: the caller names no record, and the case asserts the request carries **no**
  `history=` parameter, that no provenance line is mounted, and that `data-review-history` reads
  `live`. Without it, a surface that always sent the historical form would pass the first case while
  silently answering a different question for every ordinary live entry.

## Code Commentary

### Logic

The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.

**The entry's target is applied to the question rather than to the response.** `ReviewSurface` takes
`history` as part of its target, `targetKeyOf` includes it in the target key (the key is
`repo/master/leaf/<history ?? "live">/<question>/<position>`), and `intentReview` appends it to the
query string only when it is defined. So a response read for one record is never applied to a surface
that asked for another, and the live read stays byte-identical to the request every existing caller
makes — which is exactly what the second case pins.

**The provenance line is a claim about everything under it, not decoration.** `ReviewHeader` renders the
`data-testid="review-history"` paragraph only when the record is `recorded`, and the surface publishes
`data-review-history` on its own root, so both a reader and a case can see which record the panes are
read from without opening a pane. The case asserts the rendered sentence contains "recorded comparison"
and that the refusal region carries `data-review-code="candidate_not_live"` with the
"records no comparison generation" detail — the shape a closed leaf with nothing recorded really earns.

**Only `fetch` is stubbed; everything else is the shipped client.** `serving()` returns the refusal body
with a 404 status, which is how the route answers a refusal, and `requestUrl()` reads the first call's
URL from the fetch mock. The component still resolves through the shared review decode, the real
`intentReview`, and the real panes' rendering path, so the assertions are about produced behaviour
rather than about a mock's contract.

### Conventions

The module sits beside the surface it measures and is named for the property it pins rather than for the
leaf that added it. Constants (`REPO`, `MASTER`, `LEAF`, `SUBJECT`) name one real task context, and
`NOTHING_RECORDED` is the server's own refusal body — including its `next_action` — so the case fails if
the surface stops showing an action the server supplied. `afterEach` calls `cleanup()` and
`unstubAllGlobals()` so no case observes another's DOM or stubbed global.

### Invariants And Boundaries

- **No record is claimed that was not asked for.** The live case asserts the absence of the history
  parameter and of the provenance line; the recorded case asserts both present with the record named.
- **The refusal is shown, never hidden behind the entry.** The entry stays openable and the refusal
  reaches the reader with its code, detail and action.
- **The assertion reads the built query string.** It is the URL the real client produced, not a
  hand-built string compared against itself.
- **The browser boundary is R24/R25's.** This module is a mounted-component case over the real client;
  the leaf-history drill-down navigation is `ICR-R24@v1`'s and the assembled browser acceptance is
  `ICR-R25@v1`'s.
- **No limit was widened to admit these cases.** The surface's own `ReviewHeader`/`ReviewPanes`
  extraction is what kept the component inside its lint rail; this module adds no ignore and no rule
  exception.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's two cases, the surface and
client they drive, and the entry that produces the historical target in the first place. Three details a
reader should carry: the record is part of the surface's **question key**, so switching records reloads
rather than reinterpreting; the live read's query string is unchanged from every existing caller's; and
the entry that supplies `history="recorded"` is the change-set bar's closed-leaf branch, which is where
the "Intent review (recorded)" label is chosen.

- **The module's own statement of what it exercises and the defect it catches, including that only `fetch` is stubbed.** [1]
- The one real task context the cases name, and the subject the historical target carries. [2]
- **The refusal a closed leaf with nothing recorded earns, carried verbatim from the server so the case fails if the surface stops showing the action.** [3]
- The test server stub supplies the response body; requestUrl reads the actual request emitted by the client. [4]
- Recorded task review sends the historical selector and states the recorded comparison in the mounted surface. [5]
- A live entry sends no historical selector and makes no recorded-comparison claim. [6]
- **The surface's half: the record is part of the target key, the header states it, and the root publishes which record was read.** [7]
- **The panes mounted as one block for one payload, which is what the extraction that cleared the lint rail produced: `ReviewPanes` mounts the workspace and the technical-details disclosure, whose knowledge, source and evidence panes live in `ReviewRecordPanes.tsx` since L48 and render only for the payload that answers the subject on screen.** [8]
- **The client's half: the record is appended to the query string only when it is defined, and it carries the one value the server admits.** [9]
- **The entry that produces the historical target: the closed leaf keeps its Intent review, labelled as the recorded one, and the working change-set stays live-gated. Since `260921-ICR-L47` the target and label are built by `IntentReviewEntry`, which `LeafEntries` mounts.** [10]
- **The takeover that hands the record to the surface: a closed leaf's entry carries `historical`, and the surface then asks for that leaf's recorded comparison.** [11]
- **The target field the record travels in, beside the subject the entry already carried.** [12]
- **The server's admission of the one historical form, and the transport ref that carries it beside the subject.** [13]

### Cross-Repo References

No cross-repository behavior is exercised by this module. It drives one repository's own review route
through a stubbed transport.

No meaningful cross-repo references found.
