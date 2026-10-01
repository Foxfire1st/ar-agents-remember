# dashboard/src/data/review.ts

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

Since ICR-R31@v1 it is also the public entry for the **family half** of the review contract. That half
lives in its own mirror module, `data/reviewFamily.ts`, and this module **re-exports** it whole — the
five values (`FAMILY_CONTEXT_JOIN_KEY`, `FAMILY_SIDES`, `UNRESOLVED_SELECTION_STATES`,
`guaranteeComparison`, `memberComparison`) and the twenty-one types of its vocabulary — including the
member-source locator types `ReviewSourceLocator`, `ReviewSourceLineRange` and
`ReviewSourceLocatorState` added for ICR-R31@v1's per-side locators — so a consumer of
the review payload imports one public entry rather than two, the same rule the transport already
follows.

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

The client mirrors the server existing revision_selection and record channels. Central subject rendering can therefore preserve exact before/after selection and distinguish missing or unmeasured assessment channels from no returned assessment; this adds no browser revision or evidence authority.

**The module is one vocabulary of interfaces plus three request functions; there is no store, no
reducer and no hook.** It declares eight string-union types, thirty-three interfaces and three exported
functions, and on top of that declared vocabulary it re-exports the family mirror's five values and
twenty-one types (ICR-R31@v1). The absence of state is the point: the review surface owns its own
component state (`ReviewSurface.tsx`), exactly as the change-set viewer owns its component state, so
this module never appears in `data/store.ts` and no `useDashboard` selector reads it.

**`ReviewPagedCollection` names three bounded collections, and only two of them are walkable with no
cursor (ICR-R10, extended by ICR-R31@v1).** The union is
`"knowledge" | "records" | "family_members"` because the *server* accepts all three — narrowing it
would misdescribe the wire — and `REVIEW_PAGED_COLLECTIONS` lists all three.
`REVIEW_WALKABLE_COLLECTIONS` is the separate, smaller set a request may name with **no** cursor:
`family_members` is excluded because it is not one walk but the set of per-family roster walks a single
response composed, so naming it without a cursor addresses no single page and earns the server's own
`comparison_page_unreadable` refusal rather than serving an arbitrary walk's first page. Its walk is
reached instead by continuing `ReviewFamilyRosterPage.continuation` on the family that published it.
The two constants therefore answer two different questions — which collections the wire carries, and
which collections a control may offer as a first page — and neither is derivable from the other.

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
`ReviewPayload` carries `surface_version`, the `candidate`, the `comparison`, the optional
`family_context`, the three panes, the `staleness`, the `submission` and a `limitations` list.
**`family_context` is the one optional member whose absence is a fact of its own (ICR-R31@v1):** the
route composes one on every answer it returns — including the task-context review, which states
`no_subject_selected` — so a body without the key did not come from this route (a capture recorded
before the field existed, a hand-written body), and the client renders that as itself rather than as
`no_family_recorded`, which asserts that the recorded scope was read and held no family. `ReviewResult`
carries `state`
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

**The client gained the expansion's wire types and a third request, which opens one listed entry at the two generations the listing published.** `ReviewSourceSideState` is the closed six-member literal a side's `state` may be (`present`, `absent`, `binary`, `symlink`, `submodule`, `unavailable`), `ReviewSourceSide` carries that state with an optional `text` — present only for the two textual states, so a missing or unrenderable side can never arrive as an empty document — plus `detail`, optional `object_id`/`byte_length` and `truncated`, `ReviewSourceExpansion` carries the entry's `path`, `status`, `mode_change`, `language`, the two sides, both generation ids, the three-member `currentness` with its detail, `path_bound` (`requested_generation`/`leaf_change_set`) with its detail, `admission` (`ReviewSourceAdmission`: `changed`/`attributed_unchanged`) with its detail — added by 260921-ICR-L43 so the pane can label an unchanged file a recorded realization of the same comparison links without inferring it; such an expansion's `status` is the expansion-only `"unchanged"`, which is why the field is typed `ReviewFileStatus | "unchanged"` while the inventory keeps `ReviewFileStatus` — and the `reference`/`command`, and `ReviewSourceContentResult` is the envelope whose `state` is `"content"` with an optional `expansion` or `"refused"` with an optional `refusal`.

**`reviewSourceContent` no longer decodes its own body: it delegates to the one shared review decode.** A refused source read is a *normal* answer on this route — a path outside the measured change set, a baseline that is not this leaf's recorded one — and the transport carries it as the typed refusal in the body **with** a `400`/`404` status. That decode used to be inline here; ICR-R16 moved it into `data/reviewTransport.ts`, so this function is now a one-expression delegation to `getReviewJson<ReviewSourceContentResult>` over the same URL, and `grep -rn "api/review/intent" dashboard/src` finds the route URL only in the two review client modules. The behaviour a caller sees is unchanged for a typed answer and strictly better for everything else: a body that is not this route's answer now becomes a named `ReviewTransportError` failure carrying the owner's code, reason, offending input and next action — where the old inline decode built a `FilesApiError` from the response's status and the body's own `status` string and dropped the rest.

**The generation is an input here too, not a lookup.** `reviewSourceContent(repo, master, leaf, path, beforeCodeTreeId, afterCodeTreeId, base = "")` takes the two tree ids the inventory published to this client and sends them back with the request — in that camelCase spelling, which is the spelling the route binds — so the content a reader opens is the content of the generation they were looking at, never re-resolved from whatever the leaf holds by the time the request lands. The function resolves no path and no tree of its own, and its own comment states that boundary.

**The client gained the inventory's wire types and the three states that let a review exist without a subject.** `ReviewChangedFile` (the raw `path` exactly as Git recorded it — a tab or a newline inside it is part of the address — plus `status`, `content`, `mode_change` and an optional `detail`), `ReviewUnrepresentablePath` (`path_bytes`: the exact bytes in an ASCII-safe spelling, listed rather than dropped and never re-encoded) and `ReviewSourceInventory` (`state` `measured`/`unavailable`, the entries, `listed_total`, `detail`, `partial`, `command`, both tree ids and `unrepresentable_paths`), with `ReviewSourcePane.inventory` now required and first. `ComparisonIdentity` gained `knowledge_compared` and its three knowledge-half digests became optional, `ReviewKnowledgePane` gained `selection_state`/`selection_detail`, `ReviewStaleness.state` gained `not_compared`, and `ReviewPayload.comparison` became optional. `intentReview` sends **no selector parameters at all** when there is none, which is the task-context request; the same "a field the server omits is absent rather than defaulted" rule now covers an entire absent identity, and no fallback value was introduced for it.

### Conventions

The module imports `getReviewJson` from `./reviewTransport`, `qs` from `./files` and the
`ReviewFamilyContext` type from `./reviewFamily`, and declares everything else itself; the transport
surface (ICR-R16) and the family mirror (ICR-R31@v1) are **re-exported** rather than re-declared, so a
consumer of either has one import. Interfaces are exported and named with the `Review`/`Comparison`
prefix so a
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
  because the server may not send it, and no fallback value is provided. `ReviewPayload.family_context`
  is the member this rule is load-bearing for: the route composes one on every answer it returns, so an
  absent key means the body did not come from this route, and it is never rendered as
  `no_family_recorded`, which would assert that a measured scope held no family.
- **A collection may be named with no cursor only when it has a first page.** `REVIEW_WALKABLE_COLLECTIONS`
  is that set — `knowledge` and `records` — while `family_members` is a member of the wire union and not
  of it: it is a set of per-family walks, so a cursor-less request for it earns the server's
  `comparison_page_unreadable` and its walk is continued from the roster page that published the cursor.
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own header and its two
stated rules, the two unions and the interfaces that mirror the server's models, the three request
functions and the helper each one borrows from the file API, and the clients that consume it. Every row
was re-derived against this candidate — this leaf's expansion types and third request moved every
construct below the source pane — and every anchor in a row occurs inside the range that row cites.

- The header's own statement of what this file mirrors, the rule that a field the server omits is absent rather than defaulted, and the second model module the expansion types mirror. [1]
- **The family mirror's re-export: five values and twenty-one types, including the three member-source locator types.** [2]
- The two client-side unions, each mirroring a server literal. [3]
- **The missing-side rule on the client: text is optional beside the state, so no empty string is manufactured.** [4]
- The shared shape that makes an unresolved reference a displayed fact on every surface that can have one. [5]
- The candidate reference, which carries task identities and no path, and the comparison identity carried rather than derived. [6]
- The per-side revision count and the field transition whose absent value is the recorded fact. [7]
- The authored record with its examined inputs, and the detection fact with its versions and scope limitations and no severity. [8]
- The assessment display with its author, examined inputs, binding state and evidence refs. [9]
- The three panes, each carrying its own `unresolved` rows. [10]
- The selected source location with its optional role and its three-member change state. [11]
- **The count shape whose optional value beside its optional reason is how a quantity with no meaning states why rather than reporting a zero.** [12]
- The evidence claim reference and the observation displayed exactly. [13]
- **The two display unions with no favourable member.** [14]
- The whole payload — including the optional `family_context` whose absence is a fact of its own — and the two response shapes. [15]
- **The comparison request: a task context, one recorded subject and a same-origin default, with no path.** [16]
- **The reviewed subject as the server selected it — the entry's only legitimate selector source, with no path field on purpose.** [17]
- **The entry read's response envelope: a refused read is a typed outcome carrying its refusal and no entries, not an error to catch.** [18]
- **The entry request: the task context alone, because a selector is what it is being asked for, and the same same-origin default as the comparison.** [19]
- **The six-member state literal a side may be, and the side value whose optional `text` is present only for the two textual states — so no missing or unrenderable side can arrive as an empty document.** [20]
- **The expansion value: both sides, both generation ids, the three-member currentness, `path_bound` naming which measured change set bounded the path, and `admission` naming why it was opened (a changed path, or unchanged context a recorded realization of the same comparison links).** [21]
- **The source-content envelope whose two states are the two answers this route gives, a refusal being a normal one.** [22]
- **The source-content request: the task context, the published path and both published generation ids, read through the route's own decode because the body is this route's answer whatever the status was.** [23]
- **The error idiom this route deliberately steps outside of: `getJson` throws on a non-OK status, while a refused source read arrives with a typed refusal in the body.** [24]
- The sibling client whose shape this file mirrors, including its own no-store-mutation comment. [25]
- The surface that consumes this client: the comparison read, and the entry expansion an openable inventory row mounts. [26]
- **The catalogue consumer: since `260921-ICR-L47` the reviewer (not the task entry) reads this client's subject catalogue when it opens, keyed on the comparison's identity; the task entry reads the changed-intent summary instead, and a refused or empty catalogue still leaves the task-context review available.** [27]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The client talks to its own origin and names
one repository namespace in the query string.

No meaningful cross-repo references found.

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

**ICR-R31@v1 adds the third member and the walkable subset.** `ReviewPagedCollection` is now
`"knowledge" | "records" | "family_members"` and `REVIEW_PAGED_COLLECTIONS` lists all three, because
the *server* accepts all three — narrowing the union would misdescribe the wire.
`REVIEW_WALKABLE_COLLECTIONS` is the separate two-member set a request may name with **no** cursor, and
it is the set the collection picker offers. `family_members` is not one walk but the set of per-family
roster walks a response composed, so naming it without a cursor addresses no single page and fetches the
server's own `comparison_page_unreadable` refusal rather than an arbitrary walk's first page; its walk
is continued from `ReviewFamilyRosterPage.continuation` on the family that published it, and a response
whose page is `family_members` still renders through the same bounds and continuation controls as any
other.

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

## 260921-ICR-L12 The Client Appends The Record Only When It Was Named

`260921-ICR-L12` (`ICR-R12@v1`) adds one type and one optional argument to this client:

- `export type ReviewHistory = "recorded"` carries the **one** value the server admits, so a client
  cannot ask for a generation that is not this leaf's and the mirror cannot drift from the request
  model's own literal.
- `intentReview(..., history?: ReviewHistory)` appends `params.history` **only when it is defined**, so
  the live read's query string is byte-identical to the one every existing caller already builds — a
  property the mounted case for the live read pins by asserting the absence of the parameter.

The record is part of the question the surface asks, not a decoration on the answer it renders, which
is why it is a parameter of the read rather than a field applied to the result.

## 260921-ICR-L17 The Client Builds One Query String And Names The Refresh Parameter Once

`260921-ICR-L17` (`ICR-R17@v1`) gives `intentReview` a ninth argument and moves the query string into
its own function.

**The ninth argument.** `previousBindingDigest?: string` is the comparison the reader was already
looking at — the `binding_digest` the displayed payload published — carried only by a read that is
**replacing** a display rather than making a first one. The response compares it against the comparison
it rendered, so a candidate that moved while the panel stayed open arrives as the `stale` state with the
previous identity labelled instead of silently passing as the same generation. The comment above the
function states what it is not as well: it is the *previous* identity and never a substitute for the
current one, the read still renders the resolved candidate's own comparison, and a caller cannot use it
to choose a dataset.

**`reviewQuery` is why the function is a function.** The branch-per-parameter assembly moved out of
`intentReview` into one helper, for two reasons the comment gives: adding a parameter can no longer
quietly raise the client's branch count, and the two spellings of "absent" — `undefined` and the empty
string a form sends — are collapsed once, so neither reaches the server.

**`PREVIOUS_BINDING_QUERY` is the one spelling of the wire name.** It is declared once because the
server's admission reads the parameter by that exact name (`serving/review.py`, alias
`previousBindingDigest`), and a second spelling at a call site is how a refresh silently stops carrying
the identity it is measured against. `reviewQuery` is its only reader.


## 260921-ICR-L23 The Raw-Git Boundary's Fourth Staleness State

`ReviewStaleness.state` gains `"not-measured"` beside `"current" | "stale" | "not_compared"`
(`:357-363`). It is the state the raw-Git identity boundary reports when it could not take its
comparison **at all** — a checkout that left its declared branch, a recorded object that is gone,
a generation that could not be read — so this client may not present the displayed comparison as
the candidate's current one. It is deliberately not `stale`: nothing was observed to move, and
`stale` additionally disables submission, a consequence an unperformed comparison has not earned.
The line comment above the union carries that reasoning so the next reader of the type does not
have to reconstruct it from the server.

The change is one member and one comment: no other field of `ReviewStaleness` moves, and the
`moved` list stays empty for this state because there is no replaced identity to name.
