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

The converted-drift module (`test_converted_onboarding_drift.py`, one test per packet rule) rides
the same registration: one lane line in `unit-regression` and consumer lines wherever the lifecycle
catalog supports it.

**Canonical form and merging.** Both catalogs are kept in one canonical form: contract rows ordered
by `id`, artifact rows by `path`, every list ascending, without duplicates and with one path per
line. Both loaders refuse a catalog that is not in it and name the command. Git merges both
catalogs by union (`.gitattributes`), so two changes that add lines to the same list do not
conflict. A union merge can leave a line twice, leave a list out of order, bring back a line that
one side deleted, or interleave two rows. The loaders refuse a duplicate line, an unordered list,
the line of a file that no longer exists and a file that does not parse. The lane loader runs at
every collection, and the validator command (the same command without `--write`) loads both
catalogs. The lifecycle catalog's consumer lines pin the live set: after any merge, a consumer
line for a file that no longer exists is refused, and restoring the base file plus the live
consumer lines is the repair.

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
| The tool entry-point sweep judging delivered answers | `tool_entry_point_world.py`, `test_tool_entry_point_sweep.py`, `test_tool_entry_point_controls.py`, `test_tool_entry_point_valid_progression.py` |

## Tool Entry-Point Sweep

The sweep over every public tool validates each call's whole result — read back from the file the delivered answer names in `log`, under the tool's registered model — and judges the delivered answer in its own shape: none of the four envelope fields, and no key that neither the whole result at the same place nor the shaping's framework keys account for. A missing or unreadable whole-result file is an unvalidatable finding, never a fallback to the delivered answer. Every tool and every aspect runs on its own subTest, and one tool's deadline never keeps the tools behind it unjudged. The pins record the measured surface with bidirectional exactness: the four lifecycle raisers owned by L111 and the bare `memory_quality_check` answer owned by L110; a repair removes its entry in the same change.

- A returned call is judged from the whole result and the delivered answer through one shared classifier. [1705]

- The sweep judges every tool and aspect on its own subTest with the pins exact in both directions. [1704]

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

- The install-contract module. \[27] [1701]

- The no-stop module. \[28] [1702]

- The node module. \[29] [1703]

The curator-authoring lane row for test_curator_scope.py, test_curator_realization_authoring.py and test_curator_family_authoring.py is gone with its modules under the catalog rewrite rule (rows whose owner and evidence files are both gone are removed); no replacement row names them.

## Closed-leaf agent archive suite (MIK-R76)

`test_leaf_agent_archive.py` is the focused proof suite for the closed-leaf archive: receipt
selection and settlement, the prepared-start closing mark, debt recovery through the existing
observer, truthful outcomes, bounded budgets and archive-before-removal ordering. It is registered
as a consumer in both governed test-evidence catalogs.
## CCR-R12@v5 Transaction-Only Delivery Route

`test_transaction_only_worktree_delivery.py` exercises real public closeout and paired integration. It checks actual code/memory refs and the memory-content `Code-Commit:` trailer, source movement refusals, configured-hook behavior, interrupted recovery and cache rebuilds. Missing, malformed or changed cache bytes do not create commit objects or gate delivery. The suite retains real content/ref failures instead of replacing them with cache checks. This overview describes coverage, not a current aggregate test result.
## Development And Certification Policy

Ordinary Python development is supported directly through `mcp/.venv/bin/python -m pytest`; four workers run the isolated unit population. `-m integration` selects the small real-boundary population and `-m ""` selects both. Focused file/node execution, including serial debugging, is valid development work and does not acquire certification authority. **The budgets are declared once, in the repository-root `pyproject.toml` under `[tool.pytest.ini_options]` — `unit_case_budget` = 4000 at `:278` and `integration_case_budget` = 1000 at `:279` when this was read — and `mcp/tests/conftest.py` carries no number of its own**: it registers the two ini names with `addini` and no `default=`, because `mcp/pyproject.toml` declares no `[tool.pytest.ini_options]` and the root file is the `inifile` pytest reads. Read the pair from there; it moves, and the dated tradeoff comment above it records every raise. The 150/200/250/400/600 integration ceilings and the 1000/1100/1250/1500/2300/3000 unit ceilings named below are the dated readings of the leaves that raised them, kept as as-of records — none is the current rail. Extend or consolidate distinct behavior protection before adding cases; do not restore deleted matrices, private-branch tests or unused fixture machinery because an old milestone names them.

Coverage, including changed-line coverage, is diagnostic only. No percentage floor requires additional tests. Production-only CRAP retains 20 as a review trigger, not a delivery blocker; tests and verification support are excluded. Lint, formatting, typing, structural rules and test failures still enforce. Diagnostic-tool execution errors remain visible failures distinct from metric findings. There is no coverage baseline, score-exception registry or ratchet.

Only genuine Dagger admission and the existing lifecycle owners can issue immutable candidate-bound certifying evidence. A host pytest pass, copied report, green helper result or use of Dagger alone is insufficient. Reuse the existing shared engine and preserve process identity, disposable state, credential isolation, exact candidate and publication ownership. Full-suite execution and whole-master independent review belong to the master aggregation boundary under the current execution policy; this overview does not impose either on every leaf. Focused development evidence remains useful without pretending to be final acceptance.
### Docs And Cross-Repo References

No Domain Documentation entries are configured in the resolved memory root. Current local policy and source owners are cited above; no live external system or sibling repository is used to grant authority.
## Fixture Roles And Claims

`test_agent_notifier.py` and `test_agent_notifier_ladder.py` supply row/topology builders. `test_codex_app_server_adapter.py` and `test_codex_adapter_thread_demux.py` supply transport/observation helpers. `test_closeout_queue.py`, `test_closeout_projection_member_helpers.py`, `test_final_codex_models.py`, `test_gate_certification_evidence.py`, `test_memory_citation_fix.py` and `test_observer_projection.py` likewise retain shared setup rather than their former standalone matrices.

**The citation fixtures now build real Git provenance (260831-LOCR-L33).** The continuity rule the
leaf introduced — a tree-wide relocation is admitted only when no cited file survives and the anchor
existed in a cited file at the document's `lastVerifiedCommitHash` with the same extent kind — is
only expressible against a real repository, so `test_memory_citation_fix.py`'s shared `Tree` gained
`history()`, `stamp()` and `remove_source()`, and its `document()`/`card()` accept a `stamp` that
lands a `lastVerifiedCommitHash` row **inside** the metadata table (never below the citation header,
where it would parse as another claim). `Tree.row()` locates a citation row by its table header
rather than a fixed index, so card metadata cannot shift it. `test_citation_document_transaction.py`'s
`Scenario` carries the same stamp and its fixture commits the verified tree before deleting both
cited files; the TypeScript move fixtures in `test_memory_citation_grammars.py` and the
`_two_failing_cards` helper in `test_memory_citation_fix_scopes.py` were given provenance the same
way. The previously pinned relocation tests therefore still test the legitimate kind-preserving move
instead of having their expectations relaxed, and `test_memory_citation_resolution.py` adds
`MechanicallyProjectedRangeTests`, which pins that a range written by the mechanical projection is
surfaced with the support question rather than an assertion that the citation is current.

Preserve useful shared fixtures only for real consumers. Fake inspectors, synthetic profile inputs, hand-built report payloads and pending finalizers must stay labeled as such. A source-range citation proves the described assertion exists; only a retained execution record proves it ran. Whole-master review and aggregation must assess actual protection rather than historical test names or counts.
## Hot Path Summary

The imported native Paseo role route retains canonical task/workspace identity, exact launch/replay and independent model/effort/tier validation alongside the existing converted MIK memory and publication owners.

For the ledger retirement, start with transaction-only delivery, direct landing, integration/checkpoint concurrency, memory ledger projection and backfill tests. Assertions distinguish cache-only conditions from actual content, ancestry, ref and ownership failures. The retained producer census checks every active attributed memory writer; no scenario expects a third ledger commit.

Start with the distinct failure or user operation, then locate its retained owner. Checkout isolation, Dagger registry locking, private Git preparation, protected-ref recovery, durable-store races, submission authority and native framing each retain concrete behavioral protection. Compiler/certificate fixtures establish library contracts; they are not live Dagger, Codex or final-memory execution evidence. Preparation checks can guide memory repair before certification without becoming Gate 5.

`test_knowledge_read_scope.py` (unit-regression — the selection policy, the corrected page counts, revision
grouping, budget, the execution bound and typed absence), `test_knowledge_read_boundaries.py` (integration —
the seven anchor observations against a real committed Git tree, the snapshot/namespace/schema refusals and the
continuation bindings) and `test_knowledge_read_paths.py` (integration — what a *path* is to this read: an
address, not a pattern), all three consuming the governed artifact `read_scope_test_support.py` under contract
`knowledge-read-scope-cases`.

## Isolation And Collection

Root test conftest sets candidate imports and disposable home/config/data/cache paths, removes inherited credentials and live-provider opt-ins, and restores owned global state. Ordinary units do not automatically bootstrap application composition; tests request `worktree_services` when that boundary matters. Integration-only modules are skipped before import during unit runs. Collection budgets inspect already selected items without nested pytest or a second repository scan.
## Memory Preparation And Final Certification

Memory quality is useful before gate admission: a contract-scoped full request observes the exact code/memory pair and candidate trees, runs quality checks, and builds an enclosure-local curator worklist covering repair findings, commit-owned findings, missing onboarding, stale route indexes and source drift. Use that worklist to perform the authorized semantic onboarding updates before entering the expensive certification sequence. It is not necessary to obtain code-gate certificates merely to discover the memory work.

Preparation does not grant a final certificate. The interactive catalog projection explicitly lacks affected-closure and code-prefix authority. The existing prepared-memory adapter consumes the selected four original code terminals and exact prepared candidate, runs the final memory producer, publishes its physical result and selects Gate 5 through the normal owner. Finalization requires that selected original fifth certificate and its bound memory inputs. MCAR continues from these existing owners; this overview does not declare the unfinished master accepted or create a second final proof path.

Candidate capture uses an isolated add-all index and stable observed HEAD, leaving the user's real index unchanged. External-memory identity binds configured repositories, worktree roots, branches, bases, onboarding root and contract digest; the cache path is informational. A changed pair or candidate must refuse stale publication. Metadata stamping and cache refresh cannot substitute for substantive memory repair.

The current manifest records 450 lines and 432 entries: 299 unit-regression, 2 public-contract, 95 integration, 22 architecture-fitness and 14 provider-conformance, with stress-durability and migration empty; the declared collected-case budgets are 4,000 unit and 1,000 integration (`pyproject.toml:278-279`). The `test-evidence-lanes.toml` card owns the per-lane brackets; membership is selection and cost classification only, never execution or acceptance evidence.

260831-LOCR-L30 registered eight more members and, in doing so, repaired a manifest that could not
load. `load_lane_manifest` is fail-closed — it derives the repository's actual test modules and
refuses a manifest that omits one — so the seven tracked modules that declared no lane (one of them,
`test_record_landing.py`, shipped by the immediately preceding leaf) were a hard load failure rather
than a silent default. The leaf's own `test_checkpoint_landing.py` joined them. Detail lives in the
`test-evidence-lanes.toml` card, which is the owner of record for lane membership.

The same leaf's follow-up added three more forcing cases, one per behaviour the checkpoint state had
to teach, and this route gained two new file cards with them:

- `test_post_integration_cleanup_guidance.py::test_a_checkpointed_series_keeps_working_instead_of_being_told_to_integrate`
  — a checkpointed contract projects `worktree-started` + `continue_work` + `worktree_status`, not
  `integration-pending` + `worktree_integrate` (the tool that refuses while the series is open).
- `test_record_landing.py::RecordLandingTests::test_a_checkpointed_series_is_not_upgraded_into_a_reclaimable_integration`
  — the pull-request route reports `already-recorded` for a checkpointed contract and leaves both cells
  as the checkpoint wrote them.
- `test_closeout_kept_rules_pins.py::test_r3_closeout_accepts_the_source_head_a_checkpoint_landed`
  — the ancestry validator accepts the commit a checkpoint recorded as its own landed head, with
  `test_r3_closeout_refuses_when_the_source_branch_moved` still refusing foreign movement.

The latter two modules had no file card before this pass and are now covered
(`test_post_integration_cleanup_guidance.py.md`, `test_closeout_kept_rules_pins.py.md`). All three
cases were proven non-vacuous by temporary production mutation, which is why each is documented as the
assertion set that failed without its fix. Lane membership is unchanged: all three files were already
registered, so no manifest row moved.
The current evidence-lifecycle registry declares both registered consumers in each shared
closeout-input and curator-coherence support row. Registry SHA
`15bea1c01f402c382dad1667dec601313bb8aabfc511bb8cedac66076287606a1` and validator PASS42 are
source/diagnostic evidence only; they do not establish execution or acceptance.
## Public-Surface Inventory Contract

`test_tools.py::PublicSurfaceInventoryTests` (260831-LOCR-L29) is the executor of a
surface-agreement invariant that had none. `server_info` reports `PUBLIC_TOOLS` itself, so the
comparison it made possible was self-referential; `worktree_record_landing` shipped registered by
`mcp/registration/closeout.py`, advertised by FastMCP, and absent from both `PUBLIC_TOOLS` and
`TOOL_RESPONSE_MODELS`, and every existing case stayed green while the tool could not return a
payload.

The two cases register `TOOL_REGISTRARS` against a probe `FastMCP("inventory-probe")` and compare
the live `asyncio.run(server.list_tools())` order to `PUBLIC_TOOLS`, then drive one
`finalize_tool_response("worktree_record_landing", ...)` call so a missing registry row fails here
rather than at a caller. `_permissive_registration_config()` only has to satisfy registrars that
close over the config without reading it during registration, so these cases stay about the
inventory rather than about building a runtime; the probe is hermetic and reaches no network.

`test_worktree_status_terminal_next_tool.py` (260831-LOCR-L32) is the same shape of executor one layer
down: the *advertised vocabulary of one surface* had no enforcement. `PUBLIC_TOOLS` moved from
`mcp/tools/base.py` to the zero-import `models` leaf `models/tools/public_roster.py`
cit:([`PUBLIC_TOOLS`], mcp/src/agents_remember/models/tools/public_roster.py:22-97) so that
`models/worktree.py::WorktreeCommandResponse` could read it, declare `nextAction` / `nextTool` /
`nextArgs`
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-405), and refuse a `nextTool` outside the roster
(`_require_registered_public_next_tool`
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442)). Before that the envelope was `extra="allow"` and
cit:([`_require_registered_public_next_tool`], mcp/src/agents_remember/models/worktree.py:431-442)). Before that the envelope was `extra="allow"` and
cit:(["# The next-move triple, declared here so the worktree surface's guidance is part of"], mcp/src/agents_remember/models/worktree.py:400-405), and refuse a `nextTool` outside the roster
declared none of the keys, so `application/worktree_status.py::_project_terminal_contract_status`'s
write crossed the wire verbatim and unchecked. The suite reaches the real `terminal-archive-ready`
state for both `worktree_cleanup` and `worktree_abandon`, binds the emitted args against the real
builder signature, and pins the validator in both directions — including that the registered but
non-public `session_retire` is refused on the worktree surface while the `task_doc` surface still
accepts it. That branch had **zero** coverage before this module.
## Registered first-leaf preview proof

[test_worktree_start_preview.py](test_worktree_start_preview.py.md) drives the existing registered public path on confined real Git/task worlds. It distinguishes repeated two-mode startup-state no-materialization, exact journal ref states and current durable apply, preserving concrete refusal/organizational controls. Read-only means unchanged startup-owned state, repository refs, worktree lists and index bytes, not an unobserved tool call: the proof admits and checks the call-day daily tool-log lines, named detail files and completed-call workspace-river events. Earlier record bytes remain a prefix, each row accounts for an actual call, existing details stay unchanged, and a kept record directory's mtime changes only with an admitted new direct child. An ambient lifecycle's event is proved separately with kind/mode preserved. The fixture keeps its transcript root inside coordination and its empty river lockfile outside the admission. [preview_read_only_test_support.py](preview_read_only_test_support.py.md) owns that comparison and no production log behavior. Negative cases pin stray, rewritten, unnamed, stale-day and metadata-only changes. Source-bound archived payloads are task evidence; canonical synthetic task/contract files are never extracted into live coordination. L40 proof rows and ownership budgets remain preserved.

- Registered preview preserves startup/Git state while checking call records. [1706]
- The shared comparator checks call-day paths, causal directory entries, log details and completed-call river records. [1707]
### Repo-Internal References

These current source and policy ranges establish the development/certification distinction and the
existing memory preparation surfaces. A citation is source evidence, not a recorded test execution.

- Development commands, budgets, diagnostic metrics and isolation.
- Certifying publication and accepting consumers.
- The lane rows that admit both L14 modules to the `unit-regression` lane.
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register.
- The lane rows that admit both L14 modules to the `unit-regression` lane.
- The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane.
- The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair.
- The L36 lane registration the fail-closed manifest requires.
- The lane registration the fail-closed manifest requires for that module.
- The L4 census module's lane row, which closed the gap the L4 route section recorded.
- The lane registration the fail-closed manifest requires for that module (row 165 after the KS-L2 and KS-L3 insertions).
- The architecture-fitness lane registration the fail-closed manifest requires for that proof.
- The rewritten contract-scoped activation forcing suite and its shared-source-pair fixture.

Current working-candidate evidence for this route:

- The shared fixture world the seam's cases are built on. [1697]
- The launch-binding fixture that makes the adapter suite's launches verifiable. [1698]
- Final memory adapter requires the selected four-code-terminal prefix. [1699]
- Finalization consumes original selected fifth-certificate inputs. [1700]

## Exact population through bounded family pages

The family-population tests read expected membership and claim identities from the public authorship owners and follow actual HTTP continuations at fixed small bounds. They assert exact whole-walk coverage for content-only and claim-only pages, while primary knowledge, evidence, comparison identity and complete source inventory remain unchanged. The companion context-walk cases count unique membership identities instead of repeated sparse projection rows.

## Retained Behavioral Routes

| Concern | Current starting point | Boundary |
| --- | --- | --- |
| Checkout/host lock composition | `test_checkout_coordination_isolation.py`, `test_dagger_registry_lock.py` | Real path/lock refusal with temporary state; host authority does not open coordinator writes. |
| Durable state and event-loop liveness | `test_durable_store_contract.py`, `test_cross_store_lock_order.py` | Thread/process ordering and actual store outcomes, bounded by watchdogs. |
| Candidate and protected-ref safety | `test_git_command.py`, `test_integration_branch_authority.py` | Real Git identity, private commits, hooks and race preservation. The former `test_integration_ref_transaction.py` was deleted with the removed mid-crash ref-recovery capability..; mcp/tests/test-evidence-lanes.toml:224-341; mcp/tests/test-evidence-lanes.toml:181-217; mcp/tests/test-evidence-lanes.toml:229-348; mcp/tests/test-evidence-lanes.toml:247-247 |
| Terminal liveness cadence and readiness | `test_terminal_liveness.py` | Controlled-clock sweeper checks preserve the configured full-sweep interval and the one-second starting-row path with its four-row cap; lifecycle production wiring remains a separate candidate proof. |
| Serving-owned steady-state observation and pass-failure isolation | `test_serving_observation_loop.py` | The real `_serving_lifespan` finalizer under a virtual event-loop clock with no HTTP route registered: the completion-relative `DEFAULT_STARTING_SWEEP_INTERVAL_SECONDS` sleep after each attempt (including a failed one), attempt non-overlap when a pass outruns its tick, the sweeper's retained ten-second full-sweep limit, observation continuing while `agent_notifier.enabled` is false, the off-loop refresh through the drained helper, exactly one observer task cancelled at teardown, and a failed pass that neither marks success nor changes cadence. Its `ServingObservationFailureIsolationTests` half then pins the failure boundary itself on the real task collection: one unexpected pass failure leaves the owner scheduled and the five sibling loops plus an in-process ASGI request alive, publishes nothing durable (with a control proving a *successful* pass does change the tree), and retries on the cadence alone from the current persisted catalog while rows, the emitted-signal marker and the workspace cursor survive; cancellation still ends the task because the boundary is `except Exception` and `CancelledError` is a `BaseException`. This module also owns the **shared serving fixture**: `_ServingFixture` is imported by `test_serving_startup_prime.py`, and its `startup` witness plus its `_Gate` parkable probe `inner` are a shared contract — **call 1 of a lifespan timeline is the pre-serve prime and call 2 is the recurring owner's own first pass**, so a case that parks or fails invocation 1 addresses the prime rather than the owner. Unit lane; the sweeper's own cadence files stay the owners of their clocks. The notifier's pre-existing inline refresh, any structured observer-failure *publication* surface, and the prime's own ordering contract are out of this proof. |
| Startup observation prime before projection and recurring loops | `test_serving_startup_prime.py` | The `LOCR-R18@v1` half of the same serving seam, driving the real `_serving_lifespan` through the shared fixture imported from `test_serving_observation_loop.py`: exactly one observation prime at the head of the timeline, dispatched off-loop through the drained helper and parked while event-loop timers keep firing, positioned before `runtime.projector.prime()`, before every recurring task and before the lifespan yield; the seeded `ready` row committed as the adapter's `unsupported` verdict and read back by both the captured initial projection and the captured first notifier sweep; a prime taken with a real `GET /api/terminal/sessions` route registered and never dispatched and with the notifier loop started but never sweeping; and the committed entry equal to one reference canonical pass over an identical seed, so no startup-only reader, cursor or write path took part. A raised prime is contained — startup, the projection prime and the recurring owner all survive and the owner retries on its first cadence. Unit lane, hermetic, ordinary test source; it asserts no health or readiness payload, and its ordering witness does not constrain prime-versus-migration/compaction (that edge rests on the production straight-line order). |

| Deferred terminal work | `test_terminal_liveness_deferred_work.py` | Real catalog/sweeper proof that hosted-interaction syncs and turn callbacks run after commit, aborted batches dispatch nothing, and post-commit failures preserve durable truth. Caller ownership remains adjacent lifecycle work. |
| Terminal catalog liveness | `test_terminal_liveness.py` | Fake-clock host/control-read hysteresis, restart continuity, and successful reset against existing production transitions. This row is the LOCR-R21 hysteresis proof only: cadence (`R12`) and sweep non-overlap (`R22`) cases for the same module are still in their own unlanded worktrees, so the composed module's case count and extents will be larger than this leaf's four cases. |

| Terminal catalog batch and sweep non-overlap | `test_terminal_catalog.py`, `test_terminal_liveness.py` | Counted `_write_disk` replacements (zero clean, one dirty, one dirty-partial) and real-thread sweep contention returning the committed snapshot without a second probe; cadence (`R12`) and hysteresis (`R21`) values stay with their leaves. |
| Candidate and protected-ref safety | `test_git_command.py`, `test_integration_branch_authority.py`, `worktrees/integration/integration_ref_transaction.py` | Real Git identity, private commits, hooks, race preservation and exact recovery..; mcp/tests/test-evidence-lanes.toml:223-340; mcp/tests/test-evidence-lanes.toml:207-207; mcp/tests/test-evidence-lanes.toml:244-244; mcp/tests/test-evidence-lanes.toml:246-246; mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py:103-103; mcp/tests/test-evidence-lanes.toml:210-210 |
| Registry/certificate semantics | `test_certification_rail_registry.py`, `test_gate_certificate_authority.py` | Typed plan/result contracts and dependency-aware reuse, not a live producer claim. |
| Memory preparation and repair | `test_memory_quality_runs.py`, `test_citation_document_transaction.py`, `test_memory_citation_fix_scopes.py` | Exact-pair revalidation, document isolation, conflict refusal and preserved evidence. |
| State-signal structural routing | `test_state_signal_relay.py` | Action-time current-manager replacement, per-subject topology refusal, no-row/no-marker behavior while an owner is absent, and no owner wake while a seat's own turn is still open. |
| State-signal boundary delivery | `test_state_signal_boundary_delivery.py` | Row persisted before the emitted marker, zero adapter submission while the target is `working`, and delivery of that same durable row at the target's next admissible boundary across occupant replacement, fresh notifier context, and failed submission. |
| State-signal crash and restart recovery | `test_state_signal_restart_recovery.py` | The durable order row persisted → marker stamped → delivery attempted across a failed marker write, a stop after the marker, and a same-seat structural rebind: one pending row per exact seat/evidence identity, zero adapter submissions while that source marker is unstamped, and an action-time fence on the shared delivery action that state-signal recovery alone may lift. Seven cases, each rebuilt from the durable files through new store objects. |
| Curator turn owner wake | `test_state_signal_curator_wake.py` | The curator seat's own canonical terminal turn reaches the same shared role predicate and current-manager routing as the worker seat, with the durable payload carrying the curator role, the subject leaf document, the mechanical outcome and the terminal evidence identity — all derived by the real liveness sweep and the real agent-notifier sweep, never written by a curator post. A `completed` ending and an `interrupted` ending each mint exactly one durable signal and never a second on re-observation; `failed` reaches terminal truth and emits nothing while leaving the seat eligible; a curator seat whose own master has no current manager fails closed instead of routing to another master's manager; and the wake neither validates nor declares curator coherence or memory readiness. Unit-regression, one new module, no production byte changed. |
| Parked external-await separation | `test_parked_external_await_separation.py` | The parked open-turn external-await design stays out of the ended-turn relay: no `waiting` expectation kind is parseable, no wait-registration tool is advertised, and no wait/recheck/check-descriptor machinery ships. Absence guard only, not relay behavior evidence. |
| Reviewer turn owner wake | `test_lifecycle_owned_completion_relay_reviewer.py` | The reviewer role's own production-wiring relay: a short-lived reviewer seat's canonical terminal truth, produced by a real observation pass rather than a seeded row, wakes the reviewer's **current** manager as one durable inbox row — with no completion post from the reviewer and no dependence on the terminal-session read route. Six cases pin the boundaries separately. The row is truthless before the pass (`turn_state`, `terminal_outcome` and `terminal_evidence_id` all absent) and carries `completed` plus its evidence identity after it; the durable row holds while the owner is mid-turn with zero submissions and lands exactly once at the owner's next boundary. Liveness, a ready `control_state` and even a pane whose own diagnostic reads `turn-ended` authorize nothing, with a control proving the identical row does wake once canonical evidence exists — so the silence is about missing evidence, not an inert fixture. An `interrupted` turn is reported as `interrupted` with `interrupted_by=unknown`, no verdict vocabulary and a byte-unchanged leaf document. The wake is addressed by current occupancy, so a recorded `spawned_by_session` naming an exited manager generation receives nothing while the live manager gets the one row. Re-observing the same evidence identity mints no second signal even after the first row has landed and can no longer absorb a repeat by coalescing. And `failed` — production-reachable with a real evidence identity, since the pi projector settles `stopReason="error"` into it — is refused while leaving the seat eligible, so a later canonical turn still wakes the manager. Unit lane: a temporary coordination root, a scripted single-seat adapter endpoint and a tmux double at the process boundary; the lift, the outcome and the evidence identity are production's, and the relay's own structural rules stay `test_state_signal_relay.py`'s contract. |
| Worker turn owner wake | `test_state_signal_worker_wake.py` | A worker is not required to author a second completion message, so the wake must arrive on its own: an owned `worker` row whose **catalog terminal evidence** says `completed` or `interrupted` becomes a state-signal finding and the notifier persists and routes exactly one durable row to the leaf's **current** manager through the existing inbox path. Seven cases pin the boundaries separately. No inbox row is created for the worker at all, and the whole store is asserted rather than its state-signal subset, so a worker-authored row would be visible rather than filtered out. The eligible-outcome set is pinned from both sides: `completed` and `interrupted` wake the manager, and `failed` or `unknown` must not however real the evidence identity is — with a final leg re-reporting the same seat and evidence identity as `completed` and requiring the wake, which makes the empty store a measured refusal rather than an inert relay. Per-turn dedupe is pinned in both directions too: the same evidence identity projected twice mints one row, and a **second distinct terminal turn** on the same seat mints its own wake instead of being swallowed by the first turn's marker. An `interrupted` turn travels with its origin and is not mislabelled as completed; a report on disk is not terminal evidence, so the adapter evidence identity is the discriminator; the leaf and master documents are captured around the sweep and compared byte for byte, because reporting a seat turn never closes task work; and a worker below a managerless master wakes nobody, stamps no marker and guesses no global owner while staying eligible for the next sweep. An empty live terminal-session read is a measured zero on a host the delivery path demonstrably reached, because `_RecordingHost` counts every contact the sweep makes. Unit lane: a temporary coordination root with real task documents, a real catalog file, a real inbox log and the real durable stores; no HTTP request, no server, no process. The relay's own structural rules stay `test_state_signal_relay.py`'s contract, and the pre-existing dead-upstream supervision row the same sweep separately raises is outside this module's assertions. |
| Incremental memory scope | `test_memory_incremental_scope_compiler.py` | Dependency-complete work and exact reuse remain non-accepting with final-full pending. |
| Native submission and IPC | `test_harness_submission_authority.py`, `test_harness_control_ipc.py` | One request authority, idempotence, withdrawal races and ambiguous receipt reconciliation. |
| Conversation projection and assets | `test_conversation_active_service.py`, `test_conversation_control_attachments.py` | Ordering, honest pagination, one-use assets and unknown-outcome retention. |
| Canonical terminal-evidence mapping | `test_terminal_evidence_mapping.py`, `test_conversation_native_ingestion.py` | Native projectors remain the terminal-outcome authority; malformed or open frames make no terminal claim and do not hide a later canonical outcome. |
| Protocol framing | `test_codex_native_history.py`, `test_pi_rpc_process.py` | Bounded paging/correlation and real fixture subprocess behavior. |
| L38 actionable admission and closeout transport | `test_activation_admission_registered.py`, `test_worktree_closeout_route_review_transport.py` | Registered response-shape and refusal-projection checks, including bounded malformed-contract parser detail, for the frozen candidate. The activation admission is contract-scoped: a refusal carries no `classification`/`blocking`/`sourcePair*` key and never names a foreign master as blocker or retry precondition. Preparation evidence only. |
| CCR-R12 transaction-only delivery | `test_transaction_only_worktree_delivery.py` | Public code/memory delivery, interruption recovery, source/ref safety, hooks, memory attribution and cache-only no-op behavior. |
| Ledger attribution and the projected source ledger | `test_memory_ledger.py`, `test_worktree_sync.py` | Git-only computed rows, cache misses/malformed bytes and hand edits, attributed source history, and cache-independent synchronization. |
| Producer census and the one renderer | `test_memory_attribution_producers.py` | Five memory-content producers and zero untrailered, measured from source: the trailer key identifier and its interpolation appear in exactly one production module, no production module spells the trailer as a quoted literal, each of the five producers reaches a shared renderer entry, and a hostile multi-paragraph caller body survives byte for byte with the trailer appended as its own final block. The two non-closeout producers are driven end to end through the public `memory_carryover_apply` and `memory_baseline_adopt`. Source census plus real-repository cases. **Superseding the note this row used to carry: the module's `unit-regression` lane row now exists** (`.; mcp/tests/test-evidence-lanes.toml:1-223; mcp/tests/test-evidence-lanes.toml:122-122 |
| Leaf document master-link binding | `test_leaf_doc_master_link_binding.py` | The derived master link, end to end on real repositories: a leaf authored through `task_doc` with no series contract acquires `seriesContractPath` and its one `enclosures[]` ref when it is started; an already-damaged document (`lifecycleId` stale, no link) is repaired by its next start with objective, requirements, steps and title unchanged; a leaf under a task root with no master document is refused with `seriesContractPath`, the exact missing `task.json` and the remedy, writing nothing; and the planning flow (master plus two leaves, no start) still succeeds, still unstamped. Integration lane: one disposable code repository and one external memory repository per case. The restamp decision table is the unit half in `test_task_document_application_1.py`. |
| Closeout recovery attribution | `test_transaction_only_worktree_delivery.py` | Interrupted closeout proves actual journaled code/memory commits and refuses forged output evidence; cache state is immaterial. |
| Closeout auto-carry and parked candidate | `test_source_lineage.py` (`CloseoutSourceLineageHealTests`), `test_sync_parked_candidate.py` | The closeout boundary carries a settleable stale break, refuses a preview without mutating, escalates an unprovable break, and returns a parked dirty candidate through the sync transaction (restore on completed/resume/cancel, kept unmerged-index refusal); transaction-level detail lives in the new unit-lane module. |
| Memory-history trailer backfill | `test_memory_backfill.py` | Disposable history rewrite selection, loss reporting, byte-faithful objects, trailer-only acceptance, idempotence and multi-ref CLI publication. |

| Terminal evidence cursors | `test_terminal_evidence_cursors.py` | Focused deque envelope validation, no-advance refusal, bounded Pi continuation, and liveness containment; unit evidence only. |
| Public tool-surface inventory | `test_tools.py` (`PublicSurfaceInventoryTests`) | Live registration order against a probe `FastMCP` equals `PUBLIC_TOOLS`, and the advertised names have response models that validate. Two further cases pin the advertised **text** rather than the roster: the checkpoint landing's description must present a partial publication and deny being the pause (L36), and `worktree_pause`'s must present a stop that publishes NOTHING, name the checkpoint as the separate publication, carry no refusal the verb no longer performs, and still name the release it does perform (L37, extended by L38). Hermetic inventory contract: the probe starts no server and touches no provider. |
| Worktree next-move typing and enforcement | `test_worktree_status_terminal_next_tool.py` | The `terminal-archive-ready` branch of `worktree_status` names the accepted cleanup operation, its emitted args bind to the real tool signature (checked with `inspect.signature(...).bind`), the envelope declares `nextAction`/`nextTool`/`nextArgs`, and the `PUBLIC_TOOLS` membership validator is driven in both directions. Integration lane: real worktree services and a real repository under `tmp_path`. First coverage of that branch. |
| Stop-only pause, and the pause/publication split | `test_pause_stop_only_end_to_end.py`, `test_pause_is_not_publication.py` | The public `worktree_pause` stops an atomic master over one real temporary Git world holding two masters: it releases only this contract's activation record to `vacant`, leaves the other master's record byte-identical and still `active`, moves no ref and creates no commit (both repositories' tips, complete object databases, coordination tree, both worktrees, the enclosure and every task document measured identical before and after), reports `paused: true` with **no** `nextTool`/`nextArgs`/`nextOperation` at the top level or inside `nextStep`, reports a never-selected master as the explicit `atomic-series-already-vacant` success (that case asserted a refusal before the 260831-LOCR-L38 change set) — naming in its summary that no selection was held, and carrying an observation with no `record` where a released pause carries the one its own release wrote — and keeps the four refusal shapes apart without writing anything: a leaf contract (`pause-requires-atomic-master`), a record this contract does not own and an unreadable record (both `atomic-series-activation-release-unreadable`), and a **vacant** record naming another master (`atomic-series-activation-selected-contract-mismatch`), which is the only foreign shape that reads `vacant` and therefore the only one that could be mistaken for the success — an *active* foreign record is refused one step earlier by the observation, so the two cases prove different guards. It is idempotent, and resumes through `worktree_sync` with nothing published. Its sibling is the structural half: `test_pause_is_not_publication.py` (architecture-fitness) asserts the pause module's static import closure is disjoint from all twelve publication modules — measured 60 modules including the root, 5 direct imports, 54 beyond them — with non-vacuity assertions and named witnesses so a walker stopping at the direct imports fails rather than passes, so the stop cannot become the checkpoint publication. `worktree_checkpoint_landing` is the separate, explicitly requested publication and no case here reaches it. Integration + architecture-fitness lanes. |
| Checkpoint landing plan/apply parity | `test_checkpoint_landing_end_to_end.py` | Public unfinished-master checkpoints, actual paired refs, idempotent retry, cache independence, and real source/content/ref-race refusal parity. |
| Sub-task index reachability across a writer skew | `test_task_documents_graph_projection.py` (`SubTaskIndexReachabilityTests`) | Projection-only unit evidence that a completed leaf whose durable JSON carries a field this reader's schema does not know stays reachable from the master's sub-task index, an unstarted row keeps resolving, and a document with a required field deleted is still withheld. `_index_doc` reproduces the dashboard's own index rule (`sliceForRef`) rather than approximating it. Hermetic temporary task root; one case, one helper, no lane change. |
| Cross-master concurrency on one protected source pair | `test_cross_master_concurrency.py`, `test_atomic_series_activation.py` | One sprint commands every atomic master from its own source branches, so two atomic masters share one protected source pair; each keeps its own activation record. Both masters stay ready and progress, each master's work stays private until it lands, releasing a master's activation publishes nothing and blocks no sibling (the same statement the stop-only pause now makes as a real public operation, `worktree_pause`, proved separately in `test_pause_stop_only_end_to_end.py`), a conflicting or stale publication is refused at the pair (`blocked-non-ff`, `atomic-series-checkpoint-candidate-moved`), and a master that reconciles with a landed sibling finishes through ordinary public closeout and final integration rather than a checkpoint. A graph-less sprint serializes nothing — `executionGraph=None` resolves to the `atomic-sequential` sprint shape (every commanded master executes atomically, no dependency is declared) and both masters hold their own activation concurrently with no waiting reason. Only a real sprint-graph wave edge still gates (`predecessor-incomplete:`). Integration lane: real temporary Git repositories and the public operations. |
| Capacity refusal source classification | `test_closeout_projection_source_classification.py` | The three states of a projected source stay distinct on the code its own raiser published. `graph_context` refuses a sprint whose authored graph is one node past `MAX_CLOSEOUT_MASTERS` with `closeout-queue-master-capacity-exceeded` — its own declared code, read back from the refusal rather than retyped — and that code classifies `invalid`, because the source was read and is past its bound; `contract-unreadable` and `atomic-series-contract-unreadable` still report `unreadable`; and the ordinary projected source stays readable with no problems and classifies `active`. The classifier tests membership of `closeout_queue_errors.py`'s `CAPACITY_REFUSAL_CODES` instead of the substring `cap-exceeded`, which neither surviving capacity code contains. Integration lane: real temporary Git repositories through `QueueFixture` and the production graph admission path. |
| Registration before compaction | `test_terminal_liveness_registration_order.py` | The full sweep's post-commit order, pinned where it happens: the traced terminated-row read records the batch-commit state observed **at the read**, so the chain `batch-enter → batch-exit → enumerate[include_terminated=True, batch=closed] → register → compact` fails if the enumeration moves inside or ahead of the observation batch. The registrar's returned proved-id set is the only argument `compact` receives, an absent registrar yields the empty proved set (so a task-bound leaf row survives), a raising registrar stops the pass before `compact`, a crash after registration re-registers idempotently on the next pass, and the starting-row fast path does neither stage. Hermetic unit lane; no production byte changes for this contract. |
| Terminal observer health | `test_terminal_observer_health.py` | The observer stage's own health reading (`LOCR-R17@v1`), sixteen cases in three classes: the exact atomic v1 record and its writer (constant-size row, no partial document, the failed-write source of truth being the persisted row rather than the newer in-memory accumulator), the status ladder `initializing`/`degraded`/`healthy`/`stale` at exactly `6 ×` the configured sweep interval, omission-and-no-repair for every unusable source (missing, unreadable, wrong marker, extra or missing key, wrong type, naive stamp, prior-lifetime stamp, above-ceiling counter), the bounded ordered secret-safe failure vocabulary, publication on the observer CALL for success and failure alike through the real lifespan, the fixed write-failure log line with retry, and the served tail driven through the real `_state_response` handler and `stream_events` generator (additive key, untouched ETag/304 path, health on the snapshot and none on a delta, plus the packet's cross-read rows including "healthy beside a fresh notifier"). Unit lane: no HTTP transport, no server, no real second. |
| Terminal blocker reasons | `test_terminal_blocker_reasons.py` | A cleanup or finalize blockage always names the component it stopped on and a non-empty reason. The L6 shape — terminal archive proven, provider runtime already gone — finalizes on the first call with an empty `notRemoved` inventory; a real permission failure on the provider tree blocks with `remove_tree`'s own `permission denied: ...` reason, closes nothing and refuses identically on retry; and both invariant owners are driven directly (`_blocker` refuses a missing, blank or non-string reason, and `remove_tree` names a reason whenever it reclaimed nothing). The L6 payload is reproduced through the provider port boundary, not by re-enacting the original physical event. Integration lane; one new module, no deleted module. |
| Pane diagnostics are non-authoritative for turn truth | `test_terminal_liveness_pane_authority.py` | The pane's own reading is persisted only as `control_raw["paneDiagnostic"]`; adapter snapshots plus the canonical terminal projection own `turn_state`, terminal outcome/identity, interruption origin and state-signal eligibility. Ten cases pin the boundary: contradictory pane/adapter readings in both directions, **readiness** (an adapter `control="disconnected"`/`"failed"` snapshot with a `working` pane keeps the adapter's `control_state`, activity/acceptance `unknown`, turn `stale`), below-threshold retention with the `controlReadFailures` counter, the R21 third failure owning `disconnected`/`stale`, alive-starting retention, the legacy no-`control_endpoint` `unsupported`/`stale` projection proved never to consult the control surface, a failed terminal page advancing nothing, startup-prime and steady-pass sharing one boundary (`host.calls == 3` discriminates the fast path), a four-reading pane-independence matrix, and a negative AST source guard over `terminal_liveness.py` itself. This module is a **deliberate split** from the 574-line `test_terminal_liveness.py`, which it leaves byte-unchanged and from which it imports its fixtures; an in-place extension had reached the coding-guidelines 900-1200 band, so the two cards must not be merged. The source guard is defence-in-depth over behaviour, not the sole pin: it is measured blind to a pane-derived constant inside an enclosing `if`, to positional writer arguments and to `CatalogTurnEvidence(state=…)`, all three of which stay caught behaviourally. Integration lane; one new module, no production byte changed. |

| Observer-to-notifier handoff latency | `test_serving_notifier_handoff.py` | `LOCR-R04@v1`'s completion-relative relay proof, eight cases over one disposable world that enters the real `_serving_lifespan` under a deadline-correct virtual clock, so the real observation loop, the real `TerminalCatalogLivenessSweeper.refresh`, the real catalog commit boundary and the real `run_agent_notifier_sweep` are what is measured. The two loops share no wake-up channel: the observer polls every `P` (1.0 s) after each attempt returns and the sweeper admits one full sweep per `F` (10.0 s) from the previous full sweep's **start**, while the notifier evaluates the durable catalog and sleeps `N` (10.0 s) after its pass returns — so the delivered worst phase is `F + P + R_observer + D_commit + N + R_notifier`, 21.0 s of logical scheduling for the default knobs plus only measured overrun. Each case asserts the bound **and** its decomposition from measured terms, and each protects one clause: the nominal phase, the previous full sweep's own overrun, a starting-row fast-path overrun, a notifier pass in flight at the commit (whose interval starts at its own completion, not at the commit), committed-truth-only reads (a read attempted before the commit and returned after it carries the committed rows in the notifier's own `include_terminated=True` scope), coalesced missed ticks for both loops, a live pass that did not observe the fact being unable to satisfy the stage, and notifier disablement with in-place re-enabling. The oracle documents three relations it deliberately does **not** assert — the telescoping decomposition, the observer phase's maximum, and `bound` as the sum — because each holds in every reachable state; an assertion that cannot fail is not evidence. Unit lane: no HTTP request, no server, no process. |

- The lane row. [1414]
- The packet's examples: ready once current rows answer every item; a new edit reopens two. [1415]
- One refusal test per public route entry, starting with the worktree closeout. [1416]
- The sync-merge cases. [1417]
- The two lane rows. [1418]
- The folder-master finalize cases. [1419]
- The four reopen cases. [1420]
- Buckets and destinations reconcile; long paths answer typed. [1421]
- The lane row. [1422]
- The registry compared as a set. [1423]
- The lane row. [1424]
- The module's own statement of its fixture. [1425]
- The walk-tree case (F16, R3-1, R3-2). [1426]
- The route case: every view, 503 unwired, nothing written. [1427]
- The lane row. [1428]
- The cards-read case and its four helpers. [1429]
- The proof admission at the route. [1430]
- The Q8 case. [1431]
- The MIK-R05 lane row. [1432]
- The budget and resumption case. [1433]
- The lacking-revision case on resume and fresh read. [1434]
- The entry-less page in the adapted leaf-read module. [1435]
- The MIK-R10 lane row. [1436]
- Delete-only: only no_invariant. [1437]
- The knowledge items, without the unexplained kinds. [1438]
- The two MIK-R25 lane rows. [1439]
- A repeat read writes nothing. [1440]
- Archival deletes only the task's own artifacts. [1441]
- The decision-record lane row. [1442]
- A lifted decision round-trips with its requirement endpoints reported. [1443]
- A decision is never an export (review F6). [1444]
- The leaf-read lane row. [1445]
- The leaf-read module's two consumer lines. [1446]
- The lane registration. [1447]
- The conforming directory move. [1448]
- A forged legacy ID does not make a record exported. [1449]
- The writer refuses an unsupported admission claim. [1450]
- The planned-effects lane row. [1451]
- The planned-effects module's consumer line. [1452]
- The paging lane row. [1453]
- The paging module's two consumer lines. [1454]
- The onboarding gate's lane row. [1455]
- The gate cases' fixture description. [1456]
- The lane row. [1457]
- The consumer addition. [1458]
- The two lane rows. [1459]
- The lane row. [1460]
- The three consumer additions. [1461]
- The migration-pass case. [1462]
- The three lane rows. [1463]
- The two lane rows. [1464]
- The conforming example's measures carry their counts. [1465]
- A recorded assessment is never edited; a correction appends. [1466]
- The two lane rows. [1467]
- The Doc14 family example validates. [1468]
- The lane row. [1469]
- A file failing its schema marks the index partial and is named. [1470]
- Parity of the reused selection over the index and the database. [1471]
- Every tool surface reports a partial index as incomplete. [1472]
- The three lane rows. [1473]
- The baseline and the pinned report-only set. [1474]
- The managed sync refuses, keeps the merge staged, and syncs after the repair. [1475]
- The two lane rows. [1476]
- The freeze cases. [1477]
- The parallel-merge case. [1478]
- The lane row. [1479]
- The nine fixtures and the model each must parse as. [1480]
- The two lane rows. [1481]
- The module's own statement of what it pins. [1482]
- Its lane registration. [1483]
- **The new route-level case: the served `200`, the state after serialization, and the unknown leaf that is still a named `404`.** [1484]
- The one-half degradation, unchanged, whose docstring now records that the code side reads `recorded` beside it. [1485]
- The producer both cases drive. [1486]
- The module's own statement of the admitted population and its cases. [1487]
- Its lane registration beside the sibling module. [1488]
- The module's own statement of the read bound and the preserved projection. [1489]
- The count-based scaling case. [1490]
- Its lane registration. [1491]
- The module's own statement of what it protects. [1492]
- The count-based scaling case. [1493]
- Its lane registration. [1494]
- The module's own statement of what it protects. [1495]
- Availability loss reported, not remembered. [1496]
- Its lane registration. [1497]
- The three new lane rows beside their siblings. [1498]
- **The movement module's own statement of what it measures, and the fixture it authors through the store's operations.** [1499]
- **The packet's conforming example and the non-conforming reading measured beside it.** [1500]
- The withdrawal boundary and the labelled inference with its no-fabrication control. [1501]
- The family, route and ungoverned cases, and the unresolved anchor that keeps its reason. [1502]
- **The reach module's own statement of the five states the ruling turns on, and the member-head case.** [1503]
- The multi-ended line, the named-instead-of-denied withdrawal, and the member-wise family pairing. [1504]
- **The three lane rows and the six consumer rows the same change registered.** [1505]
- **The re-contracted mechanism case in the surface module.** [1506]
- The unit-regression registry includes the revision-selection test module. [1507]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [1508]
- **The fixture that makes a chain, a fork and a history real: two independently built snapshots under one namespace through the public write path.** [1509]
- **The two chain defaults with exact selected revision ids.** [1510]
- **The two fork ambiguities and the two lineage failures, each with no pair recorded.** [1511]
- **The pane case that closes the loop through the served payload.** [1512]
- **The two rewritten surface cases: the old both-sides assertions replaced by ambiguity assertions.** [1513]
- **The module's own statement of what it measures — endpoint-correct, generation-bound, through the operations the dashboard really calls.** [1514]
- **The shared master-shaped world and its builder.** [1515]
- **The lane row, and the manifest extent it sits in.** [1516]
- **The module's own statement of what it is — the fast transport contract, driving the real route — and of the two shapes a refusal arrives in.** [1517]
- **The module's own definition of actionable, asserted as a set inclusion in every transport-level case.** [1518]
- **The bare app with the real routes registered, which is what makes the ports the only injected part.** [1519]
- **The conforming example at the transport, with no `payload` key so a refusal cannot read as a success.** [1520]
- **The status family derived from the refusal's own code.** [1521]
- **The lane row, and the manifest extent it sits in.** [1522]
- **The module's own statement of the requirement and of the property behind each case.** [1523]
- **The first case: both bound objects' own bytes, each against an independent `git show` observation.** [1524]
- **The content classes the fixture materializes for real, and the routes wired as the composition root wires them.** [1525]
- **The generation binding, the two availability cases, and the verifier's path-confinement finding.** [1526]
- **The refusal family and the closing identity case.** [1527]
- **The shared R01 fixture these cases extend rather than duplicate.** [1528]
- **The lane row the insertion created, and the two rows it displaced.** [1529]
- **The two consumer rows this module joined, and the counts they do not move.** [1530]
- The expansion owner and route constant these cases are the regression surface for. [1531]
- **The module whose cases are the production-composition evidence, and its lane row.** [1532]
- **The production port the cases read through, and the bundle they read beside it.** [1533]
- The fixture's external-memory shape, which the assessment channel needs. [1534]
- **The nine partition cases, appended after the module's former end.** [1535]
- **The six precedence and receipt cases on the real enclosure route.** [1536]
- One collected subject covering all three arrivals at the series publication. [1537]
- The interrupted reset resumes rather than stranding the branches the series stands on. [1538]
- The one collected case that now pins all three directions of the step rule. [1539]
- The counter-case the new admission must not weaken: a position descending from a step cannot vacate it. [1540]
- **The lane row, inserted mid-list, and the row it displaced.** [1541]
- The module's own lane declaration, which is what makes the classification its own rather than a budget convenience. [1542]
- **The fixture that makes an addition and a removal real: two independently built snapshots under one namespace, plus the four authored revisions.** [1543]
- **The addition and the removal: the complete present-side statement beside the named absent side, with the comparison's own side-absence code.** [1544]
- The field-row cases: the roster asserted by exact key set, and the structured value served as its own projection on both sides. [1545]
- The one-sided-record case and the task-context case. [1546]
- **The catalog consumer row the same registration produced, on the shared read-scope fixture.** [1547]
- **The catalog consumer row the same registration produced, on the shared read-scope fixture.** [1548]
- **The renderer half that uses these same values, which is what makes a change to either half fail in one of the two.** [1549]
- The acceptance pair, read out of each started session's own first prompt. [1550]
- The production-chain pair that replaced the hand-supplied case. [1551]
- The refusal before any host effect, the mode gate, the byte-identical legacy payload, the single-carrier bound and the site enumeration. [1552]
- The declared legacy exclusion, the free agent's admission, and the two defect pins. [1553]
- The production-chain evidence the module's in-process cases complement. [1554]
- The fixture world and the synthetic corpus every hermetic case is built from. [1555]
- The admission guarantees: no role acquisition by string, no caller-selected source, no write to the read tree. [1556]
- The guards the repairs pinned, each driven directly by its own case. [1557]
- The SEP entry contract, asserted separately from this server's own index shape. [1558]
- The two independent-SDK-client exchanges, including both extension methods and the `-32602` refusal. [1559]
- The case that keeps the seeded-mutation evidence honest. [1560]
- The lane row that selects this module into the unit population. [1561]
- The Python half, whose refusal cases assert a named defect. [1562]
- The TypeScript half, executing the shipped modules under a real Node. [1563]
- The trace's effective-prompt key, which the live capsule scenarios assert against. [1564]
- The live end-to-end capsule scenarios, which are the whole-seam proof rather than a unit claim. [1565]
- Exact contract scope, full check and curator worklist publication. [1566]
- Interactive catalog names missing authority without eligibility. [1567]
- The citation index's exclusion register, its ruled caps and its reported-skip behaviour, defended case by case. [1568]
- The divergence between the register's re-inclusion rule and Git's, measured on both sides. [1569]
- The consumer of record for the three new `scripts/e2e_harness` governed artifacts, and the fixture/scenario shape it pins. [1570]
- The lane rows that admit both L14 modules to the `unit-regression` lane. [1571]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1572]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1573]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1574]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1575]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1576]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1577]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1578]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1579]
- The lane rows that admit both L14 modules to the `unit-regression` lane. [1580]
- The live public-surface inventory contract for the advertised MCP tool tuple. [1581]
- The advertised roster the inventory comparison uses, in its new zero-import `models` leaf. [1582]
- The L32 module itself: archive-ready reachability for both cleanup verbs, the declarations, and the validator in both directions. [1583]
- The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. [1584]
- The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. [1585]
- The L36 lane registration the fail-closed manifest requires. [1586]
- The L37 structural half: the pause's import closure is disjoint from every publication module. [1587]
- The ordered lifecycle playthrough that is the regression proof for the deleted atomic-series child-admission seal: master open → leaf start → closeout → landing → checkpoint → pause → attach → a leaf commanded after the landing still starts. [1588]
- The lane registration the fail-closed manifest requires for that module. [1589]
- The L4 census module's lane row, which closed the gap the L4 route section recorded. [1590]
- The L23 registration-order proof: the observed chain with the terminated-row read carrying its own batch-commit state, the partial-proof singleton, the raising registrar that stops the pass, the restart that re-registers and loses nothing, and the fast-path exclusion measured in both directions. [1591]
- The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. [1592]
- The shared fixtures the L27 module imports instead of rebuilding. [1593]
- **260913-LCA-L8:** the L6 shape finalizes on the first call, a real permission failure blocks with its own reason and refuses identically on retry, and the two invariant owners are driven directly. [1594]
- **260913-LCA-L8:** the only construction path for a terminal blockage, and the operator-language answer for a reasonless or malformed result item. [1595]
- The L37 stop boundary proof: the public pause, the measured world, the eight independently-failing cases and the refusals. Its never-selected case now asserts the already-vacant success rather than a refusal. [1596]
- The lane registration the fail-closed manifest requires for that module (row 165 after the KS-L2 and KS-L3 insertions). [1597]
- The architecture-fitness lane registration the fail-closed manifest requires for that proof. [1598]
- The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. [1599]
- The shared fixtures the L27 module imports instead of rebuilding. [1600]
- **The mid-flight reporting boundary:** a completed pass beside a reconciling selection is not this call's success, and a refusal left beside one leads with the mid-flight state. [1601]
- The rewritten contract-scoped activation forcing suite and its shared-source-pair fixture. [1602]
- The registered admission refusal now addresses only the addressed contract's own state. [1603]
- Public closeout exercises the actual pair, attribution and cache-independent delivery. [1604]
- Cache damage cannot change the accepted integration pair or block ref publication. [1605]
- The migration acceptance proof reads only committed trailers. [1606]
- Cache damage cannot change the accepted integration pair or block ref publication. [1607]
- The migration acceptance proof reads only committed trailers. [1608]
- **The completeness node that derives the mandatory set from recorded rows rather than from the implementation's own page manifest.** [1609]
- The ordering node the review sealed as HIGH, and the truncated-page node. [1610]
- **The three path facts, and the case that authors, stores, seeds and resolves a path holding glob characters.** [1611]
- The lookup that ran and could not answer, refused as unavailable rather than absent. [1612]
- The lookup that could not be run at all, reported as the same fact. [1613]
- The continuation bindings, each with its own control, and the read-only property on a real file. [1614]
- The read fixture and its registered contract. [1615]
- The unit-lane row the read's selection module occupies. [1616]
- The two integration-lane rows the read's boundary and path modules occupy. [1617]
- The read fixture and its registered contract. [1618]
- The unit-lane row the read's selection module occupies. [1619]
- **The packet's first non-conforming example, and the node `M1`/`M2` kill.** [1620]
- **The present-outside-versus-absent distinction side by side, and the per-table rule-2 subsumption assertion.** [1621]
- **The forbidden-overreach case: nine verdict words searched over the serialized response, with a positive control.** [1622]
- **The node that drives a real candidate write and refuses its continuation, and the substituted-snapshot refusal.** [1623]
- The expansion, the visible unattributed gap, and the filter that narrows the display and never the comparison. [1624]
- **The fixture and the governed contract it is registered under.** [1625]
- **The fixture and the governed contract it is registered under.** [1626]
- **The harness that owns the admitted candidate and the recorded fixture.** [1627]
- **The refusal an over-budget population raises, which is why the loops live inside their cases.** [1628]
- The publish refusal names the one omitted member, for each of the nine. [1629]
- The all-nine refusal names every member in declaration order. [1630]
- The positive control binds the declaration to the request model's own field order. [1631]
- The prepare text is asserted from the real `_prepare` path. [1632]
- The sibling refusal names the supplied member for each read action. [1633]
- The multi-field refusal names every supplied field in model order, `judgments` included. [1634]
- The freeze branch keeps its own named refusal. [1635]
- **The signal suite's 28 cases, including the nine-parameter required-field table and the two halves of "a conclusion is unrepresentable".** [1636]
- The L27 pane-authority proof, its fixture import from the sibling sweeper suite, and the lane registration the fail-closed manifest requires. [1637]
- **260913-LCA-L8:** the nine exact-consumer rows `mcp/tests/test_terminal_blocker_reasons.py` adds to the evidence registry under the `synthetic-test-evidence-candidate` contract. [1638]
- The read fixture and its registered contract. [1639]
- The two integration-lane rows the read's boundary and path modules occupy. [1640]
- **The fixture and the governed contract it is registered under.** [1641]
- The new case module and its lane marker. [1642]
- The forbidden-name set the whole payload schema is walked against. [1643]
- The row-level proof that a full render stores nothing. [1644]
- The case that the adapter selects nothing, compared value for value. [1645]
- The transport case: typed result, a 400 and a 503. [1646]
- The two `consumers` registrations the module obliged. [1647]
- The five lane rows, appended rather than inserted. [1648]
- **The four consumer registrations the two governed-support consumers and the item-16 case obliged.** [1649]
- **The budget pair the populations are measured against, and the `UsageError` that makes an over-budget lane execute zero tests.** [1650]
- The scaffold the sibling imports, still exported from the kept module. [1651]
- The publication-input cases in their new home, asserting the declaration is the model's own field order. [1652]
- **The module itself: the eight cases and the production composition they drive.** [1653]
- **The production owners the cases measure: the delegated resolution, the capture owner, and the recorded-range resolver.** [1654]
- **The two new classes and the fixtures they drive, including the `_selection()` narrowing helper the type-checked call sites need.** [1655]
- **The carrier-parity case: the vocabulary is derived from a real page, and the unproduced camelCase variants are required to be absent.** [1656]
- **The mounted-route class, which measures the block through the call an agent actually makes. Since MIK-R24 an unconverted memory tree is read as `legacy-format` there, so its two cases assert that, with and without a database.** [1657]
- **The no-datasets fixture shape and the selector-less request the task-context cases use.** [1658]
- **The four cases R02 is measured by through the real composition and the real route.** [1659]
- **The real-repository fixture and the six cases that measure the inventory against every change class.** [1660]
- **The two new unit cases, the narrowing helper the optional selector obliged, and the selector-kind transport case.** [1661]
- New-member context preserves the independent family counterpart. [1662]
- Genuine ambiguity and exact requested history are distinct assertions. [1663]
- The lane row. [1664]
- The record-only successor case (L47-R1-F3). [1665]
- The new cutover module's docstring: what it covers. [1666]
- The new reopen module's docstring. [1667]
- The two lane rows. [1668]
- The public closeout refuses an open item and commits once it is answered. [1669]
- `# The next-move triple, declared here so the worktree surface's guidance is part of` [1670]
- refuse a `nextTool` outside the roster (`_require_registered_public_next_tool`) [1671]

- The trace's effective-prompt key, which the live capsule scenarios assert against. [1672]
- The lifecycle catalog registration for the shared support module, with its four derived consumers. [1673]
- The lifecycle catalog registration for the shared support module, with its four derived consumers. [1674]
- The lifecycle catalog registration for the shared support module, with its four derived consumers. [1675]
- The lifecycle catalog registration for the shared support module, with its four derived consumers. [1676]
- Development commands, budgets, diagnostic metrics and isolation. [1677]
- Certifying publication and accepting consumers. [1678]
- The lane rows that admit both L14 modules to the `unit-regression` lane. [1679]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1680]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1681]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1682]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1683]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1684]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1685]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1686]
- The three `scripts/e2e_harness` [[artifact]] rows a leaf under that permanent support root must register. [1687]
- The lane rows that admit both L14 modules to the `unit-regression` lane. [1688]
- The lane row that admits the L3 module: `test_memory_backfill.py` in the `unit-regression` lane. [1689]
- The contract-scoped activation record: one record per series contract, keyed by the contract fingerprint rather than a source pair. [1690]
- The L36 lane registration the fail-closed manifest requires. [1691]
- The lane registration the fail-closed manifest requires for that module. [1692]
- The L4 census module's lane row, which closed the gap the L4 route section recorded. [1693]
- The lane registration the fail-closed manifest requires for that module (row 165 after the KS-L2 and KS-L3 insertions). [1694]
- The architecture-fitness lane registration the fail-closed manifest requires for that proof. [1695]
- The rewritten contract-scoped activation forcing suite and its shared-source-pair fixture. [1696]
