# GrepAI Worktree Warm-Start Feasibility 01

**Task:** `task-provider-workflow-compatibility.md`
**Date:** 2026-05-27
**Scope:** Validate whether GrepAI can support worktree-local provider containers while preserving the broad all-memory provider shape and swapping only the active repo memory root.

---

## Verdict

The proposed GrepAI worktree mode is feasible, but the safe implementation shape is a full provider-instance database clone plus a scoped root swap, not a direct content rewrite of indexed rows.

GrepAI's workspace database schema is project-scoped and does not store workspace names. The workspace file defines the set of projects and paths, while the database rows are keyed by `project_id`. That means a workflow-local GrepAI instance can copy the main provider database, regenerate a worktree-local workspace config, keep unrelated memory projects unchanged, and point only the active repo project at the worktree-local memory root.

The target watcher must then reconcile the active project after startup. Directly rewriting `chunks.content` for path/base-URL text would make embeddings stale unless the affected chunks are re-embedded, so content/link changes should come from the worktree memory files and be refreshed by GrepAI's normal watcher/update path.

---

## Evidence

### Source Evidence

- GrepAI provider settings already support a list of memory roots with independent `projectId` values. `grepai_roots_from_provider_settings` normalizes each root independently, and `grepai_runtime_layout_from_provider_settings` mirrors each root under `<runtimeRoot>/index-roots/<projectId>`.
- Workspace config rendering writes one workspace with many projects, where each project has only `name` and `path`.
- Container paths are derived from the provider runtime mount. If worktree instances keep the same in-container mount path shape, `documents.path` and `chunks.file_path` can remain stable across provider instances.
- Current `prepare_grepai_workspace` syncs mirrored roots from their configured source roots, so a target worktree instance can use the normal source roots for unrelated projects and the worktree-local memory root for the active project.

### Live Read-Only Schema Evidence

Read-only inspection of the current GrepAI Postgres container showed only two public tables:

- `documents(path, project_id, hash, mod_time, chunk_ids)`
- `chunks(id, project_id, file_path, start_line, end_line, content, vector, hash, updated_at, content_hash)`

Primary/index keys:

- `documents_pkey` on `(project_id, path)`
- `chunks_pkey` on `(project_id, id)`
- secondary indexes on `chunks(project_id)`, `chunks(project_id, file_path)`, and `chunks(content_hash)`

There is no workspace table and no foreign key across projects. The full schema dump includes `CREATE EXTENSION IF NOT EXISTS vector`, so a full dump/restore can carry schema and pgvector requirements into a fresh target Postgres instance.

The current live database happened to have zero indexed rows, so it proved the schema shape but not row-copy behavior with real data.

### CLI/Runtime Evidence

`grepai workspace show agents-remember-memory` reports one workspace with eight projects, all as project name plus in-container path. `grepai watch --help` states that startup performs an initial scan, skips unchanged files by comparing modification times, indexes modified and new files, and handles file events.

The current mirrored roots contain provider-generated `.grepai` artifacts such as `config.yaml` and `symbols.gob`. These are provider-owned cache artifacts and should not be treated as durable memory content.

---

## Safe Implementation Shape

1. Create or reuse the worktree-local GrepAI provider instance with its own Postgres, watcher, runtime root, logs, workspace name, network, and containers.
2. Generate target GrepAI provider settings with the full memory root list from the source workspace.
3. Replace only the active repo root:
   - external memory: use `contract.memory_worktree`
   - internal/local memory: use the memory root inside `contract.code_worktree`
4. Keep every unrelated memory repo root unchanged.
5. Preserve project ids and in-container project path shape: `/grepai/runtime/index-roots/<projectId>`.
6. Copy the source provider Postgres database into the target provider database with a consistent Postgres snapshot, preferably `pg_dump --single-transaction` and `pg_restore`/`psql` into the fresh target DB.
7. Sync target mirror roots from their configured source roots. This swaps the active project files to the worktree-local memory root while leaving unrelated projects sourced from normal memory roots.
8. Remove or ignore provider-generated `.grepai` artifacts in target mirrored roots where needed; let the target provider regenerate cache artifacts.
9. Start the target watcher and wait for reconciliation before reporting the worktree provider as ready.
10. Verify that queries against the target provider return the workflow-local workspace/provider instance and that active-project results come from the worktree-local memory content.

---

## Rewrite Rules

Path column rewrites:

- Usually unnecessary if project ids and in-container project paths are preserved.
- Required only if the target changes `project_id`, `runtimeMount`, or `index-roots/<projectId>` shape.
- If required, rewrite only `documents.path` and `chunks.file_path` for the active project id.

Content/link/base-URL rewrites:

- Do not directly rewrite `chunks.content` unless the affected chunks are re-embedded.
- Prefer changing the worktree memory files and allowing watcher reconciliation to update `chunks.content`, hashes, vectors, and document metadata.
- Any explicit file-content rewrite must be scoped to the active repo memory root and followed by reindex/reconciliation.

Unrelated projects:

- Do not rewrite unrelated memory roots, project ids, paths, content, or links.
- They are carried over by the copied DB and normal root sync, then only reconciled if their source memory files differ from the copied snapshot.

---

## Constraints And Risks

- The source provider database and mirror roots may change while being copied. A Postgres snapshot makes the DB copy consistent, but target startup must still reconcile against the current filesystem roots.
- The target provider must not be considered ready until watcher reconciliation has completed or a bounded health check proves the active project is searchable.
- The current live DB had no indexed rows, so an integration test with a small indexed fixture is still required before claiming end-to-end behavior.
- Current MCP settings rendering only derives external memory roots from configured repositories. Worktree-local/internal memory root selection must be added at provider-settings generation time.

---

## Implementation Consequences

- Prefer full DB clone for GrepAI warm-start because it preserves the all-memory index shape and avoids per-table/project copy edge cases.
- Add a target settings builder that can replace exactly one GrepAI root by `projectId`.
- Add a GrepAI warm-start module that can:
  - discover source and target provider settings
  - verify source and target provider ownership
  - dump/restore the source Postgres DB into the target instance
  - sync target roots with the active repo root override
  - start/wait for the target watcher reconciliation
- Add tests for:
  - external-memory worktree root override
  - internal/local memory root override
  - unrelated roots preserved
  - DB path rewrite skipped when container paths are stable
  - content rewrite avoided without re-embedding
