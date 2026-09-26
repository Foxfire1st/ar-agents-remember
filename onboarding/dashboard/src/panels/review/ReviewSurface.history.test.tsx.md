# dashboard/src/panels/review/ReviewSurface.history.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/ReviewSurface.history.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T19:49:05Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's two cases, the surface and
client they drive, and the entry that produces the historical target in the first place. Three details a
reader should carry: the record is part of the surface's **question key**, so switching records reloads
rather than reinterpreting; the live read's query string is unchanged from every existing caller's; and
the entry that supplies `history="recorded"` is the change-set bar's closed-leaf branch, which is where
the "Intent review (recorded)" label is chosen.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of what it exercises and the defect it catches, including that only `fetch` is stubbed.** | `ReviewSurface`; `intentReview` | dashboard/src/panels/review/ReviewSurface.history.test.tsx:1-14; dashboard/src/panels/review/ReviewSurface.tsx:856-928; dashboard/src/data/review.ts:543-559 |
| The one real task context the cases name, and the subject the historical target carries. | `REPO`; `MASTER`; `LEAF`; `SUBJECT` | dashboard/src/panels/review/ReviewSurface.history.test.tsx:27-30 |
| **The refusal a closed leaf with nothing recorded earns, carried verbatim from the server so the case fails if the surface stops showing the action.** | `NOTHING_RECORDED`; `candidate_not_live` | dashboard/src/panels/review/ReviewSurface.history.test.tsx:34-49 |
| The test server stub supplies the response body; requestUrl reads the actual request emitted by the client. | `serving`; `requestUrl` | dashboard/src/panels/review/ReviewSurface.history.test.tsx:51-64; dashboard/src/panels/review/ReviewSurface.history.test.tsx:66-68 |
| Recorded task review sends the historical selector and states the recorded comparison in the mounted surface. | "asks for the leaf's recorded comparison and says so when the entry carries the record" | dashboard/src/panels/review/ReviewSurface.history.test.tsx:76-112 |
| A live entry sends no historical selector and makes no recorded-comparison claim. | "asks for the live candidate and claims no record when the entry names none" | dashboard/src/panels/review/ReviewSurface.history.test.tsx:114-133 |
| **The surface's half: the record is part of the target key, the header states it, and the root publishes which record was read.** | `targetKeyOf`; `ReviewHeader`; `history?: ReviewHistory`; "review-history"; `data-review-history={history ?? "live"}` | dashboard/src/panels/review/ReviewSurface.tsx:722-776; dashboard/src/panels/review/ReviewSurface.tsx:817-817; dashboard/src/panels/review/ReviewSurface.tsx:885-885 |
| **The three panes mounted as one block for one payload, which is what the extraction that cleared the lint rail produced.** | `ReviewPanes` | dashboard/src/panels/review/ReviewSurface.tsx:658-720 |
| **The client's half: the record is appended to the query string only when it is defined, and it carries the one value the server admits.** | `intentReview`; `history?: ReviewHistory`; `params.history = history`; `export type ReviewHistory = "recorded"` | dashboard/src/data/review.ts:543-559; dashboard/src/data/review.ts:470-470; dashboard/src/data/review.ts:487-487; dashboard/src/data/review.ts:495-495 |
| **The entry that produces the historical target: the closed leaf keeps its Intent review, labelled as the recorded one, and the working change-set stays live-gated.** | `LeafEntries`; `historical: true`; "Intent review (recorded)" | dashboard/src/panels/detail-panel/changeSetBar.tsx:421-497 |
| **The takeover that hands the record to the surface: a closed leaf's entry carries `historical`, and the surface then asks for that leaf's recorded comparison.** | `ChangeSetTakeover` | dashboard/src/cockpit/Cockpit.tsx:561-600 |
| **The target field the record travels in, beside the subject the entry already carried.** | `ChangeSetTarget` | dashboard/src/panels/changeset/ChangeSetViewer.tsx:33-55 |
| **The server's admission of the one historical form, and the transport ref that carries it beside the subject.** | `RECORDED_HISTORY`; `_admitted_history`; `ReviewQuestionRef`; `ReviewSelectorRef` | mcp/src/agents_remember/serving/review.py:419-438; mcp/src/agents_remember/serving/review.py:79-79; mcp/src/agents_remember/serving/review.py:219-240; mcp/src/agents_remember/serving/review.py:246-246 |

## Cross-Repo References

No cross-repository behavior is exercised by this module. It drives one repository's own review route
through a stubbed transport.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T21:10:04+00:00: Generated citation repair: `REPO`; `MASTER`; `LEAF`; `SUBJECT` repointed to dashboard/src/panels/review/ReviewSurface.history.test.tsx:27-27; dashboard/src/panels/review/ReviewSurface.history.test.tsx:28-28; dashboard/src/panels/review/ReviewSurface.history.test.tsx:29-29; dashboard/src/panels/review/ReviewSurface.history.test.tsx:30-30. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:04+00:00: Generated citation repair: `ReviewPanes` repointed to dashboard/src/panels/review/ReviewSurface.tsx:658-720. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:10:04+00:00: Generated citation repair: `LeafEntries`; "Intent review (recorded)" repointed to dashboard/src/panels/detail-panel/changeSetBar.tsx:421-497; dashboard/src/panels/detail-panel/changeSetBar.tsx:489-489. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T19:49:05Z — The comparison-focused cases isolate the shared catalogue hook so its additional request cannot consume a comparison fixture. The ordinary-entry catalogue/comparison interaction is covered separately by ReviewSurface.navigation.test.tsx. Assertions follow the compact labels, central display controls and changed-region default without weakening the existing record, paging or refusal contracts.
- 2026-09-24T17:20:00+02:00 — 260921-ICR-L32 curator (uncommitted change set on `ar/260921-icr-l32-ar`, code base `71a170796f5380bd3a5b65a5c3323ca4f92b0cc0` plus the working-tree delta; gate `verify-l32-round2.md` = `pass`): **citation pass — the rows this leaf's own line movement displaced were re-anchored from each row's own finding message.** Every flagged range was repointed or widened to the lines that actually carry the anchor at this candidate, using the memory-quality checklist's own per-row message as the ground truth rather than adding a delta to an old number; the repair was applied row-scoped by the cited-range string, so duplicate rows were each corrected. No claim was re-worded to fit a stale pointer, no anchor or range was dropped to silence a finding, and the two legacy mechanical-projection bullets on rows this pass re-read were retired with this entry as their dated disposition, and no new projection bullet was written. No verification stamp was advanced: the candidate is uncommitted, so no commit carries this body, and the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **five enforced citation rows re-cited to the constructs they name, wording unchanged.** This leaf shortened `ReviewSurface.tsx` (995 → 910 lines) by moving the complete source change explorer into its own module, so three ranges that ended past the file's end were rewritten to the constructs they cite — the surface component `819-910` (`ReviewSurface`), the provenance paragraph `809-814` (`review-history`) and the root's record attribute `869-869` (`data-review-history={history ?? "live"}`) — and the panes block was re-cited to `ReviewPanes`'s own extent `712-765`, which is what reopens-then-holds that claim: its declaration now falls inside a cited range. The client's half followed `intentReview` to its declaration range `data/review.ts:533-549`. Contributing ranges (`targetKeyOf` `22-22`, `ReviewHeader`'s `858-903`, the three client single-line ranges and the module's own `1-14`) are kept verbatim and no claim was reworded or dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T05:15:00+02:00 — 260921-ICR-L12 curator (candidate `ar/260921-icr-l12`, uncommitted; production line at this leaf's base `870701b43039cd205a8c98e418382729510c3de3`, confirmed from the enclosure contract): created this one-to-one card for the mounted client case module this leaf introduced (`ICR-R12@v1`). The card records the two properties the pair pins — the recorded read asks for the record it was handed and says so, and the live read asks for no record and claims none — and why each case is necessary to keep the other's failure open. The boundaries this leaf routes rather than closes are stated: R24 owns the leaf-history navigation and R25 the assembled browser acceptance. **Stamp accounting:** the verification pair names the production line at this leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate; the governed closeout owns the real stamp once the code commit exists.
