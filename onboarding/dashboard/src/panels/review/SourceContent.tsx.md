# dashboard/src/panels/review/SourceContent.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Render one file's structured source-content answer at the two code trees supplied by its caller. This is the retained expression-card Full file renderer, not the comparison change-set page and not a surviving dataset `ReviewExpressions` mount. The server owns endpoint resolution, admissible paths, side states, bytes and currentness; this module renders the returned facts and does not resolve a replacement tree or conclude a review.

## Code Commentary

### Side rendering and provenance

`sideLine` always shows each supplied state and records state/truncation attributes. Optional object identity and byte length sit in Object identity details; the side detail remains open when state is not `present` or the side is truncated. It does not infer a missing object's identity.

`Sides` first checks whether both states are `present`: only that branch draws `DiffPane`, with each supplied text or the literal empty-string fallback, language, caller layout/collapse and full-file marks. This is a rendering conditional, not independent validation that a supplied present-state object contains complete text. Otherwise `textual` tests `text !== undefined`: neither textual side yields state lines alone; any textual side yields the explicit no-diff-claimed line and its own `FilePane`. The other side is not manufactured as an empty operand. Thus branch selection uses both declared state and actual text presence, not exclusively the state label.

`Expansion` discloses normal currentness, generation/status/mode-change and reproduction command only for `current`. A non-current answer instead keeps its supplied reason open. Leaf-change-set admission is outside that branch and remains visible whenever that bound is supplied. `boundedNote` names truncated sides as prefixes; it does not turn a prefix into a complete file or independently enforce the server's byte limit. The reproduction command is in the current-only provenance disclosure, not promised visible for every non-current answer.

### Full-file marks and their independent list

Relative to actual BASE, this file adds the `useFullFileMarks` integration and responsive pane/list layout. `useSourceMarking` still owns the marker note/panel and supplied pane marks; `useFullFileMarks` receives those marks and can add a reveal request plus a separate list. The two-present branch places that list beside the diff; the textual one-sided branch passes side-filtered full-file marks into each pane and draws the list below them. The no-text branch returns the state lines even though the hooks were invoked before the branch.

The helper owns list eligibility: active marker scope, ready classification, matching drawn object identities and a hunk classification. It enumerates classified hunks independently of editor viewport placement. Only IDs present in pane marks are enabled for reveal; missing placement is labelled unavailable, including the helper's stated first-2-MiB wording for truncated content. That wording is not a byte limit enforced in this renderer. The helper binds the requested reveal to the expansion path, forwards the pane's existing reveal path and clears its local request after reveal. This module does not recompute hunk ownership or equate an unavailable mark with a complete classification.

### Request identity, cache and outcomes

`SourceContentRequest` and `useSourceContentRead` remain exported. The cache key names repo/master/leaf/path and both supplied code trees. The hook uses a cached result when available, otherwise keeps answer and failure under the exact key they answered. Cleanup makes the asynchronous completion inactive; it suppresses later cache/state updates rather than aborting the underlying request. A result hides a failure, and a failure from another key is not displayed.

`ReviewReadCache.keepSource` keeps only content answers with an expansion, never typed refusals or thrown failures. A cache hit avoids the effect's request. This code does not coalesce concurrent in-flight requests or guarantee one lifetime request per key: eviction, absent providers, key changes and remounts matter. Retry clears failure and advances the effect's attempt; it can issue another read when no cached answer exists, not unconditionally force a network read over a cache hit. Cache generation clearing belongs to its owner, not this component.

The component's ordered outcomes are shared `ReviewProblemBlock` with retry, loading, its own typed-refusal block, expansion, and otherwise null. A typed refusal has code/detail/next action and optional offending input; it is not a content success. Defaults are split layout and no collapse. These display inputs do not themselves change the six-field request identity.

### Current caller and declared regression scope

`ExpressionCards.FullFile` supplies the review inventory's two code-tree IDs, candidate task context, path, layout, inverse-fullFile collapse and pane marker name. Without both tree IDs it renders its own unavailable paragraph. An entry not listed in the inventory is represented as unknown for this bound read, not invented as a measured changed file. The removed dataset expression renderer is historical, not an alternate current caller.

`SourceContent.test.tsx` separates the actual comparison `ChangeSetViewer` helper from its direct retained `SourceContent` helper; the latter stubs this route's transport, not the removed source explorer. Its declarations cover non-text side rendering, prefixes, superseded reasons, typed refusal and bound generation/path behavior. Some cases exercise comparison-page navigation as well; the byte-form and missing-tree inventory cases belong to that comparison helper. Those assertions do not prove this component owns inventory navigation, nor constitute fresh Curator test execution.

## Invariants And Boundaries

- Supplied endpoint facts are rendered, not re-derived; absence is not a known empty text operand.
- A bounded prefix, unavailable classification, typed refusal or transport failure is not a completeness or review-success claim.
- Source identity is generation-keyed; transient mounted display state and server authority are distinct.
- Hunk-list eligibility, placement and reveal are delegated to the marker helpers. This file wires their results into existing panes.
- The two existing typed realization attachments are retained for their actual cache/read and presentation roles; this ordinary-card repair does not invent or retire an invariant.
- This is source inspection and documented assertion scope, not a transferred R7 CODE verdict, current MEMORY grade or fresh execution result.

## Previous Input Account — Historical Only

The complete preceding ordinary account is preserved below. Its claims about a retained dataset expression mount, state-only branch selection, header provenance and unconditional one-request/retry behavior are superseded, not operative promises. Numeric prose labels are inert historical references; code and array indices remain literal. The current evidence follows this quotation.

> # dashboard/src/panels/review/SourceContent.tsx
>
> ## Governing Overview
>
> [dashboard/src/panels route overview](../overview.md)
>
> ## Purpose
>
> The retained card Full file renderer: complete available content at the two
> bound code trees the listing published, plus each side's own declared state and measured object
> identity. R86 changed-path inventory actions use the comparison change-set viewer; this module preserves
> the structured side/currentness/truncation/path-bound facts and intent markers of card full-file reads.
>
> It exists because the pane before it printed a path, a status and a reproducing command and had **no
> source-content interaction at all**: a row labelled as an expansion showed no bytes, so a reader had to
> leave the surface and run the command to learn what actually changed. The module's header states that
> history and rendering rules; the central expression card is its surviving full-file owner.
>
> Since ICR-R16 the pane also renders the **other** answer shape this route can give. Its *typed*
> refusal (`state: "refused"`) is still R03's, rendered by this module's own `refusalBlock` and untouched;
> everything else — an unwired process, a query the route does not admit, a socket that never answered —
> now goes through the shared `ReviewProblemBlock` the review surface uses, carrying the code, reason,
> offending input and next action the thrown message used to drop. See the transport paragraph under
> Logic for the boundary between the two.
>
> Two boundaries decide its shape. It is **display-only** in the same sense the rest of the surface is:
> one read, no control that writes, no conclusion. And it **reuses the shipped renderers rather than
> growing a third view** — `DiffPane` from the change-set route for the two-document case and `FilePane`
> from the file-viewer route for a single readable operand — so a reader sees the same diff engine and the
> same viewer here as everywhere else on the cockpit.
>
> Since ICR-R24@v3 it also takes the reader's two display preferences from its caller. The optional
> `mode` (a `DiffMode`) and `collapse` props are threaded straight into `DiffPane` rather than decided
> here, because the workspace/card owns the diff layout and the full-file disclosure — and because a
> layout switch there must not be able to reset an expansion here. Their defaults (`"split"` and `false`)
> are exactly the shipped rendering: a split diff of the whole file.
>
> Since MIK-R34 it also draws per-hunk intent markers through optional `markers` (`SourceMarkers`):
> the pane name and an optional classification already held by a caller. The current card Full file
> caller supplies its pane name, and `IntentMarkers` obtains the classification through the shared
> scope. Lane/explorer Full file callers are not current integrations. This renderer only threads
> marks into the existing panes; outside a tree comparison's marker scope the view stays unmarked.
>
> ## Code Commentary
>
> ### Logic
>
> Expansion renders the bound source content through the shipped panes. Side states and abnormal/truncated details remain open; only measured object ids and byte lengths sit inside each side's Object identity disclosure. Normal currentness/generation/reproduction provenance has a separate disclosure, while non-current reasons, leaf-change-set admission and truncation notes remain visible. Layout and collapse are caller-supplied.
>
> **Every branch is decided by each side's declared `state`, and never by inspecting its text.** The
> header states the rule and the three cases it produces; `Sides` implements them by asking the two
> questions in a fixed order — are both sides `present`, then is either side textual at all — so the
> `text` of a side that is not text can never be read as an operand. `textual(side)` is the one
> predicate (`side.text !== undefined`) and it is deliberately *not* `state === "present"`: a `symlink`'s
> recorded target is content a reader can be shown, while a `binary` side is not text and an `absent`
> side is a measured fact about that endpoint rather than an empty file.
>
> **Both sides always state their declared state; measured identity is identifiers-only.** `sideLine`
> puts the before/after state in `review-source-<name>-state`, with `data-side-state` and
> `data-side-truncated`. Object id and byte length are optional measured facts inside Object identity;
> no object is invented for an absent endpoint. The long detail is outside that disclosure when
> `side.state !== "present" || side.truncated`, so non-present and bounded-side reasons remain open.
>
> **Both sides `present` → the shipped two-sided diff over their own bytes.** `DiffPane` receives
> `before.text ?? ""`, `after.text ?? ""`, `language={expansion.language}` and caller `mode`/`collapse`
> (defaults `"split"`/`false`). The card Full file and retained dataset expression callers supply
> layout and full-file collapse state; no source explorer controls this renderer. The empty fallback
> applies only to `present` sides whose model supplies text.
>
> **One side `present` (or `symlink`) and the other not textual → the readable operand as content, the
> unavailable side's own reason above it, and an explicit no-diff line.** `review-source-no-diff-claimed`
> says that no addition or a change is claimed "from the two sides beside it", because a diff there would
> assert that the other endpoint is a known-empty document — precisely the claim a `binary`, `submodule`,
> `unavailable` or `absent` side makes unavailable. Each textual side is drawn in `FilePane` inside a
> `review-source-<name>-content` host, and a side that is not textual gets **no content block at all**
> rather than an empty one.
>
> **Neither side textual → the two state lines and nothing else.** No diff, no content block and no
> no-diff note: there is no operand to caveat, so the pane states what each endpoint is and stops.
>
> **The generation is an input, never a lookup.** `SourceContent` takes `beforeCodeTreeId` and
> `afterCodeTreeId` from the caller — the ids the inventory published to this client — and sends them
> with every read; since L48 the read's identity is `sourceContentKey(repo, master, leaf, path,
> beforeCodeTreeId, afterCodeTreeId)` (declared in `ReviewReadCache.ts`), so a different row or a
> different listed generation is a different read and an unrelated re-render is not. A read therefore
> describes the generation the reader was looking at even after the branch moved, which is what makes the
> `currentness` line meaningful.
>
> **`currentness`, `path_bound` and the command are the read's own provenance.** Normal currentness and
> endpoint identities may live in provenance; non-current reasons remain open. The existing
> `review-source-path-bound` paragraph is outside the current-only branch, after stale reason and before
> Sides, so leaf-change-set admission remains visible for superseded content too;
> `review-source-generation` prints `generation <before> → <after> · <status>` plus `mode changed` when
> the recorded status carried one; `review-source-path-bound` is rendered **only** when
> `path_bound === "leaf_change_set"`, because the ordinary `requested_generation` bound is the row's own
> listing and needs no explanation, while the leaf-bound case admits the path by a *different*
> measurement and must say which; and `review-source-command` prints the reproduction the server
> composed, `pre-wrap` because it is two lines of shell.
>
> **A bounded read is a stated prefix, not a shorter file.** `boundedNote` collects whichever sides are
> `truncated` and renders `review-source-truncated` once, naming those sides and saying the text above is
> a stated prefix of the object whose exact identity and size are on its own line. The note is drawn
> after `Sides`, so it annotates the text it qualifies rather than replacing it.
>
> **Refusal is a rendered state, not an exception.** `refusalBlock` prints the typed `code` and `detail`,
> the `next_action`, and the `offending_input` when there is one, under `review-source-refusal`, and it
> shows no content: a refused read is a normal answer from this route (a path outside the measured change
> set), not a degraded success.
>
> **A transport-level failure is a `ReviewFailure` rendered by the shared block, not a thrown message
> (ICR-R16).** The catch keeps `reviewProblemFromCause(cause)` in `problem` — the same classification the
> surface and the entry bar use — and the component renders it through `ReviewProblemBlock` with
> `origin="failure"` and `subject="this entry's content"`, so the server's own code, reason, offending
> input and next action are all shown here too, plus a retry for a socket that never answered. The
> pre-existing rendering printed only `cause.message`, which for a `503` read `503 unavailable` and dropped
> the adapter's instruction. The retry re-arms the effect through an `attempt` counter, so a retried read
> is a real read; R03's typed path is below it and unchanged: this module still renders its own
> `refusalBlock` for a `state: "refused"` answer and never re-specifies that rendering.
>
> **Four outcomes, and the order they are decided in.** The component returns the shared failure block
> when `problem` is set, then the `review-source-loading` line (naming the path and "at the listed
> generation") while `result` is `null`, then `refusalBlock` when the typed answer is `refused`, then
> `Expansion` — carrying the two display preferences down to `Sides` — when the answer carries one, and
> `null` otherwise.
>
> **The read is `useSourceContentRead`, and its answer is bound to its key (L48).** The hook holds the answer
> and the failure *together with the request key they answer*, and derives what to render: the surface
> cache's kept answer for this key, else the stored answer if its key is this key, else nothing; the failure
> is shown only when there is no result and its key is this key. So a different path or generation can
> never render a previous entry's content or failure, without the old reset-to-`null` before each read. A
> `live` flag cleared by the effect's cleanup still drops a superseded read. The hook reads through the
> surface's `ReviewReadCache` (via `ReviewReadCacheContext`): a cache hit issues no request, and an answer
> is offered to the cache, which keeps it only when it is `content` with an expansion. Content rendered
> outside a review surface has no provider and reads every time, as before. The retry clears the failure
> and bumps `attempt`, which is on the effect's dependencies, so a retried read is a real read.
>
> **Retained exported read API.** `SourceContentRequest` and `useSourceContentRead` remain exported,
> generation-keyed and cache-aware. Their former LaneFileFocus/source-explorer consumers are retired;
> exports do not imply a focused-lane window or inventory-row renderer still exists.
>
> **The per-hunk intent markers of this view (MIK-L34).** `SourceContent` and `Expansion` pass the optional `markers`
> down to `Sides`, which asks `IntentMarkers.useSourceMarking(expansion, mode, markers)` once. The answer is three
> pieces the branches place around the panes they already draw: `marking.note` above them (why a changed file shows
> no marks: its classification is loading, unavailable, describes other content than the drawn blobs, or is not read
> because a partial inventory does not list the path; or a count of hunks past a bounded text), `marking.marks` into
> the panes, and `marking.panel` below them (the open marker's list). Both sides `present`: the one `DiffPane` takes
> all the marks. The one-sided branch: each textual side's `contentBlock` hands its `FilePane` only that side's marks
> (`sideMarks(marking.marks, side)`); `contentBlock` gained the optional `marks` argument for this. Nothing here decides
> which hunk a mark belongs to or where it sits.
>
> ### Conventions
>
> The component takes nine props — the six it has always taken (`repo`, `master`, `leaf`, the
> `ReviewChangedFile` `entry`, and the two
> generation ids) plus the two optional display preferences `mode` and `collapse` (ICR-R24@v3) and the optional
> `markers` (MIK-R34, its type `SourceMarkers` exported) — and its
> helpers are plain module-level functions in lower case (`textual`, `sideLine`,
> `contentBlock`, `Sides`, `boundedNote`, `refusalBlock`, `Expansion`) with the one exported
> `PascalCase` component, matching the route's idiom. It imports its types and its one function from
> `../../data/review`, the `DiffMode` type it now takes from the change-set route's own `DiffPane`, and
> both renderers by their shipped paths, and it declares no client, no store and
> no CSS module. Every rendered fact carries a `data-testid` (`review-source-*`) or a data attribute
> (`data-side-state`, `data-side-truncated`, `data-currentness`), which is how the cases read a side's
> declared state back out of the DOM instead of inferring it from a sentence, and inline `style` objects
> match the cockpit panels' idiom.
>
> ### Invariants And Boundaries
>
> - **A state is drawn, never inferred.** Every branch is a function of the declared `state`; the only
>   read of a side's `text` is `textual`'s presence test, which decides *renderability*, not identity.
> - **A missing or unrenderable side is never an empty document.** `text` is absent for a non-textual
>   side, and the content path renders a block only for a side that is textual — so the pane cannot
>   manufacture the operand a diff or a viewer would need.
> - **An edit is never claimed from a pairing that is not two documents.** The two-`present` case is the
>   only path that draws a diff, and the one-sided case says in words that it claims no addition or
>   change.
> - **The content belongs to the generation the listing published.** The two tree ids are inputs, are
>   echoed with the request, and are on the effect's key; a superseded generation is labelled rather than
>   substituted, and a read bounded by the leaf's own change set says so.
> - **Bounded text is stated as bounded.** A truncated side prints its own note naming the sides, beside
>   the object identity and size the state line already carries, and the command that reaches the rest.
> - **Both renderers are reused, not re-implemented.** `DiffPane` comes from the change-set route and
>   `FilePane` from the file-viewer route; this module declares neither a differ nor a viewer, and it
>   decides neither the diff's layout nor its disclosure.
> - **Intent marks are threaded, never computed here (MIK-L34).** Which hunks a file has, what each names and on
>   which line its mark sits come from `IntentMarkers.tsx` over the classification owner's response; without a
>   marker scope `useSourceMarking` returns no marks and no note, so a dataset review and any view outside the
>   workspace render the landed pane.
> - **The diff layout and the full-file disclosure are inputs, never state.** `mode` and `collapse` arrive
>   as props and are threaded into `DiffPane`; this module holds no display preference of its own, so a
>   layout switch in the workspace/card cannot reset an expansion, and the defaults (`"split"`, `false`) are
>   exactly the shipped rendering.
> - **Display-only, and refusal-safe.** One read per request key and mounted review surface (a reopened
>   file at the same trees is served from the surface's cache), no write, no control; a
>   typed refusal and a rejected transport are two different rendered states, and neither is a success.
> - **One renderer for a transported failure.** The block this pane renders for a transport-level answer
>   is the shared `ReviewProblemBlock` imported from `ReviewOutcome.tsx`, not a second block declared for
>   this pane; R03's own typed-refusal block stays this module's and is not re-specified.
> - **A retry is a real re-read.** It re-arms the effect through `attempt` rather than re-rendering the
>   stored failure, so the second read travels the same path as the first. A failure or refusal is never
>   kept by the cache, so it is always asked again.
> - **An answer never outlives its key.** Result and failure are bound to `sourceContentKey`; the cache is
>   emptied by the surface whenever an answer from another comparison generation arrives (see
>   `ReviewReadCache.ts`).
> - **Boundary.** It owns one entry's *rendering* contract. Which generation is bound, which change set
>   admits the path, what each side's state is and what its bytes are belong to the server
>   (`models/knowledge/review_source_content.py` and the source-content route); this file re-derives
>   none of them, and it never resolves a path or a tree for itself.
>
> ### Todos
>
> None recorded.
>
> ## Evidence
>
> ### Docs References
>
> No domain documentation source is configured for this repository (`system/sources.md` carries no
> `Domain Documentation` entries). The statements below are grounded in repository source only.
>
> No configured domain documentation could be checked.
>
> ### Repo-Internal References
>
> The rendering claims on this card are grounded in the current helpers, the shipped panes, the
> client and wire types, the expression card Full file mount and retained dataset expression mount.
> The retired inventory/lane mounts are historical owners, not current integration witnesses. Test
> provenance and current assertion scope are qualified separately; no execution is claimed here.
>
> - **The header's own record of the defect and of the three rendering rules, including the rule that an `absent` side is a measured fact rather than an empty file.** (historical reference 1)
> - SourceContent obtains bound bytes through the client; its operand renderers reuse the existing diff and file panes. (historical reference 2)
> - Text renderability is determined by the supplied text value, rather than inferred from a present-state label. (historical reference 3)
> - Each side's declared state and abnormal/truncated detail remain open; measured object id and size alone sit inside Object identity. (historical reference 4)
> - The single readable operand drawn in the shipped viewer, in its own testid host, for a textual side only. (historical reference 5)
>
> - **The branch itself: both sides present draw the shipped two-sided diff, neither textual stops at the state lines, and the one-sided case states that no diff is claimed before drawing each readable side; each branch places the view's intent-marker note, marks and list around the panes it draws (MIK-L34).** (historical reference 6)
> - **The bounded read stated as a prefix of the object, naming which sides are truncated.** (historical reference 7)
> - **The typed refusal rendered with its code, detail, next action and offending input, and with no content beside it.** (historical reference 8)
> - Expansion preserves non-current reason and the existing leaf-change-set admission paragraph openly before Sides, even when superseded; normal endpoint provenance and marker threading remain. (historical reference 9)
> - **The four outcomes in order — transport error, loading, typed refusal, expansion — over one read keyed on the task context, the path and the two published generation ids.** (historical reference 10)
> - Where a view's intent markers come from: the pane's name and the classification a caller already holds (MIK-L34). (historical reference 12)
> - The marking of this view, and each side's own marks for the one-sided panes. (historical reference 13)
> - **The key the read is bound to, and the cache it reads through (L48).** (historical reference 15)
> - The client function this module reads through: the typed refusal is read out of the body whatever the HTTP status, and only a body that is not this route's answer throws. (historical reference 16)
> - **The wire shape a side is: the closed six-member state literal, the optional `text` that is present only for the two textual states, and the identity facts the state line prints.** (historical reference 17)
> - **The wire shape one opened entry is: the two sides, both generation ids, the three-member currentness, and the `path_bound` that says which measured change set admitted the path.** (historical reference 18)
> - The response envelope whose two states are the two rendered answers. (historical reference 19)
>
> - The central card Full file and retained dataset expression renderer supply the exact inventory trees to this source renderer; inventory navigation itself belongs to the comparison viewer. (historical reference 29)
> - The central card Full file and retained dataset expression renderer supply the exact inventory trees to this source renderer; inventory navigation itself belongs to the comparison viewer. (historical reference 30)
>
> - Central expression expansion reuses this bound source renderer. (historical reference 22)
> - **The cases that drive the real surface and the real client over a stubbed transport: the addition, the two-sided modification, the binary side, the symlink target and the submodule pointer.** (historical reference 23)
> - **The generation and boundedness cases: a superseded read keeps the listed generation's text on screen, and a truncated side is stated as a prefix beside its object size.** (historical reference 24)
> - **The failure and provenance cases: a typed refusal with no content, the exact generation and path the listing published, and the leaf-change-set bound stated when the requested generation could not be measured.** (historical reference 25)
> - **The two boundary cases: the byte-form row is listed without an open control, and an inventory that named no code trees offers no expansion at all.** (historical reference 26)
>
> | `Expansion` owns the behavior described above. | `Expansion` | dashboard/src/panels/review/SourceContent.tsx:155-157 |
> | `SourceContent` owns the behavior described above. | `SourceContent` | dashboard/src/panels/review/SourceContent.tsx:252-254 |
> | `Sides` owns the behavior described above. | `Sides` | dashboard/src/panels/review/SourceContent.tsx:71-73 |
>
> ### Cross-Repo References
>
> No cross-repository behavior is implemented in this file. The renderer draws one repository namespace's
> records at one repository's two bound code trees, and carries no identity that ranges beyond it.
>
> No meaningful cross-repo references found.
> - Per-hunk intent markers on the drawn full file (historical reference 27)
> - Typed route refusal with code and next action (historical reference 28)
>
> - Cached content read keyed on the two bound trees (historical reference 31)
> - Cached content read keyed on the two bound trees (historical reference 32)
>
> - Retained bound full-file source renderer for expression cards and dataset expression views (historical reference 33)
> - Retained bound full-file source renderer for expression cards and dataset expression views (historical reference 34)
>
> - The generation-keyed SourceContentRequest and useSourceContentRead remain exported; the focused-lane caller is retired and the retained card Full file consumer passes the review’s own code trees. (historical reference 11)
> - The generation-keyed SourceContentRequest and useSourceContentRead remain exported; the focused-lane caller is retired and the retained card Full file consumer passes the review’s own code trees. (historical reference 27)
> - The generation-keyed SourceContentRequest and useSourceContentRead remain exported; the focused-lane caller is retired and the retained card Full file consumer passes the review’s own code trees. (historical reference 28)

## Evidence

No Domain Documentation source is configured in this repository. The following witnesses are current source and checked-in assertions, not fresh executions.

- Side state, detail disclosures and the actual text-presence predicate are rendered literally. [35]
- Only the two-present branch draws a diff; other textual sides draw individual panes, with full-file marks and list placement. [36]
- Current-only provenance, open non-current/leaf-bound reasons and bounded-prefix wording are separate rendering decisions. [37]
- The exported request hook binds results/failures to its exact key, skips a cached read and makes superseded completions inactive. [38]
- The source cache key includes all six request fields; only content answers with an expansion are kept. [39]
- Failure/loading/typed refusal/expansion are distinct outcomes; layout/collapse/markers remain display inputs. [40]
- The current expression-card FullFile caller passes the review trees, task context, display inputs and pane marker. [41]
- Marker classification must describe the drawn endpoint objects before pane marking is used. [42]
- The separate marks list admits only the matching active hunk classification, labels unplaced entries and binds reveal to path and placed IDs. [43]
- The retained component helper and comparison-page helper are distinct, including an added-file case that checks both paths. [44]
- Binary, symlink, submodule, superseded and prefix declarations inspect the retained full-file renderer. [45]
- Refusal/generation cases distinguish comparison route requests from the retained source-content query; the leaf-bound case uses the retained component. [46]
- Byte-form and unavailable-inventory cases exercise the comparison helper, not a resurrected dataset or source-explorer mount. [47]
- The client sends all six supplied identity fields to the source-content route. [48]
