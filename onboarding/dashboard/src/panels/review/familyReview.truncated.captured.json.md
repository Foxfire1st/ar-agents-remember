# dashboard/src/panels/review/familyReview.truncated.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyReview.truncated.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:00+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3` |
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

One **captured route answer body**: the bytes the intent-review route published for one real enclosure,
recorded at `63b47629` by a leaf-local probe that is not part of the repository, and installed as the fixture the
family workspace case stubs `fetch` with. **31,590 bytes; sha256
`91b6a1d6b4a2885389b80355a1dbf7aade71d00693556960d8a9d7bbe0efa9d6`.** It is untracked in this leaf's
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

**What this body pins apart from its six siblings: a bounded roster whose page carried none of the rows
the read measured.** Every side measured **2** recorded membership rows and carried **0** — the owner's
own sentence reads `holds 2 recorded membership(s) and this page carried 0` — so
`unique_member_revision_total` is **0** while `membership_rows_total` stays **8**. The sentence this body
must produce is therefore the **page-scoped** one; "the read measured zero memberships" is false about
this store, and the body's sibling `emptyRoster` is the only one of the seven where it is true. This is
also the cursor partner of the sibling `continued` body: the cursor its after roster page published **is**
the cursor that page continues.

## Code Commentary

### Logic

The current consumer sends the exact cursor published by the selected side. This older continued capture answers the after-side walk; when the control selected the before walk or another primary revision selection, the client rejects that response and retains the coherent display. A capture being a valid server answer for one cursor does not make it a valid answer for every sibling control. Valid complete walks are covered by the separate familyPaging capture and read-cycle cases.

**Every roster page on this body is a position in a walk with nothing carried.** Each side's page block
is `complete: false`, `state: "first_page"`, `page_size=1`, and publishes a `continuation`; the counts
beside it say one item was returned of a walk of 13 (before) and 12 (after) items for the first family,
and 11 / 9 for the second, with 12, 11, 10 and 8 remaining respectively. Each side's members list is
empty while `members_total` is 2 — the read measured two rows per side and this page reached none of
them.

**This body has no payload-level `page` block at all.** The four cursor-bearing siblings carry one; here
the read is the first page of the selection and the per-side roster pages carry their own cursors. A
reader can re-check that by listing the payload's own keys; the card states it so the absence is not
mistaken for a lost field.

**The two families are the same two the `complete` body records, with the same revisions and the same
authored texts.** Family `65a7c216-c8d0-422d-a114-6822fba97f90` records revision
`ad5f45e2-0b95-4370-8a5e-e039b23c68f9` on both sides with `The retry budget is shared by integration and
synchronization.`; family `c23a294f-fb8a-45e4-b930-3dedbdb751bb` moves from revision
`e38f2f7c-ef1c-4044-9c4e-f13b0b566939` to revision `7d5100c2-e038-439b-987a-13758488c098`. What differs
from `complete` is only what the pages carried, which is exactly what makes the pair useful: the
comparison is the same, the roster state is the opposite.

**The cursor is the server's, and this body is what the continued page answers.** The `continuation`
this body's after roster page publishes and the sibling `familyReview.continued.captured.json`'s
`payload.page.continued_from` are the **same bytes** (both decode to `position 1`). The mounted case
reads that cursor out of the rendered control, clicks it, and asserts the request carries the published
value unchanged — so the walk's first step is proved from these two bodies together, and no cursor the
client invents can advance it.

**The client keeps the three "no member row here" facts apart, and this body is the third one.**
`emptyRosterSentence` decides from the owner's own `members_total` and the page's own `complete` flag:
no recorded revision at all states the entry's own detail; a measured zero prints the measured-zero
sentence; rows measured but not carried print `this page carried no member row — <per-side carried of
measured counts>.` plus, when a roster is still open, `The continuation beside each bounded roster
reaches the rows this page did not carry.` The per-side counts come from `carriedOf` in the owner's two
numbers, which is why the case can assert `0 of the 2 recorded membership row(s) it measured` and the
owner's own `records 2 membership row(s) and this page carried 0 of them` on the same screen without the
two disagreeing.

**Five cases drive these bytes.** They walk the roster only from the published cursor (paired with the
continued body), assert the page-scoped sentence and the absence of "measured zero", head a bounded
member context `partial` and count the owner's rows rather than this page's, assert that the tree and
the centre print **one** empty-roster sentence for the same family rather than two that happen to agree,
and keep the reader's workspace state across two page requests through the centre's own control.

### Conventions

- Captured bytes, never hand-edited: the provenance lives in the consuming case file's header, and this
  card adds no second provenance.
- One JSON document, minified to a **single line** with sorted keys. Every reference row below cites the
  whole file (`:1-1`) and names the exact key path and value in the finding, because a line number
  cannot distinguish two facts in a one-line file. Two candidate anchors — the empty `members` array and
  the `recorded_revision_ids` array literal — were **dropped rather than cited**: a bracketed literal
  does not verify under the literal-grep rule, so the emptiness is carried by the owner's own sentence
  and by `members_total` instead.
- The body is opaque data to this client: the case types it `unknown` and narrows it at runtime.
- Numbers on this card are the file's: byte size and digest are the file, counts are the owner's.

### Invariants And Boundaries

- **A page that carried none of N measured rows is not a measured zero.** The two facts share a screen
  and must never share a sentence; only `emptyRoster` may say "the read measured zero".
- **The owner's two numbers are printed above the page-scoped sentence**, so the clause and the count
  cannot disagree — that disagreement is the defect this body and its case exist to prevent.
- **The cursor belongs to the server.** The continuation this page publishes is the continuation the
  walk continues; the client forwards it unchanged.
- **An absent payload-level page is a shape, not a loss.** This is a first read whose per-side rosters
  carry the cursors.
- **A captured body is evidence, not a specification.** The contract it evidences is the read response
  the route publishes and the sentence pair the client composes from the owner's counts.
- **No conclusion is carried anywhere in the body.** The evidence state is `none_recorded`, the
  assessment state is `unassessed`, and the submission block is `unavailable`.
- **Not browser evidence.** These are the bytes a real route published, rendered by the real client in a
  mounted test tree; they are not a live page fed by a running publication.

### Todos

None recorded. Every user-visible sentence this body drives is pinned by a case; no obligation is
attached to this file.

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
| **The envelope: the one review read the surface makes, its surface version, and its state.** | "\"operation\":\"read_knowledge_review\""; "\"surface_version\":\"knowledge-review-surface/1\""; "\"state\":\"review\"" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The enclosure the bytes were recorded over, and the single normalization: the per-run fixture repository uuid is written as a placeholder.** | "\"leaf_id\":\"260921-icr-l1\""; "review-source-endpoints-fixture"; "<repository_id>" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The family context: two families, the owner's eight measured rows, and no distinct carried revision at all — the count that separates this body from every sibling.** | "\"family_context\":{\"detail\":\"this family context is partial"; "\"membership_rows_total\":8"; "\"unique_member_revision_total\":0"; "\"state\":\"partial\"" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The page-scoped fact in the owner's own words: two recorded rows measured, none carried, on a page that is a position in a walk and publishes the cursor that reaches the rest.** | "holds 2 recorded membership(s) and this page carried 0"; "\"members_total\":2"; "\"page\":{\"complete\":false,\"continuation\""; "\"state\":\"first_page\""; "\"page_size=1" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The walk arithmetic behind the sentence: one item returned per side, with twelve and eleven remaining of thirteen and twelve items, and the same for the second family.** | "\"primary_items_remaining\":12"; "\"primary_items_remaining\":11" | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| **The same two families, revisions and authored texts the `complete` body records — so the only difference between the pair is what the pages carried.** | "65a7c216-c8d0-422d-a114-6822fba97f90"; "c23a294f-fb8a-45e4-b930-3dedbdb751bb"; "e38f2f7c-ef1c-4044-9c4e-f13b0b566939"; "7d5100c2-e038-439b-987a-13758488c098"; "The retry budget is shared by integration and synchronization." | dashboard/src/panels/review/familyReview.truncated.captured.json:1-1 |
| The one constant that binds this body to its cases, and the runtime narrowing that keeps a body with a missing field from mounting the surface. | `captured("familyReview.truncated.captured.json")`; `firstFamilyId` | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:75-78; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:84-107|
| **The provenance of this body after the locator re-capture: it still holds its capture at `63b47629`, when a roster page listed only membership rows, and it was not re-captured — the current route cannot reproduce it, because since a5bec6c3 a roster page also resolves the members its content and claim items represent. Its member sources therefore predate the structured `locator`, `resolved_ranges` and `locator_state` fields.** | "63b47629"; "not_recaptured" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:14-19 |
| **The receipt's worker-stated `not_recaptured` entry for this file, with the evidence it cites.** | "familyReview.truncated.captured.json" | dashboard/src/panels/review/familyReview.capture-provenance.json:36-52 |
| **The statement that bounds what this evidence is: a mounted tree over real server bytes, never a live page.** | "These are not browser evidence"; "Dagger-only" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:33-37 |
| The bounded-roster case states owner totals while refusing to call the current empty page a measured zero. | "says a bounded roster carried none of the measured rows, never that the read measured zero" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:448-469 |
| The bounded capture keeps the exact continuation, owner-measured counts and reader state; a returned foreign walk is rejected. | "sends the family's published cursor and refuses a response from another walk"; "heads a bounded member context partial and counts the owner's rows, not this page's"; "keeps the reader's workspace state across two page requests through the centre's own control" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:296-339; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:482-516; dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:647-700 |
| The case that asserts one empty-roster sentence is printed in both columns, so the tree and the centre cannot drift into two sentences that happen to agree. | "prints one empty-roster sentence in both columns, not two that happen to agree" | dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:592-616 |
| Empty-roster wording and carried counts remain owned by the same page-aware tree helpers. | `emptyRosterSentence`; `carriedOf` | dashboard/src/panels/review/FamilyTree.tsx:222-236; dashboard/src/panels/review/FamilyTree.tsx:218-220 |
| Partial member context retains owner counts and continuation; completing a page is not the same as carrying the whole selection. | `FamilyMemberContext`; `completionNote` | dashboard/src/panels/review/FamilyReviewCenter.tsx:533-594; dashboard/src/panels/review/FamilyTree.tsx:211-216 |

## Cross-Repo References

No cross-repository behavior is exercised in this file: it is one recorded response body from this
repository's own route over this repository's own fixture enclosure.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |


## Update History

- 2026-09-28T16:55:00+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): provenance correction; the fixture bytes are unchanged and still hold their `63b47629` capture. The case header that cited the retired probe script now names that capture and the receipt's `not_recaptured` section, so the provenance row and the Purpose sentence were corrected to say this body was not re-captured and why, and the ranges into the lengthened header and `reviewFamily.ts` were re-measured.

- 2026-09-27T01:27:31+00:00 — Reconciled the source-linked test references after the cursor case rename and line movement. Current loaded-context and mismatched-walk behavior is stated explicitly; capture bytes, recorded provenance and generated history are preserved. No verification hash/date was changed.
- 2026-09-26T21:12:36+00:00: Generated citation repair: "prints one empty-roster sentence in both columns, not two that happen to agree" repointed to dashboard/src/panels/review/ReviewWorkspace.family.test.tsx:583-607. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T03:00:00+02:00 — 260921-ICR-L36 curator, **citation repair only, re-checked at the post-fix tip:** `missingRowNote` sits above the A4 section, so this card's range `:256-263` is unchanged by the F1 fix round; it is re-confirmed here rather than left implicit. No verification stamp was advanced.
- 2026-09-26T02:35:00+02:00 — 260921-ICR-L36 curator (memory worktree only; no code changed by this card's own pass; the code worktree is uncommitted at base `09329a7ee598920c519b06305b73ba8e48d72c88`): **citation repair only — the row naming the centre's bounded-missing-row sentence was re-anchored, and no claim wording changed.** `missingRowNote` moved `:255-262` → `:256-263` with L36's one-line import addition; the anchor still resolves inside the new range and the sentence's two branches are unaltered. **This body also feeds the case this leaf added** (`ReviewWorkspace.family.test.tsx`: the A4 collection case mounts `WALK_FINAL`, not this body), so nothing about this capture's own case changed. No verification stamp was advanced: the candidate is uncommitted, so the governed closeout owns the real stamp.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (candidate `ar/260921-icr-l24`, uncommitted; base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe`): **created this one-to-one card for the leaf's bounded-roster body.** It records the file's exact identity (31,590 bytes; sha256 `91b6a1d6b4a2885389b80355a1dbf7aade71d00693556960d8a9d7bbe0efa9d6`) and the state it pins apart from its six siblings: **every side measured two recorded membership rows and carried none**, so `unique_member_revision_total` is 0 while `membership_rows_total` is 8 and only the page-scoped sentence is true — with the cursor this body publishes being the very cursor the sibling `continued` body continues (byte-equal, both decoding to `position 1`). It also records the two anchors this card **dropped rather than cited** (the empty `members` array and the `recorded_revision_ids` array literal) because a bracketed literal does not verify under the literal-grep rule. **Stamp accounting:** no verification stamp was advanced beyond the leaf base commit — the candidate is uncommitted, and governed closeout owns the real stamp.
