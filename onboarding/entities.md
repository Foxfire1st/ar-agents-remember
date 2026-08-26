# Entities

| Field       | Value                  |
| ----------- | ---------------------- |
| repository  | agents-remember     |
| doc_type    | `repo-entity-catalog`  |
| lastUpdated | 2026-08-26T19:27+02:00 |
| lastVerifiedCommitHash | `cb6623775a04cbdeb0509dc26f08a8268189c3f6` |
| lastVerifiedCommitDate | `2026-08-25T08:12:56+02:00` |
| status      | active                 |

## Purpose

This catalog documents load-bearing real entities in `agents-remember`. It is not a glossary of every workflow term and it does not catalog task files. Task files remain planning artifacts; this file describes current reusable repository concepts and the boundaries between them.

### IAS Frozen Candidate Evidence Boundary

The queue, external-ledger, worktree-contract, lineage, and integration narratives below are
reconciled to the architect-frozen source-pair coordination candidate. The candidate includes new,
uncommitted activation and sync owners, so their real-commit entity fingerprints and catalog
verification metadata remain closeout-owned. Existing fingerprint rows deliberately remain pinned
to committed source; no uncommitted blob or verification stamp is fabricated here.

## Entity Fingerprints

Each row records the deterministic source evidence used by `c-02-memory-quality-control` skill for entity drift detection. The `git-blob-set-v1` fingerprint sorts the evidence paths, resolves each current `HEAD:<path>` Git blob hash, and hashes the resulting `path + blob_hash` list. A changed fingerprint means the entity entry needs review; it does not automatically prove the prose is wrong. `c-02-memory-quality-control` skill also reconciles this table against `## Entity Inventory`, so missing rows and orphaned rows are actionable catalog maintenance.

| Entity                              | Algorithm         | Fingerprint                                                               | Evidence Paths                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------- | ----------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Onboarding Unit                     | `git-blob-set-v1` | `sha256:52fbceb01ca55fe0c3a212c06af879d13fee19444df7527d403f6d3784748d6b` | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py`                      |
| Runtime AGENTS Template Package     | `git-blob-set-v1` | `sha256:49e5e4a592af6a808a4588fb25e2891681fe00cdb06bbcfa65603b6b1721e023` | `mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md`; `mcp/src/agents_remember/install/runtime.py`                                                                                                                                                                                                                                    |
| Coordination Context                | `git-blob-set-v1` | `sha256:8725cd636fe7a28a9cc46bc37f2ee1dd615c892c7e1733d10a9f865b8a042130` | `mcp/src/agents_remember/package_data/runtime/skills/c-08-ar-coordination-context-resolver/SKILL.md`; `mcp/src/agents_remember/kernel/coordination_context_resolver.py`                                                                                                                                                                                                                                                 |
| Path Rule                           | `git-blob-set-v1` | `sha256:77175049abc3fb1a4cb416fc7d451a1c52bcce8ffb01bf078726c5f534b70e61` | `mcp/src/agents_remember/kernel/coordination_context_resolver.py`; `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.json`; `examples/mcp/settings.example.json`                                                                                                                                                                                                       |
| Memory Quality Control              | `git-blob-set-v1` | `sha256:ba5ef2ced55476dbb709f5a7a9d2252a619d51e928de87a483dbd6d3e8d74d37` | `mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md`; `mcp/src/agents_remember/memory_quality/check.py`; `mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py`; `mcp/src/agents_remember/memory_quality/style/update_history/history_order.py`; `mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py` |
| File-Level Onboarding Content Model | `git-blob-set-v1` | `sha256:cd698aab9465ecd7ddd2a7dfa2606ff49013e9cba93507bdb9d52e559d894259` | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md` |
| Light Task Artifact                 | `git-blob-set-v1` | `sha256:2670e6700fad52cb381a310a5e97b85d5979debccc59e86aadaef96cd6908f74` | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md`                                                                                                                                                                                                                                                                                      |
| External Memory Ledger              | `git-blob-set-v1` | `sha256:ce0cee7e6f66de3c30629c2b45770ff23aa4ff2943c959a510861ebc5839c5cb` | `mcp/src/agents_remember/kernel/memory_ledger.py`; `mcp/src/agents_remember/memory/baseline.py`; `mcp/src/agents_remember/worktrees/modules/closeout.py`; `mcp/src/agents_remember/worktrees/modules/closeout_external.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| Sprint Closeout Queue               | `git-blob-set-v1` | `sha256:3046f6750181d09ec60a5e67d51330f96bff5fda40054142be4656b41f67d6f4` | `mcp/src/agents_remember/controlplane/closeout_queue_store.py`; `mcp/src/agents_remember/models/closeout/projection.py`; `mcp/src/agents_remember/models/queue/closeout_queue.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py`; `mcp/src/agents_remember/worktrees/queue/closeout_queue.py` |
| Closeout Effective Input            | `git-blob-set-v1` | `sha256:c4eaddec85de1781f2f9f1f8c66953090f7ecf62f74c8bc40eb8374ecb9128f6` | `mcp/src/agents_remember/application/worktree_tools.py`; `mcp/src/agents_remember/mcp/registration/closeout.py`; `mcp/src/agents_remember/models/closeout/input.py`; `mcp/src/agents_remember/worktrees/closeout_input.py`; `mcp/src/agents_remember/worktrees/direct_landing.py`; `mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py` |
| Closeout Mutation Evidence          | `git-blob-set-v1` | `sha256:103e79c3f83973ac8a3354bc2693188ae985232c35367cb643cafeb714e9a556` | `mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py`; `mcp/src/agents_remember/models/lifecycles/mutation_evidence.py`; `mcp/src/agents_remember/models/lifecycles/operation.py`; `mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py`; `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py`; `mcp/src/agents_remember/worktrees/modules/closeout_external.py`; `mcp/src/agents_remember/worktrees/queue/closeout_recovery.py` |
| Memory Baseline Adoption            | `git-blob-set-v1` | `sha256:f7f1696e0c096898ca582e056d9130b8036a2e39a4c6360d524391ce01f91e63` | `mcp/src/agents_remember/package_data/runtime/skills/c-10-adopt-memory-baseline/SKILL.md`; `mcp/src/agents_remember/memory/baseline.py`                                                                                                                                                                                                                                                                                  |
| Worktree Contract                   | `git-blob-set-v1` | `sha256:36935de1c502931a76d07b1a57e2eb4cec9f570eec45d190c939d647b5b00a81` | `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md`; `mcp/src/agents_remember/worktrees/modules/closeout.py`; `mcp/src/agents_remember/worktrees/modules/guidance.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py`; `mcp/src/agents_remember/worktrees/worktree_contract.py` |
| Source Lineage                      | `git-blob-set-v1` | `sha256:1d51bdde074702b6bdbf6bae54b0d4f7c4d7c0bd815fe3f49789a8369559e8b0` | `dashboard/src/panels/engine-room/DiagnosticsPanel.tsx`; `mcp/src/agents_remember/models/worktree.py`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-brief.md`; `mcp/src/agents_remember/serving/terminal_opener.py`; `mcp/src/agents_remember/worktrees/modules/closeout.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py`; `mcp/src/agents_remember/worktrees/source_lineage.py` |
| Worktree Integration                | `git-blob-set-v1` | `sha256:b53ee822ebb5b801fdae72b793353f16dda56159d9fc3f09091307bd1f329327` | `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md`; `mcp/src/agents_remember/worktrees/modules/cleanup.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| Branch-Gated Cross-Repo Source      | `git-blob-set-v1` | `sha256:8725cd636fe7a28a9cc46bc37f2ee1dd615c892c7e1733d10a9f865b8a042130` | `mcp/src/agents_remember/package_data/runtime/skills/c-08-ar-coordination-context-resolver/SKILL.md`; `mcp/src/agents_remember/kernel/coordination_context_resolver.py`                                                                                                                                                                                                                                                 |
| Provider Degradation Protocol       | `git-blob-set-v1` | `sha256:4ea471279c09fa98cc621c6dda34c56c7edfe765d94e12044148fd787c58d52c` | `mcp/src/agents_remember/providers/degradation.py`; `mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py`; `mcp/src/agents_remember/controlplane/operator_inbox_records.py`; `mcp/src/agents_remember/controlplane/orchestration_artifacts.py`; `skills/l-01-agent-lifecycles/roles/system-specialist.md` |
| Seat Binding Identity               | `git-blob-set-v1` | `sha256:e53888cdad34b05f52703bfcc43b61bfd6b246c8b7335f7d91198753ca9a7902` | `dashboard/src/data/railModel.ts`; `dashboard/src/data/sessions.ts`; `dashboard/src/data/taskHierarchy.ts`; `mcp/src/agents_remember/controlplane/signal_routing.py`; `mcp/src/agents_remember/models/declared_caller.py`; `mcp/src/agents_remember/models/task_document_ref.py`; `mcp/src/agents_remember/models/terminal_catalog.py`; `mcp/src/agents_remember/serving/ambient_seat.py`; `mcp/src/agents_remember/serving/structural_seats.py`; `mcp/src/agents_remember/serving/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_task_assignment.py`; `mcp/src/agents_remember/tasks/document_refs.py` |
| Seat Retirement                     | `git-blob-set-v1` | `sha256:21e9546e55ca5d1b8ef04b35ecf433327f9a544c3786af505b093907f93e9d96` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/app.py`; `mcp/src/agents_remember/serving/retire.py`; `mcp/src/agents_remember/serving/retire_policy.py`; `mcp/src/agents_remember/models/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_catalog.py` |
| Seat Landing Archive                | `git-blob-set-v1` | `sha256:0a7b402913ae0ef137b82fc8dbb22c2cee2b5b5e18d384472da2fd2d07ecf895` | `dashboard/src/data/railModel.ts`; `dashboard/src/data/sessionLifecycle.ts`; `dashboard/src/panels/session-cockpit/SessionRail.tsx`; `mcp/src/agents_remember/application/worktree_tools.py`; `mcp/src/agents_remember/models/terminal_catalog.py`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/manager-brief.md`; `mcp/src/agents_remember/serving/app.py`; `mcp/src/agents_remember/serving/landing.py`; `mcp/src/agents_remember/serving/terminal_catalog.py` |
| Supervisor Sweep                    | `git-blob-set-v1` | `sha256:fd9d0c4f603a37ab62854f0a38843ff5fefd9b4ab1ae2925c8d92a36584068aa` | `mcp/src/agents_remember/kernel/agentic_settings.py`; `mcp/src/agents_remember/mcp/tools/base.py`; `mcp/src/agents_remember/serving/pane_signals.py`; `mcp/src/agents_remember/serving/agent_notifier_heartbeat.py`; `mcp/src/agents_remember/kernel/primitives/inbox_backoff.py`; `mcp/src/agents_remember/controlplane/operator_inbox_store.py`; `mcp/src/agents_remember/controlplane/signal_routing.py`; `mcp/src/agents_remember/controlplane/agent_notifier_signals.py` |
| Task Document                       | `git-blob-set-v1` | `sha256:5e5c4b3326d36b6937d9b03d5e90aa4cd10efefa15f69705bd406978e09e9db4` | `dashboard/src/data/taskDocuments.ts`; `dashboard/src/data/taskHierarchy.ts`; `dashboard/src/data/taskIdentity.ts`; `dashboard/src/panels/detail-panel/DetailPanel.tsx`; `mcp/src/agents_remember/models/task_document_ref.py`; `mcp/src/agents_remember/observer/projection.py`; `mcp/src/agents_remember/observer/projection_graph.py`; `mcp/src/agents_remember/serving/projections/snapshots.py`; `mcp/src/agents_remember/tasks/document_refs.py`; `mcp/src/agents_remember/tasks/execution_graph_titles.py` |
| Delivery Injector                   | `git-blob-set-v1` | `sha256:299a2f1410f700e8eda5ea3aab2134204bf3a8205a1000145102ba122e7690f9` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/harness_adapters.py`; `mcp/src/agents_remember/serving/harness_logs.py`; `mcp/src/agents_remember/serving/inbox_delivery.py`; `mcp/src/agents_remember/serving/injector.py`; `mcp/src/agents_remember/models/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_paste.py` |
| Harness Capability Snapshot         | `git-blob-set-v1` | `sha256:6cfad83472938de71395a43989d5c861bbcb8d8c2590ceb5fb4fd3df85190073` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/claude_stream_protocol.py`; `mcp/src/agents_remember/serving/codex_app_server_adapter.py`; `mcp/src/agents_remember/serving/codex_app_server_session.py`; `mcp/src/agents_remember/serving/harness_capabilities.py`; `mcp/src/agents_remember/serving/harness_capability_catalog.py`; `mcp/src/agents_remember/serving/harness_control_adapter.py`; `mcp/src/agents_remember/serving/harness_control_api.py`; `mcp/src/agents_remember/serving/harness_control_bridge.py`; `mcp/src/agents_remember/serving/harness_control_claude.py`; `mcp/src/agents_remember/serving/harness_control_client.py`; `mcp/src/agents_remember/serving/harness_control_factories.py`; `mcp/src/agents_remember/serving/harness_control_models.py`; `mcp/src/agents_remember/serving/harness_control_runner.py`; `mcp/src/agents_remember/serving/harness_launch.py`; `mcp/src/agents_remember/serving/pi_rpc_adapter.py`; `mcp/src/agents_remember/serving/pi_rpc_configuration.py`; `mcp/src/agents_remember/serving/pi_rpc_events.py`; `mcp/src/agents_remember/serving/terminal_opener.py` |
| Harness Submission Authority        | `git-blob-set-v1` | `sha256:42c45b45c86c2522a2dd4a50d1c688a73c5951e54fe42a3c55eab5bff0b9f7c9` | `dashboard/src/data/submissionLifecycleClient.ts`; `dashboard/src/data/submitClient.ts`; `dashboard/src/data/submitMachine.ts`; `mcp/src/agents_remember/serving/codex_app_server_adapter.py`; `mcp/src/agents_remember/serving/harness_control_adapter.py`; `mcp/src/agents_remember/serving/harness_control_api.py`; `mcp/src/agents_remember/serving/harness_control_bridge.py`; `mcp/src/agents_remember/serving/harness_control_claude.py`; `mcp/src/agents_remember/serving/harness_control_client.py`; `mcp/src/agents_remember/serving/harness_control_ipc.py`; `mcp/src/agents_remember/serving/harness_control_models.py`; `mcp/src/agents_remember/serving/harness_submission_authority.py`; `mcp/src/agents_remember/serving/harness_submission_ledger.py`; `mcp/src/agents_remember/serving/pi_rpc_adapter.py` |

## Entity Inventory

### Onboarding Unit

| Field                        | Value                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Documentation artifact                                                                                                                                                                                                                                                                                                                               |
| Represents In Reality        | A durable unit of repository knowledge that can be retrieved and verified before an agent relies on it.                                                                                                                                                                                                                                              |
| Description                  | File-level onboarding mirrors one concrete source file; overviews summarize repo or route scopes; repo-level catalogs document recurring entities, carry deterministic evidence fingerprints, and require one fingerprint row per inventory entity. Onboarding maintenance starts from the resolved memory layer's `Domain Documentation` category for documentation evidence; live sources named there are authoritative, local mirrors are orientation caches, and refactor maintenance preserves useful onboarding before deleting or regenerating it. |
| Canonical Source Of Truth    | `c-05-create-or-update-onboarding-files` skill onboarding maintenance rules, the resolved memory layer source registry for documentation discovery, and the generated onboarding files under the resolved onboarding root.                                                                                                                                                                      |
| Current Naming Drift         | None recorded after the external-memory terminology alignment; internal memory uses `ar-memory/`, while external memory uses `ar-coordination/memory-repos/ar-<repo>/`.                                                                                                                                                                              |
| Key Identifiers              | `repository`, `path`, `sourceRoute`, `doc_type`, `lastVerifiedCommitHash`, `lastVerifiedCommitDate`, inline `sourceDigest`, and entity `git-blob-set-v1` fingerprint rows.                                                                                                                                                                           |
| Parent / Child Relationships | Lives under the onboarding root returned by `c-08-ar-coordination-context-resolver` skill. File-level units mirror repo-relative source paths.                                                                                                                                                                                                                                                |
| Often Confused With          | Task artifacts, roadmap specs, source registries as proof, local documentation mirrors as authoritative sources, and temporary drift reports.                                                                                                                                                                                                        |
| Source References            | [README.md](agents-remember/README.md) L57-L61; [`c-05-create-or-update-onboarding-files` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md) L8-L19; L58-L65; L137-L148; [file-level workflow](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) L20-L29; L113-L121 |
| Migration Notes              | The worktree-support stack should preserve one-to-one file-level mapping even as roots are renamed or split, and refactors should move or reuse accurate onboarding when behavior moves across files.                                                                                                                                                 |

### Runtime AGENTS Template Package

| Field                        | Value                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Installable runtime instruction package                                                                                                                                                                                                                                                                                                                                                                                                            |
| Represents In Reality        | The source-owned set of `AGENTS.md` templates that can be installed into a coordinator runtime tree.                                                                                                                                                                                                                                                                                                                                               |
| Description                  | The current package lives under `mcp/src/agents_remember/package_data/runtime/agents-md-files/` and contains four templates: `coordinator/AGENTS.md`, `skills/AGENTS.md`, `system/AGENTS.md`, and `tasks/AGENTS.md`. The coordinator template routes spawned roles by brief and treats the developer-facing free chat as a launcher: research stays inline, while role-shaped work spawns a clean architect with the settings-owned profile. The coordinator and system templates use `context_packet` provider status when configured; provider authority lives in MCP settings outside the coordinator root. The system template separates clean-source drift candidates from dirty-source work in progress before curation. |
| Canonical Source Of Truth    | The four source templates under `mcp/src/agents_remember/package_data/runtime/agents-md-files/` and their file-level onboarding units.                                                                                                                                                                                                                                                                                                                                                  |
| Current Naming Drift         | No `workflow` or memory-repo `AGENTS.md` template exists after the shuffle; memory repos are not expected to provide root-level `AGENTS.md` files and use `system/*` files for repo-specific guidance. Coordinator `system/settings.json` is no longer the MCP/provider authority surface. |
| Key Identifiers              | Source paths under `mcp/src/agents_remember/package_data/runtime/agents-md-files/`; intended installed destinations `ar-coordination/AGENTS.md`, `ar-coordination/skills/AGENTS.md`, `ar-coordination/system/AGENTS.md`, and `ar-coordination/tasks/AGENTS.md`.                                                                                                                                                                                                                         |
| Parent / Child Relationships | Complements `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/` fixtures and MCP package runtime install behavior; file-level onboarding mirrors each of the four templates.                                                                                                                                                                                                                                                                                             |
| Often Confused With          | The repo-root `AGENTS.md`, example memory-repo instructions, or old scattered source-tree `AGENTS.md` files.                                                                                                                                                                                                                                                                                                                                       |
| Source References            | [runtime installer](agents-remember/mcp/src/agents_remember/install/runtime.py); [coordinator template](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md) L3-L112; [skills template](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md) L1-L33; [system template](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md) L1-L68; [tasks template](agents-remember/mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md) L1-L153 |
| Migration Notes              | Runtime installation should copy only the four package-owned templates. Memory-repo `AGENTS.md` content should be created with the memory repo, not installed from this package.                                                                                                                                                                                                                                                                   |

### Coordination Context

| Field                        | Value                                                                                                                                                                                                                                                                                                                                                                                 |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Resolver output contract                                                                                                                                                                                                                                                                                                                                                              |
| Represents In Reality        | The resolved topology, roots, settings, storage rules, path rules, and cross-repo allowances for one code repository.                                                                                                                                                                                                                                                                 |
| Description                  | `c-08-ar-coordination-context-resolver` skill produces this context so downstream skills do not rebuild topology rules. MCP settings own installed coordination-root authority; the package-local resolver no longer reads source-checkout `.env` or `.env.example` as coordination-root inputs. The public facade remains `coordination_context_resolver.py`, while implementation responsibilities now live under `kernel/coordination_context/`. Since 260731-EFA-L4 `CoordinationContext.memory_mode` is typed as the worktree contract's own `MemoryMode` alias rather than a second hand-written `Literal`, because `resolver.build_coordination_context` reads `contract.memory_mode` straight into the field (the code comment on that field names a `resolver._resolve` that does not exist): the resolved context and the contract now share one declaration of `internal`/`external`/`disabled`. The three values are unchanged, and no other resolved field moved. |
| Canonical Source Of Truth    | `c-08-ar-coordination-context-resolver` skill docs, the package facade, and the focused coordination-context implementation modules.                                                                                                                                                                                                                                                   |
| Current Naming Drift         | None recorded for the `c-08-ar-coordination-context-resolver` skill resolver output contract.                                                                                                                                                                                                                                                                                                                                  |
| Key Identifiers              | `topology`, `code_repository_name`, `code_repository_root`, `coordination_root`, `memory_root`, `onboarding_root`, `settings_path`, `path_settings_path`, `task_root`, `temp_root`, `pathRules`, `contract_path`, `worktree_group`, `ledger_path`, `memory_mode` (the worktree contract's `MemoryMode` alias). Without a task name, `task_root` is `ar-coordination/tasks/<repo>/`; with a task name or contract, it is the concrete task folder. |
| Parent / Child Relationships | Consumed by `c-02-memory-quality-control` skill, `c-05-create-or-update-onboarding-files` skill, `c-03-repo-bootstrap` skill, and task workflows.                                                                                                                                                                                                                                                                                                                                     |
| Often Confused With          | The onboarding root itself or the worktree task contract.                                                                                                                                                                                                                                                                                                                             |
| Source References            | [`c-08-ar-coordination-context-resolver` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-08-ar-coordination-context-resolver/SKILL.md); [coordination_context_resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context_resolver.py); [resolver.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/resolver.py); [models.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/models.py) |
| Migration Notes              | `c-08-ar-coordination-context-resolver` skill is now worktree-contract-aware but remains facts-only; `c-09-git-worktree-manager` skill owns mutation.                                                                                                                                                                                                                                                                                                       |

### Path Rule

| Field                        | Value                                                                                                                                                                                                                                                 |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Settings and eligibility rule                                                                                                                                                                                                                         |
| Represents In Reality        | Include/exclude rules that decide which source paths and file types are eligible for onboarding.                                                                                                                                                      |
| Description                  | Path rules are parsed from JSON-first settings where possible and are evaluated separately from storage mode. JSON and Markdown parsing now live in focused settings modules, while storage evaluation lives in `coordination_context/storage.py`.      |
| Canonical Source Of Truth    | `c-08-ar-coordination-context-resolver` skill settings and storage modules plus README storage guidance.                                                                                                                                                                                       |
| Current Naming Drift         | Coordinator and memory-repo settings scope path rules per repository; unscoped rules can accidentally read as global defaults.                                                                                                                        |
| Key Identifiers              | `path`, `include.paths`, `include.fileTypes`, `exclude.paths`, `exclude.fileTypes`, `storage`.                                                                                                                                                        |
| Parent / Child Relationships | Belongs to coordination context storage settings and influences `c-02-memory-quality-control` skill classification.                                                                                                                                                                  |
| Often Confused With          | Storage mode; storage decides where artifacts live, path rules decide eligibility.                                                                                                                                                                    |
| Source References            | [path-rules.md](agents-remember/docs/reference/path-rules.md); [settings.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/settings.py); [json_settings.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/json_settings.py); [storage.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/storage.py) |
| Migration Notes              | Cross-repo/worktree changes should not replace path rules; they remain an eligibility layer.                                                                                                                                                          |

### Memory Quality Control

| Field                        | Value                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Category                     | Memory quality workflow                                                                                                                                                                                                                                                                                                                          |
| Represents In Reality        | `c-02-memory-quality-control` skill's active control loop for task-start drift trust, current-worktree missing-onboarding checks, closeout memory quality checks, and targeted style repair.                                                                                                                                                                                    |
| Description                  | Memory quality control uses `drift_check` at task start, `check_missing_onboarding` before code commits that add source files, and `memory_quality_check` before memory content commits. Task-start drift control separates clean-source update candidates from dirty-source active work-in-progress before `c-05-create-or-update-onboarding-files` skill handoff. Drift reports still classify onboarding units as up to date, drifted, missing verification, missing, orphaned, disabled, or unsupported and are written under the resolved temporary artifact root by default. Style findings such as update-history ordering are reported during closeout and repaired through focused scripts. Since 260731-EFA-L3 both integrity checkers read Git through the one kernel runner `kernel/git_command.run_git`: `check_missing_onboarding.py`'s own sixth copy of that function is gone, replaced by a local `require_git` that wraps the shared runner and keeps this module's contract that any non-zero exit is fatal, and `onboarding_drift_check/git_ops.py` (whose helpers `drift.py` re-exports) does the same. Because that runner strips `GIT_REPOSITORY_SELECTOR_ENV` and decodes with an explicit UTF-8 / `surrogateescape`, the "which sources did this worktree add" answer (`diff --cached`, `diff`, `ls-files --others`) and the drift and entity-fingerprint blob reads (`rev-parse HEAD:<path>` in `git_blob_hash`) now resolve against the repository the check was pointed at rather than an inherited `GIT_DIR` — a gate whose verdict is trusted can no longer be answered by a different repository. Since 260731-EFA-L4 the drift summary's own status vocabulary is declared once, as `DriftStatus = Literal["notChecked", "checked", "error"]` in `onboarding_drift_check/models.py`, beside the `DriftSummaryPacket` TypedDict that `summary.py`'s three producers now return; `models/drift.DriftSummary` (the context packet) and `models/memory.DriftCheckResponse` (the tool) both read that one declaration instead of keeping copies. The packet's copy was missing `error` — both the status and the key — while `run_drift_summary` returns exactly `{"status": "error", "error": ...}` whenever the onboarding root does not exist, so `context_packet(include_drift=true)` against a repo with no onboarding raised out of the tool on the very call meant to explain the problem. |
| Canonical Source Of Truth    | `c-02-memory-quality-control` skill docs and the `mcp/src/agents_remember/memory_quality/` package.                                                                                                                                                                                                                                                                        |
| Current Naming Drift         | This entity was previously named `Drift Report`; drift remains one integrity check inside the broader memory quality control domain.                                                                                                                                                                                                              |
| Key Identifiers              | `drift_check`, `check_missing_onboarding`, `memory_quality_check`, `history_order_fix.py`, report path, `classification`, `trust`, source path, affected sections, finding count, and closeout pass/fail state.                                                                                                                                  |
| Parent / Child Relationships | Uses the `c-08-ar-coordination-context-resolver` skill context, hands onboarding content maintenance to `c-05-create-or-update-onboarding-files` skill, and feeds `c-09-git-worktree-manager` skill closeout before memory commits.                                                                                                                                                                                                                               |
| Often Confused With          | Onboarding content itself or optional style guidance. Quality control is actionable workflow state, not passive advice.                                                                                                                                                                                                                          |
| Source References            | [`c-02-memory-quality-control` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md); [check.py](agents-remember/mcp/src/agents_remember/memory_quality/check.py); [check_missing_onboarding.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py); [drift.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py); [history_order.py](agents-remember/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |
| Migration Notes              | Worktree support should preserve `c-02-memory-quality-control` skill as quality reporting/routing, not onboarding prose writing.                                                                                                                                                                                                                                                 |

### File-Level Onboarding Content Model

| Field                        | Value                                                                                                                                                                                                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Onboarding schema                                                                                                                                                                                                                                                                                 |
| Represents In Reality        | The required section, source-discovery, and citation model for one concrete source file's onboarding unit.                                                                                                                                                                                        |
| Description                  | The model includes purpose, code commentary, docs references, repo-internal references, cross-repo references, metadata, and prepend-only update history. Docs references must start from the resolved `Domain Documentation` category, cite actual evidence rather than source registries, link canonical live references when available, record no relevant documentation only after live-source checks or blockers, and preserve still-accurate file-level knowledge across moves, splits, merges, or deletion cleanup. |
| Canonical Source Of Truth    | `c-05-create-or-update-onboarding-files` skill file-level workflow and template.                                                                                                                                                                                                                                                            |
| Current Naming Drift         | Inline onboarding reuses the same semantic content model; only storage adapter behavior differs. Local documentation mirrors are not a separate source-of-truth class; they are orientation caches when a live source is named.                                                                     |
| Key Identifiers              | Metadata table fields, required sections, `Domain Documentation`, live retrieval path/tool/MCP, canonical live reference, and `No relevant documentation found after checking live sources.`                                                                                                       |
| Parent / Child Relationships | File-level units complement repo overview and entity catalog.                                                                                                                                                                                                                                     |
| Often Confused With          | Component overviews, task-local findings, source registries as evidence, or local docs mirrors as authoritative references.                                                                                                                                                                         |
| Source References            | [file-level workflow](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) L20-L29; L47-L86; L113-L121; [file-level template](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md) L41-L49; [inline template](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md) L34-L35 |
| Migration Notes              | The content model should survive storage changes from sidecar to inline, from internal-memory roots to external-memory roots, and from old source paths to new source paths when behavior is preserved or relocated.                                                                                                                                             |

### Light Task Artifact

| Field                        | Value                                                                                                                                                                                                                                                                                       |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Workflow artifact                                                                                                                                                                                                                                                                           |
| Represents In Reality        | A durable single-file plan/checklist for medium-sized work that needs approval and continuity.                                                                                                                                                                                              |
| Description                  | `w-02-light-task-workflow` skill creates or updates one task file under the `c-08-ar-coordination-context-resolver` skill resolved task root and uses checkboxes as the live implementation tracker. When the Task Collaboration Doctrine warrants it, the file carries a `## Design` section above the implementation steps from which those steps derive. Its planning gate follows `c-02-memory-quality-control` skill clean-source versus dirty-source drift classification before relying on onboarding. Slice 3c makes the artifact JSON-primary: an `ar-task-document/v1` JSON is the source of truth and `task.md` is rendered by the `task_doc` MCP tool. The format covers `light`, `subTask`, and `master` documents (a master carries a `subTasks` series index + ordered `sections`); masters stay hand-authored markdown until the runtime ships `task_doc`.                                                                                                                                                             |
| Canonical Source Of Truth    | `w-02-light-task-workflow` skill docs, workflow, and template.                                                                                                                                                                                                                                                    |
| Current Naming Drift         | Worktree-backed tasks live beside `contract.md` in repo-scoped task folders; non-worktree `w-02-light-task-workflow` skill artifacts can still use the resolved flat task root.                                                                                                                                         |
| Key Identifiers              | `Status`, `Repo`, `Type`, `Created`, design section, implementation checklist, decision log.                                                                                                                                                                                                                |
| Parent / Child Relationships | Task artifacts can lead to onboarding updates, but they do not become onboarding content.                                                                                                                                                                                                   |
| Often Confused With          | Onboarding overview, entity catalog, and worktree contract.                                                                                                                                                                                                                                 |
| Source References            | [`w-02-light-task-workflow` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md) L25-L34; [workflow.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md) L111-L149; [template.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md) L8-L97 |
| Migration Notes              | Worktree support should keep task artifacts as planning state, not durable current-state onboarding.                                                                                                                                                                                        |

### External Memory Ledger

| Field                        | Value                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Memory compatibility artifact                                                                                                                                           |
| Represents In Reality        | The `memory.md` mapping between code commits and external memory commits.                                                                                               |
| Description                  | The helper parses and writes the fenced `json ar-memory-ledger` metadata plus newest-first code-to-memory state history. Repeated code commits are valid: a settings-only memory change creates a new memory content commit and a newer ledger row for unchanged code while preserving older exact edges as audit history. `find_mapping` returns current newest-first authority; `contains_mapping` answers exact historical containment. Journaled worktree closeout and direct landing use explicit messages and journal evidence to create memory then ledger commits; exact current edges are idempotent, while changed memory state appends history. Source-pair admission requires a newest current mapping, divergent memory resolution preserves every exact parent row, integration accepts an already-current pair or exactly one new prefix row, and organizational completion proves both current sibling authority and exact final-ledger containment. Malformed bytes, missing mappings, broken ancestry, and dropped parent history still fail closed. The durable authority is the committed Git object; there is no generated subject, blank fallback, compatibility reader, or queue-owned lifecycle evidence. |
| Canonical Source Of Truth    | `mcp/src/agents_remember/kernel/memory_ledger.py` plus mutation/proof owners in `mcp/src/agents_remember/worktrees/modules/closeout_external.py`, `mcp/src/agents_remember/worktrees/queue/closeout_recovery.py`, `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py`, `mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py`, `mcp/src/agents_remember/worktrees/integration/organizational_completion.py`, `mcp/src/agents_remember/worktrees/sync_transaction_authority.py`, and `mcp/src/agents_remember/worktrees/sync_transaction_git.py`; coordinators do not redefine the ledger format. |
| Current Naming Drift         | The parser/writer lives in the MCP package; CLI commands are now adapters around service functions. `LedgerError` now subclasses the shared `AgentsRememberError` (still a `ValueError`), so it is part of the package typed-error family rather than a bare `ValueError`.                               |
| Key Identifiers              | `schema`, `repoName`, `lastVerifiedCodeCommit`, `lastMemoryContentCommit`, table rows.                                                                                  |
| Parent / Child Relationships | Belongs to one external memory repo and is consumed by `c-09-git-worktree-manager` skill worktree lifecycle, baseline adoption, and cross-repo resolution.                                                                                  |
| Often Confused With          | Drift report or task contract.                                                                                                                                          |
| Source References            | [memory_ledger.py](agents-remember/mcp/src/agents_remember/kernel/memory_ledger.py); [closeout_external.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout_external.py); [closeout_recovery.py](agents-remember/mcp/src/agents_remember/worktrees/queue/closeout_recovery.py); [direct_landing_execution.py](agents-remember/mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py); [integration_ref_transaction.py](agents-remember/mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py); [organizational_completion.py](agents-remember/mcp/src/agents_remember/worktrees/integration/organizational_completion.py); [sync_transaction_authority.py](agents-remember/mcp/src/agents_remember/worktrees/sync_transaction_authority.py); [sync_transaction_git.py](agents-remember/mcp/src/agents_remember/worktrees/sync_transaction_git.py) |
| Migration Notes              | 260821-CLIVE-L1 moved worktree-closeout ledger mutation from `closeout.py` to `closeout_external.py` rather than keeping a compatibility path; CLIVE L2 made direct landing journaled and recoverable. The IAS source-pair repair initially introduced global per-code uniqueness, which rejected valid settings-only memory history and stranded atomic activation. This correction removes that rule at the kernel and every lifecycle consumer: current authority is newest-first, exact older edges remain audit history, and no fallback or parallel ledger implementation was added. |

`260815-DAG-L3 route impact:` queue declaration and every later lifecycle transition bind the
exact external-memory base, candidate tree, and ledger mapping as candidate evidence. The queue
does not replace or rewrite ledger authority; a changed mapping invalidates readiness and must be
reconciled through the existing closeout/integration ledger owner.

### Sprint Closeout Queue

| Field | Value |
| --- | --- |
| Category | Disposable sprint scheduling projection |
| Represents In Reality | One bounded, source-fingerprinted materialized view of the current waiting closeout-door generations that are schedulable inside a sprint. |
| Description | Each sprint projection is derived from an exact-current census of canonical task topology, waiting door generations, and source-pair activation observations. Multiple live series are valid: the one selected `active` master may expose ready candidates, a selected `reconciling` master waits on sync, and every other live series is logically paused without being retired. Its service condition is only `invalid-empty` or `valid-built`; valid members are classified `ready`, `waiting`, or `blocked` and carry deterministic priority, order, and bounded reasons. Canonical task mutation publishes without queue permission, invalidates affected projections to durable empty, rebuilds off-side without consulting old rows, and publishes only if source identity remains exact-current. The projection owns no selection, claim, worker, commit, certification, integration, cancellation, recovery, or terminal evidence. |
| Canonical Source Of Truth | `models/closeout/projection.py` defines strict projection state/member/problem/effect models; `controlplane/closeout_queue_store.py` owns invalid-empty/valid-built persistence; `worktrees/queue/closeout_projection.py`, `closeout_projection_members.py`, `closeout_projection_activation.py`, and `closeout_projection_publication.py` own exact source census, activation observation, member computation, and invalidation/rebuild publication. `models/queue/closeout_queue.py` and `worktrees/queue/closeout_queue.py` expose only sprint-scoped status/rebuild plus the short first-ready admission fence. Task/door truth is upstream, activation is a separate disposable selector, and journal truth remains separate. |
| Current Naming Drift | Public tools and dashboard projections retain the established `closeout_queue` / `closeoutQueues` labels. Here “queue” means a disposable scheduling projection, not a durable job queue or lifecycle ledger; a projected candidate is a waiting door generation, not a claimed operation. |
| Key Identifiers | Sprint `TaskDocumentRef`, projection revision, service condition, source classification/fingerprint, bounded source problems, door generation id, candidate and owning-master refs, contract path, candidate tree, source-door fingerprint, member classification, effective priority, order, and reasons. No operation generation, worker identity, commit tuple, certification, or lifecycle owner fingerprint belongs here. |
| Parent / Child Relationships | Belongs to one sprint and is rebuilt from current task, door, and activation truth. A short task/door publication CAS may require the exact first-ready generation at claim admission; after claim, the door and enclosure-external operation journal own lifecycle evidence. Task authoring remains authoritative and can invalidate/rebuild affected projections without queue or activation permission. |
| Often Confused With | The sprint task document, source-pair activation, a closeout-door generation, Judgment/Priority Registers, the operation journal, a generic durable job queue, the external-memory ledger, the landing lane, or the terminal archive. |
| Source References | `mcp/src/agents_remember/controlplane/closeout_queue_store.py`; `mcp/src/agents_remember/models/closeout/projection.py`; `mcp/src/agents_remember/models/queue/closeout_queue.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py`; `mcp/src/agents_remember/worktrees/queue/closeout_queue.py` |
| Migration Notes | Introduced by 260815-DAG and completed by 260821-CLIVE L3. The transitional selected/in-flight/certified rows, task-document queue veto, blocker/lifecycle commands, and `closeout_queue_lifecycle.py` owner were removed rather than retained behind compatibility readers. The direct IAS repair replaces single-live-series assumptions with read-only source-pair activation. Current rebuild never consumes stale rows, and lifecycle evidence survives only at its door/journal owners. |

### Closeout Effective Input

| Field | Value |
| --- | --- |
| Category | Lifecycle admission entity |
| Represents In Reality | The one accepted statement of which closeout commit legs apply and the exact explicit message for every enabled leg. |
| Description | Raw public observations are normalized once against a lease-stable route, contract, and code candidate. The result contains typed `code`, `memory`, and `ledger` legs: enabled legs carry stripped nonblank explicit messages; not-applicable legs carry reasons and no sentinel message. Worktree closeout persists this value in the lifecycle operation; entry returns it once and every preview, fingerprint, worker, code, external-memory, ledger, resume, and recovery consumer receives that exact typed value explicitly rather than rereading optional transport or creating shadow intent. Direct landing shares the contract for verified-existing code plus enabled external-memory/ledger intent, validating before its landing lock and Git. |
| Canonical Source Of Truth | `models/closeout/input.py` defines the vocabulary; `worktrees/closeout_input.py` owns plan derivation and normalization; `worktrees/integration/closeout/operation_admission.py` owns lease-stable durable admission. |
| Current Naming Drift | Public code may call the raw shape messages or commit-message input, while durable code calls the result `effectiveInput` / `EffectiveCloseoutInput`. Only the latter may cross below validation. |
| Key Identifiers | Route, resolved plan, code/memory/ledger leg state, explicit message, reason, candidate tree/HEAD/tree, invalid field observation, corrected call, candidate fingerprint. |
| Parent / Child Relationships | Created from a worktree contract and stable Git candidate; embedded in one closeout lifecycle generation; consumed by mutation evidence owners. Queue selection is neither parent nor authority. |
| Often Confused With | Optional public JSON-schema fields, blank-message defaults, generated commit subjects, queue candidate declarations, or the legacy raw `WorktreeArgs` message fields. |
| Source References | `mcp/src/agents_remember/models/closeout/input.py`; `mcp/src/agents_remember/worktrees/closeout_input.py`; `mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py`; `mcp/src/agents_remember/application/worktree_tools.py`; `mcp/src/agents_remember/worktrees/direct_landing.py` |
| Migration Notes | Introduced by 260821-CLIVE-L1 as a replacement, not a compatibility layer. Raw strings stop at admission; there is no generated ledger subject or empty enabled sentinel. CLIVE L2 implements the public task-addressed retry/recover/cancel/revise controls while preserving this input unchanged within one generation. |

### Closeout Mutation Evidence

| Field | Value |
| --- | --- |
| Category | Durable lifecycle evidence entity |
| Represents In Reality | Per-enabled-leg proof of the exact repository state before, during, and after a journaled worktree-closeout Git mutation. |
| Description | Each enabled repository leg advances through `pre-mutation`, `mutation-intent`, `reconciled-unchanged`, or `commit-proven` evidence bound to branch/ref, HEAD/tree, reflog fingerprint, index/candidate trees, and worktree status. Intent is journaled before Git; commit proof validates the exact ref/parent/tree transition. After restart, exact unchanged state is distinguished from exact expected output and from ambiguity such as a ref moving away and back. A public retry of unchanged intent preserves attempt one, does not launch implicitly, and remains cancellable; status or reflog observation failure leaves the literal journal and evidence unchanged. A cancelled generation advances only through the current contract-owned waiting door plus cancelled disposition and worker-exit proof; historical door rows remain audit evidence rather than a uniqueness authority. Commit-proven evidence derives the compatibility recovery tuple, while exact canonical contract-publication proof retains verified-existing/no-op generations without fabricated Git mutation evidence. |
| Canonical Source Of Truth | `models/lifecycles/mutation_evidence.py`, `worktrees/integration/mutation_evidence.py`, `worktrees/integration/closeout/recovery_projection.py`, and the strict lifecycle operation store. |
| Current Naming Drift | Older fields named recovery commits or irreversible boundary are retained only as derived/public projection where required; they are not evidence authorities. |
| Key Identifiers | Leg, repository, state, before/observed snapshot, expected output tree, commit proof, operation key/generation, recovery projection, finalized contract SHA-256. |
| Parent / Child Relationships | Belongs to one journaled closeout operation generation and its accepted effective input. It owns recovery projection; the queue consumes only downstream lifecycle outcomes. |
| Often Confused With | Progress phase, approval claim, irreversible boolean, queue row state, a nonblank recovery cell, or direct-landing lock ownership. |
| Source References | `mcp/src/agents_remember/models/lifecycles/mutation_evidence.py`; `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py`; `mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py`; `mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py` |
| Migration Notes | Introduced by 260821-CLIVE-L1 for journaled worktree closeout. Legacy synchronous apply and generic raw closeout start fail closed. CLIVE L2 makes direct landing journaled and crash-recoverable through its own accepted-input and ledger-intent models; that sibling operation does not reuse closeout mutation evidence as a compatibility shortcut. |

### Memory Baseline Adoption

| Field                        | Value                                                                                                                                                                                                                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | External-memory migration operation                                                                                                                                                                                                                                           |
| Represents In Reality        | The explicit one-time conversion of existing external-memory onboarding into the first ledgered `memory.md` baseline.                                                                                                                                                         |
| Description                  | `c-10-adopt-memory-baseline` skill resolves the external-memory context, runs `c-02-memory-quality-control` skill drift, reports ledger status, blocks actionable drift unless the developer accepts it, and then creates the first memory content and ledger commits through the baseline service.                                                                |
| Canonical Source Of Truth    | `c-10-adopt-memory-baseline` skill and `mcp/src/agents_remember/memory/baseline.py`.                                                                                              …37697 tokens truncated… discloses exact per-id source/state/timestamps/vendor-correlation (1..64 unique ids, epoch-checked, honest not-found) to the exact-session daemon peer over the same private socket, delegated bridge → queue → authority as the sole path. The L2E additive `operation-timeline` read follows the same delegation (paged, never bodies, epoch-checked end to end), the additive `interrupt` write crosses the same socket epoch-guarded with a bridge-stamped epoch, and the additive `assets` submit key admits only schema-validated, spool-confined, sha256-verified references. Since L4 every one of these routes declares its success and refusal bodies as strict `extra="forbid"` wire models (`serving/response_contract.py`, and `serving/conversation/response_contract.py` for the conversation half); because the handlers answer with `Response` objects, FastAPI validates none of it and `test_serving_response_conformance.py` carries the enforcement. |
| Server authority | One timeline for prompt/model/effort; atomic queued-withdraw versus dispatch; full operation refs; early terminal dominance; response bypass; 64/256 live-safe retention. L2E: the retained ledger enumerates in bounded never-bodies pages whose eviction floor is tracked at the sole pop site; the withdrawal recovery body is captured pre-tombstone at the one true transition; the idempotence digest extends over canonical asset identity only when assets ride. |
| Native adapters | Codex fresh-turn guarded write with bounded correlation; Claude sole accepted operation and shared lock; Pi fresh-state token guard and settled-plus-fresh-idle completion. No native queue is authority. |
| User recovery | Alt+Up requests exact withdrawal; unchanged drafts auto-restore by revision CAS, concurrent edits create one explicit recovery slot, and replace/keep-current/dismiss are local exact decisions. |

### Branch-Gated Cross-Repo Source

Entity inventory entry; current evidence and fingerprint are recorded above.

### Delivery Injector

Entity inventory entry; current evidence and fingerprint are recorded above.

### Harness Capability Snapshot

Entity inventory entry; current evidence and fingerprint are recorded above.

### Harness Submission Authority

Entity inventory entry; current evidence and fingerprint are recorded above.

### Provider Degradation Protocol

Entity inventory entry; current evidence and fingerprint are recorded above.

### Seat Binding Identity

The stable identity of an agent seat is exactly one canonical real task document paired with one
role. Sprint roles bind to the sprint document, a manager binds to its master document, and
worker/reviewer/curator bind to their leaf documents. A terminal/session/lifecycle id identifies the
current runtime occupant only; replacing that occupant does not change the seat or require another
agent to learn a new address. Task-document containment and role authorize parent/child resolution,
and zero or multiple qualified live occupants fail closed. Spawn ancestry remains internal
provenance and a separate diagnostic projection, never the default Chats hierarchy or public address.

`260815-DAG-L14 route impact:` sprint seats become first-class structure — the sprint
document owns `SprintSeat` rows (role/label/identity/state) and seat task documents leave the
sprint task index (existing ones stay on disk as historical records). Seat identity remains the
canonical `(taskDocumentRef, role)` pair; a seat row identity is correlatable provenance,
never an authority source.

`260815-DAG-L3 route impact:` the public queue derives its caller from this plane-owned
`(taskDocumentRef, role)` seat. Requests carry neither an actor nor lifecycle identity; manager and
orchestrator transitions fail closed when the ambient structural seat lacks the required authority.

### Seat Landing Archive

Entity inventory entry; current evidence and fingerprint are recorded above.

`No content impact:` 260815-DAG-L2 changes planning and landing authority prose in shared role
evidence, but it does not change the archive's landed status, cleanup outcome, dashboard identity,
or retention semantics.

`No content impact:` 260815-DAG-L3 adds pre-closeout scheduling and lifecycle ownership but does
not change the archive's landed result, cleanup outcome, dashboard identity, or retention rules.

`No content impact:` 260821-CLIVE-L1 changes `application/worktree_tools.py` closeout admission
from raw messages to normalized effective input. That shared evidence path changes the fingerprint,
but it does not change archive identity, landed status, cleanup outcome, or retention semantics.

### Seat Retirement

Entity inventory entry; current evidence and fingerprint are recorded above.

### Supervisor Sweep

Entity inventory entry; current evidence and fingerprint are recorded above.

`No content impact:` 260815-DAG-L3 appends one public tool name through shared MCP registry
evidence. It does not alter supervisor predicates, delivery, cooldown, heartbeat, or escalation.

### Task Document

The canonical sprint, master, and leaf JSON task documents are both planning artifacts and the
stable work-domain topology for structural seats. Sprint documents carry the canonical
`executionGraph`; master documents carry an explicit `executionNature` of `organizational` or
`atomic`. Graph-selected dependency meaning is authored in the evidence-cited judgment register:
architect owns the initial plan loop, an approved strategist may build it, and the orchestrator
adopts it for runtime frontier decisions. Since 260815-DAG-L13, a sprint without an
`executionGraph` runs the atomic-sequential default (every commanded master executes atomically,
one at a time, regardless of declared nature) instead of requiring an explicit migration, and a
nature-less standalone master resolves at master altitude by default — only an explicit
`organizational` standalone master stays a dead-end. `TaskDocumentRef` remains the repository-qualified durable address; no runtime
id or synthetic parallel identity may compete with it.

`260815-DAG-L3 route impact, superseded by 260821-CLIVE-L3:` the sprint document remains canonical
input to the closeout scheduling projection, but the projection is disposable rather than task
authority. Graph, execution-nature, register, and completion facts are read structurally. A task
mutation publishes canonical truth first, invalidates affected projections to durable empty, and
rebuilds from exact-current task and waiting-door sources; no queue state can veto task authoring.

`260815-DAG-L14 route impact:` sprint documents carry typed `SubTaskRef.masterRef` rows
and first-class `seats`; `attach_master`/`detach_master` write the typed row, membership slug, and
graph node as one atomic batch, and `validate_sprint_linkage` hard-fails new-shape drift while
legacy shapes surface as `linkageFacts`.

`260815-DAG-L12 route impact:` the sprint document's `executionGraph` is now projected into
the render-ready `executionGraphView` (`observer/projection_graph.py` builds the per-node view;
`tasks/execution_graph_titles.py` owns the shared master/leaf title join; the serving task-documents
readers wire it onto `TaskDocNode`). The mermaid document diagram and the dashboard wave-grid view
both render this projection; the frontend never joins raw refs or re-derives waves/frontier state.

`260815-DAG-L4 route impact:` topology publication now shares repository authority with Git
mutation, so execution-nature, sprint ownership, and protected-surface edits cannot strand a live
leaf or contradict an active atomic series.

`260821-CLIVE route impact:` task writers capture exact JSON/Markdown source snapshots and recheck
the entire selected/affected set under the short publication lock before one atomic publication.
After publication they invalidate affected scheduling projections and rebuild from current truth;
the queue is a downstream projection and cannot refuse otherwise-valid task mutation.

### Source Lineage

| Field | Value |
| --- | --- |
| Category | Structural admission entity |
| Represents In Reality | The Git ancestry admitted for one sprint execution node: `super → leaf` for an organizational master and `super → master → leaf` for an atomic master. |
| Description | The plane resolves a canonical task document to its exact organizational or atomic contract edge, proves every applicable code and external-memory parent relation, and reduces Git facts to a strict current/blocked/unavailable projection. Stale or unprovable ancestry fails closed before checkout exposure or lifecycle mutation. Closeout and integration recheck the task-derived edge after quality and at the last reversible boundary; repository-global branch authority separately prevents the same named ref from being used as an ordinary workbench. |
| Canonical Source Of Truth | `worktrees/source_lineage.py` over canonical task documents, enclosure contracts, and repository branch facts. |
| Current Naming Drift | Status payloads use `source_lineage`; strict public/dashboard projections use `sourceLineage`. Both represent the same entity. Remote stale-base freshness is a separate later policy. |
| Key Identifiers | Canonical task document, `executionNature`, relation (`super-to-leaf`, `super-to-master`, or `master-to-leaf`), side (`code` / `memory`), Git common-directory identity, canonical local branch, and owning contract path. Checkout paths, commits, and runtime ids remain evidence rather than agent-supplied addresses. |
| Parent / Child Relationships | Organizational managers own direct sprint-super leaves without a series contract. Atomic managers own one series ref and their leaves descend from it; the complete leaf pair chain is sealed before the series can close. |
| Often Confused With | Remote tracking freshness, seat binding identity, a remembered base commit, or a new replacement master. |
| Source References | `mcp/src/agents_remember/worktrees/source_lineage.py`; `mcp/src/agents_remember/worktrees/modules/closeout.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py`; `mcp/src/agents_remember/models/worktree.py`; `mcp/src/agents_remember/serving/terminal_opener.py`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-brief.md`; `dashboard/src/panels/engine-room/DiagnosticsPanel.tsx` |
| Migration Notes | L4 completed the nature-aware mechanical cutover across start, lineage projection, closeout, integration, and dashboard schema. The retired universal-master-branch workflow must not be reintroduced as compatibility behavior. |

`260815-DAG-L3 route impact, current ownership corrected by CLIVE:` waiting-door scheduling and the
irreversible integration seam both recheck canonical transitive lineage, but claims and
certification are journal-owned rather than queue-owned. A candidate whose relevant source edge
changes leaves the rebuilt ready frontier before any ref movement.

`260821-CLIVE-L1 route impact:` closeout admission now binds a lease-stable candidate snapshot and
normalized effective input before observing lifecycle compatibility. Source-lineage validation
still owns ancestry; it neither derives message enabledness nor delegates that authority to the
queue. The response model change makes typed closeout refusal visible without changing lineage
topology.

`Direct IAS source-pair coordination impact:` atomic start, attach, and implementation dispatch
admit work only after the selected master has reconciled against the exact current code and memory
sources. Switching selection logically pauses the previous master; it does not rewrite lineage or
retire that master's contracts, worktrees, tasks, chats, or journals.

### Worktree Contract

Entity inventory entry; current evidence and fingerprint are recorded above.

`260815-DAG-L3 route impact, current ownership corrected by CLIVE:` the contract supplies exact
repository/worktree/base/memory-mode facts referenced by a waiting-door projection member. The
projection stores only disposable source identity and never becomes a second contract; closeout and
integration still own contract publication.

`260815-DAG-L4 route impact:` configured coordination/task roots, code and memory Git identities,
memory mode, canonical branch spelling, candidate commits, door/series source identity, and exact
caller-selected contract path are immutable lifecycle authority. A copied, moved, rebound, or
topology-inconsistent contract fails before recovery or protected mutation.

`260821-CLIVE-L1 route impact:` `contract_publication_text` is now the sole normalize, validate,
and serialize owner used by `write_contract`, closeout finalization identity, and organizational
completion reset identity. Exact publication proof may retain a verified-existing/no-op closeout
generation; it does not fabricate Git mutation evidence. Candidate/plan enabledness is derived
from the contract plus stable Git facts before lifecycle compatibility.

`260821-CLIVE-L2 route impact:` new enclosures publish an immutable root manifest and locked
address-only locator before normal lifecycle admission. Normal lookup is strictly locator → root
manifest → canonical root journal, so task/contract loss cannot erase operation controls. Existing
readable pre-locator enclosures use one explicit audited adoption route; schema-1 record repair is
a separate bounded bridge, not a fallback reader.

`Direct IAS source-pair coordination impact:` the contract remains the public durable address for
sync, while `.lifecycle/sync-operation.json` at the enclosure root owns resumable transaction state
independently of task-document readability. Conflict worktrees under `.sync/` and pinned
`refs/agents-remember/sync/<digest>/...` are operation evidence, not contract fields, queue rows, or
fallback lookup surfaces.

### Worktree Integration

Entity inventory entry; current evidence and fingerprint are recorded above.

`260815-DAG-L3 route impact:` a graph-managed leaf must be selected, closeout-certified, and still
current before integration claims the lane. The final source move revalidates the same candidate
facts under queue/task locks, consumes the candidate on success, and releases recoverable
pre-boundary failures through the task-addressed lifecycle rather than a public operation key.

`260815-DAG-L4 route impact:` integration is now a cross-operation-leased, journal-bound named-ref
transaction. Exact expected-old CAS, external-memory ledger/content ancestry, pair rollback and
recovery, checkout refresh, task-topology revalidation, and contract-before-lane-release ordering
replace ambient checkout merges and unowned helper mutation.

`260821-CLIVE-L1 route impact:` cleanup's changed evidence path only migrates from the old
lease-with-census API to a pure serialization lease plus explicit compatibility check. Integration
transaction semantics are otherwise unchanged; closeout mutation evidence is a separate journal
entity and no queue lifecycle compatibility fallback is added.

`260821-CLIVE-L2 route impact:` integration claim transfer snapshots and consumes the exact
transitional certified candidate once, publishes claim evidence in the root journal, and never
depends on a surviving queue row for later protected-ref publication or recovery. Moved/missing/
unreadable refs remain same-generation journal decisions. The remaining queue lifecycle schema is
transitional until L3; terminal archive/readback ordering before destructive cleanup remains L5.

`Direct IAS source-pair coordination impact:` cleanup, finalize, and abandon release activation
only when the terminal contract is still the exact selected master for its normalized source pair.
A paused or stale contract cannot clear a newer selection. Cancellation rolls back both sync sides
from pinned pre-sync refs and durably publishes `vacant`; integration does not acquire selector or
queue lifecycle ownership.

## Ownership Notes

- This catalog intentionally excludes the eight worktree task files as onboarding subjects.
- This catalog treats `mcp/src/agents_remember/package_data/runtime/agents-md-files/` as the package source for runtime `AGENTS.md` templates. Memory repos use `system/*` guidance files rather than root-level `AGENTS.md` files.
- Roadmap specs are cataloged only where they define active current design concepts that explain the repository's direction.
- Legacy roadmap specs remain historical context where they disagree with the implemented memory/coordination split.

## Update History

- 2026-08-26T19:27+02:00 — Reconciled Closeout Mutation Evidence after the IAS successor repair:
  the current waiting door, cancelled journal disposition, and worker-exit proof authorize
  replacement; publication history remains audit rather than uniqueness authority. Recomputed its
  `git-blob-set-v1` fingerprint against committed code `c51373425be3e3f488590ad2f444810df89b4ffb`.

- 2026-08-26T16:03+02:00 — Memory hygiene: removed a pre-existing tool-output truncation banner
  accidentally committed above the document title; entity content is unchanged.

- 2026-08-26T14:32+02:00 — Corrected the External Memory Ledger entity after the activation
  regression: repeated code commits are valid ordered memory state, newest lookup is current
  authority, and exact older edges remain audit history. Fingerprint refresh remains post-code-commit.


- 2026-08-26T08:40+02:00 — Reconciled the affected queue, ledger, lineage, contract, and
  integration entities to the frozen IAS source-pair activation/sync candidate. Real-commit
  fingerprints remain closeout-owned for the new uncommitted source owners.

- 2026-08-25T08:27+02:00 — 260824-PDLS wave 004: reviewed the nine drifted entity evidence sets against emergency-landed code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`, repaired closeout package paths, and refreshed their deterministic fingerprints. The entity meanings remain current; the mapping records onboarding provenance and does not certify the red Dagger result.

- 2026-08-24T16:00+02:00 — Final cumulative closeout audit: corrected the live Task
  Document, Source Lineage, and Worktree Contract narratives so disposable scheduling is downstream
  of task/door truth and claims/certification remain journal-owned.

- 2026-08-24T15:41+02:00 — 260821-CLIVE final entity reconciliation: replaced the stale
  transitional Sprint Closeout Queue entry with the implemented disposable-projection contract;
  removed deleted `closeout_queue_lifecycle.py` and selected the seven current model, store,
  census, member, publication, and facade owners as its evidence set. The fingerprint digest and
  catalog verification metadata remain architect-owned for mechanical refresh. Timestamp is the
  curator host's Europe/Berlin system time.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: repointed the Closeout Effective Input and Closeout Mutation Evidence inventory/fingerprint evidence to canonical nested source routes and recomputed both `git-blob-set-v1` values against code commit `1d446724d099517f6f52d596b47827ae2391a2a4`; entity ownership is unchanged.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2 curator: reconciled External Memory Ledger, Sprint
  Closeout Queue, Closeout Effective Input, Closeout Mutation Evidence, Task Document, Worktree
  Contract, and Worktree Integration. The catalog now distinguishes landed L2 root-journal,
  locator/manifest, worker/direct-landing, claim-transfer, and exact task-source transaction facts
  from the still-present pre-L3 queue lifecycle/task-publication schema. No new catalog entity was
  invented: these changes extend existing reusable entities. Evidence paths are unchanged; their
  deterministic fingerprints and catalog verification stamp remain pinned until architect-owned
  closeout can recompute them from the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 curator: added `Closeout Effective Input` and
  `Closeout Mutation Evidence`; reconciled External Memory Ledger, Sprint Closeout Queue,
  Worktree Contract, Source Lineage, Worktree Integration, and Seat Landing Archive boundaries.
  Candidate-11 rebinding is test-only and therefore has no entity-evidence path or fingerprint
  impact. The unchanged production fingerprints still match frozen tree `4241908c`: effective input (`sha256:9e5e9365…`), mutation evidence
  (`sha256:23921c56…`), ledger (`sha256:ea59b460…`), contract (`sha256:99a15991…`), lineage
  (`sha256:10523264…`), queue (`sha256:6d356bdc…`), integration (`sha256:53bbd3b8…`), and archive
  (`sha256:a8bf13d1…`). Verification metadata remains pinned
  until governed closeout stamps the landed code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair curator: recomputed the drifted
  `git-blob-set-v1` fingerprints at code commit `e5cb139f` — External Memory Ledger
  (`sha256:f3dca290…`), Sprint Closeout Queue (`sha256:6d356bdc…`), Memory Baseline Adoption
  (`sha256:f7f1696e…`), Worktree Contract (`sha256:0b20fa32…`), Source Lineage
  (`sha256:b005744f…`), Worktree Integration (`sha256:481d402d…`), and Seat Landing Archive
  (`sha256:41d9c800…`) — because their evidence changed under the repair (`modules/closeout.py`
  and `modules/integrate.py` refactors, `memory/baseline.py`, `application/worktree_tools.py`).
  Sprint Closeout Queue evidence paths updated to the moved package locations
  (`models/queue/closeout_queue.py`, `worktrees/queue/closeout_queue.py`,
  `worktrees/queue/closeout_queue_lifecycle.py`).


- 2026-08-20T21:30+02:00 — 260815-DAG-L15 curator: recomputed the drifted `git-blob-set-v1`
  fingerprints at code commit `de3a0fd9` — Seat Binding Identity
  (`sha256:dd86dfc7…`), Seat Landing Archive (`sha256:019de72c…`), and Task Document
  (`sha256:58850cfa…`) — because their evidence changed under L15: `tasks/document_refs.py`
  gained the shared atomic node-kind rule, and the lifecycle doctrine copies
  (`roles/orchestrator.md`, `templates/manager-brief.md`) carried the review-doctrine repair.
  Evidence path sets unchanged; prose verified current.


- 2026-08-20T10:45+02:00 — 260815-DAG-L12 curator: recomputed the Task Document `git-blob-set-v1`
  fingerprint at code commit `b7f2c8e2` (`sha256:3dc16924…`); evidence gains the two new
  load-bearing projection files (`observer/projection_graph.py` — the primitives-only render-ready
  graph-view builder; `tasks/execution_graph_titles.py` — the shared title join). Prose gains the
  L12 render-ready-view note.

- 2026-08-20T09:35+02:00 — 260815-DAG-L16 curator: recomputed the drifted `git-blob-set-v1`
  fingerprints at code commit `a9d50e08` — Sprint Closeout Queue (`sha256:d5cbe8e2…`;
  `models/closeout_queue.py` + `worktrees/closeout_queue.py` carry the declared-caller field and
  the L16 R9 declaration refusals) and Supervisor Sweep (`sha256:2c76b810…`;
  `mcp/tools/base.py` now advertises `direct_landing`, 59 public tools). Seat Binding Identity
  evidence gains `models/declared_caller.py` (the request-carried ambient identity — L16-R2/R3)
  and its fingerprint recomputed (`sha256:1aaeb262…`).


- 2026-08-20T05:16+02:00 — 260815-DAG-L14 curator: recomputed the three drifted
  `git-blob-set-v1` fingerprints at code commit `8071a644` — Seat Binding Identity
  (`sha256:ef9cab6b…`), Seat Landing Archive (`sha256:35bf9ca4…`), and Task Document
  (`sha256:1d21b82a…`; evidence includes the L14-touched `observer/projection.py`,
  `tasks/document_refs.py`, and dashboard task files). Evidence path sets are unchanged. Seat
  Binding Identity prose gains the first-class-sprint-seats note (seat rows are structure, not
  seat task documents); Task Document prose gains the typed `masterRef` + atomic
  `attach_master`/`detach_master` note.


- 2026-08-19T22:32+02:00 — 260815-DAG-L13 curator: recomputed the eight drifted
  `git-blob-set-v1` fingerprints at code commit `b523f53b` — External Memory Ledger, Seat Binding
  Identity, Seat Landing Archive, Source Lineage, Sprint Closeout Queue, Task Document, Worktree
  Contract, Worktree Integration (each evidence set includes L13-touched files; the reproduction
  was validated by recomputing the unchanged Coordination Context row to its catalogued value
  first). Evidence path sets are unchanged. Sprint Closeout Queue prose gains the degraded
  readout/lane-narrowing/blocker-module note; Task Document prose replaces the explicit-migration
  sentence with the atomic-sequential default and nature-less standalone resolution.

- 2026-08-19T04:20+02:00 — 260815-DAG-L10 curator: the leaf changed the **Worktree Contract** and
  **Worktree Integration** evidence files (`worktrees/worktree_contract.py` and
  `worktrees/modules/cleanup.py`); both `git-blob-set-v1` fingerprints remain stamped at the
  pre-L10 base `e41ea31d` while the leaf code is uncommitted in the worktree, and the closeout
  refresh owns restamping them at the new code commit. Entity prose and evidence path sets are
  unchanged.

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-15T23:38+02:00 — 260815-DAG-L4: reconciled Task Document, Source Lineage, Worktree
  Contract, and Worktree Integration with task-derived organizational/atomic authority, exact
  named-ref transactions, configured identity, and atomic series sealing. Entity fingerprint
  restamping remains closeout-owned.

- 2026-08-15T09:36+02:00 — 260815-DAG-L3 fast-hook repair: clarified that Task Document identity
  bounds are runtime validators after normalization, preserving bounded durable input without an
  untruthful generated TypeScript length type. Fingerprint restamping remains closeout-owned.
- 2026-08-15T09:32+02:00 — 260815-DAG-L3 curator: added Sprint Closeout Queue as the durable,
  bounded materialized view of mechanically eligible leaf closeouts; recorded exact judgment/task
  authority boundaries and its closeout/integration lifecycle. Reconciled related ledger, seat,
  task-document, lineage, contract, and integration entities; Seat Landing Archive and Supervisor
  Sweep were reviewed as no-content-impact. Existing drifted fingerprints and the provisional new
  row remain governed-closeout-owned for recomputation against the real code commit.
- 2026-08-15T04:32+02:00 — 260815-DAG-L2: Task Document now records the canonical execution graph,
  explicit master nature, and attributed planning authority. Source Lineage now distinguishes the
  ruled organizational/atomic target from the still-current universal mechanical chain so later
  cutover leaves cannot mistake doctrine for enforcement. No content impact to Seat Landing
  Archive; fingerprints remain closeout-owned.
- 2026-08-13T14:32+02:00 — No content impact: the manager/orchestrator/brief quality-guidance
  changes assign acceptance to Dagger and do not change Seat Landing Archive or Source Lineage
  identity, evidence topology, or lifecycle semantics. Fingerprints remain closeout-owned.

- 2026-08-13T09:27+02:00 — L23 curator: clarified that Source Lineage compares repository identity
  through Git's resolved common directory, so sibling linked worktrees do not become false
  cross-repository mismatches. Final entity fingerprint remains closeout-owned.

- 2026-08-13T09:02+02:00 — 260731-EFA-L23 curator follow-up: expanded Source Lineage from start/resume admission to the enforced pre-curator, closeout, and integration boundaries. The catalog now records transitive rechecks after long quality work, the final pre-claim/pre-merge check, and exact source-tip pinning across integration. Its evidence path set now includes the manager/curator dispatch doctrine and closeout/integration enforcement; the existing fingerprint remains deliberately pinned to the committed base for governed closeout recomputation after the dirty source delta is committed.

- 2026-08-12T20:20+02:00 — 260731-EFA-L23 curator: added Source Lineage as a cross-layer structural admission entity and clarified Task Document as its identity source. The fingerprint was computed over the exact current worktree blobs because `source_lineage.py` is new and cannot resolve through `HEAD:<path>` until closeout commits it; governed closeout must recompute the same `git-blob-set-v1` row from the real code commit. Existing Worktree Contract, Seat Binding Identity, and Task Document rows whose evidence changed remain pinned for closeout recomputation; no verification stamp was fabricated.

- 2026-08-12T07:10+02:00 — No content impact: 260731-EFA-L24 changes
  full-gate resource policy inside shared evidence files but does not change the
  External Memory Ledger, Seat Landing Archive, Supervisor Sweep, Worktree
  Contract, or Worktree Integration identities or lifecycle semantics. Their
  `git-blob-set-v1` fingerprints remain pinned for closeout recomputation against
  the real L24 commit.

- 2026-08-11T06:47+02:00 — Seat Binding Identity moved from `(leafKey, seatRole)` to canonical `(taskDocumentRef, role)` at sprint/master/leaf altitude. The evidence now follows real task topology, ambient/structural resolution, generalized task assignment, and the task-projected dashboard. Task Document now records its topology-authority role. Fingerprints remain pinned until governed closeout can derive them from the eventual code commit.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: re-pointed moved entity evidence paths
  (provider-degradation settings, inbox backoff, task-document snapshots reader, terminal-catalog
  row vocabulary) and recorded the L9 clarifications; fingerprint hashes remain pinned for
  closeout recomputation. Verification metadata pinned until closeout stamps the L9 code commit.
- 2026-08-07T08:19Z — 260731-EFA-L8 curator: re-pointed the Task Document entity's evidence path from dashboard/src/panels/DetailPanel.tsx to the detail-panel/ canonical entry after the L8 responsibility split; the fingerprint hash itself is not hand-edited and closeout must recompute it against the landed code commit. Seat Binding Identity and Harness Submission Authority fingerprints will also change because their evidence sources (sessions.ts, LeafAttachPicker.tsx, submissionLifecycleClient.ts, submitClient.ts) changed, and closeout recomputes those rows.

- 2026-08-04T15:29:35+02:00 — 260731-EFA-L6 S18-B11 same-reviewer residual correction: rebound the generated projection mirror, canonical schema, and sync/check behavior to packet-specified source spans. Verification metadata unchanged.

- 2026-08-02T01:42+02:00 — 260731-EFA-L6: the class-split work deleted `serving/harness_control_queue.py`, which invalidated the declared evidence path set of TWO more entities — **Harness Capability Snapshot** and **Harness Submission Authority** both listed it. The dead path is removed from both; no replacement was substituted for it, because the facade owned no behavior. **Harness Submission Authority** additionally gains `mcp/src/agents_remember/serving/harness_submission_ledger.py`, the module `OperationRecord` and `SubmissionLedger` (records, retention, eviction, the paged `operation_timeline`) were split into — real evidence for this entity that did not exist when the row was written. The `Harness Capability Snapshot` prose pointer at the deleted file was dropped. Both fingerprints are pinned to the committed base and must be recomputed after the L6 code commit; all 21 rows were re-checked afterwards and every declared evidence path resolves.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: the rename of `mcp/src/agents_remember/controllers/` to `application/` (plus `worktrees/status.py` to `application/worktree_status.py`) invalidated the declared evidence path set of exactly ONE entity. **Seat Landing Archive** listed `mcp/src/agents_remember/controllers/worktree_tools.py`; that path no longer exists, so its `git-blob-set-v1` fingerprint is currently computed over a set that cannot be resolved. The declaration is corrected to `mcp/src/agents_remember/application/worktree_tools.py` and its three prose references (`Canonical Source Of Truth`, `Parent / Child Relationships`, `Source References`) follow. The fingerprint hash itself is NOT hand-edited: `git-blob-set-v1` sorts the evidence paths, resolves each `HEAD:<path>` blob, and hashes the `path + blob_hash` list, so it cannot be derived by inspection and it cannot be computed at all until the rename is committed — at the current code `HEAD` (`a714114`) the new path does not resolve. Closeout must restamp it; `worktree_closeout_preview`/`worktree_closeout_apply` raise the recompute requirement (the `ENTITY_FINGERPRINT_ALGORITHM` gate in `worktrees/modules/onboarding.py` lists every entity whose evidence paths changed), and `drift_check`/`memory_quality_check` are what detect a row left stale. Two further entities cite the renamed package only in prose and needed no path-set change: **Provider Degradation Protocol** (`application/provider_tools.py` teardown path) and **Worktree Contract**/**Worktree Integration** (vocabulary only). All 21 fingerprint rows were re-checked against the code worktree afterwards; every declared evidence path now resolves. Fingerprints remain pinned to the committed base and must be recomputed after the L6 code commit.
- 2026-08-01T19:25+02:00 — 260731-EFA-L5 correction pass (three claims in the L5 clarifications section, found by a curator working an adjacent lane). **(a)** "each store carries two deliberate read policies" was the false blanket this leaf corrected elsewhere: only `GateStore` and `ExpectationRowStore` carry both readers; `OperatorInboxStore` is strict only and the other three are tolerant only, rewriting from that tolerant read and dropping an unparseable row permanently. Restated as the rule the contract actually makes — every rewrite of an AUTHORITY-BEARING log reads strictly. **(b)** The claim that `durable_store.py`'s opening "summarizes '7-18% record loss'" is **stale**: that text was replaced earlier in this leaf with the per-store figures, and no `7-18` string exists anywhere in the code tree (the only match is an unrelated 2026-07-18 timestamp). The sentence noting the two were "not obviously the same measurement" went with it. **(c)** "0 lost across 10 runs of all three scenarios" overstated coverage on two axes; `MultiProcessDurabilityTests` asserts `lost == 0` in all three scenarios but over FIVE stores in `forced_unlink` (attention dismissals has no `append` and is excluded by construction), and the torn/raised zeros only in `stress`. Added the one base-commit fact a reader can actually check — `HarnessSensitivityTests` extracts the base commit with `git archive` at test time — and stated once that no base-commit measurement artifact is committed, so every rate is quoted on the source's authority. Verification metadata pinned until closeout stamps the L5 commit.
- 2026-08-01T13:20+02:00 — 260731-EFA-L5 curator. Added the `260731-EFA-L5 Entity Clarifications`
  section and updated five entity entries. **Method, since the verdict is not readable off the file
  list:** intersected every entity's `Evidence Paths` against the leaf's 25-file changed set, then
  read the hunks in each hit to decide moved vs re-signed. Five entities intersect —
  **External Memory Ledger, Worktree Contract, Provider Degradation Protocol, Supervisor Sweep,
  Task Document** — and **three moved, two were only re-signed**. Moved: *Worktree Contract*
  (`series-contract.md` front matter gained `schemaVersion`, and `load_contract` gained a
  document-level unknown-major refusal that reuses the durable-store version policy rather than
  declaring a second one); *External Memory Ledger* (behaviour byte-identical, but R12 turned the
  unguarded whole-file write from an unexamined omission into a decided property resting on a new
  caller obligation — write and commit in the same function); *Supervisor Sweep* (its cooldown log
  went from unlocked to locked across read and rewrite, and its inbox store became the leaf's one
  declared exception to single-owner compaction). Re-signed only: *Provider Degradation Protocol*
  (`operator_inbox_records.py` moved solely in the record base class; detector, state machine,
  thresholds, failsafe and role/kind literals untouched — the same call the HFX2-L1 note above
  already made) and *Task Document* (`snapshots.py` changed, but in `read_gates` and
  `read_expectation_rows`; every task-document reader is byte-identical, verified hunk by hunk).

  **Recorded three declarations that now live outside their entity's evidence set**, rather than
  silently extending any evidence set — that changes what `git-blob-set-v1` hashes and is a
  deliberate decision, not a curator's: Worktree Contract's version policy (in
  `controlplane/durable_store.py`), Supervisor Sweep's compaction-ownership declarations (same
  file), and two of External Memory Ledger's six write-and-commit call sites
  (`worktrees/modules/start.py`, `memory/carryover.py`). None of these will ever surface as a stale
  fingerprint row, which is why they are in prose. Also recorded, and left open for the manager and
  the `controlplane/` curator: the whole `ar-durable-store/1.0` contract belongs to no entity —
  checked against every `Evidence Paths` cell, nine `controlplane/` modules including the gate store
  appear in none of them.

  **Corrected one stale entry this leaf did not cause.** Supervisor Sweep's Migration Notes carried
  a "Known HFX2-L11 deferral: `supervisor_signals.py` is an unbounded append-only log with no
  compactor yet". `AgentNotifierSignalCooldownStore.compact` exists at the leaf's base commit
  cit:([`AgentNotifierSignalCooldownStore`], mcp/src/agents_remember/controlplane/agent_notifier_signals.py:68-215) and `serving/supervisor.py` calls it once per sweep cit:([`run_agent_notifier_sweep`], mcp/src/agents_remember/serving/agent_notifier.py:95-182), returning the folded snapshot every `in_cooldown` check
  then reads in memory. The note was false before L5; L5 only added the lock around that
  read-filter-rewrite.

  **No fingerprint hash and no evidence path was hand-edited**, and none could be: `git-blob-set-v1`
  resolves `HEAD:<path>` and this leaf's code is uncommitted. The five stale rows are named in the
  section for closeout to recompute. Verification metadata pinned.
- 2026-08-01T10:50+02:00 — 260731-EFA-L4 curator, **three corrections to this register, all
  re-derived from the working tree**. (1) *The TypeScript partition.* The `260731-EFA-L4 Entity
  Clarifications` section said "The TypeScript mirror has **not** adopted that partition; it still
  keeps `LIFECYCLE_STATES` and `TERMINAL_STATES` as two lists that can disagree." A worker landed the
  partition in `dashboard/src/types/projection.ts` after that was written: the halves are written out
  (`LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, and `ACTIVE_STATES`) cit:([`LIVE_STATES`, `TERMINAL_STATES`, `LIFECYCLE_STATES`, `ACTIVE_STATES`], dashboard/src/types/projection.ts:9-9; dashboard/src/types/projection.ts:11-11; dashboard/src/types/projection.ts:13-13; dashboard/src/types/projection.ts:21-21) with no `Exclude<>` anywhere. Replaced with the current fact
  *plus its honest limit*, verified here by mutation rather than taken on report: double-filing
  `"completed"` onto `LIVE_STATES` fails with `error TS2344: Type '"completed"' does not satisfy the
  constraint 'never'`, while a duplicate *within* one half (`["running", "running", …]`) compiles
  clean — `Literal` collapses it in Python, a tuple does not — and is caught only at runtime, where
  it fails three assertions in `dashboard/src/test/contract.test.ts` (3 failed / 12 passed).
  `projection.py`'s "STATE OF THE MIRROR" comment now records the same reading. (2) *The response
  contract, which this file contradicted itself about 250 lines apart.* The body said "59 of the 61
  routes return a `Response` subclass **or feed an `EventSourceResponse`**" (right) while the 09:33
  history entry said "59 of 61 routes return a `Response`" (wrong —
  it collapses the SSE pair into the `Response` count and implies all 59 are the same shape). Both
  now state the verified split, which `serving/response_contract.py`'s own docstring and
  `mcp/tests/test_serving_response_conformance.py` carry: **57** handlers return a `Response`
  subclass, **2** are SSE async generators (`GET /api/stream`, `GET /api/events`) = **59** on which
  `response_model` validates nothing, and the remaining **2** (`GET /api/terminal/sessions`,
  `GET /api/harnesses`) return a bare dict and *are* validated by FastAPI. Also tightened "declares a
  strict `extra="forbid"` model for **every route** the serving app registers" to **every HTTP
  route** — the websocket `WS /api/terminal/{session}` has none, which the same paragraph already
  said twelve lines later. (3) *The fixture-provenance chain.* The dashboard-mirror paragraph named
  the unheld link as "the mirror↔server link", which is the composed claim rather than the link, and
  described `contract.test.ts` as a one-way measurement. Restated as four nodes and three links
  (`wire.ts` →A→ `projection.ts` →B→ `snapshot.json` →C→ `projection.py`), with link B's three
  directions named and link C identified as the one held by nothing; added the one-letter trap
  (`mirror ⊆ served` is enforced, `mirror ⊆ server` is not) and re-stated the no-generator negative
  at the strength the evidence supports — **no in-repo generator and no in-repo mechanism keeping the
  two sides in step**, which cannot exclude a generator outside this repository. No fingerprint hash,
  no evidence path, and no verification-metadata cell was touched; the eleven stale rows recorded
  below still await closeout.
- 2026-08-01T09:33+02:00 — 260731-EFA-L4 curator: derived the moved set from the diff by intersecting
  every entity's evidence paths with the leaf's 149 changed files, then reading each hit. Eleven
  entities have a changed evidence blob (Memory Quality Control, External Memory Ledger, Worktree
  Contract, Worktree Integration, Seat Retirement, Seat Landing Archive, Supervisor Sweep, Task
  Document, Delivery Injector, Harness Capability Snapshot, Harness Submission Authority); nine of
  those moved in substance and were edited, while **External Memory Ledger** and **Delivery
  Injector** were only re-signed by neighbours and are recorded as such. A twelfth, **Coordination
  Context**, moved *without* its fingerprint moving — `kernel/coordination_context/models.py` is not
  in its evidence set, and that is where `memory_mode` became the worktree contract's `MemoryMode`
  alias. Checked and found unmoved: Onboarding Unit, Runtime AGENTS Template Package, Path Rule,
  File-Level Onboarding Content Model, Light Task Artifact, Memory Baseline Adoption, Branch-Gated
  Cross-Repo Source, Provider Degradation Protocol, Seat Binding Identity — none of their evidence
  files is in the diff, and the near misses were checked by hand
  (`observer/worktree_provider_admission.py` is not degradation-protocol evidence and its one
  changed line replaces an inline literal set with the module's existing
  `ARCHIVED_CLEANUP_STATES`; `models/terminal.LeafAssignmentStatus` folds in `worktrees.leaf_refs.LeafRefStatus`,
  and because `Literal` flattens nested aliases the published attach vocabulary is byte-identical).
  Corrected the **Worktree Contract** claim that closeout's quality wrapper runs "before any
  mutation" and "gate failure preserves every one of those states": where the gate runs it now
  stages the whole task worktree first, that index write is a mutation, and it is deliberately not
  undone on refusal — the entry, its Parent / Child row and its `Closeout quality gate` projection
  row all say so, including why the two refusals must precede the `git reset`. Recorded the contract
  reader's new totality and the exact write-boundary (a hand-edited contract still loads, degraded
  and quarantined), the `ContractCells`/`amend_contract` replacement for `dataclasses.replace`, the
  six reconciled wire vocabularies, and the one genuine response change (`nextTool`/`nextArgs`/
  `nextRequiredArgs` omitted rather than filled). Added a `260731-EFA-L4 Entity Clarifications`
  section, which also states plainly that the new HTTP `response_model` declarations are a contract
  and not an enforcement (of the 61 HTTP routes, 57 return a `Response` subclass and two more are
  SSE async generators feeding an `EventSourceResponse` — 59 on which FastAPI serializes nothing and
  so validates nothing; the remaining two, `GET /api/terminal/sessions` and `GET /api/harnesses`,
  return a bare dict and *are* validated by FastAPI; the conformance suite is what holds the 59) and
  that `dashboard/src/fixtures/snapshot.json` is
  hand-maintained with **no generator**, so the mirror↔server link is unchecked
  **[Sharpened 2026-08-01T10:50 — read "no generator *in this repository*"; and the unheld link is
  `snapshot.json` against `projection.py`, not "mirror↔server", which is the composed claim. The
  section body now states both precisely.]**. Repaired seven
  citations in **Harness Capability Snapshot**, two of which were out of bounds. Recorded, as a
  dated verification note under **Delivery Injector**, that `serving/injector.py` and
  `serving/harness_adapters.py` have no importer under `mcp/src/` at all — drift that predates this
  leaf and that no fingerprint could flag, because the modules that took delivery over are not in
  that entity's evidence set. No fingerprint hash and no evidence path was hand-edited: this leaf's
  code is uncommitted and `git-blob-set-v1` resolves `HEAD:<path>`, so closeout must recompute all
  eleven stale rows against the landed commit. Verification metadata pinned until closeout stamps
  the commit.
- 2026-07-31T20:58+02:00 — 260731-EFA-L3 curator: reviewed the six entities whose evidence this leaf
  touched, after six private `run_git`/`_run_git` copies were consolidated onto the single owner
  `kernel/git_command.run_git` (strips the eight `GIT_REPOSITORY_SELECTOR_ENV` variables via
  `git_environment()`; `GIT_LOCAL_TIMEOUT_SECONDS = 300` / `GIT_REMOTE_TIMEOUT_SECONDS = 120` /
  `GIT_METADATA_TIMEOUT_SECONDS = 30` replace the hard-coded `timeout=5`). Three entries were
  understated and were corrected. **External Memory Ledger**: writing `memory.md` is plain I/O, but
  *publishing* a row is a commit (`closeout.py` and `integrate.replay_memory_content` via
  `require_git` / `commit_if_dirty`) that ran through an unguarded copy, so an exported `GIT_DIR`
  could put the compatibility record in another repository; the Description now records that the
  commit is guarded. **Worktree Integration**: this phase's mutations — the code `rebase`, the memory
  `checkout -b` + `rebase --onto` replay, both `merge --ff-only` landings and the two rollback
  `reset --hard` calls in `_merge_integrated_commits` — had neither the environment guard nor any
  timeout, so the entry's "all-or-nothing" claim never said *which* repositories it held for; also
  recorded that cleanup's `ls-remote --heads` and `push origin --delete` now run under
  `cleanup._remote_git` at 120s and report a stall as the already-defined `remote-unreachable` reason
  instead of holding an uncancellable MCP tool call open. **Memory Quality Control**:
  `check_missing_onboarding.py`'s private copy became a `require_git` wrapper over the shared runner
  (non-zero exit still fatal), so the added-sources scan (`diff --cached`, `diff`, `ls-files
  --others`) and the drift / entity-fingerprint blob reads (`rev-parse HEAD:<path>` in
  `git_blob_hash`) can no longer be answered by an inherited `GIT_DIR`. Three entries were left
  unchanged because their diff is a pure import repoint that does not touch what the entity is:
  **Onboarding Unit** (`drift.py` is a one-line import move; the unit's definition, key identifiers
  and maintenance rules are untouched), **Worktree Contract** (`guidance.py`'s only `run_git` is the
  `show -s --format=%cI` dating of a ledger row, and the contract fields, `sync_log` and closeout-gate
  ordering are unchanged) and **Task Document** (`snapshots.py`'s `run_git` is the best-effort
  ledger-popover `git log --no-walk`, not the summary/body task-document projection the entry
  describes). No metadata or fingerprint cell was hand-edited; closeout recomputes those.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 curator: recomputed the `git-blob-set-v1` fingerprints for
  the nineteen entities the closeout preview flagged (Onboarding Unit, Runtime AGENTS Template
  Package, Coordination Context, Path Rule, Memory Quality Control, External Memory Ledger, Memory
  Baseline Adoption, Worktree Contract, Worktree Integration, Branch-Gated Cross-Repo Source,
  Provider Degradation Protocol, Seat Binding Identity, Seat Retirement, Seat Landing Archive,
  Supervisor Sweep, Task Document, Delivery Injector, Harness Capability Snapshot, Harness
  Submission Authority) against the staged index, since the leaf's code commit has not landed yet;
  the two unflagged rows were re-verified and already matched. Added a `260731-EFA-L2 Entity
  Clarifications` section recording that **no entity was added, removed, split, merged or moved** —
  the fingerprints turned because implementations were re-signed onto parameter objects — and naming
  the changes that do alter what a caller may write: the resolver's keyword-bundle input API
  (`CoordinationHints`/`EnclosureSelector`, resolved output unchanged), the `SeatClosure` provenance
  shared by retirement and landing, `EscalationSchedule`/`OwnerSignal` in the sweep, the
  single-capability-decision-point in the submission authority (and the two deleted duplicate
  re-checks that were **not** relaxations), and the relocation of the liveness hysteresis config from
  `terminal_liveness.py` to `terminal_catalog.py`. Corrected the Delivery Injector relationship row,
  which claimed it wraps `TerminalPaster.paste` unchanged: dispatch now goes through the separate
  `paste_dispatch` whose acceptance probe is required by the signature, replacing a deleted runtime
  `ValueError`. Closeout should re-verify every fingerprint against the landed `HEAD`.
- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental CRAP/commit-gate curation:
  clarified the Worktree Contract projection so approved closeout runs the strict
  repository wrapper before any mutation and preserves all code, memory, ledger,
  contract, and applied-gate state on failure. Existing entity fingerprints remain
  intentionally unchanged until the code commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: clarified the existing Harness Capability Snapshot and Harness Submission Authority projections for fixture-backed interrupt evidence and queued-receipt honesty; fingerprint values intentionally unchanged before code commit.

- 2026-07-21T11:30+02:00 — 260718-CHATS-L5F curator: extended `Harness Capability Snapshot` for the
  R2 resolved-identity launch acceptance (requested-alias-wins-on-resolved-model; the opus[1m]/default
  collision is accepted, a genuinely different model still refused). No entity added or renamed.
  Honest finding: entities.md carries NO conversation-capability (`FeatureCapability`/
  `ConversationCapabilities`) entity, so the R4 version-gate removal required NO version-lock
  correction here — that doctrine lives in the `serving/conversation/*` capability sidecars/overviews.
  Fingerprint note: L5F changed several `Harness Capability Snapshot` evidence files
  (`harness_control_models.py`, `harness_control_bridge.py`, `harness_control_client.py`,
  `harness_control_claude.py`, `harness_launch.py` — R1 native-method carry, R2 acceptance, R6 honest
  control-socket note), so its `git-blob-set-v1` fingerprint is now STALE; the changes are uncommitted,
  so closeout must recompute the fingerprint after the candidate commit.
- 2026-07-20T00:08+02:00 — 260718-CHATS-L2E curator: extended both harness entities for the native
  control-plane substrate; no entity added or renamed. `Harness Submission Authority` records the
  paged never-bodies `operation_timeline` enumeration, the once-only pre-tombstone
  `WithdrawalRecovery` payload, and the asset-carrying submit channel in its description,
  key-identifier, and daemon-boundary/server-authority projection rows, and its evidence set
  gains the four channel files `harness_control_models.py`, `harness_control_queue.py`,
  `harness_control_ipc.py`, and `harness_control_client.py` (10 → 14 paths). `Harness Capability
  Snapshot` records the structural `InterruptCapableAdapter`/`AssetSubmitCapable` capability
  contract (fail-closed typed refusal naming the adapter, fixture-gated enablement) in its
  description, key-identifier, and normalized-adapter projection rows, and its evidence set gains
  `harness_control_bridge.py`, `harness_control_models.py`, and `pi_rpc_events.py` (17 → 20
  paths). Both fingerprint rows carry candidate working-tree fingerprints (`Harness Submission
  Authority` `sha256:7072511b2fc0fd4efc510dac0f57dd272f5928954b843d2bccfbc6e56d4787f6`,
  `Harness Capability Snapshot` `sha256:204ce5d816238315e6c9920e7ecbbe56a8d4eb206618a17381b79872b5c54b64`)
  computed over the extended sets with the canonical `git-blob-set-v1` line format (validated by
  reproducing both prior rows from HEAD blobs); closeout must recompute both against the landed
  L2E code commit via `refresh_entity_fingerprints_for_context`.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: extended both harness entities for the native
  evidence and resume substrate. `Harness Capability Snapshot` records the additive codex-only
  `resume_thread_id` launch channel (opener → `RunnerConfig` payload → factory → sole
  `CodexAppServerSettings` site, pre-spawn fail-closed, never validated/authorized by the opener)
  in its description, naming-drift, key-identifier, and launch-boundary projection rows.
  `Harness Submission Authority` records the additive read-only `submission-provenance` batch
  (epoch-checked, 1..64 unique ids, exact three-source disclosure with honest not-found, sole
  bridge → queue → authority delegation) in its description, key-identifier, and daemon-boundary
  projection rows. No entity was added or renamed and no evidence path list changed; both
  fingerprint rows stay pinned to the committed L0 base because the leaf's code is uncommitted.
  Candidate working-tree fingerprints are `Harness Capability Snapshot`
  `sha256:601bc93731ef22bb94336e0a2212f954d57727b2a1905e507db41042224f89ce` and
  `Harness Submission Authority` `sha256:1526ac63bf4fca6794b6f840d0216e3dcb6ea9db1aba9cd00183d6715202c180`;
  closeout must recompute both against the landed L0E code commit.

- 2026-07-18T15:22+02:00 — FEUI-MX-FIX-2 curator: clarified that dashboard binding identity is
  materialized only from the validated accepted server row and that failed/request-only opens create
  no provisional binding row. The Seat Binding Identity fingerprint remains pinned pending closeout
  recomputation against the landed code commit.

- 2026-07-18T07:22+02:00 — FEUI-L8 curator: moved Seat Landing Archive dashboard evidence from
  retired `sessionGroups.ts`/`Chats.tsx` to `railModel.ts`, `SessionRail.tsx`,
  `sessionLifecycle.ts`, and `LandedCleanupNotice.tsx`; preserved read-only landed inspection and
  exact cleanup outcome/unknown-result recovery. Fingerprint recomputed from current HEAD evidence;
  closeout will recompute after the L8 code commit.
- 2026-07-17T21:39+02:00 — 260715-FEUI-L5 curator: added the load-bearing `Harness Submission
  Authority` entity and cross-layer projection for the sole epoch-bound prompt/setter timeline,
  atomic dispatch/withdraw, full refs, early-completion dominance, raw-free bounded status,
  dispatch-now adapters, and revision-safe pop-back. Updated `Harness Capability Snapshot` to remove
  stale shared/native queue ownership and distinguish capability evidence from lifecycle authority.
  Candidate working-tree fingerprints are `Harness Submission Authority`
  `sha256:bcea73128e11...` and `Harness Capability Snapshot` `sha256:8ca47ead9a60...`; closeout must
  recompute both against the landed FEUI-L5 code commit.
- 2026-07-17T04:20+02:00 — 260715-FEUI-L6 curator: extended the two cockpit consumption records —
  Seat Retirement gains the L6 residual surface (the focus-independent
  `retireControlStopError` sweep into informational, never-dropped stage notes + the retired-row
  inspector) and the explicit boundary that the cockpit renders retirement but cannot issue it
  (the retire route requires a catalog actor seat; the cockpit's operator action is the honest
  terminate confirm); Seat Landing Archive gains the L6 cleanup-outcome rendering (the rail shows
  the landed-cleanup route's own closed + skipped-with-reasons response via `endLandedDetailed`).
  No entity was added or renamed; fingerprints remain pinned to the committed base and must be
  recomputed after the L6 code commit.
- 2026-07-17T02:30+02:00 — 260715-FEUI-L2 curator: recorded the sessions cockpit as a live
  consumer on Seat Retirement (the `seat.retired` pre-apply path + provenance surfaces) and Seat
  Landing Archive (rail completed folders + master/sprint bulk end over the same landed-cleanup
  endpoint, `seat.landed` pre-apply), adding the dashboard seatEvents/railModel/SessionRail
  source references. No entity was added or renamed; fingerprints remain pinned to the committed
  base and must be recomputed after the L2 code commit.
- 2026-07-16T07:27+02:00 — 260714-ACPUI-L5 curator: closed the live three-harness matrix for
  Harness Capability Snapshot and added Claude's exact discovery-only MCP isolation versus normal
  installed-session startup. Recorded dynamic Fable, Codex queued promotion, Pi readback/clamp,
  resource-evidence, and startup-failed stop boundaries; expanded the curated evidence set from 16
  to 17 paths. The fingerprint reflects the committed L4 base and must be recomputed after the L5
  code commit.
- 2026-07-16T06:26+02:00 — 260714-ACPUI-L4 curator: extended Harness Capability Snapshot through
  the daemon boundary: bounded install-fingerprinted advertise with auth-refresh quarantine,
  settings/request launch convergence through one live-truth opener, exact-session setters,
  first-byte ambiguity, idempotent whole-message submit, retained reconciliation without resend,
  raw-free public responses, and liveness-first status classification. Preserved role spawn and the
  durable bus, and expanded the curated evidence set from 12 to 16 paths. The L3 fingerprint remains
  intentionally pinned until closeout commits L4 code and recomputes the expanded set.
- 2026-07-16T01:34+02:00 — 260714-ACPUI-L3 curator: extended Harness Capability Snapshot to the
  implemented normalized `CapabilitySnapshot`/`SetResult` pair, exact five-value truth contract,
  queue-ordered setters, and truthful Claude correlated-terminal, Codex fresh-turn, and Pi bounded
  error/clamp semantics. Recorded the dynamic Fable correction and preserved settings-owned role
  spawn plus the durable inbox/brief bus as independent moats. Expanded the curated evidence set;
  its prior fingerprint remains intentionally pinned until closeout creates the L3 code commit and
  the new Pi configuration source has a `HEAD` blob.
- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: expanded Harness Capability Snapshot from the
  L1 advertise-only state to settings/role-resolved `ResolvedLaunch`, pre-discovery conflict
  refusal, dynamic model-gated validation, Claude/Codex/Pi native launch channels, honest effective
  evidence, the temporary roleless Codex default, exact Pi identity, Claude mismatch failure, and
  the L3/L4 handoff. Curated eight load-bearing evidence paths; the prior committed fingerprint is
  deliberately retained only until manager closeout recomputes it against the L2 code commit.
- 2026-07-15T20:04+02:00 — 260714-ACPUI-L1 curator: added the selective Harness Capability
  Snapshot entity for the normalized contract, three native dynamic catalog projections, cached
  advertise versus transient discovery, ACP Sense 1 derived view, and explicit no-transport/no-
  prompt boundary. Fingerprint uses current worktree blobs and closeout must recompute it against
  the eventual L1 code commit.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: reviewed the Provider Degradation Protocol
  entity for the additive inbox reader seam; only the exact two delivery-evidence fields are
  tolerated and the fingerprint is refreshed by delegated closeout after the code commit.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.

- 2026-07-10T21:05+02:00 — Super-exit curator fingerprint reconciliation against code commit
  `e400ed0ce98752d1b65d00de97c9b84c7ea20814`: recomputed all 19 `git-blob-set-v1` entity rows
  with the canonical ref-pinned algorithm; every stored fingerprint matched, every inventory entry
  had exactly one row, and no evidence path was missing. Entity prose was reviewed as unchanged.

- 2026-07-10T19:49+02:00 — Positional 260707-HFX2-L19: refreshed the existing `Supervisor Sweep`
  entity for the hosted-delivery retry-before-escalation boundary; added the guard/attempt threshold
  identifiers, detection and inbox-state relationships, and the F1 regression-pin disposition.
  Refreshed its current candidate-worktree fingerprint to `sha256:11b285be...`. Also reviewed the
  `Seat Landing Archive` shared manager/orchestrator role evidence: those changes add only
  Developer Clarification Triage and do not alter landing/archive semantics, so its prose remains
  unchanged while its candidate fingerprint refreshes to `sha256:9a392aab...`. Manager-owned
  closeout must recompute both against the eventual L19 code commit.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added the selective cross-layer `Seat Binding
  Identity` entity for canonical `(leafKey, seatRole)` ownership, origin-vs-current-role
  separation, legacy migration, live replacement, explicit hand-opened claims, and dashboard/
  control-plane projections. Updated Seat Retirement and Supervisor Sweep for pair identity and
  binding-first authority/routing; Seat Landing Archive now lands current roles. Preserved reviewer
  O1 migration-read race, O2 local trust model, O3 reopen precedence, and O4 bounded fixed-point
  adjustment at their actual entity homes. Refreshed candidate working-tree fingerprints:
  `Seat Binding Identity` `sha256:b1ca3089...`, `Provider Degradation Protocol`
  `sha256:6399c205...`, `Seat Retirement` `sha256:5b40314e...`, `Seat Landing Archive`
  `sha256:edf86482...`, `Supervisor Sweep` `sha256:cbdd9c09...`, `Task Document`
  `sha256:460b3970...`, and `Delivery Injector` `sha256:e9eea669...`. The last three shared-file
  entities retain their prior meaning except where explicitly described; closeout must recompute
  all candidate fingerprints against the eventual L17 commit.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16: refreshed the Task Document entity for merged
  on-demand bodies, explicit unavailable-body fallback, and single-rendered steps; recorded the
  scalar-overwrite/cache notes. Seat Landing Archive meaning is unchanged, but its shared
  `sessionGroups.ts` evidence moved to repo-qualified sprint grouping. Candidate-worktree
  fingerprints are `Task Document` `sha256:89352b...` and `Seat Landing Archive`
  `sha256:6f06df...`; closeout must recompute both against the eventual code commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: refreshed Delivery Injector and Supervisor Sweep for
  harness-log acceptance, duplicate-safe bounded recovery, explicit replacement-leaf chain credit,
  and one-row redelivery. Refreshed their candidate-worktree fingerprints and the shared changed
  evidence fingerprints for Seat Retirement, Seat Landing Archive, and Task Document after review
  confirmed those three entity meanings were unchanged. Closeout must recompute all five against
  the eventual code commit.

- 2026-07-10T02:39+02:00 — HFX3 retro curation: refreshed `Runtime AGENTS Template Package` for
  the coordinator template's otherwise-free-chat launcher and settings-owned architect spawn;
  recomputed its worktree-content fingerprint to
  `sha256:5adc4ca9be01f8499b29818bbbb6f2677c1a6a38d61b3a52cd0bb96c0e008b9f`.
  Closeout must recompute against the eventual two-parent code commit.

- 2026-07-10T01:14+02:00 — 260707-HFX2-L13 curator pass: refreshed the existing `Supervisor
  Sweep` entity for current-manager-first routing, leaf-chain progress, redundant rung dwell, same-
  sweep transition protection, and completion wake; explicitly retained the accepted unbound-worker
  S1 follow-up for HFX2-L14. Added the selective cross-layer `Task Document` entity for bounded
  summary broadcast plus path-confined on-demand bodies and dashboard path/revision caching.
  Fingerprints were computed from current worktree blobs and remain closeout-verification inputs
  until the eventual L13 code commit exists.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator pass: split the old completion-edge
  auto-retire model into two current entities. `Seat Retirement` now covers explicit/authority-
  checked termination and landed-group cleanup only, with a refreshed fingerprint over retire
  surfaces. Added `Seat Landing Archive` for `status:"landed"`, `_auto_land_completed_seats`,
  `autoLandedSeats`, sweep-cold liveness behavior, dashboard grouping, package-data doctrine, and
  explicit cleanup; fingerprint computed over current uncommitted worktree blobs. Recorded the
  known limitation that a landed row whose tmux session later dies is not reclaimed by the
  background sweep. Verification metadata pinned until closeout stamps the HFX2-L11 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9 (redelivery cadence + signal throttling, curator
  pass): EXISTING-ENTITY update, not a new entity — `Supervisor Sweep`'s evidence, Description,
  Key Identifiers, Parent/Child row, Source References, Migration Notes, and Cross-Layer Projection
  now include the 900-second redelivery floor (`inbox_backoff.py`), floor-aware inbox scheduling
  (`operator_inbox_store.py`), and the persisted signal cooldown store (`supervisor_signals.py`).
  The new store's unbounded/no-compactor limitation is explicitly recorded as an HFX2-L11 deferral.
  Fingerprint computed over current worktree content with `git hash-object` because the code is
  uncommitted. Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
- 2026-07-08T23:59+02:00 — 260707-HFX2-L5 (doctrine rewrite + focused liveness simulations, curator
  pass): NOT a new entity — this leaf touches no runtime code (5 doctrine-only `skills/` files
  synced to 9 downstream copies + 1 new test file). `Supervisor Sweep`'s Migration Notes gains a
  forward-reference row recording a real gap the new `mcp/tests/test_liveness_simulations.py` found
  and documented in THIS entity's own module: `evaluate_predicates` cannot be fed an injectable pane
  capturer through `AgentNotifierContext`, so 2/8 of the leaf's P-15 fixture-zoo scenarios stay hybrid
  (predicate-unit classify + real downstream sweep response) rather than full end-to-end — recorded
  as a forward reference for the natural follow-up leaf (thread a capturer parameter through
  `AgentNotifierContext`/`evaluate_predicates`), in the same spirit as this entity's own
  Naming-Drift-row forward reference to the L3 injector before that leaf existed. Verification
  metadata pinned until closeout stamps the 260707-HFX2-L5 commit.
- 2026-07-08T23:15+02:00 — 260707-HFX2-L4 (P-15 tier 3 escalation ladder + dead-man respawn, curator
  pass): EXISTING-ENTITY update, not a new entity — `Supervisor Sweep`'s evidence/Description/Key
  Identifiers/Migration Notes extended to cover the two new `controlplane/` modules
  (`escalation_ladder.py`, `orphan_policy.py`) and the `signal_routing.py` two-hop extension, judged
  against this entity's OWN Migration Notes (written at HFX2-L3 closeout, anticipating this exact
  leaf: "when it lands this entity's evidence paths and Description should be revisited"). Reasoning:
  the ladder is wired DIRECTLY into `serving/supervisor.py` with no independent lifespan task or
  settings family of its own — it extends this entity's existing detection/response/settings layers
  rather than clearing the bar for a new entity (unlike `Delivery Injector`, which had its own
  transport/classification/per-harness layer independent of the sweep). Fingerprint marked pending
  recompute at closeout (this pass runs against an uncommitted worktree, so the current `HEAD` blob
  hashes would not reflect the new evidence paths). Verification metadata pinned until closeout
  stamps the 260707-HFX2-L4 commit.
- 2026-07-08T22:30+02:00 — 260707-HFX2-L3 (paste injector hardening, R1-R5, curator pass): added the
  `Delivery Injector` entity — `serving/injector.py`'s `deliver(row)` four-way `DeliveryOutcome`
  contract plus `serving/harness_adapters.py`'s per-harness `HarnessAdapter` interface, judged
  entity-worthy against the same bar `Supervisor Sweep` (HFX2-L2) was added under: a real cross-
  cutting primitive that recurs across two independent call layers (the MCP spawn-tool payload
  builder in `mcp/tools/` and the inbox/supervisor delivery layer in `serving/`) and had already
  caused forward-reference naming ("the L3 injector") in `Supervisor Sweep`'s own Response row before
  this leaf existed — exactly the recurring/naming-confusion bar the catalog workflow names. Judged
  as a NEW entity rather than folding into `Supervisor Sweep`, since it is used by the spawn-brief
  path which has nothing to do with the supervisor sweep at all; `inbox_delivery.py` is a caller of
  this new entity, not itself added to `Supervisor Sweep`'s evidence set. Fingerprint computed via
  `git hash-object` over the four evidence paths' current worktree content (no commit yet at this
  leaf) — `sha256:312577ee…`. Added the matching Cross-Layer Projections entry. Also recomputed
  `Supervisor Sweep`'s own `git-blob-set-v1` fingerprint (`sha256:48d7a2e6…`, was `sha256:b940f1f8…`)
  because this leaf's diff touched `pane_signals.py`, one of that entity's own evidence paths (new
  `blocked_reason_label`/`composer_state`, populated `_HARNESS_BLOCKED_PATTERNS["codex"]`) — reviewed
  the diff directly: additive signatures the `Delivery Injector` entity composes, no change to
  `classify_pane_signal`'s own precedence or `Supervisor Sweep`'s predicate/dispatcher/heartbeat
  logic, so only a Migration Notes/Current Naming Drift update was warranted, not a Description
  rewrite. Verification metadata pinned until closeout stamps the 260707-HFX2-L3 commit.
- 2026-07-08T18:45+02:00 — 260707-HFX2-L2 (supervisor sweep + predicates): added the `Supervisor
  Sweep` entity — a new load-bearing cross-layer protocol (predicate library + action executors +
  self-liveness heartbeat + settings family + MCP-tool and dashboard surfacing) judged against the
  same bar `Provider Degradation Protocol` (HFX-L7) and `Seat Retirement` (HFX-L8) were added under:
  a genuine detection/response subsystem crossing multiple package routes (`serving/`, `kernel/`,
  `mcp/tools/`, `dashboard/`), not a single-file feature. Fingerprint computed via `git hash-object`
  over the five evidence paths' current worktree content (the code worktree has no commit yet at
  this leaf; the blob hashes match what `HEAD:<path>` will resolve to once closeout commits land) —
  `sha256:b940f1f8…`. Added the matching Cross-Layer Projections entry. Verification metadata
  pinned until closeout stamps the 260707-HFX2-L2 commit.
- 2026-07-08T16:15+02:00 — 260707-HFX2-L1 (curator delta round 2, closeout-preview gap): refreshed
  the `Provider Degradation Protocol` `git-blob-set-v1` fingerprint (`sha256:98247629…`) after this
  leaf's diff touched the entity's shared `operator_inbox_records.py` evidence path. Reviewed the
  diff directly: the change adds `attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt`
  (R1 ack-semantics) and `ownerRole`/`ownerAgentId`/`ownerLifecycleId` (R4 hierarchical routing)
  fields to `OperatorInboxEntry` — purely additive record fields for an unrelated feature, touching
  neither the `AgentRole`/`InboxMessageKind` Literals this entity's `system-specialist`/
  `degradation-alert` values live on, nor the detector/response protocol itself — so no entity
  prose change beyond a short Migration Notes disclosure of the touch. Fingerprint computed
  manually (sorted `path:blob_hash` pairs over `git hash-object` output on the leaf's uncommitted
  working tree, joined `\0`, sha256), same as the Seat Retirement precedent, since no commit exists
  yet for this leaf's diff to run the canonical `compute_git_blob_set_fingerprint` tool against;
  flagged for recompute via the actual `c-02-memory-quality-control` skill tooling at closeout.
- 2026-07-08T02:55+02:00 — 260707-HFX-L8 (seat lifecycle: retirement + live identity + turn-state,
  issues #12/#4): added the `Seat Retirement` entity — the first genuine new cross-layer entity this
  leaf introduces per the mgmt-L4 routing rule (catalog + policy + automation hooks + doctrine all
  cross-cut). Live identity (rename) and live turn-state were judged NOT independently catalog-worthy
  entities: rename is a simple identity-text field on the existing catalog row with no new protocol
  of its own, and turn-state is a derived/observational signal (classification + projection), not a
  load-bearing structural entity with its own authority/lifecycle — both are documented in the
  relevant file sidecars and the `serving/` route overview instead. `git-blob-set-v1` fingerprint for
  `Seat Retirement` was computed manually (sorted `path:blob_hash` pairs over `git hash-object` output
  on the leaf's uncommitted working tree, joined `\n`, sha256) since no commit exists yet for this
  leaf's diff to run the canonical `compute_git_blob_set_fingerprint` tool against; flagged for
  recompute via the actual `c-02-memory-quality-control` skill tooling at closeout, same as several
  prior entries in this history that left fingerprints pending a tooled recompute.
- 2026-07-08T01:00+02:00 — 260707-HFX-L7 curator memory pass: added the `Provider Degradation
  Protocol` entity (detector/state-machine, `providerDegradation` settings surface,
  `system-specialist` role, `degradation-alert` inbox kind) with its Entity Inventory row and
  Cross-Layer Projection. Fingerprint left pending — the R1+R2 evidence files are uncommitted at
  this curator pass (code worktree HEAD `607cab0d`); recompute the `git-blob-set-v1` fingerprint
  at closeout once the HFX-L7 commit lands.
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): recomputed the `Coordination Context`, `Branch-Gated Cross-Repo Source`, and `Path Rule` `git-blob-set-v1` fingerprints. The series carryover stamped them against the series tip (`bb69380`), but merged main changed their shared `coordination_context_resolver.py` evidence (the facade now re-exports `find_worktree_contract`, #90 / MCP 2.9.3), so the blob set differs at 84e95ad. Coordination Context + Branch-Gated Cross-Repo Source share evidence → `sha256:e23cab68…`; Path Rule → `sha256:83bad6ef…`. Recomputed with the canonical `compute_git_blob_set_fingerprint` and validated by reproducing the prior `bb69380` fingerprints first. Entity prose unchanged (the worktree_name fallback is a no-route-impact addition).
- 2026-06-21T06:40+02:00 — Slice 05m (carryover-before-cleanup): updated the `Worktree Integration` entry's Description and its `Cleanup` Cross-Layer Projections row — cleanup (`cleanup_result`) is now carryover-guarded (hard-refuses until the parked memory is carried into official memory, proven by `guidance.carryover_done` against the official ledger, since cleanup deletes the parked memory branch the carry reads from) and, once carryover has run, retires both the worktree branch and the (PR'd) source branch (local for code + memory, remote for the code source branch). The `Worktree Contract` entry was left unchanged (its body records the `cleanup` contract field, not the lifecycle phase sequence). Entity metadata/fingerprint rows left for closeout recompute.
- 2026-06-19T06:03: Slice 3c reopened (R4, leaf-doc fidelity) — the w-02 skill (SKILL/template) now documents the leaf extensions (`statusNote`/`headerNotes`/freeform `sections`). The `Light Task Artifact` evidence (the w-02 `package_data` skill files) changed; the `git-blob-set-v1` fingerprint row is left for closeout recompute.
- 2026-06-19T05:15: Slice 3c reopened (R3, deferred-examples honesty) — the w-02 skill (SKILL/template/workflow) now teaches `codeExamplesNote` (a deferred planning slice records it so the render reads as deferred rather than none-needed). The `Light Task Artifact` evidence (the w-02 `package_data` skill files) changed; the `git-blob-set-v1` fingerprint row is left for closeout recompute.
- 2026-06-14T00:16: Slice 3c commit 3 — the JSON-primary format now also covers a series `master` (`kind:"master"`: a `subTasks` index + ordered `sections`); updated the `Light Task Artifact` description. Its evidence (the w-02 `package_data` `SKILL.md`) changed again; the `git-blob-set-v1` fingerprint row is left for closeout recompute.
- 2026-06-13T22:34: Slice 3c commit 2 — updated the `Light Task Artifact` entry for the JSON-primary task-document format: the `task_doc` MCP tool authors the `ar-task-document/v1` JSON and renders `task.md` (`light`/`subTask`; series master files stay hand-authored). Its evidence (the w-02 `package_data` skill files) changed; the `git-blob-set-v1` fingerprint row is left for closeout recompute.
- 2026-06-11T14:32+02:00: Refreshed the `Path Rule` fingerprint after the rename sweep (PR #75, merged main `b9f1a31`) changed its `examples/mcp/settings.example.json` evidence; entity prose unchanged.
- 2026-06-11T14:20+02:00: Re-verified the `External Memory Ledger` and `Worktree Contract` entries against merged main `b9f1a31` and recomputed both `git-blob-set-v1` fingerprints; the 2026-06-11T06:28 refresh had stamped them against a pre-merge worktree state whose evidence blobs did not survive the PR #63 landing verbatim. Entity prose verified accurate (sync_log, typed `WorktreeArgs` DTO, `AgentsRememberError` hierarchy all current); no prose changes.
- 2026-06-11T06:28+02:00: Refreshed the `Worktree Contract` and `Worktree Integration` fingerprints after the issue #54 / 2.8.0 landing (`worktree_sync`, stale-base preflight) changed `worktree_contract.py`, `modules/guidance.py`, and the shared c-09 skill evidence. Recorded the contract's new `sync_log` base-pair field in the Worktree Contract entry and noted mid-task sync's `ff-only` preservation in the Worktree Integration entry; the rest of both entries remains accurate.
- 2026-06-09T14:52+02:00: Reviewed the `Runtime AGENTS Template Package` evidence after MCP 2.4.1 changed the coordinator template, confirmed the entity description remains accurate with the hard onboarding trust gate, and refreshed its `git-blob-set-v1` fingerprint to `sha256:9e731db9b99f5a3c0910e323a50b1674f2d05544ce4b672318548b18b7ed4cfe`.
- 2026-06-03T04:32+02:00: Refreshed the `Worktree Contract` and `Worktree Integration` fingerprints after the C-09 source-branch clarification changed their shared skill evidence; entity prose remains accurate.
- 2026-05-31T12:30+02:00 — Updated External Memory Ledger, Worktree Contract, and Worktree Integration descriptions for the 1.0.0 review remediation: `LedgerError`/`ContractError` now subclass the shared `AgentsRememberError` typed-error family, worktree service functions take a typed `WorktreeArgs` DTO instead of `argparse.Namespace`, and integration's final merge is now atomic (pre-validates both fast-forwards and rolls both branches back on memory-side failure). Fingerprint rows left as-is for closeout recompute.
- 2026-05-30T21:51+02:00: Recomputed the `Path Rule` (`sha256:7a2575aa…`) and `Runtime AGENTS Template Package` (`sha256:1bef3bb4…`) fingerprints after the 0.9.x run changed their evidence (`examples/mcp/settings.example.json` gained `timeoutCaps`; `install/runtime.py` gained `no_cache`); both entity descriptions were reviewed and remain accurate. Repaired the `Path Rule` Source References — the stale `README.md L122-L135` citation (out of range; path-rule guidance moved to `docs/`) now points to `docs/reference/path-rules.md`. Fingerprints recomputed with the canonical `compute_git_blob_set_fingerprint` and validated against an unchanged entity.
- 2026-05-29T11:11+02:00: Refreshed the File-Level Onboarding Content Model fingerprint to `sha256:2c2e5cac` and aligned its prose to prepend-only update-history wording after source commit `1ccbc2d` corrected the file-level onboarding template's update-history comment from append-only to prepend-only.
- 2026-05-25T20:57+02:00: Updated coordination context, path rule, and cross-repo source descriptions after the `c-08-ar-coordination-context-resolver` skill resolver moved behind focused `coordination_context/` implementation modules.
- 2026-05-25T20:41+02:00: Updated worktree ledger, contract, and integration entity evidence paths after `c-09-git-worktree-manager` skill worktree lifecycle logic moved behind focused implementation modules.
- 2026-05-25T16:37+02:00: Refreshed drifted onboarding verification metadata to source commit `a8ee844`, repaired packaged runtime evidence paths, and recomputed entity fingerprints.
- 2026-05-24T10:06+02:00: Refreshed fingerprints after source commit `f48a346` moved Codex setup to `.codex`, removed source `.env` resolver authority, and added clean-source versus dirty-source drift classification guidance.
- 2026-05-24T04:34+02:00: Renamed the drift-report entity to memory quality control, refreshed fingerprints after the `c-02-memory-quality-control` skill rename, and updated approval-gate evidence.
- 2026-05-24T03:24+02:00: Refreshed worktree fingerprints after `c-09-git-worktree-manager` skill adopted the pre-code-commit missing-onboarding check.
- 2026-05-24T02:47+02:00: Refreshed drift, baseline, and worktree fingerprints after memory quality moved drift integrity under `memory_quality` and `c-09-git-worktree-manager` skill adopted `memory_quality_check` closeout guidance.
- 2026-05-24T00:37+02:00: Refreshed external memory ledger, baseline adoption, worktree contract, and worktree integration fingerprints after MCP worktree and memory controllers moved to service-backed result functions.
- 2026-05-23T04:29+02:00: Updated Runtime AGENTS Template Package after templates moved provider startup guidance to `context_packet` MCP tool and external MCP settings authority.
- 2026-05-22T13:32+02:00: Updated onboarding-unit and file-level content model entities after `c-05-create-or-update-onboarding-files` skill made domain-doc discovery provider-neutral while treating live registry-named documentation sources as authoritative over local mirrors. Fingerprints remain pinned until closeout commits the source change.
- 2026-05-18T21:44+02:00: Refreshed drifted fingerprints after pulling the committed `c-04-retrieval-strategy-router` skill onboarding read-mode rename from `origin/main`.
- 2026-05-18T21:38+02:00: Refreshed drifted fingerprints for runtime AGENTS template package, coordination context, and branch-gated cross-repo source after reviewing their current evidence paths.
- 2026-05-16T18:08+02:00: Refreshed the runtime `AGENTS.md` template package fingerprint after closing out the benchmark workspace install and runner changes.
- 2026-05-16T11:38+02:00: Refreshed the runtime `AGENTS.md` template package fingerprint after the benchmark installer `.gitignore` and Windows pruning fixes changed installer evidence.
- 2026-05-16T11:08+02:00: Refreshed the runtime `AGENTS.md` template package fingerprint after the installer and template evidence set changed in the latest source commit.
- 2026-05-15T12:57+02:00: Clarified that entity drift also checks inventory-to-fingerprint coverage, with missing rows and orphaned rows treated as actionable maintenance.
- 2026-05-15T12:23+02:00: Added deterministic `git-blob-set-v1` fingerprints for current catalog entities and refreshed drift-report/onboarding-unit wording for overview and entity checks.
- 2026-05-15T01:07+02:00: Clarified that `c-08-ar-coordination-context-resolver` skill's no-task-name `task_root` is the repo-specific task namespace under `ar-coordination/tasks/<repo>/`.
- 2026-05-15T00:38+02:00: Added the runtime `AGENTS.md` template package entity after the source templates were consolidated under `mcp/src/agents_remember/package_data/runtime/agents-md-files/`.
- 2026-05-14T20:00: Updated entity terminology after the alpha model switched to external-memory and `c-05-create-or-update-onboarding-files` skill renamed non-inline onboarding storage to sidecar onboarding.
- 2026-05-12T10:59: Updated the external memory ledger entity after branch fields were removed from canonical ledger metadata.
- 2026-05-11T19:01: Renamed the resolver entity to coordination context after `c-08-ar-coordination-context-resolver` skill moved its semantic API to coordination terminology.
- 2026-05-09T23:55: Added worktree integration as a current lifecycle entity and updated contract fields for integration commits.
- 2026-05-09T23:22: Updated coordination context and drift report entities after `c-08-ar-coordination-context-resolver` skill added `temp_root` and `c-02-memory-quality-control` skill moved reports under `temp/drift-reports`.
- 2026-05-09T22:46: Added memory baseline adoption as the current-state entity introduced by `c-10-adopt-memory-baseline` skill.
- 2026-05-09T22:10: Refreshed entity wording so ledger, contract, `c-09-git-worktree-manager` skill, and cross-repo v2 are described as implemented current state.
- 2026-05-09T21:15: Created first `agents-remember` entity catalog for the preliminary onboarding baseline.
