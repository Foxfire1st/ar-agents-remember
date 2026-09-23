# dashboard/src/data/review.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/data/review.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated            | 2026-09-23T02:40+02:00 |
| lastVerifiedCommitHash |  `870701b43039cd205a8c98e418382729510c3de3`|
| lastVerifiedCommitDate |  2026-09-23T03:12:21+02:00|
| governingOverview | `dashboard/src/data/overview.md` |

## Governing Overview

[dashboard/src/data route overview](overview.md)

## Purpose

The browser-side, same-origin client for the read-only Intent Reviewer API
(`mcp/src/agents_remember/serving/review.py`). It now exports **three** requests, one per thing the
surface asks for: `intentReview` renders one comparison, `intentReviewEntries` asks which subjects that
comparison can be opened on — the call the task view makes before it can offer the button at all — and
`reviewSourceContent` opens one listed inventory entry into the actual content of both bound code trees.
Since ICR-R16 all three reads take their **transport** from `data/reviewTransport.ts` and this module is
their public entry: it imports `getReviewJson` and **re-exports** the moved surface (`ReviewTransportError`,
`getReviewJson`, `intentOnlyRefusal`, `reviewFailureToken`, `reviewProblemFromCause`,
`reviewProblemFromRefusal`, `unreadableAnswer`, and the `ReviewFailure`/`ReviewFailureToken`/
`ReviewRefusalFacts` types), so the surface and the task view still import one public entry and no
existing importer changed its import path.

Its own header states the shape it mirrors and the boundary it keeps: it mirrors `data/changeset.ts` — a
`base` arg with a same-origin default, typed results taken from the application models, a thrown error,
and **no store mutation** — and it is a *read* client, because the surface exposes no submission control
and so no function here writes anything. The header's new TRANSPORT paragraph records the one thing a
reader of this file needs: the route answers with its typed result and maps a refusal onto a `400`/`404`/
`503` status, so the refusal is in the **body** of a non-2xx response, and the shared `getJson` — which
reads only `body.status` and throws — dropped every one of them before a reader could see it.

The header also states the one rule every type below obeys: **every type mirrors one model in
`models/knowledge/review.py`, and a field the server omits is absent here rather than defaulted**, so
an unresolved reference stays unresolved on the client too. That is why the optional members are
declared with `?` and never given a fallback value. The expansion types mirror
`models/knowledge/review_source_content.py` the same way, which is the second model module this client
now speaks — the source-content route has its own wire shape rather than reusing the comparison's.

## Code Commentary

### Logic

**The module is one vocabulary of interfaces plus three request functions; there is no store, no
reducer and no hook.** It declares seven string-union types, twenty-nine interfaces and three exported
functions. The absence of state is the point: the review surface owns its own component state
(`ReviewSurface.tsx`), exactly as the change-set viewer owns its component state, so this module never
appears in `data/store.ts` and no `useDashboard` selector reads it.

**`ReviewSideState` and `ReviewSelectorKind` are the two client-side unions, and each mirrors a server
literal.** `ReviewSideState` is `"present" | "absent" | "binary" | "unresolved"`, mirroring the
`ReviewSideState` literal in the models module; `ReviewSelectorKind` is `"invariant" | "family"`,
mirroring `SELECTOR_KINDS` in the serving transport. Because the second is a union rather than a
`string`, a caller cannot pass an unadmitted selector kind without a type error, which is how the
server's `400 bad-request` for a third kind is kept out of the happy path on the client.

**`ReviewSideContent` carries `state`, an optional `text`, a `language` and a `detail`.** The
optionality is the whole rule: `text?: string` beside `state: ReviewSideState` means the diff renderer
is fed text only when the server said `present`, and an `absent`, `binary` or `unresolved` side arrives
with its own `detail` instead of an empty string. The client never manufactures the text it renders.

**`ReviewUnresolvedReference` is the client's own way of displaying "cannot be resolved".** It carries
`field`, an optional `recorded_reference` and a `detail`, and it appears inside five different
interfaces — the knowledge pane, the authored effect, the source pane, the evidence link and the
evidence pane — so an unresolved attribution is a rendered fact on every surface that can have one.

**The identity pair is `ReviewCandidateRef` and `ComparisonIdentity`.** `ReviewCandidateRef` carries
`repository_id`, `master`, `leaf_id` and an optional `task_ref` — task identities only, and no path,
which is the client half of the server's "a browser cannot choose which dataset is reviewed".
`ComparisonIdentity` carries `reference`, `policy_version`, the `binding_digest`, the
`selector_digest`, both snapshot digests and both optional code tree ids, so the surface renders the
comparison's identity rather than deriving one.

**The three panes are three interfaces whose fields are the panes' own statements.**
`ReviewKnowledgePane` carries `invariant_ids`, `family_ids`, the two `ReviewSideContent` statements,
the two condition lists, the `revision_groups`, the `field_changes`, the `authored_effects`, the
`signals`, the `assessments` and its own `unresolved` rows. `ReviewSourcePane` carries the `locations`,
the `remaining` counts, the optional `expansion_reference` and `expansion_command`, the attributed and
unattributed changed paths and its own `unresolved` rows. `ReviewEvidencePane` carries
`evidence_state`, `assessment_state`, the `evidence_links`, the `observations`, the `assessments`,
`source_inspection_available` and its own `unresolved` rows.

**The per-record interfaces each answer one question the panes print.**
`ReviewRevisionGroup` carries `side`, `record_id` and `selected_revision_count`, so the retained
revision count is kept per side. `ReviewFieldChange` carries `item_id`, `item_kind`, `field` and the
two optional values, where an absent value is the recorded fact. `ReviewSourceLocation` carries the
`claim_id`, the optional `invariant_revision_id`, the `path`, the optional `role` and `rationale`, the
recorded and observed source identities, the `resolution`, the three-member `change_state` and
`before_only`. `ReviewRemainingCount` carries `name`, an optional `value` and an optional `reason` —
`value?: number` beside `reason?: string` is exactly the server's rule that a quantity with no meaning
states why rather than reporting a zero.

**`ReviewStaleness` and `ReviewSubmission` are the two display values the surface's header block
prints.** `ReviewStaleness` carries `state` (`"current" | "stale"`), a `statement`, an optional
`previous_comparison_ref` and a `moved` list; `ReviewSubmission` carries `state`
(`"unavailable" | "disabled_stale"`), `reason`, `next_action`, `proposed_dispositions` and
`none_is_approval`. Neither union has a favourable member, so the client cannot render an absence as a
clearance.

**`ReviewPayload` and `ReviewResult` are the two response shapes.**
`ReviewPayload` carries `surface_version`, the `candidate`, the `comparison`, the three panes, the
`staleness`, the `submission` and a `limitations` list. `ReviewResult` carries `state`
(`"review" | "refused"`), `operation`, `repository_id` and the optional `payload`/`refusal` pair, and
`ReviewRefusal` carries `code`, `detail`, `next_action` and the optional `offending_input`, `expected`
and `observed`.

**`ReviewEntry` is one subject of the comparison's before/after population as the server's catalogue
lists it, and this client has no way to manufacture one (`ICR-R09@v1`).** `selector_kind` is the
existing `ReviewSelectorKind` union, `selector_id` and `label` are strings, and `presence` — the new
`ReviewSubjectPresence` union `"before_only" | "after_only" | "both"` — states which of the two
snapshots record the identity, so a retired (before-only) subject and a newly added (after-only) one
travel in the same list as the subjects both snapshots hold. **`selected_item_count` is deleted**:
it was the wire carrier of the per-subject compare-to-earn-a-row mechanism the packet removes (the
"only the first is reachable" defect's count), and an entry that carried a comparison count would
oblige the catalogue read to compare every subject before answering. The interface's own comment
still records the contract: it is "the ONLY legitimate source of the entry's selector", the id is a
recorded identity inside the pair the server resolved from task context, and **"There is no path
field here on purpose."** `ReviewEntryListResult` is its response envelope — `state`
(`"entries" | "refused"`), the literal `operation`, the task context, an optional `entries` array,
the **labelled totals** (`total_subjects`/`invariant_total`/`family_total`, the server's own
partition of the whole catalogue, so a caller traversing the list tells a whole catalogue from a
first row) and an optional `refusal` — so a refused read is a normal typed outcome with no entries
rather than an error a caller must catch.

**`intentReviewEntries` is the entry read, and it takes the task context and nothing else.** It returns
`getReviewJson<ReviewEntryListResult>` over `${base}/api/review/intent/entries?${qs({ repo, master,
leaf })}`, with the same `base = ""` same-origin default as `intentReview`. There is no selector in its
signature because a selector is exactly what it is being asked for. **Its comment was rewritten by
ICR-R16, and the rewrite is the point:** a refused read is now "*read* rather than thrown: the answer is
`entries` with the subjects the pair offers (an empty list is the known-empty answer "no subject is
recorded here"), or `refused` with the owner's own code, reason and next action, which the task view
shows beside the entry. The entry itself never depends on this read: it is offered for an admitted live
candidate, and a refusal here leaves the task-context review reachable." The old semantics — "it yields
no entry and the caller renders no button" — is exactly the behaviour this leaf removed.

**`intentReview` is the comparison request and it never names a path.** It takes
`repo`, `master`, `leaf`, `selectorKind`, `selectorId` and a `base` defaulting to `""` (same-origin),
and returns `getReviewJson<ReviewResult>` over `${base}/api/review/intent?${qs({...})}`. Only `qs` still
comes from `data/files.ts` — it is the one query-string encoder the other clients use — while the
transport is this route's own decode, because the comparison route's refusal arrives in the body of a
non-2xx response and `getJson`'s throw-on-non-2xx idiom (right for the other serving routes) would turn
it into a transport error. The trailing comment states the omission that matters: it names
canonical task context and one recorded subject, and never a filesystem path, because the candidate is
resolved on the server and the browser must not be able to choose which dataset is reviewed.

**The client gained the expansion's wire types and a third request, which opens one listed entry at the two generations the listing published.** `ReviewSourceSideState` is the closed six-member literal a side's `state` may be (`present`, `absent`, `binary`, `symlink`, `submodule`, `unavailable`), `ReviewSourceSide` carries that state with an optional `text` — present only for the two textual states, so a missing or unrenderable side can never arrive as an empty document — plus `detail`, optional `object_id`/`byte_length` and `truncated`, `ReviewSourceExpansion` carries the entry's `path`, `status`, `mode_change`, `language`, the two sides, both generation ids, the three-member `currentness` with its detail, `path_bound` (`requested_generation`/`leaf_change_set`) with its detail, and the `reference`/`command`, and `ReviewSourceContentResult` is the envelope whose `state` is `"content"` with an optional `expansion` or `"refused"` with an optional `refusal`.

**`reviewSourceContent` no longer decodes its own body: it delegates to the one shared review decode.** A refused source read is a *normal* answer on this route — a path outside the measured change set, a baseline that is not this leaf's recorded one — and the transport carries it as the typed refusal in the body **with** a `400`/`404` status. That decode used to be inline here; ICR-R16 moved it into `data/reviewTransport.ts`, so this function is now a one-expression delegation to `getReviewJson<ReviewSourceContentResult>` over the same URL, and `grep -rn "api/review/intent" dashboard/src` finds the route URL only in the two review client modules. The behaviour a caller sees is unchanged for a typed answer and strictly better for everything else: a body that is not this route's answer now becomes a named `ReviewTransportError` failure carrying the owner's code, reason, offending input and next action — where the old inline decode built a `FilesApiError` from the response's status and the body's own `status` string and dropped the rest.

**The generation is an input here too, not a lookup.** `reviewSourceContent(repo, master, leaf, path, beforeCodeTreeId, afterCodeTreeId, base = "")` takes the two tree ids the inventory published to this client and sends them back with the request — in that camelCase spelling, which is the spelling the route binds — so the content a reader opens is the content of the generation they were looking at, never re-resolved from whatever the leaf holds by the time the request lands. The function resolves no path and no tree of its own, and its own comment states that boundary.

**The client gained the inventory's wire types and the three states that let a review exist without a subject.** `ReviewChangedFile` (the raw `path` exactly as Git recorded it — a tab or a newline inside it is part of the address — plus `status`, `content`, `mode_change` and an optional `detail`), `ReviewUnrepresentablePath` (`path_bytes`: the exact bytes in an ASCII-safe spelling, listed rather than dropped and never re-encoded) and `ReviewSourceInventory` (`state` `measured`/`unavailable`, the entries, `listed_total`, `detail`, `partial`, `command`, both tree ids and `unrepresentable_paths`), with `ReviewSourcePane.inventory` now required and first. `ComparisonIdentity` gained `knowledge_compared` and its three knowledge-half digests became optional, `ReviewKnowledgePane` gained `selection_state`/`selection_detail`, `ReviewStaleness.state` gained `not_compared`, and `ReviewPayload.comparison` became optional. `intentReview` sends **no selector parameters at all** when there is none, which is the task-context request; the same "a field the server omits is absent rather than defaulted" rule now covers an entire absent identity, and no fallback value was introduced for it.

### Conventions

The module imports three helpers — `FilesApiError`, `getJson` and `qs` from `./files` — and declares
everything else itself. Interfaces are exported and named with the `Review`/`Comparison` prefix so a
reader can tell a review display value from the change-set client's own types; the optional members use
`?` with no default, which is the client half of the server's `exclude_none=True`. There is no `default`
export and no class. The module declares **three** functions, one per request the surface makes, and
each is appended after the response types it answers with rather than beside its predecessors, so the
file still reads top-down as the response shape: the comparison's vocabulary and `intentReview`, the
entry half's two types and `intentReviewEntries`, then the expansion half's four types and
`reviewSourceContent`.

### Invariants And Boundaries

- **Read-only, with no store mutation.** Every function here is a `GET` and nothing else; the surface
  exposes no submission control, so no function here writes.
- **No path is accepted for a comparison, and the one path this client does send is one the server
  published.** `intentReview` and `intentReviewEntries` name a task context and (for the former) one
  recorded subject, because the candidate is resolved server-side; `reviewSourceContent` names a path
  **and** the two generation ids the inventory published to this client, so it addresses a row of a
  measurement the server already made rather than choosing a file.
- **A typed refusal is a returned state; a transport-level failure is a named throw.** All three reads
  go through `getReviewJson`, which returns the body as the typed result whenever it carries this
  route's `state` (a payload, a subject list or a typed refusal) and throws `ReviewTransportError`
  otherwise — so an unadmitted answer is named and never rendered as an empty review.
- **The transport has one owner and this module is its public entry.** The decode lives in
  `data/reviewTransport.ts` and is re-exported here, so a consumer has one import and the review client
  has no second implementation.
- **Unrelated clients are untouched.** `getJson` still reads only `body.status` and still throws for the
  routes that use it — which is exactly why the change-set client below is unchanged (see Todos).
- **A field the server omits is absent rather than defaulted.** Every optional member is optional
  because the server may not send it, and no fallback value is provided.
- **Unresolved is displayed, not filled in.** `ReviewUnresolvedReference` appears wherever an
  attribution or a coverage statement can be missing.
- **Neither display union has a favourable member.** `ReviewSubmission.state` is `unavailable` or
  `disabled_stale`, and `ReviewStaleness.state` is `current` or `stale`; an absence cannot be read as a
  clearance.
- **The error idiom is the file API's, specialised for this route.** A review read throws
  `ReviewTransportError`, which **extends** `FilesApiError` so an existing catcher keeps working, and
  carries the whole `ReviewFailure` so a caller can render the refusal instead of only its status line;
  the other serving routes keep `getJson`'s plain throw.

### Todos

One routed item is recorded rather than fixed, because it is a different route, client and owner:

- **The change-set client still swallows its own refusal detail.** `data/changeset.ts` mirrors this
  client's shape and reads through `getJson` — `/api/changeset/task`, `/api/changeset/master`,
  `/api/changeset/file-diff` — and `changeSetBar.tsx`'s live-leaf `committed`/`working` counter
  consequently drops a failed read with `() => live && setCounters(null)`: no reason, no next action.
  That is the change-set client, not the review transport, and it is **routed to R12 (historical
  committed-leaf review) / R24 (usable review navigation)**. Measured in this leaf; not fixed here, to
  keep the blast radius to the review route.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and its two
stated rules, the two unions and the interfaces that mirror the server's models, the three request
functions and the helper each one borrows from the file API, and the clients that consume it. Every row
was re-derived against this candidate — this leaf's expansion types and third request moved every
construct below the source pane — and every anchor in a row occurs inside the range that row cites.

| Finding | Anchor | Source |
| --- | --- | --- |
| The header's own statement of what this file mirrors, the rule that a field the server omits is absent rather than defaulted, and the second model module the expansion types mirror. | `Mirrors`; `FilesApiError`; `same way (ICR-R03)` | dashboard/src/data/review.ts:1-9; dashboard/src/data/changeset.test.ts:4-4; dashboard/src/data/changeset.test.ts:54-54; dashboard/src/data/changeset.test.ts:56-56; dashboard/src/data/changeset.ts:3-3; dashboard/src/data/files.test.ts:4-4; dashboard/src/data/files.test.ts:49-49; dashboard/src/data/files.test.ts:51-51; dashboard/src/data/files.ts:76-84; dashboard/src/data/notes.test.ts:3-3; dashboard/src/data/notes.test.ts:28-28; dashboard/src/data/notes.test.ts:30-30; dashboard/src/data/reviewTransport.test.ts:25-25; dashboard/src/data/reviewTransport.test.ts:175-175; dashboard/src/data/reviewTransport.test.ts:180-180; dashboard/src/data/reviewTransport.test.ts:295-295; dashboard/src/data/reviewTransport.test.ts:300-300; dashboard/src/data/reviewTransport.ts:18-18; dashboard/src/data/reviewTransport.ts:100-100; dashboard/src/data/reviewTransport.ts:102-102; dashboard/src/panels/changeset/ChangeSetViewer.tsx:27-27; dashboard/src/panels/changeset/ChangeSetViewer.tsx:306-306; dashboard/src/panels/file-viewer/FileViewer.tsx:12-12; dashboard/src/panels/file-viewer/FileViewer.tsx:112-112 |
| The two client-side unions, each mirroring a server literal. | `ReviewSideState`; `ReviewSelectorKind` | dashboard/src/data/review.ts:33-34 |
| **The missing-side rule on the client: text is optional beside the state, so no empty string is manufactured.** | `ReviewSideContent` | dashboard/src/data/review.ts:36-41 |
| The shared shape that makes an unresolved reference a displayed fact on every surface that can have one. | `ReviewUnresolvedReference` | dashboard/src/data/review.ts:43-47 |
| The candidate reference, which carries task identities and no path, and the comparison identity carried rather than derived. | `ReviewCandidateRef`; `ComparisonIdentity` | dashboard/src/data/review.ts:55-55; dashboard/src/data/review.ts:56-69 |
| The per-side revision count and the field transition whose absent value is the recorded fact. | `ReviewRevisionGroup`; `ReviewFieldChange` | dashboard/src/data/review.ts:71-75; dashboard/src/data/review.ts:77-83 |
| The authored record with its examined inputs, and the detection fact with its versions and scope limitations and no severity. | `ReviewAuthoredEffect`; `ReviewSignal` | dashboard/src/data/review.ts:91-101; dashboard/src/data/review.ts:144-154 |
| The assessment display with its author, examined inputs, binding state and evidence refs. | `ReviewAssessmentDisplay` | dashboard/src/data/review.ts:156-167 |
| The three panes, each carrying its own `unresolved` rows. | `ReviewKnowledgePane`; `ReviewSourcePane`; `ReviewEvidencePane` | dashboard/src/data/review.ts:169-190; dashboard/src/data/review.ts:256-265; dashboard/src/data/review.ts:344-354 |
| The selected source location with its optional role and its three-member change state. | `ReviewSourceLocation` | dashboard/src/data/review.ts:137-149 |
| **The count shape whose optional value beside its optional reason is how a quantity with no meaning states why rather than reporting a zero.** | `ReviewRemainingCount`; `value?: number`; `reason?: string` | dashboard/src/data/review.ts:151-155 |
| The evidence claim reference and the observation displayed exactly. | `ReviewEvidenceLink`; `ReviewObservation` | dashboard/src/data/review.ts:323-329; dashboard/src/data/review.ts:331-342 |
| **The two display unions with no favourable member.** | `ReviewStaleness`; `ReviewSubmission` | dashboard/src/data/review.ts:356-369; dashboard/src/data/review.ts:304-310 |
| The whole payload and the two response shapes. | `ReviewPayload`; `ReviewRefusal`; `ReviewResult` | dashboard/src/data/review.ts:371-442; dashboard/src/data/review.ts:318-318; dashboard/src/data/review.ts:335-346 |
| **The comparison request: a task context, one recorded subject and a same-origin default, with no path.** | `intentReview` | dashboard/src/data/review.ts:403-403 |
| **The reviewed subject as the server selected it — the entry's only legitimate selector source, with no path field on purpose.** | `ReviewEntry` | dashboard/src/data/review.ts:372-379 |
| **The entry read's response envelope: a refused read is a typed outcome carrying its refusal and no entries, not an error to catch.** | `ReviewEntryListResult` | dashboard/src/data/review.ts:381-401 |
| **The entry request: the task context alone, because a selector is what it is being asked for, and the same same-origin default as the comparison.** | `intentReviewEntries` | dashboard/src/data/review.ts:403-419 |
| **The six-member state literal a side may be, and the side value whose optional `text` is present only for the two textual states — so no missing or unrenderable side can arrive as an empty document.** | `ReviewSourceSideState`; `ReviewSourceSide` | dashboard/src/data/review.ts:272-287; dashboard/src/data/review.ts:225-241 |
| **The expansion value: both sides, both generation ids, the three-member currentness, and `path_bound` naming which measured change set admitted the path.** | `ReviewSourceExpansion` | dashboard/src/data/review.ts:243-258 |
| **The source-content envelope whose two states are the two answers this route gives, a refusal being a normal one.** | `ReviewSourceContentResult` | dashboard/src/data/review.ts:260-266 |
| **The source-content request: the task context, the published path and both published generation ids, read with `fetch` because the body is this route's answer whatever the status was.** | `reviewSourceContent` | dashboard/src/data/review.ts:421-439 |
| **The error idiom this route deliberately steps outside of: `getJson` throws on a non-OK status, while a refused source read arrives with a typed refusal in the body.** | `getJson`; `FilesApiError`; `qs` | dashboard/src/data/files.ts:76-97; dashboard/src/data/files.ts:99-101 |
| The sibling client whose shape this file mirrors, including its own no-store-mutation comment. | `taskChangeset`; `FilesApiError` | dashboard/src/data/changeset.ts:1-8; dashboard/src/data/changeset.ts:25-25; dashboard/src/data/changeset.ts:78-78; dashboard/src/data/changeset.ts:128-128 |
| The surface that consumes this client: the comparison read, and the entry expansion an openable inventory row mounts. | `intentReview`; `reviewSourceContent` | dashboard/src/data/review.ts:456-618; dashboard/src/data/review.ts:547-547 |
| **The task-view consumer that makes the entry reachable: the hook that asks this client for the leaf's reviewable subjects and leaves the button hidden on a refusal or an empty list.** | `useReviewCatalogue` | dashboard/src/panels/detail-panel/changeSetBar.tsx:122-187 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The client talks to its own origin and names
one repository namespace in the query string.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T16:20:00+02:00 — 260921-ICR-L9 curator (candidate `ar/260921-icr-l9`, uncommitted; production line `f141d164265e926be9249acf6ae680ccf9ffae61`, this leaf's base): **the client mirrors the catalogue wire shape, and the count field is deleted (428 → 439 lines; `ICR-R09@v1`).** `ReviewSubjectPresence` (`"before_only" | "after_only" | "both"`) is declared beside the entry it travels in, `ReviewEntry.presence` **replaces** `selected_item_count` — the deleted field was the count the per-subject compare-to-earn-a-row mechanism earned its rows with, and an entry carrying a comparison count would oblige the catalogue read to compare every subject before answering — and `ReviewEntryListResult` gains the labelled totals (`total_subjects`/`invariant_total`/`family_total`), which is how a caller traversing the list tells a whole catalogue from its first row. The Logic's entry paragraph was rewritten rather than annotated because its old account of `selected_item_count` is false at this candidate, and the vocabulary-count sentence now says seven unions and twenty-nine interfaces. **Citation accounting:** every row citing this file re-derived from its construct's own measured extent in the 439-line candidate — the interfaces had also moved with earlier leaves' insertions the card had not re-derived (`ReviewSideState`/`ReviewSelectorKind` `33-34`, `ReviewSideContent` `36-41`, `ReviewUnresolvedReference` `43-47`, `ReviewCandidateRef`/`ComparisonIdentity` `49-54`/`56-69`, `ReviewRevisionGroup`/`ReviewFieldChange` `71-75`/`77-83`, `ReviewAuthoredEffect`/`ReviewSignal` `85-94`/`96-105`, `ReviewAssessmentDisplay` `107-117`, the panes `119-135`/`201-215`/`287-295`, `ReviewSourceLocation` `137-149`, `ReviewRemainingCount` `151-155`, `ReviewStaleness`/`ReviewSubmission` `297-302`/`304-310`, `ReviewPayload`/`ReviewRefusal`/`ReviewResult` `312-324`/`326-333`/`335-346`, `intentReview` `348-370`, `ReviewSubjectPresence`+`ReviewEntry` `372-379`, `ReviewEntryListResult` `381-401`, `intentReviewEntries` `403-419`, the expansion types `217-241`/`243-258`/`260-266`, `reviewSourceContent` `421-439`) — and the task-view-consumer row re-anchored to the renamed hook (`useReviewSubject` → `useReviewCatalogue` at `changeSetBar.tsx:122-187`). **Stamp accounting:** the verification pair names the leaf's base — the last real commit the reading was taken against — because the presence union and the totals exist only in this leaf's uncommitted candidate; closeout owns the stamp once the code commit exists.
- 2026-09-22T07:05:34+02:00 — 260921-ICR-L16 curator (candidate `ar/260921-icr-l16`, uncommitted; base `8ff80ce08814856c9d6fec5b19093e6540fc6d7f`): **the client's three reads delegate to one decode, and the card's account of `getJson` as this route's error idiom is corrected rather than carried.** Three statements the card previously made have been **removed or replaced** because this change made them false: (1) "a thrown `FilesApiError`" in the Purpose — the header now says "a thrown error", and the read throws a `ReviewTransportError` that extends `FilesApiError` so existing catchers keep working while gaining the whole `ReviewFailure`; (2) the account of `intentReview`/`intentReviewEntries` as `getJson<…>` calls — both now call `getReviewJson`, and the entry read's own comment was rewritten, so the card quotes the new comment and names the old "no subject means no button" semantics as the behaviour this leaf removed; (3) "**`reviewSourceContent` is the one function here that does not go through `getJson`**" — that inline decode **moved** into `data/reviewTransport.ts` and the function is now a one-expression delegation, with the route URL still living only in this module and the transport module. The card also records the module's new shape: `getReviewJson` imported, the moved surface re-exported so existing importers keep one public entry, and a new `Todos` note that the **change-set client is unchanged and still swallows its own refusal detail** (`data/changeset.ts` → `getJson` → `/api/changeset/task`, dropped by `changeSetBar.tsx`'s counter handler) — a different route, client and owner, **routed to R12/R24**. Line count 414 → 428. Every row of the reference table was re-derived against this candidate. **Stamp accounting:** the verification pair names the **merged production line** `8ff80ce08814856c9d6fec5b19093e6540fc6d7f` (2026-09-22T00:48:09+02:00), and the leaf's own recorded working candidate states what was actually read; nothing in this leaf is committed, so closeout owns the stamp.
- 2026-09-21T22:40+02:00 — 260921-ICR-L3 curator (uncommitted change set on `ar/260921-icr-l3`, base `d80a0513e928ef29a973527d09597c82c96fde87`): **the client gained the expansion's wire types and a third request, and it is the one function here that deliberately does not go through `getJson`.** Added `ReviewSourceSideState` (the closed six-member literal), `ReviewSourceSide` (the optional `text` that is present only for the two textual states, so a missing or unrenderable side can never arrive as an empty document), `ReviewSourceExpansion` (both sides, both generation ids, the three-member `currentness`, and the `path_bound` that says which measured change set admitted the path), `ReviewSourceContentResult`, and `reviewSourceContent(repo, master, leaf, path, beforeCodeTreeId, afterCodeTreeId, base = "")` — which `fetch`es the route, decodes the body **whatever the HTTP status was**, returns it typed when `body.state` is `"content"` or `"refused"`, and throws `FilesApiError` only for a body that is not this route's answer. The rationale is recorded on the card because it is the reason a reader will not find `getJson` there: on this route a typed refusal is a normal answer carrying a 400/404 status, and `getJson`'s throw-on-non-OK idiom would turn it into a transport error. `intentReview` and `intentReviewEntries` are **unchanged** by this leaf. The file is 414 lines (was 320 at `d80a0513`), and the two rules the header states now cover an expansion type set that mirrors a second model module. **Citation accounting:** every row of the reference table was re-derived against this candidate — the new types are cited at `192-213`, `214-238` and `240-246`, `reviewSourceContent` at `379-414`, and every construct below the source pane moved, which is stated here so the pass is auditable: `intentReview` `271-290` → `323-342`, `ReviewEntry` `291-296` → `344-353`, `ReviewEntryListResult` `298-311` → `355-363`, `intentReviewEntries` `312-320` → `365-377`, `ReviewPayload`/`ReviewRefusal`/`ReviewResult` `235-247`/`249-256`/`258-270` → `292-304`/`306-313`/`315-321`, `ReviewStaleness`/`ReviewSubmission` `220-225`/`227-233` → `277-282`/`284-290`, `ReviewKnowledgePane` `94-107` → `99-113`, `ReviewSourcePane` `180-189` → `181-190`, `ReviewEvidencePane` `210-218` → `267-275`, `ReviewEvidenceLink`/`ReviewObservation` `191-196`/`198-208` → `248-253`/`255-265`, `ReviewSourceLocation` `109-121` → `114-126`, `ReviewRemainingCount` `130-134` → `128-135`, the two unions `12-13` → `13-14` and `ReviewSideContent` `15-20` → `16-21`; the helpers row was repointed at `files.ts:76-97` (the thrower's own body) so `getJson` and `FilesApiError` both occur inside it, and the consumer row now names both requests this surface makes. **Stamp accounting:** the verification pair now names the master line `d80a0513e928ef29a973527d09597c82c96fde87` (2026-09-21T19:51:20+02:00) — the last real commit the reading was taken against — and the recorded working candidate states the leaf's own uncommitted candidate; no commit contains the new bytes, so closeout owns the real stamp.
- 2026-09-21T14:59:00+02:00 — 260921-ICR-L2 curator (uncommitted change set on `ar/260921-icr-l2`, base `702714fc05363cb28eacaf101ba8384475a6aa56`): **the client mirrors the new wire shape, and the request can now ask for the task's own review.** Added the inventory's three interfaces and the `source.inventory` field; made `comparison` optional with `knowledge_compared`; added `selection_state`, `not_compared` and the optional knowledge-half digests; and changed `intentReview` so it omits `selectorKind`/`selectorId` entirely when there is no subject, which is the task-context entry a leaf with no invariant still has. The two rules the header states are unchanged and now cover an absent identity as well as an absent field. Every row in the reference table was re-derived against this candidate. **Stamp accounting:** the verification rows still name the last real commit whose bytes this card was verified against, because nothing in this leaf is committed; claims whose evidence this leaf's change moved were re-read against the candidate and are stamp-class leftovers that only closeout can stamp.

- 2026-09-20T13:43:00+02:00 — 260915-KS-L45 curator (uncommitted change set on `ar/260915-ks-l45-ar`, base `fb719f89`): **the client gained the entry read, which is what makes the task view able to offer the reviewer at all.** The card now records `ReviewEntry` (the reviewed subject as the *server* selected it — a `ReviewSelectorKind`, a recorded id, the identity's own label and the operation's count, with **no path field on purpose**, because the browser never chooses the candidate), `ReviewEntryListResult` (a `state`/`operation`/task-context envelope whose refused form carries a `refusal` and no entries, so a refusal is a normal typed outcome rather than a thrown error), and `intentReviewEntries(repo, master, leaf, base = "")` — the second request this module exports, taking the task context alone because a selector is precisely what it is being asked for. The Conventions paragraph was corrected from "the module's one request" to two, and the row that said so now distinguishes the comparison request from the entry request. No verification stamp was advanced, because no commit contains this body.
- 2026-09-18T18:05+02:00 — 260915-KS-L22 curator (uncommitted change set on `ar/260915-ks-l22`, base `2dcacb27`): created this one-to-one card for the Intent Reviewer's browser client. It records the two rules the file's own header states — every type mirrors one model in `models/knowledge/review.py`, and **a field the server omits is absent here rather than defaulted**, so an unresolved reference stays unresolved on the client — plus the two boundaries a reader needs: it is a *read* client with **no store mutation** (it is not in `data/store.ts`, and the surface owns its own component state), and the one request names a task context and one recorded subject and **never a filesystem path**, because the candidate is resolved server-side. It also records that the two display unions (`ReviewStaleness`, `ReviewSubmission`) have no favourable member, so an absence cannot be rendered as a clearance. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. What was actually read is this leaf's uncommitted working tree, and closeout owns the stamp once the code commit exists.

## 260921-ICR-L10 The Page Contract On The Client, And The One Normaliser Of "No Page"

`260921-ICR-L10` (`ICR-R10@v1`) gives this client the page it was missing. It gained
`ReviewPagedCollection` (the two bounded collections named rather than inferred, because their cursors
are different documents), the `ReviewCollectionPage` interface with the server's own `total`/`returned`/
`remaining`, the owner's opaque `continuation`, the active `scope` and the `total_basis` that says what
`total` counts, a separate `page_refusal` on the payload for a requested page no owner could serve, and
the `pageOf`/`continuation`/`pageSize` request parameters.

Four pure helpers carry the decisions so no component has to: `continuationOf` (what a control may
offer), `pageBounds` (one sentence per basis), `carriedPage` and `RESET_GLOSS`. **`carriedPage` is the
one a later reader must not undo:** the route serializes with `exclude_none=True`, so a refused page
*omits* the `page` key instead of sending `null`, and a consumer comparing against `null` never fires
for a real response. Every consumer reads through the normaliser, and none constructs or parses a
cursor — the server's own token is echoed back.

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-23T00:30:00+02:00 — 260921-ICR-L10 curator (candidate `ar/260921-icr-l10`, uncommitted; production line at this leaf's base `dcf35a0e0fc06bccdafd22390b7588b0aea811bc`): **the client carries a page, and one normaliser owns the two spellings of "no page".** The page
contract (`ReviewPagedCollection`, `ReviewCollectionPage` with `total_basis`, the payload's separate
`page_refusal`), the three request parameters and the four pure helpers (`continuationOf`, `pageBounds`,
`carriedPage`, `RESET_GLOSS`) are new, and every row on this card that cited `data/review.ts` by line was
re-derived against this candidate because this leaf moved them. **The fact that must not be lost:** the
route omits the `page` key under `exclude_none=True`, so the client reads through `carriedPage` and no
consumer compares against `null`. No verification stamp was advanced: nothing in this leaf is committed, so the commit/closeout stamp remains closeout's.
## 260921-ICR-L26 The Client Mirrors The Applicability Vocabulary

`260921-ICR-L26` (`ICR-R26@v1`) gives this client the three interfaces of the attribution half —
`ReviewDisplayedApplicability` (the treatment one displayed record earned, with its true subject and the
exact references it was decided from), `ReviewContextRecord` (the labelled context row: true subject, the
recorded relationship that reached it, author/role and references, and no judgment content) and
`ReviewApplicabilitySummary` (one collection's six-way count) — and adds the optional `applicability`
field to the five display types that carry a supplied record. **565 → 618 lines.**

**Both new pane fields are optional, and the mirror keeps that.** A payload published before these
labels existed carries no `applicability`, no `context` and no `applicability` counts, and this client
renders it unchanged: absent means "this body states no label", never "this record is unrelated" and
never "nothing was filtered". The two mirrors therefore stay a faithful copy of the wire rather than a
normaliser that invents a default — the same rule the rest of this module follows.

**The vocabulary mirrors the model, not a rendering.** `state` is the closed four-member union of
*displayed* treatments (`direct`/`historical`/`candidate`/`unresolved`); `context` and `unrelated` are
deliberately not members, because a context record travels as its own value and an unrelated one is not
sent as a record at all — it appears only as the summary's own count.

## Update History
- 2026-09-23T02:40:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): **the client mirrors the applicability vocabulary and the optional labels (565 → 618 lines; `ICR-R26@v1`).** The card records the three new interfaces, the optional fields on the five display types and both panes, and the rule that an absent label is not an unrelated record. **Citation accounting:** the rows this leaf's insertions moved were re-derived from each interface's own extent in the 618-line candidate — `ReviewAuthoredEffect`/`ReviewSignal` `85-94`/`96-105`→`91-101`/`144-154`, `ReviewAssessmentDisplay` `107-117`→`156-167`, the three panes `119-135`/`201-215`/`287-295`→`169-190`/`256-265`/`344-354`, `ReviewEvidenceLink`/`ReviewObservation` (six one-line ranges)→`323-329`/`331-342`. Wording was retained where the claim still states what the code does. **Stamp accounting:** no verification stamp was advanced — the candidate is uncommitted, the header already names this leaf's base, and the governed closeout owns the real stamp.
