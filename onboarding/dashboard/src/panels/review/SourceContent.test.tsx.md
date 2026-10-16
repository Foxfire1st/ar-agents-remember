# dashboard/src/panels/review/SourceContent.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

The renderer half of source inspection after R86: twelve retained subjects split between the real
`ChangeSetViewer`/change-set client and the real card Full file `SourceContent`/source-content client,
with only `fetch` stubbed. Six primary viewer cases and six primary metadata cases protect changed-path
inspection and retained full-file facts; selected mixed cases exercise both owners. They guard content
shown for a side that has none, a diff
claimed from a pairing that is not two documents, bytes drawn from a generation the reader did not ask
for, a bounded read presented as a whole file, a refusal rendered as a degraded success, and a row
offering to open something this vocabulary cannot address.

No expansion or client is mocked: shipped CodeMirror panes render in jsdom, and assertions inspect DOM
and actual client requests. Fetch replies are declared synthetic inputs, not captured server answers or
Git-object admission. `FileDiff` has no structured object-state/currentness/truncation/path-bound fields;
those facts are checked on retained card `SourceContent`, not invented on the replacement viewer.

## Code Commentary

### Logic

**Two actual owners, separate fetch-only adapters.** `reviewed` mounts `ChangeSetViewer` at a numbered
comparison with an All filter and held inventory. Its stub answers `/api/changeset/task` and
`/api/changeset/file-diff`, adapting declared side text into `FileDiff` or a typed refusal. `fullFile`
mounts the actual card `SourceContent` and admits only `/api/review/intent/source-content` replies.
Both return the real fetch-call log; unexpected routes or unstubbed paths throw rather than pass silently.

**The builders are the wire shape, not a convenience layer.** `present`, `absent`, `binary`, `symlink`
and `submodule` each construct one `ReviewSourceSide` with the detail text the server composes for that
state; `expansion` fills a whole `ReviewSourceExpansion` (since 260921-ICR-L43 including the required `admission: "changed"` and its detail, so every case here is a changed-path read); `content`/`refused` wrap those in the two
`ReviewSourceContentResult` states; and `inventory` builds the declared inventory whose
`listed_total` is the entries' own length. `entry(path, over)` is the one changed-file factory, so a
case's subject is stated where it differs.

**The twelve cases, and what each one would catch.**

1. **Added text and known absence.** The viewer draws empty-before/exact whitespace-dense candidate
   text in its two editors. Retained SourceContent separately preserves absent/present side states
   and the explicit no-diff-claimed fact in the same case.
2. **A modified file as the two-sided diff of its two bound texts.** Both bodies are asserted inside
   the shipped viewer `diff-pane` DOM. Its caption uses shortened tree IDs; the full endpoint IDs
   remain independently asserted in the retained source-content requests of case 9.
3. **A binary side's identity and size with no content.** The state line carries `binary`, the object
   id and `4096 byte(s)`; `diff-pane` and `review-source-after-content` are both absent. It fails if a
   binary operand is ever rendered as text or as an empty document.
4. **A symlink's target as content with no claimed edit.** The state is `symlink`, the recorded target
   is *in* the content block (a link target is text a reader can be shown), and no `diff-pane` exists —
   so renderable content and a claimed document edit stay two different facts.
5. **A submodule pointer by its recorded commit and nothing drawn.** The state line carries the
   `submodule` token and the recorded commit, and neither content nor diff is rendered.
6. **A superseded generation still showing the listed generation's text.** `data-currentness` on
   `review-source-expansion` is `superseded`, the visible superseded paragraph names why the candidate tree
   moved, and the **listed** text is still asserted in the DOM: the newer generation is named, never
   substituted.
7. **A bounded expansion stated as a prefix.** `review-source-truncated` says "bounded expansion",
   `data-side-truncated` is `true`, and the state line still carries the object's real size
   (`2099134 byte(s)`) beside the shorter text.
8. **Typed refusal, not degraded success.** The viewer renders its not-found/404 reason and no diff;
   retained SourceContent then renders source_content_unresolved, reason, next action and no content.
9. **Published binding at both actual request paths.** The viewer asks the numbered comparison and
   path/kind/task context, with no current-mode or review-route substitution. Retained SourceContent
   separately asks the exact full beforeCodeTreeId/afterCodeTreeId and path/task context.
10. **`path_bound=leaf_change_set` is stated.** When the requested generation could not be measured,
    `review-source-path-bound` names that the admission came from the leaf's own published change set
    (`13 changed path(s)`), the readable side is still drawn `present`, and the unreadable side is
    `unavailable` rather than blank.
11. **Byte-form paths are not openable.** The viewer preserves exact byte spelling and cannot-open
    reason, no byte-row button and no byte-path file request; the ordinary text row remains openable.
    The old byte-row data-status hook has no replacement DOM field and is explicitly retired.
12. **Unavailable trees are not measured-empty.** The viewer renders a typed list refusal/reason,
    no ordinary file row and no file-diff request, rather than fabricating an empty measured inventory.

**The helpers encode the two measurement problems this module has.** `dense(text)` strips whitespace
before comparing, because a CodeMirror editor renders its own gutter and line elements and the
assertion is about the text rather than the editor's layout. `open(view, path)` finds the path label's
closest button and clicks it, throwing when no openable entry exists — so a case
that forgot to make its row expandable fails loudly instead of asserting against nothing.
`afterEach` runs cleanup, resets `dashboardStore`, unstubs globals and clears localStorage so cached conditional reads, stubs and view preferences do not outlive a case.

### Conventions

The module is one `describe` (`source inspection through the change-set page and retained card full files`) over twelve `it` cases, each
naming the rendering fact it protects rather than the function it calls. Fixtures are module-level
`const`s in `SCREAMING_CASE` (`REPO`, `MASTER`, `LEAF`, `BEFORE_TREE`, `AFTER_TREE`, `ADDED_TEXT`,
`MODIFIED_BEFORE`, `MODIFIED_AFTER`, `SYMLINK_TARGET`, `SUBMODULE_COMMIT`) with lowercase factory
functions, matching the route's other behaviour test modules. It imports `render`/`fireEvent`/`waitFor`
from `@testing-library/react` and `vi` from `vitest`, and it imports the real `ChangeSetViewer`, `SourceContent` and the
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
  the content host are `null`, and the byte-form case asserts no byte-row button or byte-path request; the
  negative assertion is where the boundary actually lives.
- **The generation is measured at the request.** The exact query parameters are decoded from the fetch
  mock, so "the read is the generation the listing published" is a fact about the wire, not about a
  rendered string.
- **A missing fixture fails loudly.** The transport throws for an unstubbed path and `open` throws for a
  row with no control, so a drifted case cannot degrade into a vacuous pass.
- **Boundary.** This module owns the renderer half's expectations only; the values it feeds are the
  shape the server's route returns, and the server half is asserted against real Git objects by
  `mcp/tests/test_knowledge_review_source_content.py`. The viewer uses the real store-owned change-set read caches, which cleanup resets between cases; no server route or cockpit dispatch is exercised.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The source defines the retained subjects, actual renderer/client adapters, DOM/request assertions and
explicit representation limits. It is mounted synthetic evidence, not browser geometry or server admission.

- Twelve retained subjects use actual comparison viewer and card SourceContent owners with fetch-only synthetic replies; metadata is not invented in FileDiff. [1]
- Real ChangeSetViewer, SourceContent and their wire types are imported rather than replaced by a compatibility renderer. [2]
- The task context and the two generation ids every case reads at. [3]
- **The exact texts a real read carries** — an added file's whole body, a modified file's two bodies, a symlink's recorded target, a submodule's commit. [4]
- The whitespace-dense comparison that asserts the text rather than the CodeMirror editor's line layout. [5]
- **The five side builders, one per declared state a case exercises, each carrying the detail the server composes for it.** [6]
- The changed-file and payload builders, with `listed_total` the entries' own length. [7]
- **The expansion and result builders, and the typed refusal carrying a code, a detail, a next action and an offending input.** [8]
- reviewed adapts declared replies to comparison task/file-diff endpoints and returns the actual fetch log; unexpected routes/paths throw. [9]
- fullFile mounts retained SourceContent with exact tree inputs and its source-content route stub, returning the actual request log. [10]
- open finds the path label's closest button and throws when no openable entry exists. [11]
- The per-case cleanup: the rendered tree and every stubbed global. [12]
- Added text is checked in the viewer editors; retained SourceContent separately keeps absent/present and no-diff facts. [13]
- The viewer modification shows both bound texts and short tree captions; full tree-ID requests are preserved separately. [14]
- **The non-text cases: a binary side's identity and size with no content, a symlink's target as content with no claimed edit, and a submodule pointer by its recorded commit with nothing drawn.** [15]
- **The superseded generation keeps the listed bytes on screen while naming the newer one, and a bounded expansion is stated as a prefix beside the object's real size.** [16]
- **The typed refusal rendered with its code, detail and next action and with no content, and the request carrying the listing's own generation, path and task context.** [17]
- **The leaf-change-set bound stated when the requested generation could not be measured, with the readable side still drawn and the unreadable one named.** [18]
- Byte spelling/reason/nonopening and ordinary-only requests survive; unavailable trees produce typed list refusal and no file request, not measured-empty. [19]

- Comparison changed paths open through the existing viewer; retained cards use SourceContent for structured full-file metadata. [24]
- Comparison changed paths open through the existing viewer; retained cards use SourceContent for structured full-file metadata. [25]

- The renderer under test, and the rules its cases are the evidence for. [21]
- The client the real surface reads through, which parses the typed body whatever the HTTP status. [22]
- **The server half of the same contract: the values these cases feed are the shape the production route returns, asserted against real Git objects there.** [23]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The cases measure one repository namespace's
renderer against one repository's two bound code trees and carry no identity that ranges beyond it.

No meaningful cross-repo references found.
