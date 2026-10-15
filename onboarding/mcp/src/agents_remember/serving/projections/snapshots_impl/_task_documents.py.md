# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Task-document and series readers: summaries, full bodies, lifecycle binding. Task JSON is the source of truth (never the rendered markdown). Canonical `TaskDocumentRef` comes directly from `models.task_document_ref`; the projection facade supplies DTO aliases, not the identity type's definition or a required re-export. These readers project task documents and the series checklist, resolve cross-folder lifecycle links, and hash full bodies for the on-demand body endpoint.

## L126 Decision Projection Marking

`_reader_fields` projects each stored decision in stored array order (no sort —
the frontend `orderDecisionsNewestFirst` helper orders by parsed time) and sets
`product_record` from the writers' own predicate
`is_product_record_decision(item.decision)` (exact/prefix string match). The
projection preserves order; it does not decide recency.

The two kinds of reader have different costs. Always-on task summaries and series readers enumerate the canonical corpus through `_common._iter_task_document_payloads`; it admits raw `schema == ar-task-document/v1` payloads, and only successful tolerant parses become task nodes. Summary Order uses that already-read document map, not per-leaf rereads.

The on-demand body resolves an existing requested file within `tasks/`, requires its raw schema key, and parses it without corpus enumeration. Its sprint join remains `_graph_master_docs`: no graph means an empty graph-master table; otherwise canonical candidates for graph-named tails are schema-filtered before `_master_docs_by_ref`. Separately, `read_order_fields` starts with the requested parsed document. For a master it uses that path; for a non-master it reads `path.parent / Path(doc.master or "task.md").with_suffix(".json")`. An unreadable/unparseable owner returns no Order. An owner that is not a master, or is a sprint, returns before child reads. An ordinary owner reads only explicit nonempty `subTasks[].file` JSON paths, skipping paths already in its document map; it neither recursively follows dependency names nor enumerates unrelated masters. Thus a graph-less ordinary master/leaf may read its owner/listed tasks, but a graph-less sprint requests no listed Order children. External grant census is a separate cost.

Historical named-input schema-admission gap (F01 cc238585): owner/listed-child dictionaries previously reached projected_document without checking the raw schema key, whose default could admit a schema-less payload. RF01 read_order_fields now requires payload.get("schema") == TASK_DOCUMENT_SCHEMA before parsing each newly read owner and listed child. A missing/wrong-schema owner returns no Order before child reads; a missing/wrong-schema child is not admitted to the document map. Schema-bearing inputs still use the shared tolerant parser. The requested body and sprint graph-master filters remain explicit. These source predicates and the new admission-test assertions address that specific divergence; they do not establish universal body-byte parity or an executed regression result.

The tolerant durable-data parser now belongs to [_task_document_parse](./_task_document_parse.py.md): this reader imports `projected_document as _projected_document`. The extracted parser is the model-validation owner: it retries only addressed `extra_forbidden` pruning, returns `None` when a report has no unknown fields, and withholds unresolved failures after four passes. The authoring/read split, deep-copy pruning and residual augmented-loc limitation remain distinct from raw-schema admission, which is enforced by the callers that actually check it.

## Code Commentary

### Bounded summaries and whole reader bodies

`_task_doc_form` uses the TaskDocument model's sprint classification, not a title or client heuristic.
The always-on summary bounds long note/outcome/status/finding-description strings to 400 characters,
header notes to six carried rows and findings to twenty-five; totals name the complete collections.
The review producer counts open flags before cutting the findings list. The on-demand body carries
every note/finding and whole strings, with clear tested preview flags. A carried six-header-note
summary is not the same as the head's six drawn-note bound after independent strip facts are suppressed.

`bodyRevision` also hashes statusNote, headerNotes, type, complete steps and reviewState, in addition
to the existing long reader content and sprint structure. This makes displayed-field changes invalidate
an open cached body. The client still keeps current summary identity/status/progress/review aggregates
rather than allowing a fetch-time body to become current fact authority. Nested notes are preserved as
body data, but the current nested-row renderer does not draw them or label their summary truncation.

The revision also includes raw `nonGoals`, `acceptance`, `waitsFor`, and `completedAt`. `_task_doc_node` additionally hashes derived Order graph and both directional dependency lists when OrderFields are present, so sibling-derived display changes join body identity. Fixed prose is body-only; raw waits, dependency lists, and completion time are node fields. `_completion_time` prefers a truthy stored `completedAt`; otherwise it selects the greatest parsed datetime among decisions whose text exactly equals `Finalize task lifecycle.`, skipping invalid timestamps and treating naive ones as UTC for comparison, while returning the original timestamp string. No valid matching decision yields None. The F01 reversed-array/last-matching-record behavior is retained history, not the current selection rule. Steps remain fully nested reader data, while display counts use major-only progress helpers.


- `read_task_documents`
- `read_task_document_body` (resolves the requested schema-admitted file, joins sprint graph-named masters and the addressed ordinary owner/listed-task Order closure without corpus enumeration; newly read Order owner/child dicts require the raw task schema before tolerant parsing, and external grant census remains separate)
- `_graph_master_docs` (since 260921-ICR-L42; the body read's master join table. It returns `{}` for a
  document without an `executionGraph`. For a sprint it probes only the graph-named
  `<task>/<file>.json` tails through `_common._canonical_task_json_candidates`, keeps only
  payloads carrying the task-document schema, and hands them to the unchanged `_master_docs_by_ref`)
- `_task_document_lifecycle_maps`
- `_task_doc_lifecycle_id`
- `_doc_enclosure_lifecycle`
- `_projected_document` (compatibility import alias of `_task_document_parse.projected_document`)
- `_task_document_parse._UNKNOWN_FIELD_PASSES` (`= 4`) and `_without_paths` (deep-copy addressed-key pruning) are definition-owned by the extracted parser, not local functions/constants.
- `read_series_documents`
- `_series_subtask_nodes`
- `_series_subtask_created_at`
- `_ref_lifecycle`
- `_task_step_nodes`
- `_task_doc_node`
- `_task_doc_body_revision` (since 260815-DAG-L14 the revision covers `subTasks` + `seats` so
  an open reader refetches when sprint linkage/seat edits land)
- `_task_doc_node` since 260815-DAG-L14 passes `SubTaskRef.masterRef` through to
  `TaskSubTaskRefNode.masterRef` and projects `doc.seats` as `TaskSeatNode` rows

Since 260831-CCR (commit `99dc249b`) the readers canonicalize the typed requirement and open-question
slots into stable reader strings: `_requirement_reader_text` renders an
`ApprovedRequirementPacketRef` as `{stableId}@{version} — {path}`, `_question_reader_text`
renders an `AcceptanceObligationQuestion` as `Acceptance obligation {id}: {question}`,
and `_task_doc_body_revision` hashes typed intent slots through a stable by-alias dump
(`_task_intent_body_value`) so a change to a packet version or an obligation question
text alters the body revision and open readers refetch.

## Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py`.
- Type-preserving intent slots must keep their canonicalized text stable: the reader surface is a
  string projection, while the digest path uses the typed by-alias dump.
- **Read tolerance is definition-owned by `_task_document_parse.projected_document`.** It retries
  only the addressed `extra_forbidden` keys; non-unknown failures that remain after pruning
  still withhold the document. Do not turn the import alias into a second parser or a blanket
  per-key ignore policy. This tolerance is not a raw-schema-presence check: the requested-body, graph-master and newly read Order owner/child callers enforce their own raw-schema predicates.
- **Authoring is the strict end of the split.** The document model keeps `extra="forbid"`, `task_doc`'s
  write-time validation is untouched, and `write_task_doc` takes an already-validated `TaskDocument`.
  A read-edge tolerance change must never be read as permission to write an unknown key.
- The shared parser now owns the single projection `TaskDocument.model_validate` loop in
  `_task_document_parse.py`; `_task_documents` and `_task_order` consume that owner. Keep the
  old anti-duplicate-parser rationale, not the obsolete claim of a local definition here.
- The residual unprunable-loc gap (a loc pydantic augments, such as the legacy `ref`) stays fail-closed
  and must be changed only deliberately: closing it re-opens the proven fix's semantics.
- **The body read must not enumerate the task corpus.** `master_docs` remains the separate
  sprint graph-ref join. Ordinary-master/leaf dependency fields use `read_order_fields`: the
  requested document, its addressed owner when different, then explicit owner-listed tasks.
  No unrelated-master census or dependency-name recursion is introduced. Retain the historical
  read-count-test rationale as history, not an executed result for this widened path.
- **Raw-schema admission remains a caller boundary.** RF01 now checks the raw task schema for newly read Order owners/listed children as well as the existing requested-document and graph-master checks. Tolerant parsing alone never proves schema presence. Keep the earlier missing-check defect as F01 history; do not weaken schema-bearing admission or generalize the new scoped assertions into all-input byte parity.
- **The schema filter in `_graph_master_docs` is load-bearing.** `TaskDocument.schema_` has a default,
  so a master-shaped JSON with no `schema` key would validate, and at a graph-named path it would win
  the last-wins join. The corpus-wide join never admitted it, because `_iter_task_document_payloads`
  filters on the schema. The body read must keep that filter so the bytes stay identical.
> **Retained historical source account — superseded by the current contract:**
> - **The body read serves the same bytes as the corpus-wide join.** `_graph_master_docs` sends
>   `_master_docs_by_ref` exactly the canonical-enumeration subset for the named refs, in the same
>   order, so duplicate-key last-wins resolves as it did before. Changing that order or subset changes
>   which master a sprint shows.

- Current scope: `_graph_master_docs` retains the schema-filtered canonical candidate subset and `_master_docs_by_ref` last-wins assignment for the sprint graph join only. Preserve that order/subset rationale. RF01 also adds explicit schema checks to newly read Order inputs, but that is not a reason to extend the archived sprint-only body-byte identity result into universal Order parity; the new source test separately compares dependency/graph fields against the corpus reader in its admission matrix.

## External grant annotation and request cost

Summaries, full bodies and series children join readable external grant display evidence by actual canonical leaf identity/path, never a guessed slug. Missing/broken display grants do not break projection; this does not authorize execution. A body request avoids canonical corpus enumeration but may read the requested document, sprint graph-named masters, or the ordinary owner/listed-task closure described above. Its explicit task-addressed external grant census adds grant-store I/O with a retained legacy unaddressed fallback. This is neither constant-I/O nor zero-directory-read. Grant display is not authored task JSON, bodyRevision input, or cached permission.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.

- Canonicalized requirement text reader for typed packet refs. [1]

- Canonicalized open-question reader for typed acceptance obligations. [2]
- The tolerant parser is definition-owned by _task_document_parse.projected_document: validate first, retry addressed unknown-field pruning, and return None for remaining non-unknown or exhausted failures. It is not raw-schema-presence admission. [4]



- Deep-copy pruning of addressed keys is definition-owned by _task_document_parse._without_paths; augmented locations that cannot be walked are still not healed. [5]



- The four-pass retry bound and augmented-location limitation belong to the extracted parser. Retained L10 measurements motivate the bound; no new run or derived pass-count guarantee is claimed. [6]


- The repository's own stated read-versus-enforcement split this change follows. [7]
- Authoring strictness is untouched: the strict base model, and the step-level `note` a newer build writes. [8]
- The durable-data writer takes an already-validated document, so it can write no unknown key. [9]

- No summary count cap remains, but the current population is canonical direct task-root JSON with the explicit raw task schema and a successful tolerant parse; summaries project each admitted doc and series projects admitted masters. Missing/bad-schema/failed parses are not a completeness promise. Retain the silent-eviction removal rationale. [10]
- The legacy-bare-node `ref` synthesis that leaves one loc path unprunable. [12]
- The closeout-queue reader skips a payload that fails model validation. Historical site counting and unchanged-source comparison belong to the retained task evidence, not this current-source reference. [13]

- The body read's master join table: none without a graph, otherwise only the graph-named masters that carry the schema. [15]
- The named-path probe that returns exactly the enumeration's subset for those tails, in the same order. [16]

- The only consumer of `master_docs`, which looks masters up solely by graph ref. [17]
- The HTTP handler that calls the body read: 503 before the first projection, 404 when the read returns `None`. [18]

- Retained L42 regression account: byte identity against the corpus-wide join and same touched files at 4/40 unrelated tasks concerned the earlier graph-only closure. It remains historical execution evidence, not a result from this reconciliation. RF01 source updates the leaf-touch expectation to include its owner and adds owner/listed-child admission assertions; those compare dependency/graph fields, not complete serialized bodies for every possible Order population. [19]
## 260815-DAG-L12 Render-Ready Graph View Wiring

> **Retained historical source account — superseded by the current contract:**
> Both snapshot readers now project `TaskDocNode.executionGraphView` (L12-R4): `_task_doc_node` was split into the include-body-gated `_reader_fields` and the sprint-only `_execution_graph_fields` behind a bundled `_TaskDocProjectionOptions` (`include_body` + `master_docs`), and `_master_docs_by_ref` builds the title/status/nature join table. For the summary reader its input is the whole projected task-document set: every valid master under `tasks/<repo>/<task>/` is indexed, so a sprint's commanded masters are always present (no bound evicts any document; see the removal rationale at `_common.py:65-71`). **For the body reader, since 260921-ICR-L42, the input is only the graph-named masters** (`_graph_master_docs`). For those refs these are the same entries the whole-set table held, so the projected graph is unchanged. `_execution_graph_view` does the tasks-domain walk — derived waves, resolved edge endpoints, joined titles, per-master facts — and feeds the primitives-only `build_execution_graph_view` builder (the observer package must not import tasks). Docs without a graph project `None`; `_task_doc_body_revision` is unchanged.

Current split: corpus summaries build OrderFields from their parsed document map. Bodies call both `_graph_master_docs` for the sprint join and `read_order_fields` for the ordinary owner/listed-task closure. `_execution_graph_view` still feeds the primitives-only sprint builder. An ordinary master can receive an Order view without a persisted graph; `_task_doc_node` prefers that Order graph and includes derived graph/dependency fields in revision identity. The historical claim that every graph-less document projects None and revision is unchanged no longer describes this source. RF01 owner/listed-child reads now explicitly filter raw schema before parsing; the archived sprint subset result still is not universal new-population byte-parity evidence.


## 260821-CLIVE Discarded-Unstarted Projection

Master task and series nodes now project `discardedCount` plus typed `discardedSubTasks`, including
the audited reason, timestamp, disposition, and exact unstarted proof. The discarded history also
participates in task-body revision identity so an open reader refetches after a valid discard.
Discarded entries are historical task truth and never disappear merely because they are absent from
the active subtask list.

## CCR-R02@v2 Typed Slot Canonicalization

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, the reader surface accounts for
typed `ApprovedRequirementPacketRef` and `AcceptanceObligationQuestion` slots (never raw model
reprs) and includes them in body-revision identity, so served bodies and revision tokens reflect
normative intent content exactly.

## 260913-LCA-L10 Tolerant Read Edge For Durable Task Documents

> **Retained historical source account — superseded by the current contract:**
> A document a newer build wrote stays readable by this reader. All five read-edge call sites —
> `read_task_documents`, `read_task_document_body`, `read_series_documents`,
> `_series_subtask_created_at` and `_master_docs_by_ref` — now call `_projected_document`
> instead of each wrapping `TaskDocument.model_validate` in its own
> `except ValueError: continue|return None`. `_projected_document` is the module's **only**
> `TaskDocument.model_validate` site, so a future caller cannot reintroduce the strict-only
> parse by accident. Pre-change, each of those five sites **deleted the whole document** rather than
> marking it unreadable.
>
> What it does: validate strictly first; on a `ValidationError` whose reports include `extra_forbidden`,
> drop exactly those addressed keys with `_without_paths` and validate again; any other failure
> (missing required field, bad enum, malformed nested value) still yields `None`, exactly as before. Why
> the old behavior read like a status filter: a completed leaf whose durable JSON carried a step-level
> `note` (`tasks/document.py:121`, a field a newer build writes) was refused whole, so it never reached
> `analytics.taskDocuments` and the master's sub-task row fell to the non-clickable
> `title="not authored as a task document yet"` branch
> (`dashboard/src/panels/detail-panel/taskReader.tsx:434`) while unstarted rows stayed live. Status was
> correlated, never causal: notes are written when a step advances, so completed leaves fell out first.
>
> **Authoring stays strict, and that is the deliberate split.** `_Doc` keeps `extra="forbid"`
> (`tasks/document.py:73-76`), `task_doc`'s write-time validation and `application/task_docs` are
> untouched, and `write_task_doc` (`tasks/store.py:108`) takes an already-validated `TaskDocument`, so it
> can write no file carrying a key the model refuses. Only the durable-data **read** edge became
> version-tolerant — this repository's own stated doctrine, not a new precedent: "The read is
> deliberately the TOLERANT one ... the STRICT read is what the enforcement fold uses, and it still
> raises" (`snapshots_impl/_runtime.py:121-123`).
>
> `_UNKNOWN_FIELD_PASSES = 4` is **unproven-but-generous, not derived.** No measurement in this
> change produced a prunable shape needing more than two passes, and the patch's original comment — one
> retry per nesting level — was measured false and corrected: pydantic reports `extra_forbidden` for
> every nesting level in a single error report (re-measured for this card: one report carried four
> `extra_forbidden` locs across document, step, substep and section level, and the instrumented loop
> reached a valid document in two passes). The bound's real job is to stop a loc this reader cannot
> address from looping, so it is a stop, not a computation.
>
> **Residual gap, documented in the code comment and deliberately not changed.** `_without_paths` walks
> the raw payload by the loc's own keys; a loc pydantic *augments* has no raw key to walk and prunes
> nothing, so the document is still withheld once the bound is spent. That is reachable for the `ref`
> `SprintExecutionNode._lift_legacy_ref` invents for a legacy bare node (`tasks/document.py:212-219`) or
> for a union branch label in an edge endpoint. It is fail-closed, not corruption; no writer produces
> those shapes today; and closing it would change the semantics of the proven fix, so it is recorded
> rather than repaired.
>
> **Not the cause and not the fix:** `TASK_DOCUMENT_SUMMARY_LIMIT = 250` was measured irrelevant to this
> defect — the withheld documents sat well inside the summary window, so the missing rows were never an
> eviction or a tightened bound and raising the limit would not have restored them. The dashboard renderer
> was not changed either; it was correct, and a truthy `match` is what the projection owed it.
>
> **That bound no longer exists (260916-TDPU).** `TASK_DOCUMENT_SUMMARY_LIMIT`,
> `SERIES_DOCUMENT_SUMMARY_LIMIT`, `_bounded_task_document_payloads` and `_stat_mtime_ns` are deleted, so
> this reader projects **every** canonical task document under `tasks/<repo>/<task>/`; the measurement
> above stands as the reason the bound was never load-bearing, not as a live constraint. The removal
> rationale is recorded in the code at `_common.py:65-71`. See the 2026-09-16 entry below.
>
> **Found for follow-up, not changed here:** a sixth same-class drop site outside this leaf's five, at
> `snapshots_impl/_closeout_queue.py:33-36`.

Current ownership note: this entire L10 account retains the original diagnosis, measurements, bound rationale and unresolved augmented-loc caveat. Its local `_projected_document`/`_without_paths`/single-validation-site descriptions now refer to the extracted `_task_document_parse` owner. The stale frontend diagnostic location is now `indexRows.tsx:55-78`. No measurement or test in that historical report was rerun for this proposal.

## 260921-ICR-L42 The Body Read Opens Only What It Names

> **Retained historical source account — superseded by the current contract:**
> **What changed.** `read_task_document_body` used to call `_iter_task_document_payloads(tasks_root, now=now)`,
> which enumerated and parsed the whole canonical corpus. It built `_master_docs_by_ref` from the result
> for every document, including leaves and masters that have no graph and consume no master. The read now
> resolves and reads the one requested file and takes its join table from `_graph_master_docs`. A leaf,
> a master or a standalone document therefore lists no directory and reads no other file. A sprint lists
> the repository folders and the task folders its graph names, and reads the files at those paths.

Current extension: that L42 graph-only request closure is historical. Ordinary-master/leaf dependency display opens the addressed owner and explicit listed task files through `read_order_fields`; no corpus-wide scan is reintroduced. Graph-less sprint and unusable/non-master owners return before Order-child reads. RF01 checks the raw task schema on newly read owner/listed-child dicts before tolerant parsing; the earlier missing-check concern remains historical.

**Why.** ICR-R24@v3 requires the reviewer's normal task entry to be usable, and requires loading not to
be dominated by unrelated corpus work. The audit measured 3.865 s in the browser for one leaf read. The
function profile showed 1.754 of 1.770 s in corpus enumeration (14,282 `relative_to` calls). Review R1
decomposed the browser figure: three concurrent whole-corpus enumerations competed for one GIL. They
were the leaf's own read, the master read the browser fires at the same moment, and the live
projector's pass through `read_closeout_queues`. The L42 candidate removes the first two from this
reader and makes the third about 76 times cheaper through `_common._iter_task_json`. On the real
corpus the isolated HTTP route median fell from 0.591 s to 0.019 s for a leaf and from 0.593 s to
0.023 s for a master. These are task-evidence figures that depend on the corpus, not a contract.

**Scope choices the Architect accepted (2026-09-28T12:34:35+02:00).**

> **Retained historical source account — superseded by the current contract:**
> - The leaf design named "the governing master" as something to resolve. The body read does not open it,
>   because no body field consumes a document's own master. Only sprint graph views consume masters.
>   Byte identity across the corpus confirms nothing depended on it.

- Current R128 extension: leaf dependency lists consume the addressed owning master and its explicitly listed tasks. The former scope choice and byte-identity report remain L42 history; RF01 adds raw-schema filtering of newly read Order inputs and scoped body/corpus dependency-field assertions, not a universal byte-identity result.
- The body path does not use `TaskDocumentPayloadCache`. Passing it a subset would have pruned the
  projector's cache entries for the same root. Reading the handful of named files directly also means
  HTTP threadpool threads no longer mutate that single-owner cache. The projector's cache logic is
  unchanged.
- There is no index, persistent cache, store or daemon. The lookup is bounded by path.

**Negative knowledge and what remains.**

- An exact-path request for any schema-valid JSON under `tasks/` is still served, including historical
  `notes/` copies and `0_archive` documents. That is pre-existing behavior, preserved byte for byte.
- The eager review-catalogue cost belongs to L47, and `notes/list` belongs to L55. The installed-build
  before/after, with concurrent master+leaf reads and projector CPU, belongs to L50 (review finding
  L42-R1-F1). None of these is claimed here.



- Body revision hashes typed intent values and raw fixed-prose/dependency/time slots; node construction also hashes derived Order graph/dependencies, while completion-time projection prefers stored time then the greatest valid exact-finalization timestamp. [3]
- An unresolved authored-document row remains non-clickable; resolveRowTarget and IndexLink now live in the shared indexRows owner, including the same diagnostic text. [11]



- Body reads the requested schema-admitted payload plus sprint graph-named masters and/or the addressed ordinary owner/listed-task closure, without corpus enumeration. RF01 newly read Order owner/child dicts must carry the raw task schema before tolerant parsing; separate grant-store census remains a distinct cost. [14]

- Summary/body/series retain optional external grant annotation; corpus summary/series enumeration and addressed body owner/listed-task reads have different costs. Display grants remain outside authored JSON, revision identity and permission. [20]
