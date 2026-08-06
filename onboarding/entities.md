# Entities

| Field       | Value                  |
| ----------- | ---------------------- |
| repository  | agents-remember     |
| doc_type    | `repo-entity-catalog`  |
| lastUpdated | 2026-08-02T01:42+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00
| status      | active                 |

## Purpose

This catalog documents load-bearing real entities in `agents-remember`. It is not a glossary of every workflow term and it does not catalog task files. Task files remain planning artifacts; this file describes current reusable repository concepts and the boundaries between them.

## Entity Fingerprints

Each row records the deterministic source evidence used by `c-02-memory-quality-control` skill for entity drift detection. The `git-blob-set-v1` fingerprint sorts the evidence paths, resolves each current `HEAD:<path>` Git blob hash, and hashes the resulting `path + blob_hash` list. A changed fingerprint means the entity entry needs review; it does not automatically prove the prose is wrong. `c-02-memory-quality-control` skill also reconciles this table against `## Entity Inventory`, so missing rows and orphaned rows are actionable catalog maintenance.

| Entity                              | Algorithm         | Fingerprint                                                               | Evidence Paths                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ----------------------------------- | ----------------- | ------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Onboarding Unit                     | `git-blob-set-v1` | `sha256:ec102301fff3b4f96de37992c314cc9ffde407bf4474edc39ff103910b237088` | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/repo-entity-catalog-workflow.md`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py`                      |
| Runtime AGENTS Template Package     | `git-blob-set-v1` | `sha256:3774902dc704b86702adc6268948914db1c281428660f0ba36dc67a4eaa02333` | `mcp/src/agents_remember/package_data/runtime/agents-md-files/coordinator/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/skills/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/system/AGENTS.md`; `mcp/src/agents_remember/package_data/runtime/agents-md-files/tasks/AGENTS.md`; `mcp/src/agents_remember/install/runtime.py`                                                                                                                                                                                                                                    |
| Coordination Context                | `git-blob-set-v1` | `sha256:5f4e69d2974736bedbe021d9ceceb9e00fcf488556f4e8ece655ce8108208830` | `mcp/src/agents_remember/package_data/runtime/skills/c-08-ar-coordination-context-resolver/SKILL.md`; `mcp/src/agents_remember/kernel/coordination_context_resolver.py`                                                                                                                                                                                                                                                 |
| Path Rule                           | `git-blob-set-v1` | `sha256:786e99efd0140a464c034d5d01951bbddb5dce3d20c285a735cf606839fad9fe` | `mcp/src/agents_remember/kernel/coordination_context_resolver.py`; `mcp/src/agents_remember/package_data/runtime/system/defaults/examples/memory-repo/settings.json`; `examples/mcp/settings.example.json`                                                                                                                                                                                                       |
| Memory Quality Control              | `git-blob-set-v1` | `sha256:3bbe647611f3413b1a186b0082cd5553975e8d60ea60971073b6c521e09c0d90` | `mcp/src/agents_remember/package_data/runtime/skills/c-02-memory-quality-control/SKILL.md`; `mcp/src/agents_remember/memory_quality/check.py`; `mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py`; `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py`; `mcp/src/agents_remember/memory_quality/style/update_history/history_order.py`; `mcp/src/agents_remember/memory_quality/style/update_history/history_order_fix.py` |
| File-Level Onboarding Content Model | `git-blob-set-v1` | `sha256:cd698aab9465ecd7ddd2a7dfa2606ff49013e9cba93507bdb9d52e559d894259` | `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/file-level-onboarding-template.md`; `mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/templates/inline-onboarding-block-template.md` |
| Light Task Artifact                 | `git-blob-set-v1` | `sha256:2670e6700fad52cb381a310a5e97b85d5979debccc59e86aadaef96cd6908f74` | `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/SKILL.md`; `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/workflow.md`; `mcp/src/agents_remember/package_data/runtime/skills/w-02-light-task-workflow/template.md`                                                                                                                                                                                                                                                                                      |
| External Memory Ledger              | `git-blob-set-v1` | `sha256:c052aa14a1c366f3a19a0ed2ab386b473bdd90bcfe4daf6c5e75c53e1f535fb1` | `mcp/src/agents_remember/kernel/memory_ledger.py`; `mcp/src/agents_remember/worktrees/modules/closeout.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py`; `mcp/src/agents_remember/memory/baseline.py`                                                                                                                                                                                |
| Memory Baseline Adoption            | `git-blob-set-v1` | `sha256:46d11aad907580077564f5b85c7fa57a1fc472503737521433ac997c51df9af1` | `mcp/src/agents_remember/package_data/runtime/skills/c-10-adopt-memory-baseline/SKILL.md`; `mcp/src/agents_remember/memory/baseline.py`                                                                                                                                                                                                                                                                                  |
| Worktree Contract                   | `git-blob-set-v1` | `sha256:031324f50419668f94096337f93e79a185fecc1ba921f7ec03e777c3369d16a3` | `mcp/src/agents_remember/worktrees/worktree_contract.py`; `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md`; `mcp/src/agents_remember/worktrees/modules/guidance.py`; `mcp/src/agents_remember/worktrees/modules/closeout.py`; `mcp/src/agents_remember/worktrees/modules/integrate.py`                                                                                                                                                                                                     |
| Worktree Integration                | `git-blob-set-v1` | `sha256:a9278e69e3d6b9d1eb4fd39108d01f50cfdb6632abbcff18f06ea8c3e012d2fa` | `mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md`; `mcp/src/agents_remember/worktrees/modules/integrate.py`; `mcp/src/agents_remember/worktrees/modules/cleanup.py`                                                                                                                                                                                                                                                                                     |
| Branch-Gated Cross-Repo Source      | `git-blob-set-v1` | `sha256:5f4e69d2974736bedbe021d9ceceb9e00fcf488556f4e8ece655ce8108208830` | `mcp/src/agents_remember/package_data/runtime/skills/c-08-ar-coordination-context-resolver/SKILL.md`; `mcp/src/agents_remember/kernel/coordination_context_resolver.py`                                                                                                                                                                                                                                                 |
| Provider Degradation Protocol       | `git-blob-set-v1` | `sha256:04e82db07db55153dbf56c51ddce949aef0033e6b91606cffd9b4bfcb823ef3a` | `mcp/src/agents_remember/providers/degradation.py`; `mcp/src/agents_remember/mcp/provider_degradation_settings.py`; `mcp/src/agents_remember/controlplane/operator_inbox_records.py`; `mcp/src/agents_remember/controlplane/orchestration_artifacts.py`; `skills/l-01-agent-lifecycles/roles/system-specialist.md` |
| Seat Binding Identity               | `git-blob-set-v1` | `sha256:9330c661f5c3f6206ba53f309e138dafa667ade8a4250837b462bbbfb7065191` | `dashboard/src/data/sessions.ts`; `dashboard/src/panels/LeafAttachPicker.tsx`; `mcp/src/agents_remember/controlplane/signal_routing.py`; `mcp/src/agents_remember/serving/seat_binding.py`; `mcp/src/agents_remember/serving/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_leaf_assignment.py` |
| Seat Retirement                     | `git-blob-set-v1` | `sha256:defd6fe5d6e6332574b0b786a10b3d381fdab820a813a14f361cd33039c1f594` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/app.py`; `mcp/src/agents_remember/serving/retire.py`; `mcp/src/agents_remember/serving/retire_policy.py`; `mcp/src/agents_remember/serving/terminal_catalog.py` |
| Seat Landing Archive                | `git-blob-set-v1` | `sha256:772934264b1261753d479f68dbc872ed73f7edbf860eaab209b17cb639038268` | `dashboard/src/data/railModel.ts`; `dashboard/src/data/sessionLifecycle.ts`; `dashboard/src/panels/session-cockpit/SessionRail.tsx`; `mcp/src/agents_remember/application/worktree_tools.py`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md`; `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/manager-brief.md`; `mcp/src/agents_remember/serving/app.py`; `mcp/src/agents_remember/serving/landing.py`; `mcp/src/agents_remember/serving/terminal_catalog.py` |
| Supervisor Sweep                    | `git-blob-set-v1` | `sha256:92d93e5baa16fdef3f6f8aa4bbb77da46901cbe508e0d9433da1c6390cbb726d` | `mcp/src/agents_remember/kernel/agentic_settings.py`; `mcp/src/agents_remember/mcp/tools/base.py`; `mcp/src/agents_remember/serving/pane_signals.py`; `mcp/src/agents_remember/serving/supervisor.py`; `mcp/src/agents_remember/serving/supervisor_heartbeat.py`; `mcp/src/agents_remember/controlplane/escalation_ladder.py`; `mcp/src/agents_remember/controlplane/inbox_backoff.py`; `mcp/src/agents_remember/controlplane/operator_inbox_store.py`; `mcp/src/agents_remember/controlplane/orphan_policy.py`; `mcp/src/agents_remember/controlplane/signal_routing.py`; `mcp/src/agents_remember/controlplane/supervisor_signals.py` |
| Task Document                       | `git-blob-set-v1` | `sha256:8801daccd0038ffb34a40ea5e8c58762f0302fd0c4312dbb1aa1873ebb2ff7cf` | `dashboard/src/data/taskDocuments.ts`; `dashboard/src/panels/DetailPanel.tsx`; `mcp/src/agents_remember/observer/projection.py`; `mcp/src/agents_remember/observer/snapshots.py`; `mcp/src/agents_remember/serving/app.py` |
| Delivery Injector                   | `git-blob-set-v1` | `sha256:a0c2f9f58423795dbafda85dd8b092e919f4bf680721533249e0b844c1600a4f` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/harness_adapters.py`; `mcp/src/agents_remember/serving/harness_logs.py`; `mcp/src/agents_remember/serving/inbox_delivery.py`; `mcp/src/agents_remember/serving/injector.py`; `mcp/src/agents_remember/serving/terminal_catalog.py`; `mcp/src/agents_remember/serving/terminal_paste.py` |
| Harness Capability Snapshot         | `git-blob-set-v1` | `sha256:975b1c1ece72aa10886b47a4b39d7da10a4b95f817462688a6436887c5fd945d` | `mcp/src/agents_remember/mcp/tools/terminal.py`; `mcp/src/agents_remember/serving/claude_stream_protocol.py`; `mcp/src/agents_remember/serving/codex_app_server_adapter.py`; `mcp/src/agents_remember/serving/codex_app_server_session.py`; `mcp/src/agents_remember/serving/harness_capabilities.py`; `mcp/src/agents_remember/serving/harness_capability_catalog.py`; `mcp/src/agents_remember/serving/harness_control_adapter.py`; `mcp/src/agents_remember/serving/harness_control_api.py`; `mcp/src/agents_remember/serving/harness_control_bridge.py`; `mcp/src/agents_remember/serving/harness_control_claude.py`; `mcp/src/agents_remember/serving/harness_control_client.py`; `mcp/src/agents_remember/serving/harness_control_factories.py`; `mcp/src/agents_remember/serving/harness_control_models.py`; `mcp/src/agents_remember/serving/harness_control_runner.py`; `mcp/src/agents_remember/serving/harness_launch.py`; `mcp/src/agents_remember/serving/pi_rpc_adapter.py`; `mcp/src/agents_remember/serving/pi_rpc_configuration.py`; `mcp/src/agents_remember/serving/pi_rpc_events.py`; `mcp/src/agents_remember/serving/terminal_opener.py` |
| Harness Submission Authority        | `git-blob-set-v1` | `sha256:a27f17f6a161db8e5dd6ed738ad402f4ea64030243a4442ff3c35d0e61b5fcd8` | `dashboard/src/data/submissionLifecycleClient.ts`; `dashboard/src/data/submitClient.ts`; `dashboard/src/data/submitMachine.ts`; `mcp/src/agents_remember/serving/codex_app_server_adapter.py`; `mcp/src/agents_remember/serving/harness_control_adapter.py`; `mcp/src/agents_remember/serving/harness_control_api.py`; `mcp/src/agents_remember/serving/harness_control_bridge.py`; `mcp/src/agents_remember/serving/harness_control_claude.py`; `mcp/src/agents_remember/serving/harness_control_client.py`; `mcp/src/agents_remember/serving/harness_control_ipc.py`; `mcp/src/agents_remember/serving/harness_control_models.py`; `mcp/src/agents_remember/serving/harness_submission_authority.py`; `mcp/src/agents_remember/serving/harness_submission_ledger.py`; `mcp/src/agents_remember/serving/pi_rpc_adapter.py` |

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
| Description                  | The implemented helper parses and writes a fenced `json ar-memory-ledger` metadata block plus a newest-first two-column table that maps code commits to memory commits. Worktree closeout, integration, and baseline services use it when recording external-memory compatibility. Writing the file is plain I/O, but *publishing* a row is Git: `closeout.py` and `integrate.replay_memory_content` both `git add memory.md` and then commit through `worktrees/modules/git.py`'s `require_git` / `commit_if_dirty`, which since 260731-EFA-L3 call the one kernel runner `kernel/git_command.run_git` instead of a module-local copy that had dropped its environment guard. That runner strips the eight repository selectors in `GIT_REPOSITORY_SELECTOR_ENV` (`GIT_DIR`, `GIT_WORK_TREE`, `GIT_INDEX_FILE`, `GIT_OBJECT_DIRECTORY`, `GIT_ALTERNATE_OBJECT_DIRECTORIES`, `GIT_COMMON_DIR`, `GIT_NAMESPACE`, `GIT_PREFIX`) via `git_environment()`, so the compatibility record now lands in the contract's own memory repository even when the calling process exports `GIT_DIR` — previously it landed wherever `GIT_DIR` pointed. Since 260731-EFA-L5 (R12) the *durability* of that plain write is a decided property rather than an unexamined one: `write_ledger` stays an unguarded whole-file `write_text` — no lock, no temp-and-rename, no fsync — because all six call sites `git add memory.md` and commit within the next two statements, so the durable authority for a mapping is the git object and a truncated `memory.md` costs the uncommitted delta, recoverable with `git checkout -- memory.md`. The ruling therefore rests on a CALLER obligation, now recorded in the function's own docstring: write and commit in the same function. A caller that defers the commit, or one reached from a process running concurrently with another writer, converts "lose a delta" into "lose the mapping history" and moves this artifact onto the `ar-durable-store/1.0` contract with the six control-plane JSONL logs. |
| Canonical Source Of Truth    | `mcp/src/agents_remember/kernel/memory_ledger.py` plus service call sites in `mcp/src/agents_remember/worktrees/modules/closeout.py`, `mcp/src/agents_remember/worktrees/modules/integrate.py`, and `mcp/src/agents_remember/memory/baseline.py`.                                                                               |
| Current Naming Drift         | The parser/writer lives in the MCP package; CLI commands are now adapters around service functions. `LedgerError` now subclasses the shared `AgentsRememberError` (still a `ValueError`), so it is part of the package typed-error family rather than a bare `ValueError`.                               |
| Key Identifiers              | `schema`, `repoName`, `lastVerifiedCodeCommit`, `lastMemoryContentCommit`, table rows.                                                                                  |
| Parent / Child Relationships | Belongs to one external memory repo and is consumed by `c-09-git-worktree-manager` skill worktree lifecycle, baseline adoption, and cross-repo resolution.                                                                                  |
| Often Confused With          | Drift report or task contract.                                                                                                                                          |
| Source References            | [memory_ledger.py](agents-remember/mcp/src/agents_remember/kernel/memory_ledger.py); [baseline.py](agents-remember/mcp/src/agents_remember/memory/baseline.py); [closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py); [integrate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/integrate.py)                                                       |
| Migration Notes              | Git fixture coverage is still needed for full bootstrap and closeout integration beyond parser-level tests. **260731-EFA-L5 R12 (no code change, a recorded ruling):** the six `write_ledger` call sites were enumerated and each verified to commit immediately — `worktrees/modules/closeout.py` L539, `worktrees/modules/integrate.py` L254-L257, `worktrees/modules/start.py` L1128, `memory/carryover.py` L759-L762 and L849, `memory/baseline.py` L153. Note that two of those six modules, `start.py` and `carryover.py`, are NOT in this entity's evidence set, so the obligation the ruling depends on is load-bearing at call sites this fingerprint does not cover. Nothing under `observer/` or `serving/` writes the ledger; the dashboard imports `load_ledger` and never a writer, which is why no lock was added. Adding a seventh caller means re-checking both properties, not just the parser.                                                             |

### Memory Baseline Adoption

| Field                        | Value                                                                                                                                                                                                                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | External-memory migration operation                                                                                                                                                                                                                                           |
| Represents In Reality        | The explicit one-time conversion of existing external-memory onboarding into the first ledgered `memory.md` baseline.                                                                                                                                                         |
| Description                  | `c-10-adopt-memory-baseline` skill resolves the external-memory context, runs `c-02-memory-quality-control` skill drift, reports ledger status, blocks actionable drift unless the developer accepts it, and then creates the first memory content and ledger commits through the baseline service.                                                                |
| Canonical Source Of Truth    | `c-10-adopt-memory-baseline` skill and `mcp/src/agents_remember/memory/baseline.py`.                                                                                                                                                                                                            |
| Current Naming Drift         | This is not onboarding refresh. It is ledger adoption for onboarding the developer already considers factual enough to trust.                                                                                                                                                 |
| Key Identifiers              | `BaselineRequest`, `baseline_status`, `baseline_adopt`, `status`, `adopt`, `--accept-drift`, `ready`, `blocked-drift`, `already-ledgered`, `adopted`, `would-adopt`, `memory.md`.                                                                                                                                                     |
| Parent / Child Relationships | Consumes the `c-08-ar-coordination-context-resolver` skill coordination context and `c-02-memory-quality-control` skill drift rows; uses memory ledger helpers and Git worktree manager primitives to create the memory content and ledger commits.                                                                                                                                             |
| Often Confused With          | `c-05-create-or-update-onboarding-files` skill onboarding maintenance, `c-02-memory-quality-control` skill drift reports, `c-00-initialize-memory-repo` skill memory-root initialization, and `c-09-git-worktree-manager` skill task worktree lifecycle work.                                                                                                                                                      |
| Source References            | [`c-10-adopt-memory-baseline` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-10-adopt-memory-baseline/SKILL.md); [baseline.py](agents-remember/mcp/src/agents_remember/memory/baseline.py) |
| Migration Notes              | When drift is actionable but the developer says the current onboarding is factual, run adoption with `--accept-drift`; otherwise refresh affected onboarding through `c-05-create-or-update-onboarding-files` skill first.                                                                                              |

### Worktree Contract

| Field                        | Value                                                                                                                                                                                                                                                                                         |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Runtime coordination artifact                                                                                                                                                                                                                                                                 |
| Represents In Reality        | A local record of task identity, workflow artifact, worktree group, code worktree, memory worktree, ledger path, review state, mid-task sync log, closeout commits, integration commits, and cleanup state.                                                                                                      |
| Description                  | The helper locates contracts under `ar-coordination/tasks/<repo-name>/<task-name>-ar/contract.md` and keeps them out of memory repos and worktrees. The worktree manager facade exposes result-returning service functions implemented in focused modules so MCP application entry points can update and report contract state without shelling through a command facade. Since the issue #54 mid-task sync landing the contract also records `sync_log` — one entry per `worktree_sync` that advanced the recorded base pair — serialized as a single JSON scalar under a `sync:` front-matter section because the limited scalar parser regenerates the document from the dataclass and freeform prose does not survive. Since 260731-EFA-L4 the six persisted vocabulary cells are declared once, in `worktree_contract.py`, as `WorkflowKind`/`MemoryMode`/`HumanReviewStatus`/`CloseoutStatus`/`IntegrationStatus`/`CleanupStatus`, each runtime `VALID_*` frozenset derived from its own alias by `get_args`; `models/worktree.py` imports those aliases instead of retyping them. The read path is total: `_vocabulary_cell` reads a blank cell as the declared default, a member as itself, and anything else as the default plus a quarantine record on `WorktreeContract.unknown_cells` (`"<field>=<raw token> read as <fallback>"`), logged once per parse by `load_contract` and surfaced as `unknown_contract_cells` on the status payload and `unknownContractCells` on the context packet. `memory_mode` is the one cell whose fallback is read rather than fixed — `_memory_mode_fallback` answers `disabled` for `memory.state: disabled`, `external` when a memory worktree or ledger is recorded, and `internal` otherwise — because guessing `internal` for a contract that owns a memory worktree would make closeout skip work that exists. The write path is closed: `validate_contract(contract, *, path)` refuses every one of the six. That refusal reaches only writes. `load_contract` calls the same function, but the reader has already narrowed each cell, so a contract hand-edited on disk still loads: it degrades and quarantines rather than being rejected, and heals the next time any lifecycle tool rewrites the document. The asymmetry is deliberate — no lifecycle tool catches `ContractError`, so raising on read would leave a task that cannot be closed out, integrated, cleaned up or even abandoned. An approved closeout runs the strict repository quality wrapper before every code, memory, ledger, and contract commit, but it is no longer the predecessor of every mutation; see Parent / Child Relationships. Since 260731-EFA-L5 (R6) the persisted front matter carries a second version line, `schemaVersion`, written directly under `schema:` by `contract_to_text`. The two answer different questions and are deliberately not merged: `schema: ar-series-contract/v1` names the document vocabulary, while `schemaVersion` versions the durable-record contract the document is written under. Its constant and its accept/reject rule are REUSED, not redeclared — `CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION` and `_require_supported_schema_version` calls `schema_version_supported`, both imported from `controlplane/durable_store.py`, so the tree holds one version policy rather than two that can drift. The rule has exactly three cases: an absent line means 1.0 and is accepted, an unknown MINOR is accepted as additive, and an unknown MAJOR raises `ContractError` naming the file. This is a DOCUMENT-level refusal, joining absent front matter and an unrecognized `schema`; it is not a seventh vocabulary cell and does not weaken the total reader, which stays total for all six cells. It can only ever fire on a document some other build wrote — measured for this pass, 214 `series-contract.md` files exist under this workspace's coordination tasks root and zero carry a `schemaVersion` line, which is why the absent case had to be the accepted one and why no migration was needed or written. |
| Canonical Source Of Truth    | `mcp/src/agents_remember/worktrees/worktree_contract.py` plus `c-09-git-worktree-manager` skill.                                                                                                                                                                                                                                     |
| Current Naming Drift         | The parser/writer and service functions live in the MCP package; the contract is not the same entity as a `w-02-light-task-workflow` skill task file. The worktree service functions now take a typed `WorktreeArgs` DTO instead of a loose `argparse.Namespace`, and `ContractError` now subclasses the shared `AgentsRememberError` (still a `ValueError`). Since L4 the six vocabulary cells are moved through `ContractCells` + `amend_contract`, never `dataclasses.replace`: typeshed declares `replace(obj, /, **changes: Any)`, so `replace(contract, cleanup="reclaimed-ish")` produced no pyright diagnostic at all, at any of the six fields. `WorkflowKind` is exactly `chat-task`/`light-task` — the bare `chat`/`light` the wire model used to carry had no writer and, by this leaf's own scan, zero occurrences across the 213 contracts on disk — and `CleanupStatus` now holds `reopened`, which `worktrees/reopen.py` has always written. |
| Key Identifiers              | `contract.md`, task id/name, worktree group, code worktree, memory worktree, ledger path, human review state, `sync_log`, closeout commits, integration commits, cleanup state, `unknown_cells`/`unknownContractCells`, `ContractCells`, `amend_contract`, `validate_contract(..., path=...)`, `schemaVersion`/`CONTRACT_SCHEMA_VERSION`, `_require_supported_schema_version`.                                                                                                                           |
| Parent / Child Relationships | Owned by local coordinator and consumed by `c-08-ar-coordination-context-resolver` and `c-09-git-worktree-manager` skill worktree-aware flows plus MCP worktree tools. Closeout preview/approval remains non-mutating; the strict repository wrapper is the apply-side predecessor of every code, memory, ledger, contract, and applied-gate **commit**. Since L4 it is not the predecessor of every *mutation*: where the gate runs, `closeout._gate_staged_code` first refuses a code checkout that is not a linked worktree (git reports `--git-dir` equal to `--git-common-dir`, which is what a repository's own checkout looks like and what `default_series_contract` records as `code_worktree` for a `kind: series` contract), then refuses a checkout with unmerged index entries, and only then runs `git reset --mixed HEAD` + `git add -A` and the wrapper over exactly that staged content. That index write precedes the gate and is not undone when the gate refuses — nothing is committed, and the next attempt resets and restages from the working tree. The order is load-bearing: `git reset` drops the unmerged entries and `MERGE_HEAD`, so running it ahead of the conflict refusal would disable that refusal silently and let `add -A` stage the conflict markers into the commit. A checkout carrying no wrapper runs no gate, stages nothing early, and previews as `wrapper-unavailable`. |
| Often Confused With          | Task artifact, onboarding unit, or memory ledger.                                                                                                                                                                                                                                             |
| Source References            | [worktree_contract.py](agents-remember/mcp/src/agents_remember/worktrees/worktree_contract.py); [guidance.py](agents-remember/mcp/src/agents_remember/worktrees/modules/guidance.py); [closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py); [integrate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/integrate.py) |
| Migration Notes              | Task files should remain planning artifacts; contracts should record operational state. Closeout commits and integration commits are separate because replay can change landed SHAs.                                                                                                          |

### Worktree Integration

| Field                        | Value                                                                                                                                                                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Worktree lifecycle phase                                                                                                                                                                                                                                                           |
| Represents In Reality        | The approved landing of closed task work from code and memory worktrees back onto their source branches.                                                                                                                                                                           |
| Description                  | `c-09-git-worktree-manager` skill `integrate` requires completed closeout and clean checkouts, supports `ff-only` for unchanged source ancestry, supports `replay` for parallel non-overlapping source movement, and regenerates the memory ledger row for landed commits. The final merge is atomic: it pre-validates that both the code and memory ledger fast-forwards are possible before mutating either branch, and if the memory side fails after the code branch advanced it rolls both branches back to their pre-merge heads, so integration is all-or-nothing rather than leaving a half-integrated state. `integrate_result()` lives in the integration module, takes a typed `WorktreeArgs`, and returns the same lifecycle result shape for MCP application entry points while the CLI remains an adapter. Mid-task `worktree_sync` (2.8.0) advances the contract's recorded base pair while parallel cycles land, which is what keeps end-of-series integration `ff-only` instead of forcing replay. Cleanup (`cleanup_result`) runs after successful integration and is now carryover-guarded (slice 05m): it hard-refuses while integration is completed but the parked memory has not been carried into official memory — the proof is the official ledger via `guidance.carryover_done`, not a contract stamp, since cleanup deletes the parked memory branch the carry reads from. Once carryover has run, cleanup retires both the worktree branch and the (PR'd) source branch — locally for code and memory, plus the remote for the code source branch — instead of only deleting Git-proven-merged branches. Since 260731-EFA-L3 every Git mutation in this phase — the code `rebase`, the memory `checkout -b` + `rebase --onto` replay, both `merge --ff-only` landings and the two rollback `reset --hard` calls in `_merge_integrated_commits` — runs through the one kernel runner `kernel/git_command.run_git`, which strips the `GIT_REPOSITORY_SELECTOR_ENV` selectors and bounds local work at `GIT_LOCAL_TIMEOUT_SECONDS = 300`; the worktree-local copy it replaced had neither guard nor timeout, so the all-or-nothing guarantee above is now a guarantee about the contract's own repositories rather than about whatever an exported `GIT_DIR` named. Cleanup's two remote-talking commands (`ls-remote --heads origin <branch>` and `push origin --delete <branch>`) go through `cleanup._remote_git` at `GIT_REMOTE_TIMEOUT_SECONDS = 120`, and a stall is now reported as the already-defined `{"remote_deleted": false, "reason": "remote-unreachable"}` outcome instead of holding the uncancellable MCP tool call open indefinitely. Since 260731-EFA-L4 every contract write in this phase moves its status cells through `ContractCells`/`amend_contract` (`blocked_integration_payload`, `_integrated_result`, `cleanup_result`, `abandon_result`), and the phase vocabulary this module drives is declared in `worktrees/modules/guidance.py` — `WorktreePhase`, `NextOperation`, `NextTool` — rather than hand-copied into `models/worktree.py`. Reconciling the two copies added four values this phase machine was already emitting and the context packet was rejecting: the `carryover-pending` and `abandoned` phases, the `request_carryover_decision` operation, and the `memory_carryover_apply` tool. `commit-approval-pending` and `request_commit_approval` left the packet's vocabulary in the same move: they are not phases of this machine but the closeout preview's own gate, and they now ride the separate `recovery_guidance` builder (`RecoveryOperation`/`RecoveryTool`), which emits the same keys in the same order onto a `FlexibleToolResponse` without widening `WorktreeSummary.nextOperation`. |
| Canonical Source Of Truth    | `c-09-git-worktree-manager` skill docs and `mcp/src/agents_remember/worktrees/modules/integrate.py`.                                                                                                                                                                                                                                     |
| Current Naming Drift         | Integration is not cleanup. Cleanup is asked after successful integration and remains pending until explicitly approved.                                                                                                                                                           |
| Key Identifiers              | `integrate_result`, `cleanup_result`, `integrate`, `--strategy ff-only`, `--strategy replay`, `integration.status`, `integrated_code_commit`, `integrated_memory_content_commit`, `integrated_ledger_commit`, `cleanup`.                                                                                                 |
| Parent / Child Relationships | Consumes the worktree contract closeout commits and writes integration result fields back to the same contract.                                                                                                                                                                    |
| Often Confused With          | Closeout commits, manual merge, push, or worktree deletion.                                                                                                                                                                                                                        |
| Source References            | [`c-09-git-worktree-manager` SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-09-git-worktree-manager/SKILL.md); [integrate.py](agents-remember/mcp/src/agents_remember/worktrees/modules/integrate.py); [cleanup.py](agents-remember/mcp/src/agents_remember/worktrees/modules/cleanup.py)                  |
| Migration Notes              | Replay integration preserves parallel work support by producing new landed SHAs instead of pretending the closeout SHAs are still the source branch tips.                                                                                                                          |

### Branch-Gated Cross-Repo Source

| Field                        | Value                                                                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Cross-repo trust contract                                                                                                                                                          |
| Represents In Reality        | A configured external repository context source that is included only when branch and memory-ledger checks pass.                                                                   |
| Description                  | The resolver parses `crossRepo.allow` as strict v2 objects with `repo`, `expectedBranch`, `includeCode`, and `includeMemory`; legacy strings are excluded with a migration reason. Parsed entries are resolved through the focused cross-repo module, which validates adjacent repo branches and optionally memory ledger state. |
| Canonical Source Of Truth    | `c-08-ar-coordination-context-resolver` skill settings parsing, focused cross-repo resolution, and the cross-repo mode design spec.                                                                                         |
| Current Naming Drift         | Legacy string allow entries are not branch-safe and should be treated as invalid in v2.                                                                                            |
| Key Identifiers              | `repo`, `expectedBranch`, `includeCode`, `includeMemory`, result state.                                                                                                            |
| Parent / Child Relationships | Uses committed memory settings, resolver context, worktree context, and memory ledger metadata.                                                                                    |
| Often Confused With          | Local coordinator path hints or implicit repository browsing.                                                                                                                      |
| Source References            | [setting_values.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/setting_values.py); [cross_repo.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/cross_repo.py). The former roadmap design-spec link was removed after reference health checking proved the target no longer exists. |
| Migration Notes              | Cross-repo inclusion must remain read-only toward external repos.                                                                                                                  |

### Provider Degradation Protocol

The durable inbox record used by this entity now has a narrowly bounded rolling-reader seam:
legacy projections may preserve optional `adapterDeliveryState` and `adapterDeliveryDetail`, while
unrelated extensions remain rejected. This does not change provider degradation state transitions
or consume semantics.

| Field                        | Value                                                                                                                                                                                                                                                                                          |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Category                     | Runtime detection/response protocol                                                                                                                                                                                                                                                            |
| Represents In Reality        | The provider-only degradation detector (a healthy/degraded/critical state machine over the central provider metrics log), its response protocol (durable events, role-addressed inbox alerts, critical-threshold failsafe stop), and the `system-specialist` role that investigates before any fix. |
| Description                  | 260707-HFX-L7 (developer plan-gate ruling 2026-07-07) lands the detector/state-machine in `providers/degradation.py`, the `providerDegradation` settings surface in `mcp/provider_degradation_settings.py`, the `system-specialist` `AgentRole`/`OrchestrationRole` literal plus the `degradation-alert` `InboxMessageKind`, and the doctrine additions to `roles/manager.md` (stop starting providers, no kill authority) and `roles/orchestrator.md` (dispatch system-specialist, read report, fix-or-stop). The serving metrics sampling loop (`serving/app.py`) calls the detector once per tick. Providers-only this iteration; Sentry (260703_spotlight-dev-observability) is the designated future detection source that can replace/feed this same response protocol without redoing it. |
| Canonical Source Of Truth    | `providers/degradation.py`, `mcp/provider_degradation_settings.py`, the `AgentRole`/`InboxMessageKind` literals in `controlplane/operator_inbox_records.py`, the `OrchestrationRole`/`_ROLE_ESCALATION` literals in `controlplane/orchestration_artifacts.py`, and `skills/l-01-agent-lifecycles/roles/system-specialist.md`. |
| Current Naming Drift         | None recorded; this is a newly landed entity as of HFX-L7.                                                                                                                                                                                                                                     |
| Key Identifiers              | `healthy`/`degraded`/`critical` state, `ar-provider-degradation-state/v1`, `ar-provider-degradation-event/v1`, `degradation-alert` message kind, `system-specialist` role, `providerDegradation` settings key, `failSafeEnabled`.                                                            |
| Parent / Child Relationships | Reads `providers/metrics.py`'s central metrics log; posts through `controlplane/operator_inbox_store.py` and `serving/inbox_delivery.py`; stops stacks through `application/provider_tools.py`'s always-legal teardown path; consumed once per tick by `serving/app.py`.                       |
| Often Confused With          | The lower-level per-container containment metrics sampler (260707-HFX-L1, `providers/metrics.py`) — that module only samples and stores; this entity is the decision/response layer built on top of it. Also not the future Sentry integration, which is a detection-source replacement, not this entity's response protocol. |
| Source References            | [degradation.py](agents-remember/mcp/src/agents_remember/providers/degradation.py); [provider_degradation_settings.py](agents-remember/mcp/src/agents_remember/mcp/provider_degradation_settings.py); [operator_inbox_records.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_records.py); [orchestration_artifacts.py](agents-remember/mcp/src/agents_remember/controlplane/orchestration_artifacts.py); [system-specialist.md](agents-remember/skills/l-01-agent-lifecycles/roles/system-specialist.md) |
| Migration Notes              | When Sentry-based detection lands (260703_spotlight-dev-observability), it should feed this same event/alert/failsafe response protocol rather than duplicate it; the setup-failure-streak and probe-latency evidence paths in `classify_degradation` are the designated seams (currently producer-less/disclosed). 260707-HFX2-L1 added `attemptCount`/`lastAttemptAt`/`nextAttemptAt`/`escalatedAt`/`ownerRole`/`ownerAgentId`/`ownerLifecycleId` fields to `OperatorInboxEntry` in this entity's shared `operator_inbox_records.py` evidence file — purely additive record fields for the unrelated R1 ack-semantics/R4 hierarchical-routing feature, touching neither the `AgentRole`/`InboxMessageKind` Literals this entity's `system-specialist`/`degradation-alert` values live on nor the degradation detector/response protocol itself; no entity prose change warranted. **260731-EFA-L5 is the same shape and gets the same answer: re-signed, not moved.** The one changed evidence file is again `controlplane/operator_inbox_records.py`, where `OperatorInboxCompatibleRecord` (the base of `OperatorInboxEntry`, so of every `degradation-alert` row this entity posts) now derives from the durable-store contract's `DurableRecord` and therefore carries a persisted `schemaVersion` field and its unknown-major refusal. Two facts worth stating so nobody re-derives them: this store deliberately KEEPS `extra=allow` plus its named forward-compatibility allowlist rather than taking the contract's default `extra=forbid`, and it is the contract's one declared `extra` exception; and the new refusal is a validation refusal on a row written by a future MAJOR, which no build in this tree writes. The detector, the healthy/degraded/critical state machine, the thresholds, the failsafe, the `AgentRole`/`InboxMessageKind` literals and the response protocol are all untouched. |

### Seat Binding Identity

| Field                        | Value |
| ---------------------------- | ----- |
| Category                     | Terminal-catalog identity protocol |
| Represents In Reality        | The durable current assignment of one hosted session to a canonical task leaf and one seat role, distinct from how that session was originally launched. |
| Description                  | 260707-HFX2-L17 makes `(leafKey, seatRole)` the server-authoritative binding key. `spawnRole` remains immutable origin provenance; `seatRole` can be established by spawn or explicit attach and changes atomically with `leafKey`. Worker, reviewer, curator, manager/architect anchors, generic chat, and terminal roles can coexist on one leaf, while one live same-role owner still excludes a duplicate. Legacy rows migrate from `spawnRole`, otherwise `chat`; terminals remain `terminal`. Spawn and attach liveness-check the current same-pair owner so a dead holder is marked exited and routine replacement proceeds. In the dashboard, a new session's binding fields are materialized only from the validated accepted server row; request fields and failed opens cannot create a provisional binding. |
| Canonical Source Of Truth    | `serving/seat_binding.py` for normalization, `serving/terminal_catalog.py` for persistence/migration/current binding properties, and `serving/terminal_leaf_assignment.py` for explicit attach plus live pair arbitration. |
| Current Naming Drift         | `role` on compatibility payloads still means transport (`chat`/`terminal`); `spawnRole` means launch provenance; `seatRole` is current orchestration identity. Older “leaf role” prose often meant transport role and must not be read as the new seat role. |
| Key Identifiers              | `leafKey`, `seatRole`, `spawnRole`, `binding_role`, `binding_leaf_key`, `migrated_seat_role`, `attach_seat_role`, `with_leaf_binding`, `active_for_leaf(..., seat_role=...)`, `role-required`, `leaf-taken`. |
| Parent / Child Relationships | Spawn derives and persists the first binding; attach can claim/rebind a hand-opened or existing session; retire, supervisor, expectations, inbox, provider discovery, landing, and dashboard grouping/rendering consume current binding identity. The dashboard session registry accepts the server-returned `leafKey`/`seatRole` only after authoritative-open validation and creates no binding row on failure. Spawned-by fields remain the historical parent edge. |
| Often Confused With          | Session transport kind, immutable spawn provenance, mutable display label, lifecycle attachment, or retirement/landing status. None determines the current leaf-seat pair. |
| Source References            | [seat_binding.py](agents-remember/mcp/src/agents_remember/serving/seat_binding.py); [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py); [terminal_leaf_assignment.py](agents-remember/mcp/src/agents_remember/serving/terminal_leaf_assignment.py); [signal_routing.py](agents-remember/mcp/src/agents_remember/controlplane/signal_routing.py); [sessions.ts](agents-remember/dashboard/src/data/sessions.ts); [LeafAttachPicker.tsx](agents-remember/dashboard/src/panels/LeafAttachPicker.tsx) |
| Migration Notes              | Reviewer O1: the self-limiting legacy rewrite currently occurs on the lock-free read path, so first-upgrade read could theoretically lose a concurrent mutation; unique-temp atomic replace still prevents corruption. O2: attach-with-role is deliberately self-service authority in the local single-operator trust model. O3: reopening an existing id preserves persisted binding ahead of a new role env; normal spawn uses fresh ids and attach is the rebind surface. All three are non-blocking observations, not alternate semantics. Candidate fingerprint uses working-tree blobs and must be recomputed against the eventual L17 commit. |

### Seat Retirement

| Field                        | Value                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Category                     | Terminal-catalog lifecycle protocol                                                                                                                                                                                                                                                                                                              |
| Represents In Reality        | The server-authoritative explicit lifecycle by which a dashboard-owned chat seat is terminated and marked with retirement provenance, plus the authority policy that decides who may retire whom. |
| Description                  | 260707-HFX-L8 (issues #12/#4) introduces seat retirement as a genuine cross-layer entity, not just a new catalog field: a retire is a terminal mark (`status == "terminated"` plus `retired_at`/`retired_by_session`/`retired_reason`/`retired_edge` provenance) layered onto the existing catalog terminal state, so it composes with the pre-existing L5 liveness hysteresis (a retired row can never be resurrected). Authority is enforced server-side via `retire_policy.check_retire_authority`: owner-never-self-retires checked first unconditionally; a manager may retire worker/reviewer/curator seats whose binding leaf belongs to its own master; only the orchestrator has portfolio-wide authority. HFX2-L17 builds `SeatRef` from current binding role and `binding_leaf_key`, so an explicitly typed hand-opened seat and an unbound failed dispatch with `replacementForLeaf` resolve correctly. Retirement is reached through the manual `session_retire` MCP tool, `POST /api/terminal/{session}/retire`, destructive `/terminate`, or the landed-archive cleanup endpoint after an explicit group-cleanup action. Normal successful completion marks seats `landed` under the separate `Seat Landing Archive` entity. 260731-EFA-L4 gives the tool surface one payload builder: `mcp/tools/terminal._retire_payload` replaces four hand-written dicts, is typed on the wire alias `SessionRetireStatus`, and derives `ok` once from `_RETIRE_OK_STATUSES = {"retired", "already-retired"}` — so a refusal status added later cannot arrive as `ok=True` from a fifth call site that forgot the rule. A closure row contributes the four provenance fields and a refusal contributes `detail`; nothing carries both. |
| Canonical Source Of Truth    | `mcp/src/agents_remember/serving/retire_policy.py`, `mcp/src/agents_remember/serving/retire.py`, the retirement fields/copiers on `TerminalCatalogEntry` in `mcp/src/agents_remember/serving/terminal_catalog.py`, and the `session_retire`/dashboard retire routes that call the policy before mutation. |
| Current Naming Drift         | HFX2-L11 splits completion-edge landing from explicit retirement. Old prose that says a successful integration/finalize "auto-retires" spent seats is stale; current successful completion marks rows `landed`, while retire means terminal cleanup with retirement provenance. |
| Key Identifiers              | `retired_at`, `retired_by_session`, `retired_reason`, `retired_edge`, `SeatRef`, `binding_leaf_key`, `binding_role`, `replacementForLeaf`, `RetirePolicyError`, `session_retire`, `api_terminal_retire`, `landed-group-cleanup`. |
| Parent / Child Relationships | A specialization of the pre-existing `TerminalCatalogEntry` terminal state (composes with, does not replace, the L5 liveness-hysteresis terminal invariant); consumed by the `session_retire` MCP tool, `POST /retire`, `/terminate`, and the landed archive cleanup endpoint. Since 260715-FEUI-L2 the sessions cockpit ALSO consumes it live: the `seat.retired` observer event pre-applies the terminal mark + provenance (`dashboard/src/data/seatEvents.ts`, poll-authoritative, never resurrecting), and retirement provenance renders on rail tooltips and the seat inspector. Since 260715-FEUI-L6 the cockpit additionally renders retirement RESIDUALS: `controlRaw.retireControlStopError` is swept focus-independently across every registry row (`dashboard/src/data/sessionLifecycle.ts` `startRetireResidualSweep`, dedup-once per sessionId) into dismissable INFORMATIONAL `role="status"` stage notes + the retired-row inspector — never silently discarded, never styled as failure. The cockpit itself never calls the retire route: the authority policy requires a real catalog actor SEAT, which the dashboard does not have, so the operator action from the cockpit is terminate (honest confirm naming session · leaf · state) and retirement stays agent-side, rendered not issued. |
| Often Confused With          | A landed archive row (`status:"landed"`, inspectable, not terminated); the L5 liveness "exited" state (probe-observed, self-healing, non-terminal); a rename (identity-only, does not touch `status`). |
| Source References            | [terminal.py](agents-remember/mcp/src/agents_remember/mcp/tools/terminal.py); [app.py](agents-remember/mcp/src/agents_remember/serving/app.py); [retire_policy.py](agents-remember/mcp/src/agents_remember/serving/retire_policy.py); [retire.py](agents-remember/mcp/src/agents_remember/serving/retire.py); [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py); [seatEvents.ts](agents-remember/dashboard/src/data/seatEvents.ts) |
| Migration Notes              | Do not reintroduce completion-edge auto-retirement as a silent cleanup courtesy. Normal success must remain inspectable through the landed archive; retirement is explicit cleanup or authority-checked manual action. |

### Seat Landing Archive

| Field                        | Value |
| ---------------------------- | ----- |
| Category                     | Terminal-catalog lifecycle protocol |
| Represents In Reality        | The non-destructive successful-completion state for worker/reviewer/manager chat seats, plus the dashboard archive group and explicit cleanup action that owns later reclamation. |
| Description                  | 260707-HFX2-L11 reverses HFX-L8's success-edge auto-retire model. `worktree_integrate` and `lifecycle_finalize_task` now call `_auto_land_completed_seats`, which resolves the qualified leaf key and calls `serving.landing.land_seats_for_leaf` for the edge's role set. HFX2-L17 matches that set against current binding role rather than spawn provenance. Matching rows become `status:"landed"` with `landed_at`/`landed_reason`/`landed_edge` provenance and are returned as `autoLandedSeats`; tmux sessions are not killed. Pair-scoped `TerminalCatalog.active_for_leaf` stays running-only, so landed rows release only their seat-role slot while remaining visible. The liveness sweeper returns landed rows but skips background probing/classification/writes; attach can inspect liveness on demand. The dashboard groups only landed rows into the collapsed archive and explicit cleanup rechecks before retirement. |
| Canonical Source Of Truth    | `mcp/src/agents_remember/serving/landing.py`, `mcp/src/agents_remember/application/worktree_tools.py`, `mcp/src/agents_remember/serving/terminal_catalog.py`, `mcp/src/agents_remember/serving/app.py`, dashboard `railModel.ts`/`SessionRail.tsx`/`sessionLifecycle.ts`/`LandedCleanupNotice.tsx`, and the manager/orchestrator package-data doctrine. |
| Current Naming Drift         | The setting family remains named `retirement` for compatibility, but the current keys are `autoLandOnIntegration`/`autoLandOnFinalize`; legacy `autoRetireOnIntegration`/`autoRetireOnFinalize` are parser aliases only. |
| Key Identifiers              | `status:"landed"`, `landed_at`, `landed_reason`, `landed_edge`, `land_seats_for_leaf`, `_auto_land_completed_seats`, `autoLandedSeats`, `autoLandOnIntegration`, `autoLandOnFinalize`, `landed archive`, `landed-group-cleanup`. |
| Parent / Child Relationships | Extends the terminal catalog lifecycle beside `running`/`exited`/`terminated`; completion-edge application entry points produce it, serving liveness treats it as sweep-cold, dashboard grouping consumes it, and explicit cleanup converts it to retirement. Since 260715-FEUI-L2 the sessions cockpit rail is a second dashboard consumer: landed rows fold into per-master collapsed completed folders with master- and sprint-level bulk end over the same `landed-cleanup` endpoint (honest naming previews, backend-rechecked), and the `seat.landed` observer event pre-applies landing provenance. Since 260715-FEUI-L6 the rail also renders the cleanup route's OWN outcome instead of dropping it: `dashboard/src/data/sessionLifecycle.ts` `endLandedDetailed` keeps the response's closed + skipped-with-reasons counts and `SessionRail.tsx` shows them after a bulk end. |
| Often Confused With          | Seat Retirement (terminates tmux with retirement provenance); the historical HFX-L8 auto-retire behavior; legacy exited/absent rows in the chat list, which are not grouped by the new landed archive. |
| Source References            | [worktree_tools.py](agents-remember/mcp/src/agents_remember/application/worktree_tools.py); [landing.py](agents-remember/mcp/src/agents_remember/serving/landing.py); [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py); [app.py](agents-remember/mcp/src/agents_remember/serving/app.py); [railModel.ts](agents-remember/dashboard/src/data/railModel.ts); [sessionLifecycle.ts](agents-remember/dashboard/src/data/sessionLifecycle.ts); [SessionRail.tsx](agents-remember/dashboard/src/panels/session-cockpit/SessionRail.tsx); [LandedCleanupNotice.tsx](agents-remember/dashboard/src/panels/session-cockpit/LandedCleanupNotice.tsx); [manager.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md); [orchestrator.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/orchestrator.md); [manager-brief.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/manager-brief.md) |
| Migration Notes              | Known limitation from the HFX2-L11 review: because landed rows are sweep-cold, a landed row whose tmux session later dies stays displayed until explicit cleanup; attach performs the live check and fails rather than the background sweep reclaiming it. |

### Supervisor Sweep

| Field                        | Value                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Category                     | Runtime detection/response protocol                                                                                                                                                                                                                                                                                                              |
| Represents In Reality        | The deterministic, zero-model reconciliation loop hosted in the serving daemon that sweeps authoritative control-plane stores on its own cadence, evaluates mechanical predicates over what it finds, and acts (redeliver, auto-nudge, signal-emit, escalate) — "the model is never the polling layer" (P-15 tiers 1+2) — plus its own self-liveness heartbeat. |
| Description                  | 260707-HFX2-L2 lands `serving/supervisor.py` (`SupervisorContext`, five R2 predicate families — pane-state, expectation-deadline expiry, turn-report staleness, unacked-row redelivery, seat-liveness — and the R4 action dispatcher, each action logging an `orchestration.supervisor.*` observer event), `serving/pane_signals.py` (the R2a pane-state classifier, distinct from `turn_state.py`'s UI-state classifier over the same captured text), and `serving/supervisor_heartbeat.py` (the R5 self-liveness tick store, issue #15 "the watcher must be code AND watched"). The sweep is hosted as a third decoupled-cadence lifespan task in `serving/app.py` beside the projector and metrics loops, configured by the new `orchestration.supervisor` settings family in `kernel/agentic_settings.py`, and surfaced two ways: a fail-loud MCP-tool banner (`mcp/tools/base.py::_tool_payload`, reading `AmbientLifecycle.root`) and a dashboard header badge (`/api/state`/SSE `supervisorHeartbeat`, `cockpit/Cockpit.tsx`'s `SupervisorHeartbeatBadge`). Level-triggered by design: any event lost anywhere (a dropped push, a crashed dispatch call) is caught by the next sweep — the backstop even protocol-grade push (A2A/MCP) needs. **260707-HFX2-L4 fills the P-15 tier-3 stub in**, wired DIRECTLY into this same module rather than as a separate entity: two more predicates (`evaluate_escalation_findings`/`evaluate_dead_upstream_findings`) and two more actions (`_escalate_rung`/`_signal_dead_upstream`) call through NEW pure modules `controlplane/escalation_ladder.py` (the rung walker — renudge/skip-level/developer-attention) and `controlplane/orphan_policy.py` (dead-manager orphan-worker detection), plus a NEW two-hop `signal_routing.derive_skip_level_owner`/`is_seat_dead` pair kept deliberately SEPARATE from the existing one-hop `derive_signal_owner`. Past the respawn threshold, `_escalate_rung` retires the suspect seat (HFX-L8's `retire_entry`), re-delivers its pending queue to the successor, and surfaces (never auto-reparents) a retired manager's orphaned workers. **260707-HFX2-L9 adds the cadence safety layer:** `controlplane/inbox_backoff.py` owns the 900-second retry floor and fail-loud sub-floor validation, `operator_inbox_store.py` persists floor-aware `nextAttemptAt` scheduling, and `controlplane/supervisor_signals.py` persists pane/seat-liveness signal cooldown records so short sweeps do not mint per-sweep owner inbox rows. **260707-HFX2-L13 round 2 repairs the live hierarchy/wake seam:** leaf signals resolve the current manager first, supervisor predicates suppress stale work when the leaf chain progressed, later rungs have a redundant five-minute floor, duplicated findings cannot advance one row twice in one sweep, and completion reports are readdressed and hosted-delivered to the current manager. **260731-EFA-L4 repairs both surfacing seams, which were writing keys nothing declared.** `supervisorBanner` is now a field of `models.base.ResponseModel` and `FlexibleResponseEnvelope`, set by `_tool_payload` on the validated response *before* the single `model_dump`; it used to be stamped onto the already-dumped dict, and because `StrictResponseModel` is `extra="forbid"` that made every tool response fail its own `model_validate` whenever the supervisor was stale — and put the banner's bytes, along with the whole `nextStep` object, outside the `tokens` the response advertised. `emit_tool` now observes the finished payload, so the tokens recorded against the lifecycle are the tokens served. `TOOL_RESPONSE_MODELS` is typed `dict[str, type[ResponseEnvelope]]` rather than `type[BaseModel]`, which is what makes those two fields reachable by type at the choke point. On the dashboard side `serving/supervisor_heartbeat.SupervisorHeartbeatPayload` declares the tick age as the wire carries it — deliberately serialized *without* `exclude_none`, so a supervisor that has never ticked reports explicit nulls and the cockpit can still tell "never ticked" from "this server reports no heartbeat at all" — and `serving/served_state.ServedWorkspaceProjection` declares it (with `servingBuild`) as the serve-time tail that `/api/state` and the SSE `snapshot` frame merge onto the memoized projection dump. Both keys were previously injected with nothing declaring them, so a served body could not be fed back through `WorkspaceProjection`. **260731-EFA-L5 puts this sweep's durable stores on one declared storage contract and names this sweep the compaction owner of most of them.** Both changed evidence files are about that. `controlplane/supervisor_signals.py`: the cooldown log now takes an unconditional per-log lock across its read AND its rewrite (`compact` delegates to a `_compact_locked` half inside `exclusive_access`), and the dashboard — this sweep — is its declared single writer and compaction owner. It was previously unlocked on single-writer grounds, and the leaf's proof run measured 31.45% loss on its structural twin, attention-dismissals, whose single-writer claim was equally true: one process writing a file is a deployment fact, not a structural one. `controlplane/operator_inbox_store.py`: this is the leaf's ONE DECLARED EXCEPTION to single-owner compaction, because both long-lived processes must physically REMOVE rows and neither removal can move without moving the decision it implements — the MCP deletes a cancelled gate's inbox rows (`delete_by_gate`) at the moment it cancels the gate, while this sweep must resolve and compact under one continuously held lock (`reconcile_and_compact`) so that a consume which won the lock stays terminal. Its pre-existing flock was kept and re-expressed through the shared `exclusive_access`, which adds a once-per-lockfile probe that refuses a filesystem where flock does not actually exclude (NFS, SMB, WSL DrvFs). Across the wider contract, four of the six logs name the DASHBOARD PROCESS as compaction owner, and this sweep is the reclaim pass for three of those four: it calls `expectation_store.compact` and `signal_cooldown_store.compact` once per sweep (`serving/supervisor.py` L1235, L1242) and `inbox_store.reconcile_and_compact` (L1208) on the ownerless inbox. The other two are not this sweep's: attention-dismissals is reclaimed by the projection pass (`observer/projection_store.py` L268), and orchestration-nudges has no production reclaim pass at all yet — the dashboard is named its owner now so that whoever writes one does not have to re-decide it. |
| Canonical Source Of Truth    | `mcp/src/agents_remember/serving/supervisor.py`, `mcp/src/agents_remember/serving/pane_signals.py`, `mcp/src/agents_remember/serving/supervisor_heartbeat.py`, `mcp/src/agents_remember/controlplane/escalation_ladder.py`, `mcp/src/agents_remember/controlplane/inbox_backoff.py`, `mcp/src/agents_remember/controlplane/operator_inbox_store.py`, `mcp/src/agents_remember/controlplane/orphan_policy.py`, `mcp/src/agents_remember/controlplane/signal_routing.py`, `mcp/src/agents_remember/controlplane/supervisor_signals.py`, the `orchestration.supervisor`/`orchestration.escalation` families in `mcp/src/agents_remember/kernel/agentic_settings.py`, and the surfacing call sites in `mcp/src/agents_remember/mcp/tools/base.py` and `mcp/src/agents_remember/serving/app.py`.                                                                                                                                                     |
| Current Naming Drift         | `signal-grandparent` is historical terminology from the pre-L13 dead-upstream action; current behavior is `signal-manager`, with upward movement owned by the timed ladder. HFX2-L3's `deliver_inbox_entry` remains implemented through the separate `Delivery Injector` entity. The ladder, signal cooldown, current-manager resolver, and chain-progress predicate are internal substrates of this one supervisor entity rather than separate runtime entities. |
| Key Identifiers              | `SupervisorContext`, `SupervisorFinding`/`SupervisorActionResult`, `run_supervisor_sweep`, `classify_pane_signal`, `SupervisorHeartbeatStore`, `SupervisorSignalCooldownStore`, `_delivery_failure_still_retrying`, `PERSISTENT_FAILURE_ATTEMPTS`, `MIN_REDELIVERY_INTERVAL_SECONDS`, `MIN_RUNG_DWELL_SECONDS`, `rungTransitionAt`, `leafKey`, `subjectAgentId`, `leaf_chain_has_progress`, `derive_leaf_manager_owner`, `derive_skip_level_owner`/`is_seat_dead`, `find_orphaned_workers`, `orchestration.supervisor.{enabled,intervalSeconds,staleCutoffSeconds,redeliverRateLimitSeconds,signalCooldownSeconds,redeliverBudget}`, `orchestration.escalation.{slaSeconds,rungSeconds,nudgeRateLimitSeconds,respawnAfterRung}`, `orchestration.supervisor.*`/`orchestration.escalation.rung` event kinds, `supervisorBanner`, `supervisorHeartbeat`, `SupervisorHeartbeatPayload`, `ServedWorkspaceProjection`/`served_state_tail`. |
| Parent / Child Relationships | Reads `TerminalCatalog`/`OperatorInboxStore`/`ExpectationRowStore`/the nudge store/signal cooldown store directly (never the projection, R3); gives `orchestration_nudges.missing_artifact()` its first caller; owns `mark_missed`/`advance_rung`; checks inbox delivery state, attempt count, and escalation stamp before handing a row to `escalation_ladder.rung_due`; asks `signal_routing` for current-manager and chain-progress facts; uses inbox backoff/signal cooldown for pacing; calls HFX-L8's `retire_entry` for respawn; completion wake enters through `mcp/tools/operator_inbox.py`; hosted by `serving/app.py`; surfaced by `mcp/tools/base.py` and the dashboard cockpit. |
| Often Confused With          | The lower-level catalog liveness hysteresis sweep (260707-HFX-L5, `terminal_liveness.py`) — that module only probes tmux/pane aliveness and persists status transitions; this entity is a broader cross-store reconciliation-and-action layer built partly ON TOP of that liveness state (R2e). Also not `Seat Retirement` (HFX-L8) itself, though this entity now CALLS its `retire_entry` primitive for respawn — retirement authority/mechanics stay owned by that entity, this one only decides WHEN to invoke it. |
| Source References            | [supervisor.py](agents-remember/mcp/src/agents_remember/serving/supervisor.py); [pane_signals.py](agents-remember/mcp/src/agents_remember/serving/pane_signals.py); [supervisor_heartbeat.py](agents-remember/mcp/src/agents_remember/serving/supervisor_heartbeat.py); [escalation_ladder.py](agents-remember/mcp/src/agents_remember/controlplane/escalation_ladder.py); [inbox_backoff.py](agents-remember/mcp/src/agents_remember/controlplane/inbox_backoff.py); [operator_inbox_store.py](agents-remember/mcp/src/agents_remember/controlplane/operator_inbox_store.py); [orphan_policy.py](agents-remember/mcp/src/agents_remember/controlplane/orphan_policy.py); [signal_routing.py](agents-remember/mcp/src/agents_remember/controlplane/signal_routing.py); [supervisor_signals.py](agents-remember/mcp/src/agents_remember/controlplane/supervisor_signals.py); [agentic_settings.py](agents-remember/mcp/src/agents_remember/kernel/agentic_settings.py); [base.py](agents-remember/mcp/src/agents_remember/mcp/tools/base.py); [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| Migration Notes              | HFX2-L3 landed: the delivery contract `_redeliver`/`_post_owner_signal` call through (`deliver_inbox_entry`) is routed through the `Delivery Injector` entity instead of a direct `TerminalPaster.paste` call; `inbox_delivery.py` deliberately NOT added to this entity's evidence (it belongs to `Delivery Injector`'s call-site layer). **260707-HFX2-L4 has now landed** (this pass): the escalation ladder is wired DIRECTLY into `serving/supervisor.py` rather than reached from outside, so per this leaf's curator judgment it EXTENDS this entity's evidence/Description rather than creating a new entity — the ladder's own pure logic lives in two new small `controlplane/` modules with no independent runtime surface of their own (no lifespan task, no settings family beyond what feeds this entity's context). **260707-HFX2-L9 likewise extends the existing entity** rather than creating a new one: the 900-second floor and cooldown store exist to make this sweep safe to re-enable at short observation cadence. The fingerprint above was computed from current worktree content because this pass runs against an uncommitted worktree; closeout should verify/recompute against the landed commit. **The HFX2-L11 deferral recorded here is discharged, and the note was stale before 260731-EFA-L5 rather than because of it.** `supervisor_signals.py` has had a `SupervisorSignalCooldownStore.compact(now, retain_seconds)` since before this leaf's base commit (`e52edaf5`), and `serving/supervisor.py` calls it once per sweep alongside `expectation_store.compact` — one read that both bounds the log on disk and returns the folded cooldown snapshot every per-finding `in_cooldown` check then reads in memory, so the store is neither unbounded nor re-parsed per finding. L5's contribution is the missing half: that read-filter-rewrite now happens under one hold of the log's lock. Verified for this pass at `serving/supervisor.py` L1235 and L1242. **260707-HFX2-L5 forward reference (curator judgment, no code change to this entity):** the leaf's `mcp/tests/test_liveness_simulations.py` proved 6/8 P-15 fixture-zoo incidents fully end-to-end through `run_supervisor_sweep`, but found and documented a real gap in THIS entity's own module: `evaluate_predicates` calls `evaluate_pane_findings(ctx.catalog)` with no capturer override, so `run_supervisor_sweep` always shoots a real `tmux capture-pane` — there is no way to inject a fake pane capturer through `SupervisorContext` today. This is why the chip-stacked-delivery-stall and pane-classified-never-briefed scenarios stay hybrid (predicate-unit classify + real downstream sweep response) rather than full E2E. Threading a capturer parameter through `SupervisorContext`/`evaluate_predicates` is the natural next leaf that would close this gap — a forward reference in the same spirit as the L2-era "the L3 injector" reference this entity's Naming Drift row already records for a different seam. |

**260712-TRH-L5 current disposition.** Confirmed-gone inbox reclamation extends the existing
Supervisor Sweep entity rather than creating a new runtime entity: the sweep now folds the inbox
once, reads one terminal-catalog snapshot, optionally takes one deduplicated tmux-name snapshot,
resolves only eligible supervisor nudge/escalation rows, and compacts before redelivery. Its
body-free `inbox-compacted` event is silent for no-op sweeps; the 48-hour TTL and 500-row cap stay
the fallback. Reviewer residuals F3-F6 are non-blocking. The fingerprint row is intentionally
unchanged for this uncommitted candidate; closeout must recompute it against the landed code tip
and include the new `inbox_reclamation.py` evidence.

**260707-HFX2-L13 current disposition.** The manager accepted reviewer S1 as non-blocking for L13:
current-manager targeting/wake, chain-aware reviewer/curator suppression, cooldowns, and the
five-minute rung floor are current code truth. Active-phase chain credit still excludes an unbound
worker, so bounded false-inactivity refires remain possible until HFX2-L14 S7; this catalog does not
claim that residual is fixed. The fingerprint above uses current worktree blobs and closeout must
verify/recompute it against the eventual L13 commit.

**260707-HFX2-L15 current disposition.** The S7 boundary is now closed through explicit catalog
provenance: an unbound worker/reviewer/curator counts only when the current manager spawned it and
`replacementForLeaf` names this leaf. Same cwd never grants credit. The supervisor's default
redelivery budget is one because each delivery may synchronously wait on calibrated harness-log
evidence; `never-briefed` and stacked-chip pane triggers are removed, while mid-turn/blocked remain
intervention/diagnostic signals. The candidate fingerprint above uses current worktree blobs and
must be recomputed against the eventual L15 commit.

**260707-HFX2-L17 current disposition.** Every supervisor finding and durable condition row carries
`seatRole` with `leafKey`; cooldown and coalescing identity include both. Current manager,
architect, worker, chain-credit, and suspect discovery use binding identity, while the historical
ladder parent hop remains spawn-provenance based. Delivery persistence uses the injected sweep
timestamp. Reviewer O4's `seeded*8` to `seeded*9` test ceiling is one bounded pair-scoped snapshot,
not a divergence finding. The candidate fingerprint uses working-tree blobs and must be recomputed
against the eventual L17 commit.

**Positional 260707-HFX2-L19 current disposition.** Hosted-delivery failures remain in the
persistent redelivery domain while `escalatedAt` is unset and `attemptCount` is below
`PERSISTENT_FAILURE_ATTEMPTS`; only the exhausted counterpart enters the generic unacked ladder.
The F1 `test_supervisor.py` pin proves that boundary through `evaluate_escalation_findings` without a
catalog-side suppression path. The fingerprint above uses current candidate-worktree blobs and must
be recomputed by manager-owned closeout against the eventual L19 code commit.

### Task Document

| Field                        | Value |
| ---------------------------- | ----- |
| Category                     | Planning/runtime projection entity |
| Represents In Reality        | One JSON-primary `ar-task-document/v1` planning record whose structural summary is continuously projected and whose full reader body is loaded only when selected. |
| Description                  | 260707-HFX2-L13 splits the task document across two transport shapes without creating two entities. `observer.snapshots.read_task_documents` emits at most 250 body-free `TaskDocNode` summaries into `/api/state` and `/api/stream`; `bodyRevision` fingerprints the omitted reader fields. `serving.app` exposes `GET /api/task-document?path=...`, which delegates path confinement and schema validation to `read_task_document_body`. `dashboard/src/data/taskDocuments.ts` fetches that full node, and L16's `DetailPanel` merges it over the visible summary with absent-array preservation, caches by `docPath + bodyRevision`, and renders an explicit summary fallback when the body is unavailable. 260731-EFA-L4 declares the body edge (`response_model=TaskDocNode`, with `404`/`503` `HttpDetailRefusal`) and separates the two sub-task row shapes that had been collapsed into one interface: a task-doc master's `TaskSubTaskRefNode` may carry a cross-series `linkedLifecycleId` and is never stamped with `createdAt`, while a series' `SeriesSubTaskNode` carries `createdAt` and never a cross-link; `SubTaskRow` is their union. Creation order is therefore server-side — `snapshots.py::_series_subtask_nodes` sorts it — and `DetailPanel`'s `SubTaskIndex` renders rows in the order received, keeping `orderedByCreation` only on `seriesAsMasterDoc` as an order-preserving safety net. The client sort it removed could never have done anything for a master's rows, which carry no `createdAt` at all. |
| Canonical Source Of Truth    | The JSON-primary task file under `coordination_root/tasks`; `observer/snapshots.py` defines summary/full projection, `observer/projection.py` defines the wire node, `serving/app.py` exposes the body edge, and the dashboard adapter/panel consume it. |
| Current Naming Drift         | `analytics.taskDocuments` still names the always-on collection, but its nodes are summaries after L13; `TaskDocNode` is used for both summary and full-body shapes, distinguished by endpoint and populated body fields rather than a second DTO name. `Analytics.series` is a compatibility master summary, not a second source of task truth. |
| Key Identifiers              | `ar-task-document/v1`, `TaskDocNode`, `docPath`, `bodyRevision`, `TASK_DOCUMENT_SUMMARY_LIMIT`, `SERIES_DOCUMENT_SUMMARY_LIMIT`, `read_task_documents`, `read_task_document_body`, `/api/task-document`, `fetchTaskDocument`, `fullTaskDocs`. |
| Parent / Child Relationships | The task JSON owns authored content; enclosure/lifecycle maps add optional runtime attachment; the always-on projection carries bounded navigation/progress summaries; the serving endpoint returns one confined full node; `DetailPanel` joins the body back to the selected summary by path/revision. |
| Often Confused With          | A series/master aggregation (`SeriesNode`), an enclosure `series-contract.md`, rendered `task.md`, or a second browser-owned copy of the task. None replaces the JSON-primary document. |
| Source References            | [projection.py](agents-remember/mcp/src/agents_remember/observer/projection.py); [snapshots.py](agents-remember/mcp/src/agents_remember/observer/snapshots.py); [app.py](agents-remember/mcp/src/agents_remember/serving/app.py); [taskDocuments.ts](agents-remember/dashboard/src/data/taskDocuments.ts); [DetailPanel.tsx](agents-remember/dashboard/src/panels/DetailPanel.tsx) |
| Migration Notes              | Broadcast bodies are removed end to end, but the 250-node window currently truncates silently and summary nodes retain full step/sub-task lists. The panel cache has no eviction across body revisions. L16 reviewer D-N4 also notes that present body scalars overwrite live summary scalars until `bodyRevision` changes; arrays preserve the summary only when absent from the body. These are accepted follow-ups, not alternate current contracts. The fingerprint uses current L16 worktree blobs and closeout must verify/recompute it against the eventual code commit. **260731-EFA-L5: re-signed, not moved — checked, not assumed.** `observer/snapshots.py` is in this entity's evidence set and did change, but the leaf's three hunks in that file are the deleted gate-compaction cadence constants, `read_gates`, and `read_expectation_rows`. `read_task_documents`, `read_task_document_body`, `_task_doc_node`, `_series_subtask_nodes` and `_series_subtask_created_at` are byte-identical; the summary window, `bodyRevision`, the confinement rule and the server-side sub-task ordering are all unchanged. The only consequence for this entity is arithmetic: every citation into `snapshots.py` past L134 shifted by six lines, and those were repaired on that file's card. |

### Delivery Injector

| Field                        | Value                                                                                                                                                                                                                                                                                                                                            |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Category                     | Runtime delivery/transport protocol                                                                                                                                                                                                                                                                                                              |
| Represents In Reality        | The single mechanism through which any payload class — a spawn brief/session command, an inbox dispatch/nudge/redelivery/signal row — actually reaches a hosted agent session over the tmux paste-into-chat seam, classified into one of four outcomes and read per-harness through one adapter interface. |
| Description                  | 260707-HFX2-L3 lands `serving/injector.py` (`DeliveryRow`/`DeliveryResult`/`DeliveryOutcome`, `deliver(row, *, tmux_name, paster, harness=None)` — the four-way outcome `{acked, landed-unacked, blocked(reason), failed(reason)}`, never a bare boolean) and `serving/harness_adapters.py` (`HarnessAdapter` — `boot_ready`/`composer_state`/`mid_turn`/`mid_turn_behavior`/`blocked_reason`/`turn_started`, a thin composition over `pane_signals.py`/`turn_state.py` with no new pattern table of its own, plus `get_adapter` — named `CLAUDE_CODE_ADAPTER`/`CODEX_ADAPTER`, generic fallback for any other id). Both existing delivery call sites — the spawn-brief/session-command path (`mcp/tools/terminal.py::_deliver_spawn_pastes`) and the inbox-row path (`serving/inbox_delivery.py::deliver_inbox_entry`, which `supervisor.py`'s `_redeliver`/`_post_owner_signal` call) — now route through this one function instead of calling `terminal_paste.TerminalPaster.paste` directly; the raw-spawn seam's separate delivery loop is retired into it. Developer-ruled non-goals: harness hooks, Agent SDK sessions, and the codex app-server protocol are never delivery channels here or downstream of it. |
| Canonical Source Of Truth    | `mcp/src/agents_remember/serving/injector.py` and `mcp/src/agents_remember/serving/harness_adapters.py`. |
| Current Naming Drift         | Referred to informally as "the L3 injector" in the `Supervisor Sweep` entity's Response row before this leaf landed (a forward reference written at L2 time); now resolved to this entity. `deliver_inbox_entry`/`_deliver_spawn_pastes` are the two call-site names — they are consumers of this entity, not the entity itself. |
| Key Identifiers              | `DeliveryRow`, `DeliveryResult`, `DeliveryOutcome`, `deliver`, `envelope_text`, `HarnessAdapter`, `get_adapter`, `CLAUDE_CODE_ADAPTER`, `CODEX_ADAPTER`, `GENERIC_ADAPTER`. |
| Parent / Child Relationships | Called by `serving/inbox_delivery.py::deliver_inbox_entry` (itself called by `serving/supervisor.py`'s `_redeliver`/`_post_owner_signal` — part of the `Supervisor Sweep` entity's Response layer) and by `mcp/tools/terminal.py::_deliver_spawn_pastes` (the MCP spawn-tool payload builder); reads `harness_adapters.get_adapter`, which composes `pane_signals.classify_pane_signal`/`composer_state` and `turn_state.classify_turn_state`/`boot_ready`; wraps the `terminal_paste.TerminalPaster` transport. **Since 260731-EFA-L2 it selects between two explicit paster methods rather than one method with an optional argument**: a row carrying a `dispatch_policy` goes to `paste_dispatch(tmux_name, text, accepted=…, policy=…)` (exact-once, no Enter re-presses, no duplicate re-pastes, and the harness-log acceptance probe is **required in the signature**), everything else to `paste(tmux_name, text, submit=True, accepted=…)`. `paste()` no longer accepts `dispatch_policy` at all, and its old `ValueError("dispatch paste requires a harness-log acceptance probe")` guard is gone — the rule it enforced is now carried by the type. The outcome classification this entity owns is unchanged. |
| Often Confused With          | The lower-level transport it wraps, `terminal_paste.py`'s `TerminalPaster` (that module owns the actual capture-verify/idempotent-retry paste mechanics; this entity owns outcome classification and per-harness interpretation on top of it, never re-implementing the paste itself). Also not the `Supervisor Sweep` entity — that entity is the polling/predicate/action loop that is ONE caller of this entity via `deliver_inbox_entry`, not this entity itself. |
| Source References            | [injector.py](agents-remember/mcp/src/agents_remember/serving/injector.py); [harness_adapters.py](agents-remember/mcp/src/agents_remember/serving/harness_adapters.py); [inbox_delivery.py](agents-remember/mcp/src/agents_remember/serving/inbox_delivery.py); [terminal.py](agents-remember/mcp/src/agents_remember/mcp/tools/terminal.py) |
| Migration Notes              | `InboxDeliveryState` (`controlplane/operator_inbox_records.py`) is deliberately left unchanged by this leaf — a `blocked` outcome rides as a `NEEDS-ATTENTION:`-prefixed `deliveryDetail` string rather than a first-class enum value; a future leaf could widen the dashboard-visible schema to surface `blocked` directly (bigger blast radius: `dashboard/src/types/projection.ts`, `inbox_backoff.py`'s redeliverable-state set). |

**260707-HFX2-L15 current disposition (supersedes the L3 screen-acceptance details above).** The
entity remains one delivery protocol, but `HarnessSessionLog` is now its acceptance authority.
Messages carry their existing unique id; commands are separate and require command plus non-error
stdout evidence; `TerminalPaster` owns one Enter re-press and one verified-absence clear/replace
re-paste; `HarnessAdapter` labels only final failure captures. Spawn, inbox, supervisor, and REST
paste all compose `injector.deliver`, while `TerminalCatalog.bind_session_log` persists the exact
bound id/path without clobbering newer liveness. Reviewer residuals N1/N2/N3/N5 remain documented in
the concrete sidecars rather than becoming alternate entity semantics. The candidate fingerprint
above adds the log, transport, and catalog evidence and must be recomputed against the eventual L15
commit.

**260731-EFA-L4 verification note — this entity no longer describes the running code, and 260731-EFA-L4
did not cause that.** Verified against the current tree: `serving/injector.py` and
`serving/harness_adapters.py` have **no importer anywhere under `mcp/src/`**; the only modules that
import them are `mcp/tests/test_injector.py` and `mcp/tests/test_harness_adapters.py`. Every claim
above about "spawn, inbox, supervisor, and REST paste all compose `injector.deliver`" is therefore
stale, and so are the two named call sites. Current truth, module by module.
`serving/inbox_delivery.py::deliver_inbox_entry` delivers through
`harness_control_client.submit_control_prompt` and immediately `del`s its `paster` argument, which
its own docstring calls a compatibility composition parameter that harness delivery never invokes
and that has no raw-input fallback — so the durable inbox and supervisor path is a protocol
submission, not a tmux paste. `mcp/tools/terminal.py` carries no delivery path at all: spawn refuses
the one-call brief contract outright (`_brief_delivery_separate_refusal`, status
`brief-delivery-separate`) and `_SpawnDelivery` records only launch-phase session-command outcomes —
the function this entry names, `_deliver_spawn_pastes`, exists neither in the tree nor at `HEAD`.
The REST paste route answers with either harness submission evidence or plain pane transport
(`TerminalHarnessDelivery`/`TerminalPaneDelivery`), and `serving/app.py` composes `TerminalPaster`
for the pane half directly. The change landed with `cff3e8f feat: cut hosted sessions over to
protocol bridge`, which is why no fingerprint in the table above ever flagged it: this entity's evidence set
does not include the modules that took the delivery over. The four-way `DeliveryOutcome`
classification survives only in `serving/injector.py` itself, which is now reachable from tests
alone. This paragraph records the finding as current-state truth; deciding whether the entity is
retired, redrawn around the protocol submission path, or reconnected is a code decision, and the
rows above are left intact so that decision is made against what they actually said.

### Harness Capability Snapshot

| Field                        | Value |
| ---------------------------- | ----- |
| Category                     | Runtime capability contract |
| Represents In Reality        | A native Claude, Codex, or Pi installation/session's dynamic authenticated model catalog, model-gated effort choices, settings- or request-resolved initial selection, ordered same-session desired/effective selection, honest mutation evidence, and normalized daemon projection. |
| Description                  | `CapabilitySnapshot` contains dynamic `ModelCapability` rows whose effort choices live under the accepting model. A running adapter returns retained native state through `advertise()`; a short-lived own adapter performs token-free `discover(launch)`. The daemon pre-session catalog caches only successful normalized discovery under the installed executable/effective-argv fingerprint and uses explicit refresh for auth/account invalidation. Claude discovery replaces accepted inherited MCP selectors with one strict empty config so enumeration does not launch unrelated MCP children, while normal sessions preserve their installed MCP configuration. `ResolvedLaunch{harness, model, effort, workspace}` carries either settings/role authority or an optional complete daemon request pair into the one native launch path; 260718-CHATS-L5F R2 makes launch acceptance validate on resolved-model IDENTITY — when several catalog rows share one `resolved_model` and the running harness echoes the resolved id, the REQUESTED alias key wins (`_select_current_model(requested_key=…)` threaded through `negotiate_claude_catalog`, plus `verify_effective_launch`'s `_resolves_to_same_model` guard), so a natively-succeeding launch of an aliased model (e.g. claude `opus[1m]` collapsing onto the default's `claude-opus-4-8[1m]`) is ACCEPTED instead of refused on strict key-equality, while a genuinely different or absent resolved model still fails (codex/pi exact-key guards unchanged); the additive codex-only `resume_thread_id` rides the same opener → runner payload → factory path into the sole `CodexAppServerSettings` site as a native-identity selector in the `launch_args` authority class (never validated or authorized by the opener, refused pre-spawn for non-codex or malformed values). Same-session `set_model` and `set_effort` return exactly the five honest `SetResult` states and join prompt work on the separate Harness Submission Authority timeline; native adapters do not own a second queue. Exact-session submit/reconcile preserves request correlation without paste or resend, while public responses omit private raw evidence. The catalog projects into ACP Sense 1 category-keyed selects without importing ACP transport. 260718-CHATS-L2E extends the contract with two runtime-checkable structural sub-protocols: `InterruptCapableAdapter` (one epoch-guarded native interrupt write — codex `turn/interrupt` on the exact active turn, pi RPC `abort` guarded pre-write by the caller's expected active-operation identity, replay-once per (expected, active) pair) and `AssetSubmitCapable` (asset-carrying submit dispatched only when verified asset references ride). A harness without a seam fails closed typed naming the adapter — claude stays honestly unverified with the CL-3 headless-unproven reason — and asset submissions on non-capable adapters answer an `unsupported` terminal receipt with the exact reason; capability is advertised only with landed installed-runtime fixture evidence captured through the production seam (`control-plane/*` rows, `enablesCapabilities: false`). 260731-EFA-L4 declares this entity's four daemon routes — `GET /api/harnesses/{harness}/capabilities` (`HarnessCapabilityEnvelope`, with `404`/`503` `StatusRefusal` for an uninstalled harness and for discovery being unavailable), `GET /api/terminal/{session}/capabilities` (`CapabilitySnapshotWire`) and the two `set-model`/`set-effort` routes (`SetResultWire`), the last three sharing the `SESSION_CONTROL_RESPONSES` refusal table — and types the spawn-side knob validation on the wire alias: `mcp/tools/terminal._knob_refusal`'s check table is typed `tuple[tuple[SpawnAgentSessionStatus, str \| None], ...]`, so a `model-invalid`/`effort-invalid` status the tool invents is a pyright error at the producer instead of a pydantic `ValidationError` escaping an MCP handler that has no `except` for one. The route declarations are the contract, not the check: these handlers return `JSONResponse`, which FastAPI hands back unserialized, so `mcp/tests/test_serving_response_conformance.py` — which drives every route through the real app and validates the body that came back — is what enforces them. |
| Canonical Source Of Truth    | `harness_capabilities.py` defines `CapabilitySnapshot`, `SetResult`, and the fixed acceptance vocabulary; `harness_capability_catalog.py` owns token-free pre-session cache/refresh; `harness_control_adapter.py` owns the normalized setter port and result truth, while the separate Harness Submission Authority owns ordering/idempotency/operation lifecycle and `harness_control_queue.py` remains a facade; `harness_control_api.py` and `harness_control_client.py` own the daemon/exact-session boundary; `harness_launch.py`, `mcp/tools/terminal.py`, the runner/factory, and `terminal_opener.py` own one settings/request-resolved launch path; `claude_stream_protocol.py` and `harness_control_claude.py` own Claude discovery isolation and native evidence; each native adapter owns its remaining protocol-specific evidence. |
| Current Naming Drift         | `CapabilitySnapshot` is not `AdapterHandshake.capabilities`, which is the fixed control-operation set. `SetResult.acceptance` is mutation evidence, not prompt `SubmissionReceipt.acceptance`; `queued` means admitted for later dispatch by the shared authority, not an adapter-native queue and not already-effective state. `ResolvedLaunch` is the normalized launch selection, while the daemon's `TerminalOpenRequest` is only one request DTO and `AR_SPAWN_MODEL`/`AR_SPAWN_EFFORT` remain provenance. A selectionless roleless request may still adopt the native authenticated catalog default; that is not a second settings default. `requestId` is submission idempotency/correlation, not a model selection key. `resume_thread_id` is a codex-only native-identity selector riding `RunnerConfig`, not a `ResolvedLaunch` member and not a capability claim. |
| Key Identifiers              | `CapabilitySnapshot`, `ModelCapability`, `EffortOption`, `SessionConfigOption`, `ResolvedLaunch`, `LaunchKnobs`, `SetAcceptance`, `SetResult`, `CapabilityCatalogResult`, `HarnessCapabilityCatalog`, `resolve_terminal_open_selection`, `read_control_capabilities`, `set_control_model`, `set_control_effort`, `submit_control_prompt`, `reconcile_control_prompt`, `OpenTerminalResult.launch-conflict`, `advertise`, `discover`, `resume_thread_id`/`resumeThreadId`, `InterruptCapableAdapter`, `AssetSubmitCapable`, `submit_with_assets`, `InterruptResult`/`InterruptAcknowledgement`, `SUBMIT_ASSET_MIME_TYPES`/`MAX_SUBMIT_ASSETS`/`MAX_SUBMIT_ASSET_BYTES` |
| Parent / Child Relationships | `orchestration.roles.<role>` and `rolesPerLevel` resolve through `spawn_agent_session_payload` into `ResolvedLaunch`; the daemon may resolve an optional complete pair into the same type. The shared opener serializes both through one live-identity/batch fence into one runner. The runner performs adapter-owned conflict preflight, transient discovery, model/model-local-effort validation, then fresh runtime construction. After readiness, the bridge serializes setters and prompts; the private exact-session client carries request/response evidence, and the public API strips raw vendor detail. Role-based spawn remains settings-owned and the durable inter-agent inbox/brief bus remains the assignment and messaging root; neither is replaced by capability or submit routes. |
| Often Confused With          | A hardcoded model enum, a global effort ladder, ACP transport, Toad hosting, a native-config environment shortcut, a prompt/composer command, or the durable inbox bus. Enumeration is dynamic and token-free; normalized initial and same-session model/effort never become composer paste, tmux injection, or synthesized session commands. |
| Source References            | [normalized snapshot/result shapes](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) L20-L194 and [strict IPC parsing](agents-remember/mcp/src/agents_remember/serving/harness_capabilities.py) L216-L325; [pre-session cache/refresh](agents-remember/mcp/src/agents_remember/serving/harness_capability_catalog.py) L48-L195; [normalized port](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) L31-L80, L145-L171; [daemon capability route boundary](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py) L156-L289; [first-byte client boundary](agents-remember/mcp/src/agents_remember/serving/harness_control_client.py) L58-L156, L205-L337; [typed launch and validation](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) L17-L182; [role/settings resolution](agents-remember/mcp/src/agents_remember/mcp/tools/terminal.py) L305-L418; [one-opener live truth](agents-remember/mcp/src/agents_remember/serving/terminal_opener.py) L170-L257, L425-L648; [Claude discovery selector replacement](agents-remember/mcp/src/agents_remember/serving/claude_stream_protocol.py) L116-L145 and [discovery-only wiring](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) L246-L260; [Claude same-session evidence](agents-remember/mcp/src/agents_remember/serving/harness_control_claude.py) L233-L308; [Codex ordered selection](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) L221-L306 and [state](agents-remember/mcp/src/agents_remember/serving/codex_app_server_session.py) L210-L309; [Pi mutation/readback transaction](agents-remember/mcp/src/agents_remember/serving/pi_rpc_configuration.py) L24-L165 |
| Migration Notes              | ACPUI-L5 live-confirmed the complete own-adapter matrix and closed Claude discovery amplification: accepted pre-separator MCP selectors are replaced only for ephemeral discovery, while normal session startup keeps the installed configuration. Captured model rows, effort menus, versions, process costs, and catalog counts remain installation evidence rather than enums or capacity policy. Claude Code 2.1.210 Fable remains live-switchable with generic mapping for any future native refusal; Codex selection remains queued until the next accepted turn on the same thread; Pi preserves model-error versus thinking-clamp/readback asymmetry. A startup-failed bridge can still surface `control command queue is stopped`, but terminate/retire retain the detail and reap the host. The 17-path fingerprint is computed against the current committed L4 base; manager closeout must recompute it after the L5 code commit. |

### Harness Submission Authority

| Field | Value |
| --- | --- |
| Category | Cross-layer hosted-control lifecycle protocol |
| Represents In Reality | The one bridge-generation authority that decides whether prompt/model/effort work is queued, dispatching, completed, withdrawable, ambiguous, or terminal, and projects that truth to the cockpit. |
| Description | `HarnessSubmissionAuthority` owns one epoch-bound prompt/setter timeline. Admission binds immutable request id, source, payload digest, and operation ref; async preflight is followed by a lock-linearized dispatch claim; queued withdrawal competes atomically with that claim. Adapters dispatch immediately under final write guards and report exact full-ref completion. Early exact completion may dominate a later unknown receipt, while id-only/FIFO/stale evidence cannot release a successor. Public status/withdraw is cockpit-only and raw-free. Timeline and duplicate ledgers are bounded without evicting live, active, or unknown work; terminal prompt text is dropped while digest/correlation remain. The browser keeps the same epoch/id/text through retry/reconcile, uses one evidence fold, and restores a withdrawn composer draft only by revision CAS. The additive `provenance` batch reads the same records epoch-checked and read-only: each exact request id discloses its source (cockpit/terminal/durable), state, submitted/updated/accepted timestamps, and vendor correlation to the exact-session daemon peer over the private socket, with honest `not-found` — never an inferred origin. 260718-CHATS-L2E adds three channels over the same records: the paged never-bodies `operation_timeline` enumeration (all three prompt sources plus set-model/set-effort identity, count-capped and byte-budgeted pages carrying `latestSequence`/`evictedBeforeSequence`/`truncated`/`bridgeEpoch`, completeness as the union of pages, eviction floor tracked at the sole pop site), the pre-tombstone `WithdrawalRecovery` payload (the exact body crosses once inside the already `cockpit_only` withdrawal response at the true transition; replays carry none; tombstone timing/class byte-preserved), and the asset-carrying submit channel (idempotence digest covers canonical asset identity only when assets ride, dispatch routes to `submit_with_assets` on capable adapters, non-capable adapters answer `unsupported`, and native acceptance evidence crosses as additive receipt `assetIds`). 260731-EFA-L4 declares the public surface: `submission-authority`, `submission-status`, `withdraw`, `submit` and `reconcile` each name their success model (`SubmissionAuthorityWire`, `SubmissionStatusBatchWire`, `WithdrawalResultWire`, `PublicReceiptWire`, `PublicReconciliationWire`) and their refusal models, with `submit` carrying two refusals no other control route can produce — `409` for an unsupported seat, a stale bridge epoch, or a reused request id, and `503 PreDispatchFailureRefusal` for the certified retry-safe pre-dispatch failure. The 17 conversation control routes do the same through `CONTROL_RESPONSES`/`INTERRUPT_OUTCOME_RESPONSES`/`WITHDRAW_OUTCOME_RESPONSES`. None of these declarations is self-enforcing — the handlers return `Response` objects, which FastAPI passes through — so `mcp/tests/test_serving_response_conformance.py` is what holds them, by driving the real app and validating the body that came back.
| Canonical Source Of Truth | `mcp/src/agents_remember/serving/harness_submission_authority.py` for server lifecycle/linearization/retention; `harness_control_models.py`, API/bridge/client/adapter seams for transport and projection; native Claude/Codex/Pi adapters for guarded exact completion; dashboard `submitMachine.ts`, `submitClient.ts`, and `submissionLifecycleClient.ts` for monotonic browser projection and authoritative pop-back. |
| Current Naming Drift | `HarnessControlQueue` remains a compatibility class name but is now only a facade. `queued` means authority-admitted and withdrawable, not a vendor/native queue. “Pop-back” is UI language for an exact server withdrawal followed by revision-safe recovery; it is not local queue mutation, rewind, or resend. |
| Key Identifiers | `HarnessSubmissionAuthority`, `ControlOperationRef`, `bridgeEpoch`, `operationSequence`, `expectedBridgeEpoch`, `submission/status`, `submission/withdraw`, `submission-provenance`, `SubmissionProvenance{,Batch}`, `pre-dispatch-failed`, `retrySafe`, `foldSubmitEvidence`, `withdrawLatestQueuedSubmission`, `pendingWithdrawal`, `submissionRecovery`, `OperationTimeline{,Item}`, `operation-timeline`, `evictedBeforeSequence`, `WithdrawalRecovery`, `AssetReference`, `assetIds`. |
| Parent / Child Relationships | Created once by the hosted control bridge and surfaced through the legacy queue facade; calls dispatch-now native adapters; receives their direct completion before coalesced publication; API/IPC/client expose normalized authority/status/withdraw; dashboard store/composer/QueuePreview consume the raw-free projection. Capability Snapshot supplies model/effort vocabulary but does not own lifecycle ordering. |
| Often Confused With | The durable inter-agent inbox (assignment/message root), Delivery Injector (tmux-paste delivery for older inbox/spawn seams), adapter-native queue state, browser optimistic state, or interaction gate answers. None can grant prompt lifecycle authority. |
| Source References | [server authority](agents-remember/mcp/src/agents_remember/serving/harness_submission_authority.py); [bridge](agents-remember/mcp/src/agents_remember/serving/harness_control_bridge.py); [API](agents-remember/mcp/src/agents_remember/serving/harness_control_api.py); [frontend fold](agents-remember/dashboard/src/data/submitMachine.ts); [frontend lifecycle](agents-remember/dashboard/src/data/submissionLifecycleClient.ts); [shared composer](agents-remember/dashboard/src/panels/SessionComposer.tsx) |
| Migration Notes | FEUI-L5 replaces the ACPUI-L3/L4 model in which `HarnessControlQueue` and native busy/steer paths could be read as co-authorities. Review rounds exposed and closed real gaps in deadline handling, answer-channel separation, full-text retention, source/draft provenance, exact retry certification, response-loss intent, early-completion dominance, revision recovery, full-ref dedupe, bounded Codex correlation, not-found projection, keep-current dismissal, and central response/poll ordering. The candidate fingerprint uses working-tree blobs; closeout must recompute it against the landed code commit. |

## 260718-CHATS-L5I Entity Clarifications

**Harness Capability Snapshot** now carries a narrow fixture-backed interrupt verdict from the control layer into the active-conversation view. That bridge is deliberately single-source: proving native interrupt support does not promote steer, follow-up, attachment, policy, history, or telemetry capability claims.

**Harness Submission Authority** distinguishes a timely accepted/queued receipt from terminal delivery. A bounded dispatch-acceptance grace can return `queued` before a healthy native echo arrives, but only later lifecycle evidence settles the operation; a receipt must never be projected as a completed turn.

These are prose-only clarifications of existing load-bearing entities. Their `git-blob-set-v1` rows intentionally remain pinned until the code commit supplies truthful `HEAD` blobs.

## 260731-EFA-L2 Entity Clarifications

**No entity was added, removed, split or merged in this leaf, and no entity's identity, boundary or
canonical source of truth moved.** 260731-EFA-L2 armed the quality gate at full strength with zero
exemptions; the code it touched changed *shape* — long parameter lists became named values, long
routers became named branches, a few guards were deleted at their cause — which is why nineteen
fingerprints moved at once. Read a changed fingerprint here as "the implementation was re-signed",
not "the concept changed". The specifics below are the ones that alter what a caller may write.

**Coordination Context**, **Path Rule** and **Branch-Gated Cross-Repo Source** share one changed
fact: the resolver's *input* API. `resolve_coordination_context(code_repository_name=None,
workspace_root=None, code_repository_root=None, *, hints: CoordinationHints | None = None, selector:
EnclosureSelector | None = None)` replaces the nine former resolution keywords; `CoordinationHints`
carries `topology` / `coordination_root` / `settings_path` / `onboarding_root`, and
`EnclosureSelector` carries the contract/leaf selection. All four models (plus `CodeRepository` and
`CoordinationRoots`, which type what the private helpers pass between them) are re-exported from the
`kernel.coordination_context_resolver` facade, which remains the supported import path. **The
resolved context — every `Key Identifiers` field recorded above, resolution order, the
onboarding-root branch and contract-lookup precedence — is unchanged.** Only how a caller *asks*
moved. `memory/baseline.py`, `memory_quality`'s two CLI entry points and `serving/scope.py` were
updated accordingly.

**Delivery Injector** is the one entity whose contract genuinely narrowed: dispatch delivery is now
a separate paster method with a mandatory acceptance probe rather than an optional argument on the
ordinary paste. See the entity's Parent / Child Relationships row.

**Harness Submission Authority** now has exactly one capability decision point. The dispatch-time
asset-capability guard was reduced to an assert, and `_unsupported_prompt_locked` decides under the
same lock that enrols the record — so the decision and the enrolment cannot disagree. Its bounds are
declared as one `SubmissionLimits` (`timeline`, `ledger`) and its snapshot access as one
`BridgeSnapshotPort`. `harness_control_ipc.py` collapsed two `if action == …` chains into a single
`_CONTROL_ACTIONS` table with one unknown-action refusal (the separate "unknown capability action"
message is gone; capability actions are ordinary table entries). `harness_control_client.py`'s
`_submission_state` now raises for anything outside the seven lifecycle states unless
`optional=True`, so the removed "operation timeline item requires lifecycle state" re-check was a
duplicate, **not** a relaxation.

**Seat Retirement** and **Seat Landing Archive** now share one provenance value: `SeatClosure`
(`at`, `reason`, `edge`, `by_session`) in `serving/retire.py`, written by both closure paths —
retirement marks `killed`, landing marks `archived`. The four facts are one record: a timestamp
with no reason is an unexplained tombstone, and a reason with no edge cannot be traced back to the
chain step that closed the seat. Retire authority policy and landing selection rules are unchanged.

**Supervisor Sweep** gained `EscalationSchedule` (`sla_seconds`, `rung_seconds` — one timetable,
because raising the SLA without the dwell only moves where the same storm starts) and `OwnerSignal`
(one owner-addressed signal and the seat it is about, inseparable because coalescing looks a row up
by `(ask, kind, leaf, role)` and renewal rewrites the subject from the same value). The
deterministic posture — zero tokens, pure code, predicates reading the durable stores rather than
the projection — is unchanged.

**Seat Binding Identity** and the liveness surface: `TerminalCatalogLivenessConfig`,
`DEFAULT_LIVENESS_HYSTERESIS` and the four `DEFAULT_LIVENESS_*` constants **moved from
`terminal_liveness.py` to `terminal_catalog.py`**. Any reference to
`terminal_liveness.DEFAULT_LIVENESS_FAILURE_THRESHOLD` or its siblings is stale. Values unchanged.

**Worktree Contract** and **Worktree Integration**: `worktree_contract.py` names `RepoBranchPlan`
(one repository's branch plan for a worktree pair), `ContractTask` (the task a contract speaks for)
and `LeafIdentity`; `integrate.py` names `IntegrationSources` (where each side's source branch stands
when integration starts, with `replay_required()` as a method rather than a caller-side computation)
and `IntegratedCommits` (**the three commits one integration lands — code, memory content, contract
rewrite — consumed all three or none**); `cleanup.py` names `RetiringBranch`; `guidance.py` splits
lifecycle phase reporting into `_reclaimed_phase` / `_post_integration_phase` /
`_pre_integration_phase`. The contract fields, the integration order and the ledger alignment rules
are unchanged.

**Runtime AGENTS Template Package**: `install/runtime.py` names `RuntimeTreeSync` (one packaged tree
mirrored into the coordination root — `prune_tree` and `copy_tree` both take it),
`ProviderDependencyInstall` and `RuntimeInstallRequest`. The four packaged `AGENTS.md` templates
themselves are byte-identical; only the installer's call shape moved.

**Onboarding Unit** and **Memory Quality Control**: verdict construction was centralized per
classifier — `check_missing_onboarding.py` splits into `_missing_sidecar_onboarding` /
`_missing_inline_onboarding` with the unsupported-storage-mode fallthrough as the visible last
statement, `sidecar.py` builds every `DriftRow` through one `row(...)` closure that fixes identity
and verification stamp (with `_early_classification` grouping the three pre-diff verdicts), and
`entities.py` takes an `EntityCatalog` value. **The classification vocabulary, trust levels and
emitted rows are byte-identical**, which matters here because this entity's own drift output is what
readers of this catalog rely on.

**Provider Degradation Protocol**: `degradation.py` names `_DegradationTransition` (the event id,
from-state, to-state and timestamp that *are* the event's identity — everything else in the payload
is the evidence justifying it) and posts alerts through the control-plane `InboxMessage` /
`InboxRouting` / `InboxAddress` / `InboxPoster` bundles plus `HostedSessionRuntime`. States,
thresholds and alert content are unchanged.

**External Memory Ledger**, **Memory Baseline Adoption** and **Task Document** were re-signed by
their neighbours rather than changed in themselves: `memory_ledger.py` was touched only by the
whole-tree `ruff format` pass, `memory/baseline.py` only by the resolver-hints call shape, and the
`Task Document` evidence only by `serving/app.py`'s and `observer/snapshots.py`'s own re-signing.

Fingerprints in the table above were recomputed from the **staged index** — the exact content
closeout will commit — because this pass runs before the code commit. Closeout should re-verify them
against the landed `HEAD`.

## 260731-EFA-L4 Entity Clarifications

**No entity was added, removed, split or merged in this leaf, and no entity's canonical source of
truth was relocated.** 260731-EFA-L4 gave the repository's escape hatches real types: `dict[str,
Any]` returns became declared models and TypedDicts, and vocabularies that had been carried as two
or three hand-written copies became one declaration each, imported by everyone else. Read a changed
fingerprint here mostly as "this entity's vocabulary is now checkable", not "the concept changed".
Four changes are exceptions, in that they alter what the code does rather than what the checker can
see, and each is recorded in its own entry above: **Worktree Contract** — the closeout quality gate
now stages the whole task worktree before it runs (an index mutation that precedes the gate and is
not undone on refusal), the contract reader became total, and three response keys are now omitted
where they used to be filled in; **Memory Quality Control** — the drift summary can report `error`
instead of raising out of the tool; **Seat Retirement** — the tool's `ok` is derived once from a
named status set instead of being written out per call site; **Task Document** — a no-op client-side
sub-task sort was removed in favour of the server ordering that was already authoritative.

**Worktree Contract** is the largest entry. Three facts are worth stating separately because they
are easy to state wrongly. *First*, the read/write asymmetry: `validate_contract(contract, *,
path)` refuses all six vocabulary cells, but `load_contract` calls it only after `_vocabulary_cell`
has already narrowed every cell, so the refusal is reachable from `write_contract` alone. **A
contract written directly as markdown — hand-edited, produced by an older build or a newer one —
still loads with an off-vocabulary cell in it.** That cell degrades to the declared default, its raw
token is quarantined in `unknown_cells`, it surfaces as `unknownContractCells` on the context
packet, and the file heals the next time a lifecycle tool rewrites it. It is not rejected. (The
document-level refusals are unaffected: absent or unclosed front matter, an unrecognized schema, a
missing required field, an empty required path, a leaf with no `leaf_id`, and an external-memory
leaf with no memory repository all still refuse on read, as they did.) That is the whole point: no lifecycle tool catches
`ContractError`, so refusing on read would leave a task that `worktree_closeout_apply`,
`worktree_integrate`, `worktree_cleanup`, `worktree_sync` and `worktree_abandon` had all
simultaneously lost the ability to touch. *Second*, the six cells are now moved by `ContractCells` +
`amend_contract` rather than `dataclasses.replace`, because typeshed declares
`replace(obj, /, **changes: Any)` and one `Any` in a third-party stub voided the guarantee: an
off-vocabulary literal at any of the six fields produced no pyright diagnostic at all.
`test_wire_vocabulary_exhaustiveness` keeps the loophole shut from the other side, with a scan that
no `replace` call anywhere may carry one of these keywords. *Third*, nine refusals in
`worktree_contract.py` now name the file they are about, in two shapes — `<problem>: {path}` for
the document as a whole, `<problem>: <detail> (in {path})` for something inside it — and `_path`
additionally names the front-matter line (`section.key`), because `repo_path` and `worktree` each
appear under both `code:` and `memory:`.

**Worktree Contract** and **Worktree Integration** also share the reconciliation that motivated the
leaf. `models/worktree.py` had been retyping six vocabularies that other modules produce, and the
copies had drifted in six places at once: `chat-task`, `reopened`, `carryover-pending`, `abandoned`,
`request_carryover_decision` and `memory_carryover_apply` were all writable by the producer and none
of them validated at the wire model — which, by this leaf's own scan, made the context packet reject
165 of the 213 series contracts on disk with a `ValidationError` that no handler on the tool path
catches. The fix is directional: `models/worktree.py` imports from `worktree_contract.py` and
`worktrees/modules/guidance.py`, never the reverse. `application/worktree_status.py` now builds
`WorktreeSummary` instead of returning a dict for `application/context_packet.py` to
`model_validate`, which is what moves the failure from response time to type-check time.
**One response shape genuinely changed**: `nextTool`, `nextArgs` and `nextRequiredArgs` are now
omitted when the producer omits them, where the projection used to substitute `""`, `{}` and `[]`.
The leaf measured 48 of 213 responses losing a `"nextRequiredArgs": []` key. An absent key means
what the empty list meant; the invented `""` was a `nextTool` value no producer declares.

**Memory Quality Control**'s change is small and load-bearing: `DriftStatus` is declared once, with
`error` in it, and `models/drift.DriftSummary` gained the matching `error` field. Before, an
`include_drift` context packet against a repository whose onboarding root does not exist raised out
of the tool — on exactly the call meant to explain that. The classification vocabulary, trust
levels and emitted drift rows are unchanged.

**Supervisor Sweep**, **Seat Retirement**, **Seat Landing Archive**, **Task Document**, **Harness
Capability Snapshot** and **Harness Submission Authority** were all reached by the same HTTP-wire
pass, and it carries one caveat that must not be paraphrased away. `serving/response_contract.py`
(plus `serving/conversation/response_contract.py`) declares a strict `extra="forbid"` model for
every **HTTP** route the serving app registers — all 61 of them, and only those: the websocket
`WS /api/terminal/{session}` has no declaration at all, as this paragraph says again below. Each
route now names its success model and its per-status refusal models. **That declaration is not the
enforcement.** FastAPI applies `response_model` only to values it serializes itself, and **57** of
the 61 handlers return a `Response` subclass directly while **two more** — `GET /api/stream` and
`GET /api/events` — are async generators feeding an `EventSourceResponse`; on all **59** of those
the decorator contributes an OpenAPI schema and validates nothing.
Only `GET /api/terminal/sessions` and `GET /api/harnesses` return a bare dict, and those two now
answer HTTP 500 on payload drift — a deliberate fail-loud trade, mitigated by a CI check that
compares `TerminalCatalogEntry.to_json`'s emitted key set against the wire model's aliases. The real
enforcement for the rest is `mcp/tests/test_serving_response_conformance.py`, which drives every
route through the real app and validates the body that came back. `WS /api/terminal/{session}` is
the only undeclared route, found by its route class rather than by a path skip-list.

**The dashboard mirror is generated from the Python projection schema and checked for drift.**
`dashboard/src/types/projection.ts` is marked generated/do-not-edit, names
`WorkspaceProjection.model_json_schema()` as canonical, and names
`scripts/sync-projection-types.py` plus its `--check` command. The generator writes the schema and
TypeScript outputs when not checking, while `check()` reports out-of-sync files without writing
when `--check` is used cit:(["GENERATED FILE", "DO NOT EDIT", "Canonical core model:"], dashboard/src/types/projection.ts:1-2) cit:(["WorkspaceProjection.model_json_schema()"], dashboard/src/types/projection.ts:2-4) cit:([`Generator`, "Drift check"], dashboard/src/types/projection.ts:5-5; dashboard/src/types/projection.ts:7-7) cit:(["sync_generated_files(root)", "out of sync"], scripts/sync-projection-types.py:49-49; scripts/sync-projection-types.py:62-62) cit:(["def check(repo_root: Path) -> int:", "--check", "do not write files"], scripts/sync-projection-types.py:25-25; scripts/sync-projection-types.py:27-27; scripts/sync-projection-types.py:43-43).
This is a generated mirror with an explicit drift gate, not a hand-maintained/no-generator surface.

**External Memory Ledger** and **Delivery Injector** were re-signed by their neighbours rather than
changed in themselves. `kernel/memory_ledger.py` and `memory/baseline.py` are untouched; the ledger
entity's two changed evidence files, `closeout.py` and `integrate.py`, moved only in the
contract-amend and staged-gate paths, and the one fact that reaches this entity is that a refused
quality gate now commits nothing at all, so no ledger row is published either. `Delivery Injector`'s
single changed evidence file, `mcp/tools/terminal.py`, moved only in `_knob_refusal`,
`_spawn_refusal`, `_retire_payload` and `_rename_payload`; `serving/injector.py` and
`serving/harness_adapters.py` are untouched. Checking that turned up drift **this leaf did not
cause and could not have caused**: those two modules have no importer anywhere under `mcp/src/`, so
the `Delivery Injector` entry describes a mechanism the running code no longer uses. The finding is
written up as current-state truth in a dated verification note under that entity, with the evidence
for each claim; it is not deferred, and it is not silently patched over either, because choosing
between retiring the entity, redrawing it around
`inbox_delivery.deliver_inbox_entry`'s protocol submission, and reconnecting the injector is a code
decision and not a curator's.

**Coordination Context** moved without its fingerprint moving, which is the case this table cannot
flag: `kernel/coordination_context/models.py` is not in its evidence set, and that is where
`CoordinationContext.memory_mode` became the worktree contract's `MemoryMode` alias. The resolved
values are unchanged; the declaration is now shared.

Two vocabularies that L4 made checkable belong to no entity in this inventory and are recorded here
so a later curator does not go looking for them: `observer/lifecycle_state.py` now composes `State`
from a `LiveState`/`TerminalState` partition validated at import by `check_state_partition` (with
`EndOutcome` as the terminal half, since a lifecycle reaches a terminal state only by being ended),
and `observer/projection.py` derives the `Metrics` per-state buckets from the live half — which is
how `awaitingDeveloperCount` came to exist, a state that had been inflating `lifecycleCount` and
`totalTokens` while landing in no bucket at all.

The TypeScript mirror **now holds the same partition, in the same shape** — a worker landed it in
`dashboard/src/types/projection.ts` after the first pass of this leaf's curation, so any card still
saying otherwise is stale. It writes out `LIVE_STATES` (four) and `TERMINAL_STATES` (two) as the
halves, spreads `LIFECYCLE_STATES` from them, derives `State` from that tuple, and binds
`ACTIVE_STATES` to the live half **directly** rather than by subtraction — there is no second list
left to disagree. State the limit precisely rather than trading one overclaim for another: the
mirror refuses double-filing at **compile** time (`StatesAreFiledOnce = FiledOnce<ActiveState &
TerminalState>`; verified by mutation — filing `"completed"` live fails with
`error TS2344: Type '"completed"' does not satisfy the constraint 'never'`), but it **cannot** refuse
a duplicate *within* one half, because `Literal["a", "a"]` collapses to one member in Python while a
TypeScript tuple keeps both. A duplicated half compiles clean and is caught only at runtime, by
three assertions in `dashboard/src/test/contract.test.ts`. Nothing enforces the agreement between
the two vocabularies in either direction — that is link C above, in its most load-bearing instance.

**No fingerprint hash and no evidence path in the table above was hand-edited.** Eleven entities
have at least one changed evidence blob and their fingerprints are therefore stale — Memory Quality
Control, External Memory Ledger, Worktree Contract, Worktree Integration, Seat Retirement, Seat
Landing Archive, Supervisor Sweep, Task Document, Delivery Injector, Harness Capability Snapshot and
Harness Submission Authority. Closeout must recompute all eleven against the landed `HEAD`; they
cannot be computed here, because `git-blob-set-v1` resolves `HEAD:<path>` and this leaf's code is
uncommitted. Verification metadata is pinned until closeout stamps the commit.

## 260731-EFA-L5 Entity Clarifications

**No entity was added, removed, split or merged in this leaf.** 260731-EFA-L5 gave the six
append-only control-plane JSONL stores one declared storage contract, `ar-durable-store/1.0` in the
new `controlplane/durable_store.py`: every append and every rewrite of every log takes that log's
`flock` unconditionally, in every process; each log names a single compaction owner (with one
declared exception); records carry a `schemaVersion` whose unknown major is refused and unknown
minor accepted; and the read policy is split deliberately rather than uniformly — **only `GateStore`
and `ExpectationRowStore` carry both a strict and a tolerant reader**. `OperatorInboxStore` is strict
only; attention dismissals, orchestration nudges and supervisor signals are tolerant only, and their
rewrites run off that single tolerant read, so those three drop an unparseable row permanently. That
is tolerable only because none of the three carries authority; the rule the contract actually states
is that **every rewrite of an authority-bearing log reads strictly**, not that every rewrite does.

The defect it closes is record loss under ordinary two-process operation. **No base-commit
measurement artifact is committed to this tree**, so every base-commit rate below is checkable only
as "the source says so". Two figures are corroborated across independent sites and are quoted here on
that authority: **31.45%** on attention dismissals (`durable_store.py`, `supervisor_signals.py`) and
**11.50%** of appended gate snapshots (`store.py`, which also reports 100% in a deterministic
forced-window scenario). The remaining rates, the run count, and the whole-records-not-torn property
rest on `durable_store.py`'s module docstring alone.

One base-commit fact *is* checkable, and it is the one worth citing:
`test_controlplane_store_durability.py::HarnessSensitivityTests` extracts the base commit with
`git archive` at test time and asserts the forced scenario loses a record in each of the five
unlocked stores and none in operator-inbox. The post-fix zeros are likewise asserted, by
`MultiProcessDurabilityTests` — but over five stores rather than six in the `forced_unlink` scenario
(attention dismissals has no `append` and is excluded by construction), and the torn-line and
raised-error zeros only in `stress`.

**Five entities have at least one changed evidence blob.** Intersecting each entity's `Evidence
Paths` against the leaf's 25-file changed set gives exactly: External Memory Ledger, Worktree
Contract, Provider Degradation Protocol, Supervisor Sweep, Task Document. **Three moved and two were
only re-signed**, and the split is not guessable from the file list — it needed reading the hunks.

**Moved — Worktree Contract.** The persisted artifact itself changed: `series-contract.md` front
matter now carries `schemaVersion` under `schema:`, and `load_contract` gained a document-level
refusal for an unknown major. Three things are easy to state wrongly here. *First*, the constant and
the policy are **reused, not redeclared** — `CONTRACT_SCHEMA_VERSION = SCHEMA_VERSION` and the
refusal calls `schema_version_supported`, both from `controlplane/durable_store.py`, so the tree has
one version rule rather than two that can drift. *Second*, this is **not** a seventh vocabulary
cell. The L4 entry above draws the read/write asymmetry carefully — a cell outside its vocabulary
degrades and is quarantined, because refusing it would strand a task that no lifecycle tool could
close, integrate, clean up or abandon — and `schemaVersion` sits on the other side of that line,
with absent front matter and an unrecognized `schema`. *Third*, the refusal is unreachable for
anything this build wrote: an absent line means 1.0 and is accepted, and 214 `series-contract.md`
files under this workspace's coordination tasks root carry **zero** `schemaVersion` lines today. It
can only fire on a document a future major wrote, which is what "telling an old record from a new
one" means and why no migration exists.

**Moved — External Memory Ledger, in its contract rather than its behaviour, and the distinction is
the point.** `kernel/memory_ledger.py::write_ledger` is byte-identical: still
`mkdir` + `write_text`, still no lock, no temp-and-rename, no fsync — in the same leaf that gave all
six JSONL stores exactly those things. What L5 added is a 20-line docstring recording requirement
R12's ruling, **degraded not unrecoverable**, and a ruling is a change to what the entity guarantees
even when no instruction changed. It was settled by measurement: all six `write_ledger` call sites
`git add memory.md` and commit within the next two statements, so the durable authority for a
mapping is the git object and a truncated file costs only the uncommitted delta; and nothing under
`observer/` or `serving/` writes the ledger at all, so there is no second daemon to serialize
against and a lock would guard nothing. **The load-bearing consequence is a new obligation on
callers** — write and commit in the same function — which is now recorded on that file's card as an
invariant, because a seventh caller that defers its commit turns "lose a delta" into "lose the
mapping history".

Two corrections to that docstring's own precision were verified and carried into the file card
rather than repeated here as fact. It says `observer/snapshots.py` "imports `load_ledger` and
nothing else"; it imports `LedgerError`, `LedgerRow` and `load_ledger` — three names, none of which
writes, so the claim that matters holds. And it says the five callers are "reached only through MCP
tool registrations"; `worktrees/modules/cli.py` registers `start`, `closeout` and `integrate`
subcommands and `worktrees/git_worktree_manager.py` ends with
`if __name__ == "__main__": raise SystemExit(main())`, so three of them are also reachable as a
script. That is a short-lived process on the same commit-immediately path, so the ruling stands, but
the accurate premise is "no concurrent daemon writes this", not "only the MCP process ever writes
this".

**Moved — Supervisor Sweep.** Both of its changed evidence files changed *about this sweep's own
durability*, not incidentally. `supervisor_signals.py`: the cooldown log the sweep owns went from
unlocked to locked across read **and** rewrite, and the reason the earlier draft left it unlocked is
worth carrying — it has one writer, which was true and irrelevant. The proof run measured 31.45%
loss on its structural twin, attention-dismissals, whose single-writer claim was just as true; "one
process writes this file" is a deployment fact, not a structural one. `operator_inbox_store.py`: the
inbox is **the leaf's one declared exception** to single-owner compaction, because both long-lived
processes must physically remove rows — the MCP deletes a cancelled gate's inbox rows at the moment
it cancels the gate, and this sweep must resolve and compact under one continuously held lock so a
consume that won the lock stays terminal. Neither removal can move to the other process without
moving the decision it implements, so this is the one log where the lock is the whole mechanism
rather than a backstop behind an owner — which is what it already was, and why its pre-existing
flock reads as the right call kept rather than a habit inherited.

**Re-signed, not moved — Provider Degradation Protocol.** Its one changed evidence file,
`controlplane/operator_inbox_records.py`, moved only in `OperatorInboxCompatibleRecord`, which now
derives from `DurableRecord` and so carries `schemaVersion` and its unknown-major refusal on every
`OperatorInboxEntry` — including this entity's `degradation-alert` rows. This is the same shape as
the HFX2-L1 note already in its Migration Notes and gets the same answer: the detector, the
healthy/degraded/critical state machine, the thresholds, the failsafe and the
`AgentRole`/`InboxMessageKind` literals are untouched. One detail is worth having recorded rather
than rediscovered: this store deliberately keeps `extra="allow"` and its named forward-compatibility
allowlist instead of the contract's default `extra="forbid"`, and is the contract's one declared
`extra` exception.

**Re-signed, not moved — Task Document.** `observer/snapshots.py` is in its evidence set and did
change, but the leaf's three hunks there are the deleted gate-compaction cadence constants,
`read_gates`, and `read_expectation_rows`. Every task-document reader is byte-identical. The only
consequence for this entity is arithmetic: `snapshots.py` citations past L134 shifted six lines, and
those were repaired on that file's card.

### Declarations that now live outside the entity's evidence set

This is the gap the fingerprint cannot see, and it is recorded rather than quietly closed, because
changing an evidence set changes what `git-blob-set-v1` hashes and is therefore a deliberate
decision rather than a curator's to make silently. **Three instances, all caused by this leaf:**

- **Worktree Contract.** The rule that decides whether a `series-contract.md` loads at all —
  `SCHEMA_VERSION`, `SUPPORTED_SCHEMA_MAJOR`, `schema_version_supported` — now lives in
  `controlplane/durable_store.py`, which is not in this entity's evidence set. Raising
  `SUPPORTED_SCHEMA_MAJOR` would change which contracts this build accepts and would not move this
  entity's fingerprint by a single bit.
- **Supervisor Sweep.** The declarations naming this sweep the compaction owner of expectation-rows,
  orchestration-nudges and supervisor-signals, and declaring the operator inbox ownerless, are all
  `StoreOwnership` values in `controlplane/durable_store.py` — outside the evidence set. So are
  `controlplane/expectation_rows.py` and `controlplane/orchestration_nudges.py`, two stores this
  sweep drives that the set has never named.
- **External Memory Ledger.** The ruling itself is inside the set (`kernel/memory_ledger.py`), but
  the caller obligation it depends on is not: `worktrees/modules/start.py` and `memory/carryover.py`
  are two of the six `write_ledger` call sites and neither is in the evidence set, which names only
  `closeout.py`, `integrate.py` and `baseline.py`.

**And one gap this leaf makes newly visible rather than creates:** the whole `ar-durable-store/1.0`
contract — the lock policy, the ownership register, the two read policies, the schema-version rule —
belongs to **no entity in this inventory**. Checked against every `Evidence Paths` cell in the table
above: `controlplane/durable_store.py`, `store.py`, `records.py`, `expectation_rows.py`,
`attention_dismissals.py`, `orchestration_nudges.py`, `enforcement.py`, `gate_policy.py` and
`interaction_retention.py` appear in none of them, and neither do `mcp/tools/gates.py`,
`mcp/server.py` or `cli/dashboard.py`. The control plane is visible to this catalog only through
Supervisor Sweep's inbox/signal entries and Provider Degradation Protocol's record file — which
means the gate store, the artifact whose `applied` marker stops one human approval being consumed
twice, is not covered by any fingerprint at all. Whether that
warrants a new entity (a "Durable Control-Plane Store" peer of Supervisor Sweep) or an evidence-set
extension on the existing ones is a decision for the manager and the `controlplane/` route's
curator, and is deliberately left open here.

### Fingerprints

**No fingerprint hash and no evidence path in the table above was hand-edited.** Five entities have
at least one changed evidence blob and their fingerprints are therefore stale — **External Memory
Ledger, Worktree Contract, Provider Degradation Protocol, Supervisor Sweep, Task Document**.
Closeout must recompute all five against the landed `HEAD`; they cannot be computed here, because
`git-blob-set-v1` resolves `HEAD:<path>` and this leaf's code is uncommitted. Verification metadata
is pinned until closeout stamps the commit. Note that the three "declaration outside the evidence
set" cases above will **not** appear as stale rows at closeout either now or ever, which is the
whole reason they are written out in prose.

## Cross-Layer Projections

### Onboarding Unit

| Layer              | Representation                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Repository source  | One concrete source file or repo-level entity set.                                                        |
| Onboarding storage | Mirrored Markdown file or repo-level `entities.md` under the resolved onboarding root.                    |
| Drift detection    | File metadata, overview source routes, inline digests, or entity fingerprints compared deterministically. |
| Agent workflow     | Read alongside source; update through `c-05-create-or-update-onboarding-files` skill when durable state changes, using resolved domain docs as discovery input and live docs as authoritative when configured. |

### Runtime AGENTS Template Package

| Layer              | Representation                                                                                                                        |
| ------------------ | ------------------------------------------------------------------------------------------------------------------------------------- |
| Repository source  | Four templates under `mcp/src/agents_remember/package_data/runtime/agents-md-files/{coordinator,skills,system,tasks}/AGENTS.md`.                                           |
| Runtime install    | Intended destinations under the coordinator root, skills tree, system tree, and task tree.                                            |
| Onboarding storage | Four mirrored file-level onboarding units under `onboarding/mcp/src/agents_remember/package_data/runtime/agents-md-files/`.                                                |
| Agent workflow     | Agents read the installed templates at runtime; source changes to the templates are maintained as normal file-level onboarding units. |

### Coordination Context

| Layer            | Representation                                                                                                               |
| ---------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| Settings         | `system/settings.md` plus JSON-first `system/settings.json` when present.                                                    |
| Resolver code    | `CoordinationContext` dataclass and JSON/text output.                                                                        |
| Consumer skills  | `c-02-memory-quality-control` skill, `c-03-repo-bootstrap` skill, `c-05-create-or-update-onboarding-files` skill, and task workflows consume resolved roots instead of guessing, including the repo-specific task namespace. |
| Worktree support | Explicit memory, coordination, task, temp, worktree, contract, and ledger facts. `memory_mode` is copied from the in-scope contract and typed as that contract's `MemoryMode` alias, so the two cannot declare different sets. |

### Light Task Artifact

| Layer            | Representation                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------- |
| Planning         | JSON-primary `ar-task-document/v1` doc rendered to `task.md` (by the `task_doc` tool) under the `c-08-ar-coordination-context-resolver` skill resolved task root.                                    |
| Implementation   | Checkbox checklist is the live execution state.                                             |
| Onboarding       | Durable current-state findings may be propagated to onboarding through `c-05-create-or-update-onboarding-files` skill after approval. |
| Worktree support | Lives beside `contract.md` for worktree-backed tasks.                                       |

### Memory Baseline Adoption

| Layer              | Representation                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Developer decision | Current onboarding is either refreshed through `c-05-create-or-update-onboarding-files` skill or explicitly accepted despite drift.                 |
| `c-10-adopt-memory-baseline` skill service/CLI   | `baseline_status` reports drift and ledger state; `baseline_adopt` creates the baseline only when allowed, with the CLI commands as adapters. |
| `c-09-git-worktree-manager` skill mutation      | Bootstrap commits current memory content and writes the initial `memory.md`.                              |
| Future worktrees   | `c-09-git-worktree-manager` skill can use the ledger to decide whether external memory is compatible with a selected code base commit. |

### Worktree Contract

| Layer             | Representation                                                  |
| ----------------- | --------------------------------------------------------------- |
| Current repo      | Common parser/writer plus result-returning `c-09-git-worktree-manager` skill service functions. |
| Local coordinator | `ar-coordination/tasks/<repo-name>/<task-name>-ar/contract.md`. |
| Persisted vocabulary | Six `Literal` aliases declared once in `worktree_contract.py`; the reader degrades an unknown cell onto the declared default and quarantines the raw token in `unknown_cells`, the writer refuses it. A hand-edited file therefore loads degraded and heals on the next rewrite; nothing in the package can create that state. |
| `c-08-ar-coordination-context-resolver` skill              | Facts-only contract reader; its `memory_mode` is the contract's own `MemoryMode` alias. |
| `c-09-git-worktree-manager` skill              | Creator/updater and lifecycle owner; every status-cell write goes through `ContractCells`/`amend_contract`. |
| Context packet    | `application.worktree_status.worktree_status_packet` constructs `WorktreeSummary` directly instead of returning a dict for the caller to validate, and omits `nextTool`/`nextArgs`/`nextRequiredArgs` when the producer omitted them rather than substituting `""`/`{}`/`[]`. |
| Closeout quality gate | Mandatory repository wrapper after preview/approval and before every code, memory, ledger, contract, or applied-gate **commit**. Where the wrapper is present the gate first refuses a code checkout that is not a linked worktree and one with unresolved merge conflicts, then resets the index and stages the whole task worktree so the gate's scope is the commit's content — created files included, not only edited ones. A refusal leaves the worktree staged and commits nothing; the next attempt resets and restages, so it reaches the index a first run would. A checkout carrying no wrapper runs no gate, stages nothing early, and previews as `wrapper-unavailable`. |

### Worktree Integration

| Layer              | Representation                                                               |
| ------------------ | ---------------------------------------------------------------------------- |
| Closeout snapshot  | Reviewed code, memory content, and ledger commits recorded in `closeout`.    |
| Integration replay | Optional code rebase and memory-content replay when source branches moved.   |
| Source branches    | Fast-forward only after integrated code and memory ledger commits are ready. |
| Cleanup            | Asked after success; not automatic. Carryover-guarded (05m): refuses until the parked memory is carried home, then retires the work + (PR'd) source branches. |
| Phase reporting    | `worktrees/modules/guidance.py` declares `WorktreePhase`/`NextOperation`/`NextTool` and is the sole producer that reaches `WorktreeSummary`; `carryover-pending`, `abandoned`, `request_carryover_decision` and `memory_carryover_apply` are members it always emitted and the packet used to reject. Gate and block payloads use the separate `recovery_guidance` builder — same keys, same order, its own `RecoveryOperation`/`RecoveryTool` vocabulary — so `commit-approval-pending`/`request_commit_approval` are no longer values the packet's phase machine claims it can produce. |

### Provider Degradation Protocol

| Layer              | Representation                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Detection          | State machine over `providers/metrics.py`'s central metrics log; hysteresis-gated healthy/degraded/critical. |
| Durable record      | `ar-provider-degradation-state/v1` + append-only `ar-provider-degradation-event/v1` under `logs/observer/providers/`. |
| Response            | Role-addressed `degradation-alert` inbox rows (orchestrator + active managers) and the critical-threshold failsafe stop. |
| Investigation seat  | `system-specialist` role: reports first, fixes only on explicit orchestrator order.                        |
| Future detection    | Sentry (260703_spotlight-dev-observability) is designed to replace/feed detection without changing this response protocol. |

### Seat Binding Identity

| Layer              | Representation |
| ------------------ | -------------- |
| Catalog storage    | `TerminalCatalogEntry.leaf_key` plus persisted `seat_role`; `spawn_role` remains immutable origin provenance and `binding_leaf_key` falls back to `replacement_for_leaf` for an unbound failed dispatch. |
| Spawn              | Settings-resolved `AR_SPAWN_ROLE` derives the first binding role; live arbitration refuses only a same-pair owner and replaces a dead holder. |
| Attach/API         | MCP and HTTP accept role with canonical leaf key; explicit choice types hand-opened sessions, otherwise provenance/current binding may default, and an untyped harness returns `role-required`. |
| Control plane      | Retire authority, chain credit, expectations, inbox rows, supervisor findings/cooldowns/coalescing, landing, and provider discovery consume binding identity. |
| Dashboard          | Session data carries `seatRole`; authoritative open materializes `leafKey`/`seatRole` from the accepted server row only, with no row on failure; attach/move requires a role choice; grouping, chips, ordering, manager collapse, and pane identity are binding-first. |

### Seat Retirement

| Layer              | Representation                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Catalog storage    | `TerminalCatalogEntry.status == "terminated"` plus `retired_at`/`retired_by_session`/`retired_reason`/`retired_edge`, written only when set (migration-safe). |
| Authority policy   | `retire_policy.check_retire_authority(SeatRef, SeatRef)` over current binding leaf/role — owner-never-self-retires, manager-scoped-to-own-master worker/reviewer/curator seats, orchestrator-portfolio-wide; an unbound failed dispatch resolves through replacement leaf. |
| Manual surface     | `session_retire` MCP tool + `POST /api/terminal/{session}/retire` — both actor-declared, both policy-checked before mutation. Since L4 the tool's four results are built by one `_retire_payload` typed on `SessionRetireStatus`, and the route declares `TerminalRetired \| TerminalAlreadyRetired` with `403 TerminalRetireRefused` (the only 403 on the whole serving surface) and `404 UnknownSessionRefusal \| UnknownActorRefusal`. The route declaration is the contract, not the check: the handler returns a `Response`, so FastAPI validates nothing — `mcp/tests/test_serving_response_conformance.py` drives the real route and validates the body that came back. |
| Explicit cleanup   | `POST /api/terminal/landed-cleanup` converts selected landed archive rows to retired rows after a backend status re-check; since L4 it declares `TerminalCleanupResult`, under the same declaration-is-not-enforcement caveat. |
| Doctrine           | `roles/manager.md`/`roles/orchestrator.md` document the authority split for agents calling `session_retire` by hand. |
| Composition        | Rides the pre-existing L5 liveness-hysteresis terminal invariant (`with_liveness_success` never revives `terminated`) rather than using the landed archive state. |

### Seat Landing Archive

| Layer              | Representation                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Catalog storage    | `TerminalCatalogEntry.status == "landed"` plus `landed_at`/`landed_reason`/`landed_edge`, preserving the tmux session for inspection. |
| Completion surface | `worktree_integrate` (worker/reviewer at the leaf edge) and `lifecycle_finalize_task` (manager/reviewer at the master edge) call `_auto_land_completed_seats`, config-gated by `autoLandOnIntegration`/`autoLandOnFinalize`, and return `autoLandedSeats`. |
| Liveness surface   | `TerminalCatalogLivenessSweeper.refresh()` returns landed rows but skips background tmux probe/capture/classification/catalog writes for them; attach checks on demand. |
| Dashboard surface  | `railModel.ts`/`SessionRail.tsx` group landed rows into completed folders; `PtySurface.tsx` keeps landed terminals read-only; `sessionLifecycle.ts`/`LandedCleanupNotice.tsx` retain backend-confirmed cleanup outcomes and unavailable-result retry targets. |
| Cleanup            | The landed archive cleanup endpoint retires only rows still `landed` after re-read and reports closed/skipped rows separately. Since 260731-EFA-L4 that closed/skipped split is declared on the wire as `response_contract.TerminalCleanupResult` (with `TerminalCleanupSkip` rows), enforced by the response-conformance suite against the real route rather than by FastAPI, which never serializes this handler's `Response`. |

### Supervisor Sweep

| Layer              | Representation                                                                                            |
| ------------------ | --------------------------------------------------------------------------------------------------------- |
| Detection          | Seven R2 predicates evaluated every sweep directly over `TerminalCatalog`/`OperatorInboxStore`/`ExpectationRowStore`/the nudge store/signal cooldown store (never the projection) — findings preserve `(leafKey, seatRole)` so parallel roles remain distinct, and hosted-delivery failures below persistent retry exhaustion are filtered before generic ladder due-time evaluation. |
| Durable record      | `orchestration.supervisor.redeliver`/`.escalate`/`.signal`/`.respawn`/`.dead-upstream` observer events plus the dedicated `orchestration.escalation.rung` event (and the reused `orchestration.nudge` kind) under `logs/observer/`; the sweep's own tick row under `logs/observer/workspace/supervisor-heartbeat.json`; the signal cooldown log under `logs/observer/workspace/supervisor-signals.jsonl`; the ladder's own `rung`/re-anchored `escalatedAt` fields on the `OperatorInboxEntry` row itself. |
| Response            | Redeliver via `deliver_inbox_entry` on the injected sweep clock, auto-nudge, signal-emit, or escalate one rung. Condition coalescing and cooldown identity include leaf plus seat role; current routing uses binding identity while historical ladder parentage uses spawn provenance. |
| Self-liveness       | `SupervisorHeartbeatStore` ticks unconditionally at the end of every sweep; surfaced as an MCP-tool banner and a dashboard header badge, silent when never-ticked. Since L4 both surfaces are declared: the banner is a `supervisorBanner` field of the two response envelopes (set before the one `model_dump`, so it is inside the advertised `tokens`), and the badge reads a `SupervisorHeartbeatPayload` declared on `ServedWorkspaceProjection` and dumped without `exclude_none`, so "never ticked" stays an explicit null rather than an absent key. |
| Settings            | `orchestration.supervisor` family in `kernel/agentic_settings.py` (enabled/interval/staleness cutoff/redeliver rate limit/signal cooldown/redeliver budget) plus `orchestration.escalation` (per-kind SLA/per-rung dwell/renudge rate limit/respawn-after-rung, HFX2-L4), both re-read per-use. |

### Task Document

| Layer              | Representation |
| ------------------ | -------------- |
| Durable source     | JSON-primary `ar-task-document/v1` under `coordination_root/tasks`; rendered Markdown and enclosure contracts are not content authority. |
| Always-on backend  | At most 250 `TaskDocNode` summaries plus compatibility series summaries, body fields empty, `bodyRevision` populated. |
| On-demand backend  | `GET /api/task-document?path=...` returns one full, schema-validated task node only after the resolved path is confined under `tasks/`; since L4 the route declares `TaskDocNode` plus `404`/`503` `HttpDetailRefusal`, checked by the response-conformance suite rather than by FastAPI (the handler returns a `JSONResponse`, which FastAPI passes through unserialized). |
| Frontend           | `fetchTaskDocument` retrieves the selected body; `DetailPanel` merges it over the live summary with absent-array preservation, caches by `docPath + bodyRevision`, and visibly falls back to summary data when unavailable. Sub-task rows are the `SubTaskRow` union of the master and series shapes and render in the order received; only a series row carries `createdAt`, and the server has already ordered by it. |

### Delivery Injector

| Layer          | Representation                                                                                            |
| -------------- | --------------------------------------------------------------------------------------------------------- |
| Transport      | `terminal_paste.TerminalPaster.paste` — sanitized tmux input with one Enter re-press and one verified-absence clear/replace re-paste; pane text cannot grant acceptance. |
| Classification | `injector.deliver` retains the four-way outcome, but `acked` requires a unique-id user record or command+non-error-stdout evidence in the bound harness log. |
| Per-harness    | `harness_logs.HarnessSessionLog` parses real Claude/Codex record schemas; `HarnessAdapter` is failure-modal labeling only. |
| Callers        | Spawn (`mcp/tools/terminal.py`), durable inbox/supervisor (`inbox_delivery.py`), and REST paste (`serving/app.py`) all compose the same injector. |

### Harness Capability Snapshot

| Layer              | Representation |
| ------------------ | -------------- |
| Settings / role    | `orchestration.roles.<role>` and per-level overrides resolve into a complete `ResolvedLaunch`; namespaced spawn env is provenance only. |
| Launch boundary    | Settings-owned role selection and an optional complete daemon request pair both become `ResolvedLaunch` and use the shared opener. A live same-id process is immutable truth: exact/selectionless reopen returns it, changed launch identity conflicts, and only a dead row starts a fresh control generation. The runner then refuses owned-selector conflicts, validates the dynamic model/model-local effort catalog, and creates the configured runtime adapter. The additive codex-only `resume_thread_id` rides the same opener → `RunnerConfig` payload → factory seam into the sole `CodexAppServerSettings` site, failing closed before any spawn for non-codex or malformed values; the transient discoverer never receives it. |
| Native harness     | Launch uses Claude `--model`/`--effort`, Codex thread model/config effort, and Pi provider-qualified `--model`/`--thinking`. Same-session set uses Claude structured `/model`/`/effort` plus exact replay/terminal evidence; Codex fresh-turn overrides on the same thread; and Pi correlated mutation plus bounded state/catalog readback. Dynamic discovery and Claude/Pi set evidence require no model prompt; Codex applies queued settings on the next real turn. Claude's ephemeral discovery replaces supported inherited MCP selectors with one strict empty set, while its normal session launch preserves the installed MCP configuration. |
| Normalized adapter | `CapabilitySnapshot` retains provider/model identity, selected/effective state, and model-local effort options; `LaunchKnobs` declares native launch material and exclusively owned selectors; `SetResult` separates requested/effective values and carries only the five evidence states. The Harness Submission Authority timeline serializes set with prompt submission, rejects dishonest result combinations, makes request ids idempotent, and reconciles retained known outcomes without native resend; adapters dispatch now and own no second queue. The L2E structural sub-protocols extend the same honesty: interrupt and asset-submit capability is detected structurally, never inferred from the harness id, and a harness without the seam fails closed typed with the adapter named. |
| ACP Sense 1 view   | Derived `SessionConfigOption` select rows use `model` and `thought_level`; unknown current values are omitted rather than fabricated. |
| Orchestration moat | Settings-owned role and per-level selection still create the session; the durable inbox/brief bus remains the assignment and inter-agent messaging root. Capability setters configure that owned session and never replace either boundary. |
| Daemon API         | Since L4 each of the four capability routes declares its success shape (`HarnessCapabilityEnvelope`, `CapabilitySnapshotWire`, `SetResultWire`) and its refusal shapes, the three session-scoped ones through the shared `SESSION_CONTROL_RESPONSES` table; the declaration is the contract and `test_serving_response_conformance.py` is the enforcement, because these handlers return `JSONResponse` and FastAPI never serializes it. Pre-session advertise returns `ar-harness-capabilities/v1` around the unchanged normalized snapshot; explicit refresh owns auth/account invalidation. Live advertise/set and whole-message submit/reconcile address the exact running control endpoint. Public responses retain normalized acceptance/correlation but strip private raw evidence; first-byte ambiguity and duplicate request ids never cause blind resend. |

### Harness Submission Authority

| Layer | Representation |
| --- | --- |
| Browser composition | Shared CodeMirror composer plus source/draft revisions; one immutable epoch/id/text request and no PTY-paste fallback. |
| Browser evidence | `submitMachine` central partial order; `submitClient` certified-retry/ambiguity boundary; `submissionLifecycleClient` raw-free polling, authoritative withdraw, and revision-CAS recovery. |
| Daemon boundary | Epoch/source/id validation, cockpit-only authority/status/withdraw routes, 64-id status batches, 409 conflict/mismatch, exact retry-safe 503, private IPC. The additive `submission-provenance` action discloses exact per-id source/state/timestamps/vendor-correlation (1..64 unique ids, epoch-checked, honest not-found) to the exact-session daemon peer over the same private socket, delegated bridge → queue → authority as the sole path. The L2E additive `operation-timeline` read follows the same delegation (paged, never bodies, epoch-checked end to end), the additive `interrupt` write crosses the same socket epoch-guarded with a bridge-stamped epoch, and the additive `assets` submit key admits only schema-validated, spool-confined, sha256-verified references. Since L4 every one of these routes declares its success and refusal bodies as strict `extra="forbid"` wire models (`serving/response_contract.py`, and `serving/conversation/response_contract.py` for the conversation half); because the handlers answer with `Response` objects, FastAPI validates none of it and `test_serving_response_conformance.py` carries the enforcement. |
| Server authority | One timeline for prompt/model/effort; atomic queued-withdraw versus dispatch; full operation refs; early terminal dominance; response bypass; 64/256 live-safe retention. L2E: the retained ledger enumerates in bounded never-bodies pages whose eviction floor is tracked at the sole pop site; the withdrawal recovery body is captured pre-tombstone at the one true transition; the idempotence digest extends over canonical asset identity only when assets ride. |
| Native adapters | Codex fresh-turn guarded write with bounded correlation; Claude sole accepted operation and shared lock; Pi fresh-state token guard and settled-plus-fresh-idle completion. No native queue is authority. |
| User recovery | Alt+Up requests exact withdrawal; unchanged drafts auto-restore by revision CAS, concurrent edits create one explicit recovery slot, and replace/keep-current/dismiss are local exact decisions. |

## Ownership Notes

- This catalog intentionally excludes the eight worktree task files as onboarding subjects.
- This catalog treats `mcp/src/agents_remember/package_data/runtime/agents-md-files/` as the package source for runtime `AGENTS.md` templates. Memory repos use `system/*` guidance files rather than root-level `AGENTS.md` files.
- Roadmap specs are cataloged only where they define active current design concepts that explain the repository's direction.
- Legacy roadmap specs remain historical context where they disagree with the implemented memory/coordination split.

## Update History

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
  compactor yet". `SupervisorSignalCooldownStore.compact` exists at the leaf's base commit
  cit:([`SupervisorSignalCooldownStore`], mcp/src/agents_remember/controlplane/supervisor_signals.py:68-215) and `serving/supervisor.py` calls it once per sweep cit:([`run_supervisor_sweep`], mcp/src/agents_remember/serving/supervisor.py:1195-1282), returning the folded snapshot every `in_cooldown` check
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
  history entry said "59 of 61 routes return a `Response`, which FastAPI never serializes" (wrong —
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
  capturer through `SupervisorContext`, so 2/8 of the leaf's P-15 fixture-zoo scenarios stay hybrid
  (predicate-unit classify + real downstream sweep response) rather than full end-to-end — recorded
  as a forward reference for the natural follow-up leaf (thread a capturer parameter through
  `SupervisorContext`/`evaluate_predicates`), in the same spirit as this entity's own
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
