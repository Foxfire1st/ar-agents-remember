# Provider Workflow Compatibility Audit 01

**Task:** `task-provider-workflow-compatibility.md`
**Date:** 2026-05-27
**Scope:** S1 current-state audit for provider identity, storage, warm-start/copy paths, worktree integration, and benchmark integration.

---

## Summary

GrepAI does persist copyable state, but Agents Remember does not currently expose a GrepAI seed/export/import path equivalent to CodeGraphContext.

The current GrepAI warm-start candidate is feasible in principle because the semantic index is stored in PostgreSQL tables and the indexed files are mirrored into provider-owned runtime roots. The implementation should copy or restore the relevant Postgres data plus mirrored roots into a workflow-local provider instance. There is no discovered GrepAI CLI command for exporting/importing a project bundle, so this needs Agents Remember-owned copy logic.

CodeGraphContext already has a deliberate seed path: source backend start, `cgc export`, bundle path rewrite, and target `cgc load --clear`. That path is present in code and has unit coverage for bundle rewriting, but it still needs MCP/integration validation with the namespaced provider runtime model.

The provider identity bug is broader than GrepAI. Both GrepAI and CGC still use global Compose project/network names. Worktree CGC already tries to create isolated backend data, but it remains attached to the global `agents-remember-cgc` project and `ar-cgc-code` network.

---

## GrepAI Storage Model

Current source and runtime evidence show these GrepAI state layers:

| Layer | Current location | Purpose | Copyability |
| --- | --- | --- | --- |
| Workspace config | `providers/runners/grepai/home/.grepai/workspace.yaml` | Defines workspace, projects, Postgres DSN, embedder endpoint, and project paths. | Copyable, but should usually be regenerated for the target provider instance. |
| Mirrored index roots | `providers/runners/grepai/index-roots/<projectId>/` | Provider-owned copy of memory roots, mounted into the watcher container at `/grepai/runtime/index-roots/<projectId>`. | Copyable. Current sync intentionally excludes `.git`, `.grepai`, and `__pycache__` from the source memory root. |
| Semantic DB | `providers/data/grepai/postgres/data` mounted to `/var/lib/postgresql/data` | PostgreSQL/pgvector storage used by GrepAI workspace backend. | Copyable through Postgres dump/restore or controlled table copy. Raw data-directory copy is only safe while Postgres is stopped. |
| Embedder model cache | `providers/data/grepai/ollama/data` mounted to `/root/.ollama` | Ollama model cache. | Copyable, but not workflow-specific. Prefer sharing by explicit cache policy or letting model pull/install handle it. |
| Symbol artifacts | `.grepai/symbols.gob`, `.grepai/config.yaml` inside mirrored roots | GrepAI-generated local symbol/index config artifacts. | Copyable if they are part of the target mirrored root, but source memory roots should not receive them. |

Observed GrepAI DB tables after a search initialized schema:

- `public.documents(path, project_id, hash, mod_time, chunk_ids)`
- `public.chunks(id, project_id, file_path, start_line, end_line, content, vector, hash, updated_at, content_hash)`

The path-bearing columns are `documents.path` and `chunks.file_path`. Current container workspace paths use `/grepai/runtime/index-roots/<projectId>`.

Implication: if every provider instance mounts its own runtime root at the same container path `/grepai/runtime`, and uses the same `projectId`, copied GrepAI rows may not need path rewriting inside the DB. If the internal container path or project id changes, the copy step must rewrite `documents.path`, `chunks.file_path`, and any path-bearing metadata discovered in later schema versions.

---

## GrepAI Copyability Answer

GrepAI data is copyable in principle, but not currently implemented as a safe Agents Remember workflow operation.

Required implementation shape:

1. Stop or quiesce the target GrepAI watcher before import.
2. Prepare the target provider instance and mirrored root.
3. Copy the source mirrored root into the target provider runtime, excluding source-only artifacts that should be regenerated.
4. Copy semantic DB rows for the selected `project_id` from source Postgres to target Postgres, or use a project-scoped dump/restore.
5. Rewrite DB path columns if the target container path or project id differs.
6. Regenerate target workspace config.
7. Start the target watcher and let it perform cheap incremental reconciliation for branch/commit changes.
8. Verify with a search/status query that target results point at the target provider instance.

Current gap: there is no discovered GrepAI CLI equivalent to CGC `export`/`load`, so this needs an Agents Remember-owned GrepAI seed/copy module.

---

## GrepAI Identity And Collision Evidence

Current source uses fixed Docker identifiers:

- Compose project: `agents-remember-grepai`
- Network: `ar-grepai-memory`
- Watcher: `ar-grepai-watcher`
- Postgres: `ar-grepai-postgres`
- Ollama: `ar-grepai-ollama`
- Workspace: `agents-remember-memory`

Live container inspection also showed an unsafe mixed state:

- `ar-grepai-watcher` mounted the main workspace runtime root under `/home/mohamedreadone/Projects/ar-coordination/providers/runners/grepai`.
- `ar-grepai-postgres` mounted a temp validation data root under `/tmp/ar-mcp-real-validate-02/ar-coordination/providers/data/grepai/postgres/data`.
- `ar-grepai-ollama` mounted a temp validation data root under `/tmp/ar-mcp-real-validate-02/ar-coordination/providers/data/grepai/ollama/data`.

That proves name-based ownership is insufficient. The lifecycle must verify labels and mounts before treating a container as owned by the active MCP config.

---

## CodeGraphContext Current State

CGC has a more mature warm-start design:

- `providers/cgc/seed.py` resolves source and target repo roots, checks commit equality unless mismatch is explicitly allowed, starts the source backend, exports a source bundle, rewrites paths, then loads the rewritten bundle into the target backend.
- `providers/cgc/bundle.py` rewrites JSON, JSONL, Markdown, and text files inside the bundle. Existing tests verify POSIX and Windows-style path replacement.
- Worktree start already passes source repo root and target worktree root into `CgcSeedOptions` and asks for an isolated CGC runtime root.

Remaining CGC problems:

- CGC still uses global Compose project `agents-remember-cgc`.
- CGC still uses global network `ar-cgc-code`.
- Normal CGC backend name is global: `ar-cgc-falkordb`.
- Watchers are per repo id, but not per provider instance. The same repo id in another workspace can collide.
- Worktree isolated backend containers can still attach to the global Compose project/network.
- Worktree contracts do not currently record provider instance metadata.
- Worktree cleanup removes code and memory worktrees, but does not stop/remove provider containers, networks, runtime data, or logs.

Live evidence showed a worktree backend container named `ar-cgc-falkordb-device-management-provider-runtime` mounted to a worktree provider runtime path, while still carrying Compose project label `agents-remember-cgc` and using the shared `ar-cgc-code` network.

---

## Benchmark Current State

Benchmark provider setup already creates benchmark-local MCP settings and provider settings, then calls provider setup.

Current behavior:

- Source-only/no-onboarding workspace has no Agents Remember memory/provider setup.
- With-memory workspace gets a benchmark-local `ar-coordination`, memory repo, skill exposure, and MCP registration.
- `benchmark_lifecycle_settings` modifies some backend container names for benchmark use.
- CGC seeding can use a source coordination root discovered from the benchmark root.

Remaining benchmark problems:

- Provider identity is still ad hoc, not a shared provider instance contract.
- GrepAI benchmark namespacing is incomplete.
- CGC benchmark namespacing is partial.
- Benchmark provider setup is not proven through MCP/integration tests.
- Per developer clarification, the target model should be one provider set for the Agents Remember-enabled benchmark side, not one provider set per run or per enabled variant.

---

## Design Consequences

The provider compatibility implementation should introduce one provider instance model and thread it through all provider settings.

Suggested scopes:

- `workspace`: default MCP coordination-root provider instance.
- `worktree`: provider instance stored in the worktree contract or linked state file.
- `benchmark`: one provider instance for the Agents Remember-enabled benchmark workspace.

Each instance must own:

- Docker Compose project name
- Docker network names
- container names
- runtime roots
- data roots
- log roots
- workspace names or graph names
- ownership labels

Status/start/stop/cleanup must check:

- `agents-remember.provider`
- `agents-remember.instance-id`
- `agents-remember.scope`
- `agents-remember.coordination-root`
- expected bind mounts
- expected Compose project/network labels

Mismatched resources should be reported as collisions or legacy resources, not reused or removed automatically.

---

## Proposed Implementation Slices

1. Provider identity module:
   - derive stable instance ids from coordination root, worktree contract, or benchmark workspace
   - sanitize ids for Docker names
   - generate labels and expected ownership predicates

2. Settings renderer update:
   - make GrepAI and CGC settings include instance id and scoped names
   - update tests that currently assert global names

3. Docker ownership checks:
   - add label/mount verification before status/start/stop/cleanup
   - preserve legacy/global detection as a non-destructive warning

4. CGC integration:
   - thread instance id through isolated/worktree/benchmark settings
   - keep export/rewrite/load seed path
   - add integration tests around path rewrite and target status

5. GrepAI seed/copy:
   - implement project-scoped copy from source provider to target provider
   - copy mirror root plus DB project rows
   - rewrite DB paths only when required
   - let watcher reconcile small branch/commit deltas after import

6. Worktree cleanup:
   - record provider instance facts
   - stop/remove only provider resources with matching ownership labels

7. Benchmark integration:
   - allocate one provider instance for the with-memory side
   - ensure no-onboarding side has no provider visibility
   - avoid per-run/per-variant provider instances

---

## Open Follow-Ups

- Confirm whether GrepAI DB schema can be copied project-by-project while the source watcher is running, or whether source Postgres needs a read-only transaction/snapshot.
- Decide whether GrepAI warm-start should copy `.grepai/symbols.gob` from the source mirrored root or allow the target watcher to regenerate symbol artifacts.
- Decide whether Ollama data should be shared by default, copied, or left to normal model setup.
- Add a dedicated integration fixture with a small GrepAI index so copy/restore can be tested without touching the developer's real provider state.
