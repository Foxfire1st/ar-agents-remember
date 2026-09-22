# dashboard/src/panels/review/SourceContent.tsx

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/SourceContent.tsx` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T07:05:34+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l3`, uncommitted; base `d80a0513e928ef29a973527d09597c82c96fde87` |
| lastVerifiedCommitHash | `dcf35a0e0fc06bccdafd22390b7588b0aea811bc` |
| lastVerifiedCommitDate | 2026-09-22T20:08:58+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

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

## Code Commentary

### Logic

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
called with `before.text ?? ""`, `after.text ?? ""`, `language={expansion.language}`, `mode="split"`
and `collapse={false}` — the same shape the change-set viewer and the statement area use. The `?? ""`
can only apply to a `present` side, which the model guarantees carries text.

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
with every read; the `useEffect` key is
`[repo, master, leaf, entry.path, beforeCodeTreeId, afterCodeTreeId]`, so a different row or a
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
`Expansion` when the answer carries one, and `null` otherwise. The effect sets both `result` and
`problem` back to `null` before each read and guards every assignment with a `live` flag its cleanup
clears, so a superseded read cannot write into the current row; `attempt` is on the effect's key, which
is what makes the retry a re-read.

### Conventions

The component takes six props — `repo`, `master`, `leaf`, the `ReviewChangedFile` `entry`, and the two
generation ids — and its helpers are plain module-level functions in lower case (`textual`, `sideLine`,
`contentBlock`, `Sides`, `boundedNote`, `refusalBlock`, `Expansion`) with the one exported
`PascalCase` component, matching the route's idiom. It imports its types and its one function from
`../../data/review` and both renderers by their shipped paths, and it declares no client, no store and
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
  `FilePane` from the file-viewer route; this module declares neither a differ nor a viewer.
- **Display-only, and refusal-safe.** One read on mount and on input change, no write, no control; a
  typed refusal and a rejected transport are two different rendered states, and neither is a success.
- **One renderer for a transported failure.** The block this pane renders for a transport-level answer
  is the shared `ReviewProblemBlock` imported from `ReviewOutcome.tsx`, not a second block declared for
  this pane; R03's own typed-refusal block stays this module's and is not re-specified.
- **A retry is a real re-read.** It re-arms the effect through `attempt` rather than re-rendering the
  stored failure, so the second read travels the same path as the first.
- **Boundary.** It owns one entry's *rendering* contract. Which generation is bound, which change set
  admits the path, what each side's state is and what its bytes are belong to the server
  (`models/knowledge/review_source_content.py` and the source-content route); this file re-derives
  none of them, and it never resolves a path or a tree for itself.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and helpers,
the two renderers it reuses rather than declares, the client function it reads through, the wire types
it consumes, the surface that mounts it from an openable row, and the case module that drives the real
surface over the real client.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The header's own record of the defect and of the three rendering rules, including the rule that an `absent` side is a measured fact rather than an empty file.** | `ReviewSourceContentResult`; `DiffPane`; `FilePane` | dashboard/src/panels/review/SourceContent.tsx:1-38; dashboard/src/panels/review/SourceContent.tsx:40-40; dashboard/src/panels/review/SourceContent.tsx:188-188 |
| The reused renderers and the one client function this module reads through, with the wire types it consumes. | `DiffPane`; `FilePane`; `reviewSourceContent` | dashboard/src/panels/review/SourceContent.tsx:27-38; dashboard/src/panels/review/SourceContent.tsx:5-5; dashboard/src/panels/review/SourceContent.tsx:46-46; dashboard/src/panels/review/SourceContent.tsx:98-98; dashboard/src/panels/review/SourceContent.tsx:13-13; dashboard/src/panels/review/SourceContent.tsx:47-47; dashboard/src/panels/review/SourceContent.tsx:80-80; dashboard/src/panels/review/SourceContent.tsx:44-44; dashboard/src/panels/review/SourceContent.tsx:202-202 |
| **The one renderability predicate: a side with `text` is text a reader can be shown, and it is deliberately not the `present` state.** | `textual`; `present` | dashboard/src/panels/review/SourceContent.tsx:40-56 |
| **One side's state line, carrying its declared state, its measured object identity and size, and the detail only when the state is not a complete untruncated text.** | `sideLine` | dashboard/src/panels/review/SourceContent.tsx:46-66 |
| The single readable operand drawn in the shipped viewer, in its own testid host, for a textual side only. | `contentBlock`; `FilePane` | dashboard/src/panels/review/SourceContent.tsx:68-74; dashboard/src/panels/file-viewer/FilePane.tsx:20-20; dashboard/src/panels/review/SourceContent.tsx:77-77; dashboard/src/panels/review/SourceContent.tsx:117-117; dashboard/src/panels/review/SourceContent.tsx:118-118 |
| **The branch itself: both sides present draw the shipped two-sided diff, neither textual stops at the state lines, and the one-sided case states that no diff is claimed before drawing each readable side.** | `Sides`; `review-source-no-diff-claimed` | dashboard/src/panels/review/SourceContent.tsx:76-112 |
| **The bounded read stated as a prefix of the object, naming which sides are truncated.** | `boundedNote`; `review-source-truncated` | dashboard/src/panels/review/SourceContent.tsx:114-124 |
| **The typed refusal rendered with its code, detail, next action and offending input, and with no content beside it.** | `refusalBlock`; `review-source-refusal` | dashboard/src/panels/review/SourceContent.tsx:126-138 |
| **The read's own provenance: currentness always, the generation and status line, the leaf-change-set bound only when that is the measured bound, and the reproducing command.** | `Expansion`; `review-source-currentness`; `review-source-path-bound`; `review-source-command` | dashboard/src/panels/review/SourceContent.tsx:140-162 |
| **The four outcomes in order — transport error, loading, typed refusal, expansion — over one read keyed on the task context, the path and the two published generation ids.** | `SourceContent`; `useEffect` | dashboard/src/panels/review/SourceContent.tsx:164-222 |
| The client function this module reads through: the typed refusal is read out of the body whatever the HTTP status, and only a body that is not this route's answer throws. | `reviewSourceContent`; `FilesApiError` | dashboard/src/data/review.ts:421-439; dashboard/src/data/changeset.test.ts:4-4; dashboard/src/data/changeset.test.ts:54-54; dashboard/src/data/changeset.test.ts:56-56; dashboard/src/data/changeset.ts:3-3; dashboard/src/data/files.test.ts:4-4; dashboard/src/data/files.test.ts:49-49; dashboard/src/data/files.test.ts:51-51; dashboard/src/data/files.ts:76-84; dashboard/src/data/notes.test.ts:3-3; dashboard/src/data/notes.test.ts:28-28; dashboard/src/data/notes.test.ts:30-30; dashboard/src/data/reviewTransport.test.ts:5; dashboard/src/data/reviewTransport.ts:18-18; dashboard/src/data/reviewTransport.ts:100-100; dashboard/src/data/reviewTransport.ts:102-102; dashboard/src/panels/changeset/ChangeSetViewer.tsx:27-27; dashboard/src/panels/changeset/ChangeSetViewer.tsx:306-306; dashboard/src/panels/file-viewer/FileViewer.tsx:12-12; dashboard/src/panels/file-viewer/FileViewer.tsx:112-112 |
| **The wire shape a side is: the closed six-member state literal, the optional `text` that is present only for the two textual states, and the identity facts the state line prints.** | `ReviewSourceSideState`; `ReviewSourceSide` | dashboard/src/data/review.ts:217-241 |
| **The wire shape one opened entry is: the two sides, both generation ids, the three-member currentness, and the `path_bound` that says which measured change set admitted the path.** | `ReviewSourceExpansion` | dashboard/src/data/review.ts:243-258 |
| The response envelope whose two states are the two rendered answers. | `ReviewSourceContentResult` | dashboard/src/data/review.ts:260-266 |
| **The row that opens this renderer: a button carrying the published path, `aria-expanded`, and the generation the content will be read at — drawn only when the inventory named both code trees.** | `inventoryEntry`; `review-inventory-open`; `SourceContent` | dashboard/src/panels/review/ReviewSurface.tsx:214-260; dashboard/src/panels/review/ReviewSurface.tsx:8-8; dashboard/src/panels/review/ReviewSurface.tsx:49-49; dashboard/src/panels/review/ReviewSurface.tsx:277-277 |
| **The parent that owns the open row and passes the two published tree ids down, so the read is the generation the reader was looking at.** | `Inventory` | dashboard/src/panels/review/ReviewSurface.tsx:291-335 |
| The header's own statement of the two reused renderers, `DiffPane` for the statements and this module for the Source pane's entry expansion. | `SourceContent` | dashboard/src/panels/review/ReviewSurface.tsx:1-9 |
| **The cases that drive the real surface and the real client over a stubbed transport: the addition, the two-sided modification, the binary side, the symlink target and the submodule pointer.** | "draws an added file's entire candidate text beside the named absent side"; "draws a modified file as the two-sided diff of its two bound texts"; "states a binary side's identity and size and draws no content for it"; "carries a symlink's target as content and never claims a document edit"; "reports a submodule pointer by its recorded commit and draws nothing for it" | dashboard/src/panels/review/SourceContent.test.tsx:269-291; dashboard/src/panels/review/SourceContent.test.tsx:293-316; dashboard/src/panels/review/SourceContent.test.tsx:318-339; dashboard/src/panels/review/SourceContent.test.tsx:341-364; dashboard/src/panels/review/SourceContent.test.tsx:366-385 |
| **The generation and boundedness cases: a superseded read keeps the listed generation's text on screen, and a truncated side is stated as a prefix beside its object size.** | "labels a superseded generation while still showing the listed generation's text"; "states a bounded expansion as a prefix of the object" | dashboard/src/panels/review/SourceContent.test.tsx:387-409; dashboard/src/panels/review/SourceContent.test.tsx:411-437 |
| **The failure and provenance cases: a typed refusal with no content, the exact generation and path the listing published, and the leaf-change-set bound stated when the requested generation could not be measured.** | "renders a refused entry read as its typed refusal and no content"; "sends the generation and path the listing published, not a re-resolved one"; "states which measured change set admitted the path when the requested one could not be measured" | dashboard/src/panels/review/SourceContent.test.tsx:439-457; dashboard/src/panels/review/SourceContent.test.tsx:459-488; dashboard/src/panels/review/SourceContent.test.tsx:490-520 |
| **The two boundary cases: the byte-form row is listed without an open control, and an inventory that named no code trees offers no expansion at all.** | "lists a byte-form row without implying it can be opened"; "offers no expansion for an inventory that named no code trees" | dashboard/src/panels/review/SourceContent.test.tsx:522-560; dashboard/src/panels/review/SourceContent.test.tsx:562-588 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The renderer draws one repository namespace's
records at one repository's two bound code trees, and carries no identity that ranges beyond it.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **the pane's transport-level failures now render through the shared block, and R03's typed path is deliberately untouched.** The fix round's F1: the catch keeps `reviewProblemFromCause(cause)` as a `ReviewFailure` and renders it through the shared `ReviewProblemBlock` (`origin="failure"`, `subject="this entry's content"`) with a retry wired to a new `attempt` counter, so an unwired process, an unadmitted query or a socket that never answered shows the code, reason, offending input and next action instead of only `cause.message` — the pre-fix rendering printed `the entry's content could not be read: 503 unavailable` and dropped the adapter's own instruction. `refusalBlock` (R03's typed-refusal rendering), its side states, its generation binding and its own cases are **unchanged and green**, and the card says so explicitly rather than implying the pane was re-specified. Line count 222 → 241. This card is the **body update** for that change; every row of the reference table was re-derived against this candidate in the same pass. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00), and the leaf's own `reviewedWorkingCandidate` row states what was actually read; nothing in this leaf is committed, so closeout owns the stamp.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **created.** The module is new in this leaf and this is its one-to-one card. It records what the renderer is *for* rather than where its lines are: one listed inventory entry opened into the actual content of both bound code trees, with the three rendering rules the header states and the defect they close (the pane printed a path and a command and showed no bytes), the reuse of the shipped `DiffPane` and `FilePane` rather than a third viewer, the generation as a caller-supplied input rather than a lookup (so a read describes the listing the reader was looking at), `currentness`/`path_bound`/`command` as the read's own provenance with the leaf-bound case stated only when it is the fact, the bounded read stated as a prefix of the object, the typed refusal rendered with no content, and the four outcomes in the order they are decided. Every row was re-verified against this candidate with `sed -n 'START,ENDp'` before it was written, and every anchor in a row occurs inside the range that row cites. **Stamp accounting:** the verification pair names the master line `d80a0513e928ef29a973527d09597c82c96fde87` (2026-09-21T19:51:20+02:00) — the last real commit the reading was taken against — because the module exists only in this leaf's **uncommitted** candidate and no commit contains the bytes a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read; closeout owns the stamp.
