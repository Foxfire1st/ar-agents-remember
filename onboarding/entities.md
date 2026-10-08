# Entities

| Field       | Value                  |
| ----------- | ---------------------- |
| status      | active                 |

## Purpose

This catalog documents load-bearing real entities in `agents-remember`. It is not a glossary of every workflow term and it does not catalog task files. Task files remain planning artifacts; this file describes current reusable repository concepts and the boundaries between them.

### Historical CCR Committed-Fingerprint Boundary

The catalog is reconciled to prepared code candidate
`602143bd1d48226f4d53b83ff7c5002a695dcdff` (tree `4c6b7bc2362bc03d50fc7a0643f34b591b805d45`). Entity fingerprints below resolve only committed
`602143bd1d48226f4d53b83ff7c5002a695dcdff:<path>` blobs from that candidate; no working-tree fingerprint or provisional verification
stamp is treated as authority. This is source verification of the prepared implementation candidate, not aggregate acceptance. All seven candidate-local evidence sets were re-read against this source view; the three changed rows were refreshed in this pass and the other four already matched it.

### Current Scoped Committed-Source Review

The recorded refresh from committed code `7cbda30d9a9a4c2944382fbef46ac58b85329935` covers 11 entity fingerprints: `Onboarding Unit`, `File-Level Onboarding Content Model`, `Light Task Artifact`, `External Memory Ledger`, `Closeout Effective Input`, `Closeout Mutation Evidence`, `Memory Baseline Adoption`, `Worktree Contract`, `Source Lineage`, `Worktree Integration`, `Seat Landing Archive`. The stored rows match the [scoped refresh receipt](ar-coordination/tasks/agents-remember/260913_ledger-commit-attribution/notes/reports/2026-09-15-live-cutover/entity-fingerprint-refresh.json); the External Memory Ledger evidence set includes the committed cache owner. These 11 rows are no longer pending a source commit or fingerprint recomputation. This closure confirms that recorded refresh and its current wording; it does not certify the full catalog or restamp unrelated entities and global verification fields.

## Entity Fingerprints

### 260915-CAPS-L5 Capsule Delivery Impact

The Codex capsule-delivery seam (`serving/capsule_delivery.py` plus the carrier chain through
`terminal_opener.py`, `harness_control_runner.py`, `harness_control_factories.py` and
`codex_app_server_session.py`) is a **new implementation of the existing adapter instruction-channel
boundary, not a new cross-layer entity**, so this catalog adds no entity row for it. Two existing
entities own the affected evidence and their recorded fingerprints are therefore stale at this
candidate:

- **Harness Capability Snapshot** — four of its evidence paths are edited by this leaf
  (`codex_app_server_session.py`, `harness_control_factories.py`, `harness_control_runner.py`,
  `terminal_opener.py`), and the boundary it describes gained a real capability rule: a delivered
  capsule is accepted only by a harness with a verified instruction channel (`codex`), and the launch
  configuration carries it as one optional value.
- **Source Lineage** — `terminal_opener.py` is in its evidence set and now transports the capsule from
  the launch boundary to the runner configuration.

Both stored fingerprints remain at the prior committed baseline. `git-blob-set-v1` resolves committed
`HEAD:<path>` blobs, so the refreshed value cannot be computed from this deliberately uncommitted
candidate and **no value was hand-edited here**; the governed closeout recomputes both rows against the
actual code commit, exactly as the ledger-retirement note above already requires.

### 260915-CAPS-L6 Native eve Adapter Impact

The native eve session adapter (`serving/eve_adapter.py`) is a **new implementation of the existing
adapter/capability boundary, not a new cross-layer entity**, so this catalog adds no entity row for it.
The two entities that own that boundary each gained real evidence paths, and their recorded fingerprints
are therefore stale:

- **Harness Capability Snapshot** gains the seven `serving/eve_*.py` modules, because the adapter
  advertises a real catalog through the existing `CapabilitySnapshot`/`LaunchKnobs` port — including the
  honest `session_settable: False` model/effort shape that a catalog reader must see.
- **Harness Submission Authority** gains `eve_adapter.py`, `eve_protocol.py` and `eve_runtime_client.py`,
  because the adapter now carries a real submission path: acceptance-versus-completion, the
  never-repeat-a-possibly-accepted-write reconcile, and the queued-turn policy.

Both stored fingerprints remain at the prior committed baseline. `git-blob-set-v1` resolves committed
`HEAD:<path>` blobs, so the refreshed value cannot be computed from this deliberately uncommitted
candidate and **no value was hand-edited here**; the governed closeout recomputes both rows against the
actual code commit, as the existing ledger-retirement note above already requires.

**A2 revision (same candidate, same entity judgment).** The A2 round repaired the candidate without
changing what either entity's evidence set proves, so the two rows above stand and no third entity
appears. The strengthened facts a future reader should not have to rediscover: acceptance on a
reconciled submission is proved by the durable record holding the exact accepted message (the
delivery-id branch was deleted as unreachable), the queued `turnPolicy` is spelled on the create **and**
the follow-up from one literal, and the replay window has a single owner.

Each row records the deterministic source evidence used by `c-02-memory-quality-control` skill for entity drift detection. The `git-blob-set-v1` fingerprint sorts the evidence paths, resolves each current `HEAD:<path>` Git blob hash, and hashes the resulting `path + blob_hash` list. A changed fingerprint means the entity entry needs review; it does not automatically prove the prose is wrong. `c-02-memory-quality-control` skill also reconciles this table against `## Entity Inventory`, so missing rows and orphaned rows are actionable catalog maintenance.

<!-- merged 2026-09-19: fingerprint cells carry each line's as-of values; the closeout recomputes the rows the landed range changes -->

| Entity                              | Algorithm         | Fingerprint                                                               | Evidence Paths                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------- | ----------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Onboarding Unit                     | `git-blob-set-v1` | `sha256:89afb9018098cf675ffb23d2b61e099c66f2fb4f186eff306693690881c2d567` | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py`                      |
| Runtime AGENTS Template Package     | `git-blob-set-v1` | `sha256:953ada2dc705ae567c6847def1dbd515c03c09ec8c8bb7457f21ef182c84a7da` | `mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md`; `mcp/src/agents_remember/install/runtime.py`                                                                                                                                                                                                                                    |
| Coordination Context                | `git-blob-set-v1` | `sha256:744cd1ba7638ef2d232d280ff228e8b7d3930a5b58c51979e2a0f11bed0b7a37` | `mcp/src/agents_remember/package_data/runtime/skills/c-08-ar-coordination-context-resolver/SKILL.md`; `mcp/src/agents_remember/kernel/coordination_context_resolver.py`                                                                                                                                                                                                                                                 |
| Path Rule                           | `git-blob-set-v1` | `sha256:1f544d85e78ade878387f698079757e64e31944cce872d03d140d4a2ab564c35` | `mcp/src/agents_remember/kernel/coordination_context_resolver.py`; `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.json`; `examples/mcp/settings.example.json`                                                                                                                                                                                                       |
| Memory Quality Control              | `git-blob-set-v1` | `sha256:4a7bc836deb5ef1405fdba529c95d511076f8862f352c0b1d9580a573051198a` | `mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md`; `mcp/src/agents_remember/memory_quality/check.py`; `mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py`; `mcp/src/agents_remember/memory_quality/style/update_history/history_order.py`; `mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py` |
| File-Level Onboarding Content Model | `git-blob-set-v1` | `sha256:ff7cf10808177dc3dabb1875eefc15325d6f209fe30dbbfa30a67968f615ccfe` | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md` |
| Light Task Artifact                 | `git-blob-set-v1` | `sha256:90bffff6b13e6377070fd9c68acedd2f7a730f4051d493efe144207e7c8cdfe3` | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md`; `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/requirement-packet-template.md`                                                                                                                                                                                               |
| External Memory Ledger              | `git-blob-set-v1` | `sha256:444568df87e1c051c7e341bfe9cbd7812dca8085836afd8c2d46e7b1bbe2ec9c` | `mcp/src/agents_remember/kernel/memory_attribution.py`; `mcp/src/agents_remember/kernel/memory_cache.py`; `mcp/src/agents_remember/kernel/memory_ledger.py`; `mcp/src/agents_remember/worktrees/ledger_projection.py` |
| Sprint Closeout Queue               | `git-blob-set-v1` | `sha256:a6fafc8bc6b520ce455985181786f01b4af49a0129dfe774f5a6e5cde7918077` | `mcp/src/agents_remember/controlplane/closeout_queue_store.py`; `mcp/src/agents_remember/models/closeout/projection.py`; `mcp/src/agents_remember/models/queue/closeout_queue.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py`; `mcp/src/agents_remember/worktrees/queue/closeout_queue.py` |
| Closeout Effective Input | `git-blob-set-v1` | sha256:fd1f3832d8557310928b00bf00944b2f92b5205651c6baf8f051c00e3bc58016 | `mcp/src/agents_remember/application/worktree_tools.py`; `mcp/src/agents_remember/mcp/registration/closeout.py`; `mcp/src/agents_remember/models/closeout/input.py`; `mcp/src/agents_remember/worktrees/closeout_input.py`; `mcp/src/agents_remember/worktrees/direct_landing.py`; `mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py` |
| Curator Coherence Authority         | `git-blob-set-v1` | `sha256:03de97986def566170b2d442903c4bc803226db8384f6ac7c21797fac43d8cd3` | `mcp/src/agents_remember/application/curator_coherence.py`; `mcp/src/agents_remember/models/lifecycles/curator_coherence.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_render.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_records.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py` |
| Closeout Mutation Evidence          | `git-blob-set-v1` | `sha256:2b816ddb8a79a4cdba0d36a21d8335a6e2408bdb061913ac133b562bc49350bb` | `mcp/src/agents_remember/models/lifecycles/mutation_evidence.py`; `mcp/src/agents_remember/models/lifecycles/operation.py`; `mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py`; `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py`; `mcp/src/agents_remember/worktrees/modules/closeout_external.py`; `mcp/src/agents_remember/worktrees/queue/closeout_recovery.py` |
| Memory Baseline Adoption            | `git-blob-set-v1` | `sha256:977453a2c326a13776dd507862c5d3ba47b54955e67d37b881b693e46505b859` | `mcp/src/agents_remember/package_data/runtime/skills/c-10-adopt-memory-baseline/SKILL.md`; `mcp/src/agents_remember/memory/baseline.py`                                                                                                                                                                                                                                                                                  |
| Worktree Contract                   | `git-blob-set-v1` | `sha256:66267b0d25bcfad8c8761c1999118918a336896b3082c60802eafb98ea5909cb` | `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md`; `mcp/src/agents_remember/worktrees/modules/closeout.py`; `mcp/src/agents_remember/worktrees/modules/guidance.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py`; `mcp/src/agents_remember/worktrees/worktree_contract.py` |
| Source Lineage | `git-blob-set-v1` | sha256:0abab6beee212b7fd91f5a82a73fc8a44d299c39cffece8cd537dad8ad19bd35 | `dashboard/src/panels/engine-room/DiagnosticsPanel.tsx`; `mcp/src/agents_remember/models/worktree.py`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-brief.md`; `mcp/src/agents_remember/serving/terminal_opener.py`; `mcp/src/agents_remember/worktrees/modules/closeout.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py`; `mcp/src/agents_remember/worktrees/source_lineage.py` |
| Worktree Integration                | `git-blob-set-v1` | `sha256:69f0f93f7873c3f98a03ff53eee97054143f3d7ae1af715756032a88f5a9a842` | `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md`; `mcp/src/agents_remember/worktrees/modules/cleanup.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py` |
| Branch-Gated Cross-Repo Source      | `git-blob-set-v1` | `sha256:8725cd636fe7a28a9cc46bc37f2ee1dd615c892c7e1733d10a9f865b8a042130` | `mcp/src/agents_remember/package_data/runtime/skills/c-08-ar-coordination-context-resolver/SKILL.md`; `mcp/src/agents_remember/kernel/coordination_context_resolver.py`                                                                                                                                                                                                                                                 |
| Provider Degradation Protocol       | `git-blob-set-v1` | `sha256:f82dd73d2d12cb8e8378bcd41f94322476aa91b2d73b662e9d8480e4c4ca1e7f` | `mcp/src/agents_remember/providers/degradation.py`; `mcp/src/agents_remember/kernel/primitives/provider_degradation_settings.py`; `mcp/src/agents_remember/controlplane/operator_inbox_records.py`; `mcp/src/agents_remember/controlplane/orchestration_artifacts.py`; `skills/l-01-agent-lifecycles/roles/system-specialist.md` |
| Seat Binding Identity               | `git-blob-set-v1` | `sha256:1f094294bcbfe42728a003e5e2ef6baebd0fab5652b48030c9b72d0d2cc802e9` | `dashboard/src/data/railModel.ts`; `dashboard/src/data/sessions.ts`; `dashboard/src/data/taskHierarchy.ts`; `mcp/src/agents_remember/controlplane/signal_routing.py`; `mcp/src/agents_remember/models/declared_caller.py`; `mcp/src/agents_remember/models/task_document_ref.py`; `mcp/src/agents_remember/models/terminal_catalog.py`; `mcp/src/agents_remember/serving/ambient_seat.py`; `mcp/src/agents_remember/serving/structural_seats.py`; `mcp/src/agents_remember/serving/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_task_assignment.py`; `mcp/src/agents_remember/tasks/document_refs.py` |
| Seat Retirement                     | `git-blob-set-v1` | `sha256:0ece0438f7cc57b0a1979bd4cf45e0a5ee5562b271650534bffcea219fca9cad` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/app.py`; `mcp/src/agents_remember/serving/retire.py`; `mcp/src/agents_remember/serving/retire_policy.py`; `mcp/src/agents_remember/models/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_catalog.py` |
| Seat Landing Archive                | `git-blob-set-v1` | `sha256:f3fda1e7433fdad6d64f6dd8ed51a5d6814a72b0c3b1e199498804acfa6aad19` | `dashboard/src/data/railModel.ts`; `dashboard/src/data/sessionLifecycle.ts`; `dashboard/src/panels/session-cockpit/SessionRail.tsx`; `mcp/src/agents_remember/application/worktree_tools.py`; `mcp/src/agents_remember/models/terminal_catalog.py`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/manager-brief.md`; `mcp/src/agents_remember/serving/app.py`; `mcp/src/agents_remember/serving/landing.py`; `mcp/src/agents_remember/serving/terminal_catalog.py` |
| Supervisor Sweep                    | `git-blob-set-v1` | `sha256:18cf88e232df93512f913ee00a2af56b8f3dd4ccfe7b1df7c40c3ec50731a158` | `mcp/src/agents_remember/kernel/agentic_settings.py`; `mcp/src/agents_remember/mcp/tools/base.py`; `mcp/src/agents_remember/serving/pane_signals.py`; `mcp/src/agents_remember/serving/agent_notifier_heartbeat.py`; `mcp/src/agents_remember/kernel/primitives/inbox_backoff.py`; `mcp/src/agents_remember/controlplane/operator_inbox_store.py`; `mcp/src/agents_remember/controlplane/signal_routing.py`; `mcp/src/agents_remember/controlplane/agent_notifier_signals.py` |
| Task Document                       | `git-blob-set-v1` | `sha256:b4ab813a82cbc258fe5510656d55fe86973fcf3b6e6a9b779cbe70b810b0acb8` | `dashboard/src/data/taskDocuments.ts`; `dashboard/src/data/taskHierarchy.ts`; `dashboard/src/data/taskIdentity.ts`; `dashboard/src/panels/detail-panel/DetailPanel.tsx`; `mcp/src/agents_remember/models/task_document_ref.py`; `mcp/src/agents_remember/observer/projection.py`; `mcp/src/agents_remember/observer/projection_graph.py`; `mcp/src/agents_remember/serving/projections/snapshots.py`; `mcp/src/agents_remember/tasks/document_refs.py`; `mcp/src/agents_remember/tasks/execution_graph_titles.py` |
| Delivery Injector                   | `git-blob-set-v1` | `sha256:ea4bf0985b523517ec6e3c1ad59c26470279d25a4476e3f42b5c3253adb0938e` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/harness_adapters.py`; `mcp/src/agents_remember/serving/harness_logs.py`; `mcp/src/agents_remember/serving/inbox_delivery.py`; `mcp/src/agents_remember/serving/injector.py`; `mcp/src/agents_remember/models/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_paste.py` |
| Harness Capability Snapshot         | `git-blob-set-v1` | `sha256:7cd055565ead778b24130bb9a114a178afb0364d37310474ca0290474a3f66a0` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/claude_stream_protocol.py`; `mcp/src/agents_remember/serving/codex_app_server_adapter.py`; `mcp/src/agents_remember/serving/codex_app_server_session.py`; `mcp/src/agents_remember/serving/eve_adapter.py`; `mcp/src/agents_remember/serving/eve_events.py`; `mcp/src/agents_remember/serving/eve_interactions.py`; `mcp/src/agents_remember/serving/eve_protocol.py`; `mcp/src/agents_remember/serving/eve_runtime_client.py`; `mcp/src/agents_remember/serving/eve_runtime_launch.py`; `mcp/src/agents_remember/serving/eve_stream_cursor.py`; `mcp/src/agents_remember/serving/harness_capabilities.py`; `mcp/src/agents_remember/serving/harness_capability_catalog.py`; `mcp/src/agents_remember/serving/harness_control_adapter.py`; `mcp/src/agents_remember/serving/harness_control_api.py`; `mcp/src/agents_remember/serving/harness_control_bridge.py`; `mcp/src/agents_remember/serving/harness_control_claude.py`; `mcp/src/agents_remember/serving/harness_control_client.py`; `mcp/src/agents_remember/serving/harness_control_factories.py`; `mcp/src/agents_remember/serving/harness_control_models.py`; `mcp/src/agents_remember/serving/harness_control_runner.py`; `mcp/src/agents_remember/serving/harness_launch.py`; `mcp/src/agents_remember/serving/pi_rpc_adapter.py`; `mcp/src/agents_remember/serving/pi_rpc_configuration.py`; `mcp/src/agents_remember/serving/pi_rpc_events.py`; `mcp/src/agents_remember/serving/terminal_opener.py` |
| Harness Submission Authority        | `git-blob-set-v1` | `sha256:713f1a043366c8c3c2b8dff4237aaeb50fa40dab50eab05f4b66ea2c868bfd77` | `dashboard/src/data/submissionLifecycleClient.ts`; `dashboard/src/data/submitClient.ts`; `dashboard/src/data/submitMachine.ts`; `mcp/src/agents_remember/serving/codex_app_server_adapter.py`; `mcp/src/agents_remember/serving/eve_adapter.py`; `mcp/src/agents_remember/serving/eve_protocol.py`; `mcp/src/agents_remember/serving/eve_runtime_client.py`; `mcp/src/agents_remember/serving/harness_control_adapter.py`; `mcp/src/agents_remember/serving/harness_control_api.py`; `mcp/src/agents_remember/serving/harness_control_bridge.py`; `mcp/src/agents_remember/serving/harness_control_claude.py`; `mcp/src/agents_remember/serving/harness_control_client.py`; `mcp/src/agents_remember/serving/harness_control_ipc.py`; `mcp/src/agents_remember/serving/harness_control_models.py`; `mcp/src/agents_remember/serving/harness_submission_authority.py`; `mcp/src/agents_remember/serving/harness_submission_ledger.py`; `mcp/src/agents_remember/serving/pi_rpc_adapter.py` |

## Entity Inventory

### Onboarding Unit

| Field                        | Value                                                                                                                                                                                                                                                                                                                                                |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Documentation artifact                                                                                                                                                                                                                                                                                                                               |
| Represents In Reality        | A durable unit of repository knowledge that can be retrieved and verified before an agent relies on it.                                                                                                                                                                                                                                              |
| Description                  | File-level onboarding mirrors one concrete source file; overviews summarize repo or route scopes; repo-level catalogs document recurring entities, carry deterministic evidence fingerprints, and require one fingerprint row per inventory entity. Onboarding maintenance starts from the resolved memory layer's `Domain Documentation` category for documentation evidence; live sources named there are authoritative, local mirrors are orientation caches, and refactor maintenance preserves useful onboarding before deleting or regenerating it. |
| Canonical Source Of Truth    | `c-05-create-or-update-onboarding-files` skill onboarding maintenance rules, the resolved memory layer source registry for documentation discovery, and the generated onboarding files under the resolved onboarding root.                                                                                                                                                                      |
| Current Naming Drift         | The `ar-memory-*` schema identifiers (`ar-memory-ledger/v1`, `ar-memory-candidate-pair/v1`, `ar-memory-census/v1`) retain the historical prefix as wire contracts and are not memory-mode vocabulary. Memory topology no longer has an internal/external split: external memory repos at `ar-coordination/memory-repos/ar-<repo>/` are the only supported topology, and the former repo-local `ar-memory/` internal mode was removed from the product (`CAPS-R12@v1`) and is refused by name. `repo-sidecar` survives only as a per-artifact storage placement, not as a topology.                                                                                                                                                                              |
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
| Description                  | `c-08-ar-coordination-context-resolver` skill produces this context so downstream skills do not rebuild topology rules. MCP settings own installed coordination-root authority; the package-local resolver no longer reads source-checkout `.env` or `.env.example` as coordination-root inputs. The public facade remains `coordination_context_resolver.py`, while implementation responsibilities now live under `kernel/coordination_context/`. Since 260731-EFA-L4 `CoordinationContext.memory_mode` is typed as the worktree contract's own `MemoryMode` alias rather than a second hand-written `Literal`, because `resolver.build_coordination_context` reads `contract.memory_mode` straight into the field (the code comment on that field names a `resolver._resolve` that does not exist): the resolved context and the contract share one declaration. That declaration is now **two** values, `external` and `disabled`, and it lives in `kernel/memory_mode.py` rather than in `kernel/coordination_context/models.py`; the `internal` member was removed from the product (`CAPS-R12@v1`) and is refused by name with status `memory-mode-unsupported` rather than substituted or defaulted. The repository's separate `Topology` literal has the single member `external`. No other resolved field moved. |
| Canonical Source Of Truth    | `c-08-ar-coordination-context-resolver` skill docs, the package facade, and the focused coordination-context implementation modules.                                                                                                                                                                                                                                                   |
| Current Naming Drift         | The `memory_mode` identifier is still the worktree contract's `MemoryMode` alias, but that alias now lives in `kernel/memory_mode.py` (moved out of `kernel/coordination_context/models.py` by `CAPS-R12@v1`) and holds two supported values, `external` and `disabled`; the removed `internal` member is refused by name rather than accepted.                                                                                                                                                                                                                                                                                                                                  |
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

CCR cumulative source verification: No content impact: the changed settings example adds the repository-owned certificationProfile reference. Include/exclude and storage rules retain their existing authority and behavior; a certification profile is not a path-rule replacement.

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
| Source References            | [`c-02-memory-quality-control` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md); [check.py](agents-remember/mcp/src/agents_remember/memory_quality/check.py); [check_missing_onboarding.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py); [drift.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py); [history_order.py](agents-remember/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py); [exclusion_register.py](agents-remember/mcp/src/agents_remember/memory_quality/style/citations/exclusion_register.py); [citation_index_settings.py](agents-remember/mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py); [source_index.py](agents-remember/mcp/src/agents_remember/memory_quality/style/citations/source_index.py) |
| Citation-Index Contract (260915-CAPS-L14) | The quality surface's citation index consumes a **shared exclusion register** fed by three sources — `onboarding.pathRules.exclude.paths` in the memory layer's `system/settings.json`, the code repository's `.gitignore`, and optional caller-supplied excludes on `citation_fix` / `--exclude` — and records the rule set that produced each published generation. Exceeding a cap is a **reported skip naming the file and its size**, never a silent omission and never a whole-tree refusal (developer ruling 2026-08-20: 4 MiB per file, 512 MiB aggregate over the post-exclusion/post-skip set, a ~2 GiB hard stop, settings-overridable through `onboarding.citationIndex`). The register, the caps and the settings key are **mode-independent**. This entity's evidence set gains `exclusion_register.py` and `citation_index_settings.py`; the `git-blob-set-v1` fingerprint is **not** re-signed in this pass — the leaf's source is uncommitted, so `rev-parse HEAD:<path>` cannot resolve a blob for a file that does not exist at HEAD, and the governed closeout re-derives the fingerprint over the real commit. |
| Converted-Format Dispatch (260928-MIK-L24) | On a memory tree holding `knowledge/layout.json` (the text knowledge format, MIK-R24 rule 5), `memory_quality/check.py` dispatches every selected check by format. The legacy-format checks (Update History order, citation `range_resolution` and `claim_reopen`) report `not-applicable-converted`. The drift slot runs `memory_quality/converted_check.converted_knowledge_check` instead: the knowledge validator's refusals are findings, and stale sidecar references (`memory_quality/reference_state`) are report-only, refreshed through the onboarding gate (MIK-R30). The quality controller refuses a contract-scoped run on an unconverted leaf tree whose official line is converted (rule 9). That refusal is inert until MIK-R37 converts the first line, so every run today takes the legacy path unchanged. |
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
| Represents In Reality        | A durable JSON-primary plan/checklist that projects an approved, versioned requirement corpus into executable task topology.                                                                                                                                                                    |
| Description                  | Before any sprint, master, task, or leaf document is created, the architect compiles independently falsifiable obligations into a stable ID/version index, creates one self-contained immutable packet per requirement revision, cold-reads the packets, and obtains developer approval. Task documents then project only the approved IDs, versions, and packet links; they do not rewrite the contracts. `task_doc` owns the `ar-task-document/v1` JSON source and deterministic Markdown render for `light`, `subTask`, and `master` shapes, while workflow policy may retain an existing hand-authored series master until it is intentionally migrated. Checkboxes remain the live implementation tracker. Each leaf owns one primary requirement revision, and delivery evidence plus immutable attempt/adjudication records remain requirement-bound rather than aggregate completion prose. |
| Canonical Source Of Truth    | `w-02-light-task-workflow` skill docs, workflow, task render template, and canonical requirement-packet template.                                                                                                                                                                                                     |
| Current Naming Drift         | Worktree-backed tasks live beside `contract.md` in repo-scoped task folders; non-worktree `w-02-light-task-workflow` skill artifacts can still use the resolved flat task root.                                                                                                                                         |
| Key Identifiers              | Task-document ref, `kind`, `Status`, stable requirement ID + version, canonical packet link, topology role, primary owned revision, implementation checklist, decision log, acceptance evidence, and leaf manifestation/attempt identity.                                                                                                                      |
| Parent / Child Relationships | The approved canonical requirement corpus precedes topology. Masters and leaves are filtered projections of it; task artifacts can lead to onboarding updates, but neither task prose nor onboarding may replace the requirement packets.                                                                                                                        |
| Often Confused With          | A rewritten master/leaf requirement contract, onboarding overview, entity catalog, worktree contract, acceptance envelope, or requirement-attempt summary.                                                                                                                                     |
| Source References            | [`w-02-light-task-workflow` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md); [workflow.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md); [template.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md); [requirement-packet-template.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/requirement-packet-template.md) |
| Migration Notes              | Existing hand-authored masters remain planning state until intentionally migrated; new topology must still derive from the separately approved canonical requirement corpus.                                                                                                                                                                                     |

### External Memory Ledger

| Field                        | Value                                                                                                                                                                   |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category | Computed consumer cache |
| Represents In Reality | The disposable `memory.md` representation of code attribution recorded in external-memory Git commits. |
| Description | The ledger format retains fenced metadata and newest-first code/memory rows for downstream consumers. `kernel/memory_attribution.py` reads each reachable memory commit's `Code-Commit:` trailer; `kernel/memory_cache.py` derives and materializes the view. Repeated code revisions can retain several attributed memory states, and the consumer lookup selects the newest matching row. Cached rows and headers never add mappings to Git history. Missing, malformed, unreadable or manually changed cache bytes are cache observations; they cannot request a commit or block closeout, synchronization, integration or cleanup. The actual transaction proves code/memory refs, substantive content, ancestry and ownership. Cache refresh reports updated/current/unavailable without publishing a third commit. |
| Canonical Source Of Truth | Reachable memory commit objects and their `Code-Commit:` attribution. `mcp/src/agents_remember/kernel/memory_attribution.py` owns trailer parsing/rendering; `mcp/src/agents_remember/kernel/memory_cache.py` owns derivation/materialization; `mcp/src/agents_remember/kernel/memory_ledger.py` owns the consumer format. `worktrees/ledger_projection.py` compares the optional cache with Git-derived rows; it does not union table rows into the source. |
| Current Naming Drift | The public ledger name and row format remain for consumers, but ledger status is not Git transaction authority. `ledgerCache`/cache projection results report availability or differences, not a commit or publication requirement. |
| Key Identifiers | `Code-Commit:`, selected memory tip, code/memory object IDs, `LEDGER_RELATIVE_PATH` (`memory.md`), newest-first rows, and informational cache state. |
| Parent / Child Relationships | Derived from one external-memory history and exposed to existing readers. Git worktree operations own actual output/ref evidence independently; the cache is excluded only from memory-domain content comparisons and staging. |
| Often Confused With | The actual memory-content commit, task/worktree contract, closeout mutation evidence or a separate ledger commit. |
| Source References | `mcp/src/agents_remember/kernel/memory_cache.py`; `mcp/src/agents_remember/kernel/memory_attribution.py`; `mcp/src/agents_remember/kernel/memory_ledger.py`; `mcp/src/agents_remember/worktrees/ledger_projection.py`; `mcp/src/agents_remember/worktrees/named_ref_memory.py`. |
| Migration Notes | Earlier LCA milestones temporarily retained ledger commits and source-table/trailer union; those descriptions are historical. Current readers derive only attributed Git history. The committed cache owner is included in this entity's evidence set and its recorded fingerprint refresh from `7cbda30d9a9a4c2944382fbef46ac58b85329935`. Operational migration and selected-ref publication receipts remain with the owning task, separate from this scoped catalog closure. |

Closeout readiness and recovery bind the actual code/memory candidate, task intent and Git evidence. Cache rows, cache paths and cache availability do not become a second candidate or lifecycle authority. Current output owners publish at most code and one memory-content output, then refresh the disposable ledger.

#### Current Source Evidence

- The cache derives only attributed history. [1]
- Cache write failure is reported without a Git publication. [2]
- The source reader does not import cached rows. [3]

### Sprint Closeout Queue

| Field | Value |
| --- | --- |
| Category | Disposable sprint scheduling projection |
| Represents In Reality | One bounded, source-fingerprinted materialized view of the current waiting closeout-door generations that are schedulable inside a sprint. |
| Description | Each sprint projection is derived from an exact-current census of canonical task completion-readiness, the separate `semantic-topology/v2` identity, waiting door generations, and per-contract atomic-series activation observations. Multiple live masters are valid: each canonical series contract's own record decides its state, so one `active` master may expose ready candidates while another is `reconciling` and waits on its own sync — no live master is paused, blocked, or retired by another master's selection, and waiting reasons are per contract rather than sprint-wide. Nothing serializes a graph-less sprint: a sprint without an `executionGraph` declares no dependencies, so the `atomic-sequential` default describes the sprint's shape (every commanded master executes atomically) and not a serialization mechanism; a real authored graph still gates its masters on genuine predecessors. The projection observes activation read-only; it never selects, releases, or reconciles a contract. Its service condition is only `invalid-empty` or `valid-built`; valid members are classified `ready`, `waiting`, or `blocked` and carry deterministic priority, order, and bounded reasons. Canonical task mutation publishes without queue permission, invalidates affected projections to durable empty, rebuilds off-side without consulting old rows, and publishes only if source identity remains exact-current. Graph-backed rebuild binds one admitted immutable graph generation and indexes every candidate from it. The projection owns no selection, claim, worker, commit, certification, integration, cancellation, recovery, or terminal evidence. |
| Canonical Source Of Truth | `models/closeout/projection.py` defines strict projection state/member/problem/effect models; `controlplane/closeout_queue_store.py` owns invalid-empty/valid-built persistence; `tasks/document_field_effects.py`, `tasks/semantic_topology.py`, and `tasks/semantic_topology_graph.py` own schema classification and candidate topology identity; `worktrees/queue/closeout_projection.py`, `closeout_projection_source_facts.py`, `closeout_projection_snapshot.py`, `closeout_projection_members.py`, `closeout_projection_activation.py`, and `closeout_projection_publication.py` own exact source census, explicit source planes, immutable observation, activation, member computation, and publication. `models/queue/closeout_queue.py` and `worktrees/queue/closeout_queue.py` expose only sprint-scoped status/rebuild plus the short first-ready admission fence. Task/door truth is upstream, activation is a separate disposable selector, and journal truth remains separate. |
| Current Naming Drift | Public tools and dashboard projections retain the established `closeout_queue` / `closeoutQueues` labels. Here “queue” means a disposable scheduling projection, not a durable job queue or lifecycle ledger; a projected candidate is a waiting door generation, not a claimed operation. |
| Key Identifiers | Sprint `TaskDocumentRef`, projection revision, service condition, source classification/fingerprint, explicit completion-readiness fact, `semantic-topology/v2` fingerprint, immutable graph generation, bounded source problems, door generation id, candidate and owning-master refs, contract path, candidate tree, source-door fingerprint, member classification, effective priority, order, and reasons. No operation generation, worker identity, commit tuple, certification, or lifecycle owner fingerprint belongs here. |
| Parent / Child Relationships | Belongs to one sprint and is rebuilt from current task, door, and activation truth. A short task/door publication CAS may require the exact first-ready generation at claim admission; after claim, the door and enclosure-external operation journal own lifecycle evidence. Task authoring remains authoritative and can invalidate/rebuild affected projections without queue or activation permission. |
| Often Confused With | The sprint task document, per-contract atomic-series activation, a closeout-door generation, Judgment/Priority Registers, the operation journal, a generic durable job queue, the external-memory ledger, the landing lane, or the terminal archive. |
| Source References | `mcp/src/agents_remember/controlplane/closeout_queue_store.py`; `mcp/src/agents_remember/models/closeout/projection.py`; `mcp/src/agents_remember/models/queue/closeout_queue.py`; `mcp/src/agents_remember/tasks/document_field_effects.py`; `mcp/src/agents_remember/tasks/semantic_topology.py`; `mcp/src/agents_remember/tasks/semantic_topology_graph.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_source_facts.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_snapshot.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_members.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_activation.py`; `mcp/src/agents_remember/worktrees/queue/closeout_projection_publication.py`; `mcp/src/agents_remember/worktrees/queue/closeout_queue_graph.py`; `mcp/src/agents_remember/worktrees/queue/closeout_queue.py` |
| Migration Notes | Introduced by 260815-DAG and completed by 260821-CLIVE L3. The transitional selected/in-flight/certified rows, task-document queue veto, blocker/lifecycle commands, and `closeout_queue_lifecycle.py` owner were removed rather than retained behind compatibility readers. The direct IAS repair replaces single-live-series assumptions with read-only per-contract activation, and the LOCR-L36 re-key moved that selector's key from the protected source pair to the canonical series contract. 260831-CCR-L01 replaces the queue-private whole-document/v1 topology digest with explicit completion-readiness and task-domain `semantic-topology/v2` planes plus one immutable bounded graph index; no fallback reader remains. Current rebuild never consumes stale rows, and lifecycle evidence survives only at its door/journal owners. |

CCR cumulative source verification: The current source census binds canonical task intent separately from semantic-topology/v2 and completion readiness. A waiting door with absent or different intent is blocked with explicit unavailable/stale reasons. The immutable graph generation supplies both topology and member construction; unclassified task fields or malformed intent refuse a rebuild. Scheduling remains a disposable projection and acquires no certification or Git mutation authority.

### Closeout Effective Input

| Field | Value |
| --- | --- |
| Category | Lifecycle admission entity |
| Represents In Reality | The one accepted statement of which closeout commit legs apply and the exact explicit message for every enabled leg. |
| Description | Raw public observations are normalized once against a lease-stable route, contract, and code candidate. An ordinary leaf's code candidate is plane-derived as the configured base plus stable observed HEAD plus the canonical isolated-index full add-all tree; callers never supply that authoritative tree, each concurrent observation has a distinct automatically cleaned index, and derivation never stages the real index. The resulting identity is immutable. The closeout input contains typed `code` and `memory` legs: enabled legs carry stripped nonblank explicit messages; not-applicable legs carry reasons and no sentinel message. Worktree closeout persists this value in the lifecycle operation; entry returns it once and every preview, fingerprint, worker, code, external-memory, resume, and recovery consumer receives that exact typed value explicitly rather than rereading optional transport or creating shadow intent. Direct landing shares the contract for verified-existing code plus enabled external-memory content intent only for an explicitly selected leaf delivery without an enclosure; ordinary master/series closeout and integration are separate lifecycle routes and never require the direct-execution policy flag. |
| Canonical Source Of Truth | `models/closeout/input.py` defines the leg vocabulary; `memory_quality/future_code_candidate.py` owns ordinary-leaf future-code identity; `worktrees/closeout_input.py` owns plan derivation, candidate adaptation, and normalization; `worktrees/integration/closeout/operation_admission.py` owns lease-stable durable admission. |
| Current Naming Drift | Public code may call the raw shape messages or commit-message input, while durable code calls the result `effectiveInput` / `EffectiveCloseoutInput`. Only the latter may cross below validation. |
| Key Identifiers | Route, resolved plan, code/memory leg state, explicit message, reason, observed code HEAD, configured code base, full add-all candidate tree, HEAD tree, invalid field observation, corrected call, candidate fingerprint. |
| Parent / Child Relationships | Created from a worktree contract and plane-derived stable Git candidate; embedded in one closeout lifecycle generation; consumed by mutation evidence owners. Candidate acceptance identity does not replace the lifecycle journal's separate operation/mutation identity. Queue selection is neither parent nor authority. |
| Often Confused With | Optional public JSON-schema fields, blank-message defaults, generated commit subjects, queue candidate declarations, or the legacy raw `WorktreeArgs` message fields. |
| Source References | `mcp/src/agents_remember/models/closeout/input.py`; `mcp/src/agents_remember/memory_quality/future_code_candidate.py`; `mcp/src/agents_remember/worktrees/closeout_input.py`; `mcp/src/agents_remember/worktrees/integration/closeout/operation_admission.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_candidate.py`; `mcp/src/agents_remember/application/worktree_tools.py`; `mcp/src/agents_remember/worktrees/direct_landing.py` |
| Migration Notes | Introduced by 260821-CLIVE-L1 as a replacement, not a compatibility layer. Raw strings stop at admission; there is no ledger message/leg, generated subject or empty enabled sentinel. CLIVE L2 implements the public task-addressed retry/recover/cancel/revise controls while preserving this input unchanged within one generation. MCAR-L02 adds the exact future-code identity owner without weakening the existing operation-journal reconciliation boundary. |

CCR cumulative source verification: Current closeout and direct-landing admission additionally bind the canonical task-intent identity into the operation candidate and require it to equal the claimed door and any retained journal. Missing or stale intent cannot be filled from a plausible legacy value. This is separate from normalized commit messages, the future add-all code tree, and the configured certification profile. The configured worktree service bundle now installs PreparedCloseoutContinuation: selected original code certificates feed private code preparation, the real memory producer, and finalization. Effective input remains the immutable message/leg authority; it is not a substitute for those certificates or output proofs.

The ledger cache is not an enabledness choice or an input message. Disabled memory stays not-applicable, and unchanged actual memory may be reused without inventing another commit.

#### Current Source Evidence

- The normalized input and message vocabulary contain only code/memory. [4]

### Curator Coherence Authority

| Field | Value |
| --- | --- |
| Category | Candidate acceptance authority |
| Represents In Reality | The sole live leaf-scoped selection of exact curator judgments for one code tree, memory tree, task topology, memory-quality attestation, and delivery attempt. |
| Description | A configured external-memory leaf exposes one stable structured manifest. It selects one immutable content-addressed record whose exact source-candidate tuples equal its recorded judgment tuples. Each agent-owned disposition and rationale keeps its explicit code, memory, or task citation and lifecycle digest. New publication additionally stamps the existing path/SHA/size artifact value for retained judgment custody. Historical integrity uses retained bytes; live readiness still checks the original inputs. The record keeps semantic requirement revision, worker delivery attempt, code/memory candidate trees, attestation digest, record digest, and predecessor-authority digest separate. Its Markdown is deterministic human projection only. Status and prepare can observe an absent, stale, or malformed predecessor; publish validates the newly retained generation before exact CAS writes the stable selector last; validate re-proves current code, memory, topology, attestation, evidence, record, and projection. Graph-backed task observation supplies the authored graph once and fingerprints the same bound immutable sprint generation used by the door and projection. Since 260915-KS-L15 the record also carries a **second typed collection beside `judgments`**: the `ReviewAssessment` rows, an authored curator judgment with an identified author, a role, one of three closed dispositions and a binding to the exact inputs it examined. The collection is separate because a judgment's identity is the `(sourceFile, onboardingFile, classification)` triple while an assessment's subject is a knowledge record, a family, an invariant revision or a comparison — none of which is a source-file pair — so `_judgments_cover_candidates_exactly` stays the only rule relating judgments to candidates and is untouched. The record declares one `review-record` edge per stored assessment, recomputed from the record the edge points at; the assessment's own binding declares the inputs it examined and deliberately does not declare the record it lives in, which keeps the binding out of the self-invalidating sequence. Assessment evidence bytes publish to `<task_root>/notes/reports/evidence/<assessment_id>/<filename>`, outside the worktree group terminal cleanup removes and outside the terminal archive's fixed artifact set. |
| Canonical Source Of Truth | `models/lifecycles/curator_coherence.py` defines the strict record family and the `assessments` collection; `models/lifecycles/review_assessment.py` defines the assessment record and its read states; `models/lifecycles/review_assessment_binding.py` owns binding currentness; `models/lifecycles/review_assessment_store.py` builds the exact-input declaration and the record's edges; `worktrees/integration/closeout/curator_coherence.py` owns live selection/currentness; `curator_coherence_paths.py` owns explicit paths/namespaces; `curator_coherence_records.py` owns digest-addressed durable integrity; `curator_coherence_judgments.py` binds exact agent decisions and evidence bytes; `curator_coherence_publication.py` owns status/prepare/publish/validate and atomic CAS; `worktrees/integration/closeout/curator_assessment_evidence.py` owns the evidence-byte destination and its read-back; `curator_coherence_render.py` owns the one-way projection; `application/curator_coherence.py` owns configured failure translation. |
| Current Naming Drift | Historical task files may be named `*-curator-report.md` or `*-curator-report-v2.md`, but those are historical Markdown artifacts, not authority and not compatibility inputs. “Coherence report” in human discussion means the generated projection plus its selected structured record. A “review assessment” is not a judgment: a judgment is a per-source-candidate agent disposition, an assessment is an authored statement about a family, invariant revision, comparison or knowledge record with its own binding, and the two live in separate collections on purpose. |
| Key Identifiers | Leaf id and contract path; semantic requirement revision; delivery attempt; code and memory candidate trees; task-topology fingerprint; attestation and report digests; exact source tuple; disposition/rationale/evidence reference and digest; publication fingerprint; predecessor authority digest; record/report/snapshot paths and digests. Assessment identities add: assessment id and subject id; the four subject kinds; the closed disposition; the four reportable states (`none-recorded`, `unresolved`, `stale`, `current`); the exact-input declaration under the `review-assessment/v1` policy; and each cited evidence byte's task-root-relative path, digest and size. |
| Parent / Child Relationships | Prepared from the contract-resolved code/memory worktrees, canonical composite leaf topology, one bound immutable graph generation when applicable, and enclosure-local `ar-curator-memory-quality/v1` attestation. Public memory readiness, closeout-door evidence, and closeout admission are sibling consumers of the same validator. Optional attempt snapshots point to immutable generations. The closeout operation journal remains the separate owner of Git mutation and commit lifecycle evidence. |
| Often Confused With | A semantic requirement version, worker attempt journal, memory-quality checklist, task evidence link, hand-authored Markdown report, closeout queue row, closeout door generation, or operation journal. |
| Source References | `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_records.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_paths.py`; `mcp/src/agents_remember/models/lifecycles/curator_coherence.py`; `mcp/src/agents_remember/models/lifecycles/review_assessment.py`; `mcp/src/agents_remember/models/lifecycles/review_assessment_binding.py`; `mcp/src/agents_remember/models/lifecycles/review_assessment_store.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_assessment_evidence.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_judgments.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_publication.py`; `mcp/src/agents_remember/worktrees/integration/closeout/curator_coherence_render.py`; `mcp/src/agents_remember/application/curator_coherence.py` |
| Migration Notes | MCAR-L02 A005 replaces the split A003 stable Markdown/A004 `-v2` artifact model. It deliberately adds no filename search, Markdown parser, or duplicated compatibility authority. 260831-CCR-L01 makes graph-backed task observation generation-coherent by carrying the one bound immutable sprint graph rather than resolving a second mutable copy. 260915-KS-L15 adds the assessment collection to this authority rather than to the assessed knowledge database: the record has no self-invalidating binding there, and the coherence authority is the same canonical route the judgments already publish through. |

CCR cumulative source verification: Current publication and validation also bind taskIntent and explicit EvidenceDependencies. The memory-quality attestation declares the exact candidate pair, code tree, memory tree, report bytes and validator identity; coherence additionally declares semantic topology, leaf intent, attestation/report bytes, judgment evidence and any predecessor authority. Missing or stale edges refuse currentness and require fresh publication. Legacy missing-intent records can be decoded for observation but are not accepted as current authority. This existing coherence validator does not itself execute the unconnected R07 affected closure or R08 final-full certification flow.

260915-KS-L15 assessment extension, recorded against the measured tree: the review-assessment modules are
**not yet at `HEAD`** in this leaf's code worktree (all three are untracked, added by the uncommitted
change set), so the `git-blob-set-v1` evidence set above is deliberately left at the six committed
paths: `compute_git_blob_set_fingerprint` resolves `HEAD:<path>` for every evidence path, and naming an
untracked path there would make the row unrefreshable rather than more accurate. Adding the assessment
modules to the evidence set and recomputing the fingerprint is therefore the first closeout-owned step
after the code commit lands, and it is recorded here so the next curator does not read the six-path set
as an omission. The three new modules are named in `Canonical Source Of Truth` and
`Source References` above, which the drift check reads as prose rather than as fingerprint evidence.

### Closeout Mutation Evidence

| Field | Value |
| --- | --- |
| Category | Durable lifecycle evidence entity |
| Represents In Reality | Per-enabled-leg proof of the exact repository state before, during, and after a journaled worktree-closeout Git mutation. |
| Description | Each enabled repository leg advances through `pre-mutation`, `mutation-intent`, `reconciled-unchanged`, or `commit-proven` evidence bound to branch/ref, HEAD/tree, reflog fingerprint, index/candidate trees, and worktree status. Intent is journaled before Git; commit proof validates the exact ref/parent/tree transition. After restart, exact unchanged state is distinguished from exact expected output and from ambiguity such as a ref moving away and back. A public retry of unchanged intent preserves attempt one, does not launch implicitly, and remains cancellable; status or reflog observation failure leaves the literal journal and evidence unchanged. A cancelled generation advances only through the current contract-owned waiting door plus cancelled disposition and worker-exit proof; historical door rows remain audit evidence rather than a uniqueness authority. Commit-proven evidence supplies the actual code/memory recovery tuple, while exact canonical contract-publication proof retains verified-existing/no-op generations without fabricated Git mutation evidence. |
| Canonical Source Of Truth | `models/lifecycles/mutation_evidence.py`, `worktrees/integration/mutation_evidence.py`, `worktrees/integration/closeout/recovery_projection.py`, and the strict lifecycle operation store. |
| Current Naming Drift | Recovery commits are actual output references backed by Git/journal proof, including explicitly verified-existing output. Cache state is a separate consumer observation and has no mutation leg or ledger commit alias. |
| Key Identifiers | Code/memory leg, repository, state, before/observed snapshot, actual HEAD/ref/tree, memory `contentHeadTree`, expected output tree, commit proof, operation key/generation, recovery tuple and finalized contract SHA-256. |
| Parent / Child Relationships | Belongs to one journaled closeout operation generation and its accepted effective input. It owns recovery projection; the queue consumes only downstream lifecycle outcomes. |
| Often Confused With | Progress phase, approval claim, irreversible boolean, queue row state, a nonblank recovery cell, or direct-landing lock ownership. |
| Source References | `mcp/src/agents_remember/models/lifecycles/mutation_evidence.py`; `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py`; `mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py`; `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operations.py` |
| Migration Notes | CLIVE introduced journaled mutation evidence and direct-landing recovery. The LCA retirement removes ledger intent and commit/recovery cells; both actual output proofs remain. Memory-domain snapshots retain raw HEAD/tree identity while excluding root `memory.md` from substantive content. Prepared reuse independently binds the existing raw tree and its certified content tree; cache-only changes do not require a mutation. |

Evidence-path reconciliation (2026-09-11): this entity is retained. Its former evidence path `mcp/src/agents_remember/application/lifecycle/lifecycle_operation_worker.py` was deleted with the detached lifecycle worker by commit `173bb01e`, which moved the mutation-evidence record advance and its transition validation into `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_store.py`. That successor module was already an evidence path, so the row was repaired by dropping the deleted path and recomputing the `git-blob-set-v1` fingerprint rather than by retiring the entity. The door, worker-lease and journal passages retained above were not re-derived in this pass and should be re-read against the synchronous closeout route before being treated as current.

CCR cumulative source verification: The journal now separates recordRevision, advanced on durable changes, from meaningfulRevision, advanced only for the defined wait-relevant state changes. Transforms cannot assign those revisions. Commit operations also bind immutable task intent and explicit input/door/tree/policy dependencies before worker launch; terminal legacy missing-intent generations are archived exactly before a canonical successor, while active missing-intent reuse refuses. These journal transitions remain separate from finalization-certificate authority. The installed preparation continuation now consumes the selected original certificates and exact prepared outputs; it revalidates worker, contract, approval and logical refs before publication. Unexpected worker failure is translated through the terminal rail-failure projection without inventing Git commit proof.

#### Current Source Evidence

- Raw Git facts and the filtered memory-content head are separate fields. [5]
- The recovery tuple contains only actual code and memory outputs. [6]
- Recovery verifies refs/ancestry before cache refresh. [7]

### Memory Baseline Adoption

| Field | Value |
| --- | --- |
| Category | External-memory adoption operation |
| Represents In Reality | Explicit adoption of existing external-memory content into attributed Git history. |
| Description | The c10 skill resolves context, reports drift and requires acceptance of actionable drift before adoption. `memory/baseline.py` detects an existing adoption from reachable attribution, validates the checked-out repository-default branch, creates the attributed content output and refreshes the consumer cache. Cache presence or parseability does not establish adoption and no ledger commit is produced. |
| Canonical Source Of Truth | `skills/c-10-adopt-memory-baseline/SKILL.md`, `mcp/src/agents_remember/memory/baseline.py`, and Git attribution through `kernel/memory_cache.py`. |
| Current Naming Drift | Earlier wording called this the first ledgered baseline; current result fields are `memoryContentCommit` and informational `ledgerCache`. |
| Key Identifiers | Repository/default branch, exact code source commit, actual memory-content commit and attributed history. |
| Parent / Child Relationships | Adopts existing external-memory content; it does not author or semantically refresh that content. Its ledger result is the same disposable cache other consumers read. |
| Often Confused With | Onboarding bootstrap, refreshing stale onboarding, a history backfill, or committing a ledger table. |
| Source References | `skills/c-10-adopt-memory-baseline/SKILL.md`; `mcp/src/agents_remember/memory/baseline.py`; `mcp/src/agents_remember/kernel/memory_cache.py`. |
| Migration Notes | Existing attributed history makes another initial adoption invalid. A missing cache alone does not reopen adoption. This entity is included in the recorded 11-entity fingerprint refresh from committed `7cbda30d9a9a4c2944382fbef46ac58b85329935`. |

#### Current Source Evidence

- Adoption creates the memory-content output and refreshes its cache. [8]
- Adoption status is derived from Git attribution. [9]

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

260831-LOCR-L17: the evidence path `mcp/src/agents_remember/serving/app.py` is in this entity's
curated set and changed in this leaf, so the row is refreshed here as a reconciliation rather than a
fingerprint edit. The leaf adds one composition value to `_build_serving_runtime` — a single
`serving_clock` shared by the sweeper, the runtime and the new observer-health publisher, plus that
publisher on `_ServingRuntime` — and changes nothing about landed status, cleanup outcome,
dashboard identity, retention, or the archive's own boundary. **The evidence path set is unchanged
and no fingerprint value was hand-edited**; `git-blob-set-v1` cannot be derived by inspection, so it
is recomputed from the landed commit at closeout. No acceptance claim is made.

260831-LOCR-L36 second pass: the evidence path
`mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md`
changed in the L36 skill rewrite that regenerated the package-data copy, so the entity is consistent
with the corrected orchestrator text rather than the retired rule. The corrected role document now
says "Per-contract activation records each master's own `reconciling -> active` transition and
serializes nothing across masters", that queue rows "only project each contract's own active/
reconciling waiting facts", and that the atomic pre-move step must "require the master's own contract
activation to be `active`" — i.e. per-contract activation with nothing serialized across masters.
That is consistent with this archive's landed-status, cleanup-outcome, dashboard-identity and
retention semantics: a master's landing no longer depends on being the single selected master of a
protected source pair. That earlier pass left the evidence path set unchanged; the fingerprint has
since been refreshed from committed `7cbda30d9a9a4c2944382fbef46ac58b85329935` in the recorded 11-entity refresh.

260915-CAPS-L1 — **quoted text rebased; the invariant is preserved.** The same L36-quoted sentences no
longer exist verbatim in the rewritten orchestrator role: a `grep` for all three quoted strings
(`serializes nothing across masters`, `only project each contract`, `require the master`) now returns
zero hits. The rule they carried survives in the current shipped wording, so this section is rebased
rather than retired: the role now states the graph-less default as "canonical commanded order as the
stable tie-break, **no serialization across masters, none retired**" (`roles/orchestrator.md:155-157`),
and the dispatch step as "The control plane publishes **each contract's own** `reconciling → active`
activation before implementation exposure" (`roles/orchestrator.md:187-189`), with an **`atomic`** master
requiring "their own activation `active`" before it integrates and lands
(`roles/orchestrator.md:229-232`). The claim this archive makes is unchanged and still holds: landing
depends on the master's **own** per-contract activation, never on being the single selected master of a
protected source pair. Evidence path sets and the stored fingerprint are untouched — no value was
hand-advanced, and the catalog's `git-blob-set-v1` algorithm resolves committed `HEAD` blobs, which this
uncommitted working-tree rewrite does not move.

`No content impact:` 260815-DAG-L2 changes planning and landing authority prose in shared role
evidence, but it does not change the archive's landed status, cleanup outcome, dashboard identity,
or retention semantics.

`No content impact:` 260815-DAG-L3 adds pre-closeout scheduling and lifecycle ownership but does
not change the archive's landed result, cleanup outcome, dashboard identity, or retention rules.

`No content impact:` 260821-CLIVE-L1 changes `application/worktree_tools.py` closeout admission
from raw messages to normalized effective input. That shared evidence path changes the fingerprint,
but it does not change archive identity, landed status, cleanup outcome, or retention semantics.

CCR cumulative source verification: No content impact: the changed shared application paths add requirement-reader route registration, task-intent refusal translation and certification-profile propagation. They do not change archive identity, landed state, cleanup results, or retention policy.

### Seat Retirement

Entity inventory entry; current evidence and fingerprint are recorded above.

260831-LOCR-L17: the same `serving/app.py` change touches this entity's curated evidence set (that
file is one of its six paths), so the row is reconciled here. The leaf's edit is composition only —
one shared serving clock and one observer-health publisher wired onto the serving runtime — and it
adds no retirement route, policy, or terminal-catalog behaviour: retirement authority, its refusal
shapes, and the catalog evidence blobs are untouched. **Evidence path set unchanged; no fingerprint
was hand-edited**, and closeout recomputes the stored value from the landed commit. No acceptance
claim is made.

CCR cumulative source verification: No content impact: the sole changed fingerprint source, serving/app.py, registers requirement-reader routes. Retirement policy and terminal-catalog evidence blobs are unchanged from the prior IAS candidate.

### Supervisor Sweep

Entity inventory entry; current evidence and fingerprint are recorded above.

`No content impact:` 260815-DAG-L3 appends one public tool name through shared MCP registry
evidence. It does not alter supervisor predicates, delivery, cooldown, heartbeat, or escalation.

CCR cumulative source verification: No content impact: the shared public-tool registry adds worktree_status_wait. The listed sweep, signal, heartbeat, backoff and inbox evidence blobs are unchanged; the read-only wait tool introduces no sweep or escalation owner.

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

CCR cumulative source verification: No content impact: the changed detail-panel source imports the existing reader target type from its task-artifact owner. This does not alter task JSON authority, durable document references, execution-graph meaning or topology publication. Canonical task intent is separately consumed by the closeout admission and projection entities described here; a reader type import is not its authority.

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

`Direct IAS contract-scoped activation impact:` atomic start, attach, and implementation dispatch
admit work only after *that contract's own* activation record has reconciled against the exact current
code and memory sources. Selection is keyed by the canonical series contract, so two atomic masters
commanded by one sprint share the protected source pair yet hold independent records, and another
master's selection never pauses this one. Selecting a contract does not rewrite lineage or retire any
contract, worktree, task, chat, or journal.

`260915-CAPS-L1 reconciliation:` the corpus consolidation rewrote the two role files this entity cites
as evidence — `roles/manager.md` and `templates/curator-brief.md` — into the corpus's readable order
(and remounted `roles/manager.md` under a thin router with a new shared `core/`), so both citations were
re-read against the rewritten sources. The lineage facts this entry asserts are unchanged and still
hold: a manager still requires its master's own contract activation before dispatch, task-document
mutation remains upstream of runtime selection, and the recovery/backoff paths this entity names are
untouched. No evidence path changed and no fingerprint was hand-advanced — the catalog's
`git-blob-set-v1` algorithm resolves committed `HEAD` blobs, which this uncommitted rewrite does not
move. Recorded here because the entity's cited evidence moved while its meaning did not.

CCR cumulative source verification: No content impact on ancestry: the changed status model adds bounded lifecycle status-wait projection, and closeout/integration now receive the configured certification profile. The source_lineage owner and its ancestry rules are unchanged. Canonical task intent and certification identities remain separate checks, not alternative lineage evidence.

### Worktree Contract

| Field | Value |
| --- | --- |
| Category | Worktree lifecycle contract |
| Represents In Reality | The canonical address and repository/branch/base/output facts of one leaf or series enclosure. |
| Description | The contract records actual code and memory-content closeout/integration outputs. `ledger_path` remains a consumer-cache location, but no ledger commit or integrated-ledger commit is part of lifecycle state. Candidate and publication owners separately prove Git state; a cached mapping cannot fill a missing output. |
| Canonical Source Of Truth | `mcp/src/agents_remember/worktrees/worktree_contract.py`; `contract_publication_text` normalizes and validates the serialized contract. |
| Key Identifiers | Exact contract path; code/memory repositories, worktrees, branches and bases; `code_commit`, `memory_content_commit`, `integrated_code_commit`, `integrated_memory_content_commit`. |
| Parent / Child Relationships | A series/leaf contract addresses its enclosure; the operation journal retains mutation evidence and the cache reports derived consumer data. |
| Source References | `mcp/src/agents_remember/worktrees/worktree_contract.py`; `mcp/src/agents_remember/worktrees/modules/closeout_external.py`; `mcp/src/agents_remember/worktrees/modules/landing_record.py`. |

#### Historical milestone context

The following dated ownership notes preserve their original milestone context. Current ledger/output authority is the code/memory contract above.

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

`Direct IAS contract-scoped activation impact:` the contract remains the public durable address for
sync and for its own activation record — `activation_path` is derived from the contract fingerprint —
while `.lifecycle/sync-operation.json` at the enclosure root owns resumable transaction state
independently of task-document readability. Conflict worktrees under `.sync/` and pinned
`refs/agents-remember/sync/<digest>/...` are operation evidence, not contract fields, queue rows, or
fallback lookup surfaces.

`260831-DER route impact:` a root series contract does not by itself select direct execution.
Ordinary series integration records absent source-door authority as `not-applicable`; only an
explicitly selected leaf delivered without an enclosure uses policy-gated direct landing.

CCR cumulative source verification: Current contract publication additionally requires digest-bearing task intent on every attached closeout door. A legacy door without it remains an explicit provenance-repair case and cannot be republished unchanged. Profile selection is supplied from repository configuration to execution; it does not become an invented duplicate contract field. Existing canonical serialization, root-manifest and exact branch-address authority remain the owners.

#### Current Source Evidence

- The contract stores the actual two outputs and informational cache location. [10]
- One normalizer/validator owns contract serialization. [11]

### Worktree Integration

| Field | Value |
| --- | --- |
| Category | Guarded Git publication operation |
| Represents In Reality | Publication of accepted code and external-memory content to the exact integration/source refs. |
| Description | Admission proves the actual code/memory outputs, expected source heads, fast-forward ancestry and substantive checkout cleanliness. Ref publication uses expected-old compare-and-swap and retained recovery evidence. A checkpoint captures an unfinished master's actual tips. Ledger rows, cached headers and cache availability neither select output commits nor gate publication. Cleanup proves the actual code and memory output reached their official source refs. |
| Canonical Source Of Truth | `worktrees/modules/integrate.py`, `worktrees/integration/integration_ref_transaction.py`, `worktrees/series_closeout.py` and `worktrees/modules/guidance.py`. |
| Key Identifiers | Exact code/memory output commits, source refs and heads, contract identity, checkpoint candidate and journal generation. |
| Parent / Child Relationships | Consumes closeout or checkpoint output authority; writes the contract's integrated code/memory cells. Consumer cache refresh is independent of the paired Git transaction. |
| Source References | `mcp/src/agents_remember/worktrees/integration/integration_ref_transaction.py`; `mcp/src/agents_remember/worktrees/series_closeout.py`; `mcp/src/agents_remember/worktrees/modules/guidance.py`. |

#### Historical milestone context

The following dated notes preserve earlier lifecycle/certification wiring; their ledger and queue-claim language does not define the current Git publication contract above.

`260815-DAG-L3 route impact:` a graph-managed leaf must be selected, closeout-certified, and still
current before integration claims the lane. The final source move revalidates the same candidate
facts under queue/task locks, consumes the candidate on success, and releases recoverable
pre-boundary failures through the task-addressed lifecycle rather than a public operation key.

`260815-DAG-L4 route impact:` integration is now a cross-operation-leased, journal-bound named-ref
transaction. Exact expected-old CAS, external-memory content ancestry, pair rollback and
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

`Direct IAS contract-scoped activation impact:` cleanup, finalize, and abandon release only the
terminal contract's own activation record. The release is addressed by that contract, so it cannot
clear, pause, or retire another contract's selection, and another contract's newer selection never
blocks this release. Cancellation rolls back both sync sides from pinned pre-sync refs and durably
publishes `vacant` for that contract; integration does not acquire selector or queue lifecycle
ownership.

`260831-DER route impact:` a fresh ordinary series integrates without a leaf closeout door and
records that source-door authority as `not-applicable`, independently of `directExecutionEnabled`.
Fresh leaf integration still requires its exact claimed closeout source, and retained no-door
journal recovery stays bound to its existing generation rather than becoming fresh admission.

CCR cumulative source verification: Current execution routes the repository-owned certification profile into the altitude-owned quality gate. Series integration still owns the full code-quality run; leaf integration consumes its existing closeout authority. The named-ref transaction, expected-old checks, memory ancestry, rollback and recovery owners remain unchanged. Earlier queue-claim wording above is historical: the disposable queue does not own lifecycle certification. The production service bundle now wires the preparation continuation through real memory certification and exact prepared-output finalization. Series integration still owns its aggregate code-quality route; this connection does not turn leaf integration or a memory readiness observation into an aggregate acceptance pass.

#### Current Source Evidence

- Admission checks actual sources, ancestry and content before refs move. [12]
- Carryover/cleanup readiness proves both outputs reached their official sources. [13]

## Ownership Notes

- This catalog intentionally excludes the eight worktree task files as onboarding subjects.
- This catalog treats `mcp/src/agents_remember/package_data/runtime/agents-md-files/` as the package source for runtime `AGENTS.md` templates. Memory repos use `system/*` guidance files rather than root-level `AGENTS.md` files.
- Roadmap specs are cataloged only where they define active current design concepts that explain the repository's direction.
- Legacy roadmap specs remain historical context where they disagree with the implemented memory/coordination split.


### Ledger-Retirement Fingerprint Follow-Up

The six affected fingerprint values remain the prior committed baseline. Once the actual code candidate exists, refresh their reviewed evidence against that commit. The External Memory Ledger row now uses the focused current owners `mcp/src/agents_remember/kernel/memory_attribution.py`, `mcp/src/agents_remember/kernel/memory_cache.py`, `mcp/src/agents_remember/kernel/memory_ledger.py` and `mcp/src/agents_remember/worktrees/ledger_projection.py`; `memory_cache.py` has no committed blob in the reviewed base. Its retained digest is intentionally stale for the changed set until the actual committed-source refresh. The other five affected sets also require a committed-source refresh after their reviewed code changes.

### Knowledge-Storage Entity Deferral (260915-KS-L1)

This leaf adds a load-bearing cross-layer entity: the **knowledge invariant revision** — the immutable, sealed,
separately addressable authored revision aggregate stored by `memory/knowledge/`, whose identity is a repository
scoped namespace plus an opaque revision id, and whose content seal covers the whole authored payload including
its sorted predecessor set. It spans `models/knowledge/` (vocabulary), `memory/knowledge/` (storage),
`application/knowledge.py` (composition) and `kernel/canonical_json.py` (the encoder the seal is computed
through), which is the profile this catalog exists to record.

**No inventory entry and no fingerprint row are added in this pass, and that is deliberate.** A
`git-blob-set-v1` fingerprint resolves `HEAD:<path>` blobs, and every file that would evidence this entity is
**uncommitted** in the leaf's code worktree. Writing a fingerprint row now would either fail to resolve or
advance a fingerprint onto a tree that does not exist yet, which the curator seat is explicitly forbidden to do.
The entity is therefore recorded here as a deferred row with its evidence set named, and the refresh is owned by
the closeout/index transaction that commits the code:

| Deferred entity | Evidence paths for the refresh |
| --- | --- |
| Knowledge invariant revision | `mcp/src/agents_remember/models/knowledge/invariant.py`; `mcp/src/agents_remember/models/knowledge/digest.py`; `mcp/src/agents_remember/memory/knowledge/schema.py`; `mcp/src/agents_remember/memory/knowledge/store.py`; `mcp/src/agents_remember/memory/knowledge/records.py`; `mcp/src/agents_remember/application/knowledge.py`; `mcp/src/agents_remember/kernel/canonical_json.py` |

Two conditions make the refresh complete rather than nominal: the row needs a committed source blob for every
path in its evidence set, and its `## Entity Inventory` entry must be written in the same pass, because
`c-02-memory-quality-control` skill reconciles the fingerprint table against the inventory and treats a missing
row or an orphaned row as actionable maintenance. The subsystem's own account of current intent lives in the file
cards under `onboarding/mcp/src/agents_remember/{models,memory}/knowledge/` and in
[`memory/overview.md`](mcp/src/agents_remember/memory/overview.md) meanwhile, so a reader is not left without a
route while the fingerprint is pending.

### Preserved Fragment From Prior Catalog Truncation

Before this scoped edit, the baseline entity's source row contained a literal truncation marker and ran into unrelated harness-submission projection rows. The baseline entry is now coherent; the surviving unrelated fragment is preserved verbatim below rather than reconstructed or promoted as current baseline behavior. Other missing catalog bodies were not reconstructed by this ledger task.

```text
…37697 tokens truncated… discloses exact per-id source/state/timestamps/vendor-correlation (1..64 unique ids, epoch-checked, honest not-found) to the exact-session daemon peer over the same private socket, delegated bridge → queue → authority as the sole path. The L2E additive `operation-timeline` read follows the same delegation (paged, never bodies, epoch-checked end to end), the additive `interrupt` write crosses the same socket epoch-guarded with a bridge-stamped epoch, and the additive `assets` submit key admits only schema-validated, spool-confined, sha256-verified references. Since L4 every one of these routes declares its success and refusal bodies as strict `extra="forbid"` wire models (`serving/response_contract.py`, and `serving/conversation/response_contract.py` for the conversation half); because the handlers answer with `Response` objects, FastAPI validates none of it and `test_serving_response_conformance.py` carries the enforcement. |
| Server authority | One timeline for prompt/model/effort; atomic queued-withdraw versus dispatch; full operation refs; early terminal dominance; response bypass; 64/256 live-safe retention. L2E: the retained ledger enumerates in bounded never-bodies pages whose eviction floor is tracked at the sole pop site; the withdrawal recovery body is captured pre-tombstone at the one true transition; the idempotence digest extends over canonical asset identity only when assets ride. |
| Native adapters | Codex fresh-turn guarded write with bounded correlation; Claude sole accepted operation and shared lock; Pi fresh-state token guard and settled-plus-fresh-idle completion. No native queue is authority. |
| User recovery | Alt+Up requests exact withdrawal; unchanged drafts auto-restore by revision CAS, concurrent edits create one explicit recovery slot, and replace/keep-current/dismiss are local exact decisions. |
```

### Knowledge Candidate-Change Boundary Deferral (260915-KS-L3)

This leaf adds a second load-bearing cross-layer entity: the **knowledge candidate-change boundary** — the single
typed, all-or-nothing write operation the rest of the knowledge substrate mutates through. One admitted candidate
context plus a `ChangeBatch` (expected context, explicit expected-record identities, a closed twelve-command union)
becomes a `MutationResult` under one resource lock and one `BEGIN IMMEDIATE` transaction, with every refusal leaving
the stored dataset unchanged. It spans `models/knowledge/` (the context, command union, batch and receipt
vocabulary), `memory/knowledge/` (the operation, its preconditions, its apply step and the canonical logical
dataset identity), `application/knowledge.py` (the composition seam that resolves the context and supplies the
admitted provenance) and `kernel/canonical_json.py` (the encoder the context digest and the logical digest are
computed through). The requirement it manifests is `KS-R03@v1`.

**No inventory entry and no fingerprint row are added in this pass, for the same reason the L1 deferral records.**
A `git-blob-set-v1` fingerprint resolves `HEAD:<path>` blobs and every file that would evidence this entity is
**uncommitted** in the leaf's code worktree, so a row written now would fail to resolve or would advance a
fingerprint onto a tree that does not exist yet — which this seat is forbidden to do. The refresh is owned by the
closeout/index transaction that commits the code, and it must add the matching `## Entity Inventory` entry in the
same pass because the quality check reconciles the fingerprint table against the inventory.

| Deferred entity | Evidence paths for the refresh |
| --- | --- |
| Knowledge candidate-change boundary | `mcp/src/agents_remember/models/knowledge/candidate.py`; `mcp/src/agents_remember/memory/knowledge/candidate.py`; `mcp/src/agents_remember/memory/knowledge/batch_preconditions.py`; `mcp/src/agents_remember/memory/knowledge/batch_commands.py`; `mcp/src/agents_remember/memory/knowledge/candidate_records.py`; `mcp/src/agents_remember/memory/knowledge/logical.py`; `mcp/src/agents_remember/application/knowledge.py`; `mcp/src/agents_remember/kernel/canonical_json.py` |

The subsystem's own account of current intent lives in the file cards under
`onboarding/mcp/src/agents_remember/{models,memory}/knowledge/` and in
[`memory/overview.md`](mcp/src/agents_remember/memory/overview.md) meanwhile, so a reader is not left without a
route while the fingerprint is pending.

### 260928-MIK-L93 R93 Impact — developer-question routing

The R93 change edits the canonical `l-01-agent-lifecycles` role, operation, core and template instructions and regenerates their copies, including the `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/…` copies. Two entities carry those copies in their curated evidence sets:

- **Source Lineage** — the evidence set includes the `package_data` `roles/manager.md` and `templates/curator-brief.md` copies; the manager copy's developer-question sentence changed in this leaf.
- **Seat Landing Archive** — the evidence set includes the `package_data` `roles/manager.md`, `roles/orchestrator.md` and `templates/manager-brief.md` copies; those copies' question and forward/notice sentences changed in this leaf.

Both stored fingerprints remain at the prior committed baseline. `git-blob-set-v1` resolves committed `HEAD:<path>` blobs, so the refreshed value cannot be computed from this deliberately uncommitted candidate and **no value was hand-edited here**; the governed closeout recomputes both rows against the actual code commit. The route contract itself is carried by the role, operation and CLI cards and by the rule-13 invariant.
