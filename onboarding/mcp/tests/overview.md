# mcp/tests

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/tests/` |

## Governing Overview

[MCP package overview](../overview.md)

## Purpose

The Python test suite of the `agents_remember` package. The route holds the test modules
(`test_*.py`), the shared support modules and fixture files that several test modules use, the
pytest composition in [`conftest.py`](conftest.py.md), and the two test catalogs. Every support
module and most test modules have their own card, and the generated route index lists the carded
files. Six test modules have no card: `test_completion_relay_single_owner.py`,
`test_legacy_expectation_kinds_parse_only.py`, `test_lifecycle_owned_completion_relay.py`,
`test_memory_quality_is_independent_of_the_closeout_plane.py`,
`test_memory_scope_task_derivation.py` and
`test_terminal_enclosure_archive_sync_journal.py`. This overview describes what holds for the route
as a whole.

## Native Source And Protocol Qualification Tests

The route covers the Paseo host's own surfaces: runtime and settings admission, bridge and catalog
behavior, exact launch, replay and provenance, task tools, role messages and status, frames,
previous-host removal, and bounded sandbox process ownership. The cases are exact; a fixture or a
metadata field implies no paid turn, no universal containment and no semantic acceptance. The
assertion catalogs and the converted readers and writers keep their own tests in the same route.

## How A Test Run Is Composed

- `mcp/.venv/bin/python -m pytest` runs the unit population: the repository's default options
  select `-m "not integration"` and four workers. `-m integration` selects the integration
  population and `-m ""` selects both.
- [`conftest.py`](conftest.py.md) isolates the process: the candidate's source comes first on the
  import path, home and configuration directories are temporary, and inherited credentials and
  live-service opt-ins are removed.
- The lane of a test file decides its population. `conftest.py` reads the lane manifest when pytest
  is configured: the files of the `integration` and `stress-durability` lanes get the `integration`
  marker, and a run with `-m "not integration"` does not import them.
- The plugin `evidence_lanes` loads the lane manifest through its loader at collection. A manifest
  that the loader refuses ends the run with a usage error before any test executes, and each
  collected item gets the marker of its lane. The loader lists the repository's files through Git,
  so a test run needs a Git checkout.
- `pytest_collection_finish` in `conftest.py` counts the collected cases of both populations and
  ends the run when a count is above its budget. The two budgets are declared once, in the
  repository-root `pyproject.toml` under `[tool.pytest.ini_options]`.
- In an ordinary run an integration test gets the bound worktree services automatically; a unit
  test asks for the `worktree_services` fixture only when it needs that boundary.

## Test Policy

- A new case protects a distinct user operation, a consequential failure or an actual regression.
  Overlapping tests are extended, consolidated or replaced before a case is added.
- General policy forbids running this repository's suite inside a test or repeatedly scanning the
  repository to test the suite. The approved `MIK-R87@v1` rule13 is the specific bounded scanner
  exception: `test_suite_load_independence.py` checks timing syntax in `mcp/tests` and
  `mcp/test_support` (excluding the shared `waits.py`), and registered process-state syntax in
  `mcp/src/agents_remember`. It does not execute the repository suite.
  Four cases of `test_evidence_catalog_canonical_form.py` start a real pytest
  process on a small synthetic repository under the test's temporary directory, each call with a
  hard time limit.
- Coverage is diagnostic. No percentage and no changed-line floor obliges a test.
- An ordinary pytest run is development feedback. Only the pinned Dagger graph and the existing
  lifecycle owners produce certifying evidence.
- A test that a card or a document names and that does not exist is, as a rule, a deliberate
  removal and not a lost file. Commit `d3610903` ("Reduce test inventory and make coverage
  diagnostic") removes a large part of the test inventory on purpose, and many cards name it for
  their removed tests. Before a missing test is treated as an accident, find the commit that
  removed it with `git log -S '<test name>' -- mcp/tests`; the newest commit listed is the
  removal.

## The Two Test Catalogs And How A Test Module Is Registered

- [`test-evidence-lanes.toml`](test-evidence-lanes.toml.md): the lane of every test file. A test
  file without a lane line stops the test collection.
- [`evidence-lifecycle.toml`](evidence-lifecycle.toml.md): one row per governed test artifact
  (support module, fixture, recording) with its consumers, and one row per contract.
- [`test_evidence_catalog_canonical_form.py`](test_evidence_catalog_canonical_form.py.md): the cases
  for the catalogs' canonical form, the `--write` command and the union merge, over synthetic
  repositories and real Git.
- [`test_evidence_catalog_gate_boundaries.py`](test_evidence_catalog_gate_boundaries.py.md): the
  consumer oracle refuses a canonical catalog that no longer describes the source tree.
- [`test_dependency_ownership_ast_helpers.py`](test_dependency_ownership_ast_helpers.py.md): the
  census over the real repository, and the guard that the production-chain proof
  `test_lifecycle_owned_completion_relay.py` owns no governed artifact, computed from the catalog.
- [`_evidence_catalog_fixture.py`](_evidence_catalog_fixture.py.md): the builder of a valid,
  canonical synthetic catalog.

**Registering a test module.** A change that adds a test file adds one line with its path to its
lane in the lane manifest and runs
`python -m agents_remember_test_support.testing.evidence_lifecycle --project-root . --write` from
the repository root. The command puts the line in order and adds the file to every `consumers` list
of the lifecycle catalog that the source tree supports. Nothing else is edited for it: no test file
holds a digest, a row count or a note that has to follow. A change that deletes a test file runs
the same command, which removes the file's lane line and its consumer lines; where the file was the
only consumer of a row, the command leaves that list as written and the loader names the row. A new
governed support module or fixture also needs its own `[[artifact]]` row, which is written by hand. A Python file in
this route that is not a test module is governed and needs such a row, and so do the data files
that the catalog's card names.

**Canonical form and merging.** Both catalogs are kept in one canonical form: contract rows ordered
by `id`, artifact rows by `path`, every list ascending, without duplicates and with one path per
line. Both loaders refuse a catalog that is not in it and name the command. Git merges both
catalogs by union (`.gitattributes`), so two changes that add lines to the same list do not
conflict. A union merge can leave a line twice, leave a list out of order, bring back a line that
one side deleted, or interleave two rows. The loaders refuse a duplicate line, an unordered list,
the line of a file that no longer exists and a file that does not parse. The lane loader runs at
every collection, and the validator command (the same command without `--write`) loads both
catalogs.

## Reviewer operation and shared capture proof cards

- [test_review_read_latency.py](test_review_read_latency.py.md) drives the dashboard operation and protects exact supplied trees, canonical consumed task reads, bounded/failure-sensitive memo reuse and literal batched patches. Its counts of resolutions, captures and Git children do not depend on the machine.
- [test_reviewer_worklist_process.py](test_reviewer_worklist_process.py.md) (integration lane) proves the isolated worklist computation with real child processes: the child's answer equals the computation in the calling process, every transport failure is an explicit refusal that is not kept, identical requests share one child and the bound counts computations, a child and its Git processes do not outlive their requests or the dashboard, reviewer diffs do not depend on the user's Git configuration, tree reads run on their own threads, and creating a comparison pin is idempotent.
- [test_reviewer_worklist_reads.py](test_reviewer_worklist_reads.py.md) (integration lane) proves what the leaf-wide view and the invariant gate record as read and how a kept result follows those reads: task documents, settings, contracts, requirement packets, root directories and a ledger are changed under real child processes, and a kept view depends only on the task documents it read.

- The leaf-wide view captures nothing itself and is computed once per comparison. [498]
- The child's document, reads and body equal the computation in the calling process at two sizes. [499]
- The waiting bound counts computations, not the requests sharing them. [500]
- A kept view ignores every task document it did not read. [501]
- The gate's warm pass becomes the refusal when a packet locator is retargeted. [497]
- [test_worktree_candidate_capture.py](test_worktree_candidate_capture.py.md) protects the shared capture's exact state matrix, copied index time, trust flags, derived exclusions, conversion-rule boundary and real-index isolation.

## Operation witnesses and fixture ownership

The shared [wait helpers](../test_support/agents_remember_test_support/testing/waits.py.md) give ordinary operation waits a hang guard and diagnostic failure; they do not establish a performance requirement. Negative assertions follow the actual excluded operation's opportunity: held mutex/dispatch-lock contention, blocked control-authority dispatch, exact projector publication, resolve entry or completed durable-record reads. Deadline behavior uses injected owner-local time where available. A deliberate real expiry remains a behavior test with semantic outcomes, never an elapsed-speed ceiling.

- [conversation_open_test_support.py](conversation_open_test_support.py.md) owns the conversation launch and resolve-entry doubles.
- [eve_adapter_event_test_support.py](eve_adapter_event_test_support.py.md) owns the standing subscriber and exact completed-record-pass witness.
- [reviewer_worklist_process_test_support.py](reviewer_worklist_process_test_support.py.md) owns held real children, request-clock injection, occupied executor and process-tree observations.
- [knowledge_index_test_support.py](knowledge_index_test_support.py.md) owns the one same-size/same-second Git rewrite helper; its real clock alignment is the tested scenario and has a larger explicit guard.
- [test_serving_shutdown_drain.py](test_serving_shutdown_drain.py.md) witnesses cancellation drain before worker release and host close, then checks complete producers rather than a quiet time window.

## Where To Start

Module names begin with the area they test. The table names a starting module for concerns that
span several modules; the card of a module, where it has one, states what its cases assert.

| Concern | Start with |
| --- | --- |
| Knowledge as text files: formats, the curator writer, the validator, history files | `test_knowledge_file_formats.py`, `test_knowledge_writer.py`, `test_knowledge_validator.py`, `test_knowledge_history_files.py` |
| The change-to-knowledge worklist and the mandatory closeout gate | `test_knowledge_worklist.py`, `test_knowledge_closeout_gate.py`, `test_knowledge_gate_routes.py` |
| The onboarding refresh gate, unexplained changes, planned effects, reconsideration | `test_onboarding_trace_gate.py`, `test_unexplained_change_disposition.py`, `test_planned_knowledge_effects.py`, `test_reconsideration_surfacing.py` |
| The derived knowledge index and the knowledge readers | `test_knowledge_index.py`, `test_knowledge_reader.py`, `test_knowledge_reader_tree_coverage.py`, `test_knowledge_leaf_read.py` |
| The reviewer on Git trees | `test_review_git_trees.py` |
| Curation through the real writer | `test_curator_scope.py`, `test_curator_realization_authoring.py`, `test_curator_family_authoring.py` |
| Memory quality runs and citation repair | `test_memory_quality_runs.py`, `test_citation_document_transaction.py`, `test_memory_citation_fix.py` |
| Memory ledger and attribution | `test_memory_ledger.py`, `test_memory_attribution_producers.py`, `test_memory_backfill.py` |
| Task documents | `test_task_document.py`, `test_task_documents_graph_projection.py`, `test_leaf_doc_master_link_binding.py` |
| Closeout and integration delivery | `test_transaction_only_worktree_delivery.py`, `test_checkpoint_landing_end_to_end.py` |
| Worktree sync and source lineage | `test_worktree_sync.py`, `test_sync_parked_candidate.py`, `test_source_lineage.py` |
| Pause, activation and concurrency of atomic masters | `test_pause_stop_only_end_to_end.py`, `test_pause_is_not_publication.py`, `test_atomic_series_activation.py`, `test_cross_master_concurrency.py` |
| Git runner and protected integration refs | `test_git_command.py`, `test_integration_branch_authority.py` |
| Checkout coordination and host locks | `test_checkout_coordination_isolation.py`, `test_dagger_registry_lock.py` |
| Durable stores and lock order | `test_durable_store_contract.py`, `test_cross_store_lock_order.py` |
| Terminal catalog, liveness and evidence | `test_terminal_catalog.py`, `test_terminal_liveness.py`, `test_terminal_evidence_mapping.py`, `test_terminal_evidence_cursors.py` |
| Serving observation loop and notifier handoff | `test_serving_observation_loop.py`, `test_serving_startup_prime.py`, `test_serving_notifier_handoff.py` |
| State-signal relay and owner wake | `test_state_signal_relay.py`, `test_state_signal_boundary_delivery.py`, `test_state_signal_restart_recovery.py`, `test_lifecycle_owned_completion_relay.py` |
| Conversation projection and harness submission | `test_conversation_active_service.py`, `test_harness_submission_authority.py`, `test_harness_control_ipc.py` |
| Certification registry and certificates | `test_certification_rail_registry.py`, `test_gate_certificate_authority.py` |
| The public tool surface and its refusals | `test_tools.py`, `test_tool_refusal_conformance.py` |
| The test suite's own rails: lanes, budgets, bootstrap, file size, layering | `test_evidence_lanes.py`, `test_suite_budget.py`, `test_pytest_bootstrap_boundaries.py`, `test_file_size_detector.py`, `test_layering.py` |

## 260928-MIK-L99 — a leaf's agents hand over to each other

The suite gained the leaf-handover tests (`test_leaf_handover.py`, `test_leaf_handover_review_rounds.py`), the retirement-wording guard test (`test_leaf_retirement_wording.py`) and the wording-guard rework in `test_role_instruction_wording.py`. The new modules have their own cards, and have their own cards.

## 260928-MIK-L93 — a question for the developer goes up the chain

The new `test_developer_question_wording.py` joins the unit-regression lane: it requires the parent channel, recovery and answer provenance in every parentable role and the three operations, the starter roles' relay and permission-notice duties, the leaf ownerRelation peer routes, and the independent detection of each exact retired directive. `test_role_instruction_wording.py` now compiles the parent condition for all six parentable roles and the renamed ownerRelation test; the two evidence catalogs list the new module.

## Master Retirement, Finalization And Abandoned-Row Cases

[test_abandoned_series_closeout.py](test_abandoned_series_closeout.py.md) (unit lane) proves that an abandoned row needs no landing and a landed abandoned row refuses by name.
[test_master_retirement.py](test_master_retirement.py.md) and [test_standalone_master_retirement.py](test_standalone_master_retirement.py.md) (integration lane) prove the retire operation on a sprint's master and on a
master no sprint commands, the three finalization outcomes, the retry rules and the protected proof. `test_review_artifact_cleanup.py` also proves
that a repeated archive-hook attempt keeps its receipts. The test catalog files `evidence-lifecycle.toml`, `test-evidence-lanes.toml` and
`test_dependency_ownership_ast_helpers.py` register the three new modules; the catalog's rows and counts are computed from the source tree by the canonical writer command, so this card states none of them.

- A landed abandoned row refuses by name. [505]

- The partial-hook-failure retry keeps the retirement and cleans up only. [506]

- Finalizing a master no sprint commands keeps it and names the retire route. [504]

## Evidence

- The default options select the unit population and four workers. [1]
- The two case budgets are declared in the repository-root configuration. [2]
- The isolation of the pytest process and the two registered plugins. [3]
- Integration files are not imported in a run that excludes integration. [5]
- The collected cases are counted against the two budgets. [6]
- The collection hook loads the lane manifest and marks each item with its lane. [7]

- General test policy forbids recursive suite execution and repeated repository scans to test the suite; coverage stays diagnostic and the canonical-form module uses four real-pytest cases in temporary synthetic repositories. The approved MIK-R87@v1 rule13 bounded timing/process-state scanner is the specific exception described in Test Policy and the scanner evidence below. [25]

- Approved MIK-R87@v1 rule13 bounds the Python timing scan to mcp/tests and mcp/test_support, excluding the shared waits.py; it reports syntactic timing violations without running the repository suite. [502]
- The same approved bounded scanner compares syntactic process state under mcp/src/agents_remember with the exact closed register. [503]
- The real catalogs load through both loaders. [11]
- The production-chain proof owns nothing in the catalog. [12]
- The union merge attribute for both catalogs. [13]
- Which files of this route are governed test artifacts. [15]
- The command removes the lane line and consumer lines of a file that no longer exists. [16]

- The Paseo launch, replay and runtime cases. [21]
- The task-scoped MCP reader cases. [18]
- The previous-host removal guard. [19]
- The bounded sandbox process cases. [20]

- The lane manifest is read at configuration for the integration files. [22]
- The lane loader refuses a test file without a lane and a lane list that is not canonical. [26]
- The lifecycle loader refuses a catalog that is not canonical or does not agree with the source tree. [24]

## 260928-MIK-L96 The host test population

The tests route gained seven host modules (install contract, install no-stop, Node, start, dashboard host, release contract, host environment) plus additions to the existing sandbox and Paseo tests; the lane and lifecycle catalogs were extended for them.

- The install-contract module. [27]
- The no-stop module. [28]
- The node module. [29]

## Closed-leaf agent archive suite (MIK-R76)

`test_leaf_agent_archive.py` is the focused proof suite for the closed-leaf archive: receipt
selection and settlement, the prepared-start closing mark, debt recovery through the existing
observer, truthful outcomes, bounded budgets and archive-before-removal ordering. It is registered
as a consumer in both governed test-evidence catalogs.

