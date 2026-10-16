# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Canonical task-source/summary and full-body readers over JSON-primary task truth, never rendered Markdown. Canonical `TaskDocumentRef` is definition-owned by `models.task_document_ref`. `read_task_sources` and path-directed `project_task_sources` use the same builder; TaskEntry owns runtime activity and membership, not a second lifecycle/series projection here.

## L126 Decision Projection Marking

`_reader_fields` projects each stored decision in stored array order (no sort —
the frontend `orderDecisionsNewestFirst` helper orders by parsed time) and sets
`product_record` from the writers' own predicate
`is_product_record_decision(item.decision)` (exact/prefix string match). The
projection preserves order; it does not decide recency.

Canonical full acquisition admits direct-root raw task-schema payloads and successful tolerant parses. The same `project_task_sources` builder supplies summaries, declared children/parent and Order from full/directed document maps. No separate series or lifecycle-link population remains; bodies avoid corpus enumeration.

The on-demand body resolves an existing requested file within `tasks/`, requires its raw schema key, and parses it without corpus enumeration. Its sprint join remains `_graph_master_docs`: no graph means an empty graph-master table; otherwise canonical candidates for graph-named tails are schema-filtered before the extracted `_task_graph_view.documents_by_ref`, then declared child references are read for authored-stage graph facts. Separately, `read_order_fields` starts with the requested parsed document. For a master it uses that path; for a non-master it reads `path.parent / Path(doc.master or "task.md").with_suffix(".json")`. An unreadable/unparseable owner returns no Order. An owner that is not a master, or is a sprint, returns before child reads. An ordinary owner reads only explicit nonempty `subTasks[].file` JSON paths, skipping paths already in its document map; it neither recursively follows dependency names nor enumerates unrelated masters. Thus a graph-less ordinary master/leaf may read its owner/listed tasks, but a graph-less sprint requests no listed Order children. External grant census is a separate cost.

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

- read_task_sources/project_task_sources: shared full/directed source builder.
- read_task_documents: standalone source-summary adapter.
- read_task_document_body: requested JSON plus named graph masters/children and ordinary owner/listed-task dependencies.
- _graph_master_docs: raw-schema-filtered canonical named joins.
- _projected_document: extracted parser alias.
- _task_step_nodes/_task_doc_node/_task_doc_body_revision: preview/body and revision projection.
- _task_graph_view owns task references/indexing/graph facts; lifecycle/series readers are removed.

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
- **Raw schema checks are load-bearing:** named graph masters and their declared children pass the raw task-schema filter before tolerant parsing. The graph index comes from the extracted adapter; named closure/order semantics are not universal serialized-body parity.

- Graph masters and declared children pass raw-schema admission; available authored child stages win. Ordinary Order is a separate named closure, not universal body-byte parity.

## External grant annotation and request cost

Summaries/bodies join optional display grants by canonical leaf identity; missing/broken grants grant no permission. Body capture records addressed/legacy grant-store directory/file identities. Grant evidence remains outside authored task JSON and permission; HTTP reads do not mutate the summary payload cache.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.

- Canonicalized requirement text reader for typed packet refs. [1]

- Canonicalized open-question reader for typed acceptance obligations. [2]
- The tolerant parser is definition-owned by _task_document_parse.projected_document: validate first, retry addressed unknown-field pruning, and return None for remaining non-unknown or exhausted failures. It is not raw-schema-presence admission. [4]



- Deep-copy pruning of addressed keys is definition-owned by _task_document_parse._without_paths; augmented locations that cannot be walked are still not healed. [5]



- The four-pass retry bound and augmented-location limitation belong to the extracted parser. Retained L10 measurements motivate the bound; no new run or derived pass-count guarantee is claimed. [6]


- The repository's own stated read-versus-enforcement split this change follows. Anchor: "The read is deliberately the TOLERANT one" [7]
- Authoring strictness is untouched: the strict base model, and the step-level `note` a newer build writes. Anchor: `Step.note` [8]
- The durable-data writer takes an already-validated document, so it can write no unknown key. [9]

- No summary count cap remains, but the current population is canonical direct task-root JSON with the explicit raw task schema and a successful tolerant parse; canonical sources project each admitted document, not a second series population. Missing/bad-schema/failed parses are not a completeness promise. Retain the silent-eviction removal rationale. [10]
- The legacy-bare-node `ref` synthesis that leaves one loc path unprunable. [12]
- The closeout-queue reader skips a payload that fails model validation. Historical site counting and unchanged-source comparison belong to the retained task evidence, not this current-source reference. [13]

- The body read's master join table: none without a graph, otherwise graph-named masters and their declared children that carry the schema. [15]
- The named-path probe that returns exactly the enumeration's subset for those tails, in the same order. [16]

- The extracted graph adapter joins named documents for titles/nature/authored child stage. [17]
- The HTTP handler that calls the body read: 503 before the first projection, 404 when the read returns `None`. [18]

- Retained L42 regression account: byte identity against the corpus-wide join and same touched files at 4/40 unrelated tasks concerned the earlier graph-only closure. It remains historical execution evidence, not a result from this reconciliation. RF01 source updates the leaf-touch expectation to include its owner and adds owner/listed-child admission assertions; those compare dependency/graph fields, not complete serialized bodies for every possible Order population. [19]

- Retained L42 regression account: byte identity against the corpus-wide join and same touched files at 4/40 unrelated tasks concerned the earlier graph-only closure. It remains historical execution evidence, not a result from this reconciliation. RF01 source updates the leaf-touch expectation to include its owner and adds owner/listed-child admission assertions; those compare dependency/graph fields, not complete serialized bodies for every possible Order population. [19]
## 260815-DAG-L12 Render-Ready Graph View Wiring

Both snapshot readers now project `TaskDocNode.executionGraphView` (L12-R4): `_task_doc_node` was split into the include-body-gated `_reader_fields` and the sprint-only `_execution_graph_fields` behind a bundled `_TaskDocProjectionOptions` (`include_body` + `master_docs`), while `_task_graph_view.documents_by_ref` owns qualified indexing and `execution_graph_view` the task-domain adapter. For the summary reader its input is the whole projected task-document set: every admitted document under `tasks/<repo>/<task>/` is indexed, so a sprint's commanded masters are always present (no bound evicts any document; see the removal rationale at `_common.py:65-71`). **For the body reader, since 260921-ICR-L42, the input is the graph-named masters and their declared children** (`_graph_master_docs`). The extracted `execution_graph_view` does the tasks-domain walk — derived waves, resolved edge endpoints, joined titles, per-master facts — and feeds the primitives-only `build_execution_graph_view` builder (the observer package must not import tasks). An ordinary master may instead carry its derived Order graph; `_task_doc_node` includes graph/dependency fields in revision identity.

Current split: corpus summaries build OrderFields from their parsed document map. Bodies call both `_graph_master_docs` for named sprint masters and declared children and `read_order_fields` for the ordinary owner/listed-task closure. the extracted `execution_graph_view` still feeds the primitives-only sprint builder. An ordinary master can receive an Order view without a persisted graph; `_task_doc_node` prefers that Order graph and includes derived graph/dependency fields in revision identity. The historical claim that every graph-less document projects None and revision is unchanged no longer describes this source. RF01 owner/listed-child reads now explicitly filter raw schema before parsing; the archived sprint subset result still is not universal new-population byte-parity evidence.


## 260821-CLIVE Discarded-Unstarted Projection

Master task summaries and full bodies now project `discardedCount` plus typed `discardedSubTasks`, including
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
> Current tolerant parsing is definition-owned by `_task_document_parse.projected_document`; canonical task-source and full-body readers consume its import alias. Removed series readers and historical local call-site counts are not current owners.
>
> What it does: validate strictly first; on a `ValidationError` whose reports include `extra_forbidden`,
> drop exactly those addressed keys with `_without_paths` and validate again; any other failure
> (missing required field, bad enum, malformed nested value) still yields `None`, exactly as before. Why
> the old behavior read like a status filter: a completed leaf whose durable JSON carried a step-level
> `note` (`tasks/document.py:121`, a field a newer build writes) was refused whole, so it never reached
> the historical task-document projection and the master's sub-task row fell to the non-clickable
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
> Summary count caps were removed; current full acquisition admits canonical direct-root task-schema payloads with successful tolerant parses. This is not successful whole-corpus parsing or a separate series collection.
>
> **Found for follow-up, not changed here:** a sixth same-class drop site outside this leaf's five, at
> `snapshots_impl/_closeout_queue.py:33-36`.

Tolerant parsing and its augmented-location limitation are definition-owned by `_task_document_parse`, not this import alias. Historical local call-site counts are not current ownership.

## 260921-ICR-L42 The Body Read Opens Only What It Names

Body reads requested schema-admitted JSON, named graph masters/declared children and ordinary owner/listed tasks. Named candidate and grant-store reads may enumerate directories. Captured native generations support cache reuse; they are not a single-file I/O bound or filesystem snapshot transaction.

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

- Ordinary leaf dependency fields consume the addressed owning master and explicit listed tasks. Graph projection additionally consumes graph-named masters’ declared children. Retained graph-only scope measurements do not describe the whole widened read.

- Current R128 extension: leaf dependency lists consume the addressed owning master and its explicitly listed tasks. The former scope choice and byte-identity report remain L42 history; RF01 adds raw-schema filtering of newly read Order inputs and scoped body/corpus dependency-field assertions, not a universal byte-identity result.
- The body path does not use `TaskDocumentPayloadCache`. Passing it a subset would have pruned the
  projector's cache entries for the same root. Reading the handful of named files directly also means
  HTTP threadpool threads no longer mutate that single-owner cache. The projector's cache logic is
  unchanged.
- This reader owns no persistent body store or daemon. The per-runtime body cache is a separate owner and validates captured native input generations before reuse/304.

**Negative knowledge and what remains.**

- An exact-path request for any schema-valid JSON under `tasks/` is still served, including historical
  `notes/` copies and `0_archive` documents. That is pre-existing behavior, preserved byte for byte.
- The eager review-catalogue cost belongs to L47, and `notes/list` belongs to L55. The installed-build
  before/after, with concurrent master+leaf reads and projector CPU, belongs to L50 (review finding
  L42-R1-F1). None of these is claimed here.



- Body revision hashes typed intent values and raw fixed-prose/dependency/time slots; node construction also hashes derived Order graph/dependencies, while completion-time projection prefers stored time then the greatest valid exact-finalization timestamp. [3]
- `indexRows.resolveRowTarget` retains the “not authored as a task document yet” diagnostic when the summary is absent. Navigation is enabled by an entry reference, even before the summary is authored; a reference-less entry has no jump. There is no current `IndexLink` component. [11]



- Body reads the requested schema-admitted payload plus sprint graph-named masters and their declared children and/or the addressed ordinary owner/listed-task closure, without corpus enumeration. RF01 newly read Order owner/child dicts must carry the raw task schema before tolerant parsing; separate grant-store census remains a distinct cost. [14]

- Summary/body retain optional external grant annotation. Canonical full acquisition and addressed body dependencies have distinct costs. Display grants remain outside authored JSON/permission; captured grant inputs participate in generation currentness. [20]
