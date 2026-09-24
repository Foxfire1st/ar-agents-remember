# dashboard/src/panels/review/familyReview.continued.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.continued.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T00:43:00+02:00 |
| lastVerifiedCommitHash | `63b476297708f779de8ed5c0bf3555b9d1de70c2` |
| lastVerifiedCommitDate | 2026-09-24T04:10:11+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
recorded by the leaf's probe (`temp/icr/probe-l24-family-body.py`) and installed as the fixture the
family workspace case stubs `fetch` with. **48,240 bytes; sha256
`792d00c45728e6daf6a1b8a32424ad7b23edfa263e0abbbce7d4f1a3cc3bb04d`.** It is untracked in this leaf's
working tree (`??`), so these are candidate bytes a reader re-checks against the file, not bytes any
commit holds.

It is data with a provenance chain, not an assembled fixture: the case stubs **only `fetch`** and lets
the real client, the shared decode and the real component tree read these bytes. It is **not browser
evidence** — the repository's Playwright configs are Dagger-only and the case file says so in its own
header.

The envelope is the review read (`state: "review"`, `operation: "read_knowledge_review"`,
`surface_version: "knowledge-review-surface/1"`) over the fixture enclosure (`leaf_id: "260921-icr-l1"`,
master/task_ref `review-source-endpoints-fixture`) with the per-run fixture repository uuid normalized
to `<repository_id>`.

**What this body pins apart from its six siblings: it is a page of a roster walk continued from a
published cursor, and it is byte-for-byte the answer to the cursor its sibling published.** Its
`payload.page.continued_from` is the *same string* as `familyReview.truncated.captured.json`'s
`entry[0].after.page.continuation` (both decode to `position 1`, and the two strings are equal), which
is what makes the walk a walk: the client sends the cursor the server published, unchanged. It also
carries the **both-sides-listed** member row whose content fell outside the page — the row IS recorded
on both snapshots and only the after side's content is missing from this page.

## Code Commentary

### Logic

**The page block is the continuation answer, with both cursors on the wire.** `collection:
"family_members"`, `state: "continued"`, `continued_from` and `continuation` carried as opaque base64
cursors, `returned` 7, `remaining` 5, `total` 12 and `total_basis: "selection"`, with the scope naming
the side, the family revision, the policy version and `page_size=6`. The two cursors decode to
`knowledge-read-cursor/v1` payloads whose only difference is `position` (1 in, 7 out) — the page was
asked for from position 1 and answered with a cursor that reaches position 7.

**The cursor equality across two captured bodies is the whole point of the walk.** The `continuation`
that `familyReview.truncated.captured.json`'s after roster page published and this body's
`continued_from` are the same bytes. A reader can re-check it without a browser: decode both base64
strings and compare. The mounted case does the client-side half of the same fact — it reads the
`data-continuation` the roster control published, clicks it, and asserts the request carries that exact
value, which is why the walk can never be advanced from a cursor the client invented.

**The roster page on the continued side says where the cursor came from.** `entry[0].after.page` is
`state: "continued"` and carries the same `continued_from` and `continuation` as the payload-level
block, so the per-side roster line and the page line cannot disagree about which step of the walk this
is. The before side of the same family is an ordinary `first_page`.

**One row on this page is a membership without its content, recorded by both sides.** Member
`68584c1e-4952-4295-a304-c4ce25029a5b` (revision `30000000-0000-4000-8000-5a554b06baf8`) is
`state: "recorded"` on the before side and `state: "content_not_on_page"` on the after side, and the
row's own detail says the content `fell outside this page and is stated as such, not filled in`. That is
the shape the client must render as a statement **about the page** while still drawing the one-sided
statement from the side whose content is on the page — never as "the snapshot records no row" and never
as a comparison that was not made.

**The family context is `partial` and its counts are the owner's.** Two families, `membership_rows_total`
8, `unique_member_revision_total` 4; each side's remainder is published by the owner rather than
recomputed by the client, and the after side of the second family retained both of its revision ids.

**Five cases drive these bytes.** They walk the roster only from the cursor that family's own page
published (paired with the truncated body), head a bounded member context `partial` and count the
owner's rows, render the listed-but-uncarried row as a page fact, render a bounded page's missing row as
a page fact, and keep the reader's workspace state across two page requests issued by the centre's own
control.

### Conventions

- Captured bytes, never hand-edited: the provenance lives in the consuming case file's header, and this
  card adds no second provenance.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding, because a line number
  cannot distinguish two facts in a one-line file.
- The body is opaque data to this client: the case types it `unknown` and narrows it at runtime.
- Cursors are carried, never parsed, by the client: the base64 strings above are opaque to the surface
  and are forwarded exactly as published; decoding them is a *reader's* verification step, not a code
  path.
- Numbers on this card are the file's: byte size and digest are the file, counts are the owner's.

### Invariants And Boundaries

- **A page is not a whole.** The continued page states the row it carried, the rows remaining and the
  cursor that reaches them; it never claims the roster or the walk is complete.
- **The cursor belongs to the server.** The value the control sends is the value the page published;
  this body is the answer to exactly that value.
- **A row listed by both sides is not a missing row.** One side's content being outside the page is a
  fact about the page, and the other side's content is still rendered; the two facts must not be merged
  into "no comparison was made".
- **A captured body is evidence, not a specification.** The contract it evidences is the read response
  the route publishes and the client vocabulary that decides what may be said about a bounded page.
- **No conclusion is carried anywhere in the body.** The evidence state is `none_recorded`, the
  assessment state is `unassessed`, and the submission block is `unavailable`.
- **Not browser evidence.** These are the bytes a real route published, rendered by the real client in a
  mounted test tree; they are not a live page fed by a running publication.

### Todos

None recorded. The sibling bodies carry the truncated page this one continues and the row-not-carried
states; no obligation is attached to this file.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every row was re-derived against this candidate, and every anchor in a row occurs on the line the row
cites. Because each captured body is one minified line, the cited range is the whole file and the
finding names the exact key path and value a reader can re-check.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The enclosure the bytes were recorded over, and the single normalization: the per-run fixture repository uuid is written as a placeholder.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The page block that makes this a continuation: the collection, the continued state, both cursors, the returned/remaining/total arithmetic and its basis, and the scope the walk names.** | "\"collection\":\"family_members\""; "\"state\":\"continued\""; "\"continued_from\""; "\"returned\":7"; "\"remaining\":5"; "\"total\":12"; "\"total_basis\":\"selection\""; "\"page_size=6" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The cross-body identity that makes the walk a walk: the cursor this page continues is the cursor the sibling `truncated` body's after roster page published — the two strings are equal and both decode to `position 1`.** | "\"continued_from\""; "\"page_size=1" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1; dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The per-side roster page states where the cursor came from, so the roster line and the page line cannot disagree about the step.** | "\"state\":\"continued\""; "\"page\":{\"complete\":false" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The row listed by both sides whose content fell outside the page: the membership and revision identities, the row's own page-scoped detail, and the state that carries the distinction.** | "68584c1e-4952-4295-a304-c4ce25029a5b"; "30000000-0000-4000-8000-5a554b06baf8"; "while its revision content fell outside this page and is stated as such, not filled in"; "\"state\":\"content_not_on_page\"" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The family context and its owner's counts, still `partial` and still carrying every part it established.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"membership_rows_total\":8"; "\"unique_member_revision_total\":4" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| The one constant that binds this body to its cases, and the runtime narrowing that keeps a body with a missing field from mounting the surface. | `captured("familyReview.continued.captured.json")`; `firstFamilyId` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:43-52; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:62-89; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:57-57|
| **The provenance of every captured body: the real route's bytes recorded by the leaf's probe, with the real client and component tree reading them in the cases.** | "holds the bytes"; "probe-l24-family-body.py" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:6-12 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:23-27 |
| **The walk case this body answers, including the assertion that the value sent is the value the roster page published, unchanged.** | "walks a family roster only from the cursor that family's own page published"; `TRUNCATED`; `CONTINUED`; "The value sent is the value the family context's own roster page published, unchanged." | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:276-320; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:48-48; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:47-47|
| **The two page-scoped sentences this body's listed-but-uncarried row drives, and the bounded-view case that counts the owner's rows rather than this page's.** | "says a listed-but-uncarried row about the page, never that the snapshot records no row"; "says a bounded page's missing row about the page, never that the snapshot records none"; "heads a bounded member context partial and counts the owner's rows, not this page's" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:541-587; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:589-615; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:463-497 |
| The case that keeps the reader's workspace state across two page requests through the centre's own control, both of them answered by this body. | "keeps the reader's workspace state across two page requests through the centre's own control"; `CONTINUED` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:672-725; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:48-48|
| **The vocabulary the page-scoped row is read through: `content_not_on_page` as the state the distinction rests on, and `not_on_page` versus `one_sided` as two different facts.** | `content_not_on_page`; `not_on_page`; `one_sided`; `oneSidedMember` | dashboard/src/data/reviewFamily.ts:264-278; dashboard/src/data/reviewFamily.ts:298-321; dashboard/src/data/reviewFamily.ts:63-73 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the leaf's continued-roster body.** It records the file's exact identity (48,240 bytes; sha256 `792d00c45728e6daf6a1b8a32424ad7b23edfa263e0abbbce7d4f1a3cc3bb04d`) and the state it pins apart from its siblings: a **page of a walk continued from a published cursor**, whose `payload.page.continued_from` is byte-equal to the `continuation` the sibling `truncated` body's after roster page published (both decode to `position 1`) — the cross-body fact that makes "the client sends the cursor the server published" checkable without a browser. It also records that this body carries the **both-sides-listed** membership row whose content fell outside the page (member `68584c1e-4952-4295-a304-c4ce25029a5b`, revision `30000000-0000-4000-8000-5a554b06baf8`), which is the page-scoped sentence pair the two fix-round cases drive. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
