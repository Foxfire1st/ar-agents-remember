# dashboard/src/panels/review/SourceContent.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

What one listed inventory row opens **into**: the complete available content of the file at the two
bound code trees the listing published, plus each side's own declared state and measured object
identity. The Source pane lists what a task changed; this module is the renderer that answers the
question the listing raises but cannot itself answer — *what are the bytes?* — and it is the whole of
ICR-R03's rendering half.

It exists because the pane before it printed a path, a status and a reproducing command and had **no
source-content interaction at all**: a row labelled as an expansion showed no bytes, so a reader had to
leave the surface and run the command to learn what actually changed. The module's header states that
history and then the rules that replace it, and `ReviewSurface.tsx` reaches it from the row it renders.

Since ICR-R16 the pane also renders the **other** answer shape this route can give. Its *typed*
refusal (`state: "refused"`) is still R03's, rendered by this module's own `refusalBlock` and untouched;
everything else — an unwired process, a query the route does not admit, a socket that never answered —
now goes through the shared `ReviewProblemBlock` the review surface uses, carrying the code, reason,
offending input and next action the thrown message used to drop. See the transport paragraph under
Logic for the boundary between the two.

Two boundaries decide its shape. It is **display-only** in the same sense the rest of the surface is:
one read, no control that writes, no conclusion. And it **reuses the shipped renderers rather than
growing a third view** — `DiffPane` from the change-set route for the two-document case and `FilePane`
from the file-viewer route for a single readable operand — so a reader sees the same diff engine and the
same viewer here as everywhere else on the cockpit.

Since ICR-R24@v3 it also takes the reader's two display preferences from its caller. The optional
`mode` (a `DiffMode`) and `collapse` props are threaded straight into `DiffPane` rather than decided
here, because the explorer above owns the diff layout and the full-file disclosure — and because a
layout switch there must not be able to reset an expansion here. Their defaults (`"split"` and `false`)
are exactly the shipped rendering: a split diff of the whole file.

Since MIK-R34 it also draws the **per-hunk intent markers** of the diff it shows, through an optional
`markers` prop (`SourceMarkers`: the pane's name within the workspace, and the file's classification when
the caller already holds it, as the lane's full file does). The marks themselves are decided in
`IntentMarkers.tsx` from MIK-R32's one per-file classification; this module only threads them into the two
panes it already reuses. Outside a tree comparison's review workspace there is no marker scope, and the
view is exactly the landed one.

## Code Commentary

### Logic

Expansion leads with the actual content diff; the source side states, measured identities and boundary details remain available in a disclosure. Split/inline layout and collapse are supplied by the workspace, so content rendering remains bound to the exact listed trees.

**Every branch is decided by each side's declared `state`, and never by inspecting its text.** The
header states the rule and the three cases it produces; `Sides` implements them by asking the two
questions in a fixed order — are both sides `present`, then is either side textual at all — so the
`text` of a side that is not text can never be read as an operand. `textual(side)` is the one
predicate (`side.text !== undefined`) and it is deliberately *not* `state === "present"`: a `symlink`'s
recorded target is content a reader can be shown, while a `binary` side is not text and an `absent`
side is a measured fact about that endpoint rather than an empty file.

**The state line is drawn for both sides in every branch, and it carries the identity.** `sideLine`
renders `before (state) · object <id> · <n> byte(s)` inside a paragraph carrying
`data-testid="review-source-<name>-state"` and `data-side-state={side.state}`, with
`data-side-truncated` beside it. The long `detail` is appended only when `needsDetail` holds —
`side.state !== "present" || side.truncated` — because a complete untruncated `present` side needs no
explanation, while every other state is exactly the thing the reader has to be told about. The two
identity facts are optional and are printed only when the server measured them, so a side that has no
object (an `absent` endpoint) says less rather than claiming an identity it does not have.

**Both sides `present` → the shipped two-sided diff, over the two files' own bytes.** `DiffPane` is
called with `before.text ?? ""`, `after.text ?? ""`, `language={expansion.language}` and the caller's
`mode`/`collapse` — which default to `"split"` and `false`, the same shape the change-set viewer and the
statement area use, and which the explorer sets when the reader has chosen an inline layout or asked
for the whole file. The `?? ""` can only apply to a `present` side, which the model guarantees carries
text.

**One side `present` (or `symlink`) and the other not textual → the readable operand as content, the
unavailable side's own reason above it, and an explicit no-diff line.** `review-source-no-diff-claimed`
says that no addition or a change is claimed "from the two sides beside it", because a diff there would
assert that the other endpoint is a known-empty document — precisely the claim a `binary`, `submodule`,
`unavailable` or `absent` side makes unavailable. Each textual side is drawn in `FilePane` inside a
`review-source-<name>-content` host, and a side that is not textual gets **no content block at all**
rather than an empty one.

**Neither side textual → the two state lines and nothing else.** No diff, no content block and no
no-diff note: there is no operand to caveat, so the pane states what each endpoint is and stops.

**The generation is an input, never a lookup.** `SourceContent` takes `beforeCodeTreeId` and
`afterCodeTreeId` from the caller — the ids the inventory published to this client — and sends them
with every read; since L48 the read's identity is `sourceContentKey(repo, master, leaf, path,
beforeCodeTreeId, afterCodeTreeId)` (declared in `ReviewReadCache.ts`), so a different row or a
different listed generation is a different read and an unrelated re-render is not. A read therefore
describes the generation the reader was looking at even after the branch moved, which is what makes the
`currentness` line meaningful.

**`currentness`, `path_bound` and the command are the read's own provenance, and each is stated only
when it is the fact.** `review-source-currentness` always prints the three-member `currentness` with
its detail (a superseded read says so rather than silently showing newer bytes);
`review-source-generation` prints `generation <before> → <after> · <status>` plus `mode changed` when
the recorded status carried one; `review-source-path-bound` is rendered **only** when
`path_bound === "leaf_change_set"`, because the ordinary `requested_generation` bound is the row's own
listing and needs no explanation, while the leaf-bound case admits the path by a *different*
measurement and must say which; and `review-source-command` prints the reproduction the server
composed, `pre-wrap` because it is two lines of shell.

**A bounded read is a stated prefix, not a shorter file.** `boundedNote` collects whichever sides are
`truncated` and renders `review-source-truncated` once, naming those sides and saying the text above is
a stated prefix of the object whose exact identity and size are on its own line. The note is drawn
after `Sides`, so it annotates the text it qualifies rather than replacing it.

**Refusal is a rendered state, not an exception.** `refusalBlock` prints the typed `code` and `detail`,
the `next_action`, and the `offending_input` when there is one, under `review-source-refusal`, and it
shows no content: a refused read is a normal answer from this route (a path outside the measured change
set), not a degraded success.

**A transport-level failure is a `ReviewFailure` rendered by the shared block, not a thrown message
(ICR-R16).** The catch keeps `reviewProblemFromCause(cause)` in `problem` — the same classification the
surface and the entry bar use — and the component renders it through `ReviewProblemBlock` with
`origin="failure"` and `subject="this entry's content"`, so the server's own code, reason, offending
input and next action are all shown here too, plus a retry for a socket that never answered. The
pre-existing rendering printed only `cause.message`, which for a `503` read `503 unavailable` and dropped
the adapter's instruction. The retry re-arms the effect through an `attempt` counter, so a retried read
is a real read; R03's typed path is below it and unchanged: this module still renders its own
`refusalBlock` for a `state: "refused"` answer and never re-specifies that rendering.

**Four outcomes, and the order they are decided in.** The component returns the shared failure block
when `problem` is set, then the `review-source-loading` line (naming the path and "at the listed
generation") while `result` is `null`, then `refusalBlock` when the typed answer is `refused`, then
`Expansion` — carrying the two display preferences down to `Sides` — when the answer carries one, and
`null` otherwise.

**The read is `useSourceContentRead`, and its answer is bound to its key (L48).** The hook holds the answer
and the failure *together with the request key they answer*, and derives what to render: the surface
cache's kept answer for this key, else the stored answer if its key is this key, else nothing; the failure
is shown only when there is no result and its key is this key. So a different path or generation can
never render a previous entry's content or failure, without the old reset-to-`null` before each read. A
`live` flag cleared by the effect's cleanup still drops a superseded read. The hook reads through the
surface's `ReviewReadCache` (via `ReviewReadCacheContext`): a cache hit issues no request, and an answer
is offered to the cache, which keeps it only when it is `content` with an expansion. Content rendered
outside a review surface has no provider and reads every time, as before. The retry clears the failure
and bumps `attempt`, which is on the effect's dependencies, so a retried read is a real read.

**Exported for the unexplained-changes lane (MIK-L32).** `SourceContentRequest` and `useSourceContentRead` are now
exported (L32's only change to this file: two words). `LaneFileFocus.tsx` makes the same keyed, cached read of the
listed generation for a file the lane opens and cuts its focused hunk windows from the two exact side texts, so the
lane opens exactly the bytes the source explorer would, and a file already opened in the explorer is not read again.

**The per-hunk intent markers of this view (MIK-L34).** `SourceContent` and `Expansion` pass the optional `markers`
down to `Sides`, which asks `IntentMarkers.useSourceMarking(expansion, mode, markers)` once. The answer is three
pieces the branches place around the panes they already draw: `marking.note` above them (why a changed file shows
no marks: its classification is loading, unavailable, describes other content than the drawn blobs, or is not read
because a partial inventory does not list the path; or a count of hunks past a bounded text), `marking.marks` into
the panes, and `marking.panel` below them (the open marker's list). Both sides `present`: the one `DiffPane` takes
all the marks. The one-sided branch: each textual side's `contentBlock` hands its `FilePane` only that side's marks
(`sideMarks(marking.marks, side)`); `contentBlock` gained the optional `marks` argument for this. Nothing here decides
which hunk a mark belongs to or where it sits.

### Conventions

The component takes nine props — the six it has always taken (`repo`, `master`, `leaf`, the
`ReviewChangedFile` `entry`, and the two
generation ids) plus the two optional display preferences `mode` and `collapse` (ICR-R24@v3) and the optional
`markers` (MIK-R34, its type `SourceMarkers` exported) — and its
helpers are plain module-level functions in lower case (`textual`, `sideLine`,
`contentBlock`, `Sides`, `boundedNote`, `refusalBlock`, `Expansion`) with the one exported
`PascalCase` component, matching the route's idiom. It imports its types and its one function from
`../../data/review`, the `DiffMode` type it now takes from the change-set route's own `DiffPane`, and
both renderers by their shipped paths, and it declares no client, no store and
no CSS module. Every rendered fact carries a `data-testid` (`review-source-*`) or a data attribute
(`data-side-state`, `data-side-truncated`, `data-currentness`), which is how the cases read a side's
declared state back out of the DOM instead of inferring it from a sentence, and inline `style` objects
match the cockpit panels' idiom.

### Invariants And Boundaries

- **A state is drawn, never inferred.** Every branch is a function of the declared `state`; the only
  read of a side's `text` is `textual`'s presence test, which decides *renderability*, not identity.
- **A missing or unrenderable side is never an empty document.** `text` is absent for a non-textual
  side, and the content path renders a block only for a side that is textual — so the pane cannot
  manufacture the operand a diff or a viewer would need.
- **An edit is never claimed from a pairing that is not two documents.** The two-`present` case is the
  only path that draws a diff, and the one-sided case says in words that it claims no addition or
  change.
- **The content belongs to the generation the listing published.** The two tree ids are inputs, are
  echoed with the request, and are on the effect's key; a superseded generation is labelled rather than
  substituted, and a read bounded by the leaf's own change set says so.
- **Bounded text is stated as bounded.** A truncated side prints its own note naming the sides, beside
  the object identity and size the state line already carries, and the command that reaches the rest.
- **Both renderers are reused, not re-implemented.** `DiffPane` comes from the change-set route and
  `FilePane` from the file-viewer route; this module declares neither a differ nor a viewer, and it
  decides neither the diff's layout nor its disclosure.
- **Intent marks are threaded, never computed here (MIK-L34).** Which hunks a file has, what each names and on
  which line its mark sits come from `IntentMarkers.tsx` over the classification owner's response; without a
  marker scope `useSourceMarking` returns no marks and no note, so a dataset review and any view outside the
  workspace render the landed pane.
- **The diff layout and the full-file disclosure are inputs, never state.** `mode` and `collapse` arrive
  as props and are threaded into `DiffPane`; this module holds no display preference of its own, so a
  layout switch in the explorer cannot reset an expansion, and the defaults (`"split"`, `false`) are
  exactly the shipped rendering.
- **Display-only, and refusal-safe.** One read per request key and mounted review surface (a reopened
  file at the same trees is served from the surface's cache), no write, no control; a
  typed refusal and a rejected transport are two different rendered states, and neither is a success.
- **One renderer for a transported failure.** The block this pane renders for a transport-level answer
  is the shared `ReviewProblemBlock` imported from `ReviewOutcome.tsx`, not a second block declared for
  this pane; R03's own typed-refusal block stays this module's and is not re-specified.
- **A retry is a real re-read.** It re-arms the effect through `attempt` rather than re-rendering the
  stored failure, so the second read travels the same path as the first. A failure or refusal is never
  kept by the cache, so it is always asked again.
- **An answer never outlives its key.** Result and failure are bound to `sourceContentKey`; the cache is
  emptied by the surface whenever an answer from another comparison generation arrives (see
  `ReviewReadCache.ts`).
- **Boundary.** It owns one entry's *rendering* contract. Which generation is bound, which change set
  admits the path, what each side's state is and what its bytes are belong to the server
  (`models/knowledge/review_source_content.py` and the source-content route); this file re-derives
  none of them, and it never resolves a path or a tree for itself.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and helpers,
the two renderers it reuses rather than declares, the client function it reads through, the wire types
it consumes, the surface that mounts it from an openable row, and the case module that drives the real
surface over the real client.

- **The header's own record of the defect and of the three rendering rules, including the rule that an `absent` side is a measured fact rather than an empty file.** [1]
- SourceContent obtains bound bytes through the client; its operand renderers reuse the existing diff and file panes. [2]
- Text renderability is determined by the supplied text value, rather than inferred from a present-state label. [3]
- **One side's state line, carrying its declared state, its measured object identity and size, and the detail only when the state is not a complete untruncated text.** [4]
- The single readable operand drawn in the shipped viewer, in its own testid host, for a textual side only. [5]
- **The branch itself: both sides present draw the shipped two-sided diff, neither textual stops at the state lines, and the one-sided case states that no diff is claimed before drawing each readable side; each branch places the view's intent-marker note, marks and list around the panes it draws (MIK-L34).** [6]
- **The bounded read stated as a prefix of the object, naming which sides are truncated.** [7]
- **The typed refusal rendered with its code, detail, next action and offending input, and with no content beside it.** [8]
- **The read's own provenance: currentness always, the generation and status line, the leaf-change-set bound only when that is the measured bound, and the reproducing command; the optional `markers` passed on to the sides (MIK-L34).** [9]
- **The four outcomes in order — transport error, loading, typed refusal, expansion — over one read keyed on the task context, the path and the two published generation ids.** [10]
- The read's request type and hook, exported for the lane's focused diff (MIK-L32). [11]
- Where a view's intent markers come from: the pane's name and the classification a caller already holds (MIK-L34). [12]
- The marking of this view, and each side's own marks for the one-sided panes. [13]
- The lane's focused diff reading through it. [14]
- **The key the read is bound to, and the cache it reads through (L48).** [15]
- The client function this module reads through: the typed refusal is read out of the body whatever the HTTP status, and only a body that is not this route's answer throws. [16]
- **The wire shape a side is: the closed six-member state literal, the optional `text` that is present only for the two textual states, and the identity facts the state line prints.** [17]
- **The wire shape one opened entry is: the two sides, both generation ids, the three-member currentness, and the `path_bound` that says which measured change set admitted the path.** [18]
- The response envelope whose two states are the two rendered answers. [19]
- Inventory navigation carries the exact listed trees, and the central expression card reuses this source renderer. [20]
- **The parent that owns the open row and passes the two published tree ids down, so the read is the generation the reader was looking at — the explorer and its rows now, not `ReviewSurface.tsx`.** [21]
- Central expression expansion reuses this bound source renderer. [22]
- **The cases that drive the real surface and the real client over a stubbed transport: the addition, the two-sided modification, the binary side, the symlink target and the submodule pointer.** [23]
- **The generation and boundedness cases: a superseded read keeps the listed generation's text on screen, and a truncated side is stated as a prefix beside its object size.** [24]
- **The failure and provenance cases: a typed refusal with no content, the exact generation and path the listing published, and the leaf-change-set bound stated when the requested generation could not be measured.** [25]
- **The two boundary cases: the byte-form row is listed without an open control, and an inventory that named no code trees offers no expansion at all.** [26]

| `Expansion` owns the behavior described above. | `Expansion` | dashboard/src/panels/review/SourceContent.tsx:155-157 |
| `SourceContent` owns the behavior described above. | `SourceContent` | dashboard/src/panels/review/SourceContent.tsx:252-254 |
| `Sides` owns the behavior described above. | `Sides` | dashboard/src/panels/review/SourceContent.tsx:71-73 |

### Cross-Repo References

No cross-repository behavior is implemented in this file. The renderer draws one repository namespace's
records at one repository's two bound code trees, and carries no identity that ranges beyond it.

No meaningful cross-repo references found.
