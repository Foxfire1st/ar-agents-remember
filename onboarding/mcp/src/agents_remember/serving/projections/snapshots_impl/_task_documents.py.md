# mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py` |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-09-28T16:27:07+02:00 |
| lastVerifiedCommitHash | `58e22246cc09ef0ee12095e284a111a475081c38` |
| lastVerifiedCommitDate | 2026-09-28T16:46:12+02:00|
| governingOverview      | `../overview.md`                                       |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own top-level surface is listed in Code Commentary; no cross-file citation rows are needed for this split module. | — | — |
| Canonicalized requirement text reader for typed packet refs. | `_requirement_reader_text` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:563-566 |
| Canonicalized open-question reader for typed acceptance obligations. | `_question_reader_text` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:569-572 |
| Body revision hashing of typed intent slots. | `_task_doc_body_revision`; `_task_intent_body_value` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:675-705 |
| The tolerant read edge: strict first, only `extra_forbidden` keys dropped, every other failure still `None`. | `_projected_document` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:79-103 |
| Targeted pruning of exactly the addressed keys from a deep copy. | `_without_paths` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:106-121 |
| The pruning pass bound and the residual unprunable-loc gap it exists to stop. | `_UNKNOWN_FIELD_PASSES` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:72-79 |
| The repository's own stated read-versus-enforcement split this change follows. | "The read is deliberately the TOLERANT one" | mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:121-123 |
| Authoring strictness is untouched: the strict base model, and the step-level `note` a newer build writes. | `_Doc`; `Step.note` | mcp/src/agents_remember/tasks/document.py:73-76; mcp/src/agents_remember/tasks/document.py:111-121 |
| The durable-data writer takes an already-validated document, so it can write no unknown key. | `write_task_doc` | mcp/src/agents_remember/tasks/store.py:108-109 |
| The reader projects every canonical task document, and the removed summary bound with the rationale for its removal. | `_master_docs_by_ref` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:463-491; mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:65-71 |
| The dead-text element a withheld document produced, unchanged by this leaf. | "not authored as a task document yet" | dashboard/src/panels/detail-panel/taskReader.tsx:434-434 |
| The legacy-bare-node `ref` synthesis that leaves one loc path unprunable. | `_lift_legacy_ref` | mcp/src/agents_remember/tasks/document.py:212-219 |
| The sixth same-class drop site, in the closeout-queue reader rather than this leaf's five and left unchanged. | `read_closeout_queues` | mcp/src/agents_remember/serving/projections/snapshots_impl/_closeout_queue.py:22-38 |
| The on-demand body read: resolve, confine under `tasks/`, read one file, project with the graph-only join table. | `read_task_document_body` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:161-201 |
| The body read's master join table: none without a graph, otherwise only the graph-named masters that carry the schema. | `_graph_master_docs` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:204-224 |
| The named-path probe that returns exactly the enumeration's subset for those tails, in the same order. | `_canonical_task_json_candidates` | mcp/src/agents_remember/serving/projections/snapshots_impl/_common.py:93-113 |
| The only consumer of `master_docs`, which looks masters up solely by graph ref. | `_execution_graph_view` | mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:420-460 |
| The HTTP handler that calls the body read: 503 before the first projection, 404 when the read returns `None`. | `_task_document_response` | mcp/src/agents_remember/serving/_app_routes.py:109-121 |
| The regression evidence: byte identity against the corpus-wide join, and the same touched files at 4 and 40 unrelated tasks. | `test_every_document_kind_projects_the_same_body_as_the_corpus_wide_join`; `test_one_body_read_touches_the_same_files_whatever_the_corpus_size` | mcp/tests/test_task_document_body_lookup.py:138-159; mcp/tests/test_task_document_body_lookup.py:190-228 |


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

## Update History
- 2026-09-28T16:27:07+02:00 — 260921-ICR-L42 curator (uncommitted candidate tree `27409ea9f3320689c28c6a810c9a88afa288bbba` over code base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): **the body read no longer enumerates the task corpus.** Documented `_graph_master_docs` and the new body-read contract. Added three invariants: no corpus enumeration on the body path, the load-bearing schema filter, and byte identity through the same-order subset. Added the L42 section with the accepted scope choices and the negative knowledge. **Corrected a current-state falsehood:** the L12 section said both readers build the master join table from the whole projected set, which is now true only for the summary reader. Removed the line-number annotations from the L10 and CCR prose; every insertion moves them, and the reference table carries the current ranges. Re-pointed the table rows this change moved (+1 above the body read, +28 below it). The `_common.py:63-69` rationale cites now read `65-71`. No stamp was advanced; closeout owns it.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_requirement_reader_text` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:535-538. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_question_reader_text` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:541-544. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_projected_document` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:78-102. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_without_paths` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:105-120. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T07:33:51+00:00: Generated citation repair: `_task_doc_body_revision`; `_task_intent_body_value` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:647-669; mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:672-677. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `_requirement_reader_text` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:535-538. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `_question_reader_text` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:541-544. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `_projected_document` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:78-102. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `_without_paths` repointed to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:105-120. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:587 to the row 80 of this card as the citation for `_task_doc_body_revision`: no cited file carried the construct, and the checker named line(s) [587, 647] in this file as its live location
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_task_doc_body_revision` in the row 80 of this card from mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:672-674 to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:647-648, the extent of the construct the claim is about (the checker named line(s) [587, 647] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_task_intent_body_value` in the row 80 of this card from mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:647-648 to mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:672-674, the extent of the construct the claim is about (the checker named line(s) [650, 654, 672] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/src/agents_remember/serving/projections/snapshots_impl/_task_documents.py:672-674 in the row 80 of this card; the repetition added no pooled evidence
- 2026-09-16T14:20+02:00 — 260916-TDPU (`ar/260916-tdpu`, base `67b21aeb`) curator: **the
  task-document summary bound is removed, and this card now states the uncapped contract.** Deleted
  from the serving projections were `TASK_DOCUMENT_SUMMARY_LIMIT`, `SERIES_DOCUMENT_SUMMARY_LIMIT`,
  `_bounded_task_document_payloads` and `_stat_mtime_ns`; all three readers now project every
  canonical task document under `tasks/<repo>/<task>/` (measured on the live root at this change:
  517 canonical documents, 462 subTask / 55 master, against the old cap of 250 — 267 documents were
  withheld before it). Corrected the false current-claim prose: the Repo-Internal References row that
  asserted the limit was "left unchanged" cited a `_common.py:24-24` line that no longer holds any
  limit, and is replaced by the reader's actual contract plus the rationale anchor at
  `_common.py:63-69`; the L12 section no longer says `_master_docs_by_ref` builds its join table "from
  the bounded payload window" or that root documents "are never evicted" (nothing is evicted now); the
  L10 section's "`TASK_DOCUMENT_SUMMARY_LIMIT = 250` ... is unchanged" is corrected in place, with the
  historical measurement retained as the reason the bound was never load-bearing. The code-side
  falsehood of the same class — `_master_docs_by_ref`'s docstring at
  `_task_documents.py:442-443`, which still claimed root documents were exempt from a bounded payload
  window — is corrected in the same change set. Rationale recorded in the code at `_common.py:63-69`:
  the eviction was silent and untested, so an operator saw a master whose sub-task rows were not
  clickable with no diagnostic and no way to tell a missing document from an unreadable one. Ranges
  this entry adds or touches were read back at their current positions (`_master_docs_by_ref`
  `435-463`, `_common.py:63-69`); other citation ranges on this card are unchanged by this leaf and
  were not re-derived — the boundary check reports that pre-existing drift separately. Verification
  metadata remains closeout-owned; no verification stamp advanced and no code commit exists yet.

- 2026-09-14T10:16+02:00 — 260913-LCA-L10 (curator, uncommitted change set on `ar/260913-lca-l10-ar`,
  base `4214d7a1`): the module's read edge became version-tolerant. Documented `_projected_document`
  as the module's single `TaskDocument.model_validate` site and the five call sites now routed through
  it, the `extra_forbidden`-only tolerance with every other failure still withheld, the unchanged
  authoring strictness (`extra="forbid"`, `task_doc`, `write_task_doc`) and its doctrine precedent at
  `_runtime.py:121-123`, `_UNKNOWN_FIELD_PASSES = 4` as **unproven-but-generous** (no prunable shape
  needed more than two passes; the original "one retry per nesting level" rationale was measured false),
  and the residual unprunable-loc gap left fail-closed on purpose. The card previously recorded only
  that these readers project task documents, never that an unparseable one was deleted whole; the new
  section states the read edge's actual contract instead — it withholds only what fails for a reason
  other than an unknown key, and no authoring refusal was loosened. Recorded that
  `TASK_DOCUMENT_SUMMARY_LIMIT = 250` is unchanged and measured irrelevant, and that the dashboard
  renderer (`taskReader.tsx:434`) was correct and untouched. **Re-pointed the card's own citations**,
  which this change shifted by the +52…+57 lines its helper block and five call-site rewrites added
  (`_requirement_reader_text` 494 → 546, `_question_reader_text` 500 → 552, `_task_doc_body_revision`
  606 → 658, `_task_intent_body_value` 631 → 683), and added the nine rows above. Metadata stamps
  remain closeout-owned; no verification stamp advanced and the code commit does not exist yet.
  Measurement method for the re-measured pass bound: both files of this change set plus the module's
  published helpers imported from the code worktree under the repo's Python 3.13 venv with
  `PYTHONDONTWRITEBYTECODE=1`, a four-nesting-site unknown-key payload validated, and the pruning loop
  instrumented to count passes.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the serving task-document readers now canonicalize typed requirement/accepted-obligation slots and
  include them in `_task_doc_body_revision`; documented the stable reader-string and digest path.
  Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: documented projection of audited discarded-unstarted task history. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   both readers project the render-ready `executionGraphView`; `_task_doc_node` split into `_reader_fields` + `_execution_graph_fields` with `_TaskDocProjectionOptions`, `_master_docs_by_ref` join table, and the `_execution_graph_view` serving seam (L12-R4). Verified at code commit b7f2c8e2.

- 2026-08-20T04:26+02:00 — 260815-DAG-L14: `_task_doc_node` passes the typed `masterRef` through
  and projects first-class `seats` (`TaskSeatNode`); `_task_doc_body_revision` now covers
  `subTasks` + `seats` so an open sprint reader refetches on linkage/seat edits. Verified at code
  commit 9c3180c1.

- 2026-08-19T08:55+02:00 — 260815-DAG-L11: `_task_doc_node` now projects `executionWaves` as
  `TaskExecutionNode` rows (each persisted `SprintExecutionNode` re-validated into the served
  segment-aware projection type). Verification remains closeout-owned.

- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1: task snapshot hydration now carries explicit master
  nature and sprint graph, derives deterministic waves, and includes both fields in body revision identity.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
