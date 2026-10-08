# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py

## Governing Overview

[serving projections overview](../overview.md)

## Purpose

Task-document and series readers: summaries, full bodies, lifecycle binding. Task JSON is the source of truth (never the rendered markdown). These readers project task documents and the series checklist, resolve cross-folder lifecycle links, and hash full bodies for the on-demand body endpoint.

The two kinds of reader have different costs, and since 260921-ICR-L42 that difference is deliberate.
The always-on summary and series readers enumerate the canonical corpus (`_common._iter_task_json`)
on each projection pass. The on-demand body reader, `read_task_document_body`, which serves one
dashboard `/api/task-document` request, **never enumerates the corpus**. It reads the requested
document, plus the masters its own sprint execution graph names when it has a graph
(`_graph_master_docs`).

Since 260913-LCA-L10 the durable-data **read** edge is deliberately tolerant of a field a newer build
wrote: all five read-edge call sites route through `_projected_document`, which drops only the keys
pydantic reports as `extra_forbidden` and re-validates, while every other validation failure still
withholds the document. This is the read half of one split, not a relaxation of authoring — the
document model, `task_doc`'s write-time validation and `write_task_doc` all stay strict, matching
`snapshots_impl/_runtime.py:121-123`.

## Code Commentary

- `read_task_documents`
- `read_task_document_body` (since 260921-ICR-L42: resolves and reads only the requested file, then
  projects it with the join table from `_graph_master_docs`; it no longer calls
  `_iter_task_document_payloads`)
- `_graph_master_docs` (since 260921-ICR-L42; the body read's master join table. It returns `{}` for a
  document without an `executionGraph`. For a sprint it probes only the graph-named
  `<task>/<file>.json` tails through `_common._canonical_task_json_candidates`, keeps only
  payloads carrying the task-document schema, and hands them to the unchanged `_master_docs_by_ref`)
- `_task_document_lifecycle_maps`
- `_task_doc_lifecycle_id`
- `_doc_enclosure_lifecycle`
- `_UNKNOWN_FIELD_PASSES` (since 260913-LCA-L10; the pruning pass bound, `= 4`)
- `_projected_document` (since 260913-LCA-L10; the module's only `TaskDocument.model_validate` site)
- `_without_paths` (since 260913-LCA-L10; targeted pruning of exactly the addressed keys)
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
- **Read tolerance is keyed on one error type only.** `_projected_document` tolerates
  `extra_forbidden` and nothing else; a missing required field, a bad enum or a malformed nested value
  still withholds the document. Do not widen it into a blanket `try`/`except` or a per-key ignore list.
- **Authoring is the strict end of the split.** The document model keeps `extra="forbid"`, `task_doc`'s
  write-time validation is untouched, and `write_task_doc` takes an already-validated `TaskDocument`.
  A read-edge tolerance change must never be read as permission to write an unknown key.
- `_projected_document` must remain the module's single `TaskDocument.model_validate` site, so no future
  caller can reintroduce the strict-only parse that deleted a whole document.
- The residual unprunable-loc gap (a loc pydantic augments, such as the legacy `ref`) stays fail-closed
  and must be changed only deliberately: closing it re-opens the proven fix's semantics.
- **The body read must not enumerate the task corpus.** Only `_execution_graph_view` consumes
  `master_docs`, and only by the refs its graph nodes carry. If a body projection ever needs other
  masters, add them through `_graph_master_docs` from their own paths, never through
  `_iter_task_document_payloads`. The read-count test in `test_task_document_body_lookup.py` fails
  when a body read touches more files as the corpus grows.
- **The schema filter in `_graph_master_docs` is load-bearing.** `TaskDocument.schema_` has a default,
  so a master-shaped JSON with no `schema` key would validate, and at a graph-named path it would win
  the last-wins join. The corpus-wide join never admitted it, because `_iter_task_document_payloads`
  filters on the schema. The body read must keep that filter so the bytes stay identical.
- **The body read serves the same bytes as the corpus-wide join.** `_graph_master_docs` sends
  `_master_docs_by_ref` exactly the canonical-enumeration subset for the named refs, in the same
  order, so duplicate-key last-wins resolves as it did before. Changing that order or subset changes
  which master a sprint shows.

## Evidence

### Repo-Internal References

The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module.
- Canonicalized requirement text reader for typed packet refs. [1]
- Canonicalized open-question reader for typed acceptance obligations. [2]
- Body revision hashing of typed intent slots. [3]
- The tolerant read edge: strict first, only `extra_forbidden` keys dropped, every other failure still `None`. [4]
- Targeted pruning of exactly the addressed keys from a deep copy. [5]
- The pruning pass bound and the residual unprunable-loc gap it exists to stop. [6]
- The repository's own stated read-versus-enforcement split this change follows. [7]
- Authoring strictness is untouched: the strict base model, and the step-level `note` a newer build writes. [8]
- The durable-data writer takes an already-validated document, so it can write no unknown key. [9]
- The reader projects every canonical task document, and the removed summary bound with the rationale for its removal. [10]
- The dead-text element a withheld document produced, unchanged by this leaf. [11]
- The legacy-bare-node `ref` synthesis that leaves one loc path unprunable. [12]
- The closeout-queue reader skips a payload that fails model validation. Historical site counting and unchanged-source comparison belong to the retained task evidence, not this current-source reference. [13]
- The on-demand body read: resolve, confine under `tasks/`, read one file, project with the graph-only join table. [14]
- The body read's master join table: none without a graph, otherwise only the graph-named masters that carry the schema. [15]
- The named-path probe that returns exactly the enumeration's subset for those tails, in the same order. [16]
- The only consumer of `master_docs`, which looks masters up solely by graph ref. [17]
- The HTTP handler that calls the body read: 503 before the first projection, 404 when the read returns `None`. [18]
- The regression evidence: byte identity against the corpus-wide join, and the same touched files at 4 and 40 unrelated tasks. [19]


## 260815-DAG-L12 Render-Ready Graph View Wiring

Both snapshot readers now project `TaskDocNode.executionGraphView` (L12-R4): `_task_doc_node` was split into the include-body-gated `_reader_fields` and the sprint-only `_execution_graph_fields` behind a bundled `_TaskDocProjectionOptions` (`include_body` + `master_docs`), and `_master_docs_by_ref` builds the title/status/nature join table. For the summary reader its input is the whole projected task-document set: every valid master under `tasks/<repo>/<task>/` is indexed, so a sprint's commanded masters are always present (no bound evicts any document; see the removal rationale at `_common.py:65-71`). **For the body reader, since 260921-ICR-L42, the input is only the graph-named masters** (`_graph_master_docs`). For those refs these are the same entries the whole-set table held, so the projected graph is unchanged. `_execution_graph_view` does the tasks-domain walk — derived waves, resolved edge endpoints, joined titles, per-master facts — and feeds the primitives-only `build_execution_graph_view` builder (the observer package must not import tasks). Docs without a graph project `None`; `_task_doc_body_revision` is unchanged.


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

A document a newer build wrote stays readable by this reader. All five read-edge call sites —
`read_task_documents`, `read_task_document_body`, `read_series_documents`,
`_series_subtask_created_at` and `_master_docs_by_ref` — now call `_projected_document`
instead of each wrapping `TaskDocument.model_validate` in its own
`except ValueError: continue|return None`. `_projected_document` is the module's **only**
`TaskDocument.model_validate` site, so a future caller cannot reintroduce the strict-only
parse by accident. Pre-change, each of those five sites **deleted the whole document** rather than
marking it unreadable.

What it does: validate strictly first; on a `ValidationError` whose reports include `extra_forbidden`,
drop exactly those addressed keys with `_without_paths` and validate again; any other failure
(missing required field, bad enum, malformed nested value) still yields `None`, exactly as before. Why
the old behavior read like a status filter: a completed leaf whose durable JSON carried a step-level
`note` (`tasks/document.py:121`, a field a newer build writes) was refused whole, so it never reached
`analytics.taskDocuments` and the master's sub-task row fell to the non-clickable
`title="not authored as a task document yet"` branch
(`dashboard/src/panels/detail-panel/taskReader.tsx:434`) while unstarted rows stayed live. Status was
correlated, never causal: notes are written when a step advances, so completed leaves fell out first.

**Authoring stays strict, and that is the deliberate split.** `_Doc` keeps `extra="forbid"`
(`tasks/document.py:73-76`), `task_doc`'s write-time validation and `application/task_docs` are
untouched, and `write_task_doc` (`tasks/store.py:108`) takes an already-validated `TaskDocument`, so it
can write no file carrying a key the model refuses. Only the durable-data **read** edge became
version-tolerant — this repository's own stated doctrine, not a new precedent: "The read is
deliberately the TOLERANT one ... the STRICT read is what the enforcement fold uses, and it still
raises" (`snapshots_impl/_runtime.py:121-123`).

`_UNKNOWN_FIELD_PASSES = 4` is **unproven-but-generous, not derived.** No measurement in this
change produced a prunable shape needing more than two passes, and the patch's original comment — one
retry per nesting level — was measured false and corrected: pydantic reports `extra_forbidden` for
every nesting level in a single error report (re-measured for this card: one report carried four
`extra_forbidden` locs across document, step, substep and section level, and the instrumented loop
reached a valid document in two passes). The bound's real job is to stop a loc this reader cannot
address from looping, so it is a stop, not a computation.

**Residual gap, documented in the code comment and deliberately not changed.** `_without_paths` walks
the raw payload by the loc's own keys; a loc pydantic *augments* has no raw key to walk and prunes
nothing, so the document is still withheld once the bound is spent. That is reachable for the `ref`
`SprintExecutionNode._lift_legacy_ref` invents for a legacy bare node (`tasks/document.py:212-219`) or
for a union branch label in an edge endpoint. It is fail-closed, not corruption; no writer produces
those shapes today; and closing it would change the semantics of the proven fix, so it is recorded
rather than repaired.

**Not the cause and not the fix:** `TASK_DOCUMENT_SUMMARY_LIMIT = 250` was measured irrelevant to this
defect — the withheld documents sat well inside the summary window, so the missing rows were never an
eviction or a tightened bound and raising the limit would not have restored them. The dashboard renderer
was not changed either; it was correct, and a truthy `match` is what the projection owed it.

**That bound no longer exists (260916-TDPU).** `TASK_DOCUMENT_SUMMARY_LIMIT`,
`SERIES_DOCUMENT_SUMMARY_LIMIT`, `_bounded_task_document_payloads` and `_stat_mtime_ns` are deleted, so
this reader projects **every** canonical task document under `tasks/<repo>/<task>/`; the measurement
above stands as the reason the bound was never load-bearing, not as a live constraint. The removal
rationale is recorded in the code at `_common.py:65-71`. See the 2026-09-16 entry below.

**Found for follow-up, not changed here:** a sixth same-class drop site outside this leaf's five, at
`snapshots_impl/_closeout_queue.py:33-36`.

## 260921-ICR-L42 The Body Read Opens Only What It Names

**What changed.** `read_task_document_body` used to call `_iter_task_document_payloads(tasks_root, now=now)`,
which enumerated and parsed the whole canonical corpus. It built `_master_docs_by_ref` from the result
for every document, including leaves and masters that have no graph and consume no master. The read now
resolves and reads the one requested file and takes its join table from `_graph_master_docs`. A leaf,
a master or a standalone document therefore lists no directory and reads no other file. A sprint lists
the repository folders and the task folders its graph names, and reads the files at those paths.

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

- The leaf design named "the governing master" as something to resolve. The body read does not open it,
  because no body field consumes a document's own master. Only sprint graph views consume masters.
  Byte identity across the corpus confirms nothing depended on it.
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
