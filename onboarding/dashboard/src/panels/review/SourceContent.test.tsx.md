# dashboard/src/panels/review/SourceContent.test.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/SourceContent.test.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T12:38:10+02:00 |
| lastVerifiedCommitHash | `e66f1f3894116e0bb37b49f178d8bfcb130a7e28` |
| lastVerifiedCommitDate | 2026-09-28T20:02:47+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The renderer half of ICR-R03, measured at the real surface: twelve cases that open a listed inventory
entry on the **real** `ReviewSurface` through the **real** `reviewSourceContent` client, with only
`fetch` stubbed. What they protect is one user operation — *click a changed path and see what actually
changed* — and the consequential failures around it: content shown for a side that has none, a diff
claimed from a pairing that is not two documents, bytes drawn from a generation the reader did not ask
for, a bounded read presented as a whole file, a refusal rendered as a degraded success, and a row
offering to open something this vocabulary cannot address.

The module's header states the three properties that make the cases evidence rather than assertions:
nothing here renders a stand-in for the expansion, no assertion reads a prop the test itself passed
(the shipped `DiffPane` and `FilePane` CodeMirror primitives render in jsdom, so the text is read out
of the DOM), and the generation case asserts the exact request the surface made. It also names the
module's own defect baseline — the Source pane printed a path and a command and had no source-content
interaction at all — and records that the side values below are the shape the production route returns,
asserted against real Git objects by `mcp/tests/test_knowledge_review_source_content.py`, so a change to
either half's contract fails in one of the two modules.

## Code Commentary

### Logic

**One stub, two routes, and the expansion answer is selected by the path asked about.** `serve` installs
a `vi.fn` on `globalThis.fetch`: a URL containing `/api/review/intent/source-content` is answered from
the case's own `expansions` map keyed by the `path` query parameter (and an unstubbed path throws, so a
case cannot silently pass on a missing answer), while anything else is answered with the review payload.
`reviewed(...)` builds the review result, renders `ReviewSurface` with the task context, and returns
both the view and the fetch mock — which is what lets one case assert the request rather than only the
DOM.

**The builders are the wire shape, not a convenience layer.** `present`, `absent`, `binary`, `symlink`
and `submodule` each construct one `ReviewSourceSide` with the detail text the server composes for that
state; `expansion` fills a whole `ReviewSourceExpansion` (since 260921-ICR-L43 including the required `admission: "changed"` and its detail, so every case here is a changed-path read); `content`/`refused` wrap those in the two
`ReviewSourceContentResult` states; and `payload` builds the full review payload whose inventory's
`listed_total` is the entries' own length. `entry(path, over)` is the one changed-file factory, so a
case's subject is stated where it differs.

**The twelve cases, and what each one would catch.**

1. **An added file's whole candidate text beside the named absent side.** The before state line is
   `absent` with its detail, the after state line is `present`, the file's own bytes are read back out
   of `review-source-after-content` (whitespace-dense, because CodeMirror reshapes layout), and
   `review-source-no-diff-claimed` is present. An "expansion" that printed a path or a command instead
   of the bytes fails here.
2. **A modified file as the two-sided diff of its two bound texts.** Both bodies are asserted inside
   the shipped `diff-pane` DOM, and `review-source-generation` names the exact `before → after` pair.
   This is the case that keeps the reused diff engine wired to the expansion.
3. **A binary side's identity and size with no content.** The state line carries `binary`, the object
   id and `4096 byte(s)`; `diff-pane` and `review-source-after-content` are both absent. It fails if a
   binary operand is ever rendered as text or as an empty document.
4. **A symlink's target as content with no claimed edit.** The state is `symlink`, the recorded target
   is *in* the content block (a link target is text a reader can be shown), and no `diff-pane` exists —
   so renderable content and a claimed document edit stay two different facts.
5. **A submodule pointer by its recorded commit and nothing drawn.** The state line carries the
   `submodule` token and the recorded commit, and neither content nor diff is rendered.
6. **A superseded generation still showing the listed generation's text.** `data-currentness` on
   `review-source-expansion` is `superseded`, `review-source-currentness` names why the candidate tree
   moved, and the **listed** text is still asserted in the DOM: the newer generation is named, never
   substituted.
7. **A bounded expansion stated as a prefix.** `review-source-truncated` says "bounded expansion",
   `data-side-truncated` is `true`, and the state line still carries the object's real size
   (`2099134 byte(s)`) beside the shorter text.
8. **A typed refusal rendered as its refusal and no content.** The block carries the code
   (`source_content_unresolved`), the server's own detail, and a next action; no `diff-pane` and no
   content block exist. A refusal drawn as a blank pane or as an error string fails here.
9. **The request carries the listing's own generation and path.** After the diff settles, the logged
   `source-content` call is decoded and `beforeCodeTreeId`, `afterCodeTreeId`, `path`, `repo`, `master`
   and `leaf` are each asserted — this is the case that makes "the generation is an input" measurable
   rather than a comment.
10. **`path_bound=leaf_change_set` is stated.** When the requested generation could not be measured,
    `review-source-path-bound` names that the admission came from the leaf's own published change set
    (`13 changed path(s)`), the readable side is still drawn `present`, and the unreadable side is
    `unavailable` rather than blank.
11. **The byte-form row is drawn without an open control.** `review-inventory-byte-path` carries the
    exact byte form and its status, `review-byte-path-not-addressable` states that the row cannot be
    opened, and `getAllByTestId("review-inventory-open")` is asserted to have length **1** — exactly
    the text entry. The negative assertion is the point: it is what forbids a control that would
    promise content this vocabulary cannot address.
12. **No expansion is offered when the inventory named no code trees.** With an `unavailable` inventory
    carrying neither tree id, zero open controls are rendered.

**The helpers encode the two measurement problems this module has.** `dense(text)` strips whitespace
before comparing, because a CodeMirror editor renders its own gutter and line elements and the
assertion is about the text rather than the editor's layout. `open(view, path)` finds the button whose
`dataset.path` is the case's path and clicks it, throwing when no openable entry exists — so a case
that forgot to make its row expandable fails loudly instead of asserting against nothing.
`afterEach` runs `cleanup()` and `vi.unstubAllGlobals()`, so no stub outlives its case.

### Conventions

The module is one `describe` (`the source pane opening a listed entry`) over twelve `it` cases, each
naming the rendering fact it protects rather than the function it calls. Fixtures are module-level
`const`s in `SCREAMING_CASE` (`REPO`, `MASTER`, `LEAF`, `BEFORE_TREE`, `AFTER_TREE`, `ADDED_TEXT`,
`MODIFIED_BEFORE`, `MODIFIED_AFTER`, `SYMLINK_TARGET`, `SUBMODULE_COMMIT`) with lowercase factory
functions, matching the route's other behaviour test modules. It imports `render`/`fireEvent`/`waitFor`
from `@testing-library/react` and `vi` from `vitest`, and it imports the real `ReviewSurface` and the
real types from `../../data/review` — never a mocked client and never a pane stand-in. Asynchronous
content is awaited through `waitFor`/`findBy*` rather than asserted synchronously, and the one
synchronous read (the request log) is taken only after the expansion has settled, so the assertion is
about the request the surface made and not about a state update that outlives the case.

### Invariants And Boundaries

- **The real component and the real client, with only the transport stubbed.** No case renders a
  substitute pane or a mocked `reviewSourceContent`; a change to the surface, the client or either
  shipped renderer reaches these cases.
- **Assertions read the DOM, not props.** Every rendered fact is read back through a `data-testid` or a
  `data-*` attribute the component itself sets, so a case cannot be satisfied by the value it passed in.
- **Absence is asserted, not assumed.** A state that must draw no content asserts both `diff-pane` and
  the content host are `null`, and the byte-form case asserts the *count* of open controls; the
  negative assertion is where the boundary actually lives.
- **The generation is measured at the request.** The exact query parameters are decoded from the fetch
  mock, so "the read is the generation the listing published" is a fact about the wire, not about a
  rendered string.
- **A missing fixture fails loudly.** The transport throws for an unstubbed path and `open` throws for a
  row with no control, so a drifted case cannot degrade into a vacuous pass.
- **Boundary.** This module owns the renderer half's expectations only; the values it feeds are the
  shape the server's route returns, and the server half is asserted against real Git objects by
  `mcp/tests/test_knowledge_review_source_content.py`. It exercises no store, no route and no cockpit
  dispatch.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header, its fixtures
and its twelve cases, the real surface and client it drives, the wire types it builds from, and the
server half of the same contract that supplies the values.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own statement of what is real and what is stubbed, where the values come from, the defect baseline, and the rule that no assertion reads a prop the test itself passed.** | "R03 (actual source-content inspection) at the real renderer: the Intent Reviewer surface opening a"; "the source pane opening a listed entry" | dashboard/src/panels/review/SourceContent.test.tsx:1-19; dashboard/src/panels/review/SourceContent.test.tsx:270-591 |
| The real surface and the wire types under test, imported rather than mocked. | `ReviewSurface`; `ReviewSourceContentResult`; `ReviewSourceExpansion`; `ReviewSourceSide` | dashboard/src/panels/review/SourceContent.test.tsx:21-33 |
| The task context and the two generation ids every case reads at. | `BEFORE_TREE`; `AFTER_TREE` | dashboard/src/panels/review/SourceContent.test.tsx:39-40 |
| **The exact texts a real read carries** — an added file's whole body, a modified file's two bodies, a symlink's recorded target, a submodule's commit. | `ADDED_TEXT`; `MODIFIED_BEFORE`; `MODIFIED_AFTER`; `SYMLINK_TARGET`; `SUBMODULE_COMMIT` | dashboard/src/panels/review/SourceContent.test.tsx:44-48 |
| The whitespace-dense comparison that asserts the text rather than the CodeMirror editor's line layout. | `dense` | dashboard/src/panels/review/SourceContent.test.tsx:53-53 |
| **The five side builders, one per declared state a case exercises, each carrying the detail the server composes for it.** | `present`; `absent`; `binary`; `symlink`; `submodule` | dashboard/src/panels/review/SourceContent.test.tsx:55-64; dashboard/src/panels/review/SourceContent.test.tsx:66-70; dashboard/src/panels/review/SourceContent.test.tsx:72-78; dashboard/src/panels/review/SourceContent.test.tsx:80-87; dashboard/src/panels/review/SourceContent.test.tsx:89-94 |
| The changed-file and payload builders, with `listed_total` the entries' own length. | `entry`; `payload` | dashboard/src/panels/review/SourceContent.test.tsx:96-98; dashboard/src/panels/review/SourceContent.test.tsx:100-173 |
| **The expansion and result builders, and the typed refusal carrying a code, a detail, a next action and an offending input.** | `expansion`; `content`; `refused` | dashboard/src/panels/review/SourceContent.test.tsx:175-196; dashboard/src/panels/review/SourceContent.test.tsx:198-203; dashboard/src/panels/review/SourceContent.test.tsx:205-215 |
| **The transport stub: the expansion answer selected by the asked-about path, an unstubbed path throwing, and the fetch mock returned so a case can assert the request.** | `serve` | dashboard/src/panels/review/SourceContent.test.tsx:220-237 |
| The harness that renders the real surface at the task context and hands back the request log. | `reviewed` | dashboard/src/panels/review/SourceContent.test.tsx:239-255 |
| The click helper that finds the row by its published path and throws when the row is not openable. | `open` | dashboard/src/panels/review/SourceContent.test.tsx:257-263 |
| The per-case cleanup: the rendered tree and every stubbed global. | `afterEach`; `cleanup`; `vi.unstubAllGlobals` | dashboard/src/panels/review/SourceContent.test.tsx:265-268 |
| **The addition case: the absent-before and present-after state lines, the file's own bytes read out of the content host, and the explicit no-diff-claimed line.** | "draws an added file's entire candidate text beside the named absent side" | dashboard/src/panels/review/SourceContent.test.tsx:271-293 |
| **The two-sided modification case: both bodies asserted inside the shipped `diff-pane` DOM, and the generation line naming the exact pair.** | "draws a modified file as the two-sided diff of its two bound texts" | dashboard/src/panels/review/SourceContent.test.tsx:295-318 |
| **The non-text cases: a binary side's identity and size with no content, a symlink's target as content with no claimed edit, and a submodule pointer by its recorded commit with nothing drawn.** | "states a binary side's identity and size and draws no content for it"; "carries a symlink's target as content and never claims a document edit"; "reports a submodule pointer by its recorded commit and draws nothing for it" | dashboard/src/panels/review/SourceContent.test.tsx:320-341; dashboard/src/panels/review/SourceContent.test.tsx:343-366; dashboard/src/panels/review/SourceContent.test.tsx:368-387 |
| **The superseded generation keeps the listed bytes on screen while naming the newer one, and a bounded expansion is stated as a prefix beside the object's real size.** | "labels a superseded generation while still showing the listed generation's text"; "states a bounded expansion as a prefix of the object" | dashboard/src/panels/review/SourceContent.test.tsx:389-411; dashboard/src/panels/review/SourceContent.test.tsx:413-439 |
| **The typed refusal rendered with its code, detail and next action and with no content, and the request carrying the listing's own generation, path and task context.** | "renders a refused entry read as its typed refusal and no content"; "sends the generation and path the listing published, not a re-resolved one" | dashboard/src/panels/review/SourceContent.test.tsx:441-459; dashboard/src/panels/review/SourceContent.test.tsx:461-490 |
| **The leaf-change-set bound stated when the requested generation could not be measured, with the readable side still drawn and the unreadable one named.** | "states which measured change set admitted the path when the requested one could not be measured" | dashboard/src/panels/review/SourceContent.test.tsx:492-522 |
| **The two boundaries: the byte-form row listed without an open control (the open-control count asserted to be exactly the text entry), and an inventory that named no code trees offering no expansion at all.** | "lists a byte-form row without implying it can be opened"; "offers no expansion for an inventory that named no code trees" | dashboard/src/panels/review/SourceContent.test.tsx:524-562; dashboard/src/panels/review/SourceContent.test.tsx:564-590 |
| The surface the cases render: the openable row that mounts the renderer, and the inventory that owns the open row and passes the published generation down. | `review-inventory-open`; `SourceExplorer`; `SourceContent` | dashboard/src/panels/review/SourceExplorer.tsx:103-103; dashboard/src/panels/review/SourceExplorer.tsx:224-302; dashboard/src/panels/review/ReviewSurface.tsx:293-337; dashboard/src/panels/review/ReviewSurface.tsx:10-10; dashboard/src/panels/review/ReviewSurface.tsx:51-51; dashboard/src/panels/review/ReviewSurface.tsx:279-279 |
| The renderer under test, and the rules its cases are the evidence for. | `SourceContent`; `Sides`; `boundedNote`; `refusalBlock` | dashboard/src/panels/review/SourceContent.tsx:112-124; dashboard/src/panels/review/SourceContent.tsx:167-227; dashboard/src/panels/review/SourceContent.tsx:54-98; dashboard/src/panels/review/SourceContent.tsx:100-110 |
| The client the real surface reads through, which parses the typed body whatever the HTTP status. | `reviewSourceContent` | dashboard/src/data/review.ts:727-745 |
| **The server half of the same contract: the values these cases feed are the shape the production route returns, asserted against real Git objects there.** | "One inventory entry opened into the two bound endpoints' actual content (ICR-R03)." | mcp/tests/test_knowledge_review_source_content.py:1-3 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The cases measure one repository namespace's
renderer against one repository's two bound code trees and carry no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`dashboard/src/panels/review/ReviewSurface.tsx`, `dashboard/src/panels/review/SourceExplorer.tsx`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.
- 2026-09-28T17:15:39+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): No content impact: citation ranges into files this leaf changed (`dashboard/src/panels/review/ReviewSurface.tsx`) were re-pointed to where the same anchors now sit; each re-pointed row held its anchors at the base and holds them after the base-to-candidate line mapping. Claim wording unchanged. No stamp advanced.
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): **fixture-only type follow-through.** The `expansion` builder gained the two now-required fields `admission: "changed"` and `admission_detail`; no case, assertion or rendered behavior changed, and no case exercises attributed unchanged context (the pane's labelling of it is L49's). The Logic sentence names the fields; thirteen rows below the builder were re-pointed +2 lines, each verified against the candidate. No stamp advanced; closeout owns it.
- 2026-09-26T21:11:13+00:00: Generated citation repair: `reviewSourceContent` repointed to dashboard/src/data/review.ts:727-745. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-24T00:43:00+02:00 — 260921-ICR-L24 curator (memory worktree only; no code changed; no commits; leaf base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta): **two enforced citation rows re-cited to the constructs they name, wording unchanged.** This leaf moved the complete source change explorer out of `ReviewSurface.tsx` into its own module, so the inventory the cases drive is now `SourceExplorer` (`SourceExplorer.tsx:234-315`) and the anchor naming it was corrected to the construct the range actually holds; the renderer row's `boundedNote` and `refusalBlock` ranges follow the renderer's own growth (`SourceContent.tsx:131-142`, `:143-155`), because `Sides` gained the `mode`/`collapse` props. Every contributing range the rows already carried (`SourceContent` `76-112`/`164-222`, the `ReviewSurface.tsx` `291-335`/`8-8`/`49-49`/`277-277` set) is kept verbatim and no claim was reworded or dropped. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted (base `5f14fc6790cafc3ad2ae612c2e67f176392dc1fe` plus the working-tree delta) and governed closeout owns the real stamp.
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.

- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **created.** The module is new in this leaf and this is its one-to-one card. It records the testing *contract* rather than the case list: the real `ReviewSurface` and the real client with only `fetch` stubbed; assertions read the rendered DOM (and, for the generation, the actual request the surface made) rather than a prop the test passed; the stub throws for an unstubbed path and the click helper throws for a row with no control, so a drifted case cannot pass vacuously; and the negative assertions — no `diff-pane` for a refused or non-two-document read, and an open-control count of exactly one for the byte-form case — are where the boundary actually lives. It also records the two measurement problems the module solves (`dense` for CodeMirror's reshaped whitespace and the settle-before-reading-the-request-log ordering) and the server module that supplies and independently asserts the same values. Every row was re-verified against this candidate with `sed -n 'START,ENDp'` before it was written, and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** the verification pair names the master line `d80a0513e928ef29a973527d09597c82c96fde87` (2026-09-21T19:51:20+02:00) — the last real commit the reading was taken against — because the module exists only in this leaf's **uncommitted** candidate and no commit contains the bytes a stamp would claim to have verified. The recorded working candidate states what was actually read; closeout owns the stamp.
