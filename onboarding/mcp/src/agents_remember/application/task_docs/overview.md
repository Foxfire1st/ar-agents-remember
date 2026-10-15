# mcp/src/agents_remember/application/task_docs

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/application/task_docs` |

## Governing Overview

[application overview](../overview.md)

## Purpose

This package owns the application seam for task-document authoring: operation dispatch, candidate validation, publication, checklist edits, execution-graph authoring, sprint linkage, and master retirement. `task_ref` provides typed task references and `task_reopen` provides the leaf-reopen route. Shared concerns have separate owners so the dispatcher does not duplicate their rules.

## Hot Path Summary

task_doc_field_homes centralizes newly reserved section/head-note remedies and validates explicit nonempty waitsFor writes against same-master membership, self-reference and cycles before publication. Legacy sections/notes remain editable and removable. task_doc_content_edits owns content operations; task_doc_tools composes the prepared candidate with existing proof and publication guards. Dependencies are information, not a new start/refusal gate.

task_doc authoring no longer exposes successful get/read_steps projections or step_payloads. The early operation-removed answer guides canonical JSON/rendered-file reading. Ordinary writes deliver bounded phrases, create retains renderedPath, changed reviewState stays visible, and dry answers carry wouldLose/diff with independently retained locations; rich identity/preview/masterSync remains whole-result custody and a validly addressed parent-sync failure is an answered refusal. Invalid caller master references are refused by the shared master_json_path_from_ref resolver with TaskDocError during candidate validation after retirement-proof comparison, before publication; a changed or Order-refreshed parent must also pass the in-place document guard. Linkage reporting writes its facts JSON and delivers counts/location; attach/detach retain per-document previews internally. Shared task_doc_phrases owns the actual mutable allowlist, excluding seriesContractPath/enclosures. Publication refreshes the own leaf plus declared requirement copies with rollback, without turning copies into task authority. Strict model facts come from models/task_doc.py; no historical pending-model statement certifies a live session.

`task_doc_tool` resolves the task address, dispatches special operations or prepares an ordinary candidate, validates that candidate, and publishes or previews it. Publication rechecks accepted source bytes, derives affected projection scopes, writes task truth, invalidates those scopes, and rebuilds projections independently. `task_unstarted_evidence.py` checks actual code/memory-content and integrated commit cells; an existing enclosure is independent started evidence, and task, locator, lifecycle-operation, seat, and report facts also participate.

## Construction

### Dispatch And Candidate Validation

> **Retained historical source account — superseded by the current route account:**
> The MCP payload adapter calls `task_doc_tool`. The dispatcher handles create, replace, field and checklist edits, review operations, and special operations. Sprint linkage and execution-graph authoring publish through their own functions; their operation payloads are merged with the standard document identity through `_sprint_doc_identity`. `read_steps` is a focused read-only checklist projection.

> **Retained historical source account — superseded by the current route account:**
> Ordinary candidates pass retirement-proof preservation, disposition and route-review authority, unresolved-unit preservation, terminal-status checks, master completion, register shape, and execution-topology validation before publication. Route-review preparation binds the selected source path and contract context. The exact semantic admission predicate inside that owner remains a bounded verification uncertainty here. The existing strict `TaskDocResponse` wire-shape claim likewise remains pending confirmation of its response-model owner.

### Publication And Projection Scope

> **Retained historical source account — superseded by the current route account:**
> `task_doc_publication.py` owns accepted JSON/Markdown source snapshots, exact source-conflict reporting, prepared-document publication, and preview. Dry-run preflight checks source currency and resolves the affected scope union through the same owners used by apply. Publication also refreshes task-document copies; a copy-refresh failure attempts restoration of the accepted source snapshots.

`task_doc_queue_scope.py` uses the closed field-effect classification to skip changes that do not invalidate projections and derive the canonical old/new affected sprint union for those that do. Task truth is the authoring authority; queue state is a disposable scheduling projection. A planning change does not itself establish lifecycle evidence or change downstream activation state. Per-contract activation and retained sync state remain downstream authorities whose next-admission behavior is not independently established by this bounded read.

The shared `publish_task_fact_mutation` implementation validates, derives scopes, runs publication, and then invalidates and rebuilds projections. Invalidation failures and rebuild exceptions become projection effects. It does not itself acquire a publication lock or roll back task truth when invalidation fails. The shared function supplies no publication/invalidation atomicity or lock proof by itself. Locked atomic publication remains the standing intent; this account describes the observed sequential publisher and does not infer a global caller-lock absence or endorse a changed requirement.

### Graph Titles And Raw Sections

`task_doc_graph_titles.py` rejects publication batches containing more than one graph-bearing document and builds the sole in-memory batch title context. Prepared and ordinary publication defer on-disk graph-title reads to their publisher callbacks. The callbacks are not evidence of a lock: the shared publication implementation inspected here has no lock acquisition.

Create and replace share `task_doc_section_scaffolding.py`. It validates a supplied `sections` container as a list whose members are mappings before changing it, then appends missing canonical register sections when the payload is a sprint. Model and register validators retain semantic ownership; malformed raw containers are not coerced.

### Leaf Construction

`_build_doc` rejects the removed `light` kind. Without an explicit kind it derives `subTask` from a leaf contract and otherwise defaults to `master`. With a resolved contract it stamps the series path and, for a leaf contract, enclosure registration and applicable lifecycle identity.

Without a contract, a non-master candidate passes `_require_bindable_leaf_authoring`. The helper permits planning when `task_root/task.json` exists and otherwise refuses with the missing path, derived fields, and remedy. Its stated intent is master-first planning followed by first-start/attach binding of `seriesContractPath` and `enclosures`. Its actual predicate checks path existence; it does not read that file to prove it is a valid master. The downstream binding guarantee is retained as stated intent, pending verification of the start/attach publishers.

### Checklist Operations

`task_doc_tools.py` registers thin adapters; `task_doc_steps.py` owns checklist addressing and mutations. `parent` selects the namespace for an existing target, and zero or multiple matches refuse. `set_step` updates one existing unit without creating it. `add_step` creates one unit, requires an ID and title, and refuses an existing ID in that scope. `remove_step` deletes one existing unit with a nonblank reason and appends an audit decision. `skip_step` retains an unresolved unit, marks it done, and records its intentional-skip disposition and decision.

A reasoned removal may delete a done unit and may operate on a Completed document. These are explicit exceptions preserved in the implementation. Removal means that the unit should never have existed; skipping means that a planned unit was deliberately not done. They remain distinct operations, and the dispatcher must not introduce a second addressing rule.

### Declared Knowledge Effects

`expectedKnowledgeEffects` is settable through `set_field`. The resulting whole document is model-validated before publication. The declaration belongs to a leaf, must be nonempty when present, and cannot repeat a subject/effect pair. Subject and requirement-reference forms, effect vocabulary, and strict entry shape are model concerns; `null` clears the declaration.

The field is classified as normative intent and participates in task-intent projection. An absent declaration is omitted from the canonical projection, so clearing only this declaration restores the otherwise-identical undeclared intent. The declaration model checks shape without reading knowledge; an unknown subject's worklist handling is stated by the owner but was not independently inspected here. The existing architect/approved-worker authorization rule is procedural rather than a demonstrated per-field role gate.

### Sprint Linkage And Retirement

`task_sprint_linkage.py` dispatches five operations: attach, detach, retire, archive sprint, and linkage report. `archive_sprint` delegates to its sibling sprint-archive owner. `task_doc.retire_master` archives an individual master, whether or not a sprint commands it; `task_doc.archive_sprint` is the separate whole-sprint route.

[task_master_retirement.py](task_master_retirement.py.md) owns both retirement paths. For a commanded master, it records the sprint candidate and archives the folder in one publication callback, restoring the folder and sprint source pair if an exception occurs before archival. For a master commanded by no sprint, it writes proof into the master's folder and moves that folder, restoring the folder and newly created proof state on failure. These restoration rules do not establish a global lock or atomic queue-invalidation guarantee.

[task_retirement_shared.py](task_retirement_shared.py.md) supplies the request payload, nested-master refusal, and archive hook. The hook delegates review-artifact cleanup with both repository paths and reports caught exceptions as failures. A hook failure leaves the retirement retained and reports `retired-with-hook-failures`, `ok=false`, and a same-request retry for the hook. [task_retirement_authority.py](task_retirement_authority.py.md) prevents generic edits from changing complete retired rows, including proof, name, scope, and status.

[task_sprint_context.py](task_sprint_context.py.md) holds request, sprint-reading, candidate-validation, transaction, and preview helpers; [task_sprint_candidates.py](task_sprint_candidates.py.md) holds detach construction and `SprintLinkageError`; [task_execution_graph_mutations.py](task_execution_graph_mutations.py.md) holds graph-authoring models and handlers, including the retirement edge-removal helper. Their detailed shared-helper predicates and the retirement sprint-edit caller remain bounded verification uncertainties.

### Recovery And Refresh Checks

Unstarted-task evidence is derived from canonical task and lifecycle facts rather than waiting-queue state. Missing, unreadable, and started evidence remain distinct; commit evidence uses the four actual output cells, while a readable enclosure independently establishes started evidence.

The shared `validate_memory_refresh_attestations` composes sidecar and route-overview body checks, collecting either surface's error before refusing. A current memory-quality caller supplies separate evidence for the two surfaces. The original assertion that curator preparation and closeout each call it independently is retained as an integration claim awaiting confirmation of both caller paths; it is not evidence that validation ran for this proposal.

## Invariants And Boundaries

- Task-document publication and rendering authority must remain explicit and centralized. The package calls shared `tasks.store` writer APIs; the application seam is not itself the complete low-level writer implementation. The reviewed writer authority lives in `mcp/test_support/agents_remember_test_support/code_quality/single_owner.py`. The allowlist is enforcement source, not an acceptance result of this account.
- Task truth owns authoring. Waiting projections must not freeze otherwise-valid task edits or erase durable claimed/running/commit lifecycle evidence. The exact lifecycle-preservation predicates were not inspected here.
- Locked, atomic task-truth publication plus projection invalidation remains standing intent. The inspected shared implementation performs sequential publication and invalidation, reports invalidation failure, and contains no lock acquisition; the discrepancy is disclosed above.
- A publication batch admits at most one graph-bearing document, with a shared cardinality owner. No split retry or silent title fallback is part of that owner's implementation.
- Raw-section scaffolding validates the entire supplied container/member shape before mutation and preserves typed errors.
- Leaf planning requires the helper's existing `task.json` predicate when no contract is resolved. Valid-master authority and downstream lifecycle binding must not be inferred solely from that existence check.
- Commanded-master completion uses `tasks/readiness.py::master_is_terminal`: abandonment is terminal without resolving remaining planning rows; Completed is terminal only when there are no completion blockers. The topology route still names every incomplete commanded master.
- Generic task edits preserve complete retired rows. Retirement and intentional checklist removal retain their explicit audit requirements.
- Declared knowledge effects are leaf-only normative task intent. Role authorization remains procedural; declaration-shape validation does not establish that a knowledge subject exists.
- Ordinary declaration handling does not read knowledge. Retirement delegates cleanup with the memory-repository path, so the original package-wide claim of no memory-repository contact is too broad. Direct coordination-ledger access was not independently established or excluded by this bounded read.

## Lifecycle And Historical Context

The prior card records that these modules moved from flat `application/` into this package, and that extracting the step plane reduced a dispatcher reported at 1,243 lines against an armed 1,200-line limit. Those are historical accounts, not current size or acceptance evidence; their historical authority was not inspected.

The prior card also records developer authorization of reasoned removal from done units and Completed documents, architect/approved-worker authorship of knowledge-effect declarations with adversarial packet review, and the standing restriction that no real task document may carry the field before the L37 install because older installed runtimes reject unknown fields. The removal exceptions are visible in current source. The procedural rulings, install milestone, and current installed-runtime authority are not resolved here; no current lifecycle status or release acceptance is asserted.

The existing statement that finalizing a master never archives it remains an integration claim pending inspection of the finalization owner. No tests, validation commands, writes, or acceptance actions were executed for this proposal.

## External grant display, separate authoring

> **Retained historical source account — superseded by the current route account:**
> Task get/preview may display readable external grants; publication reads a batch-local census, but grants are not authored TaskDocument fields. Branch review uses explicit canonical leaf opt-in and current grant with exact series binding. Enclosed leaf start/attach keeps its enclosure; granted role preparation does not create one.

## Evidence


- **Retained historical source account — superseded by the current route account:** Task-first publication and projection refresh, with shared preview and source preflight; atomic-lock intent has the disclosed discrepancy. [1]
- **Retained historical source account — superseded by the current route account:** Zero-or-one graph-bearing publication batch and in-memory title context. [2]
- **Retained historical source account — superseded by the current route account:** Atomic raw-section shape validation and missing-register scaffolding. [3]
- **Retained historical source account — superseded by the current route account:** The step plane owns exact addressing, mutations, and the focused read projection. [4]
- **Retained historical source account — superseded by the current route account:** The settable flat fields include the knowledge-effect declaration. [5]
- **Retained historical source account — superseded by the current route account:** Execution evidence checks real code and memory output cells. [6]
- **Retained historical source account — superseded by the current route account:** Canonical task, locator, enclosure, operation, seat, and report facts determine unstarted evidence. [7]
- **Retained historical source account — superseded by the current route account:** The sprint retirement route publishes the sprint edit with the folder move and restores sources and folder on pre-archival failure. [8]
- **Retained historical source account — superseded by the current route account:** The lone-master route writes its proof into the master's folder and moves that folder. [9]
- **Retained historical source account — superseded by the current route account:** Caught archive-hook exceptions are reported failures. [10]
- **Retained historical source account — superseded by the current route account:** Generic task-document edits preserve complete retired rows. [11]
- **Retained historical source account — superseded by the current route account:** The shared fact publisher performs publication, then invalidation and independent rebuild without acquiring a lock in this function. [12]
- **Retained historical source account — superseded by the current route account:** The no-contract leaf guard tests whether task.json exists; its valid-master and first-binding descriptions are stated intent. [13]
- **Retained historical source account — superseded by the current route account:** Commanded-master completion requires abandonment or Completed without completion blockers. [14]

- task_doc authoring no longer exposes successful get/read_steps projections or step_payloads. The early operation-removed answer guides canonical JSON/rendered-file reading. Ordinary writes deliver bounded phrases, create retains renderedPath, changed reviewState stays visible, and dry answers carry wouldLose/diff with independently retained locations; rich identity/preview/masterSync remains whole-result custody and a validly addressed parent-sync failure is an answered refusal. Invalid caller master references are refused by the shared master_json_path_from_ref resolver with TaskDocError during candidate validation after retirement-proof comparison, before publication; a changed or Order-refreshed parent must also pass the in-place document guard. Linkage reporting writes its facts JSON and delivers counts/location; attach/detach retain per-document previews internally. Shared task_doc_phrases owns the actual mutable allowlist, excluding seriesContractPath/enclosures. Publication refreshes the own leaf plus declared requirement copies with rollback, without turning copies into task authority. Strict model facts come from models/task_doc.py; no historical pending-model statement certifies a live session. [15]
