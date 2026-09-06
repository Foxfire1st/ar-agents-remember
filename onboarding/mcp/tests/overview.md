# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/tests/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-09-06T00:38:37+00:00 |
| lastVerifiedCommitHash | `97e8ed2e1fae21756c3ad995c30613d4fbfcc503` |
| lastVerifiedCommitDate | 2026-09-06T02:09:33+02:00 |
| governingOverview | `../overview.md` |

## Governing Overview

[mcp overview](../overview.md)

## Current CCR assertion and integration boundaries

The current test tree distinguishes portable certification primitives from the host composition that constructs them. `test_certification_lane_bridge.py` compares the real R22 rail population plus Gate-5 memory rails with the derived five-gate R11 plan and checks provenance-independent identities. `test_gate_certification_records.py` invokes the real host gate seam but replaces clean execution with hand-built published payloads; its green certificate assertions are not proof that Dagger produced every referenced byte.

R05/R16/R07/R08 test families exercise admission/dependencies, telemetry journals, incremental closure, and final memory certification through their library owners. The R07 recording executor proves non-accepting incremental success; the R08 fixture supplies executed-check results to the final certifier. Neither constructs missing production callers. Likewise the R13/R14 run-control suites use injected inspectors/runners and temporary authority stores, so their lane classification does not imply a live Codex or Dagger invocation. The separately owned real-Codex clean-room route remains required.

L30's source-index recovery adds real linked-checkout evidence for an explicit Git candidate population. `test_memory_citation_source_index_snapshot.py` preserves ordinary filesystem discovery while exercising staged additions/deletions/renames, excluded generated competitors, retained tracked ignored source, exact frozen policy/tree binding, unsafe or changed source refusal, and capacity checks before Git hashing. Its hash-race cases run the actual Git hash command before injecting a source change; malformed census and truncated-response cases are explicit transport fault injection. The L6 source-index/database companions follow the shared state-layer bound owner and require explicit candidate identity in generation metadata.

`test_memory_incremental_scope_owners.py` composes real Git deltas, the actual citation index and R06 observation, including post-acquisition tracked-source revalidation. `test_memory_incremental_scope_model_edges.py` additionally composes real candidate Git nodes, citation edges, R06 scope, R07 planning and the production range checker. Valid ranges succeed and invalid ranges/ignored generated targets produce the expected checker findings. That case retains fixture-supplied task/admission/gate-prefix facts; it proves the library composition without establishing production admission, full Gate-5 execution or lifecycle acceptance.

L30 replaces the accepted-gap census with complete artifact-map and producer/export/host-consumer checks. `test_rail_evidence_publication.py` uses the actual clean-room reporting owners for checkpoint serialization, verifies provider phase reporting and arbitrary byte capture publication, and retains negative cases for unavailable/missing output. Its container doubles are distinct from the separately required real Dagger/clean-room execution. `test_gate_certification_evidence.py` protects selected-journal bounds, cross-authority refusal, immutable-generation retention and physical report reopening. `test_dagger_registry_lock.py` proves host admission, unchanged checkout isolation, nested release and real process/thread exclusion. R10 deterministic-projection tests still include the declined-repair expectation until L32 lands.

Current targeted tests explicitly require incomplete ownership to refuse with `test-selection-ownership-incomplete`, empty selected outputs, and no broader test command. Retry proof identity includes `selectionDigest`; a changed selection forces fresh evidence. Task-intent matrices separately cover exact text, supplemental typed packet refs, observational exclusions, consumer currentness and bounded legacy archival; direct evidence dependencies are typed, bounded and acyclic.

| Finding | Anchor | Source |
| --- | --- | --- |
| The real repository-profile bridge preserves every applicable repository rail and adds the memory-rail population. | `test_bridge_derives_one_canonical_five_gate_authority_from_the_real_profile` | mcp/tests/test_certification_lane_bridge.py:74-108 |
| Bridge digests are stable when only creation provenance changes. | `test_bridge_is_deterministic_and_ignores_creation_provenance` | mcp/tests/test_certification_lane_bridge.py:111-122 |
| R07 success remains non-accepting and keeps final-full obligations pending. | `test_r07_execution_publishes_every_member_and_never_promotes_incremental_success` | mcp/tests/test_memory_incremental_scope_compiler.py:896-917 |
| R08 green composition receives already-executed checker facts from its fixture, then binds the exact candidate pair. | `_evidence`; `test_final_certification_green_binds_exact_pair_and_gate_five_inputs` | mcp/tests/test_final_full_memory_coherence_certification.py:858-885; mcp/tests/test_final_full_memory_coherence_certification.py:888-904 |
| Missing profile authority is a typed refusal, never a skipped code gate. | `test_preview_refuses_a_missing_profile_instead_of_skipping` | mcp/tests/test_worktree_quality_gate_runner.py:119-140 |
| The current frontend and HTTP assertion oracles are 441 TypeScript inputs and 292 declared/139 driven/153 undriven response pairs. | `test_dashboard_build_reports_only_config_owned_stable_inputs`; `test_the_conformance_table_accounts_for_every_declared_pair` | mcp/tests/test_quality_scope_reporting.py:702-736; mcp/tests/test_serving_response_conformance_live.py:515-526 |
| Exact candidate acquisition follows staged Git membership while ordinary discovery remains available. | `test_linked_candidate_excludes_generated_competitors_but_retains_tracked_ignored_files`; `test_staged_add_delete_and_rename_define_the_candidate_without_moving_head` | mcp/tests/test_memory_citation_source_index_snapshot.py:314-366; mcp/tests/test_memory_citation_source_index_snapshot.py:368-386 |
| Capacity refuses before Git hashing and preserves previous readiness. | `test_candidate_size_cap_refuses_before_hashing_tracked_or_dirty_oversized_members`; `test_candidate_population_caps_refuse_before_hashing_and_preserve_prior_readiness` | mcp/tests/test_memory_citation_source_index_snapshot.py:688-722; mcp/tests/test_memory_citation_source_index_snapshot.py:724-751 |
| R06 observes actual staged candidate files and revalidates tracked source after acquisition. | `test_source_index_composes_exact_staged_git_members_with_real_candidate_observation`; `test_source_index_observer_revalidates_tracked_bytes_and_unsafe_nodes_after_acquisition` | mcp/tests/test_memory_incremental_scope_owners.py:255-279; mcp/tests/test_memory_incremental_scope_owners.py:283-306 |
| Actual R07 range-checker composition excludes generated competitors and refuses another candidate before checker start. | `test_r07_real_range_checker_uses_only_the_candidate_source_population`; `test_r07_range_executor_refuses_another_candidate_before_checker_start` | mcp/tests/test_memory_incremental_scope_model_edges.py:520-568; mcp/tests/test_memory_incremental_scope_model_edges.py:572-594 |

## CCR-R01 Evidence-Lane Ownership

Nine focused CCR-R01 suites are explicitly classified as `unit-regression` in
`test-evidence-lanes.toml`: field effects, indexed graph admission, semantic-topology field
effects/refusals/scaling, projection source facts, and the three closeout-projection,
semantic-topology, and task-document coverage-edge companions. They are deterministic ordinary
pytest regressions over production owners and no longer enter the closed test population as
unclassified files. The lane assignment governs selection and execution cost; it does not promote
these tests into durable task evidence or replace independent requirement review.

## Repository-Neutral Certification Contract Evidence

`test_certification_rail_registry.py` proves the portable five-gate registry, exhaustive semantic
findings, deterministic candidate-bound plans, strict evidence/artifact/blocker contracts, and
complete typed terminal manifests. `test_certification_plan_authority.py` independently proves
canonical plan authority, hostile-input pre-allocation refusal, exact budget boundaries, graph
storage/operation census, and scaling headroom.

Three focused edge companions make the previously aggregate boundaries independently falsifiable.
`test_certification_contract_model_edges.py` owns closed models, digests, plan catalogs, terminal
identity, and immutable error payloads. `test_certification_reachability_edges.py` owns prospective
and raw-budget refusal plus both bounded graph-search directions.
`test_certification_registry_validation_edges.py` owns typed profile, member, prerequisite, and
artifact semantic findings.

The closed lane manifest classifies all five suites as `unit-regression`, matching their in-process
owned-product-behavior boundary. Omission fails before test collection instead of selecting a
default or broader execution lane.

All five suites consume `certification_registry_test_support.py` as one permanent internal-canonical
composition owner. Its portable sample profile and generated graph families deliberately contain
no Agents Remember rail inventory. `evidence-lifecycle.toml` declares exactly these five consumers;
the helper is neither copied into the suites nor treated as an unowned test input. This evidence
tests the generic contract foundation, not the later repository-profile executor or clean-room
acceptance integration.

## ARSPAWN-L5 A005 Review-Repair Evidence

The A005 repair keeps production rules strict and corrects the forcing worlds around them. Reviewer
fixtures now carry current lineage, settings-owned launch selection, and explicit structural parent
provenance. Fake-host concurrency and WebSocket rows declare the liveness their assertions assume;
they do not weaken background reconciliation. Catalog and dashboard scope pins historically reflected the reviewed 68-field wire and 436 TypeScript inputs; the current requirement-route delta advances the dashboard oracle to 441 inputs. The final acceptance remains Dagger-owned.

## ARSPAWN-L4 Public Advertisement Acceptance

`test_public_surface_conformance.py` separates two proofs that must not be collapsed. It parses all
eight production starters and requires the self-updating `uvx --refresh-package
agents-remember-mcp agents-remember-mcp@latest` contract, so users never have to remember manual
MCP updates. Separately, its disposable stdio process imports the exact local candidate and
correlates live tools/schema with content digest, package root, interpreter, and `server_info`;
using `@latest` for that proof would test PyPI rather than the candidate.

The same module checks exact ordered live inventory, response-model ownership, closed dispatch
schema and caller-description facts, before-handler refusal of undeclared spend input and invalid
roles, and strict ambient outcome envelopes. It is explicitly assigned to the integration evidence
lane because the acceptance launches real MCP subprocesses.

The test reuses the runtime-settings builder through `test_config.py`; that path reaches the
closeout and curator-coherence fixture roots through `test_worktree_support.py`. The lifecycle
catalog therefore names this suite as an exact transitive consumer of both shared-support roots,
and the focused catalog validator proves the declaration matches the source-derived graph.

## Exact Future-Code Candidate Identity

`test_future_code_candidate.py` owns the real-Git mutation matrix for the plane-derived
future-code route identity. It proves isolated add-all semantics across staged and unstaged
content, deletions, renames, eligible untracked files, ignored files, and real-index preservation.
It also proves closeout-snapshot consumption, collision-free concurrent captures with no temporary
residue, and identity immutability. Its refusal cases force changed candidate/base/HEAD facts,
mid-observation HEAD movement, non-leaf route exclusion, and strict missing/extra schema fields.
The existing closeout-input boundary
continues to prove that a same-tree HEAD move is not silently accepted as an in-flight operation
output without journal evidence.
The module is explicitly registered in the integration evidence lane because its core proof uses
real temporary Git repositories; unknown-lane fallback remains forbidden.

## IAS Frozen Source-Pair Coordination Evidence

The focused forcing boundary must prove architecture, not just successful Git commands: multiple
live series coexist; selection replacement pauses old work; `reconciling` blocks implementation
exposure; task authoring remains independent of implementation selection, retains its serialized publication lock, and invalidates projections according to field effects; the queue owns no
lifecycle or commit evidence; retained code and memory conflicts can be agent-resolved and
continued or exactly cancelled; stable-journal status survives task/contract damage; terminal
cleanup cannot clear another selected master; and malformed authority fails closed without a
fallback reader.

The frozen forcing surface includes 22 changed/new files. Six focused edge suites partition the
stable journal, exact Git proof, sync driver, recovery, activation owner, and cross-boundary public
composition so coverage pressure does not collapse those contracts back into one oversized test.
Three shared/refusal files were also refreshed: structural refusal cases explicitly neutralize
source-pair admission when testing a later dispatch branch; shared worktree fixtures seed canonical
external-memory ledger mappings; and existing-series adoption now supplies the ref that production
must prove rather than expecting adoption to invent it.

The current delta also updates the existing registration-wiring suite to prove that
the public `worktree_sync` registration forwards optional `resolution_action` alongside
`memory_sync_choice` and the canonical contract path. This is source-shape evidence only; curation
does not claim to have executed Dagger.

Exact suite membership and line-level claims are reconciled to the frozen candidate. Acceptance
execution remains architect-owned evidence rather than a curator-authored claim.

## IAS Ledger-History Regression Boundary

Focused coverage now proves the missing memory-only case end to end: unchanged code can receive a
newer settings memory commit and ledger row while the older same-code row remains history.
Source-pair admission accepts the newest mapping; memory merge preserves every exact parent row;
closeout/direct recovery appends the new state; integration requires one new prefix; and
organizational completion separates current lookup from exact historical containment.

## 260824-PDLS Current Evidence Topology

`evidence-lifecycle.toml` is the complete durable-artifact and shared-support census: authority,
fidelity, category, cadence, lifetime, expiry/replacement, and consumers are executable metadata.
Provider recordings remain external-versioned proof; synthetic helper worlds are explicitly
internal and cannot masquerade as recordings. The former task/date model-split snapshot and its
meta-test are deleted, with lasting architecture assertions moved to ordinary behavior tests.

Candidate A's sealed manifest, static closure helpers, synthetic cohort builder, host runner, and
self-tests are deleted. `test_kernel_pure_regressions.py` retains the seven unique product
assertions as ordinary explicit unit-regression evidence and supplies the exact pure cohort for the
non-accepting representative Dagger measurement. `_evidence_catalog_fixture.py` remains the one
lifecycle-catalog test builder. Provider replay scripts live in `_adapter_event_scripts.py`,
independent from `_control_plane.py`'s structural harness. These helpers are cataloged support, not
pytest test modules and not acceptance evidence.

`_quality_evidence_fixture.py` is the one acceptance-consumer fixture that publishes the immutable
result generation a passing mocked gate promises; a green dictionary alone is intentionally
insufficient. `task_reopen_test_support.py` centralizes the real branch, enclosure, runtime, and
task-document predecessor world for the reopen family. Both are test support only and acquire no
production mutation or acceptance authority.

Ordinary tests, shared support, plugins, and governed fixtures all participate in the same
dependency-ownership graph. The graph's reasons feed targeted selection and retry invalidation;
causal suppression uses only proven import/catalog edges. Coverage/CRAP measure product code only,
while every test/support Python file remains linted, typed, size-checked, and executable.

Retry deltas preserve that ownership boundary without losing collection-time coverage:
`test_quality_retry_proof.py` pins the command split, and `test_retry_selection.py` proves the
plugin keeps only explicit affected modules, accepts an observed passing zero-body module
collection, and separately refuses empty, escaping, or genuinely uncollected populations.
`test_retry_coverage.py` proves retained and fresh Coverage.py databases are merged
explicitly into one scored data/JSON pair, an all-contexts-affected delta has a distinct
known-empty retained state, and a missing expected database removes both outputs.
`test_quality_evidence_helper_invariants.py` extracts and executes only the actual comment helper
to prove controlled Python evidence mutations retain Ruff-valid module spacing without importing
the scenario catalog and falsely acquiring ownership of all its fixture paths.
`test_quality_subprocess_environment.py` proves nested candidate tests cannot inherit the outer
wrapper's retry cache or progress path while admission and other semantic environment facts remain.
All three focused forcing files are explicitly classified as `unit-regression`.

The retry matrix also exposed missing changed-branch coverage in the direct-landing CRAP repair.
`test_direct_landing_execution_helpers.py` now owns exact existing-mapping bytes, clean branch
snapshots, and prepared ledger-intent convergence. The focused `test_direct_recovery_*` cases in
`test_lifecycle_reconciliation_concurrency_l2.py` own developer-decision refusal, typed-error fact
preservation, current-record recovery, and untyped interruption translation. These tests repair
candidate coverage without widening the current selected test population: invalid reuse executes that selected population freshly, while unresolved selection authority refuses.

## M38 Requirement-Acceptance Structural Proof

`test_requirement_acceptance_envelope_doctrine.py` is a focused architecture-fitness suite over
canonical lifecycle and task-workflow sources. It separately pins the complete worker envelope and
explicit Checks section, independent per-ID reviewer adjudication, manager preservation of the
exact stable-ID + version set, and separation of the durable-evidence promotion hold point. Its explicit
`architecture-fitness` membership in `test-evidence-lanes.toml` prevents the new proof from being
silently classified by a filename or default marker.

This is structural doctrine evidence: it catches removal of mandatory template fields and aggregate
completion regressions. It does not claim that a human or agent actually inspected cited artifacts;
that remains the reviewer-owned per-requirement adjudication recorded in the durable verdict.

## M40-M45 Requirement Attempt Journal Structural Proof

`test_requirement_attempt_journal_doctrine.py` pins the separation between semantic requirement
revision and delivery attempt, immutable candidate-bound worker append, independent exact-attempt
reviewer append, predecessor/finding lineage after rejection, bounded regression/revision
invalidation of accepted work, the closed five-class failure taxonomy, developer-owned requirement
revision, authoritative leaf journals, and a rebuildable non-gating master summary. It is explicitly
`architecture-fitness` evidence and does not make the summary a runtime, queue, or task-authoring
gate.

The structural proof also requires one physical leaf journal. Worker and independent reviewer
records append to the same ordered authority; worker reports and verdicts link exact anchors rather
than copying records into divergent authorities.

The M42 forcing explicitly distinguishes a candidate that changes before adjudication from an
unrelated candidate that lands after acceptance. The former needs a successor attempt; the latter
does not reopen accepted work without direct-regression proof plus bounded owner invalidation or an
approved requirement revision.

## M39 Requirement-Compilation And Quality-Policy Split

`test_requirement_compilation_gate_doctrine.py` pins the architect-owned pre-topology gate,
complete canonical packet shape, transcript-free cold-read questions, filtered task projections,
one-primary-requirement leaves, and version invalidation/rebriefing. It is pure
`architecture-fitness` evidence; `scripts/sync-skills.py --check` separately proves installed and
packaged projections equal the canonical skills tree.

The prior oversized `test_code_quality_check.py` mixed general quality-wrapper behavior with the
MCP wire-signature exemption. `test_code_quality_tool_signature_exemption.py` now owns the latter
as explicit architecture-fitness evidence, while `_ruff_repository_evidence.py` centralizes only
the real repository-configured Ruff invocation used by both suites. The helper and exact consumers
are lifecycle-cataloged under `repository-ruff-policy-evidence`; there is no duplicated fallback
configuration.

## Historical L3 Final Targeted-Gate Repair

The sequential-lane, read-degradation and legacy-nature filenames below record the earlier implementation; removed modules are not current test entry points. Current source-pair selection and task-intent evidence supersede their prior lane assumptions.

The final closeout-queue repair set turns the prior targeted Dagger artifact into exact owner
coverage: scheduling registers are forced against the canonical orchestration template and reject
missing outer pipes; lifecycle completion/release, task-publication error translation, partial
artifact removal, initial sprint-status WAL recovery, finalize refusal, and live MCP registration
each run through their production owner. Response-conformance worktree fixtures always retain a
real commanding sprint while `executionGraph` alone distinguishes queue-managed from intentionally
unmanaged payloads. 260815-DAG-L13 adds five focused suites: `test_sequential_default_mode.py`
(the atomic-sequential default and its series lane), `test_queue_read_degradation.py` (the
degraded `status` readout), `test_register_scaffold.py` (sprint-creation register scaffolding and
write-time shape validation), `test_legacy_nature_tolerance.py` (nature-less legacy masters
resolving atomically), and `test_closeout_lane_sync_first.py` (sync-first recovery naming and
lane-occupying exclusivity).

The next targeted artifact was behaviorally one assertion short and reached 99.92% changed
coverage. Its final bounded correction distinguishes a normal worker process that durably records
a failed command from an actual worker exception, then proves the exception combines a failed
reversible queue release into the durable reason. This owns the last changed line and branch
without weakening production.

## Final Ruff-Safe Package-Root Resolution

Five test modules that inspect the loaded package root now read
`sys.modules["agents_remember"].__file__` after their normal package-submodule imports have loaded
the package. The source-root checks and scan boundaries are unchanged; this removes the disputed
bare/direct package import entirely without adding or retaining a Ruff configuration exception.

## L23 Real-Lineage Fixture Boundary

The shared external-memory integration fixtures now build a real super→master→leaf code and memory
chain and bind leaf contracts to the parent series contract. Assertions read task-derived source
branches rather than a literal `main`. A master source that moves after leaf closeout therefore
refuses at integration admission as `source-lineage-stale` with `sync_source_lineage`, before
replay/conflict logic or any branch movement. Dedicated integration-quality tests separately cover
the two post-quality source-tip rechecks and the legacy replay helper's internal branch matrix;
gate-only seams mock lineage where that independent boundary is not their subject.

## Structural Seat Regression Boundary

`test_structural_agent_tools.py` pins both directions of replacement-aware messaging, ambiguity
refusal, curator admission, and atomic-series bootstrap/recovery. `test_dispatch_agent_ambient.py`
(extracted by the 260821-ARSPAWN-L1 file-size fix) owns the complete ambient/plane caller-mode
dispatch cohort — spawn without hosted env, unknown-ref/altitude-mismatch refusals, plane
provenance, ambient and plane rollback, stale plane identity, unauthorized child-role refusal,
and sender-less brief post. The ARSPAWN-L5 closeout split moved the final three plane tests there
unchanged so the structural suite returned below the 1,200-line hard limit.
`test_spawn_agent_session.py` asserts the real primitive's caller-kind provenance (`spawnedByKind`
on the payload and the catalog row). `test_agent_doctrine_plane_identity.py` rejects
agent-instruction regressions to control-plane id cognition and proves packaged lifecycle doctrine
is byte-identical to canonical source. `test_seat_lifecycle.py` exercises the task-document-owned
retire, land, and completion-cleanup matrix; its turn-report fixture is `AgentRole`-typed so the
worker/reviewer/curator cases preserve the wire vocabulary under full Pyright. Existing routing,
inbox, catalog, serving-response, and wire-vocabulary suites cover the broader migration surface.

`test_leaf_structural_coverage.py` retains the wrapper-adjacent cross-package seams, while
`test_task_document_structural_identity.py` owns migration, topology, structural-gate,
identity-migration, and platform-quality-environment branches. The quality-runner policy suite is
separate from closeout mutation, and citation routing is separate from provenance history; all six
resulting responsibility units stay below the hard 1,200-line gate. The separate
`test_leaf_structural_refusal_coverage.py` concentrates the fail-closed matrix:
ambiguous or missing seats/topology, invalid durable shapes, persistence-first dispatch rollback,
structural mutation refusals, dead/live binding conflicts, and exact dispatch/launch boundaries.
These are focused coverage companions. The current targeted selector refuses incomplete ownership rather than expanding to a full population; proof reuse failure can require a fresh run only within the admitted selection.

The three installed harness suites convert OS/subprocess failure of their version probe into an
explicit unavailable-runtime skip. `test_quality_scope_reporting.py` applies the same boundary only
to its two live Node assertions. No skip records observed fixture evidence or weakens assertions
when the external runtime is present.

Codex app-server fakes use the current Desktop host-first user-agent product and exact
`(agents_remember; 3.0.0)` client suffix. The retired client-first fixture shape is not retained as
an unused compatibility contract.

## Leaf Memory Pre-Closeout Gate

`test_memory_tool_enclosure_scope.py` distinguishes leaf and official memory with two real trees.
Its quality checks pin the additional provenance rule: a contract-scoped call feeds the leaf
contract's code-base commit to claim comparison, while a bare official-memory call leaves unstamped
provenance absent. That makes dirty-worktree claim repair available before closeout without
fabricating a future verification stamp.
cit:(["test_a_contract_scoped_check_uses_the_leaf_base_for_unstamped_claims"; "test_the_bare_check_does_not_invent_unstamped_claim_provenance"], mcp/tests/test_memory_tool_enclosure_scope.py:356-356; mcp/tests/test_memory_tool_enclosure_scope.py:376-376)

## Quality Command Construction

L23 adds three forcing groups. `test_lifecycle_operations.py` owns task-addressed start/observe,
immutable candidate/input identity, stale recovery, cancellation boundary, detached launch, worker
progress, terminal state, and packaged worker service composition before dispatch.
Its packaged-entry proof now pins the explicit lifecycle-operation declaration before service
construction and contains the singleton during script-entry execution. The paired checkout-isolation
case proves this mode retains live task-operation authority without claiming an MCP/dashboard daemon
role.
The same lifecycle group proves detached launch preserves the installed MCP `PYTHONPATH` and excludes
the task checkout source root, so task code cannot silently replace the installed worker runtime.
The clean-quality group (`test_agents_remember_quality.py`,
`test_clean_quality_executor.py`, `test_clean_room.py`, and the Codex clean-room probe) separates
Dagger graph semantics, host execution, CLI translation, and real-when-available harness proof.
Its ambient-harness structure tests also require the fixture tmux server's explicit option scope
and require Codex to forward the dynamic `TMUX_TMPDIR` into the candidate MCP child, preventing
session creation from diverging from the liveness and teardown namespace. The same focused group
pins strict decoding of Codex's current `Wall time`/`Output` result envelope, so C09 can prove
successful public dispatches without accepting arbitrary prefix text.
`test_platform_subprocess.py` owns the WSL/UNC/Windows-shim refusal matrix plus deterministic
existing-native `$HOME/.local/bin` admission and executable resolution, while the small L23
notifier batch suite keeps structural expiry-address edge coverage below the file-size rail.

`test_code_quality_check_scope.py` proves root pytest `addopts` includes `-n=auto`, while the
derived-scope command test separately retains its coverage targets. This pins the single
configuration owner used by pytest inside the attested Dagger boundary.

`test_code_quality_check.py` now exercises both sides of the L23 progress-report precedence seam in
one targeted-configuration regression: an omitted CLI path derives from
`AR_QUALITY_PROGRESS_REPORT`, while a subsequently supplied explicit path overrides the still-set
environment value. The paired calls retain the repository file-size arm and close the final
targeted Dagger diff-coverage edge without changing production configuration behavior.

The session-level conftest assigns every xdist worker a private `XDG_CACHE_HOME` below its worker
base temp directory, leaving the non-xdist master environment unchanged. Parameterized tests pass
only serializable diagnostic values to `subTest`; those edits do not change the assertions.

The basic Codex adapter suite exhausts the session settings-update transition through public
notifications: already-effective and stale-effective echoes are inert, a desired echo promotes,
and unrelated drift fails closed. This is branch coverage for the changed production session
owner, not a CRAP exemption.

## Purpose

Regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

The L1 execution-topology forcing slice adds two focused seams. `test_task_execution_topology.py`
drives strict graph validation, exact cross-document alias membership, production
create/replace/set-field authoring (including master/sprint kind downgrade), finite migration
preview/apply/rollback, deterministic rendering, and projection. The single-owner suite separately
forces every supported import spelling of `write_task_doc_batch`, keeping publisher authority
independent from topology behavior. The first targeted Dagger artifact then tightened this route:
the legacy application split now expects migration-required rather than implicit sprint creation,
and the focused suite forces every reported refusal branch plus multi-parent DAG release without a
coverage exclusion.

Checkout coordination isolation coverage (`test_checkout_coordination_isolation.py`) reproduces
the L19 unpublished-writer failure shape without touching live state: loaded-source linked/primary
classification, synthetic leaf config, incident-shaped inbox placement, pre-lock escape refusal,
manual rewrite refusal, trusted MCP preservation, explicit pytest temporary-root behavior, and
the task-local operational-report exception. The report case writes beneath the exact enclosure
`reports/` root and simultaneously proves no sibling inbox row is created, keeping that artifact
path distinct from coordination authority.

Terminal host registry coverage treats tmux argv as an option grammar rather than a fixed
slot layout: the custom-name regression finds `-s` and checks its operand, preserving the same
name-override assertion whether optional synchronized-frame capability flags are present or absent.

The stable structured-conversation contract gate: the contract suite uses
hostile sibling-product matrices to pin purpose-bound cursors, exact provenance, canonical status,
evidence-backed capabilities, operation identity/rollback, authoritative queued withdrawal
recovery, attachments, metrics, and fixture non-promotion. The foundation suite separately pins
exactly two read ports, three owned child routers, one global registration seam,
repository-only native-helper resolution, and redacted installed-runtime fixtures. These tests do
not claim a projector, native-history implementation, control service, or renderer exists.

The active conversation serving regression set: four focused suites cover
the implemented slice — canonical status classification/revision discipline with full-product
orchestration parity, per-harness mapper grammars with hostile shapes, the projector engine and
store (hydration, ordering, idempotence, provenance, rehydration, tool convergence, overflow and
zipper gap mechanics), and the production routes over a REAL composition (bridge + IPC server on
a real socket, real catalog row, the single route registration, HTTP over loopback uvicorn) proving
native identity, cursor forgery refusals, dual-cursor agreement, epoch-flip gap+close,
provenance through the real authority, orchestration parity, and absence of PTY/runner-log/
fixture production authority. The foundation pin asserts the active child's exact three-route
surface.

The native conversation library regression set: six focused suites cover the
implemented slice on doubled boundaries — ASGI routes with the exact O4 status ladder, cursor/key
and scope contracts, live gate demotion rules, port normalization with hostile shapes, and the
open service's idempotence/race/ownership arms — while the opt-in installed-runtime suite proves
the live Codex and Pi gates, both real end-to-end opens, and the Claude version-mismatch
fail-closed posture. The foundation pin asserts the library child's exact five-route surface and
the extended helper source set; the three runtime fixtures record observed (never enabling)
gate/open rows.

The native control-plane regression set: the contract suite
(`test_harness_control_plane.py`, 25 tests + 35 subtests) pins the interrupt write/ack/replay-once
with exact-turn and expected-operation guards plus the successor zero-write refusal, the paged
never-bodies timeline (all sources/kinds, union completeness, eviction-floor honesty, the full
256-record budget edge, epoch-flip typed), the asset channel (schema/traversal/verification
batteries, native construction with zero-write rejection, unsupported receipt, asset-conditional
digest), the once-only withdrawal recovery with byte-preserved tombstone/`cockpit_only`, and the
strict client validators. The opt-in installed suite (`test_harness_control_plane_installed.py`)
captures the same seams live against pinned codex 0.144.5 and pi 0.80.7 and enforces the Claude
version-honesty rows; the three runtime fixtures gain redacted `control-plane/*` rows with
`enablesCapabilities: false` — evidence, never enablement.

The authoritative control-API regression set: a shared topology
(`_control_plane.py`) runs the real bridge + IPC server on a real socket, the real submission
authority, and the single route composition with only the harness adapter doubled, plus the manager-
authorized `NOW`-anchored control service seeded into the `_SERVICES` memo so lease arithmetic is
time-consistent. Four focused service/route suites drive it: `test_conversation_control_operations.py`
(interrupt ledger — ack≠settlement, fingerprint idempotence with native-write counting, lost-response
reconcile, the guard battery, and both the Finding 1 content-ful and Finding 2 oversized/clipped pi
settlement regressions, each proven non-vacuous), `test_conversation_control_queue.py` (never-bodies
queue truth, the queued→dispatching race, the bounded recovery lease with an untouched frozen-clock
expiry proof, and the forgery battery), `test_conversation_control_attachments.py` (boundary-exact
limit refusals, one-use exact-receipt submit, recoverable-under-lease rebind with on-disk deletion,
timeline-driven reconcile, GET-only policy, and absent-not-zero telemetry), and
`test_conversation_control_api.py` (the seventeen routes over a real uvicorn wire with O4 mapping,
remote-peer 403, policy 405s, and the no-paste/no-substitution source scan). The opt-in
`test_conversation_control_installed.py` proves live codex/pi interrupt ack+settlement, queue truth,
withdrawal recovery, typed attachment submit, and telemetry through the registered routes plus the
Claude version-honesty gate. The foundation pin asserts the control child's exact seventeen-route
surface.

The evidence-backed hardening regression set for the production-E2E gate:
`test_chats_l5_hardening.py` pins the two master hardening obligations at their origin, each
non-vacuous on stashed source: the hosted-interaction synchronizer 500 that aborted the whole
terminal-catalog sweep (now quarantined fail-loud per row, with logging only on state change) and
the unknown-input provenance-validator 500 from a native re-map splitting a resolved user item's
authority triple (now pinned, with an identical re-map a true no-op). `test_conversation_active_service.py`
gains the projector-tier companions (the model-valid re-map and the three twin-suppression
tests, driving the real poll path), and the opt-in `test_conversation_control_installed.py` gains the
installed regression proving a settled live codex turn projects EXACTLY once on the re-read
conversation page (`2 != 1` on stashed `projector.py`). The 10,000-item DOM/interaction baseline + axe
tripwire lives in the dashboard test tree (`renderer.test.tsx`), not here.

The half-time functional regression set: `test_chats_l5f_leaks.py`
pins the per-session bounds (`SessionLockLeakTests`: `release_session` drops the lock + every
epoch channel; `_locks` bounded evicting idle-first; a held lock is never evicted; and
`QueueRowsBoundTests`: `queue_rows` capped with oldest eviction). `test_conversation_active_projectors.py`
gains the codex startup-burst-mints-zero-unknown-vendor / method-carried-mapping /
truly-unknown-names-the-method tests plus the claude `command_lifecycle` recognized-and-drift and
`rate_limit_event` drop tests; `test_conversation_active_service.py` gains the non-user-echo-skip
and the `DormantReleaseTests` (heavy-projection release + shell retire).
`test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` pins that `FeatureCapability` has no `for_observed_runtime` predicate
(the contract is the only gate), `test_conversation_control_operations.py` pins the unverified
refusal now carries a contract reason (not a version comparison), and
`test_conversation_library_gates.py`/`test_conversation_library_installed.py` pin that a version drift
still ENABLES when the contract probe passes (the codex/pi exact-identity installed skips
on drift are recorded conservatism). `test_harness_control_evidence.py` pins the native method carried
onto the frame + stripped from the byte-identical snapshot + IPC round trip,
`test_harness_control_client.py` pins that a refused control socket yields the honest note and unlinks
the stale socket, `test_harness_launch.py` pins accepting an alias collapsed onto the default
resolved model while still refusing a genuinely different model, and `test_provider_containment.py` pins
the docker-ps timeout bounded into an error-annotated sample.

The first end-to-end authoritative submit/withdraw regression matrix: the new
focused authority suite and expanded common/API/native-adapter suites prove one epoch-bound
prompt/setter timeline, atomic queued-withdraw versus dispatch, exact full-ref completion,
completion-before-receipt dominance, no native queue/steer fallback, bounded privacy-aware retention,
and browser-visible status semantics. That historical review closed the then-recorded submission blockers; it is not an assertion about later CCR findings.

A fake-adapter conformance suite covers normalized harness control,
correlated acceptance/reconciliation, private IPC, bounded queue/ledger behavior, shutdown failure
paths, and surface-owned draft preservation. Existing settings, harness, catalog, opener, and
WebSocket tests pin the additive launch/API projections and preserve legacy behavior.
Fake and stdio transport coverage pins the Codex app-server:
exact initialize/model/thread setup, protocol-only effort validation and echoing, structured
status/completion and server requests, explicit busy behavior, bounded malformed/oversized input,
and reconnect correlation without resend. An opt-in live smoke proves exact-version readiness using
an ephemeral thread with no prompt or credential output.

The current Codex completion regressions prove that parent terminal events carry the exact durable
operation/request id, so accepted and initially queued inbox receipts both converge onto their own
row. A null protocol `requestId` is resolved only by the protocol-owned text vendor correlation on
exactly one accepted inbox row in the same hosted session. Missing, non-text, unmatched, and
ambiguous correlation evidence fails loudly. Completion records adapter delivery metadata on that
same row while explicit inbox state remains `pending` and unconsumed; terminal state is `idle` /
`immediate` without a queued replacement and `settling` / `queued` only for an actual replacement.
Exact 2.1.207, 0.144.3, and 0.80.7 values remain fixture/smoke evidence, not production pins.

Pinned Claude Code 2.1.207 JSONL fixtures, fake-transport conformance,
a real-local-subprocess lifecycle tier,
and an opt-in credential-safe live smoke cover the Claude adapter boundary. The smoke submits the advertised local `/cost` command
through the same correlated acceptance/result path without a model API request.
The lifecycle tier sits between the fake and the credentialed smoke: `test_claude_stream_transport.py`
drives a real stdin-waiting child through start -> completed stop -> start to pin process-ownership
release plus the live double-start refusal, and `test_harness_control_claude.py` drives the real
adapter over the real transport against a local stream-json stub to prove the floor probe's
stop/re-launch reaches control readiness with a selectable model and effort. Both use local
interpreter children, so this tier costs no credentials and no model tokens. A mixed
`success`/`is_error=true` API-429 regression remains failed and retains only safe terminal metadata;
no result text, stderr, credentials, environment, or settings are emitted or retained.

The active Claude fake-transport fixture root is 2.1.210. Its initialization
fixture is the current test authority for separate control initialization, `system/init`, a
zero-turn bootstrap result, and correlated `list_models`; its interaction and turn companions keep
durable gates and acceptance-versus-completion covered in the same versioned cohort. The 2.1.207
fixtures remain historical evidence and are no longer loaded by the active adapter suite.
The late-replay clean-retry regression keeps production's 30-second acceptance bound
compressed to a test-only 50ms: it still expires the first set, but gives a loaded xdist
worker enough event-loop budget for the fake reader to consume replay plus result. This
prevents scheduler load from masquerading as an adapter failure while retaining the
tombstone, no-premature-promotion, and clean-retry assertions.

The test route additionally proves the projection/landing boundary: slow or failed remote observations do not delay local publication; observer results remain exact-contract and freshness-labeled; stale landing rendering is visible but motion-inert; invalid snapshot reads preserve local status; and a failed refresher does not skip serving shutdown. Projector cancellation drains an in-flight thread tick in both its success and late-failure arms; the failure is logged while `CancelledError` remains caller-visible. These are focused regressions; the full repository gate runs above this route.

`test_change_watcher.py` (plus touched `test_serving.py`/
`test_dashboard_daemon.py` fixtures) proves change-driven projection pacing: the derived watch-root
list and self-trigger event filter, the pure `ChangePacer` deadline table (heartbeat/debounce/
interval-floor/max-delay/degraded), heartbeat-only quiet-world projection, debounce-bounded change
latency, burst coalescing, LOUD fixed-interval degrade on missing `watchfiles`/crashed
watcher/failed root derivation (with retry), watch-task lifecycle ownership, exact legacy pacing
without a watcher, `--heartbeat` CLI/daemon argv plumbing, and one real-inotify end-to-end pass.
The adaptive async fixture registers temporary-root cleanup before later projector cleanup, so
unittest's LIFO stack cancels and awaits the projector before deleting its filesystem. This forces
test teardown to respect the same ownership boundary it observes without changing production drain.
The projection scaling suite proves the shared per-tick contract
snapshot: one contract enumeration and at most one parse per contract per projection tick, zero
re-parses while the `(mtime_ns, size, ctime_ns)` stat identity holds, reader-output parity with and
without the injected snapshot, cache retention bounded to live contracts, chmod-000 and
utime-pinned-rewrite invalidation via ctime, and parse failures retried every build.

## Runtime-Truth Regression Gate

Serving coverage spans four exact boundaries: client/build fingerprint and
HTML revalidation; raw-event record realignment and invalid/non-object cursor progression; owned
tmux client environment under contaminated launcher state; and omission of fictitious pre-session
adapter control. Integration coverage skips only when tmux itself is absent.

## Atomic Folded-State Stream Gate

`test_serving.py` now forces both formerly lost state paths. One case publishes while the initial
snapshot generator is suspended but already subscribed and requires the exact next delta. One case
registers before failed-prime recovery, requires one full build-decorated snapshot, proves the
identical state is not duplicated, and then requires an ordinary later delta. A third case cancels a
waiting stream and proves immediate subscriber removal. These are synchronization-driven assertions,
not sleep-based race probabilities.

## Route-Index And Carryover Authority Gate

`test_route_index.py` pins the production census boundary across ignored and generated paths,
tracked/untracked identity, symlinks without target following, sparse checkouts, index/worktree
deletions, gitlinks, all eight ambient Git repository selectors, non-UTF-8 names, and typed Git,
timeout, OS, and `lstat` failures with preserved causes. Regular, linked-worktree, and selector-
contaminated generation must produce identical bytes and a zero-write second pass.

`test_carryover.py` pins official-memory write authority before full apply. JSON and Markdown
settings with missing, invalid, unsupported, reset-to-empty, blank-member, or otherwise
semantically empty path rules must refuse with exact zero mutation. Positive retention,
repopulation, mode/layout selection, root fallback, and official-over-source cases prove the raw
preflight agrees with the typed settings parser rather than creating a second settings language.
`test_worktree_support.py` provisions explicit supported storage authority in initialized-memory
fixtures, while `conftest.py` imports the production selector inventory so tests cannot drift from
the Git boundary they exercise. That import-time strip is fixture safety and stays, but read the
Single-Runner Git Gate below before trusting it as coverage: it also removes the variables a
redirection test needs, so any suite that leans on it can only prove the harness stripped them.

## Dashboard Bundle Placement Gate (260731-EFA-L1)

`test_sync_dashboard.py` no longer tests a sync check. The cockpit bundle left version control
(master decision OQ6), so `scripts/sync-dashboard.py` is a release build step and the suite pins one
property: it cannot place an artifact that was not built from the dashboard source as it stands
right now. Three tests that asserted the opposite — absent `dist` passes, absent fingerprint
sidecar passes, absent `dashboard/src` passes — were replaced by their inversions, two of them
carrying docstrings that name the fail-open they encoded, so the history cannot be readopted by
accident. The `--check` flag's absence is asserted through a real `subprocess`, because the process
boundary is where the old fail-open lived: hooks and CI invoked `--check` and read its exit status.

Fixtures reproduce Vite's handshake rather than mocking it: `emit_bundle` writes a `dist` whose
JavaScript contains the build-input fingerprint verbatim, which is what `vite.config.ts` compiles in
as `__AR_DASHBOARD_BUILD__` and what the script searches for. Nothing in the suite reads the real
tree, and no test requires a frontend build to have happened.

`GeneratedDashboardWhitespacePolicyTests` was **removed** with the committed bundle it policed.
Root `.gitattributes` still disables `blank-at-eol` for
`mcp/src/agents_remember/package_data/dashboard/assets/*.js`, but that path is now git-ignored, so
the rule has no tracked subject and the regression had nothing to prove. The reason it existed
still holds and still forbids post-build normalization — the generated tab is CodeMirror
Python-completion indentation and removing it changes the runtime string — so if a generated path
ever returns to version control, the attribute and this regression return together.

## Static Surface Gate (260731-EFA-L1)

`test_static.py` is the new deterministic owner of both legitimate states of the serving static
surface: a built bundle and an honest absence. It never reads the repository's own bundle, so it
gives the same verdict before and after a frontend build. Its non-obvious assertion is method
parity — for `POST`/`PUT`/`DELETE`/`PATCH` on an `/api` route, the missing-bundle mount and the real
`StaticFiles` mount must return the *same* status (405), because the greedy `/` mount outranks an
API route that matched the path but not the method.

`test_serving.py` keeps the `create_app`-level version of the same two states, but its
build-dependent assertions were rewritten: `/` is served from a patched stand-in bundle rather than
the repository's, `dashboardBuild` is asserted present-or-omitted rather than indexed, and
`StaticTests` skips when this checkout has no build instead of failing.

## Single-Runner Git Gate (260731-EFA-L3)

`test_git_command.py` is the new owner of this package's git boundary, and it is written against a
**decoy repository**. Every redirection test builds a real `real/` and a real `decoy/`, points all
eight selectors (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`,
`GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_PREFIX`) at the decoy
inside a `patch.dict`, and asserts **both** halves — the real branch advanced and the decoy did not
move. Asserting only the real repository would still pass if the write were duplicated into both.

The same suite now pins the runner/facade boundary for malformed Git diagnostics. A real failing
pre-commit hook emits byte `0x81`; `run_git` must retain it through surrogateescape, while the
worktree facade's raised text must render it as a literal escape that UTF-8 JSON serialization can
carry. This keeps non-UTF-8 Git path identity intact without allowing a failed hook to tear down the
MCP transport while reporting its error.

**Those `patch.dict` blocks deliberately undo `conftest.py`.** The conftest strips the selectors at
import, which meant no test anywhere could observe a call site that failed to strip them: the
mitigation for the production hazard was installed in the only place that could have detected it.
`test_a_commit_lands_in_the_real_repository_not_the_decoy` asserts
`set(GIT_REPOSITORY_SELECTOR_ENV).issubset(os.environ)` before it acts, so it passes because
production strips, not because the harness did — delete the conftest lines and it still passes;
delete `env=` from the runner and it fails.

`SingleRunnerTests` is the decay guard and it is `test_subprocess_hygiene.py`'s shape: an AST sweep
over every package module asserting that the only file that spawns git is `kernel/git_command.py`.
Six near-identical runners is exactly how the defect was born, so the rule is that no module may
grow a seventh. **Its reach is stated rather than assumed** — it recognises a spawn whose argv is a
list literal whose head names git, so computed argv is outside that scan. The former benchmark-local builder has been removed: current benchmark operations use `run_git`, `BenchmarkRunnerEnvironmentTests` asserts their real decoy-repository behavior, and `test_single_owner_primitives.py` owns the construction-site guard. That is not a formality: the benchmark runner holds the
most destructive argv in the package (`clone`, `checkout --detach`, `reset --hard`, `clean -fdx`).

**`SingleRunnerGuardReachTests` is the guard on the guard, and it exists because of how this sweep
fails.** `SingleRunnerTests` reports safety as an *empty offender list* — which is also exactly what
it reports when its sweep cannot see the offender, so a hole in the reach does not look like a
failure, it looks like a clean tree. Each test there plants a bypass form and fails if the sweep
stops catching it. Three of those forms were live blind spots the fix workers closed: a spawn
reached through `from subprocess import run` rather than `subprocess.run`
(`test_a_spawn_imported_off_subprocess_is_still_a_spawn`, plus
`test_an_import_alias_is_followed_to_the_name_it_binds`), a path-qualified argv head such as
`/usr/bin/git` (`test_an_absolute_path_to_git_is_git`), and a `**kwargs` splat previously counted as
proof that `env=` had been passed, whose contents the syntax tree cannot see
(`test_a_kwargs_splat_is_not_proof_that_env_was_passed`). It also pins the negatives so the sweep
cannot be "fixed" into over-reporting — a program that merely *starts with* `git` is not git, a
local function named `run` is not a subprocess spawn — and pins the one remaining hole as
deliberate: `test_a_computed_argv_remains_the_documented_blind_spot`, which is the debt
`BenchmarkRunnerEnvironmentTests` pays.

`TimeoutClassTests` pins the *other* half of the consolidation, and it is the half that could have
shipped a regression invisibly. Before the leaf the kernel's runner hard-coded `timeout=5`, so
moving these reads onto a runner whose default is the local bound would have loosened them 60x —
on commands that sit under `resolve_context`, which runs on essentially every tool call. Its
`_recorder` stand-in takes `timeout` as a **required keyword**, so a call site that leaves the class
to the default fails the recorder rather than quietly recording the default.
`test_read_git_facts_bounds_its_three_ref_reads_at_the_metadata_band` and
`test_branch_freshness_classes_each_of_its_commands_by_what_it_does` assert the exact
`{command: bound}` map per module — including that `status --porcelain` and
`rev-list --left-right --count` keep the *local* bound because neither is constant time — and
`test_one_command_means_one_bound_across_the_kernel` asserts the rule itself: `branch
--show-current` and `rev-parse HEAD` are called from both `cross_repo.py` and `git_facts.py`, were
bounded at 30s in one and 300s in the other, and must now agree.
`test_the_metadata_bound_is_the_shortest_of_the_three` keeps the ordering from being reshuffled.

The rest of the module pins the runner contract the consolidation depended on. Stdin is `DEVNULL`
unless `input_text` is passed (`git patch-id` in `memory/carryover.py` is the only caller that needs
it — GitHub #49). A command that deliberately outlives the runner's old hard-coded `timeout=5`
completes, while a caller-named short timeout still raises `TimeoutExpired`, so raising the default
did not amount to removing the bound; `GIT_REMOTE_TIMEOUT_SECONDS < GIT_LOCAL_TIMEOUT_SECONDS` is
asserted rather than assumed. `RemoteBranchStallTests` pins the two remote calls in
`worktrees/modules/cleanup.py` — which previously ran with no timeout at all — reporting
`remote-unreachable` on a stall instead of holding an uncancellable MCP tool call open.
`QualityGateGitTests` covers the gate's own git calls specifically because the gate runs from the
**pre-push hook, where git itself exports `GIT_DIR`**, and keeps both wrappers converting failure
into their typed `DiffScopeError` / `ScopeError` rather than an empty scope that would certify
nothing.

**One consequence when editing an existing suite:** a module that used to spawn git now calls
`run_git`, so a test that patches `subprocess.run` in it patches nothing. `test_serving.py`'s
`BuildInfoTests` was moved onto `agents_remember.serving.build_info.run_git` for exactly that
reason, and its fake now takes `(repo, arguments)` instead of a full argv.

## Cold-Start Gate (260731-EFA-L3)

`test_cold_start.py` proves the server imports and starts with **no network egress**. It is a
subprocess, and both reasons decide whether it can fail at all. tiktoken memoizes loaded encodings
in `tiktoken.registry.ENCODINGS`, so in-process the load under test would be a dictionary hit left
warm by an earlier test in the session, and the assertion would pass against a package that ships no
vocabulary at all. And the caches must be cold: the child gets `TIKTOKEN_CACHE_DIR`,
`DATA_GYM_CACHE_DIR`, `TMPDIR` and `HOME` pointed at one empty directory — pointing the operator
variable at a *cold* directory is deliberate, because it also proves the package's own vendored copy
wins over an exported cache that would send the load back to the network.

The child blocks `socket.connect`, `connect_ex`, `create_connection`, `getaddrinfo` and
`gethostbyname`, then **proves the block took** by attempting one connection before importing
anything — a block that silently did not take would make every later assertion vacuous. It then
builds a real server through `create_server(McpRuntimeConfig(...))` and prints what it counted, and
the parent asserts the child's count equals its own warm counter's count of the same fixed payload:
same tokenizer name (`tiktoken:o200k_base`), same `exact`, same number. A lazy load behind an
approximate fallback would pass the start test and fail that one, which is why the vocabulary is
vendored rather than made optional.

**The module under test is imported through a helper, never at module scope.** `tokens_module()`
returns it per call, so no test in this file can be the one that warms
`tiktoken.registry.ENCODINGS` for the others, and the `mock.patch.object(tokens,
"VENDORED_VOCABULARY_DIR", ...)` redirections below act on a module the file does not hold a stale
reference to.

`VendoredVocabularyTests` re-derives both hashes from the installed tiktoken rather than restating
them — the SHA-1-of-URL filename `read_file_cached` looks up, and the SHA-256 tiktoken asserts on
load — so a tiktoken upgrade that moves the URL, or a truncated copy, fails here instead of quietly
sending the next cold machine back to the network. Since the loader now has to check the digest
*before* tiktoken sees the file, the package holds its own copy of it
(`tokens.VENDORED_VOCABULARY_SHA256`), and `test_the_shipped_file_is_the_one_tiktoken_asks_for`
asserts that copy equals the `expected_hash` recorded off `openai_public.o200k_base()` — which is
what keeps a restated constant from becoming a second source of truth. It also pins that an absent
vocabulary and any encoding this package does not ship raise `TokenizerVocabularyError` rather than
falling through to a download, and that the `TIKTOKEN_CACHE_DIR` override never outlives one load
(the vendored directory sits inside the installed package, which is routinely read-only).

Two further pins in that class earn their place by naming a failure that has no traceback.
`test_the_gitattributes_entry_names_the_shipped_file` asserts the root `.gitattributes` `-text`
entry is *exactly* the shipped filename: the entry is a literal path and the path is `sha1(URL)`, so
a tiktoken release that moves the URL renames the file and leaves the rule protecting nothing —
silently, and only on `core.autocrlf=true` clones, which are precisely the clones that need it.
`test_holding_the_context_open_around_a_counter_does_not_deadlock` covers the obvious use of an
exported context manager, `with vendored_vocabulary_cache(name): TiktokenTokenCounter()`, where the
counter's own load re-enters the manager on the same thread. On a non-reentrant lock held across the
`yield` that is a permanent hang — no timeout, no traceback, a gate that never returns — so the test
runs on a worker with a **bounded join** and asserts the thread finished, in order to *report* a
regression rather than reproduce the hang inside the suite.

`CorruptVendoredVocabularyTests` is the newer half and the one that states the real threat model:
present-but-wrong, not absent. tiktoken does verify the SHA-256, but it does not fail closed —
`read_file_cached` deletes the offending file and downloads a replacement over it, so "tiktoken
checks it" would have meant a corrupt vendored copy becoming a silent network fetch into the
installed package on the startup path. The class docstring records that this was *measured*, not
reasoned: CRLF-mangling the vendored file and truncating it to half its bytes both passed while the
file was quietly restored underneath.

Its shared `assert_corruption_is_refused` helper builds a **copy** of the shipped file in a
temporary directory and points `VENDORED_VOCABULARY_DIR` at that, so a test that fails part-way
cannot leave the checkout damaged and have the suite assert against its own debris. Each case
asserts four things: the refusal is raised; the message names the file, the expected digest and the
found digest (an operator's next move is to compare their copy against the one tiktoken asks for,
and "corrupt" alone does not say against what); and **the copy is still on disk afterwards** —
tiktoken was never handed the directory, so nothing was deleted and nothing was downloaded over it.
The corruptions are the ways bytes actually go wrong: CRLF-mangled
(`test_a_line_ending_mangled_copy_is_refused` — what a `core.autocrlf=true` checkout does, and the
reason the `.gitattributes` entry exists) and truncated to half
(`test_a_truncated_copy_is_refused` — a partial write, whose prefix is byte-identical, so anything
short of hashing the whole file accepts it). `test_a_counter_will_not_build_on_a_corrupt_copy` then
drives the production entry point — `TiktokenTokenCounter()`, the statement that runs while
`mcp/tools/base.py` is importing — over a **single flipped byte**, same length and same line
endings as the original, and patches `tiktoken.load.read_file` with a stub that raises: the refusal
must land before tiktoken reads anything, which is both the assertion and what stops a regression
here from actually downloading 3.6 MB over the corrupt copy.

## Durable Store Integrity Gate (260731-EFA-L5)

Nine files in this route changed for one defect: the six control-plane JSONL stores were losing
appended records. Four suites are new and five existing suites had an assertion replaced. Begin at
`_store_durability.py` — it is the instrument the numbers came from, and it explains why they can
be trusted.

**`_store_durability.py` is support code with no assertion in it, and that is the point.** It
expresses each store as four operations (`open` / `write` / `write_decoy` / `reclaim_now`), where
`reclaim_now` is always that store's own shipped reclaim entry point and never a reimplementation,
and drives three scenarios: `stress`, `forced_lost_update`, `forced_unlink`. It now covers **eight**
stores, not six — the two `providers/` logs have the identical shape and are measured by the
identical instrument — with `CASES` deliberately held at the six control-plane stores beside a
separate `PROVIDER_CASES` so the control-plane contract test is not silently widened. Every record
it writes is one of **three classes**: `survivor-*` (what policy must keep, and the only class the
accounting counts), `decoy-*` (what policy should drop, so a reclaim tick does real work instead of
returning early), and `anchor-keepalive` (never prunable, never counted, present so the kept set
stays non-empty and the tick takes the temp-and-rename path rather than the `unlink` branch). That
is what makes a reported "loss" mean *a row nobody decided to drop* rather than ordinary
bounded-store reclamation. Three properties make its output evidence rather than anecdote:

The dual-version sensitivity path statically imports the current structural `GateState`. Only its
runtime execution against the extracted pre-structural base dynamically loads historical
`models.gates`; other missing modules still fail and no production compatibility module exists.

- **Real processes, never threads** (`multiprocessing` with the `fork` context). The defect is
  cross-process; the GIL would serialise the very window under test.
- **It is dual-mode, and the second mode is what pins a run to one tree.** Importable by pytest,
  and executable as a script whose caller sets `PYTHONPATH` to the `mcp/src` it wants measured —
  the live worktree for the contract assertion, a `git archive` of the leaf's base commit for the
  reproducible baseline. `_require_source_root` refuses with `SystemExit` if `agents_remember`
  resolved anywhere else. A measurement that cannot name the tree it measured is worthless, so
  that guard is fatal rather than a warning.
- **Loss accounting deliberately does not go through the store's own `read`.** A raw tolerant
  JSON-lines reader counts "record lost" and "line torn" as two separate quantities, so a strict
  reader cannot turn a measurement into an exception and a tolerant one cannot report a torn line
  as a lost record. The appenders journal an id only *after* the store call returned, so anything
  on that list and not on disk is a record the store accepted and then lost, and a write that
  raised is counted as an error rather than as a loss.

**The instrument had a defect of its own, and the guard that closed it is the fourth property.**
The harness derived its work directory — including the reclaimer's **stop flag** — from
`root.parent`. `test_controlplane_store_durability.py` passes sibling roots under one `self.tmp`,
so **all cases shared one stop flag**: the first case to finish set it and every case after it left
the tick loop after roughly one tick. Measured directly before the fix: **25 reclaim ticks for the
first store and exactly 1 for each of the other seven, with all eight reporting 0.00% loss**. The
same layout also let the forced scenarios share `forced.id` and the `*.err` files, so a case whose
appender wrote nothing was scored off its predecessor's receipts. The fix is
`harness_work_dir(root) = root.with_name(root.name + "-harness")` — a **sibling**, chosen over a
child because `root` does not name one place: the six control-plane adapters resolve their log
under `root/workspace`, the two provider adapters under `root/logs/observer/providers`, and
`GateStore` additionally globs `root/lifecycles/*/gates.jsonl`, while the accounting reads that
whole tree as raw bytes. The guard is `MIN_SUCCESSFUL_RECLAIMS = 10`, enforced by
`require_stress_measurement` on every stress result and raising `VacuousRunError`; it lives **in
the instrument rather than in either store suite**, so the
control-plane suite, the provider suite and bare `main()` script runs are covered by one floor. The
floor is evidence-based: real runs give 22-39 ticks idle and 34-49 under 24-way CPU load — load
*raises* the count, because appender pacing stretches in wall clock while the reclaimer keeps
polling — so 10 sits an order of magnitude above a vacuous run and under half the lowest of 32
observed runs; 20 was rejected because the observed minimum is 22, which is no margin. The card
[`_store_durability.py.md`](_store_durability.py.md) carries the line-level detail.

**The base-commit numbers are quoted, not reproduced here.** `BASE_COMMIT` is `e52edaf5` and
`STRESS_PROFILE` is 4 appenders × 50 records at 2 ms against 1 reclaimer at 5 ms — both are literals
in `_store_durability.py` and are checkable. The *rates* are not: **no base-commit measurement
artifact is committed anywhere in the tree**, `main` can write a JSON payload but none is stored, no
test asserts a rate, and no committed invocation passes `runs`, so "10 runs per store" is a source
claim too. Two figures are carried at several independent sites and are quoted on that authority:
attention dismissals **31.45%** lost (`durable_store.py`, `supervisor_signals.py`,
`test_durable_store_contract.py`, `test_observer_projection.py`) and gate **11.50%**
(`durable_store.py`, `store.py`, `test_interaction_retention.py`). The rest come from
`durable_store.py`'s module docstring alone: supervisor signals 10.50%, expectation rows 10.20%,
orchestration nudges 9.20%, operator inbox 0.00% (the one store that already took a lock), **127 of
2000** writes *raising*, and "zero torn lines in every run" — the last being the claim that records
disappeared whole, which is what would explain why no reader-side validation could have detected
this.

**Those base-commit rates survived the harness fix, and that is the reassuring half.** Re-measured
through the same `git archive` under the working harness — four runs each, percentage of records
the store reported written and then did not have — the leaf's means are attention **23.91%**, gate
**9.38%**, supervisor-signals **8.00%**, expectation-rows **7.63%**, nudges **7.50%**,
operator-inbox **0.00%**: the documented ordering store for store, with the same lone survivor at
exactly zero. They survived because `main`, the entry point base-commit work runs through, already
built each case a root under its **own** parent, so `root.parent` was distinct there and the stop
flag was never shared. **The bug never corrupted the historical measurements; it hollowed out the
ongoing regression**, which is measured against the live tree and was passing over one tick per
store. Note what those six figures are and are not: they are this leaf's **four-run means and do
not appear in the source**. The source carries the *ranges* they were taken from, in
`test_controlplane_store_durability.py::HarnessSensitivityTests`' class docstring — attention
18.27-30.10, gate 7.50-10.50, supervisor_signal 7.50-9.00, expectation 6.50-9.50, nudge 5.50-9.00,
operator_inbox 0.00 (all four runs) — and each mean falls inside its own range. A reviewer grepping
the harness for `23.91` will find nothing, and that is expected rather than drift.

**Against the current tree, what is asserted is narrower than "all six stores, all three
scenarios"** and is worth reading precisely, because
`test_controlplane_store_durability.py::MultiProcessDurabilityTests` is where a reader checks it.
`lost == 0` (with `stragglers == []`) holds in all three scenarios — over six stores in
`forced_lost_update` and `stress`, and over **five** in `forced_unlink`, which iterates
`APPEND_CASES`. Attention dismissals is excluded there by construction, not by oversight: it has no
`append` at all, so it cannot be stranded in an unlinked inode, and that same whole-file
read-modify-write is why it measured worst. `torn_lines == 0` is asserted in the **`stress` scenario
only**, as are `append_error_count == 0` and `reclaim_error_count == 0` — the latter two in their
own stress run against their own root, with the "the run actually happened" guards repeated so a
zero can never be reported over zero write calls.

The two provider adapters have since landed in the instrument and do **not** widen the counts
above: the registry is split into `CONTROLPLANE_ADAPTERS` and `PROVIDER_ADAPTERS`, `CASES` stays at
the six control-plane stores beside a separate `PROVIDER_CASES`, and `APPEND_CASES` still derives
from `CASES`. The counts above are anchored on those names; verify the names, not the numerals.

`test_controlplane_store_durability.py` turns that into three assertions — no loss (R10), the
per-store torn-line policy (R8, derived from named call sites rather than from docstrings), and
sensitivity proven against the base-commit archive (R14, asserting both that the five unlocked
stores each lose a record *and* that operator-inbox loses none, which is what proves the harness
is measuring the defect). Loss and raising are asserted separately on purpose: a store that starts
raising instead of losing has moved the failure, not fixed it. R14 has a second half in
`test_durability_measurement.py::DurabilityMeasurementTests`: it refuses zero writes, reports all
write/compaction/process shortfalls together, distinguishes failed attempts from successful
compactions, and returns a complete result unchanged. That focused suite proves the shared
instrument refusal is real and reachable rather than a constant nobody consults.

`test_provider_store_durability.py` is the same three assertions over the two `providers/` stores,
and is a **fifth** new file in this gate that the "nine files / four new suites" count above
predates. Read it for one thing the control-plane suite cannot show: its `case_root` docstring is
where the shared-stop-flag defect was first found and worked around locally, before the fix moved
into the instrument where it also covered the control-plane suite, which had the same layout and no
workaround.

`test_gate_replay_window.py` states what the loss cost. **The entire defence against spending one
human approval twice is a single appended record**: `_mark_closeout_gate_applied` appends
`apply_gate`, and `enforcement.py`'s `applied` branch refuses. No flag, no marker file, no
timestamp comparison. The counterfactual test deletes *only* that line — asserting the two
remaining snapshots survive, so the deletion cannot have been indiscriminate — and the same
approval becomes spendable again. Against the pristine base commit the suite exits 1 with
`AssertionError: 'approved' != 'applied'`; against the fixed tree it exits 0.

`test_durable_store_contract.py` is the in-process axis the multiprocess harness cannot see: two
**threads** of one process, which is what the dashboard is. **Read what it claims about the mutex
before repeating it.** `flock` already excludes two threads of one process — the lock lives on the
open file description and `exclusive_access` opens a fresh one per non-reentrant acquisition — and
that was measured, not assumed, so the thread-level lost update was already closed and
`thread_mutex_for` **is not fixing a reproducible race**. What it closes is that the exclusion
rested on *where the handle came from*: cache one lockfile handle on the store — the obvious fix
for an append path that opens two files per record — and every thread shares one description,
`flock` silently stops excluding, and nothing in the tree fails. The mutex makes the in-process
half a stated property, and the first test asserts it directly via a non-holding thread's
`acquire(blocking=False)` probe rather than inferring it from an ordering `flock` alone would
produce. The re-entrancy case follows: that mutex is a second lock a thread can hang itself on.
Its unsafe-filesystem tests **fake the filesystem, not the code** — a stand-in whose `flock` is
accepted and takes no lock, exactly as WSL DrvFs behaves, substituted for `durable_store`'s own
module reference alone so no other thread in the interpreter loses its locks; every assertion is
on the raised type, the message text, and what is on disk, including that no log was created.

**The five updated suites all had an assertion that a pruned log stops existing.** That unlink is
the defect L5 removed: `_replace` called `path.unlink(missing_ok=True)` on an empty kept set, so a
concurrent appender holding an `"a"`-mode handle wrote into an inode with no remaining links.
Four of them now assert **emptiness** — `is_file()` true, `read_bytes() == b""` — which is
strictly stronger, because zero bytes proves the records physically left where a missing file only
proved a file was removed.

`test_interaction_retention.py` is the exception and is worth reading as one. Its assertion was
never about absence: it passed only because the base commit physically rewrote every gate log **on
the projection tick**, which is the behaviour this leaf removed. Restating it as emptiness would
have restated the removed behaviour. It was split into two proven claims instead — the projection
leaves the log byte-identical (non-destructiveness, newly asserted and never held anywhere before)
and `GateStore.compact`, in the owning process, is what empties it.

## Hot Path Summary

L2 forcing covers every configured-contract semantic refusal across public consumers, exact admitted-object reuse, task-addressed controls, crash cuts, locator/manifest/journal contradictions, worker termination, direct landing, bounded legacy repair, task publication races, and fail-closed cleanup.

The harness sub-agent regression set: `_agent_wire_fixtures.py` (shared
codex vendored-shape builders), `test_codex_adapter_thread_demux.py` (the 2026-07-24
bridge-death incident regression — three sub-agents mid-turn, multiplexed approvals answered by
request-id, collab identity binding, degrade-not-die, native-page thread demux — plus the
remediation pins: concurrent parent pendings answered per id with the oldest in the singular
slot, the method-first degrade split, the bounded per-thread pending map, and the load-shed
event queue with its honest `ar/load-shed` notice),
`test_conversation_projector_codex_agents.py` (roster/multiplexed projection/per-thread twin-suppression
dedupe/plural pendings in one cursor domain, incl. concurrent-parent projection and the
singular-rotation resolution), `test_conversation_projector_claude_agents.py`
(`parent_tool_use_id` sidechain binding, `task_*` roster lifecycle, the fail-closed
`--forward-subagent-text` floor), and `test_conversation_library_agents.py` (both harnesses'
agent grouping with visible `agents_note` degrade and nested-agent naming). Authority-level
multiplexed respond + plural-pending serialization round-trips extend `test_harness_control.py`
(incl. the entry-thread operation guard for concurrent parent tuple entries);
the flag-floor probe/relaunch flow extends `test_harness_control_claude.py`; the reordered
`task_started` binder pin extends `test_conversation_active_service.py`; the additive agent
fetch at the fake boundary extends `test_conversation_library_ports.py`.

For the dashboard release path, begin at `test_sync_dashboard.py` for the placement refusals and
the process-boundary proof that `--check` is gone, then `test_static.py` for what a checkout with
no bundle serves. Use `dashboard/vite.config.ts` for the compiled fingerprint the fixtures embed
and `.github/workflows/publish-mcp-to-pypi.yml` for the only production caller. Do not route this
seam through generated asset file cards or a generic normalizer, and do not expect a committed
bundle to compare against.

For repository gate ownership, begin at `test_code_quality_check.py`: it proves the accepting
wrapper lives only behind Dagger, the host hook tiers are non-test (`pre-commit` → `fast`,
`pre-push` → `targeted`, manual `full` refuses), and the pull-request-only GitHub workflow invokes
the deterministic hook rather than a second Dagger/pytest rail. Since 260731-EFA-L2 the same module also holds the gate's honesty
contracts: `RadonIsAReportNotAGateTests` (exactly the two Radon steps are declared reports; the
section header and the help text say so; a report step that exits non-zero still fails, because a
tool that exits 0 on every finding can only exit non-zero when broken),
`EveryEnforcingStepCanFailTests` (the `ruff` step routes **no** rule away from itself; `C901`,
`PLR0911`, `PLR0912` and `PLR0915` are selected, unignored and proven to reject a real over-complex
function at this repository's configuration; the format step is enforcing over the derived scope;
and `test_the_complexity_baseline_and_its_gate_step_are_gone` keeps the deleted ratchet deleted),
`test_code_quality_tool_signature_exemption.py::ToolSignatureExemptionTests` (`PLR0913`'s one exemption covers the MCP registration directory and
nothing else — an AST walk over every file the `pyproject.toml` pattern really resolves to proves
each function there is a published `@server.tool()` declaration or its registrar),
`CrapThresholdEnforcementTests` (every offender named, the clearing branch coverage inverted from
the CRAP formula, "split it" when no coverage can clear it, and no exemption file anywhere),
`test_code_quality_check_scope.py::GateScopeDerivationTests` (no hand-written scope constant may return; `git ls-files` reads the
index; a file in no importable package still reaches both rails; an underivable scope refuses
rather than certifying nothing; `main` reports the gate's verdict rather than owning one), and
`test_code_quality_check_scope.py::PytestConfigurationTests` (strictness switches, `python_classes`, an **exact-count** cap of 3 on
`filterwarnings` ignores, and two-way reconciliation between registered markers and the suite's
real `AR_*` environment gates).

**For "does the gate reach everything?", begin at `test_gate_scope.py`** — it is a different kind of
test from the above. It does not read the wrapper's dataclasses; it recomputes `git ls-files`
itself, builds the real `ruff` and `pyright` argument vectors, and asserts every tracked path
appears in them, because a scope that is declared but not passed to a tool is not a scope. It also
reads the frontend rails (`eslint.config.*` directories and `tsconfig*.json` includes, with a
hand-written glob translator because `fnmatch`'s `*` crosses `/` and would silently widen every
pattern). **It has no allowlists.** Three empty ones stood there mid-leaf and were deleted with the
complexity baseline they were shaped like; every population they were built for was brought onto a
rail instead (`.pi/extensions/tsconfig.json` for the Pi extension, `tsconfig.driver.json` for the
Playwright/perf layer, `panda.config.ts` into `tsconfig.node.json`). All four failure messages say
so: "There is no allowlist to record it in."

**For the changed-lines coverage floor, begin at `test_diff_coverage.py`** — the 100% per-diff floor
this leaf added, where every statement and branch arc on a changed line must be exercised and the
failure names each uncovered line rather than reporting a percentage. Every test drives a **real
throwaway git repository**: a fake `git diff` string would only prove the parser agrees with whoever
wrote the fixture, not with git's hunk headers for an added file, a one-line deletion, a rename, or
a working-tree-only change.

**For "is any gated path actually reachable?", begin at `test_gated_integration_runner.py`.** Eight
`AR_*` markers were registered and reconciled with the suite's skip decorators while **nothing
applied or ran any of them** — a registered marker that decorates nothing selects zero tests, and
pytest reports that as a successful run of an empty selection. This module reconciles registered
markers, applied markers and `scripts/run-gated-integration.py` entries in both directions. It also
proves no GitHub workflow invokes that pytest runner outside the Dagger attestation boundary.

**For the generated harness trees, begin at `test_sync_harness.py`.** Its first test is the
enforcing one: any drift — content **or** file mode — between `scripts/harness/` and the nine
generated trees fails the suite, so drift is caught for a contributor who has not installed the
hooks and in CI. Note the `sys.modules` registration in `load_script`: the generator defines
frozen dataclasses, which resolve their defining module through `sys.modules` at class-creation
time, so a path-imported script must be registered before `exec_module`.

**There is no complexity ratchet.** `test_complexity_baseline.py`,
`code_quality/complexity_baseline.py`, `quality/complexity-baseline.txt` and the wrapper's baseline
step were all built during 260731-EFA-L2 and then **deleted** when the developer ruled that
ratchets, baselines, grandfather lists and burn-down schedules are all forbidden. All 67 complexity
offenders were fixed by extraction instead, and 274 of 293 long signatures were fixed by
introducing 163 parameter objects. Do not reintroduce any of them —
`test_code_quality_check.py::EveryEnforcingStepCanFailTests::test_the_complexity_baseline_and_its_gate_step_are_gone`
fails if you do.

For closeout enforcement, begin at
`test_worktree_closeout_quality_gate.py`, whose argument spy is the only thing standing between the
mandatory gate and a silent no-op at an unannotated call site.

For route-overview refresh planning, `test_worktree_and_observer_helpers.py`
proves both sides of the verified-memory-baseline seam: a substantively
task-edited overview is required even when the current leaf code range is
unrelated and is stamped with the supplied verified commit during refresh,
while a metadata-only edit is still classified stale. A third case
permits only a generated final reference-cell citation-coordinate shift without
invented history; the claim, anchor, path, and table shape stay fixed. This
prevents older synced-source drift and sanctioned citation repair from
deadlocking closeout without weakening the authored body/history gate.

For route-index/carryover authority changes, begin with `test_route_index.py` for the frozen census
and byte-convergence matrix, then `test_carryover.py` for full-apply zero-mutation refusals and
parser-equivalent positive controls. Use `test_worktree_support.py` for closeout caller wiring.

For folded-state transport changes, begin at `test_serving.py::StreamEventsTests`: those
cases pin atomic activation, first-recovery snapshot semantics, later-delta continuity, and
close/cancellation cleanup against the production `Projector` and `stream_events` seam.

`test_cursor_bindings_preserve_authorization_identity_scope_and_purpose` carries semantic authority and
`test_conversation_foundation.py` the package/router/helper/fixture topology. The three
`fixtures/conversation_runtime/*.json` files are allow-listed installed observations with
`enablesCapabilities:false`; exact versions and observed counts are evidence, never maintained
feature declarations. Helper protocol behavior is also covered in its own Node test package.

The active-serving set centers four focused suites: `test_conversation_active_status.py` (canonical
classification, revision discipline, full-product orchestration parity),
`test_conversation_active_projectors.py` (per-harness mapper identity/blocks/tools/provenance),
`test_conversation_active_service.py` (engine hydration/ordering/idempotence plus the landed
review-fix pins), and `test_conversation_active_api.py` (production routes over a real socket, incl.
selected-child hydration, the live epoch-flip gap, and the no-PTY source scan). The foundation pin
asserts the active child's exact three routes; fixture rows stay evidence-not-enablement.

The library set centers six focused suites: `test_conversation_library_api.py` (real-ASGI routes
and the O4 status ladder), `test_conversation_library_cursor.py` (signed token and scope
contracts), `test_conversation_library_gates.py` (capability demotion rules),
`test_conversation_library_ports.py` (hostile normalization), `test_conversation_library_open.py`
(idempotent exact open arms), and `test_conversation_library_installed.py` (opt-in live gates and
both real opens). The foundation pin asserts the library child's exact five routes and the
four-file helper source set; fixture rows stay evidence-not-enablement.

The control set centers four focused suites plus a shared topology and an installed proof:
`_control_plane.py` (the real bridge/IPC/authority/composition seam with only the harness adapter doubled and
the `NOW`-anchored control service), `test_conversation_control_operations.py` (interrupt ledger,
Finding 1/Finding 2 pi settlement regressions), `test_conversation_control_queue.py` (never-bodies
queue truth, withdrawal race, bounded recovery lease + frozen-clock expiry, forgery battery),
`test_conversation_control_attachments.py` (limit refusals, one-use submit, recoverable-lease rebind,
policy/telemetry), and `test_conversation_control_api.py` (the seventeen routes over a real uvicorn
wire, O4 mapping, no-paste source scan), with `test_conversation_control_installed.py` the opt-in
version-locked live proof. The foundation pin asserts the control child's exact seventeen routes;
fixture rows stay evidence-not-enablement.

`test_conversation_runtime_composition.py` and
`test_conversation_authorization.py` cover the runtime composition repair: single install-once
binding at both composition seams, duplicate/missing/foreign/missing-member fail-closed shapes,
per-app child isolation over real HTTP, no import-time singleton, no production identity-injection
or fixture/PTY/browser-identity reliance, server-resolved local-operator identity, loopback-only
resolution, and cross-principal rejection in both directions through an injected seam double.

`test_harness_control_evidence.py` covers the native evidence and resume
substrate: per-harness reserved-key round-trips with the no-leak guarantee across `snapshot.raw`,
projected `control_raw`, and subscriber snapshots; unknown-vendor pass-through; buffer bounds and
clip visibility at two sizes; native-page continuation without overlap/gap, null-terminated, with
typed cross-domain rejection and epoch-mismatch detection; the provenance matrix through the sole
queue delegation; and the codex resume channel end-to-end with pre-spawn refusals.
`test_harness_control_evidence_installed.py` captures the same seam against installed runtimes
(opt-in, version-locked) into redacted `substrate-evidence/*` fixture rows, keeping the
version-mismatched Claude row honestly `not-exercised` and `enablesCapabilities` false everywhere.

`test_harness_control_evidence.py` also carries the evidence-truncation settlement
coverage: `ClipHelperTests` gains three byte-level clip terminal-identity preservation tests (a
clipped pi `message_end` keeps only `type` + `message.stopReason`; a clipped codex `turn/completed`
keeps only `turn.id` + `turn.status`; absent identity is never invented) plus a giant-scalar
drop-whole regression with a 256/257 boundary check, and the new
`EvidenceTruncationSettlementIpcTests` drives oversized (>32 KiB) production pi/codex terminal frames
end-to-end through the real bridge clip and the real `read_control_evidence` IPC surface, asserting
the preserved enums survive to scan helpers that mirror the control child's `_pi_stop_reason` /
`_codex_terminal_outcome` reads verbatim (the acceptance proxy for `probe_l3_delta.py`).

`test_harness_control_plane.py` centers the control-plane contract suite:
the interrupt batteries (bridge epoch guard, codex exact-turn, pi expected-operation guard,
successor zero-write refusal, content-less `message_end` honesty), the timeline batteries
(all-sources/kinds union, eviction floor, the 256-record budget edge), the asset batteries
(schema/traversal/verification/construction/digest/unsupported), the recovery battery, and the
client validation battery. `test_harness_control_plane_installed.py` captures the same seams live
against pinned codex 0.144.5 and pi 0.80.7 (opt-in, version-locked) into redacted
`control-plane/*` fixture rows, with the Claude version-honesty test keeping those rows
`not-exercised` and `enablesCapabilities` false everywhere.

`test_harness_submission_authority.py` centers the authority matrix: slow-adapter responsiveness,
dispatch/withdraw races, early terminal completion, full-ref id reuse, ordering, idempotency/source-
payload conflicts, certified pre-dispatch retry, impossible safe retry after possible bytes, epoch
mismatch, privacy, and retention. `test_harness_control.py` extends the same timeline across IPC,
outer response loss, durable sources, reconcile, and raw-free projection. API tests pin 64-id
status/withdraw and typed 409/503 mapping. Claude/Codex/Pi suites each prove their guarded write and
exact completion semantics; Codex/Pi live smokes remain opt-in installation evidence, not generic
authority.

Live-conformance and Claude discovery-isolation regressions complete the capability-gate coverage. Claude
fake-transport cases cover separate variadic/repeated and equals-attached MCP selectors, the `--`
suffix boundary, exactly one strict empty discovery config, and byte-preserved normal startup. The
explicit-opt-in Codex live case performs dynamic initialize/model-list discovery without a thread or
token event, validates a settings-shaped launch pair, then spends exactly two bounded turns to prove
queued model/effort promotion and subsequent-turn retention on the same PID/thread. Its recorder
retains only method, selection, thread, version, timing, and numeric token-usage evidence; ordinary
suites skip the token-spending case. Captured versions, catalog rows, and counts remain live evidence
rather than production constants.

The frozen daemon consumer boundary and its production races are pinned. Capability
catalog cases prove token-free current-environment discovery, install fingerprint invalidation,
bounded single-flight retention, failed-refresh quarantine/recovery, and protection of a later
concurrent success. API/client/IPC/queue cases prove strict normalized advertise/set parsing,
first-byte ambiguity without blind retry, whole UTF-8 multiline submit, pending and retained
request-id idempotency, retained-known reconciliation without native resend, raw-free public
serialization, and liveness-first 404/409 classification. Opener/app cases prove complete-pair
pre-spawn validation, same-pair live reopen, changed launch conflict with actual retained truth,
fresh dead replacement, and a concurrent different-pair race on two threads that must retain one process and one catalog truth (`test_terminal_opener.py:678-737`). The damaged predecessor text did not preserve its full cross-process claim, so no cross-process proof is inferred here.

### Current Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| The quality runner requires explicit repository profile authority, distinguishes enforced/no-code preview, refuses missing authority, and the closeout suite spies on the real passed gate target. | `CodeQualityGateTests`; `CloseoutCodeQualityGateTests` | mcp/tests/test_worktree_quality_gate_runner.py:15-473; mcp/tests/test_worktree_closeout_quality_gate.py:55-257 |
| The gate is shown the commit content: a created file reaches ruff through real `derive_scope`, a deleted one leaves it, and the lint-path set equals the Python paths in the resulting commit tree. | `CloseoutGateSeesCreatedFilesTests` | mcp/tests/test_worktree_closeout_gate_scope.py:130-208 |
| Both staging refusals are asserted as damage that does not happen: the repository checkout preserves its `add -p` selection and untracked secret, and a conflicted worktree keeps `MERGE_HEAD` intact. | `TaskWorktreePreconditionTests`; `ConflictedIndexTests` | mcp/tests/test_worktree_closeout_quality_gate.py:974-1084; mcp/tests/test_worktree_closeout_quality_gate.py:1087-1139 |
| A retry commits the tree a first run would: two worktrees driven to the same end state, one through a refused gate, are asserted to produce the identical commit tree, so the ignored `.dmypy.json` a refused attempt staged is not carried into the retry (`RetryStagesWhatAFirstRunWouldTests`). | `RetryStagesWhatAFirstRunWouldTests` | mcp/tests/test_worktree_closeout_quality_gate.py:1145-1199 |
| The whole HTTP surface is driven and validated against the model declared for the returned status, alias-strict, with the inventory, walker coverage, two runtime-validated dict routes, and the exact 292-declared / 139-driven / 153-listed ledger. | `_grouped`; `_driven_pairs`; "class DeclaredSurfaceCoverageTests(unittest.TestCase):" | mcp/tests/test_serving_response_conformance_live.py:449-453; mcp/tests/test_serving_response_conformance_live.py:466-489; mcp/tests/test_serving_response_conformance_live.py:492-549 |
| `/api/state` and the SSE snapshot validate as `ServedWorkspaceProjection` and refuse `WorkspaceProjection`; 304 is bodyless, deltas omit `SERVED_TAIL_FIELDS`, and the populated-projection guard rejects an empty scaffold. | `ServedStateTailTests`; `ServedStateRouteConformanceTests`; `ServedSnapshotConformanceTests` | mcp/tests/test_served_state_conformance.py:213-257; mcp/tests/test_served_state_conformance.py:260-352; mcp/tests/test_served_state_conformance.py:355-410 |
| Every producible vocabulary member validates at its wire field by three mechanisms; the module header states which vocabulary each mechanism defends. | "class GuidanceWalkTests(unittest.TestCase):"; "class ProducedLiteralTests(unittest.TestCase):"; "class AdvertisedVocabularyTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness.py:230-307; mcp/tests/test_wire_vocabulary_exhaustiveness.py:646-835; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:49-118 |
| The reader tolerates an unclassifiable contract cell by degrading and naming it while the writer refuses it, and every refusal names the contract file it was reading (`ContractBoundaryTests`). | "class ContractBoundaryTests(unittest.TestCase):" | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:159-513 |
| Tool-response conformance captures `nextStep` and `supervisorBanner` where both envelope additions fire, then validates representative payloads against their registered models. | `ToolResponseConformanceTests`; `test_the_choke_point_injections_are_actually_exercised` | mcp/tests/test_tool_response_conformance.py:1001-1136; mcp/tests/test_tool_response_conformance.py:1031-1048 |
| Next-step regressions require advertised token counts to cover the served payload including `nextStep` and `supervisorBanner`. | `test_advertised_token_count_covers_the_attached_next_step`; `test_advertised_token_count_covers_the_agent_notifier_banner` | mcp/tests/test_next_step.py:305-317; mcp/tests/test_next_step.py:319-331 |
| The lifecycle state vocabulary is partitioned live and terminal with both halves total and disjoint, every live state counted, and terminality held to the reducer that produces it. | `MetricsBucketVocabularyTests`; `StatePartitionTests`; `TerminalityIsStructuralTests` | mcp/tests/test_observer_projection_metrics.py:128-233; mcp/tests/test_observer_projection_metrics.py:236-300; mcp/tests/test_observer_projection_metrics.py:303-420 |
| The live boundary suite proves unknown contract cells degrade with the raw token retained and disappear after a canonical rewrite. | `test_an_unknown_cleanup_cell_degrades_and_names_itself`; `test_an_unreadable_memory_mode_degrades_to_the_topology_on_disk`; `test_a_rewrite_heals_the_file_and_that_is_the_recovery_path` | mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:249-314 |
| A decoy repository named by all eight selectors receives none of the real repository writes or reads, an AST sweep asserts `kernel/git_command.py` is the only git-spawning module, and the benchmark runner argv including `reset --hard` is asserted directly. | `DecoyRepositoryTests`; `SingleRunnerTests`; `BenchmarkRunnerEnvironmentTests` | mcp/tests/test_git_command.py:168-224; mcp/tests/test_git_command.py:510-582; mcp/tests/test_git_command.py:780-908 |
| The sweep reach is planted and asserted for subprocess aliases, a path-qualified git argv head, a `kwargs` splat that is not proof of `env`, and per-command timeout bands. | `SingleRunnerGuardReachTests`; `TimeoutClassTests` | mcp/tests/test_git_command.py:585-664; mcp/tests/test_git_command.py:667-777 |
| The runner scrubs repository selectors on every call, uses `input_text` for git patch-id and DEVNULL otherwise, and carries the local, remote, and metadata timeout constants. | `GIT_REPOSITORY_SELECTOR_ENV`; `GIT_LOCAL_TIMEOUT_SECONDS`; `GIT_REMOTE_TIMEOUT_SECONDS`; `GIT_METADATA_TIMEOUT_SECONDS`; `git_environment`; `run_git` | mcp/src/agents_remember/kernel/git_command.py:34-43; mcp/src/agents_remember/kernel/git_command.py:71-74; mcp/src/agents_remember/kernel/git_command.py:94-100; mcp/src/agents_remember/kernel/git_command.py:103-154 |
| A cold-cache child process with blocked sockets starts the real server and matches the warm parent count; the shipped vocabulary name and bytes are re-derived and the filename pin and re-entrant-load guard are covered. | `ColdStartTests`; `VendoredVocabularyTests` | mcp/tests/test_cold_start.py:199-218; mcp/tests/test_cold_start.py:221-331 |
| A present but incorrect vendored vocabulary is refused and left on disk across CRLF, truncation, and flipped-byte cases. | `CorruptVendoredVocabularyTests` | mcp/tests/test_cold_start.py:334-417 |
| The measurement instrument uses eight store adapters, three forked scenarios, raw on-disk loss accounting, and a dual-mode script path guarded by `_require_source_root`. | `StoreAdapter`; `ADAPTERS`; `SCENARIOS`; `surviving_ids`; `run_case`; `_require_source_root` | mcp/tests/_store_durability.py:137-194; mcp/tests/_store_durability.py:576-596; mcp/tests/_store_durability.py:1086-1090; mcp/tests/_store_durability.py:605-630; mcp/tests/_store_durability.py:1105-1109; mcp/tests/_store_durability.py:1118-1125 |
| `harness_work_dir` derives each run bookkeeping directory as a sibling named from that run root, preventing sibling cases from sharing stop or error files. | `harness_work_dir` | mcp/tests/_store_durability.py:875-902 |
| The shared non-vacuity gate refuses incomplete durability results or runs below `MIN_SUCCESSFUL_RECLAIMS` by raising `VacuousRunError`. | `MIN_SUCCESSFUL_RECLAIMS`; `VacuousRunError`; `require_stress_measurement` | mcp/tests/_durability_measurement.py:11-11; mcp/tests/_durability_measurement.py:14-15; mcp/tests/_durability_measurement.py:18-55 |
| No record reported written is missing afterwards for the six record types; loss and raising are asserted separately, torn-line policy is held per consumer class, and the harness detects the defect against a git archive of the base commit. | `MultiProcessDurabilityTests`; `TornLinePolicyTests`; `HarnessSensitivityTests` | mcp/tests/test_controlplane_store_durability.py:125-211; mcp/tests/test_controlplane_store_durability.py:214-343; mcp/tests/test_controlplane_store_durability.py:346-401 |
| The provider durability suite is the second consumer covered by the instrument tick floor; its `case_root` docstring records the shared-stop-flag defect and source fix. | `ProviderStoreDurabilityTests`; `case_root` | mcp/tests/test_provider_store_durability.py:262-277; mcp/tests/test_provider_store_durability.py:280-351 |
| One human approval is consumable exactly once, and the counterfactual proves the defence is one appended record. | `GateReplayWindowTests`; `test_the_applied_record_is_the_only_thing_closing_the_window` | mcp/tests/test_gate_replay_window.py:176-324 |
| The in-process axis covers the mutex, re-entrancy across both locks, unsafe-filesystem refusal, schema major/minor policy, and failed-rewrite temp cleanup. | `InProcessExclusivityTests`; `UnsafeLockFilesystemTests`; `SchemaVersionMajorTests`; `FailedRewriteTests` | mcp/tests/test_durable_store_contract.py:165-363; mcp/tests/test_durable_store_contract.py:366-429; mcp/tests/test_durable_store_contract.py:432-518; mcp/tests/test_durable_store_contract.py:648-726 |
| The contract the four suites are named after: what prevents loss (the unconditional lock) stated apart from what merely documents (advisory ownership), the rewrite that never unlinks, and the record validator that gives both read policies their behaviour with no version branch in either. | `exclusive_access`; `rewrite_lines`; `require_lock_held`; `thread_mutex_for`; `DurableRecord` | mcp/src/agents_remember/controlplane/durable_store.py:319-360; mcp/src/agents_remember/controlplane/durable_store.py:421-428; mcp/src/agents_remember/controlplane/durable_store.py:363-381; mcp/src/agents_remember/kernel/file_lock.py:41-55; mcp/src/agents_remember/controlplane/durable_store.py:256-279 |
| The projection tick this leaf stopped rewriting on — the reclaim pass that ran in a process owning nothing here, and the source of the measured gate-log loss. | "def read_gates(coordination_root: Path" | mcp/src/agents_remember/serving/projections/snapshots_impl/_runtime.py:107-141 |
| Interaction retention separates projection non-mutating reads from owner-side compaction, and owner compaction leaves an empty named log. | `test_an_open_gate_past_24h_leaves_the_projection_then_leaves_the_log` | mcp/tests/test_interaction_retention.py:31-76 |
| Projection-side attention acknowledgement pruning leaves an empty file rather than unlinking the log. | `test_project_and_write_prunes_completed_lifecycle_attention_acknowledgement` | mcp/tests/test_observer_projection_snapshot.py:556-590 |
| GateStore compaction that removes the last gate leaves an empty workspace log rather than unlinking it. | `test_pruning_the_last_gate_empties_the_workspace_log_without_unlinking_it` | mcp/tests/test_packaged_assets_and_context_values.py:419-444 |
| Serving attention-store pruning requires zero rows and zero bytes while retaining the log path. | `test_attention_store_upserts_and_prunes_lifecycle_rows` | mcp/tests/test_serving_actions.py:355-388 |
| The worktree contract's front matter read under the same major/minor rule as the JSONL records, through the same helper, so the two version policies cannot drift. | `ContractSchemaVersionTests` | mcp/tests/test_worktree_contract_lifecycle.py:84-145 |
### Route Contract Review

The route remains governed by the shared hosted protocol bridge: exact adapter snapshots provide
readiness and liveness, correlated receipts sit beneath durable inbox rows, interactions use durable
gates, legacy/custom sessions are explicit unsupported states, and pane/log signals are diagnostic
only. Dashboard and packaged projections remain additive and synchronized.

## Harness Sub-Agent Regression Route Impact

Harness sub-agents are first-class in test coverage: one shared codex
vendored-shape fixture module plus five focused suites prove the thread demux (the 2026-07-24
production bridge-death incident class), both projectors' agent grammar (roster, multiplexed
pendings, per-thread twin suppression, sidechain binding, the claude flag floor), and both
libraries' agent grouping with visible degrade notes. Four existing suites gain targeted
extensions (plural-pending authority + serialization, flag-floor probe/relaunch, the reordered
binder pin, the additive fake-boundary agent fetch). Native-helper sub-agent enumeration and the
agent transcript read are covered at the Python port boundary in
`test_conversation_library_agents.py`; the helper's own Node suite is unchanged.
The remediation adds twelve pins: nine in the demux suite (concurrent parent server requests
answered per id with the oldest in the singular slot, the method-first degrade split —
experimental/unknown METHODS decline + degrade on the parent while known-method malformed shapes
and boolean rpc ids still fail loud, the bounded pending map declining only the newest request,
and the load-shed queue's delta-shed/consumer-mint/notice-before-sentinel ordering), two in the
codex-agents projector suite (concurrent-parent projection with plain parent entries, the
singular-rotation resolution semantics), and one in `test_harness_control.py` (the entry-thread
operation guard for concurrent parent tuple entries); the legacy experimental-request case in
`test_codex_app_server_adapter.py` flips to decline-not-fail with the decline itself unchanged.
The original entry retained pre-commit metadata; the current document stamp records the separate L31 cumulative source review.

## Codex Native-History And Projection-Containment Regression Route Impact

`test_codex_native_history.py` pins items-first/turns-second runtime probing, exact `-32601`-only
legacy entry, 16 MiB complete source-response refusal, 64 MiB/64-walk one-shot continuation,
linear once-only source reads, cycle/repeated-id termination, aggregate legacy bounds, eviction
without refetch, and typed IPC survival. `test_codex_history_production_path.py` composes the exact
4,846,576-byte response through stdio, installed-shaped items `-32601` then turns/full success,
adapter, Unix IPC, and selected-child projection; its cyclic second-wave child fails locally while
parent and sibling remain live.

The protocol suite owns increasing below-fuse sizes, exact 128 MiB payload-plus-newline acceptance,
one-byte-over refusal, and shared-fatal above-fuse evidence. Projector/API/browser suites own
selected-child-only hydration, unlocked child I/O, same-child singleflight, necessary 64-entry
capacity bounds, valid persisted-focus one-shot hydration, stale-focus non-hydration, and visible
retry/recovery without parent stream failure. The dormant library full-read path is not covered as
repaired and remains a named follow-up.

## Serving Performance And Quality-Gate Route Impact

The regression set covers the serving performance/truth changes (single-pass repository discovery, projection-body reuse, gzip/SSE separation), opt-in heap diagnostics, landing-final reopen safety, structured multi-question interaction responses, native interrupt correlation, active page/event bootstrap recovery, and terminal startup/liveness boundaries. The final focused additions prove mandatory default CRAP failure and wrapper parity, fail-closed closeout with zero mutation on quality failure and quality-before-commit on success, updated public tool descriptions, and Claude mutation parsing through public projector paths for valid and malformed vendor inputs. These tests are split across the existing focused suites; no new test route is introduced. The original entry retained pre-commit metadata; the current stamp records the separate L31 cumulative source review.

## 260731-EFA-L16 Route Impact — cross-store lock-order forcing tests

`test_cross_store_lock_order.py` pins the 2026-08-05 ABBA repair against the daemon's real
sharing shape (ONE catalog + ONE inbox log per process): a placement property proving the
hosted-interaction synchronizer's inbox/gate locks are never taken under the catalog batch —
driven on the full sweep AND the starting fast path, with the legacy inline direct-observe path
pinned beside it; a rendezvous-parked reproduction running the real liveness sweep and
supervisor sweep on threads, which deadlocks by timeout on the pre-fix tree ("the ABBA is
live") and passes on the fix, on daemon threads so the proof cannot hang the suite; and
thread-identity proofs that control/active resolution and the terminal-image handler run their
blocking reads on worker threads, never the event loop. Every test asserts the synchronizer
actually ran — no vacuity. The closeout citation-gate tests joined them: a changed construct
completes with the stamp advanced to the new code commit, and a deleted construct refuses in
the citation gate BEFORE the code commit with no commit spent.

## 260731-EFA-L7 — Test-Tree Remediation And New Suites

All 27 over-limit test modules were split in place into families (79 new modules; every original `test_*` name reconciled item for item, plus one intentional new name for R17). New suites added: `test_file_size_detector.py` (the File Size Budget rail — bands, exit codes, wiring, scope), `test_facade_surface.py` (the eight-facade surface pin), and the harness-control conformance family `test_harness_control_conformance_1.py` / `_2.py` + `test_harness_control_ipc.py` (L8's deterministic receipt-before-release rewrite applied verbatim). That milestone recorded 426 TypeScript inputs; the current scope-reporting oracle asserts 441.


## Historical 260731-EFA-L17 — Targeted-Contract And Altitude Proofs

The test tree gained three focused suites for the quality ladder: `test_code_quality_targeted.py`
(derivation selectors, transitive reverse-import closure, uncovered-module refusal, real targeted
wrapper runs with radon consuming the changed module files), `test_code_quality_memory_cap.py`
(the wrapper's inner-cap enforcement and policy naming), and
`test_worktree_integrate_quality_gate.py` (leaf targeted / series full altitude routing,
container-runtime-managed absence and explicit settings caps, refusal-before-merge, dry-run planned-gate payload). Existing families were
extended: closeout gate mode/cap/kill-shape assertions, hook-tier `pre-push → targeted`, settings
`qualityGate` family, scope-reporting integration invocation labels, and the deterministic
observer ticker-exit assertions (`ticker.join` replacing poll loops — test-only, kills a
race-dependent diff-coverage class).

## 260731-EFA-L9 Route Impact

The test tree historically gained a migration-only zero-drift snapshot, later retired by PDLS in
favor of `test_conversation_model_architecture.py` plus owning behavior suites. The layering
fitness-function suite (`test_layering.py`) and the structural-seam coverage suite
(`test_leaf_structural_coverage.py`), plus the rewritten imports across ~184 test files. The L9
closeout-order repair extends existing suites with entity-alignment preflight cases and a real-hook
proof of memory preflight → hook → wrapper → exact-index commit, including a post-wrapper working
tree edit that must stay out of the commit.

The route-overview refresh regressions also exercise the external-tree boundary:
a source-matched overview outside the supplied memory Git tree remains required,
but the body gate does not invent stale or untraced state when no comparable
memory revision exists. This preserves source-route admission without treating
absence of revision evidence as proof of a body defect.

## L23 Source-Lineage Verification Wave

The test route now covers real-Git task-derived lineage exhaustively: current
code/external-memory chains, sprint/no-edge, stale/diverged/unavailable edges,
missing/malformed contracts, no-mutation spawn/assignment/reopen/attach
refusals, HTTP 409 transport, status/Engine Room projection, and refusal
vocabulary ownership. Shared fixtures build real master/leaf contracts rather
than bypassing the gate. The same wave makes SQLite connection ownership and
short native quality scratch explicit.

## L23 Lineage Gate Regression Surface

The route now proves transitive lineage traversal, closeout refusal after quality and before an
approval claim, integration refusal when a pinned source moves before memory/merge, and structural
dispatch refusal before worker, reviewer, or curator host creation when super ancestry is stale.
Import-only updates in existing suites follow the runtime and lifecycle-model package moves while
retaining their prior assertions.

The lineage suite additionally creates a real sibling linked checkout and points the parent
contract at it while the leaf remains on the original checkout. A current projection proves the
policy compares shared Git repository identity rather than literal checkout paths.

## Historical L23 Full-Dagger Coverage And Stability Follow-up

The full-gate repair adds focused branch proof for static conversation-helper preflight, provider
subprocess stdin/timeout handling, and Docker inspect command/JSON/shape handling. These are
test-only additions over unchanged production helpers. The IPC duplicate-submit test keeps its
strict ordering—duplicate refusal occurs while the first submit is held—but uses a five-second
outer synchronization timeout so heavily parallel full-suite scheduling does not create a
one-second false failure. Full change-set comparison must use the leaf's real `1580f927…` base,
not the empty tree.

The final public Dagger contract requires a nonblank explicit diff base for both `quality` and
`verify`, forwards it on every targeted or full run, and publishes generated help for source,
bundle, base, mode, and cap. Agents Remember acceptance is Dagger-only: leaf closeout uses targeted
mode exactly once and master integration runs full mode exactly once; leaf integration does not
rerun it. Host pytest or wrapper runs are refused. The source-lineage suite's pytest-inert script launcher was removed without changing
collection or assertions, eliminating dead launcher lines from changed-coverage accounting. The
focused proof ran 26 tests with 20 workers and passed Ruff, formatting, layering, Pyright, CRAP,
and 7/7 changed-line coverage; generated help was verified.

## L23 Final Candidate Route Disposition

The final forcing surface covers Dagger-only suite attestation, fresh attempts with one shared
result, bounded output and stale-report pruning, candidate-bound route review, transitive lineage
rechecks, failure-atomic integration, and monotonic post-claim recovery.

## Historical R39 Acceptance Forcing Matrix

The test route now proves all bypass seams: pytest and the direct wrapper share one before-planning
nonce/file guard; Agents Remember cannot delete its wrapper; leaf integration cannot rerun
acceptance; series closeout cannot create code or spend a gate; master integration alone runs
full; GitHub workflows run deterministic PR checks without pytest/Dagger; publish proves main
reachability without reaccepting. Obsolete host environment/runner tests were removed.

## R42 File-Size Extraction

Two focused suites now carry behavior that previously made the broad quality files exceed the
structural file-size rail. `test_code_quality_environment_guard.py` owns direct entry refusal and
native scratch-root selection. `test_worktree_closeout_gate_scope.py` owns created/deleted-file
scope equality against the committed tree. The extraction changes ownership and citations only;
it does not weaken the Dagger authorization or staged-candidate contracts.

## Historical R43 Failure-Repair Matrix

The focused repair tests now force accepted candidate identity in recovery fixtures, clean series
closeout reuse without commit, positive recovery outcome proof, self-versus-consumer wrapper
policy at master altitude, builder-level non-Dagger refusal, and precise non-repository Git
identity failure. These are boundary repairs, not another acceptance cadence.

## R44 Metrics Shutdown Race

`test_serving_app_background_loops.py` now blocks an in-flight metrics record call, cancels the
loop, proves the task cannot finish early, releases the worker, and then observes both propagated
cancellation and the committed sample. This is deterministic shutdown-race coverage, not a timing
fallback or a second metrics owner.

## 260815-DAG-L2 Doctrine-Plane Forcing

`test_agent_doctrine_plane_identity.py` now forces the planning contract across canonical and all
nine generated lifecycle planes. It covers architect-owned initial planning, strategist inputs,
auditable fact-versus-judgment separation, organizational and atomic master classes, direct-super
ordinary leaves, atomic blocker placement, ready-frontier reprioritization, exact pre-landing
master-exit candidates, leaf-owned remediation, retired-topology wording, and rectangular changed
templates. The suite also proves every generated mirror is byte-identical to canonical doctrine.

## Historical 260815-DAG-L3 Closeout Queue Verification

This is the original queue-era test inventory. Some named forcing/integration modules were subsequently removed or split; current projection source/field effects and lifecycle evidence owners are listed in the CCR sections. The queue does not regain lifecycle authority from this historical account.

Eleven focused suites cover the queue at complementary altitudes. `test_closeout_queue.py` exercises
models, authority, deterministic ordering, evidence drift, blockers, bounded state/WAL recovery,
scaling, and sprint publication. `test_closeout_queue_models.py` owns the small strict-model cases
and directly imports both split evidence owners so targeted scope derivation selects queue tests for
either module. The focused `actions`, `blockers`, `candidate_evidence`, `evidence`, `graph`,
`lifecycle`, and `store` suites exhaust the corresponding production owners without pushing the
primary behavior suite beyond the file-size rail. `test_closeout_queue_forcing.py` poisons route evidence, graph and
task-publication race windows, durable states, actor projections, crash cuts, raw-key serialization,
and writer census. `test_closeout_queue_integration.py` crosses the real closeout/integration,
cancellation/failure, exact-commit certification, and post-contract crash-recovery seams. Existing
tool/response/reopen/isolation tests extend public registration and the adjacent governed writers.
The forcing suite also proves that oversized canonical task refs fail at runtime while their shared
projection schema stays within constraints the TypeScript generator renders exactly.

## 260815-DAG-L4 L4 Integration-Authority Forcing

The L4 suites force repository-global surface ownership, organizational versus atomic start, aliases/tags/linked worktrees, configured identity, lowest-writer refusal, bootstrap WAL, queue-lock ordering, task-topology races, exact code-memory CAS and recovery, atomic leaf-chain sealing, terminal child preservation, and preview/apply parity through production owners.

## 260815-DAG-L14 Test Route

`test_task_sprint_linkage.py` (1063 lines) forces the atomic attach/detach operations, judgment
provenance, linkage facts, and backward tolerance; `test_observer_projection_taskdocs.py` asserts
projected `masterRef`/`seats` and body-revision movement.


## 260815-DAG-L12 Route Impact

New forcing suites: `test_execution_graph_render.py` (Mermaid render determinism, escaping,
truncation, fallbacks, title join), `test_execution_graph_view.py` (primitives-only builder:
zero-edge, segmented-master, missing-master fallback, node identity),
`test_task_documents_graph_projection.py` (projection wiring: `executionGraphView` on sprint docs,
`_master_docs_by_ref`), and `test_authoring_batch_titles.py` (publication-batch title join).
Dashboard-side `SprintGraphView.test.tsx` / `SprintGraphPage.test.tsx` are covered by the
sprint-graph route overview.

## 260821-DAGQC-L1 Graph And Raw-Section Forcing

Two focused owners are new. `test_task_doc_graph_publication.py` proves the central publication
batch accepts zero or one graph-bearing document and refuses two before task bytes, the supplied
publisher, or projection publication can change. Source reconciliation separately confirms that
on-disk title reads remain inside the publisher callback and topology/linkage preview and apply use
the same owner. `test_task_doc_section_scaffolding.py` proves missing canonical-register
scaffolding, preservation of existing sections, typed refusals for malformed list/member shapes,
and no partial mutation on failure.

Existing suites carry the rest of the L1 delta: `test_execution_graph_render.py` proves ordinal
Mermaid ids survive sanitizer-equivalent labels and master-qualified same-number leaf titles;
`test_task_documents_graph_projection.py` proves ownership survives the public reader;
`test_authoring_batch_titles.py` pins the shared batch owner;
`test_task_execution_topology.py` projects explicit `.ref`; and
`test_task_execution_topology_segments.py` proves structural node-only equality/hash in both
operand directions plus mixed set/dict behavior. This leaf deliberately adds no new zero-edge
suggestion and no direct `unittest.main` entry point; those proposed scope extensions were removed.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Central graph-publication cardinality, lock placement, and shared-caller forcing. | `TaskDocGraphPublicationTests` | mcp/tests/test_task_doc_graph_publication.py:93-160 |
| Raw-section shape, preservation, typed failure, and atomicity forcing. | `TaskDocSectionScaffoldingTests` | mcp/tests/test_task_doc_section_scaffolding.py:38-127 |
| Qualified title and ordinal Mermaid identity forcing. | `ExecutionGraphMermaidRenderTests` | mcp/tests/test_execution_graph_render.py:57-291 |
| Structural node-only equality/hash forcing. | `ExecutionGraphSegmentSchemaTests` | mcp/tests/test_task_execution_topology_segments.py:41-281 |


## 260815-DAG-L15 Route Impact

Three new forcing suites: `test_serving_preflight.py` (floor semantics + editable-detection branch matrix), `test_memory_quality_runs.py` (registry + application wrappers), `test_task_execution_topology_l15.py` (L15 tests split from the parent file for the file-size rail). `test_task_sprint_linkage.py` gained the F8 fact tests; `test_author_execution_graph.py` pinned the typed judgment-required refusal; `test_mcp_registration_wiring_tests_1.py` gained the wait/run_id registration tests; the L7 `test_orchestration_portfolio.py` was deleted.

## 260815-DAG Master Full-Gate Repair Route Impact

The forcing suites tracked the package restructure: ~100 test files had import paths updated to the moved `queue`/`integration`/`task_docs` packages and their `unittest.main` tail guards removed; new `test_task_doc_wire_shape.py` locks the special-op response envelope; several suites gained coverage tests (lifecycle operations, closeout actions/forging/lifecycle, organizational completion, integration ref transaction, memory-quality runs, serving preflight, doctrine plane identity).

## 260821-CLIVE-L1 Forcing Matrix

Fifteen new test/support owners force the explicit-input and evidence boundary. The initial six own
selected-queue fixtures, canonical closeout/evidence fixtures, generation admission, worktree
input, mutation evidence, and direct-landing input. Nine additional focused suites own candidate
publication reload, executable input guards, strict input/evidence model states, ledger evidence
ordering, queue generation transition, recovery projection, lifecycle-store transitions, detached
worker entry, and irreversible release guards. They cover omitted/empty/whitespace observations;
enabled/not-applicable and internal/external plans; preview/apply parity; duplicate/retry identity;
candidate and contract drift; no-authority/no-Git refusal; evidence ordering; exact finalization;
and direct landing before-lock refusal. Large legacy suites retain their production-route behavior
while focused owners absorb model/store/bootstrap cases. These migrations preserve the queue/task
boundary: task truth and accepted lifecycle evidence do not derive from queue rows. Candidate-11
retains those owners and adds full-record plus journal-byte invariance when public runtime progress
attempts an illegal phase after valid closeout finalization; it does not add another test owner.

## 260821-CLIVE-L2 Current Architecture

The test route now proves advertised controls execute or safely terminate, not merely that payloads name them. It checks exact state across same-generation retry/recover/revise/cancel, direct memory-before-ledger cuts, schema/adoption separation, source-ref movement, concurrency, and destructive archive boundaries. Product execution of these tests remains the architect's Dagger gate, not part of curation.

### Reconciled Source Evidence

| Finding | Anchor | Source |
| --- | --- | --- |
| Admission exhaustive forcing. | `test_every_public_consumer_exhaustively_refuses_each_semantic_category` | mcp/tests/test_configured_contract_admission_l2.py:184-274 |
| Operation-control forcing. | `test_retry_preserves_generation_input_candidate_and_approval` | mcp/tests/test_lifecycle_operation_controls_l2.py:130-161 |
| Terminal archive boundary. | `test_public_terminal_operation_retries_same_disposition_after_destructive_cut` | mcp/tests/test_terminal_enclosure_archive_boundary_l2.py:147-244 |

## 260821-DAGQC-L4 No Route Impact

Existing quality-policy assertions now pin the hook's precise Dagger-only acceptance wording.
The test inventory and ownership topology are unchanged. Direct targeted Vitest remains supported
diagnostic-only feedback; pytest, Playwright, changed-lines CLI execution, the direct Python
wrapper, and acceptance stay Dagger-attested. Curation performed no acceptance run.

## 260821-DAGQC-L2 Focused Forcing Coverage

The route covers the typed memory-quality identity/capacity/controller and public schema seams;
strict immutable quality-manifest publication, one-snapshot recovery, and public result model; the
explicit serving-preflight failure matrix; and closed direct-landing outcome/recovery projection.
The new `test_quality_gate_public_contract.py` is the focused pointer-rotation/public-model owner.
No omnibus or broad gate was added by curation.

## 260824-PDLS — Structural Evidence Proof

`_quality_admission.py` exposes the already-validated Dagger capability to certifying tests;
`test_pytest_bootstrap_boundaries.py` proves the authority states and the absence of the retired
Candidate A source/command surface; `test_kernel_pure_regressions.py` preserves the seven real
product assertions; `test_route_measurement.py` forces the representative comparison structure;
and `test_python_test_evidence_firewall.py` proves every accepting edge rejects diagnostic evidence.
The direct eligibility/runner tests and their synthetic cohort helper were removed with the
mechanism they tested rather than retained as compatibility proof.

## 260824-PDLS Wave 005 Focused Evidence Cards

Six focused test modules now have complete one-to-one onboarding and high-risk file cards:

- `test_cadence_runner.py` proves explicit cadence selection and non-accepting reports;
- `test_causal_failure_localization.py` proves exact-node suppression while same-file independent
  nodes continue;
- `test_causal_quality_preflight.py` proves contract-chain admission and fail-closed continuation;
- `test_evidence_lanes.py` proves exhaustive explicit categories with no unit fallback;
- `test_evidence_lifecycle.py` proves the lifecycle inventory and real consumer/owner contracts (the 34-artifact count belongs to the historical PDLS wave);
- `test_route_measurement.py` proves repeated pure, integration, and durability measurement under
  serial and repository-default xdist modes.

These cards describe forcing ownership only. They do not promote Q5-Q8 route artifacts to
acceptance evidence and do not replace the independent per-requirement Q9 adjudication.

## 260824-PDLS Final Evidence-System Reconciliation

The final route covers all changed test/support units, including the package-root certifying
bootstrap, dependency-ownership and causal-evidence helpers, focused lifecycle/enclosure units, and
the retired facade boundary. Import-forcing proves that bootstrap does not eagerly load the testing
facade or service graph. These tests support the accepted Dagger proof; no direct diagnostic result
is promoted to certifying evidence.

## 260821-ARSPAWN-L2 Forcing Matrix

The L2 matrix covers same-seat concurrent dispatch, bounded lock-map reclamation, real lock setup and acquisition refusal, duplicate pinned-brief ambiguity, viable retry convergence, missing-receipt repair, inbox-compaction
survival, contradictory or unknown evidence refusal, one proven-failed-generation retry, and
observer-log failure after durable retirement. Direct notifier evaluators fence ambiguous seats without
first-row selection. Replacement tests force incumbent preference,
staged-heir promotion, duplicate-primary and duplicate-heir ambiguity, vacancy-safe enqueueing,
and delivery-time rebinding.

Response and dashboard contract tests prove that public structural outcomes omit occupant ids
while the private `dispatchBriefEntryId` diagnostic remains schema-aligned. The matrix also
exercises both ambient and plane dispatch paths against the same transaction. These focused tests
are implementation evidence only; this entry does not claim that the closeout Dagger acceptance
lane has run.

## MCAR-L02 Curator-Coherence Forcing Matrix

`test_curator_coherence.py` covers exact identity separation, candidate/judgment set equality,
explicit evidence roots and content digests, candidate staleness, atomic generation publication,
byte-stable quality attestations, obsolete Markdown non-authority, crash replay, malformed-pointer
CAS recovery, and shared memory/closeout validation. Queue fixtures now publish real structured
coherence evidence, and parsing tests prove only the surviving judgment/priority Markdown remains
parsed. `curator_coherence_test_support.py` centralizes only fixture input authoring: low-level
external-closeout tests receive complete leaf/master/sprint topology, task mutations republish
against current truth, and the production prepare/publish owner still creates and validates the
canonical authority. The new suite is explicitly classified in `test-evidence-lanes.toml`, while
the shared helper and its complete source-derived transitive consumer set are explicit in
`evidence-lifecycle.toml`.

`test_git_command.py` additionally forces the shared low-level observation boundary with 24
concurrent candidate-tree captures through one requested scratch namespace. It requires one tree
identity and no residual scratch paths, catching the live queue/dashboard race where one observer
removed another observer's fixed index and made a single candidate intermittently unreadable.

`test_worktree_support_benchmark.py` now forces the shared coherence/body-gate consumer boundary:
an exact candidate decision accepts unchanged stale sidecar or governing-overview content, while
the same decision cannot hide an untraced overview body edit.

`test_l6_diff_coverage_projection_types.py` forces Python 3.13's PEP 695 schema shape separately:
one local `$defs` enum reference resolves to the exact named vocabulary, while a local reference to
a non-enum remains a generation refusal. The generated TypeScript vocabulary does not broaden.

The ledger-order and closeout-recovery suites construct the production `ExternalCloseoutEvidence`
type at every external-closeout call. Empty facts remain explicit only where the case exits before
refresh or intentionally exercises recovery; a dictionary cannot silently bypass the typed
candidate-bound no-impact boundary.

Generation 13 exposed three verification-contract deltas after every deterministic rail passed.
The projection requiredness suite now distinguishes scalar named vocabularies from object
interfaces; the facade inventory excludes module-local type parameters while its independent
consumer-import check remains authoritative; and the self-owned-wrapper ordering case explicitly
isolates canonical coherence because coherence behavior has its own forcing suite. These are test
contract repairs only: no rail, node, product behavior, or acceptance threshold was removed.

## MCAR-L03 Exact-Pair Evidence

`test_memory_candidate_pair.py` is the focused real-Git two-leaf/wrong-checkout suite. Companion
controller, enclosure, coherence, closeout-input, preview, recovery, model, fixture, and
registration cases prove the pair survives every acceptance/report surface, stale or wrong scope
refuses before scan/admission, official diagnostics cannot accept, and recovery rereads the exact
contract without mutating Git.

## 260831-CCR-L01 Semantic Topology Regression Boundary

Eleven focused ordinary regression units pin the new source identity without becoming task evidence.
They prove exhaustive field-effect classification and future-schema refusal; exact v2 shape and
non-structural exclusion; every candidate-relevant row/ref/node/edge/endpoint field; composite leaf
binding near misses; typed queue error preservation; broad/dense/shared-node operation counts;
one-time immutable graph generation; mutation isolation; pre-admission budget refusal; explicit
atomic-sequential mode; and projection currentness that contains only address plus completion
readiness and the separate topology fingerprint. The three coverage-edge companions additionally
pin complete source-problem shapes, exact adapter status/detail, unknown taxonomy/binding refusal,
both post-capture work-budget guards, indexed cycle witnesses and operation counts, and defensive
composite-binding paths. Existing closeout projection tests retain their multi-series activation
and graphless-no-owner forcing.

## 260831-CCR-L23 Requirement-Route Test Evidence

L23 added `mcp/tests/test_serving_requirements.py` (explicit `integration` lane in
`test-evidence-lanes.toml`) as the HTTP proof module for the task-local requirements
surface, extended the response-conformance driver with requirement-route cases
(`test_serving_response_conformance_cases_2.py`) and a `_seed_requirements` fixture, and
advanced the declared/driven surface ledger (292 declared, 139 driven; 63 HTTP routes). The
scope-reporting oracle for the dashboard build advanced from 436 to 441 TypeScript inputs.

## 260831-CCR-L12 — Five-Gate Execution And Shared Authority Suite

CCR-R12@v4 (commit `cfd09381`) adds the host-authority proof suite
`mcp/tests/test_dagger_runtime_authority.py` (registered in the `integration` lane) and reworks the
clean-quality group for the cost-ordered five-gate executor and shared Dagger authority:
`test_clean_quality_executor.py` forces authority admission/registration/exact-owner release without
docker, `test_agents_remember_quality.py` drives the portable `_execute_gate_rails` profile execution
with authority-digest-bound manifests and exhaustive same-gate terminalization, and the closeout-gate
suite (`test_worktree_closeout_quality_gate.py`, `test_worktree_support_tests_2.py`) pins the Gate-5
order - red code gate blocks the memory preflight; memory preflight aborts only after a green code
gate. Publication fixtures across the suite route attestation through
`clean_quality_executor.ReportBindings` and the strict manifest model validates the schema-v3.1
`runtimeAuthorityDigest` root field.

## CCR-R18@v1 Generation-Coherent Projection Evidence

260831-CCR-L18 added `mcp/tests/test_generation_coherent_lifecycle_projection.py` (explicit `unit-regression` lane) as the state-matrix/envelope/revision-discipline forcing suite, and updated the task-intent coverage, disposition, lifecycle-operation, legacy-bridge, generation-boundary, recovery-projection-invariant, and legacy-consumer suites for the coherent envelope, contract-scoped cancellable, and monotonic `recordRevision`. File-level detail lives in the test sidecars.

## 260831-CCR-L16 - Durable Gate And Rail Telemetry Suite

CCR-R16@v3 (certified commit `2cd360d8f45ccdcf640dc9c5d14b941ac2f0f8eb`, leaf 260831-CCR-L16) adds six focused
suites to this route, each registered in the `unit-regression` lane of the evidence-lanes manifest
(`mcp/tests/test-evidence-lanes.toml` rows 178-183): `test_telemetry_models.py` forces the frozen event
schema and closed vocabularies of `certification/telemetry/models.py`; `test_telemetry_store.py` verifies
the CAS-published, digest-chained durable journal on temporary roots; `test_telemetry_validation.py`
and its `_edges` companion force the exhaustive stream validator and readiness to fail closed;
`test_telemetry_projection.py` and its `_edges` companion verify the lossless boundary/Gate 1-5
reconstruction from compiled events. The suites exercise owned certification telemetry
contracts through deterministic in-process pytest forcing, so their cost and evidence class are
deliberate rather than inferred.

## 260831-CCR-L13 Non-Certifying Diagnostic E2E Evidence

CCR-R13@v2 (commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf`) adds the standalone diagnostic
suite group to `mcp/tests`. Four contract suites are registered in the `unit-regression` lane in
`test-evidence-lanes.toml`: `test_diagnostic_models.py` (closed vocabulary, structural
non-certifying literals, promotion refusal, immutable attempt/manifest chains), `test_diagnostic_planning.py`
(canonical scenario rail projection at diagnostic altitude and second-scenario refusal),
`test_diagnostic_projection.py` (optional-lane readiness projection: not-requested-optional,
running, newest-terminal blocking, R14 non-satisfaction), and `test_diagnostic_store.py` (durable
isolated manifest, gapless chain identity, in-flight/abandon guards, CAS fail-closed). The two
run-control suites are registered in the `integration` lane: `test_diagnostic_executor.py` (R12
authority freeze, Gate 1-3 green admission, one-replication terminalization, exact-owner release,
frozen-snapshot retry, R16 telemetry) and `test_diagnostic_diff_coverage.py` (diff-coverage closure
cells across the model, store, projection, planning, and executor guards, reusing only the leaf's own
builders).

## 260831-CCR-L17 Measured Replay And Reduction Evidence

CCR-R17 (commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185`, leaf 260831-CCR-L17) adds six fully
standalone measured-replay suites to `mcp/tests`, all registered in the `unit-regression`
lane of `test-evidence-lanes.toml` (rows 148-153): `test_replay_freeze.py` (freeze
digest determinism/tamper refusal, frozen-dimension comparability, append-only three-view population),
`test_replay_model_edges.py` (validator/comparability/reducer/digest refusal edges),
`test_replay_spans_and_measure.py` (union-wall arithmetic and the measured-run reducer),
`test_replay_scenario_branches.py` (green/red/not-applicable arms of all seventeen
scenarios), `test_replay_scenarios_and_compare.py` (ordered scenario projection and the
digest-bound comparison report), and `test_replay_fold_coverage.py` (every reducer fold
branch and every wall-union arc). No suite shares certification-run, evidence-lifecycle, or Dagger
artifacts, and none asserts a numeric reduction threshold.

## 260831-CCR-L14 Final Real-Codex Gate-4 Certification Evidence

CCR-R14@v3 (commit `54ff803a05209e06f732f2de1f90e2a71a069e08`) adds the standalone final-codex
suite group to mcp/tests. Five contract suites are registered in the unit-regression lane in
test-evidence-lanes.toml (rows 64-68): test_final_codex_models.py (closed two-fresh vocabulary,
structural certifying literals and retry-zero, immutable attempt/run/repetition chains, one-pass
never compensates), test_final_codex_planning.py (plan-record compilation against the canonical
R11 registry and the exact Gate-1..3 must-not-run barriers), test_final_codex_projection.py
(lane readiness: not-started, running, two-fresh-pass, red, stale), test_final_codex_store.py
(durable CAS run manifest, retry-disabled reservation, exact slot ordering, namespace
isolation, corrupt-file fail-closed), and test_final_codex_certificate.py (bound Gate-4
certificate with the exact ordered Gate-1..3 predecessors and the two-fresh run). The two
run-control suites are registered in the integration lane (rows 291-292):
test_final_codex_executor.py (R12 authority freeze, Gate 1-3 green admission, two fresh
certifying repetitions, no-compensation red aggregates, typed hard failures, abort, exact-owner
release) and test_final_codex_diff_coverage.py (diff-coverage closure cells across the model,
store, projection, planning, and certificate modules plus the executor, reusing only the leaf
own builders).

## Certificate Payload And Wait Regression Boundaries

`test_rail_bindings.py` now requires a complete artifact map, stable report-relative references, exact bounded byte tails and detached-handle observations. `gate_certification_test_support.py` owns shared real Git/profile/lane/catalog fixture construction for exactly two consumers. `test_gate_certification_records.py` additionally corrupts real admission/certificate store objects to prove invalid semantic digest and wrong exact-address refusals. These tests protect the owner boundaries; real Dagger execution remains separate acceptance evidence.
`test_certification_lane_bridge.py`, `test_gate_certification_records.py`, and the quality-gate tests cover the
bridge and record seam. Hand-built payload tests must be read together with the actual Dagger
producer before using them as end-to-end certificate evidence.

The status-wait group (`test_lifecycle_status_wait_outcomes.py`,
`test_lifecycle_status_wait_registration.py`, `test_lifecycle_status_wait_store.py`) protects typed
wait outcomes, public registration and the meaningful-revision store discipline. These tests do
not establish that the R05 finalization or R07/R08 certification APIs gained production callers.

## Update History

- 2026-09-06T00:38:37+00:00 — L30 independent-review correction: refreshed the four durable-store test class ranges and five owner ranges, including thread_mutex_for in kernel/file_lock.py, against actual C 97e8ed2e1fae21756c3ad995c30613d4fbfcc503. Preserved the existing behavior account and complete prior history.

- 2026-09-06T00:21:02+00:00 — CCR L30 candidate-index recovery: added source-index/R06/R07 composition evidence and its fixture/full-acceptance boundary without changing existing producer or lock evidence.

- 2026-09-05T22:23+00:00 — L30 route-impact review against `6e4ab81f6ae52bce35003377bb3aec7877554ed7`: Routed new lock, immutable-evidence and producer/export regressions; replaced accepted producer-gap assertions while retaining fixture-versus-live and pending L32 boundaries.

- 2026-09-05T07:45+00:00 — L31 cumulative source review at ea35964985f30080488270e71ac81657ac40682b: reconciled current profile selection/refusal, assertion ownership, route counts, library/production evidence limits and exact-intent tests; restored the damaged evidence-table boundary from verified current source and retained its damaged predecessor in the curation report. Verification records source review, not execution or acceptance.


- 2026-09-05T06:12+00:00 — Composed retained CCR route contributions without replacing sibling knowledge; preserved prior source-verification metadata and historical entries.

- 2026-09-04T22:45+02:00 - 260831-CCR-L14 Gate-5 memory pass (route impact): recorded the seven standalone CCR-R14 final-codex suites (five unit-regression rows 64-68, two integration rows 291-292) and their test-evidence-lanes.toml lane registrations. File-level detail lives in the new test cards. Verification stamp is the full leaf code commit `54ff803a05209e06f732f2de1f90e2a71a069e08` (tree `aff2e268968397ab8db042a782652957a3600dda`).


- 2026-09-04T22:23+02:00 - 260831-CCR-L17 Gate-5 memory pass (route impact): recorded the six standalone CCR-R17 measured-replay suites (unit-regression rows 148-153) and their `test-evidence-lanes.toml` lane registrations. File-level detail lives in the six new test cards. Verification stamp is the full leaf code commit `e84c004c37a4bad082e1a7f1bdc4bd062282a185` (tree `f97c4969d7ddb93eed75c80a4936fc05fab8e2eb`).


- 2026-09-04T20:19:44+02:00 — 260831-CCR-L15 Gate-5 memory pass for e375f2ebdc87f6843bc76168b646d606fa79caec: route coverage adds three status-wait test cards (outcomes, registration, store) and refreshes dispositions/conformance/evidence-lane cards; route index regenerated.


- 2026-09-04T17:50+02:00 - 260831-CCR-L13 Gate-5 memory pass (route impact): recorded the six standalone CCR-R13 diagnostic suites (four unit-regression, two integration) and their `test-evidence-lanes.toml` lane registrations. File-level detail lives in the new test cards. Verification stamp is the full leaf code commit `4ba18bb23ba90e201bb37341d61c0efc64161fcf` (tree `631145bf3e0d5899b1dcbccf8c0d4a8257821f0d`).


- 2026-09-04T12:30+02:00 - 260831-CCR-L16 Gate-5 memory pass (route impact): added the CCR-L16
  section for the six durable gate-and-rail telemetry suites
  (`test_telemetry_models.py`, `test_telemetry_projection.py`, `test_telemetry_projection_edges.py`,
  `test_telemetry_store.py`, `test_telemetry_validation.py`, `test_telemetry_validation_edges.py`)
  registered in the `unit-regression` lane. Verification metadata stays pinned until closeout
  stamps the leaf code commit.


- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 route impact: recorded the new generation-coherent projection suite and the refreshed lifecycle/test suites. File-level detail in the mcp/tests sidecars.


- 2026-09-04T10:05+02:00 - 260831-CCR-L12 Gate-5 memory pass (route impact): added the CCR-L12 section for the host-authority suite, the five-gate/authority rework of the clean-quality group, and the Gate-5-order closeout regressions. Verification metadata stays pinned until closeout stamps the leaf code commit.


- 2026-09-04T01:06+02:00 — 260831-CCR-L23 Gate-5 route impact: recorded the requirement-route test evidence (integration-lane registration, conformance driver cases, ledger advance, dashboard input-count oracle). File-level detail lives in the new test card and the refreshed conformance/scope cards.


- 2026-09-01T11:33+02:00 — CCR-L11 Attempt 10 added the three focused model, reachability, and
  registry-validation edge suites, classified all five certification suites as unit regressions,
  and extended the permanent shared-support ownership to the exact five-consumer set.
  Verification remains closeout-owned.

- 2026-09-01T08:13+02:00 — Final CCR-R01 reconciliation: added the three coverage-edge suites to
  the durable test-route account, bringing the focused regression boundary to eleven and the
  explicit `unit-regression` manifest cohort to nine. Their delivery-attempt changes are test-only;
  production semantics and external review authority remain unchanged.

- 2026-09-01T05:22+02:00 — 260831-CCR-L01 Attempt 9: recorded explicit `unit-regression`
  ownership for the six focused CCR-R01 suites. Their ordinary-test status and the external
  reviewer-owned acceptance boundary remain unchanged; verification remains closeout-owned.

- 2026-09-01T04:34+02:00 — Recorded the certification suites' explicit `unit-regression`
  ownership after the fail-closed closeout census found both declarations absent. No executor,
  product, or test-body behavior changed.

- 2026-09-01T03:58+02:00 — 260831-CCR-L01 Attempt 8: documented the focused field-taxonomy,
  semantic-topology, graph-scaling, source-plane, and composite-binding regression surface. These
  remain ordinary tests; accepted task evidence stays external. Verification remains closeout-owned.

- 2026-09-01T03:11+02:00 — Added the two focused certification contract suites and their exact
  permanent shared-support ownership boundary. Verification remains closeout-owned.

- 2026-08-31T20:30+02:00 — No route impact: 260831-DER adds one deterministic unit-regression
  module for fresh series, fresh leaf, and retained journal authority classification. Test-route
  ownership remains unchanged.

- 2026-08-31T10:56+02:00 — 260821-ARSPAWN-L5 closeout quality repair: recorded the bounded
  three-test relocation from the oversized structural suite into the existing dispatch-focused
  ambient/plane suite. Both files now satisfy the hard size rail; verification remains
  closeout-owned.

- 2026-08-31T10:33+02:00 — 260821-ARSPAWN-L5 closeout repair: recorded the focused
  regression for strict current-Codex execution-envelope decoding after generation 6 exposed the
  evidence parser at C09. Verification remains closeout-owned.

- 2026-08-31T10:13+02:00 — 260821-ARSPAWN-L5 closeout repair: added exact terminal request-id and
  queued-inbox completion forcing evidence. Verification remains closeout-owned.

- 2026-08-31T09:45+02:00 — 260821-ARSPAWN-L5 closeout repair: added route-level evidence for the
  single tmux namespace shared by the harness, Codex MCP child, liveness probes, and cleanup.
  Verification remains closeout-owned.

- 2026-08-30T16:32+02:00 — ARSPAWN-L4 recorded the public-surface suite's exact transitive
  closeout-input and curator-coherence support edges after the staged lifecycle catalog check
  exposed them; the focused validator passes with 35 governed artifacts.

- 2026-08-30T15:15:36+02:00 — ARSPAWN-L4 added exact-candidate public-surface and eight-starter
  self-update acceptance as explicitly classified integration evidence. Verification remains
  closeout-owned.

- 2026-08-29T21:46+02:00 — MCAR-L03: added the exact-pair forcing surface across memory quality,
  coherence, closeout, and recovery. Dagger verification remains closeout-owned.

- 2026-08-29T20:12+02:00 — Generation-13 repair: reconciled scalar-vocabulary, module-local
  type-parameter, and wrapper-fixture assumptions without weakening the Dagger test population.

- 2026-08-29T19:31+02:00 — Generation-12 repair: aligned legacy external-closeout fixtures with
  the typed reversible-evidence boundary exposed by the Python 3.13 Pyright gate. Verification
  remains closeout-owned.

- 2026-08-29T19:04+02:00 — Added the Python 3.13 named-literal projection-generator forcing case
  discovered by closeout generation 11. Verification remains closeout-owned.

- 2026-08-29T18:29+02:00 — Added forcing coverage for candidate-bound no-impact consumption and
  the preservation of untraced-content refusal.

- 2026-08-29T12:52+02:00 — MCAR-L02 C009 recovery: added the candidate-tree
  observation concurrency forcing boundary exposed by live closeout queue recovery. Verification
  remains closeout-owned.

- 2026-08-29T12:27+02:00 — Clarified that the shared curator-coherence helper owns the complete
  transitive test-consumer set derived through `test_worktree_support.py`, not only its three direct
  importers. Verification remains closeout-owned.

- 2026-08-29T11:41+02:00 — Added the shared structured-coherence fixture owner and documented its
  complete-topology and task-mutation ordering boundary. Verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Added the lifecycle-owned coherence publication and shared-consumer
  forcing matrix. Verification remains closeout-owned.

- 2026-08-29T07:35+02:00 — Classified the future-code candidate real-Git matrix explicitly as
  integration evidence after targeted Dagger rejected the unmarked test file.

- 2026-08-29T05:17+02:00 — A003 self-review repair: added concurrent-index cleanup,
  closeout-consumption, and immutable-identity coverage to the route summary.

- 2026-08-29T04:55+02:00 — Added the exact future-code candidate mutation/refusal matrix and
  retained the separate lifecycle-operation HEAD-reconciliation boundary. Execution remains
  lifecycle-owned Dagger evidence.

- 2026-08-28T15:45+02:00 — No route impact: the hook repair's fixture extraction restores the
  existing statement budget without adding a test route or changing Dagger acceptance ownership.

- 2026-08-28T14:38+02:00 — No route impact: the scope-reporting regression now pins the existing
  host-hook environment boundary to local/shared `mcp/.venv`; no test route, evidence lane, or
  Dagger-acceptance ownership changed. Verification remains closeout-owned.

- 2026-08-28T06:40+02:00 — Added the six missing focused evidence cards, corrected the lifecycle
  census to 34 artifacts, and preserved Q5-Q8 as non-accepting protocol evidence.
- 2026-08-28T05:10+02:00 — Reconciled Candidate A deletion, seven-assertion preservation, and the
  representative pure/integration/durability measurement owner.

- 2026-08-27T21:10+02:00 — Recorded the retry selector's explicit passing zero-body collection
  proof and preserved the separate missing/uncollected-path refusal.
- 2026-08-27T20:16+02:00 — Recorded the dependency-neutral retry-matrix formatter regression that
  distinguishes a test-tool defect from retry-cache, ownership, or affected-consumer defects.
- 2026-08-27T19:13+02:00 — Added the explicit known-empty retained-context forcing boundary and
  nested wrapper-owned cache setup exposed by the real Dagger matrix.
- 2026-08-27T18:33+02:00 — Recorded explicit retry Coverage.py composition, outer/child quality
  environment isolation, and the full M40-M45 Requirement Attempt Journal structural proof.
- 2026-08-27T17:19+02:00 — Recorded the canonical-collection/affected-execution retry boundary,
  its focused pure forcing suite, and explicit unit-regression lane membership.

- 2026-08-27T13:32+02:00 — M39@v1 and structural-budget repair: added the architect compilation
  proof, exact revision binding, and separately governed MCP tool-signature/Ruff support suite.
  Eight pure doctrine assertions pass; Dagger acceptance remains pending.

- 2026-08-27T12:43+02:00 — M38: added the focused per-requirement acceptance-envelope doctrine
  suite and explicit architecture-fitness manifest registration. The four pure structural tests
  passed locally under the approved diagnostic exception; governed Dagger acceptance remains
  pending.

- 2026-08-26T16:03+02:00 — Post-failure repair: completed deterministic lock setup, duplicate-brief, bounded recovery,
  rollback-seam, and read-only ambiguity forcing; also removed a pre-existing tool-output truncation
  banner. No certifying test execution is claimed.


- 2026-08-26T14:32+02:00 — Added the focused ledger-history regression route and moved the kernel
  round-trip case out of the oversized worktree-support omnibus. No certifying execution claim is
  made.
- 2026-08-26T12:30+02:00 — Reconciled the complete 260821-ARSPAWN-L2 lock, retry, replacement, output,
  and mixed-caller forcing matrix onto the IAS tests overview. Certifying Dagger execution
  remains pending.

- 2026-08-26T08:55+02:00 — Finalized the IAS coordination-evidence label against the frozen
  pass-13 suite inventory.

- 2026-08-26T08:50+02:00 — Rebound the vocabulary-boundary row to the frozen degradation and
  rewrite-healing test names/range.

- 2026-08-26T08:25+02:00 — Repaired the surviving durability-suite reference after the vacuity
  class removal and rebound all three cited classes to the frozen source.

- 2026-08-26T08:15+02:00 — Reconciled the frozen 22-file forcing surface, including six focused
  edge suites and the three paired-source/admission fixture repairs. Acceptance execution remains
  architect-owned; verification metadata awaits the real code commit.

- 2026-08-25T17:21+02:00 — PDLS reconciled the final test/support inventory and bootstrap import
  boundary while retaining Dagger as the sole certifying authority. Verification remains
  closeout-owned.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: added the canonical published-quality and task-reopen support owners, preserving real evidence/lineage fixtures without promoting test support to product authority. Verified against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is not Dagger certification.

- 2026-08-25T01:56+02:00 — 260824-PDLS documented the lifecycle catalog, explicit direct cohort,
  fixture-authority splits, single ownership graph, and product-only measurement boundary.
- 2026-08-24T21:23+02:00 — 260824-PDLS added the classifier/runner/bootstrap/firewall/cohort proof
  and moved shared helpers out of the test tree.

- 2026-08-24T14:19+02:00 — 260821-DAGQC-L2: indexed the focused memory-quality, publication/recovery, serving-preflight, and direct-landing forcing sets while preserving concurrent L4 test-route material. Verification metadata remains pinned until architect-owned closeout.


- 2026-08-24T13:51:26+02:00 — No route impact: 260821-DAGQC-L4 reconciled
  existing quality-policy assertions to the diagnostic-versus-acceptance boundary. Preserved the
  concurrent DAGQC-L1 route additions; Dagger acceptance remains architect-closeout-owned.
- 2026-08-24T13:43+02:00 — 260821-DAGQC-L1: added the two focused graph-publication/raw-section
  suites and reconciled existing graph identity consumers; recorded that the proposed new
  zero-edge and direct-entry tests are out of scope. Verification metadata remains pinned until
  architect-owned closeout stamps the real code commit.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: refreshed current route intent and source evidence for the accepted full L2 candidate; verification provenance and contract-scoped quality enforcement remain architect-closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11: no route impact; one existing store-invariant owner gained post-finalization record/journal no-effect forcing without changing the route inventory, against accepted tree `4241908c`. Verification metadata remains closeout-owned.

- 2026-08-21T03:15+02:00 — 260821-ARSPAWN-L1 fix round 1 route impact: the ambient dispatch cohort now lives in `test_dispatch_agent_ambient.py` (extracted from `test_structural_agent_tools.py` by the file-size fix); the structural-seat regression boundary names the new suite. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T02:50+02:00 — 260821-ARSPAWN-L1 route impact: `test_structural_agent_tools.py` gained the 6-test ambient dispatch cohort and `test_spawn_agent_session.py` the caller-kind provenance test. Verification metadata pinned until closeout stamps the 260821-ARSPAWN-L1 commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair route impact: ~100 test files updated (import paths to the moved packages, `unittest.main` tail guards removed, new wire-shape suite + coverage tests added). Verified at code commit e5cb139f.


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 route impact: three new forcing suites (serving_preflight, memory_quality_runs, task_execution_topology_l15 split); F8/wait-run_id/judgment-required test additions; orchestration_portfolio test deleted. Verified at code commit de3a0fd9.



- 2026-08-20T10:45+02:00 — 260815-DAG-L12:   L12 adds the graph-render, graph-view, projection-wiring, and title-join forcing suites. Verified at code commit b7f2c8e2.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 route impact: new `test_seat_independent_execution.py`
  and `test_direct_landing.py`; signature-compat updates across the task-document and
  registration-wiring suites; `test_config.py` covers `directExecutionEnabled`. Verified at code
  commit a9d50e08.


- 2026-08-20T05:06+02:00 — 260815-DAG-L14 route impact: new `test_task_sprint_linkage.py` suite
  plus projection tests for `masterRef`/`seats`. Verified at code commit 8071a644.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 route impact: five new forcing suites
  (`test_sequential_default_mode.py`, `test_queue_read_degradation.py`, `test_register_scaffold.py`,
  `test_legacy_nature_tolerance.py`, `test_closeout_lane_sync_first.py`) cover the
  scheduling-semantics correction; existing queue/topology/integration suites were adapted to the
  narrowed lane-occupying union, the removed `migrate_execution_topology`, and the
  effective-nature contract. Route purpose unchanged. Verification remains closeout-owned.
- 2026-08-19T04:20+02:00 — Historical DAG-L10 fixture expectations were updated; the unused rich
  simulation generator involved in that pass was later retired by PDLS.
- 2026-08-18T12:00:00+00:00 — No route impact: 260815-DAG-L9 added `inventory_execution_topology` forcing cases to `test_task_execution_topology.py`; route purpose unchanged.
- 2026-08-18T13:00+02:00 — No route impact: 260815-DAG-L8 added the closeout-queue projection surface; route purpose unchanged.

- 2026-08-18T10:30+02:00 — No route impact: 260815-DAG-L7 added the orchestrator portfolio loop; route purpose unchanged.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-18T01:24+02:00 — No route impact: 260815-DAG-L6 added `test_acquire_blocker_refuses_stale_super_tips`; the tests route purpose is unchanged.

- 2026-08-17T12:30+02:00 — No route impact: 260815-DAG-L5 added five organizational-completion test modules; the tests route purpose is unchanged.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled this governing route with the frozen integration-authority implementation and forcing surface. Verification remains closeout-owned.

- 2026-08-15T13:27+02:00 — No route impact: the closeout Pyright repair adds one test-only
  optional-result narrowing before an unchanged failure assertion.
- 2026-08-15T13:18+02:00 — No route impact: repository Ruff formatting touched the eleven paths
  reported by the closeout hook; all assertions, test ownership, and acceptance altitude remain
  identical.
- 2026-08-15T13:08+02:00 — No route impact: the closeout fast hook requested import ordering,
  a non-overwritten loop binding, and removal of one unused fixture parameter; no assertion,
  production behavior, test owner, or test altitude changed.
- 2026-08-15T12:53+02:00 — L3 targeted-gate route impact: added seven focused queue-owner suites
  and exact atomic/evidence/model/recovery branch matrices after the first full targeted artifact;
  production acceptance policy and test altitude remain unchanged.
- 2026-08-15T11:25+02:00 — L3 static-gate route impact: bound the extracted task-doc queue-scope
  owner to the existing topology suite; no production assertion or test altitude changed.
- 2026-08-15T11:07+02:00 — L3 Dagger-failure route impact: repaired canonical task fixtures,
  real lifecycle ownership, exact stale-evidence diagnostics, post-contract recovery projection,
  structured curator artifacts, graph rollback, and response graph completeness without weakening
  the production queue contract.
- 2026-08-15T10:24+02:00 — L3 file-size route impact: split queue model/ownership checks and
  reopen refusal guards into focused suites while preserving the same production-path assertions.
- 2026-08-15T10:10+02:00 — L3 targeted-gate route impact: bound both split evidence owners
  directly to the primary queue suite without changing production behavior.
- 2026-08-15T09:36+02:00 — L3 fast-hook repair: added forcing for runtime task-reference bounds
  without unsupported projection-schema `maxLength` keywords.
- 2026-08-15T09:10+02:00 — 260815-DAG-L3 route impact: added the behavior, forcing, and
  production-bound queue suites plus adjacent registration/reopen/isolation coverage. Verification
  remains closeout-owned.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2 route impact: expanded doctrine-plane forcing over the
  complete nature-aware topology, role authority, template shape, no-workbench, and synchronization
  contracts. Verification remains closeout-owned.
- 2026-08-15T03:33:21+02:00 — 260815-DAG-L1 second targeted-Dagger repair: the remaining pytest
  failure was one adjacent legacy expectation, not production or coverage. The application split
  now proves both `orchestrates` and sprint-only `integrationBranch` refuse as partial legacy-master
  edits; the exact artifact already passed CRAP and 423/423 diff coverage.
- 2026-08-15T03:20:17+02:00 — 260815-DAG-L1 independent-review repair: the focused suite now
  verifies the real out-of-root publication targets and poisons a later sprint read to prove
  graph-wave validation and dereference stay bound to one snapshot.
- 2026-08-15T03:10:06+02:00 — 260815-DAG-L1 targeted-Dagger repair: reconciled the obsolete
  implicit-orchestration regression with the explicit migration contract and added deterministic
  malformed-input, confinement, target-kind, missing-target, and diamond-DAG forcing cells from the
  exact failed artifact.
- 2026-08-15T02:42:41+02:00 — 260815-DAG-L1 review repair: forcing coverage now reaches the
  production create/replace/set-field authoring routes, exact render/projection cells, normalized
  migration failures, master/sprint kind-downgrade refusals, and every supported import spelling
  for the cross-root batch writer.
- 2026-08-15T02:16:50+02:00 — 260815-DAG-L1 route impact: `test_task_execution_topology.py` forces
  malformed-graph refusals, migration-required legacy visibility, exact command membership,
  preview/apply parity, render/projection output, and rollback on cross-root publication failure.

- 2026-08-14T14:03:04+02:00 — No route impact: R46 removes only an intentionally untaken local
  branch from the existing metrics-shutdown regression by expressing the same timeout assertion
  through `self.assertTrue`. Production, timeout behavior, test authority, and route ownership are
  unchanged; verification remains pinned to the last committed source until closeout.

- 2026-08-14T12:31:43+02:00 — R44 curator: recorded the in-flight metrics-write shutdown race and
  its deterministic worker drain. Verification remains closeout-owned.

- 2026-08-14T12:13:26+02:00 — R43 curator: summarized the candidate, recovery, self-policy,
  executor, and Git-identity forcing repairs. Verification remains closeout-owned.

- 2026-08-14T11:48:55+02:00 — R42 curator: added the two focused suite routes and repointed exact
  scope ownership after the file-size extraction. Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: summarized the direct-guard, self-policy, altitude, and
  workflow forcing evidence. Verification remains closeout-owned.

- 2026-08-14T09:08+02:00 — No route impact: reopened L23 adds one application regression for the
  existing leaf-only route-review altitude boundary. Test-route ownership and suite structure are
  unchanged; verification provenance remains closeout-owned.

- 2026-08-14T06:25+02:00 — L23 final candidate review: forcing coverage now spans Dagger-only
  startup attestations, fresh-attempt/shared-result quality projection, bounded output/report prune,
  candidate-bound route review, lineage rechecks, failure-atomic integration, and monotonic
  post-claim recovery. Verification provenance remains closeout-owned.

- 2026-08-13T14:32+02:00 — L23 final test-route review: recorded mandatory explicit Dagger diff
  base and generated help, Dagger-only acceptance altitude, diagnostic-only host execution, the
  pytest-inert lineage-launcher deletion, and the focused 26-test/7-line green proof. Verification
  remains closeout-owned.
- 2026-08-13T13:08+02:00 — L23 full-Dagger follow-up: recorded exhaustive coverage for three
  low-branch helpers, the IPC test-only wait-margin correction, and the requirement to run the full
  comparison against the real leaf base. Verification remains closeout-owned.

- 2026-08-13T12:53+02:00 — L23 lineage-fixture repair: recorded real parent series fixtures,
  task-derived source assertions, pre-integration sync refusal after master movement, isolated
  gate-only seams, both post-quality source-tip checks, and explicit replay-helper branch coverage.
  Verification provenance remains closeout-owned.

- 2026-08-13T12:53+02:00 — No route impact: updated the final five-test package-root shape from a
  direct member import to the already-loaded `sys.modules` package record. Test ownership and
  semantics remain unchanged and no Ruff exception exists; this supersedes the 12:26 route note.

- 2026-08-13T12:26+02:00 — No route impact: recorded the direct `__file__` alias used by five
  package-root-sensitive tests. Test ownership, scenarios, and assertions are unchanged and no Ruff
  compatibility configuration was retained; verification provenance remains closeout-owned.


- 2026-08-13T09:27+02:00 — L23 curator: added governing route coverage for the real sibling-
  worktree repository-identity regression; final provenance remains closeout-owned.

- 2026-08-13T09:05+02:00 — L23 integration-gate follow-up: the route now covers transitive lineage
  traversal, post-quality closeout refusal before approval claim, integration refusal on source-tip
  movement before memory/merge, and fail-before-host worker/reviewer/curator dispatch when super is
  stale. Import-only test changes follow the runtime and lifecycle model package moves without
  changing their assertions; final provenance remains closeout-owned.
- 2026-08-13T08:47+02:00 — L23 integration-gate repair: reconciled direct transitive-lineage guard coverage, post-quality closeout/integration movement refusals, task-derived parent fixtures, and pre-host worker/reviewer/curator spawn refusal. Verification metadata remains closeout-owned.

- 2026-08-13T00:00+02:00 — L23 post-closeout worker-authority curator repair: paired the worker-entry ordering proof with checkout-isolation proof that `lifecycle-operation` retains live authority but no daemon role. The owner reports 46 focused tests across the two affected files, Ruff clean, and diff-check clean. Verification remains closeout-owned.
- 2026-08-12T23:27+02:00 — L23 Dagger diff-coverage curator follow-up: the route-overview helper suite now proves that source matching still requires an overview outside the supplied memory Git tree while body classification emits no false bucket without comparable memory revision evidence. The owner reports the focused test green, all four previously uncovered branches covered, and exact-file Ruff clean. Verification remains closeout-owned.
- 2026-08-12T23:08+02:00 — L23 Dagger curator follow-up: the Claude late-replay regression now uses a 50ms test-only acceptance window, retaining forced expiry while removing a measured xdist scheduler race; production remains 30 seconds. Evidence improved from one local failure in 100 plus one Dagger gw16 failure to 100/100 one-process repetitions passing. Verification remains closeout-owned.
- 2026-08-12T22:50+02:00 — L23 Dagger curator follow-up: the terminal registry suite now locates tmux `-s` before asserting the custom session name, so optional `-T sync` capability arguments cannot invalidate a semantic name-override proof. The exact focused test passes and Ruff is clean. Verification remains closeout-owned.
- 2026-08-12T22:45+02:00 — L23 curator follow-up: the helper suite now separates generated citation-coordinate-only edits from substantive authored changes: the former may pass without invented history, while metadata-only and untraced changes remain fail-closed. The owner reports 10/10 focused plan tests and 16/16 combined route-overview tests green. Verification remains closeout-owned.
- 2026-08-12T22:36+02:00 — L23 pre-commit type-check curator follow-up: the worktree edge suite now consumes the route-overview helper's full three-value revision contract and typed source evidence, proving ordinary body prose is not citation-coordinate-only. The owner reports 14/14 combined tests and repository-wide Pyright green. Verification remains closeout-owned.
- 2026-08-12T22:25+02:00 — L23 curator follow-up: the helper suite now proves baseline-relative task-edited route overviews enter closeout planning despite unrelated leaf code, while metadata-only overview edits remain stale and refuse. Verification remains closeout-owned.
- 2026-08-12T22:24+02:00 — L23 async-closeout curator follow-up: checkout isolation now proves the exact enclosure report root accepts a self-overwriting operational artifact without opening a sibling coordination escape. The owner reports 14/14 focused tests green. Verification remains closeout-owned.
- 2026-08-12T21:39+02:00 — L23 curator follow-up: added the serving suite's complementary projector drain-failure proof: late worker-thread failure is logged while public cancellation remains `CancelledError`. Verification remains closeout-owned.
- 2026-08-12T21:27+02:00 — L23 curator follow-up: documented the adaptive projector fixture's LIFO cleanup ownership; later async cancellation/await now precedes temporary-root deletion. Production projector behavior is unchanged. Verification remains closeout-owned.
- 2026-08-12T21:18+02:00 — L23 curator follow-up: the platform-subprocess suite now forces deterministic existing-native `$HOME/.local/bin` prepending and real `node` resolution after Windows interop filtering. Verification remains closeout-owned.
- 2026-08-12T20:20+02:00 — L23 curator: documented the final lineage, SQLite ownership, projector, and quality-scratch regression wave; verification remains closeout-owned.

- 2026-08-12T17:27+02:00 — 260731-EFA-L23 final Dagger test-route review: the existing targeted
  code-quality regression now pins explicit progress-report precedence as the complement to its
  environment-fallback assertion. Focused pytest is 1/1; verification provenance remains
  closeout-owned.

- 2026-08-12T16:54+02:00 — 260731-EFA-L23 installed-runtime test-route review: lifecycle tests now
  pair packaged service binding with launcher proof that installed `PYTHONPATH` is preserved and the
  task checkout source root is excluded. Verification provenance remains closeout-owned.

- 2026-08-12T16:52+02:00 — 260731-EFA-L23 packaged-worker test-route review: the lifecycle forcing
  suite now proves the installed CLI builds and binds default worktree services before dispatching
  by task address. Focused proof is green under configuration-owned xdist auto; verification
  provenance remains closeout-owned.

- 2026-08-12T16:28+02:00 — 260731-EFA-L23 final test-route review: the code-quality wrapper suite
  now pins environment-derived enclosure progress-report configuration in the existing targeted
  file-size-arm regression, including explicit optional report arguments. This closes the staged
  diff-coverage branch without changing the route's test ownership; verification provenance
  remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: added durable lifecycle, Dagger clean-quality, Codex probe, native subprocess, and notifier-addressing forcing groups; verification provenance remains closeout-owned.

- 2026-08-12T09:20+02:00 — No route impact: the 260731-EFA-L20 reopen replaces one unreachable context body with a direct raising-`__enter__` assertion; test-route ownership and safety coverage are unchanged.
- 2026-08-12T08:41+02:00 — No route impact: 260731-EFA-L20 preserves the test route's ownership while deleting unreachable scaffolding, tightening opted-in installed-test failure honesty, and adding direct coverage for the two master CRAP findings.
- 2026-08-12T07:10+02:00 — 260731-EFA-L24: added host-managed
  full-gate and optional explicit-cap regression coverage; pytest remains
  literal `-n=auto`. Verification metadata remains pinned until closeout stamps
  L24.

- 2026-08-12T04:41+02:00 — 260731-EFA-L22 closeout repair: recorded the public settings-update
  branch matrix added to clear the session owner's enforced CRAP finding without weakening the
  threshold.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: migrated the shared and composed
  fake initialize responses to the clean-cut current Desktop grammar and recorded the exact client
  suffix gate; no conversation or history behavior changed.

- 2026-08-12T03:31+02:00 — 260731-EFA-L22 closeout repair: recorded the real invalid-byte hook
  regression that distinguishes raw runner surrogateescape from transport-safe facade diagnostics.
  The repair prevents MCP serialization failure without changing the one-runner boundary.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: recorded the three responsibility splits for
  structural identity, citation routing, and quality-runner policy; regenerated split-sensitive
  route citations without reducing coverage.

- 2026-08-12T00:20+02:00 — Corrected the xdist regression description after worker selection
  moved from wrapper argv to root pytest `addopts`. Verification metadata remains pinned until
  closeout.

- 2026-08-12T00:08+02:00 — Recorded worker-private XDG cache isolation and serialization-only
  subtest diagnostics required by the parallel pytest executor. Verification metadata remains
  pinned until closeout.

- 2026-08-11T23:56+02:00 — Recorded the focused command-construction regression that pins
  pytest-xdist `-n auto` alongside derived coverage arguments. Verification metadata remains
  pinned until closeout.

- 2026-08-11T22:28+02:00 — 260731-EFA-L19 final curator pass: recorded the new focused structural
  refusal module, the expanded structural coverage companion, and exact unavailable-runtime skips
  for installed harness and live Node probes. Verification metadata remains pinned until closeout.

- 2026-08-11T20:28+02:00 — 260731-EFA-L19 closeout-gate repair: recorded the `AgentRole`-typed
  seat-lifecycle fixture and the durability harness's type-check-safe, historical-archive-only gate
  import; no production compatibility path was added.

- 2026-08-11T14:40+02:00 — Recorded the enclosure-scope regressions that distinguish temporary leaf
  base comparison provenance from real commit verification and forbid invented provenance on a bare
  official-memory check.

- 2026-08-10T18:31+02:00 — 260731-EFA-L21: added the checkout-coordination isolation regression
  suite and updated global-state tests for the explicit kernel-owned pytest mode. Verification
  metadata remains pinned until approved closeout.

- 2026-08-10T12:46+02:00 — L9 closeout-order repair: recorded focused entity-preflight and
  real-hook/exact-index regression coverage; verification metadata stays pinned until closeout
  stamps the repair commit.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 route impact: recorded the three new suites and the
  baseline fixture. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 route impact: recorded the three new suites and the
  extended closeout/hook/settings/scope-reporting/observer families. Verification metadata stays
  pinned until closeout stamps the 260731-EFA-L17 commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 route impact: recorded the in-place test-family splits, the detector/facade-surface/conformance suites, and the count fix. Verification metadata stays pinned until closeout stamps the 260731-EFA-L7 commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: reviewed this route against the frontend-rail change set. No route impact: test_quality_scope_reporting.py was re-scoped to run the real hook with an npm shim; the tests route's meaning is unchanged.
- 2026-08-05T22:30+02:00 — 260731-EFA-L16 route impact: recorded the cross-store lock-order forcing tests (placement, rendezvous ABBA reproduction, offload proofs, anti-vacuity). Verification metadata pinned until closeout stamps the code commit.
- 2026-08-04T14:41:21+02:00 — 260731-EFA-L6 S18-B01 closing same-reviewer correction: narrowed the rich-sim claim to the complete raw-token/unknown_cells and Markdown-bypass relationship under the adversarial verdict, then the exact scoped fixer/check passed.

- 2026-08-02T01:42+02:00 — No content impact: re-derived line range(s) that ended past the end of the file the row names (`memory_quality/style/citations`, `citation_range_out_of_bounds`). Each range was rewritten by reading the cited construct at its current location; no claim was changed to fit a range, and no range was interpolated. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T19:40+02:00 — 260731-EFA-L5 curator. The Durable Store Integrity Gate section named
  three properties that make the instrument's output evidence and **was silent about the instrument's
  own defect**, which is the property that failed. Added the fourth: the harness derived its work
  directory — including the reclaimer's **stop flag** — from `root.parent`, and
  `test_controlplane_store_durability.py` passes sibling roots under one `self.tmp`, so all cases
  shared one flag and every case after the first left the tick loop after roughly one tick.
  Measured before the fix: **25 reclaim ticks for the first store and exactly 1 for each of the
  other seven, all eight reporting 0.00% loss**; the forced scenarios additionally shared
  `forced.id` and the `*.err` files, so a case whose appender wrote nothing was scored off its
  predecessor's receipts. Recorded the fix as
  `harness_work_dir(root) = root.with_name(root.name + "-harness")` — a **sibling**, because `root`
  does not name one place (control-plane logs under `root/workspace`, provider logs under
  `root/logs/observer/providers`, `GateStore` also globbing `root/lifecycles/*/gates.jsonl`) while
  the accounting reads that whole tree as raw bytes — and the guard as `MIN_RECLAIM_TICKS = 10`
  raising `VacuousRunError` at the end of `run_stress`, **in the instrument rather than in either
  suite**, so both contract suites and bare `main()` runs share one floor. The floor's evidence is
  recorded with its direction: 22-39 ticks idle, 34-49 under 24-way load, load *raising* the count,
  with 20 rejected because the observed minimum is 22. **The reassuring half is recorded beside
  it:** the documented base-commit rates survived, re-measured at attention 23.91% / gate 9.38% /
  supervisor-signals 8.00% / expectation-rows 7.63% / nudges 7.50% / operator-inbox 0.00% — same
  ordering, same lone survivor — because `main` already built each case a root under its own
  parent. The bug never corrupted the historical measurements; it hollowed out the ongoing
  regression. Those six figures are **labelled as the leaf's four-run means that do not appear in
  the source**, with the source's *ranges* named and located
  (`HarnessSensitivityTests`' class docstring) and each mean checked to fall inside its range. Two
  invariants added: *a measurement must refuse to report a vacuous result*, and *sibling roots under
  one temp directory must remain legitimate* — a guard demanding distinct parents would be the same
  defect rewritten as a convention. **Drift repaired:** the section described the instrument as
  covering six stores and carried the provider adapters as unstaged mid-flight work; they have
  landed, so it now says eight with `CASES` / `PROVIDER_CASES` held apart, and the three record
  classes (`survivor-*` / `decoy-*` / `anchor-keepalive`) are stated because they are what make
  "loss" mean a row nobody decided to drop. The two `_store_durability.py` and
  `test_controlplane_store_durability.py` evidence rows carried ranges from shorter versions of both
  files and were re-derived; rows were added for the instrument's fix/guard and for the provider
  suite. **Citations:** every range was opened and checked against each symbol the row names, ends
  included. `_store_durability.py` (now 1153 lines) and `test_controlplane_store_durability.py` are
  staged with no unstaged edits and are cited by line; `test_provider_store_durability.py` still
  carries unstaged edits and is cited **by symbol name only**, as are all `controlplane/` and
  `providers/` source modules. Verification metadata untouched; closeout owns it.
- 2026-08-01T19:10+02:00 — Measured-claim repair in the Durable Store Integrity Gate section; nothing
  about the instrument's three trustworthiness properties, the torn-line policy, the replay-window
  counterfactual or the mutex was touched, because it was right. The section asserted six
  base-commit loss rates, "127 of 2000", "10 runs per store" and "zero torn lines in every run" as
  measurements, and closed with "0 lost"
  against the current tree. **No base-commit measurement artifact is committed anywhere in the
  tree** — `_store_durability.py::main` can write a JSON payload but none is stored, no test asserts
  a rate, and no committed invocation passes `runs` — so that is now stated once and the rates are
  separated from what *is* checkable. `BASE_COMMIT = e52edaf5` and the `STRESS_PROFILE` literals
  (4 × 50 @2 ms against 1 reclaimer @5 ms) stay asserted, because they are literals in the file.
  31.45% and 11.50% stay asserted, on the authority of four and three independent sites
  respectively. 10.50 / 10.20 / 9.20 / 0.00%, 127 of 2000, "10 runs per store" and the whole-not-torn
  property are attributed to `durable_store.py`'s module docstring, which is the text these cards
  document. **The post-fix claim was overstated on two axes and is corrected against the test
  source, citing the class:** `MultiProcessDurabilityTests` asserts `lost == 0` in all three
  scenarios, but `forced_unlink` iterates `APPEND_CASES` — **five** stores, attention dismissals
  excluded by construction because it has no `append` — and `torn_lines == 0`,
  `append_error_count == 0` and `reclaim_error_count == 0` are asserted in the **`stress` scenario
  only**. Recorded as mid-flight, not as landed: `_store_durability.py` carries unstaged edits
  adding two provider adapters, which do not widen those counts because the working tree keeps
  `CASES` at the six control-plane stores beside a separate `PROVIDER_CASES`. The R14 sentence
  beneath it was already exact and was left alone. The 14:20 entry below
  carried the same six-rate list and was reduced to a pointer at this entry. Verification metadata
  untouched; closeout owns it.
- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator. Nine files in this route changed for one defect —
  measured record loss in the six control-plane JSONL stores — and **four of them are new**, so the
  card gained a section, nine invariants and nine evidence rows. **Durable Store Integrity Gate**
  documents the four new suites with the instrument first, because the numbers depend on it:
  `_store_durability.py` holds no assertion at all, expresses each store through its own shipped
  reclaim entry point rather than a reimplementation, and is trustworthy for three stated reasons —
  real processes via `multiprocessing` fork (the defect is cross-process; the GIL would serialise
  the window), **dual-mode** operation where a script run pins `PYTHONPATH` to exactly one
  `mcp/src` and `_require_source_root` refuses fatally if `agents_remember` resolved elsewhere
  (which is what let it measure a `git archive` of the pristine base commit), and **loss accounting
  that deliberately bypasses every store's own `read`** — a raw tolerant JSON-lines reader counting
  "record lost" and "line torn" separately, so a strict reader cannot turn a measurement into an
  exception and a tolerant one cannot report tearing as loss. Recorded the baseline the sources
  report at `e52edaf5` against the checkable `STRESS_PROFILE` literals (4 appenders × 50 records
  @2 ms against 1 reclaimer @5 ms) — corrected by the 19:10 entry above, which splits those rates by
  corroboration and restates the post-fix claim at its true strength.
  Recorded `test_controlplane_store_durability.py`'s three claims (R10/R8/R14, with loss and
  raising asserted separately because a store that raises instead of losing has moved the failure),
  `test_gate_replay_window.py`'s counterfactual (the whole defence is one appended record; delete
  only the `applied` line and the approval is spendable again — base commit exits 1 with
  `AssertionError: 'approved' != 'applied'`, fixed tree exits 0), and
  `test_durable_store_contract.py`'s in-process axis. **The mutex is documented as what it is and
  not as a race fix:** `flock` already excludes two threads of one process through the open file
  description, that was measured rather than assumed, and `thread_mutex_for` closes the
  *dependence of thread exclusion on where the handle came from* — cache one lockfile handle on the
  store and `flock` silently stops excluding, with nothing in the tree failing. Its
  unsafe-filesystem tests fake the **filesystem** at the `fcntl` boundary, scoped to one module's
  reference, and assert only on raised type, message text and on-disk state. Recorded that the five
  updated suites replaced "the pruned log stops existing" with emptiness (`is_file()` +
  `read_bytes() == b""`), which is strictly stronger since zero bytes proves the records left
  rather than that the file did — and that `test_interaction_retention.py` is the **exception**:
  its assertion had been reading a side effect of the projection tick's physical rewrite, the very
  behaviour the leaf removed, so it was split into two proven claims (the projection leaves the log
  byte-identical — newly asserted — and `GateStore.compact` in the owning process empties it)
  rather than restated. Added nine invariants covering measurement independence, real processes,
  naming the measured tree, emptiness-not-absence, splitting a claim whose evidence was a removed
  side effect, the mutex's exact scope, and faking a platform rather than the code. Added nine
  Repo-Internal rows. **Citations:** every added row's range was opened and checked against each
  symbol the row names, ends included; the four new suites' self-ranges are stable (none of the
  nine test files carries unstaged edits). Six control-plane source modules
  (`durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py`,
  `orchestration_nudges.py`, `supervisor_signals.py`) were still being edited in the code worktree
  during this pass, so rows pointing into them are cited **by symbol name** rather than by line
  range; the symbol is the durable anchor and closeout should treat the linked file cards as
  authoritative for line numbers. Verification metadata pinned until closeout stamps the L5 commit.

- 2026-08-01T14:05+02:00 — 260731-EFA-L4 curator (correction pass), one clause. The 00:50 entry below
  said `response_model` "enforces nothing on the 59 handlers that return a `Response`", which
  mis-describes the composition of the 59: **57** of the 61 HTTP routes return a `Response` subclass
  and **2** are SSE async generators feeding an `EventSourceResponse` (`GET /api/stream`,
  `GET /api/events`) — that is the 59 on which the decorator contributes an OpenAPI schema and
  validates nothing. The remaining **2** (`GET /api/terminal/sessions`, `GET /api/harnesses`) return a
  bare `dict` and *are* validated by FastAPI. The conclusion the entry draws was right; only the
  breakdown was wrong. Verified against `serving/response_contract.py` L11-L18 and against this
  card's own body. Nothing else changed.

- 2026-08-01T00:50+02:00 — 260731-EFA-L4 curator. Twenty-one modules in this route changed and
  **three are new**, so the card gained two sections. **Wire-Contract Conformance Gate** documents
  the three new suites as the enforcement half of the leaf, each with its stopping point stated
  rather than implied: `test_serving_response_conformance.py` (drives all 61 HTTP routes because
  `response_model` enforces nothing on 59 of them — **57** whose handler returns a `Response`
  subclass and **2** SSE async generators feeding an `EventSourceResponse`, `GET /api/stream` and
  `GET /api/events`; only `GET /api/terminal/sessions` and `GET /api/harnesses` return a bare `dict`
  and are validated by FastAPI; alias-strict
  `validate_wire`; the AST key-set equality behind the two genuinely-validated `dict` routes, pinned
  at 52 keys; **and the counted ledger — 286 declared `(method, path, status)` pairs, 133 driven,
  153 listed in `UNDRIVEN_DECLARATIONS` with a reason and asserted exactly**, with every one of the
  61 routes driven on at least one status), `test_served_state_conformance.py` (the 200 body
  validates as `ServedWorkspaceProjection` and is required to FAIL as `WorkspaceProjection`; the 304
  is body-less; a `delta` carries none of `SERVED_TAIL_FIELDS`; the tail stays out of
  `latest-state.json`; and `_assert_populated` is what stops the whole file from measuring an empty
  scaffold), and `test_wire_vocabulary_exhaustiveness.py` (three mechanisms of different kinds over
  the contract cells and seven further vocabularies; **the AST scan reads bare string literals only
  and is explicitly not a guarantee on its own** — pyright plus the no-`dataclasses.replace` rule is
  what makes it total, because typeshed types `replace` as `**changes: Any` and produced zero
  diagnostics against a four-member `Literal`). Recorded the measured motivation from the module
  header (165 of 213 `series-contract.md` files, 77.5%, made `context_packet` raise across seven
  gaps) and the route-wide evidence for it: fixtures were writing `"light"` / `"chat"` /
  `"master-series"` / `"master-task"` / `"master"` against a two-member `WorkflowKind`, and nothing
  failed, because `load_contract` degrades and quarantines while the refusal lives at the write
  boundary a markdown fixture bypasses. **Choke-Point And Closeout Gate Coverage** records the
  `TOOL_RESPONSE_MODELS` retyping consequences now pinned (a stale supervisor made every response
  fail its own `model_validate`; the advertised `tokens` excluded `nextStep`/`supervisorBanner`, and
  so did `amb.emit_tool`) and the four new closeout-gate classes (real `derive_scope` into real
  `ruff`; scope-equals-commit-tree as an equality covering the deleted-file mirror; both staging
  refusals asserted as damage that does not happen, with ordering proven by a surviving `MERGE_HEAD`;
  and retry/first-run committed-tree equality). Added ten invariants. **Citations:** all 33
  citation-bearing evidence rows in `Repo-Internal References` were re-checked against the current
  files (range in bounds, and the named symbol read back at the boundary); 2 had moved and were
  repaired — `test_serving.py` L430-L492 → **L441-L503** (the class shifted +11 when `_build_wire`
  was added; the range now runs from
  `test_snapshot_subscription_cannot_lose_an_interleaved_projection` at L441 through the end of
  `test_cancelled_waiting_stream_releases_its_subscription`, which the old range cut off by one
  line) and `test_worktree_closeout_quality_gate.py` L38-L222 → **L49-L369** (the old range covered
  only part of `CodeQualityGateTests` and never reached the `CloseoutCodeQualityGateTests` argument
  spy the claim names; both class statements confirmed at L49 and L248). Added eleven evidence rows.
  Also repaired a rendering defect: five rows in the 3-column `Repo-Internal References` table
  carried only two cells, so their source path was rendering in the Citations column; each gained an
  explicit `n/a` citation cell with no text changed. Verification metadata pinned until closeout
  stamps the commit.

- 2026-07-31T22:30+02:00 — 260731-EFA-L3 curator (re-verification pass after the fix workers).
  **Both new suites were restructured, so every citation into them was re-derived from the current
  files and every one had moved.** `test_git_command.py` (697 lines): `DecoyRepositoryTests`
  L151-L207 (was L84-L140), `SingleRunnerTests` L389-L459 (was L322-L402),
  `BenchmarkRunnerEnvironmentTests` L656-L693 (was L405-L442); each range re-read and confirmed to
  open on the named `class` statement. `test_cold_start.py` (421 lines): `ColdStartTests` L199-L218
  (was L153-L171), `VendoredVocabularyTests` L221-L331 (was L174-L228). `git_command.py` L24-L96
  re-checked and still correct (`GIT_REPOSITORY_SELECTOR_ENV` at L24 through the end of `run_git`).
  Added two evidence rows for the suites that did not exist when the first entry was written:
  `SingleRunnerGuardReachTests` L462-L540 and `TimeoutClassTests` L543-L653;
  `CorruptVendoredVocabularyTests` L334-L417. **Corrected the `.gitattributes` row**, which said the
  file's rule was inert and its regression removed — true of the `blank-at-eol` rule (still L1-L3)
  but no longer of the file: L13's `-text` entry names the shipped vocabulary by filename and
  cit:([`test_the_gitattributes_entry_names_the_shipped_file`], mcp/tests/test_cold_start.py:248-261) is its live regression. Wrote up the
  guard-on-the-guard reasoning (an AST sweep reports a hole and a clean tree identically, so each
  bypass form is planted: `from subprocess import run`, `/usr/bin/git`, `**kwargs` mistaken for
  `env=`), the per-command timeout assertions and their required-keyword recorder, the
  no-module-scope-import discipline via `tokens_module()`, the bounded-join deadlock guard, and
  `CorruptVendoredVocabularyTests` — including that it works on copies, asserts the corrupt file is
  *still there* afterwards, and that CRLF-mangling and truncation were measured to pass silently
  before the digest check moved into `models/tokens.py`. Verification metadata pinned until closeout
  stamps the code commit.

- 2026-07-31T21:05+02:00 — 260731-EFA-L3 curator: two modules joined this route and both are here
  because the property they guard cannot be observed the ordinary way. Added the **Single-Runner Git
  Gate** (`test_git_command.py`: the decoy repository whose `patch.dict` blocks deliberately undo
  `conftest.py`'s selector strip, the `SingleRunnerTests` AST sweep pinning
  `kernel/git_command.py` as the only module that spawns git, the stated blind spot covered by
  `BenchmarkRunnerEnvironmentTests`, the stdin/`input_text` and three-timeout-class contract, the
  `cleanup.py` remote-stall arms, and the pre-push-hook framing of `QualityGateGitTests`) and the
  **Cold-Start Gate** (`test_cold_start.py`: the subprocess probe with cold caches and a
  proven-effective socket block, the warm-versus-cold count equality, and the re-derived vocabulary
  hashes). Qualified the `conftest.py` selector-inventory sentence, which read as coverage and is
  only fixture safety. Recorded that `test_serving.py::BuildInfoTests` now patches
  `serving.build_info.run_git` — patching `subprocess.run` in a consolidated module patches nothing.
  Added two invariants and three evidence rows. Verification metadata pinned until closeout stamps
  the code commit.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 8 cross-file line citations, each re-anchored on a read-back boundary. `test_conversation_control_api.py` L1-L379 (382-line file; also dropped the "seventeen routes" phrase — that count is pinned in `test_conversation_foundation.py`, not here); `test_conversation_runtime_composition.py` L113-L252 (was L106-L260 in a 252-line file); `test_harness_submission_authority.py` L1-L675 (was L1-L687 in a 678-line file); `test_harness_control.py` L1-L1958 (was L1-L1180; the file is 1961 lines and the IPC class runs to L1958); `test_serving_harness_control_api.py` L1-L891 (was L1-L700; extended the claim to name `ControlLivenessMemoRetentionTests` at L779); `test_serving.py` L430-L492 (the three `StreamEventsTests` the claim names, was L395-L457); `test_route_index.py` L199-L907 (fixture through the last test, off the `unittest.main()` guard); `test_static.py` L29-L144.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator, **correcting and completing the mid-leaf entry
  below**. `test_complexity_baseline.py` was deleted along with the whole complexity ratchet and its
  file card removed; `test_gate_scope.py`'s three allowlists were deleted, so the routing paragraph
  and evidence row that described them were wrong and are rewritten. Twenty-two further modules
  joined the route and now have file cards: the gate suites `test_diff_coverage.py` and
  `test_gated_integration_runner.py`; the Pi capability helper `_pi_rpc_capabilities.py` with its
  recording `fixtures/pi_rpc/0.80.7-capabilities.json` (renamed from 0.80.6) and
  `test_pi_rpc_events.py`; the serving suites `test_serving_app_routes.py`,
  `test_serving_app_background_loops.py`, `test_serving_helper_behaviour.py`; the platform suites
  `test_platform_edge_refusals.py`, `test_platform_long_tail.py`,
  `test_packaged_assets_and_context_values.py`, `test_provider_runtime_helpers.py`; the conversation
  suites `test_conversation_control_and_library_helpers.py`,
  `test_conversation_control_projector_edges.py`,
  `test_codex_adapter_thread_routing_and_registry.py`; the harness suites
  `test_harness_control_runner_config.py`, `test_harness_logs_user_message_readers.py`,
  `test_harness_submission_authority_adapter_contract.py`; the worktree suites
  `test_worktree_and_observer_helpers.py`, `test_worktree_edge_paths.py`; plus
  `test_mcp_registration_wiring.py` and `test_onboarding_integrity_edges.py`. Recorded the Pi
  capability anti-drift contract, the branch-coverage CRAP change, and three pre-existing 1:1
  fixture gaps closed. The route index is now strictly 1:1 at 210 files. Verification metadata
  pinned to the leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 curator (mid-leaf, partly superseded above): three new test modules joined this route —
  `test_gate_scope.py` (the gate's scope is the tree, asserted against real argument vectors, with
  shrink-only reason-bearing allowlists), `test_complexity_baseline.py` (the shrink-only complexity
  ratchet in all four failing directions plus the `--write` cap asymmetry), and
  `test_sync_harness.py` (drift between `scripts/harness/` and the nine generated trees, content and
  mode). `test_code_quality_check.py` roughly doubled with four classes holding Radon-is-a-report,
  every-enforcing-step-can-fail, scope derivation, and the pytest strictness/marker/warning
  contracts. Rewrote the "local gate" routing paragraph accordingly and added five evidence rows.
  Verification metadata pinned to the leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 curator: replaced the Generated Bundle Whitespace Policy
  Gate with the Dashboard Bundle Placement Gate and added a Static Surface Gate. `test_sync_dashboard.py`
  inverted three fail-open tests into refusals and proves `--check` no longer exists through a real
  subprocess; `GeneratedDashboardWhitespacePolicyTests` was removed because the `.gitattributes`
  exception it policed now names a git-ignored path. Added the new `test_static.py` (both static
  states, deterministic, including method parity against the real `StaticFiles` mount) and recorded
  the three build-dependent rewrites in `test_serving.py`. Recorded the two-test split that holds
  the local gates to the wrapper after the hook tiering, and the closeout-gate argument spy.
  Refreshed the affected hot-path routing and reference rows. Verification metadata remains
  pre-commit.
- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: routed the new real-local-subprocess lifecycle tier for
  Claude (transport ownership release across start -> stop -> start, and the adapter's floor
  probe/re-launch to control readiness over the real transport), and recorded that the live smoke's
  `/cost` arm asserts the still-unimplemented harness slash-command capability owned by an upcoming
  master, so its red state there is expected rather than a regression.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: added the two new native-history
  regression suites and routed measured-size transport, exact probe/fallback, one-shot resource
  bounds, cycle/legacy behavior, typed IPC, selected-child concurrency/continuity, and dashboard
  persisted-focus/retry coverage. Updated active route ownership from two to three. Verification
  metadata remains pinned while uncommitted.

- 2026-07-26T21:59+02:00 — 260718-CHATS-L7R curator: recorded the sub-agent surface remediation
  regression pins — nine new demux-suite tests (concurrent parent pendings, method-first degrade,
  bounded pending map, load-shed queue), two codex-agents projector tests (concurrent-parent
  projection, singular rotation), one `test_harness_control.py` guard test, and the flipped
  decline-not-fail experimental-request case in `test_codex_app_server_adapter.py`; Hot Path
  Summary and route-impact sections updated. Verification metadata stays pinned (remediation
  uncommitted).

- 2026-07-26T15:45+02:00 — 260718-CHATS-L7 curator: added the harness sub-agent regression set —
  the NEW shared `_agent_wire_fixtures.py` and five NEW focused suites (thread demux, codex
  projector agents, claude projector agents, library agents) plus targeted extensions to
  `test_harness_control.py` (multiplexed respond + plural serialization), `test_harness_control_claude.py`
  (flag floor + relaunch), `test_conversation_active_service.py` (reordered binder pin + per-thread
  dict assertions), and `test_conversation_library_ports.py` (additive agent fetch at the fake
  boundary). New-file sidecars registered; verification metadata stays pinned until L7 closeout
  stamps the candidate commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental CRAP/commit-gate curation:
  added the default-threshold, closeout mutation-order, public-tool-description,
  and Claude public-projector regression contracts. Verification metadata remains
  pre-commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: updated the route body for the current backend/shared behavior; aggregate route-index generation remains manager-owned.

- 2026-07-21T12:00+02:00 — 260718-CHATS-L5P curator: body-reviewed against the post-L5 pyright fixup
  (commit `352d5cd`) that changed `test_chats_l5_hardening.py` after the L5 verification (`68b3205`). The
  change is strict-pyright conformance only (protocol-conformant fake-host param naming, an
  `isinstance`-narrowed assertion, an explicit transcript-`state` annotation, a `Mapping` import) — zero
  behavior change, no `type: ignore`, all seven H1/H2/F2/F4 regressions identical in intent — so the
  route's hardening-regression enumeration (H1 quarantine + F2, H2 authority-pin + F4, the projector-tier
  and installed companions, the 10k baseline) is UNAFFECTED and stands as written. No body change;
  verification metadata advanced to `352d5cd` (the enumeration was reviewed this cycle).
- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: added the half-time functional regression
  narrative — the NEW `test_chats_l5f_leaks.py` (R5 `SessionLockLeakTests` + `QueueRowsBoundTests`) and
  the R1-R6/R4 additions across `test_conversation_active_projectors.py`, `..._active_service.py`,
  `..._contracts.py`, `..._control_operations.py`, `..._library_gates.py`, `..._library_installed.py`,
  `test_harness_control_evidence.py`, `test_harness_control_client.py`, `test_harness_launch.py`, and
  `test_provider_containment.py`. Corrected no version-lock language in this route's narrative (the R4
  contract-only gate is captured in each test sidecar). The new-file sidecar's verification is blank
  (uncommitted); route index refresh registers it. Verification stays pinned until L5F closeout.
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: added the evidence-backed hardening regression
  narrative — the new `test_chats_l5_hardening.py` (H1 catalog-sweep quarantine + F2, H2
  authority-pin + F4), the projector-tier H2/F1 companions in `test_conversation_active_service.py`,
  and the F1 installed regression in `test_conversation_control_installed.py` — and noted the 10k
  renderer DOM/interaction baseline lands in the dashboard test tree, not here. New file card
  `test_chats_l5_hardening.py.md` registered in the route index. Verification metadata stays pinned
  until L5 closeout stamps the candidate commit.
- 2026-07-20T15:45+02:00 — 260718-CHATS-L3 curator: added the authoritative control-API regression
  set — the shared `_control_plane.py` topology (real bridge/IPC/authority/L0 seam, `NOW`-anchored
  service), the four focused suites (operations incl. Finding 1/2 pi settlement regressions; queue
  incl. the frozen-clock expiry proof; attachments incl. on-disk spool deletion; the seventeen-route
  API over a real wire), and the opt-in installed proof — plus the seventeen-route foundation pin, a
  control coverage reference row, and the corrected "control empty" claim. Verification metadata stays
  pinned until L3 closeout stamps the candidate commit.
- 2026-07-20T15:10+02:00 — 260718-CHATS-L3E curator: added the evidence-truncation settlement
  coverage to the `test_harness_control_evidence.py` description — the `ClipHelperTests` byte-level
  terminal-identity preservation tests plus the giant-scalar drop-whole (256/257 boundary)
  regression, and the new `EvidenceTruncationSettlementIpcTests` oversized-frame end-to-end
  regressions mirroring L3's `_pi_stop_reason` / `_codex_terminal_outcome` reads. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: added the native control-plane regression
  set — the contract suite `test_harness_control_plane.py` (interrupt/timeline/asset/recovery and
  client-validation batteries, 25 tests + 35 subtests), the opt-in version-locked installed
  capture `test_harness_control_plane_installed.py`, and the redacted `control-plane/*` fixture
  rows with `enablesCapabilities: false`. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-19T18:25+02:00 — 260718-CHATS-L1 curator (memory rebase): union-merged the landed L2
  library regression-set content with the L1 active regression-set content after the master
  memory branch advanced — both suite families, the merged foundation-pin coverage (active two
  routes + library five routes; control empty), and both reference rows survive. Verification
  metadata remains pinned until L1 closeout stamps the candidate commit.
- 2026-07-19T17:35+02:00 — 260718-CHATS-L1 curator: added the active conversation serving
  regression set — four focused suites (canonical status/parity, mapper grammars, engine/store
  with the F1/F2/F3 fix pins, and the real-socket production routes proving identity, cursor
  refusals, epoch-flip gap+close, provenance, parity, and no-PTY authority) plus the foundation
  pin's exact two-route active-child assertion. Verification metadata remains pinned until
  closeout stamps the candidate commit.
- 2026-07-19T16:04+02:00 — 260718-CHATS-L2 curator: added the native conversation library
  regression set — six focused suites over doubled boundaries (ASGI status ladder, cursor/scope,
  gates, ports, open arms) plus the opt-in installed-runtime suite proving the live Codex/Pi
  gates, both real end-to-end opens, and the Claude version-mismatch posture — the foundation
  pin's exact five-route library assertion and helper source set, and the observed
  evidence-not-enablement fixture rows. Verification metadata remains pinned until closeout
  stamps the candidate commit.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: added the native evidence contract suite and
  the opt-in installed-runtime capture — per-harness round-trips with no-leak proofs, buffer and
  continuation bounds, cross-domain/epoch typed rejection, the provenance matrix, the codex resume
  channel, and the redacted version-locked `substrate-evidence/*` fixture rows. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: added the conversation runtime composition
  and authorization contract suites — install-once/fail-closed composition shapes, per-app
  isolation, no-singleton and no-injected-identity proofs, loopback-only local-operator resolution,
  and cross-principal rejection — plus the one-line `coordination_root` call-shape follows in the
  two harness-control suites. Verification metadata remains pinned until closeout stamps the
  candidate commit.
- 2026-07-18T21:05+02:00 — FEUI-MX-FIX-5 added the real-Git generated-positive/authored-negative
  whitespace regression, the direct shipped-JavaScript `blank-at-eol` boundary, Vite/raw-sync byte
  ownership, the rejected-normalization rationale, retained near-miss checks, and the two-build
  byte/fingerprint determinism proof. Verification metadata remains pinned until closeout stamps
  the candidate commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: added the deterministic Git/path-rule census matrix,
  regular/linked/contaminated byte-convergence proof, typed failure coverage, and full-apply
  JSON/Markdown carryover-authority refusal/retention matrix with exact zero-mutation assertions.
- 2026-07-18T14:16+02:00 — 260715-FEUI-MX-FIX-1: added route-level coverage for deterministic
  snapshot/subscription handoff, first-recovery full snapshot with build identity, identical-state
  silence, later named delta, and explicit close/cancellation subscriber cleanup. Verification
  metadata remains pinned until closeout stamps the candidate commit.
- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the build/static, raw-event, tmux-environment, and
  narrow harness-discovery regression matrix. Verification metadata remains pinned pending
  candidate closeout.
- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: documented the hostile normalized-contract
  matrix, exact two-port/three-router topology, repository-only helper resolution, and redacted
  non-enabling runtime fixtures. Added current governing/reference structure; verification remains
  pinned to committed source truth until closeout stamps the candidate.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: added the authoritative submit/withdraw
  adversarial matrix, exact-ref and early-completion proofs, safe-retry/first-byte split, raw-free
  status/API bounds, native no-queue guarded-write semantics, and retention/privacy invariants after
  canonical review round 6 PASS.
- 2026-07-16T07:27+02:00 — 260714-ACPUI-L5 curator: added route coverage for the complete Claude
  discovery-selector grammar and normal-launch preservation, plus the explicit-opt-in two-turn
  Codex live advertise/launch/queued-set/retention proof with sanitized evidence recording.
  Verification metadata remains pinned until closeout stamps the L5 code commit.
- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: added route coverage for install/auth cache
  fencing, failed-refresh quarantine, complete-pair launch, live-reopen/dead-replacement truth,
  cross-process one-process publication, exact-session first-byte ambiguity, request-id idempotency,
  retained reconciliation without resend, raw-free public responses, liveness-first status, and
  shared role-spawn conflict behavior. Verification metadata remains pinned until closeout stamps
  the L4 code commit.
- 2026-07-16T01:34+02:00 — 260714-ACPUI-L3 curator: added route coverage for exact five-value
  setter truth, FIFO/cancellation behavior, Claude correlated terminal and dynamic Fable evidence,
  Codex ordered selection epochs and successful fresh-turn promotion, Pi bounded coherent
  error/clamp readback, 8/64 reclamation scaling, and the transitive 17-module no-paste guard.
  Daemon setter endpoints remain L4. Verification metadata remains pinned until closeout stamps
  the L3 code commit.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: added route coverage for the normalized
  launch contract, complete settings fixtures, native per-harness application, Codex selector
  census and roleless defaults, Pi exact identity, Claude mismatch failure, no-paste enforcement,
  and token-free failure/echo evidence. Verification metadata remains pinned until closeout stamps
  the L2 code commit.
- 2026-07-15T20:08+02:00 — 260714-ACPUI-L1 curator: made the 2.1.210 Claude JSONL cohort the
  active fake-transport fixture authority and documented token-free dynamic catalog coverage across
  Claude, Codex, and Pi. Verification metadata remains pinned until closeout stamps the L1 commit.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: added route-level delayed-reply IPC peer-disconnect
  containment and bridge reconciliation evidence.
- 2026-07-14T17:18:47+02:00 — 260713-PHA-L6 curator: added route-level Codex completion correlation,
  same-row pending semantics, loud failure cases, replacement-only queue state, and fixture-only pins.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: refreshed the test-route body for structured
  capability negotiation, rolling inbox compatibility, and the deferred R10 boundary.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: added fake protocol, pinned JSONL fixture, and
  credential-safe `/cost` live-smoke coverage for Claude 2.1.207, including failed API-429 semantics.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator: added route coverage for the Codex app-server
  fixture, adapter/protocol fake tests, and credential-safe live smoke. Verification remains pinned
  until closeout stamps the leaf commit.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: added governing route coverage for the Pi RPC
  protocol, subprocess, adapter, fixture, and isolated real-smoke regression files. Verification
  metadata remains pinned until closeout stamps the L4 code commit.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: added route-body coverage for the
  bridge conformance suite and its five changed serving regression files.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3 curator: added route coverage for the change-driven
  projection pacing regressions — new `test_change_watcher.py` (roots/filter/pacer/projector/real
  inotify) plus the `test_serving.py` `watch_changes=False` ETag fixture note and the
  `test_dashboard_daemon.py` heartbeat plumbing pins. Verification metadata remains pinned until
  closeout.
- 2026-07-12T20:02+02:00 — 260712-PTS-L2 curator: added route coverage for the shared per-tick
  contract-snapshot regressions in `test_projection_scaling_cs6.py` (one enumeration/parse pass per
  tick, stat-identity cache with ctime hardening, output parity, live-set retention, failure retry).
  Verification metadata remains pinned until closeout.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1 curator: added route coverage for walk-free contract loads
  and the explicit heal sweep (parity, idempotence, dry-run, error tolerance, CLI seam) in
  `test_leaf_ref_resolution.py`. Verification metadata remains pinned until closeout.
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: added governing route coverage for the new
  inbox-reclamation regression suite and its final PASS delta tests, including event silence and
  corrected persisted removal semantics. Verification metadata remains pinned until closeout.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: added route coverage for bounded landing observation, no-wait projection, stale rendering, invalid-snapshot containment, and shutdown after observer failure.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
