# dashboard/src/panels/review/familyReview.continued.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.continued.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:52:00+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c` |
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
**re-captured by MIK-L31 from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder) with L44's producer,
first build accepted, and installed as the fixture the family workspace cases stub `fetch` with. **49,355 bytes;
sha256 `9e13e39f3eb51f83c81f5eb878917c61c1aa6a68cf9bf895218333923c27e563`**, as its row in
`familyReview.capture-provenance.json` (`mik_l31_recapture`) records. It is the `bounded1-continued` request: the
truncated body's `retry-budget-family` after-side cursor, read at page size 6.

It is data with a provenance chain, not an assembled fixture: the cases stub **only `fetch`** and let the real
client, the shared decode and the real component tree read these bytes. It is **not browser evidence**.

The envelope is the review read (`state: "review"`, `operation: "read_knowledge_review"`,
`surface_version: "knowledge-review-surface/1"`) over the fixture enclosure (`leaf_id: "260921-icr-l1"`,
master/task_ref `review-source-endpoints-fixture`) with the per-run fixture repository uuid normalized
to `<repository_id>`.

**What this body pins: it is a page of a roster walk continued from a published cursor, and it is byte-for-byte
the answer to the cursor its sibling published.** Its `payload.page.continued_from` is the same string as
`familyReview.truncated.captured.json`'s `retry-budget-family` after-side `page.continuation` (both decode to
`position 1`). It also carries a **both-sides-listed** member row whose content fell outside the page on one side.

## Code Commentary

### Logic

The consumer sends the exact cursor published by the selected side. This continued capture answers the after-side
walk of `retry-budget-family`; when the control selected the before walk or another primary revision selection,
the client rejects that response and retains the coherent display.

**The page block is the continuation answer, with both cursors on the wire.** `collection:
"family_members"`, `state: "continued"`, `continued_from` and `continuation` carried as opaque base64 cursors,
`returned` 7, `remaining` 5, `total` 12 and `total_basis: "selection"`, with the scope naming `side=after`, family
revision `79ce3ed4…`, the policy version and `page_size=6`. The two cursors decode to `knowledge-read-cursor/v1`
payloads whose position is 1 in and 7 out.

**The per-side roster page states where the cursor came from.** `retry-budget-family`'s after page is
`state: "continued"` and carries the same `continued_from` and `continuation` as the payload-level block; the other
three side pages are ordinary `first_page`s at page size 6.

**One row on this page is a membership without its content, recorded by both sides.** Member
`cb5d5f97-d379-457f-9fa4-f41ef41beeb5` (revision `3fb46ae4-dd0a-41c1-8833-7ecf69d76101`, `candidate-batch-atomicity`)
is `state: "recorded"` on the before side and `state: "content_not_on_page"` on the after side, and the row's own
detail says the content is "stated as such, not filled in". The client renders that as a statement about the page
while still drawing the statement from the side whose content is on the page.

**The family context is `partial` and its counts are the owner's.** Two families, `membership_rows_total` 8,
`unique_member_revision_total` 4; every side carried both of its 2 recorded rows. The selected subject's revision
selection is `ambiguous`, and `source.unresolved` holds two attribution rows.

**Five cases drive these bytes:** the walk case (with `truncated`), the bounded member-context case, the
uncarried-operand case, the bounded before-only case, and the workspace-state case across two page requests.

### Conventions

- Captured bytes, never hand-edited: the provenance is the receipt's `mik_l31_recapture` row.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding, because a line number
  cannot distinguish two facts in a one-line file.
- The body is opaque data to this client: the cases type it `unknown` and narrow it at runtime.
- Cursors are carried, never parsed, by the client; decoding them is a reader's verification step.
- Numbers on this card are the file's; the identities are one draw of the scenario builder.

### Invariants And Boundaries

- **A page is not a whole.** The continued page states the rows it carried, the rows remaining and the
  cursor that reaches them; it never claims the roster or the walk is complete.
- **The cursor belongs to the server.** The value the control sends is the value the page published;
  this body is the answer to exactly that value.
- **A row listed by both sides is not a missing row.** One side's content being outside the page is a
  fact about the page, and the other side's content is still rendered.
- **No conclusion is carried anywhere in the body**, and **not browser evidence**.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every row was re-derived against the MIK-L31 re-capture, and every anchor in a row occurs on the line the row
cites. Because each captured body is one minified line, the cited range is the whole file and the finding names the
exact key path and value a reader can re-check.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The enclosure the bytes were recorded over, and the single normalization.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The page block that makes this a continuation: the collection, the continued state, both cursors, the returned/remaining/total arithmetic and the scope.** | "\"collection\":\"family_members\""; "\"state\":\"continued\""; "\"continued_from\""; "\"returned\":7"; "\"remaining\":5"; "\"total\":12"; "\"page_size=6" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The row listed by both sides whose content fell outside the page on one side.** | "cb5d5f97-d379-457f-9fa4-f41ef41beeb5"; "3fb46ae4-dd0a-41c1-8833-7ecf69d76101"; "\"state\":\"content_not_on_page\""; "stated as such, not filled in" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The family context and its owner's counts, still `partial`.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"membership_rows_total\":8"; "\"unique_member_revision_total\":4" | dashboard/src/panels/review/familyReview.continued.captured.json:1-1 |
| **The receipt row for this file in the MIK-L31 re-capture: the truncated body's after-side cursor at page size 6.** | "familyReview.continued.captured.json" | dashboard/src/panels/review/familyReview.capture-provenance.json:67-67 |
| The one constant that binds this body to its cases, and the runtime narrowing. | "const CONTINUED"; "function firstFamilyId" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:69-69; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:87-110 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:32-36 |
| The client sends the selected published cursor unchanged and rejects this capture when it answers another side or primary selection. | "sends the family's published cursor and refuses a response from another walk" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:299-342 |
| The continuation cases preserve page-scoped missing content and owner-measured totals without inventing primary statement absence. | "does not turn an uncarried roster operand into an absent statement"; "retains a bounded before-only membership without claiming that the invariant was removed"; "it(\"heads a bounded member context partial" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:600-616; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:618-630; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:504-548 |
| The captured continuation verifies that family selection, filter, layout, full-file preference and continuation controls survive two page reads. | "keeps the reader's workspace state across two page requests through the centre's own control" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:695-748 |
| **The vocabulary the page-scoped row is read through: `content_not_on_page` as the state the distinction rests on, and `not_on_page` versus `one_sided` as two different facts.** | `content_not_on_page`; `not_on_page`; `one_sided`; `oneSidedMember` | dashboard/src/data/reviewFamily.ts:290-304; dashboard/src/data/reviewFamily.ts:324-347; dashboard/src/data/reviewFamily.ts:89-99 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |


## Update History
- 2026-09-30T10:52:00+02:00 — 260928-MIK-L31 curator (follow-up after the L31 worker's comment-only edits, staged; the change set is now 46 files over `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`): **resolved Todo:** the header of `ReviewWorkspace.family.test.tsx` was refreshed by the worker (comments only) and now names this body's MIK-L31 re-capture (`mik_l31_recapture`); the Todo is removed. The rows into that test were re-pointed by the exact −1 line shift the shorter header causes.
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update for the MIK-L31 re-capture (MIK-R31 rule 6, the L44-R1-F5 remainder). The card now describes the new bytes (49,355 bytes, sha256 `9e13e39f…`): the `retry-budget-family` after-side continuation at page size 6, the both-sides-listed uncarried row `cb5d5f97…`, `unique_member_revision_total` 4, and the five cases that read it. **Claims re-anchored:** the rows naming the old member and revision identities and the old provenance rows (`63b47629`, `not_recaptured`) are replaced; the continuation-cases row, which was already stale (`560-576`, `578-590`, `482-516` held none of its test titles), is re-measured (`601-617`, `619-631`, `505-549`, the last on an `it(` quote); this pass's generated bullet for the receipt row was removed.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`dashboard/src/panels/review/ReviewWorkspace.family.test.tsx`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): provenance correction; the fixture bytes are unchanged and still hold their `63b47629` capture. The case header that cited the retired probe script now names that capture and the receipt's `not_recaptured` section, so the provenance row and the Purpose sentence were corrected to say this body was not re-captured and why, and the ranges into the lengthened header and `reviewFamily.ts` were re-measured.

- 2026-09-27T01:27:31+00:00 — Reconciled the source-linked test references after the cursor case rename and line movement. Current loaded-context and mismatched-walk behavior is stated explicitly; capture bytes, recorded provenance and generated history are preserved. No verification hash/date was changed.
- 2026-09-26T21:37:21Z — Reconciled the reference with the current source owner while retaining its scope and history.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the leaf's continued-roster body.** It records the file's exact identity (48,240 bytes; sha256 `792d00c45728e6daf6a1b8a32424ad7b23edfa263e0abbbce7d4f1a3cc3bb04d`) and the state it pins apart from its siblings: a **page of a walk continued from a published cursor**, whose `payload.page.continued_from` is byte-equal to the `continuation` the sibling `truncated` body's after roster page published (both decode to `position 1`) — the cross-body fact that makes "the client sends the cursor the server published" checkable without a browser. It also records that this body carries the **both-sides-listed** membership row whose content fell outside the page (member `68584c1e-4952-4295-a304-c4ce25029a5b`, revision `30000000-0000-4000-8000-5a554b06baf8`), which is the page-scoped sentence pair the two fix-round cases drive. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
