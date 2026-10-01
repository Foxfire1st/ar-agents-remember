# mcp/src/agents_remember/mcp/tools/knowledge.py

## Governing Overview

[mcp/tools route overview](overview.md)

## Purpose

The payload builders for the five mounted `knowledge_*` operation families — one builder per operation, each of which "validates its wire request, delegates to the application seam that owns the operation, and returns the typed shape the response model declares". Its docstring states the property that defines the whole module: "**Nothing here decides anything**: no classification is computed, no effect label is inferred, no draft is authored, no rationale is judged, no ambiguity is resolved by choosing, no missing assessment is filled, and no compatibility verdict is produced. Where a handler would have to decide something, it returns the unresolved state instead." **It deliberately has no renderer of its own, no detection logic, no diff algorithm and no projection writer**: each of those belongs to a seam it calls, and the two requirement-level cases its docstring singles out are why it stays short — `knowledge_read` "returns recorded claims and assessments as attributed records" and the payload it returns "is the view payload itself, so the classification rule has exactly one implementation", while `knowledge_diff` includes "semantic effect labels ... only when supplied by an identified agent/assessment, not inferred from the diff".

## Code Commentary

### Logic

**Five builders, one per mounted operation family, and every one of them delegates rather than implements.** `knowledge_read_payload` validates the view name against the five named views, resolves the read context through `open_read_context` and returns what `read_knowledge_view` produced; `knowledge_change_payload` records through the admitted write operation for its kind; `knowledge_diff_payload` calls `diff_knowledge_scope`; `knowledge_integrity_check_payload` reads recorded detection conditions; `knowledge_project_payload` builds a `DestinationProfile` and calls `project_knowledge`. No builder contains a comparison, a classification, a rendering or a filesystem write, so the diff engine, the view renderer and the projection writer each keep exactly one implementation.

**A caller's `databasePath` may name a converted memory tree (MIK-R23 rule 6).** The read, diff and project builders pass every caller-selected dataset path through `_select`, which calls the application route's `select_knowledge_dataset` with the coordination root the registration hands over. A path naming a converted memory tree — its root, or the published `<memory-root>/knowledge.sqlite` location inside it — is read through the derived index of that tree's current state (the index file is a dataset of the store's schema, so the same seams open it); any other path is opened exactly as before, so an unconverted tree keeps today's database path and refusals. The builders then add `memoryTree` (`memoryTrees` with `before`/`after` for a comparison) and `indexComplete` beside their existing fields; both are absent for a database. `_index_complete` is `false` when any side came from a `partial` index, and the read also forces `completeWithinDeclaredScope` and the payload's own `completeness.complete_within_declared_scope` to `false` then — the view is complete only within what the index holds. The comparison's own `has_more`/`enumeration_complete` pair is not changed, because its model requires them to stay opposites. `_SELECTION_FAILURES` (`MemoryTreeError`, `GitPreparationError`, `KnowledgeStorageError`, `apsw.Error`, `OSError`) is shared by the three handlers, and `_selection_refusal` maps a tree or Git failure to `snapshot_unavailable` naming the tree and everything else to the existing dataset refusal, so an index that cannot be built is refused, never raised. A tree-backed read is bound to the index's constant namespace (`INDEX_REPOSITORY_ID`): a caller passing an old database UUID gets the existing namespace-mismatch refusal, and seeds are the projected UUIDs.

**Where a handler would have to decide, it returns the unresolved state instead.** `knowledge_read_payload` refuses a view outside `source_context`, `invariant`, `family`, `review_matrix` and `curation_queue` through `_refused_read(view, repositoryId, "unknown_view", ...)` rather than picking a default view; a read the seam refused is returned as its typed refusal rather than as an empty page. `knowledge_integrity_check_payload` returns `"compatible": None` **present** beside `"unresolved": conditions["unresolved"]`, which is the difference between reporting conditions and manufacturing a verdict from a passing test — computing `true` from a detection's silence would be the semantic conclusion this leaf forbids. `_no_detection_run(scope_id)` is the honest special case of the same rule: no recorded run yields no conditions, a stated limitation and a named unresolved item, never an empty-list success.

**The declared write kinds name what the surface may be asked for, and every one of them is refused by name.** `DECLARED_CHANGE_KINDS` is `("evidence_claim", "verification_observation", "invariant_revision", "assumption", "semantic_change_set", "requirement_revision")` — the record kinds this mounted surface is asked about — and the module comment records why the vocabulary is *declared* rather than *admitted*: "The earlier spelling advertised two 'admitted' kinds and then refused both anyway, which made the tool's own description false and told the caller to supply an input its published signature cannot carry. Both are removed: the set below is what the surface may be *asked* for, the refusal is unconditional for every member of it, and the reason names where the write actually happens." `knowledge_change_payload` therefore has exactly **one** branch and it refuses every kind — declared here or never heard of — with the shipped `registration_absent` code and a detail naming where the write actually happens: the write plane has **one writer**, and the refusal now names **both** shipped CLI entry points that reach it — `WRITE_ENTRY_POINT`, the `agents-remember knowledge-ingest` subcommand for a leaf enclosure's ordinary route, beside `TASKLESS_WRITE_ENTRY_POINT`, the `agents-remember knowledge-bootstrap` subcommand for a repository with no enclosure in scope. **That two-name form is `260921-ICR-L32`'s correction of the singular framing `260921-ICR-L20` landed when only one reachable entry point existed** — the sentence was completed rather than deleted, which is the whole point of D55's memory consequence; at L20's bytes "the reachable entry point is the `knowledge-ingest` subcommand" was true, and it stopped being complete when `ICR-R29@v1` shipped the second. The module comment 20 lines above now states the same two names, so the file no longer contradicts itself. The reason is deliberately the same for both cases, because "two spellings of 'this tool does not write' would suggest the first one might". This module never invents a write seam for a kind another leaf owns, and it reports no missing destination facts for a write that does not exist here. **Since `260928-MIK-L12` the refusal detail adds one sentence:** on a converted memory tree (`knowledge/layout.json`) both entry points write knowledge files through the curator file writer (MIK-R12) instead of the database. The tool stays registered and refusing (architect ruling 3; its removal is MIK-R26's).

**`knowledge_read` returns the view payload itself, which is what keeps the classification rule single-sourced.** `_view_request(request)` rebuilds one `ViewRequest` from the flat tool arguments — including `source_path`, the optional path seed the published signature carries — and reconstructs a continuation token opaquely — its docstring is explicit that "its snapshot binding is checked by the seam against the snapshot the dataset actually declares, so this builder never guesses one" — and the success branch returns `"payload": payload.model_dump(mode="json")` beside the echoed `view`, `snapshot` and `completeWithinDeclaredScope`. No reshape, no re-render and no second classification path exists here; requirement 6.8's "not a second shape" holds because there is no second shape to violate it. The four request value objects `ReadToolRequest`, `ChangeToolRequest`, `DiffToolRequest` and `ProjectToolRequest` exist so the builders are one argument wide while the published FastMCP signature stays flat.

**The knowledge selection is the caller's, and this module now says so where the caller meets it rather than leaving it to be inferred.** `ReadToolRequest`'s docstring records what owns `database_path` and `repository_id`: the pair **is** the *selection*, the caller owns both, and nothing this server holds can answer either one — the runtime config's per-repository scope carries no knowledge-database or namespace field, a repository's coordination declaration (`context_packet`, and the memory layer's `system/settings.json`) names the code root, the memory root and the coordination paths and never a knowledge database, namespace or `repositoryId`, no shipped helper or filename convention resolves a repository or a task to a knowledge SQLite path (`knowledge.db` appears only in test support), and the namespace is minted by ingestion (`create_repository`), so it is a fact about a store that already exists rather than something derivable from a repository name. The published schema therefore keeps the pair **required** rather than optional-with-a-default: a default here would be this surface inventing a selection. A cold planner that has not been told the pair cannot discover it from this server; it is supplied by the party that created or holds the dataset, exactly as `databasePath` is supplied to every other `knowledge_*` operation. Exposing a real discovery contract — a settings key, a `context_packet` field, a resolver — is a product decision and is deliberately **not** taken here; what the module does is state the boundary, so "supplied" is never read as "discovered".

**`knowledge_diff` carries only labels an identified agent or assessment supplied.** `_supplied_effect_labels(request)` reads the caller's own body, accepts both the snake-case and camel-case spelling of the list, and appends an entry only when it is a dict carrying `supplied_by` — an unlabelled diff therefore returns `"semanticEffectLabels": []` rather than a derived guess. `_diff_request(repository_id, request)` then validates the shipped `KnowledgeDiffRequest` from that same caller body with the namespace injected, and a refused comparison returns its refusal fields with no payload, so "the label was not supplied" and "the comparison was refused" stay distinguishable states.

**The integrity check reports recorded conditions and their observable limits, and produces no verdict.**
`_recorded_conditions(database_path, repository_id, scope_id, selector=…)` opens the dataset read-only,
selects the namespace's recorded `detection_run` rows in record-id order and closes the connection in a
`finally`; with no rows it returns `_no_detection_run`. With rows it hands them to `_run_for_scope`,
because **the requested scope SELECTS the run instead of being echoed beside one**: when a scope is named
a run measured over a different scope is not a weaker answer but the wrong one, so the search continues
over `run.governing_route_id` and a namespace with no matching run is told so by `_no_run_for_scope` —
a stated limitation and a named unresolved item, never another run's conditions under the requested
scope's name. With a run selected it builds an `OpenedKnowledgeStore` over the same connection and reads
through `read_detection_run`, and `_condition_report(result, scope_id, selector, matching_runs)` maps the
result's signals to one `{"code": signal.condition, "matched_facts": [signal.detail]}` entry each, carries
`result.run.limitations` through verbatim, and sets `unresolved` to `["no condition matched the recorded
scope"]` when nothing matched. A run that could not be read yields `"the recorded detection run could not
be read"` as its limitation and the refusal detail as its unresolved item — again a report and not a
status.

**Scope selects, and exact inputs BIND: the caller's `runId` or `inputDigest` picks one run out of
several instead of the report silently choosing the first identity-sorted match.** `_ExactInputSelector`
is the caller's two spellings of one request as one frozen value — "report the run with this identity",
"report the run measured over these inputs" — and `as_wire()` echoes them as `{"runId": …, "inputDigest":
…}` or `None`, because a pair of `None`s is a fact worth reporting: it says the run was selected by scope
alone and that `matchingRunIds` is where a narrower request would come from. `_run_for_scope` applies the
selector as a **binding** and not a preference — a run whose recorded identity or
`detection_input_digest` does not match is a different execution, so the search continues past it and a
request that names inputs nothing was measured over reports no run rather than the first one sharing a
scope. `_runs_in_scope` and `_run_identity` then answer the other half of the same question: every run
the requested scope holds, each named with its own `runId`, its `governingRouteId` and the digest over its
inputs, so a caller that received one match can see it was one of several and issue an exact request from
the response it already has. `_report_facts` is the one composition every non-success answer goes through
— no run recorded, no run matching, or a run that could not be read — so `selectedRunId`, `inputDigest`
and `inputIdentities` are honestly empty in exactly those cases and `exactInputSelector` still names what
was asked for. The selected run's own `governing_route_id`, not the caller's string, is what the report
echoes as its `scope`, which is why a report cannot claim a scope the run it read was not bound to.

**The read context's source-resolution pair is completed rather than half-supplied, and the mount hands
over a default repository rather than half a pair.** `_source_resolution(request, workspace_root)`
returns `(repository_root, code_tree_id)` and never one without the other: a caller who named both gets
both back untouched, a caller who named a root gets that root's own current tree from
`_current_code_tree` (since 260928-MIK-L01, a named root with no tree is refused by name, below), and a
caller who named neither gets the mount's workspace default **only when a tree can actually be resolved
from it**. `_current_code_tree` shells `git -C <root> rev-parse
HEAD^{tree}` under `_GIT_TIMEOUT_SECONDS`, validates the answer against `_TREE_ID_PATTERN` and returns
`None` — never a guess — when the root is not a repository, Git is absent, Git does not answer in time,
or the answer is not a tree id; the context is then built with neither half. This is what the registration
hands over as `workspace_root=`, and it is why a minimal schema-conformant `knowledge_read` returns a
view instead of a raw `KnowledgeReadContext` validation error.

**The project builder names views and identities, and refuses before it renders.** `_projection_requests(repository_id, views)` turns each caller-named input into one `(ViewRequest, subject)` pair, defaulting the subject to the view name, because the identity is what the artifact records and the manifest tracks. An empty request set is refused by `_refused_project(destinationRoot, "unresolved_projection_input", "no view was named to project, so no artifact is emitted")` before any writer is constructed, and a refused report is relayed through the same helper, so both refusal routes carry the destination root and the renderer version. The success branch reports per-path outcomes — `published` for outcomes in `published` or `unchanged`, plus `retained` and `discrepancies` verbatim — and returns the data; the file writing happened inside the projection writer, not here.

### Conventions

Request shapes are frozen dataclasses rather than loose dictionaries, so a builder's argument list is one value wide while the published tool signature stays flat and FastMCP keeps deriving the wire schema from it. Bounded vocabularies are module constants that the refusal messages quote: `DECLARED_CHANGE_KINDS` is declared once and refused wholesale by the builder, `WRITE_ENTRY_POINT` is "kept as a constant because two detail strings and a test quote it", and the five admitted view names appear as the literal tuple the read builder checks against. Where a vocabulary belongs to another module it is imported rather than restated — `ProjectionOptions` and `project_knowledge` from the projection operation, `VIEW_RENDERER_VERSION` and `read_knowledge_view` from the views seam, `diff_knowledge_scope` from the diff seam, `DestinationProfile` from the projection-manifest vocabulary, `KnowledgeDiffRequest` and `ViewRequest`/`ViewContinuation` from the models — so this module adds no sixth spelling of a name another leaf owns. `__all__` exports exactly the four request dataclasses and the five builder functions, keeping `_refused_read`, `_view_request`, `_diff_request`, `_supplied_effect_labels`, `_recorded_conditions`, `_run_for_scope`, `_no_run_for_scope`, `_no_detection_run`, `_condition_report`, `_projection_requests` and `_refused_project` module-local. Every private helper that can fail does so by returning a state the caller can read — a `refused` dict, an unresolved list, an empty label list — rather than by raising, so a refusal crosses the wire as a first-class result.

### Invariants And Boundaries

- **No builder decides anything.** No classification is computed, no effect label inferred, no draft authored, no rationale judged, no ambiguity resolved by choosing, no missing assessment filled and no compatibility verdict produced anywhere in the module.
- **A kind without an admitted write operation is refused as `registration_absent`.** `DECLARED_CHANGE_KINDS` holds exactly `evidence_claim`, `verification_observation`, `invariant_revision`, `assumption`, `semantic_change_set` and `requirement_revision`, and `knowledge_change_payload` has one unconditional refusal branch that returns that code with a detail naming what is missing — the entry point that can write, `WRITE_ENTRY_POINT`.
- **`compatible` is `None` and present, never computed.** `knowledge_integrity_check_payload` reports conditions, traversal scope, limitations and an explicit `unresolved` list, and derives no status from the absence of a matched condition.
- **The read payload is the view payload.** The success branch dumps the seam's own payload; no second renderer, filter or classification exists in this module for requirement 6.8 to be violated by.
- **A continuation is carried opaquely.** `_view_request` mints a token whose snapshot binding the seam re-checks; the builder never resolves or guesses a snapshot binding.
- **Effect labels are only what an identified source supplied.** `_supplied_effect_labels` requires a `supplied_by` on each accepted entry and returns an empty list otherwise; nothing is inferred from the change.
- **An empty projection request set writes nothing.** `knowledge_project_payload` returns the `unresolved_projection_input` refusal before the writer is constructed.
- **An unconverted selection reads exactly as before.** A path that names no converted memory tree is opened unchanged: no `memoryTree`, no `indexComplete` and no cache directory appear.
- **A partial index is never presented as complete.** Every surface that states completeness is forced to `false` by a partial index, and `indexComplete` says so on read, diff and project.
- **This module opens no write path of its own.** It reads through the shipped read-only connection and writes only by delegating to the projection writer; `_recorded_conditions` closes its connection in a `finally`.
- **An unreadable recorded run is reported, not defaulted.** `_condition_report`'s refusal branch returns a stated limitation and an unresolved item instead of an empty success.
- **The requested scope selects the detection run; it is never just echoed.** `_run_for_scope` matches the
  caller's scope against the registered traversal scope the run itself records (`governing_route_id`) and
  keeps searching past a run measured over another one; a caller naming no scope still gets the first
  recorded run, and a caller whose scope matches no run gets `_no_run_for_scope`'s limitation and
  unresolved item rather than a different run's conditions reported under the requested scope's name.
- **An exact input selector binds; it is not a hint.** A caller-supplied `runId` or `inputDigest` is
  applied inside the scope and never across it: a run whose identity or input digest does not match is
  skipped and the search continues, so a request naming inputs nothing was measured over reports **no**
  run — with `matchingRunIds` still naming the runs the scope does hold — rather than the first
  identity-sorted match. A `runId` belonging to another scope selects nothing and the scope is not
  borrowed.
- **A reported run is named, with the digest over its exact inputs.** `_condition_report` carries
  `selectedRunId`, `inputDigest` and the `inputIdentities` value beside the conditions, so conditions
  cannot be read as belonging to a run they were not measured over; `_report_facts` is the single
  composition the three non-success answers share, and it leaves those three fields honestly empty while
  still echoing `exactInputSelector`. The echoed `scope` is the selected run's own
  `governing_route_id`, never the caller's string.
- **A source-resolution pair is named as a pair or not at all.** `_source_resolution` never returns a
  root without a tree or a tree without a root: a caller-named root is completed with that root's own
  current tree, the mount's workspace default is named only when a tree can be resolved from it, and
  since 260928-MIK-L01 a caller-named root Git cannot answer for (no commit, or not a repository) is
  refused `selected_input_unavailable` naming the root, rather than passed on as half a pair. `_current_code_tree` returns `None` — never a
  guess — for a root that is not a repository, an absent Git, a timeout or an answer that is not a tree
  id, so a minimal read reaches the context as "no source resolution was requested" instead of as a
  raised validation error out of the mounted tool.
- **The knowledge selection is the caller's, and this surface resolves neither half of it.** (Since MIK-R23 a `database_path` that names a converted memory tree is *read through* that tree's derived index, but the caller still names the tree; nothing here chooses one.) `database_path`
  and `repository_id` are required by the published schema with no default, because nothing this server
  holds can derive either one: the runtime config's per-repository scope is
  `repo_id`/`path`/`memory_root`/`contract_path`/`certification_profile`, the coordination declaration and
  the memory layer's `system/settings.json` name roots, paths and policy but no knowledge database or
  namespace, no shipped helper or filename convention resolves a repository or a task to a knowledge SQLite
  path, and the repository namespace is minted by ingestion (`create_repository`), so it is a fact about a
  store that already exists. `ReadToolRequest`'s docstring records that boundary where a caller meets it, so
  a supplied pair is never read as a discovered one. A discovery contract of its own (a settings key, a
  `context_packet` field, a resolver) is a product decision and does not exist here.
- **A projection never renders a seed a converted tree does not hold as an empty view (L37, P2 task 4).**
  `_project_result` takes its dataset from `_projection_selection`, which selects the dataset and then asks
  `_tree_seeds_absent`: for a converted tree, the first view whose `invariantRevisionId` or `familyRevisionId`
  the tree does not hold (`tree_seeds.tree_seed_refusal`) refuses the whole projection as `selector_absent`,
  naming where current seeds come from. `knowledge_read` gets the same refusal from
  `knowledge_paging/tree_read`. A database selection (no `memory_tree`) is unchanged.

## 260928-MIK-L28 Proofs Beside The Invariant And Family Views (MIK-R28 Rule 4)

`_read_result` now adds `proofs` to a read's result. Inside the existing selection-failure boundary, and
only when the selection is a converted memory tree and the view was not refused, it calls
`application/knowledge_proofs.tree_view_proofs` with the tree's index path and key. That function opens the
index only for the `invariant` and `family` views; every other view, and every database read, gets
`proofs: None`, which the response model omits.

- **The additive optional `proofs` field is accepted (architect ruling, 2026-09-29).** Database reads never
  carry it, so a caller of today's installed runtime sees byte-identical output.
- `IndexMismatchError` joined `_SELECTION_FAILURES`, so an index opened for the wrong tree key becomes the
  ordinary dataset refusal through `_selection_refusal`, not a raised error.
- A proof states what its test demonstrates, never that the test passed or that the invariant holds
  (MIK-R28 exclusions; Doc13).

- The read adds `proofs` only for a converted memory tree's page, prepared once per page since MIK-R02. [1]
- A key mismatch joins the selection failures. [2]
- Invariant and family views of a tree carry their proofs; no pass or result key exists. [3]
- A database read and the other views carry no `proofs`. [4]

## 260928-MIK-L08 The Integrity Check Returns A Leaf's Worklist (MIK-R08 Rule 7)

`knowledge_integrity_check_payload` now takes one `IntegrityCheckRequest` (the registered tool's six flat
inputs as one frozen value) instead of five keyword arguments, and accepts a new optional `contractPath`:

- **A dataset** (`databasePath` with `repositoryId`) is reported exactly as before through
  `_integrity_check_result`.
- **A leaf alone** (`contractPath` without `databasePath`) gives a `reported` result with no conditions.
- **Neither** is refused with `refusalCode: selected_input_unavailable`, naming the three accepted forms.
- Whenever `contractPath` is named, the result is extended with `application/knowledge_worklist/surface`'s
  `leaf_worklist_fields`: `worklistState` (`present`, `absent` or `unreadable`) and `worklist` (the
  summary, the owner, one `{id, kind, subject}` row per item, and the persisted file's path for the full
  facts).
- The builder computes nothing: the worklist is the one the leaf's last memory-quality run or completed
  managed sync persisted beside its series contract. The contract path is read as given (read-only).
- `databasePath` and `repositoryId` are optional **for this tool only**; the read request's pair stays
  required, as `ReadToolRequest`'s docstring states. MIK-R26 reshapes this tool later.

- The integrity check's request value. [5]
- Dataset, leaf, both or neither; the leaf's worklist fields added when a contract is named. [6]
- The worklist fields read from the persisted file. [7]
- The tool returns the latest worklist. [8]

## 260928-MIK-L03 Currentness Beside The View (MIK-R03)

`_read_result` now adds `currentness` to a read's result when the selection is a converted memory tree and
the view was not refused. Since MIK-R02 (260928-MIK-L02) it is computed by `_tree_extras`, once per page, through
`knowledge_paging.currentness.WalkCurrentness` at the walk's code tree, and it counts toward the page's
threshold; the rules below are L03's and are unchanged. A database read carries no `currentness` key.

- **Only `codeTreeId` is a request (architect ruling 2, 2026-09-29T18:42:37).** A `repositoryRoot` alone,
  or nothing, gives an `unverifiable` block with compact entries; `HEAD` is never substituted. (The view
  context still completes its own source pair from `HEAD` for the blob-level `anchor_state` it already
  reported; that is untouched.) A `codeTreeId` named without `repositoryRoot` is read from the mount's
  workspace object store.
- **A currentness failure never refuses the read (ruling N2, 19:13:41).** The block is computed after the
  `_SELECTION_FAILURES` boundary, and `read_currentness` degrades every index, SQLite, file-system or Git
  failure to `unverifiableReason`, so the view is still answered.
- **The payload is not edited,** so a stale invariant stays visible with its statement and relationships.

- A converted tree's page carries `currentness` at the walk's code tree, computed once per page beside its proofs. [9]
- A named tree flags the stale invariant and keeps it visible. [10]
- Without `codeTreeId` it is unverifiable and never reads `HEAD`. [11]
- A failing step never refuses the view. [12]

## 260928-MIK-L02 A Converted Tree's Read Is A Bounded Page (MIK-R02)

`_read_result` hands a converted memory tree's read to `application/knowledge_paging/tree_read.read_tree_page`
right after the selection (a two-line seam), so every such response is a page cut to the shared token
threshold, and its `continuation` is the shared token that also resumes the published-intent block's walks.
The database path keeps its own view read and `limit`, and no longer carries the tree-only fields
(`memoryTree`, `indexComplete`, `proofs`, `currentness`), which were always absent there; the worker and both
review rounds measured unconverted reads byte-identical to base.

- **`_tree_extras(selected)`** is a per-page factory `(subject, walk code tree, candidate rows) -> (payload ->
  extras)`: it computes `proofs` (MIK-R28) and `WalkCurrentness` (MIK-R03) once, and returns each candidate
  page's additions, so both count toward the threshold (architect ruling F3, 2026-09-29 20:40:40).
- **`_ordering(request)`** applies `DEFAULT_ORDERING` only when `ordering_input` is `None`; an empty string
  keeps the base refusal `unadmitted_ordering_input` on every path (rulings Q5 of 19:56:40 and F1 of 20:40:40).
  `ReadToolRequest.ordering_input` now defaults to `None`.
- **`knowledge_read_payload`** adds `threshold` to every refusal of a converted-tree selection (unknown view,
  ordering, selection failure), because every response states the threshold (ruling F8). Database refusals
  are unchanged.
- The view-request refusal now flows through a refused `ViewResult`, which keeps the function within PLR0911.

- A converted tree's read is handed to the paged tree read right after the selection. [13]
- The default ordering, applied only when the caller named none. [14]
- A converted-tree refusal states the threshold; a database refusal does not. [15]
- The paged tree read this module hands a converted selection to. [16]

## 260928-MIK-L01 The Family-Complete Leaf Read, And A Root With No Commit Refused By Name (MIK-R01)

The tool reaches the family-complete leaf read through `knowledge_paging.tree_read` (a converted tree's
`source_context` read with `sourcePath`, and every `leaf` continuation); nothing in `_read_result` changed
for it. This module changes in two places.

- **A root with no commit is refused by name (the obligation carried from L02, 2026-09-29 21:17:07).**
  Before L01 a `repositoryRoot` naming a repository with no commit raised a pydantic `ValidationError` out of
  `open_read_context`. `_source_resolution` now raises `_NoCodeTreeError` when a caller-named root resolves
  no tree (no commit, or not a Git repository); it is the first member of `_SELECTION_FAILURES`, and
  `_selection_refusal` answers it `selected_input_unavailable` with a detail naming the root and the three
  ways out (a repository with a commit, `codeTreeId`, or no `repositoryRoot`). The fix applies to database
  and tree reads alike (review R1 N7: intended, and not a preservation regression, because base crashed on
  that input). The workspace default is unchanged: with no root named, a workspace without a tree still
  leaves the pair unrequested.
- **A converted tree is projected whole (the obligation carried from L02 Q7, ruling 2026-09-29 23:21:57).**
  `_project_result` passes `ProjectionOptions(whole_views=selected.memory_tree is not None)`, so a
  converted tree's view is projected with every row rather than its first 64-row slice; a database
  projection is unchanged (`application/knowledge_projection.py`).
- **Refusals name the memory tree (rule 9, ruling N3 of 2026-09-30 00:08:39)** in `tree_read._refused`, for
  every refusal after the selection; the tree-selection refusals of this module state the threshold as
  before.

- A named root that resolves no code tree is its own error, refused `selected_input_unavailable` naming the root. [17]
- `_source_resolution` raises it for a caller-named root without a tree. [18]
- The projection of a converted tree reads each view whole. [19]
- The leaf read the tree read routes a `source_context` path read to (and, since MIK-R05, a read naming only `familyRevisionId`, as a family seed). [20]

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The module's own statement that nothing here decides anything, the list of decisions it refuses to make, and the unresolved-state rule that replaces them. [21]
- The public surface as the export list now reads it: five request value objects (the integrity check's own request value joined the four in MIK-R08) and the five payload builders, one per mounted operation family. [22]
- The declared set of record kinds this surface may be *asked for*, with the reason a kind outside it is refused rather than written by a second path -- and note the refusal is unconditional for every member, because this surface has no admitted write operation for any kind. [23]
- The flat read request as one frozen value: the continuation, the two revision selectors, the optional source roots, and an ordering left `None` unless the caller names one. [24]
- The closed set of record kinds this surface may be asked about, the unconditional refusal every one of them earns, and the constant naming the entry point that can actually write. [25]
- The flat read request's optional source-path seed, beside the unnamed-by-default ordering MIK-R02 introduced. [26]
- The boundary this surface cannot cross, stated where the caller meets it: the pair is the selection and the caller owns both, nothing the server holds can answer either one, and the schema keeps both required so a default cannot become an invented selection. [27]
- The change, diff and project request values, including the per-path overwrite authorization the projection operation consumes. [28]
- The one refusal envelope the read operation returns for an unknown view and for a view the seam refused. [29]
- The one refusal envelope the read operation returns for an unknown view and for a view the seam refused. [30]
- The read builder: the five-view closure, the shared dataset selection (a converted memory tree reads through its index), the resolver call, the seam call, and the payload returned as the view payload itself — with every completeness statement forced to `false` when that index is partial. [31]
- The validated view request with its continuation reconstructed opaquely, its snapshot binding left to the seam. [32]
- The record builder and its one `registration_absent` refusal, deliberately the same reason for a declared kind and for one this surface has never heard of -- the surface has nothing to add in either case, so the refusal names the entry point that owns the write. [33]
- The source-resolution pair completed rather than half-supplied: the caller's own root with its current tree (refused by name when it has none, since MIK-R01), the mount's workspace default used only when a tree can be resolved from it, and neither half when Git cannot answer for it. [34]
- The validated view request with its continuation reconstructed opaquely and its source-path seed forwarded, its snapshot binding left to the seam. [35]
- The record builder and its unconditional `registration_absent` refusal, naming the subcommand that owns the write and reporting no missing destination for a write this surface cannot make. [36]
- The record builder and its unconditional `registration_absent` refusal, naming the subcommand that owns the write and reporting no missing destination for a write this surface cannot make. [37]
- The integrity builder that returns `compatible: None` present beside its explicit unresolved list, and the recorded-conditions read with its connection closed in a `finally`. [38]
- The comparison builder's one body (behind the thin public `knowledge_diff_payload` wrapper), which resolves each side's `databasePath` through the shared dataset selection (a converted memory tree reads through its index), relays the shipped diff result with `memoryTrees` and `indexComplete`, and carries only the labels the caller's body supplied. [39]
- The comparison request, validated from the caller's own body with the namespace injected. [40]
- The label filter that keeps only entries an identified agent or assessment supplied, quoting the requirement that they are "inferred from the diff" only when supplied. [41]
- The integrity builder that returns `compatible: None` present beside its explicit unresolved list, and the recorded-conditions read with its connection closed in a `finally`. [42]
- The honest report when no detection run is recorded, and the report of one run's conditions, limitations and unresolved items with no verdict either way. [43]
- The integrity builder that returns `compatible: None` present beside its explicit unresolved list, carries the five run-binding fields, and reads the recorded conditions with its connection closed in a `finally`. [44]
- The caller's exact input selector as one value, with the two spellings it carries and the `as_wire` echo that reports "the caller named none" as `None` rather than as a silent absence. [45]
- The honest report when no detection run is recorded, the scope-and-selector run lookup that never reports another scope's conditions and never falls back to the first match, the run identities the requested scope holds, the report for a selection that matched nothing, and the report of one run's conditions, limitations and unresolved items with no verdict either way. [46]
- The project builder's one body (behind the thin public `knowledge_project_payload` wrapper): the destination profile, the refusal when no view was named, the shared dataset selection (a converted memory tree reads through its index, and a selection that cannot be indexed is refused before any writer runs), the delegation to the projection operation (since MIK-R01 reading a converted tree's views whole), and the per-path report relayed back with the optional `memoryTree` binding. [47]
- The one refusal envelope both project refusal routes use, carrying the destination root and the renderer version. [48]
- The view-and-identity pairs one projection request set resolves into, where the recorded identity rather than the destination path is what the artifact is about. [49]
- The view-and-identity pairs one projection request set resolves into, where the recorded identity rather than the destination path is what the artifact is about. [50]
- The strict response types these builders' payloads are validated against, with `compatible` typed `None`, the five run-binding fields declared beside the conditions, and the view payload travelling as the view's own JSON. [51]
- **The one dataset resolution the read, diff and project builders share (MIK-R23 rule 6): `databasePath` keeps its meaning, and a path naming a converted memory tree — its root or its published `knowledge.sqlite` location — resolves to the index of that tree's current state; every other path is opened as before.** [52]
- **Every way resolving and opening a selection can fail, refused the same way on every handler: a named root with no code tree is `selected_input_unavailable` naming the root (MIK-R01), a tree, Git or cache failure is `snapshot_unavailable` naming the tree, anything else the dataset refusal it was before.** [53]
- **A partial index is never presented as complete: `_index_complete` reports it for the diff and projection responses, and since MIK-R02 a converted tree's read page forces the payload's completeness to `false` in the paged view and states `indexComplete` beside it.** [54]
- **The memory-tree bindings the responses carry: `memoryTree` on read and project, `memoryTrees` (`before`/`after`) on diff, absent for a database.** [55]
- **The MIK-R23 tool cases: read by root and by `knowledge.sqlite` spelling (and refused without a coordination root), diff and project between trees, an unconverted selection unchanged, every surface reporting a partial index as incomplete, and an unbuildable index refused rather than raised.** [56]

- The dataset a projection reads, or the refusal of a seed the converted tree does not hold. [57]

### Cross-Repo References

No cross-repository behavior is implemented in this file. Each builder mediates one caller's request into one namespace's dataset or destination directory, and every vocabulary it names — the five views, the declared change kinds, the projection formats — is defined in this repository.

No meaningful cross-repo references found.
