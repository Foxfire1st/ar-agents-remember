# Task: Provider Workflow Compatibility For Worktrees And Benchmarks

**Status:** in-progress
**Parent Task:** `260527_pypi-mcp-install-docs-overhaul`
**Repo:** agents-remember-md
**Type:** Provider | Workflow | Tests | Config
**Created:** 2026-05-27T14:50+02:00
**Series Role:** follow-up 01, prerequisite for provider docs and full PyPI MCP workflow sign-off

---

## Objective

Make GrepAI and CodeGraphContext provider runtimes compatible with Agents Remember worktree and benchmark workflows.

The solution must prevent global Docker/runtime collisions, allow worktrees and benchmark workspaces to use independent provider instances, and preserve the intended fast path of copying or seeding existing provider data with rewritten source paths instead of forcing expensive full re-indexing.

---

## Request And Framing

### Surface Request

Create a new task in the PyPI MCP install/docs-overhaul folder dedicated to provider compatibility for worktree and benchmark workflows.

### Deeper Objective

Provider support should become trustworthy enough that the user manual can recommend worktrees and benchmarks without hidden caveats around shared containers, stale indexes, unsafe cleanup, or costly re-indexing.

### Highest-Leverage Framing

Treat providers as workflow-scoped runtime instances with explicit ownership and warm-start behavior:

- normal project providers belong to the configured MCP coordination root
- worktree providers belong to the worktree task/group
- benchmark providers belong to the benchmark workspace/case/run
- copied or seeded provider data must be rewritten to the target checkout paths before use
- cleanup must remove only the provider state owned by that workflow instance

---

## Requirements

- Add a provider instance identity model that can distinguish normal workspace, worktree, and benchmark provider runtimes.
- Namespace Docker container names, Compose project names, networks, workspaces, data roots, runtime roots, and logs by provider instance.
- Route operator-facing Agents Remember logs through a coordination-root log tree, with provider logs under `<coordination-root>/logs/providers/...`; keep provider runtime/data under `<coordination-root>/providers/...`.
- Persist provider setup summaries under `<coordination-root>/logs/providers/setup/` so a failed phase, final health state, and recovery state survive after the original command output scrolls away.
- Derive default provider instance names from human-readable workflow names: workspace folder name for normal providers, workspace folder plus worktree name for worktree providers, and workspace folder plus `benchmark` for benchmark providers. Avoid opaque hash-first ids in user-visible Docker resources; duplicate workspace names can use an explicit numbered `instanceId` such as `projects_2`.
- Stamp provider-owned Docker resources with ownership labels that include provider id, instance id, coordination root, and workflow scope where applicable.
- Make provider status/start/stop/cleanup verify ownership labels and key bind mounts before reporting a container as usable or mutating it.
- Detect legacy/global provider containers and report them as legacy or collisions; do not silently reuse or stop them from an unrelated MCP config.
- Preserve or implement the existing fast path for copying/seeding provider data into a workflow-local provider instance.
- Validate CodeGraphContext export/rewrite/load seeding for worktrees and benchmarks, including path and base URL rewrites from source repo root to target repo root.
- Implement GrepAI warm-start as a workflow-local provider database clone plus active-project memory-root swap, not as a CGC-style indexed-content rewrite.
- For worktree mode, both CodeGraphContext and GrepAI must run workflow-local provider containers independent from the main project provider containers.
- CodeGraphContext worktree mode is per code repo and must copy/seed the active repo graph from the main provider into the worktree provider, rewriting source repo paths to the code worktree path.
- GrepAI worktree mode remains one provider instance over the configured memory roots, but its copied worktree instance must swap only the active repo's memory root to the worktree-local memory root. Unrelated repo memory roots must not be rewritten as if they belong to the worktree task.
- GrepAI memory roots must support both external memory repositories and internal/local memory roots. For internal-memory worktrees, the active repo memory root must resolve inside the code worktree.
- GrepAI warm-start must clone the source GrepAI DB into the workflow-local provider, sync provider mirror roots, then let the target watcher reconcile the active repo project from the worktree-local memory files.
- GrepAI must not directly rewrite indexed `chunks.content` for links/base URLs unless the affected chunks are re-embedded. File-content/link changes belong in the worktree-local memory files and should reach the index through watcher reconciliation.
- Ensure worktree start records provider instance facts in the worktree contract or a linked provider state artifact.
- Ensure worktree cleanup stops/removes only worktree-owned provider containers, networks, runtime data, and logs after approval.
- Ensure benchmark prepare/run use benchmark-local provider settings and provider instances rather than global workspace containers.
- Ensure benchmark warm runs can reuse copied/seeded provider data with rewritten paths while the source-only/no-onboarding environment remains uncontaminated.
- Use one provider set for the Agents Remember-enabled side of a benchmark workspace. Do not create a fresh provider set per benchmark run or per enabled variant.
- Cover both GrepAI and CodeGraphContext with unit tests for identity/settings/ownership and integration tests that exercise MCP-level provider workflow behavior.
- Retest the parent PyPI MCP validation paths that were blocked by provider isolation: provider up/down, worktree provider cleanup, and benchmark provider setup.

---

## Developer Clarifications

- Provider data is expected to live somewhere durable. The task must first determine where GrepAI stores its indexed data, whether that data is copyable, and whether copied data can be safely rewritten for a new target checkout. If GrepAI data is not copyable, report that back before continuing with an implementation that assumes warm-start support.
- Providers use watchers to detect branch and commit changes. Normal incremental updates after branch/commit changes are expected to be small enough to be efficient.
- The expensive operation to avoid is a complete index rebuild from scratch, especially for a new worktree or a benchmark workspace.
- Benchmark provider scoping is not per case, per run, or per enabled variant. The no-onboarding benchmark side uses nothing from Agents Remember. The Agents Remember-enabled benchmark side uses one shared provider set across the enabled benchmark variants.
- Whether a benchmark case is run with providers turned on or off should not change the provider-compatibility architecture for this task.
- Worktree provider scoping is per worktree task/group for the active repository. The workflow-local provider instance is independent from the main project provider, but GrepAI's logical scope still spans memory roots rather than becoming a single-repo-only provider.
- In a GrepAI worktree warm-start, the copied provider data should preserve the large all-memory index shape and change only the active repo memory project/root to the worktree-local memory. The implementation should avoid direct indexed-content rewrites and rely on the target watcher to reconcile the active repo's changed files.

---

## Invariants And Non-Goals

- Do not trade correctness for cheaper indexing. Copied provider data is acceptable only when path/base URL rewrites are verified and stale source data is detected or surfaced.
- Do not let one MCP settings file mutate provider containers owned by another settings file or coordination root.
- Do not remove existing legacy/global containers automatically during migration.
- Do not make docs claim providers are worktree-safe or benchmark-safe until the MCP-level validation passes.
- Do not solve every provider performance problem in this task; the scope is workflow compatibility, isolation, safe cleanup, and validated warm-start behavior.
- Do not create provider instances per benchmark run or per Agents Remember-enabled variant.
- Do not collapse GrepAI worktree mode into a single-memory-repo index unless a later explicit decision changes that architecture.
- Do not rewrite unrelated memory repositories when preparing a GrepAI worktree provider instance.
- Do not use CGC-style bundle path rewriting for GrepAI indexed content; cloned GrepAI data must remain embedding-consistent or be refreshed by watcher reconciliation.

---

## Current Evidence

- Parent finding F-010 shows an isolated PyPI MCP provider status reused generic GrepAI containers and listed unrelated workspace projects.
- Parent finding F-003 shows worktree code/memory cleanup passed through MCP, but provider-runtime cleanup remains unvalidated because safe provider mutation is blocked.
- Parent finding F-004 shows true provider up/down through MCP is unsafe while provider Docker state is shared globally.
- GrepAI currently uses fixed Docker identities such as `ar-grepai-watcher`, `ar-grepai-postgres`, `ar-grepai-ollama`, and `agents-remember-grepai`.
- CodeGraphContext has per-repo watcher names but still shares backend/network identity across the workspace and can collide for the same repo id across different workspaces.
- Worktree provider start currently targets CodeGraphContext only, skips GrepAI, uses a worktree `provider-runtime` root, and calls CGC seed with source and target repo roots.
- CodeGraphContext bundle rewriting exists in source and rewrites JSON, JSONL, Markdown, and text path strings from source root to target root.
- Benchmark provider setup already generates benchmark-local settings and overrides some backend container names, but the naming/ownership model is incomplete and not proven by MCP-level integration tests.

---

## Evidence Plan

- Source evidence: inspect provider settings rendering, GrepAI lifecycle, CGC lifecycle, provider setup service, worktree start/cleanup, worktree contract, benchmark registration, and benchmark provider setup.
- Copy/seed evidence: prove whether CGC export/rewrite/load and GrepAI warm-start/copy preserve useful indexed data and rewrite all source-root path/base URL references.
- Docker evidence: verify actual container names, labels, networks, mounts, ports, volumes, and Compose projects for at least two simultaneous provider instances.
- MCP evidence: validate through MCP tool calls from isolated Codex sessions, not direct provider APIs, for workflow-level claims.
- Test evidence: add focused unit tests for namespace/ownership/settings generation and integration tests for provider setup/status/cleanup behavior.
- Regression evidence: rerun the parent validation scenarios that were blocked by provider isolation and update `findings.md` with retest results.

---

## Audit Artifacts

- [Provider Workflow Compatibility Audit 01](/home/mohamedreadone/Projects/ar-coordination/tasks/agents-remember-md/260527_pypi-mcp-install-docs-overhaul/provider-workflow-audit-01.md) records the first S1 audit. It confirms GrepAI persists copyable state in mirrored roots plus PostgreSQL/pgvector tables, but there is no existing GrepAI export/import seed path equivalent to CGC. Warm-start support therefore needs Agents Remember-owned copy/restore logic.
- [GrepAI Worktree Warm-Start Feasibility 01](/home/mohamedreadone/Projects/ar-coordination/tasks/agents-remember-md/260527_pypi-mcp-install-docs-overhaul/grepai-worktree-feasibility-01.md) confirms the proposed worktree shape is feasible if implemented as a full target provider database clone plus one active-project memory-root swap, followed by target watcher reconciliation.

---

## Implementation Notes

### 2026-05-27T15:19+02:00 - Provider Instance And Namespace Slice

Implemented the first source slice for provider instance identity and generated runtime names.

- Added a provider identity module for stable instance ids, Docker-safe scoped names, and ownership labels.
- Extended MCP provider config parsing so provider entries may specify `scope` and `instanceId`; default workspace providers now derive a human-readable instance id from the workspace folder name.
- Threaded instance ids through lifecycle settings for GrepAI and CodeGraphContext.
- Namespaced GrepAI workspace name, Compose project, network, watcher/postgres/ollama containers, runtime roots, log roots, and data roots by provider instance.
- Namespaced CodeGraphContext Compose project, network, backend/watcher containers, runtime roots, log roots, and data roots by provider instance.
- Added ownership labels to generated Compose services and networks.
- Updated benchmark MCP registration so provider-enabled benchmark workspaces use `scope: benchmark` and one benchmark-local provider set.
- Updated isolated worktree CGC setup so it derives its own human-readable provider instance from the workspace folder and worktree name instead of inheriting the parent workspace instance.
- Fixed an import-cycle regression exposed by provider setup tests by routing the new CGC constants import through the provider context facade.
- Fixed CGC single-repo watcher start migration so it uses the rendered Compose project name instead of the legacy global project.

Validation completed for this slice:

- `python -m pytest mcp/tests -q`: 213 passed, 2 skipped, 12 subtests passed.
- `python -m agents_remember.code_quality.check`: passed. Ruff passed; pytest passed; CRAP threshold findings remain report-only and pre-existing outside this slice.

Remaining gaps after this slice:

- Docker status/start/stop/cleanup still need explicit ownership-label and bind-mount verification before mutating resources.
- Legacy/global provider collision reporting still needs to be promoted from mount/project checks into first-class status output.
- GrepAI warm-start copy/restore is confirmed feasible in principle but still unimplemented.
- Worktree contract/provider state still needs to persist provider instance facts for cleanup.
- Parent PyPI MCP provider mutation retests are still blocked until ownership verification and cleanup are implemented.

### 2026-05-27T16:46+02:00 - GrepAI Worktree Warm-Start Slice

Implemented the source-side plumbing for GrepAI worktree warm-start and wired it into worktree provider setup.

- Added isolated GrepAI settings generation for worktree providers. The generated target settings keep the full GrepAI memory-root list, replace only the active repo project root with the worktree-local memory root, and namespace workspace, watcher, Postgres, Ollama, network, logs, runtime, and data roots by the worktree provider instance.
- Added GrepAI database clone support using source and target Postgres containers with `pg_dump --single-transaction` and `psql` restore. Dry-runs plan the clone without requiring Docker to be installed.
- Changed provider setup to write one combined isolated provider settings file when a workflow prepares both CGC and GrepAI. Lifecycle install/refresh/watchers now receive that workflow-local settings file.
- Changed provider setup ordering so GrepAI install prepares the target provider, then the DB clone runs, then refresh starts watcher reconciliation against the worktree-local roots.
- Ensured lifecycle operations receive the explicit generated provider settings file outside the isolated-worktree case too, so generated worktree/benchmark settings do not fall back to `system/settings.json`.
- Changed worktree start so it no longer hard-skips GrepAI. External-memory worktrees pass `contract.memory_worktree`; internal-memory worktrees pass `contract.code_worktree / "ar-memory"`.
- Threaded GrepAI seed options into benchmark provider setup so the benchmark-local provider can warm-start from the source provider instead of rebuilding from scratch.
- Added a linked `provider-runtime/provider-state.json` artifact for non-dry-run worktree starts so provider instance facts are available for later cleanup work.
- Changed MCP repository config parsing to prefer an existing repo-local `ar-memory` root before defaulting to external `ar-coordination/memory-repos/ar-<repo>`.
- Added focused tests for isolated GrepAI root swapping, dry-run GrepAI DB-clone planning, internal-memory root selection, worktree provider setup passing the GrepAI worktree memory root, and benchmark GrepAI seed option plumbing.

Validation completed for this slice:

- `python -m pytest mcp/tests/test_provider_setup.py mcp/tests/test_config.py mcp/tests/test_worktree_support.py -q`: 96 passed, 6 subtests passed.
- `python -m agents_remember.code_quality.check`: passed. Ruff passed; pytest passed with 218 passed and 2 skipped; CRAP threshold remains report-only with pre-existing findings.

Remaining gaps after this slice:

- Real Docker-level GrepAI clone/restore still needs an MCP-level integration validation with non-empty indexed data.
- Worktree cleanup still needs to stop/remove only worktree-owned provider containers, networks, runtime data, and logs.
- Provider lifecycle mutation still needs explicit ownership-label verification before status/start/stop/cleanup can be treated as fully safe.
- Benchmark provider warm-start is now wired to the GrepAI clone path, but still needs Docker/MCP-level validation with real provider data and proof of the one-provider-set rule for the Agents Remember-enabled side.

### 2026-05-27T17:55+02:00 - Worktree And Benchmark Integration Slice

Added and passed a Docker-backed integration test for workflow-local providers.

- Added a skip-gated real integration test that creates a source fixture, starts source providers, starts a worktree through `worktree_start_tool`, prepares benchmark providers through the benchmark registration path, checks watcher status for both providers, and cleans up the generated provider containers/networks.
- Fixed CGC doctor containment so worktree-local provider runtimes under `worktrees/.../provider-runtime` are accepted when they remain under the coordination tree and outside the source checkout.
- Fixed GrepAI DB clone by removing the unsupported `pg_dump --single-transaction` option used against the packaged Postgres/pgvector image.
- Fixed CGC seed bundle placement by writing source and target bundles under the respective CGC runtime roots so the runner containers can see them.
- Changed CGC seed load to use non-interactive `bundle import` for fresh workflow-local target providers instead of the `load --clear` shortcut/prompt path.
- Fixed benchmark GrepAI warm-start so it can clone into generated benchmark provider settings, not only isolated worktree settings.
- Added unit coverage for workflow-local CGC runtime containment, CGC seed bundle paths, GrepAI clone command arguments, and non-isolated benchmark-style GrepAI clone target settings.
- Recorded the integration-discovered defects as F-017 through F-020 in the parent findings file.

Validation completed for this slice:

- `python -m pytest mcp/tests/test_provider_lifecycle.py mcp/tests/test_provider_workflow_integration.py -q`: 29 passed, 1 skipped.
- `python -m pytest mcp/tests/test_provider_setup.py -q`: 11 passed.
- `AGENTS_REMEMBER_PROVIDER_INTEGRATION=1 AGENTS_REMEMBER_PROVIDER_INTEGRATION_TIMEOUT=1800 python -m pytest mcp/tests/test_provider_workflow_integration.py -q -s`: 1 passed in 200.72s.
- `python -m agents_remember.code_quality.check`: passed. Ruff passed; pytest passed with 222 passed and 3 skipped; CRAP threshold remains report-only with pre-existing findings.

Remaining gaps after this slice:

- Worktree provider cleanup still needs product workflow coverage, not only integration-test cleanup.
- Provider lifecycle mutation still needs explicit ownership-label verification before generic stop/cleanup operations are considered fully safe.
- Parent PyPI MCP validation still needs to be rerun from an installed package after these source changes are packaged/available.

### 2026-05-27T18:35+02:00 - Human-Readable Provider Instance Names

Adjusted the provider instance identity contract so Docker-facing names are readable to a user inspecting containers.

- Changed default workspace provider ids from opaque hash-first values to the workspace folder slug, for example `projects`.
- Changed worktree provider ids to combine the workspace folder and worktree task/group name, for example `projects-provider-task`.
- Changed benchmark provider ids to combine the benchmark workspace folder and `benchmark`, for example `with-memory-benchmark`.
- Fixed benchmark MCP registration so generated settings write the benchmark provider `instanceId` explicitly from the benchmark workspace root; otherwise the loaded config could derive `repos-benchmark` from the source repository parent.
- Kept explicit `instanceId` support for duplicate workspace names, so a second same-named workspace can use a readable numbered id such as `projects_2` instead of an opaque hash.

Validation completed for this slice:

- `python -m pytest mcp/tests/test_config.py mcp/tests/test_provider_setup.py mcp/tests/test_worktree_support.py::BenchmarkRunnerPortabilityTests::test_benchmark_provider_settings_are_generated_without_system_settings mcp/tests/test_worktree_support.py::BenchmarkRunnerPortabilityTests::test_benchmark_prepare_writes_workspace_mcp_registration -q`: 29 passed.

### 2026-05-28T11:24+02:00 - Central Logs And Provider Setup Reporting Slice

Implemented the central log-tree and setup-reporting slice.

- Changed generated MCP transcript defaults from `providers/logs/mcp` to `logs/mcp`.
- Changed generated provider log defaults from `providers/logs/<provider>/<instance>` to `logs/providers/<provider>/<instance>` for workspace, worktree, and benchmark provider settings.
- Removed `providers/logs/...` fallback scaffolding; runtime install and benchmark setup now create only the central `logs/...` operator-log tree.
- Added `logs/providers/setup/` scaffolding during runtime and benchmark workspace setup.
- Added compact provider setup summaries under `logs/providers/setup/last-<action>.json` and timestamped `<timestamp>-<action>.json`.
- Added setup payload fields for `ready`, `state`, `failedPhases`, `finalStatus`, `resultCounts`, and `setupSummary` while keeping top-level `ok` strict.
- Added reporting coverage for the recovered case where a setup phase fails but final watcher status is healthy (`state: ready-with-failed-phases`).
- Updated default coordinator notes so operator logs are described as `logs/` state while durable provider DBs remain under `providers/data/`.

Validation completed for this slice:

- `python -m pytest mcp/tests/test_install_runtime.py mcp/tests/test_context_providers.py mcp/tests/test_config.py mcp/tests/test_provider_setup.py -q`: 63 passed.
- `python -m agents_remember.code_quality.check`: passed. Ruff passed; pytest passed with 227 passed and 3 skipped; CRAP threshold remains report-only with pre-existing findings.

---

## Implementation Steps

### S1 - Current-State Audit

- [x] Map current provider identity sources for GrepAI and CodeGraphContext.
- [x] Map current copy/seed/warm-start code paths for CGC and GrepAI.
- [x] Determine where GrepAI persists indexed data and whether that data can be copied safely for worktree and benchmark warm-starts.
- [x] Map benchmark provider setup and how it differs from normal MCP provider setup.
- [x] Record any missing implementation pieces in the parent `findings.md` or this task's notes before fixing.

### S2 - Provider Instance Model

- [x] Design the provider instance id contract for normal workspace, worktree, and benchmark scopes.
- [x] Thread provider instance id through MCP runtime config, lifecycle settings, provider setup, worktree start, and benchmark setup.
- [ ] Add ownership labels and mount verification rules for provider-owned Docker resources.
- [ ] Add legacy/global collision reporting without destructive migration.

### S3 - Namespaced Provider Runtime

- [x] Namespace GrepAI container names, network, Compose project, workspace name, data roots, runtime roots, logs, and ports.
- [x] Namespace CodeGraphContext backend, watcher containers, network, runtime roots, logs, and ports.
- [x] Move generated provider log defaults from `providers/logs/...` to `logs/providers/...` without adding legacy `providers/logs/...` fallback scaffolding.
- [x] Write compact provider setup attempt summaries to `logs/providers/setup/`, including failed phases, final watcher status, and recovered/ready state.
- [ ] Make status/start/stop/cleanup refuse to mutate mismatched provider instances.
- [x] Add unit tests for two isolated MCP configs proving distinct provider identities.

### S4 - Copy, Seed, And Rewrite

- [x] Validate CGC source export, bundle rewrite, and target load for worktree and benchmark targets.
- [ ] Assert rewritten CGC data contains target repo paths and no stale source repo paths after load.
- [x] Investigate GrepAI warm-start/copy feasibility and document the accepted clone-plus-reconcile model.
- [x] Implement GrepAI source DB clone into a fresh workflow-local target provider DB.
- [x] Implement GrepAI active-project root swap in generated target settings while preserving unrelated memory roots.
- [ ] Add tests for CGC path/base URL rewrite coverage, including POSIX and Windows-style paths where relevant.
- [ ] Add tests proving GrepAI does not directly rewrite indexed `chunks.content` without re-embedding and instead reconciles active-project file changes through the target watcher.
- [ ] Define stale-source detection behavior when copied provider data does not match the source commit expected by the target workflow.

### S5 - Worktree Workflow Integration

- [x] Store provider instance metadata in the worktree contract or a linked provider state file.
- [x] Make worktree start prepare isolated providers through MCP-derived settings.
- [x] Make worktree start copy/seed provider data from the source provider when safe, instead of re-indexing from scratch.
- [x] Make worktree CGC setup use export/rewrite/load from the main code repo graph into the worktree-local CGC provider.
- [x] Make worktree GrepAI setup clone the source provider DB, copy/sync target mirror roots, and replace only the active repo memory root with the worktree-local memory root while preserving the rest of the copied all-memory provider scope.
- [ ] Validate worktree GrepAI behavior for both external memory worktrees and internal/local memory under the code worktree.
- [x] Make worktree status report the workflow-local provider instance, not global providers.
- [ ] Make worktree cleanup remove worktree-owned provider resources after approval and preserve shared/global resources.
- [ ] Add MCP-level integration tests for worktree provider start, use, closeout, integration, and cleanup.

### S6 - Benchmark Workflow Integration

- [x] Make benchmark prepare allocate benchmark-local provider instances for provider-enabled variants.
- [x] Make the Agents Remember-enabled benchmark side reuse one benchmark-local provider set with copied/seeded provider data and rewritten paths.
- [ ] Prove the no-onboarding/source-only benchmark side does not see memory/provider state.
- [ ] Make benchmark cleanup or reset remove only benchmark-owned provider resources.
- [x] Add MCP-level or harness-level benchmark integration tests that prove provider isolation and warm-start behavior.

### S7 - Retest And Handoff

- [ ] Rerun provider up/down validation from an isolated PyPI-installed MCP server.
- [ ] Rerun worktree provider lifecycle validation from the parent task.
- [ ] Rerun benchmark provider prepare/run validation.
- [x] Update parent `findings.md` with fix paths and retest results for provider-related findings.
- [ ] Mark which provider behavior is ready for the user manual and which behavior remains deferred.

---

## Proposed Code Examples

### E1 - Provider Instance Identity

Distinct change covered: provider resources must be scoped by workflow, not global WSL/Docker state.

```text
normal:    projects
worktree:  projects-260527-provider-compat
benchmark: with-memory-benchmark
```

### E2 - Ownership Verification

Distinct change covered: lifecycle operations must verify ownership before reporting or mutating resources.

```json
{
  "agents-remember.provider": "grepai-memory",
  "agents-remember.instance-id": "wt-260527-provider-compat",
  "agents-remember.scope": "worktree",
  "agents-remember.coordination-root": "/workspace/ar-coordination"
}
```

### E3 - Copy And Rewrite Acceptance

Distinct change covered: warm-started provider data must point at the target checkout.

```text
source repo root: /workspace/repos/project
target repo root: /workspace/worktrees/project-task

After seed/load:
- queries return /workspace/worktrees/project-task/...
- no indexed document still points at /workspace/repos/project/...
```

### E4 - Central Provider Logs

Distinct change covered: operator-facing logs and setup summaries belong in one coordination-root log tree.

```text
ar-coordination/
  logs/
    providers/
      setup/
        last-prepare.json
        20260528T084200Z-prepare.json
      grepai/
        projects/
          watcher.log
      codegraphcontext/
        projects/
          agents-remember-md/
            watch.log
  providers/
    data/
    runners/
    requirements/
```

---

## Resolved Questions

- GrepAI has copyable provider data, and Agents Remember now has a workflow-local DB clone path for worktree and benchmark warm-starts. The original missing capability is tracked and retested as parent finding F-016.
- GrepAI path-bearing database columns discovered so far are `documents.path` and `chunks.file_path`. If copied provider instances keep the same container mount path and project id, DB path rewrite may not be needed; if either changes, those columns need rewrite and later schema versions need the same audit.
- The all-memory GrepAI worktree shape is feasible because GrepAI's DB is project-scoped, not workspace-scoped. A target provider can clone the source DB, preserve project ids, regenerate target workspace config, and override only the active repo memory root.
- GrepAI content/link/base-URL rewrites should not be applied directly to `chunks.content` unless the affected chunks are re-embedded. Worktree-specific content should come from the worktree memory files and be reconciled by the target watcher.
- CGC and GrepAI use different warm-start strategies. CGC uses the existing export/rewrite/load seed path because graph paths can be safely rewritten. GrepAI uses a DB clone plus active-project mirror/root reconciliation because embeddings must stay aligned with indexed content.

## Open Questions

- What exact bounded readiness check should prove target watcher reconciliation has completed before worktree provider status reports ready?
- Should future deterministic provider tests add a synthetic Postgres schema fixture in addition to the current real Docker/Ollama integration pass?
- Should Ollama data be shared, copied, or left to normal model setup for workflow-local provider instances?

---

## Decision Log

| Date-Time | Decision | Rationale |
| --- | --- | --- |
| 2026-05-27T14:50+02:00 | Create the provider workflow compatibility task as follow-up 01 under the PyPI MCP docs-overhaul task. | Provider isolation and warm-start behavior are prerequisites for documenting worktree and benchmark provider workflows. |
| 2026-05-27T15:00+02:00 | Treat provider watchers as the normal mechanism for small branch/commit updates. | The expensive operation to avoid is a complete index rebuild for a new worktree or benchmark workspace, not ordinary incremental refresh after small changes. |
| 2026-05-27T15:00+02:00 | Use one provider set for the Agents Remember-enabled benchmark side, not one per case/run/variant. | The no-onboarding side uses no Agents Remember state; enabled benchmark variants should share the benchmark-local provider set rather than multiplying provider runtimes. |
| 2026-05-27T15:00+02:00 | Require a GrepAI storage/copyability audit before assuming warm-start support. | GrepAI is expected to persist data somewhere, but the task must prove where it lives and whether it can be copied and rewritten safely. |
| 2026-05-27T15:19+02:00 | Start with generated provider instance identity and namespaced runtime settings before mutating live Docker cleanup behavior. | Namespaced config and Compose output can be proven safely with tests first; live Docker mutation should wait for ownership verification and collision reporting. |
| 2026-05-27T15:45+02:00 | Worktree provider mode must create workflow-local containers for both CGC and GrepAI, while GrepAI remains an all-memory provider with only the active repo memory root swapped to the worktree-local memory root. | CGC is naturally per repo, but GrepAI's useful state is the large memory-wide index. Warm-start must avoid rebuilding that index while still routing the active task's memory to the worktree-local copy and avoiding rewrites to unrelated memory repos. |
| 2026-05-27T15:55+02:00 | Use CGC export/rewrite/load for CGC warm-starts and GrepAI DB clone plus active-project watcher reconciliation for GrepAI warm-starts. | CGC graph data can tolerate source-root path rewrites in its bundle. GrepAI embeddings must remain content-consistent, so direct indexed-content rewrites are unsafe unless followed by re-embedding. |
| 2026-05-28T10:55+02:00 | Centralize operator-facing Agents Remember logs under `logs/`, with provider logs and setup summaries under `logs/providers/...`. | Provider runtime/data belongs under `providers/`, but humans and agents need one coordination-root log tree for debugging setup failures, recovered states, watcher output, and MCP/user-facing troubleshooting. |

---

## References

- [Parent task](/home/mohamedreadone/Projects/ar-coordination/tasks/agents-remember-md/260527_pypi-mcp-install-docs-overhaul/task.md)
- [Parent findings](/home/mohamedreadone/Projects/ar-coordination/tasks/agents-remember-md/260527_pypi-mcp-install-docs-overhaul/findings.md)
- [Provider setup service](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/provider_setup.py)
- [CGC bundle path rewriting](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/cgc/bundle.py)
- [CGC seed rewrite/load path](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/providers/cgc/seed.py)
- [Worktree provider start](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/worktrees/modules/start.py)
- [Worktree cleanup](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/worktrees/modules/cleanup.py)
- [Benchmark MCP/provider registration](/home/mohamedreadone/Projects/agents-remember-md/mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py)
