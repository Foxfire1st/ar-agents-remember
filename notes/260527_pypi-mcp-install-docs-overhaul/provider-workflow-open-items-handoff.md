# Provider Workflow Compatibility Open Items Handoff

**Task:** `task-provider-workflow-compatibility.md`  
**Created:** 2026-05-27  
**Code repo:** `/home/mohamedreadone/Projects/agents-remember-md`  
**Current committed code slice:** `f20f75e Make providers workflow-scoped for worktrees and benchmarks`  
**Current memory commits:** `6ea6374 Update agents-remember provider workflow memory`, `2eedaa8 Record provider workflow compatibility closeout`

---

## Current State

The main provider workflow compatibility implementation is committed. It includes workflow-scoped provider identities, readable default instance ids, namespaced Docker/Compose resources, GrepAI worktree/benchmark warm-start through DB clone plus active-project root swap, CGC seed/export/rewrite/import support, worktree provider state output, and Docker-gated source/worktree/benchmark integration coverage.

The normal workspace provider reinstall retest was started after the commit using source-generated provider settings at:

```text
/home/mohamedreadone/Projects/ar-coordination/providers/settings/main-provider-settings.json
```

That live retest created readable `projects` provider resources:

```text
ar-grepai-postgres-projects
ar-grepai-ollama-projects
ar-grepai-watcher-projects
ar-cgc-falkordb-projects
ar-cgc-watcher-projects-<repoId>
agents-remember-cgc-projects
```

At the time this handoff was written, the live retest was still running. All CGC watcher containers were up, parallel indexing had completed for the smaller repositories, and one TensorFlow CGC index runner was still active. Do not mark F-021 through F-024 fully retested until that process finishes and targeted provider queries pass.

---

## Open Implementation Items

### 1. Worktree Provider Cleanup

`worktree_cleanup` still removes code worktrees, memory worktrees, merged task branches, and empty worktree directories only. It does not yet read the worktree provider state artifact and remove worktree-owned provider containers, networks, runtime data, or logs.

Needed behavior:

- Read `provider-runtime/provider-state.json` written during worktree start.
- Stop/remove only containers and networks whose ownership labels match the worktree provider instance and coordination root.
- Remove worktree-owned provider runtime/data/log roots after approval.
- Preserve normal workspace providers and unrelated workflow providers.
- Report skipped/mismatched resources instead of deleting them.

Primary files:

- `mcp/src/agents_remember/worktrees/modules/cleanup.py`
- `mcp/src/agents_remember/worktrees/modules/start.py`
- `mcp/src/agents_remember/providers/identity.py`
- provider lifecycle Docker/Compose helpers under `mcp/src/agents_remember/providers/lifecycle/`

### 2. Benchmark Provider Cleanup Or Reset

Benchmark prepare creates benchmark-local provider instances, but benchmark cleanup/reset does not yet remove benchmark-owned provider resources as a product workflow.

Needed behavior:

- Define where benchmark provider state is recorded.
- Remove benchmark-owned containers/networks/data/logs on benchmark reset/cleanup.
- Keep the no-onboarding/source-only workspace free of provider resources.
- Do not remove normal workspace providers or other benchmark provider sets.

Primary files:

- `mcp/src/agents_remember/benchmarks/runner_modules/workspace.py`
- `mcp/src/agents_remember/benchmarks/runner_modules/mcp_registration.py`
- provider lifecycle cleanup helpers to be added or shared with worktree cleanup.

### 3. Ownership Verification Before Mutation

Provider resources now receive ownership labels, and status checks verify important bind mounts in several places. The lifecycle still lacks one central rule that refuses mutation unless ownership labels match the configured provider id, instance id, scope, and coordination root.

Needed behavior:

- Add a shared Docker ownership verifier.
- Use it before destructive or replacing operations in provider lifecycle code.
- Treat mismatched labels as a collision, not as a container to repair automatically.
- Keep mount checks as an additional guard, not the only guard.

Affected behavior:

- GrepAI backend/embedder mismatch removal.
- CGC backend mismatch removal.
- Compose project migration helpers.
- Future provider cleanup operations.

### 4. Legacy/Global Collision Reporting

The system can avoid some old resources through new namespacing, but legacy/global containers and networks are not yet surfaced as first-class status/collision output.

Needed behavior:

- Detect legacy names such as `ar-grepai-watcher`, `ar-grepai-postgres`, `ar-cgc-falkordb`, and old hash-first names.
- Report them separately from the configured provider instance.
- Do not stop or remove them automatically.
- Include enough information for docs/troubleshooting to tell users what they are seeing.

### 5. Stale-Source Detection For Warm-Started Data

CGC and GrepAI warm-start can copy provider data, but the task still needs a clear stale-source policy.

Needed behavior:

- Record or compare the source commit/provider state used for the seed.
- Decide whether a mismatch blocks setup, warns, or forces refresh.
- Keep `--cgc-seed-allow-commit-mismatch` as an explicit escape hatch.
- Define GrepAI's equivalent behavior or document that watcher reconciliation is the freshness boundary.

---

## Open Test And Validation Items

### 1. Main Provider Reinstall Retest

Current status: in progress.

Remaining steps after the live process finishes:

- Confirm provider setup command exits successfully.
- Confirm no CGC runner commands replaced `ar-cgc-falkordb-projects`.
- Confirm all `ar-cgc-watcher-projects-*` containers remain running.
- Confirm GrepAI watcher/backend/embedder remain healthy.
- Run targeted CGC queries, for example `provider_instance_id` in `agents-remember-md` and a known symbol in `device-management`.
- Run targeted GrepAI searches against current memory.
- Update findings F-021, F-022, F-023, and F-024 from `fixed-awaiting-retest` to `retested` only after these pass.

### 2. PyPI-Installed MCP Retest

The source implementation passed source-level tests and Docker-gated integration, but the parent documentation task requires validation from an isolated PyPI-installed MCP server through real MCP tool calls.

Needed MCP retests:

- `provider_status`
- `provider_watchers(action="status", dry_run=false)`
- provider up/down or prepare using isolated settings
- worktree provider start/use/closeout/integrate/cleanup
- benchmark prepare/run with providers enabled

Relevant findings:

- F-003 worktree provider cleanup
- F-004 provider startup validation
- F-010 provider isolation

### 3. Worktree End-To-End MCP Workflow

The Docker-gated source integration starts a worktree and validates provider status, but the product workflow still needs a full MCP pass:

- start worktree with providers
- verify workflow-local CGC and GrepAI queries return useful data
- make a small code/memory change
- close out
- integrate
- cleanup
- verify cleanup removes worktree provider resources and preserves main providers

### 4. Benchmark End-To-End MCP/Harness Workflow

The source integration validates benchmark-local provider prepare/status, but remaining workflow validation should prove:

- one provider set is reused for the Agents Remember-enabled side
- no-onboarding/source-only side does not see memory/provider state
- benchmark-local provider data can be reset/cleaned safely
- provider-enabled benchmark variants do not create fresh providers per run/variant

### 5. CGC Rewrite Proof

Current tests prove bundle rewrite mechanics and Docker-level seed/import success. They do not yet query the loaded graph to prove all indexed paths point to the target repo and no stale source repo paths remain.

Needed tests:

- POSIX source to target path rewrite.
- Windows-style source to target path rewrite.
- Base URL/path-like text rewrite where applicable.
- Post-load query/assertion against target provider data.

### 6. GrepAI Reconciliation Proof

Current implementation intentionally does not rewrite `chunks.content`. A test should prove the accepted model:

- cloned GrepAI DB starts with source data
- target settings point only the active project to worktree-local memory
- target watcher reconciles active-project files
- active-project query results come from target memory content after reconciliation
- unrelated projects remain unchanged

### 7. Internal Memory Worktree Validation

Unit tests cover the internal-memory root selection path, but a real workflow test should prove worktree GrepAI uses:

```text
<code-worktree>/ar-memory
```

for internal-memory repositories.

---

## Documentation Readiness

Safe to document after current source commit:

- Provider names are workflow-scoped and readable by default.
- Normal workspace provider ids derive from the workspace folder name.
- Worktree provider ids combine workspace name and worktree/task name.
- Benchmark provider ids combine benchmark workspace name and `benchmark`.
- Explicit `instanceId` remains available for duplicate workspace names such as `projects_2`.
- Worktree and benchmark provider warm-start are implemented in source.
- CGC uses export/rewrite/import; GrepAI uses DB clone plus active-project watcher reconciliation.

Do not yet document as fully supported happy path:

- Worktree provider cleanup.
- Benchmark provider cleanup/reset.
- PyPI-installed MCP provider up/down as fully retested.
- Source-only benchmark provider isolation as proven.
- Stale-source behavior for copied provider data.
- Provider mutation safety against mislabeled/colliding resources.

---

## Recommended Next Pass

1. Let the current main provider reinstall retest finish.
2. Run targeted CGC and GrepAI queries against the `projects` provider instance.
3. Update findings F-021 through F-024 based on the live retest outcome.
4. Implement shared provider ownership verification and cleanup primitives.
5. Wire worktree cleanup to provider state and prove it with MCP-level workflow tests.
6. Add benchmark provider cleanup/reset.
7. Run the isolated PyPI-installed MCP validation pass.
8. Only then mark provider workflows ready for the user documentation overhaul.
