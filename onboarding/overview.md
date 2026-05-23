# agents-remember-md — Onboarding Overview

> **Status:** active baseline

## What This Repo Is

`agents-remember-md` is the source repository for the Agents Remember workflow system. It defines the doctrine, skills, MCP tools, task workflows, and design references that agents use to maintain durable onboarding knowledge beside code. The core idea is deterministic onboarding: source files have one-to-one onboarding units that can be verified against Git history, while overviews and entity catalogs use route scopes or curated evidence fingerprints before an agent relies on them.

The current checked-in guidance distinguishes `ar-memory/` as durable internal memory from `ar-coordination/` as local coordination. C-08 exposes that split through `code_repository_name`, `code_repository_root`, `memory_root`, and `coordination_root`, C-09 owns worktree lifecycle mutation, direct current-checkout closeout for approved micro edits, and integration back to source branches, and C-10 provides the adoption path for existing external-memory onboarding that needs an initial `memory.md` ledger.

The provider runtime guidance now routes through the MCP/package boundary: MCP settings outside the coordinator are authority, coordinator files can only teach the model what to ask for, and provider runtime state lives under one coordinator provider root. Runtime-owned binaries and Python venvs live under `providers/_bin/` and `providers/_venvs/`, provider instances live under `providers/runners/`, durable provider database data lives under `providers/data/`, and logs live under `providers/logs/`. Providers that need databases should use Docker-wrapped backends in managed mode; GrepAI uses a workspace-mode PostgreSQL/pgvector Docker backend for multiple memory roots, and CGC uses a FalkorDB Docker backend for configured code roots.

## Hot Path Summary

Use the root index to route quickly: `AGENTS.md` and `README.md` cover the source-checkout and public contracts, `mcp/` covers the package-managed MCP server, context packet, runtime install, skills install, provider lifecycle/setup, benchmark tools, settings, route-index generation, drift, worktree services, memory services, and integrity tools, `runtime/agents-md-files` covers installed instruction templates, `runtime/skills/U-01-core-skills` covers workflow guidance for resolver, drift, bootstrap, onboarding, route-index, memory, and worktree tasks, and `runtime/skills/W-*` covers task workflows. For route-index behavior start at `mcp/src/agents_remember/kernel/route_index.py`, the `route_index_refresh` MCP tool, C-05, and C-04.

## Architecture At A Glance

```text
agents-remember-md/
  AGENTS.md
    source checkout instructions and installed-runtime handoff
  README.md
    public setup and conceptual model
  mcp/
    package-managed MCP server, runtime/skills install, provider lifecycle/setup, benchmark tools, settings, and integrity checks
  runtime/
    agents-md-files/
      coordinator/AGENTS.md
      skills/AGENTS.md
      system/AGENTS.md
      tasks/AGENTS.md
    skills/
      W-* task workflows
      U-* core maintenance and resolver skills
      W-01-heavy-task-workflow/skills/P-* heavy workflow phase skills
    system/defaults/examples/
      coordinator and memory-repo example settings, sources, and tools files
  roadmap/
    design specs and historical planning notes

workspace ar-coordination/
  AGENTS.md
  skills/
  memory-repos/ar-agents-remember-md/
    memory.md
    onboarding/
      current onboarding baseline for this repo
  tasks/
    durable planning artifacts for worktree-support rollout
  temp/
    temporary generated artifacts such as drift reports
```

## Code Structure

| Area                 | Path                                                                                                                                                                            | Purpose                                                                                                        |
| -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------- |
| Source checkout instructions | [AGENTS.md](agents-remember-md/AGENTS.md)                                                                                                                               | Defines how agents work on this source checkout and when to hand off to the installed runtime instructions.    |
| Public documentation | [README.md](agents-remember-md/README.md) and [docs](agents-remember-md/docs)                                                                                       | Keeps the root README as the public front door while focused docs pages own setup, concepts, architecture, workflows, install guides, guides, and reference material. |
| MCP package          | [mcp](agents-remember-md/mcp)                                                                                                                                                       | Package-managed MCP server exposing context, runtime install, skills install, provider, worktree, memory, benchmark, settings-derived lifecycle, and integrity tools. |
| Core skills          | [runtime/skills/U-01-core-skills](agents-remember-md/runtime/skills/U-01-core-skills)                                                                                                           | Resolver, drift detection, repo bootstrap, onboarding maintenance, and related support skills.                 |
| Task workflows       | [runtime/skills/W-02-light-task-workflow](agents-remember-md/runtime/skills/W-02-light-task-workflow) and [runtime/skills/W-01-heavy-task-workflow](agents-remember-md/runtime/skills/W-01-heavy-task-workflow) | Durable task artifact workflows for medium and high-risk work.                                                 |
| Phase skills         | [runtime/skills/W-01-heavy-task-workflow/skills/P-00-creation](agents-remember-md/runtime/skills/W-01-heavy-task-workflow/skills/P-00-creation) through [runtime/skills/W-01-heavy-task-workflow/skills/P-99-review](agents-remember-md/runtime/skills/W-01-heavy-task-workflow/skills/P-99-review) | Heavy workflow phase packages and review gates. |
| Roadmap and specs    | [roadmap](agents-remember-md/roadmap)                                                                                                                                           | Design specs, migration notes, and historical task plans. These are references, not onboarding substitutes.    |
| Runtime AGENTS templates | [runtime/agents-md-files](agents-remember-md/runtime/agents-md-files)                                                                                                        | Package-owned coordinator, skills, system, and tasks `AGENTS.md` templates for runtime installation.           |
| System defaults      | [runtime/system/defaults/examples](agents-remember-md/runtime/system/defaults/examples)                                                                                          | Example settings, sources, and tools files used as scaffolding material.                                       |

## Functional Areas

### Source Checkout Contract

`AGENTS.md` is the authoritative behavioral contract for agents operating on this source checkout. It now starts by separating the package source repository from the installed `ar-coordination` runtime: when the file is reached through a workspace-level pointer during sibling-repository work, agents should use the installed runtime `AGENTS.md` instead. For work on this repository itself, it keeps `agents-remember-md` as the resolver target, preserves the chat/W-02/W-01 workflow routing, requires C-08 resolution plus C-02 drift detection before relying on onboarding, and points active settings reads at the resolved memory layer rather than a root-level source checkout `system/` directory.

### Public Documentation

The public README is now intentionally short: product positioning, core path-derived memory example, one generic quickstart, harness install links, docs links, and a compact source/runtime layout. Detailed user-facing material moved under `docs/`: `docs/README.md` is the documentation index, `getting-started.md`, `concepts.md`, `architecture.md`, `workflows.md`, and `FAQ.md` own core narrative, `docs/install/` owns harness-specific setup, `docs/guides/` owns operational tasks, and `docs/reference/` owns exact runtime/settings/skill behavior. The repo's current path rules still exclude `docs/**` from file-level onboarding, so README onboarding and this repo overview carry the durable summary of the public docs split.

### Runtime AGENTS Templates

`runtime/agents-md-files/` is the package-owned source for installed coordinator instructions. The current package has four installable templates: `coordinator/AGENTS.md` for the coordinator root, `skills/AGENTS.md` for compact C-* skill routing, `system/AGENTS.md` for the hard onboarding maintenance gate, and `tasks/AGENTS.md` for task-folder collaboration doctrine. MCP `runtime_install` installs those templates to `ar-coordination/AGENTS.md`, `ar-coordination/skills/AGENTS.md`, `ar-coordination/system/AGENTS.md`, and `ar-coordination/tasks/AGENTS.md`. Memory repos are not expected to provide a root-level `AGENTS.md`; repo-specific memory guidance lives in the memory layer's `system/*` files.

### Core Resolver And Drift Gate

C-08 resolves the active coordination context: topology, code repository, `coordination_root`, `memory_root`, onboarding/docs/system roots, settings paths, repo-specific task root, temporary artifact root, contract path, worktree group, ledger path, storage settings, path rules, and branch-gated cross-repo allowances. Without a task name, `task_root` is the repository namespace under `ar-coordination/tasks/<repo>/`; with a task name or contract, it is the concrete task folder. Path-rule defaults in `system/settings.json` now carry the standard generated/vendor/build/cache/IDE/env/Zone.Identifier excludes. For worktree-backed task names, C-08 resolves current wrapper folders first and persisted `*-ar` task folders second. C-02 consumes that context and verifies file-level onboarding metadata, overview `sourceRoute` metadata, inline digests, and repo entity `git-blob-set-v1` fingerprints against the current source state. Drift reports are temporary coordination artifacts under `temp_root`; even explicit report paths inside the durable memory repo should be redirected back to coordination temp.

### Onboarding Maintenance

C-05 owns file-level onboarding and repo-level entity catalogs. It is the maintenance path for creating or updating onboarding artifacts; C-02 detects drift but does not rewrite onboarding content. File-level onboarding now records the nearest governing `overview.md` when route-local overview coverage exists, while remaining self-sufficient for the concrete source file. Entity catalogs now carry one deterministic fingerprint row per entity over a small curated evidence file set; C-05 chooses and refreshes those paths after review. C-05 also detects route-level create, refresh, move, and deletion cleanup cases and routes those structural changes to C-03 `existing-memory-slice-maintenance`. Generated `overview.index.json` files live beside route overviews and expose route scope, covered sidecars, child routes, copied hot-path summaries, and mechanically derived source-anchor hints so C-04 can route cheaply before opening full overview prose.

### MCP And Context Provider Runtime

The runtime has optional local discovery providers, but they remain accelerators rather than proof. The MCP settings file, not coordinator `system/settings.json`, declares allowed providers and repositories for the MCP path. `context_packet` reports provider and watcher state, `runtime_install` installs runtime assets and provider dependencies from package-local code, and `skills_install` copy-installs packaged skills into harness skill roots. Managed provider installs should be coordination-owned: pinned requirements under `providers/requirements/`, runtime-owned binaries under `providers/_bin/`, reusable Python venvs only for Python providers under `providers/_venvs/`, provider instances under `providers/runners/`, durable databases under `providers/data/`, logs under `providers/logs/`, and patches under `providers/patches/`. Database and daemon infrastructure should be Docker-wrapped rather than installed as host services.

GrepAI runs in workspace mode with explicit `{ projectId, path }` roots generated from MCP repository/memory settings. Managed mode mirrors those roots under `providers/runners/grepai/index-roots/` before launching GrepAI because GrepAI still writes per-project `.grepai/` symbol/config artifacts beside each configured project path. Its runtime config, state, cache, home artifacts, and mirrors belong under `providers/runners/grepai/`; its shared PostgreSQL/pgvector Docker data belongs under `providers/data/grepai/postgres/`; and `.grepai/` inside a durable memory root is a containment failure, not durable memory. CodeGraphContext keeps one provider instance per configured repo under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, with all instances sharing the FalkorDB Docker data root under `providers/data/codegraphcontext/falkordb/`.

### Code Quality And Refactor Baseline

The source checkout now explicitly tells agents to run Ruff and Radon after Python implementation work, then use the resolved memory layer's `system/tools.md` for exact validation commands and `system/coding-guidelines.md` for repository-specific style rules. Coordinator-level tools examples keep global commands separate from repo-specific code quality tools, and the memory-repo tools example reserves a `Code Quality` section for lint, format, typecheck, test, build, and smoke-check commands.

The current `pyproject.toml` makes Ruff responsible for import/style/static hygiene and Radon responsible for complexity scouting. Ruff ignores line-length wrapping, high-branch/high-return/high-statement complexity warnings, and numeric sentinel warnings that are better reviewed through Radon or code review. Test files have targeted ignores for unused patched-callable arguments and import-path setup. Radon is configured to show `B` through `F` cyclomatic complexity, visible complexity scores, total/average output, and maintainability-index pressure points while excluding generated, cache, virtualenv, build, dist, and test paths.

The last quality sweep passed Ruff, Ruff format check, compile checks, MCP unit tests, and diff whitespace checks after safe formatting and cleanup. It also found refactor pressure that should feed Phase 06 rather than be hidden by formatter churn: `parse_settings_block` in `coordination_context_resolver.py` was the highest-complexity function seen in the sweep, and provider lifecycle/setup plus worktree and benchmark modules remain large enough to need package-level analysis before code motion.

### Task Workflows

W-02 is the compact durable-task workflow used by the current worktree-support task stack. It creates a task wrapper folder and `task.md` once task class and naming are clear, stops for implementation approval, then treats the checklist, onboarding propagation, checks, and worktree-backed commit approval handoff as one implementation cycle. When refreshed external-memory onboarding is part of intake, the memory content and ledger are committed before C-09 starts worktrees.

### Bootstrap Memory Build

C-03 now treats the root repo overview as the minimum successful bootstrap and scales through route-local overview construction pillars, evidence packs, file cards, onboarding waves, curator reviews, and handoff artifacts. Its templates live beside the skill under `runtime/skills/U-01-core-skills/C-03-repo-bootstrap/templates/` and define the shape of input ledgers, state files, coverage plans, governing route maps, overview cards, route-local overviews, docs packs, boundary packs, file cards, wave manifests, curator reviews, and final handoffs. Route-local overviews are durable memory in the mirrored onboarding hierarchy directly under the resolved onboarding root, not detached area appendices, and file-level onboarding links back to the nearest governing overview. Existing-memory slice maintenance handles added, moved, deleted, refreshed, and newly important routes without pretending the repo is blank; automated bootstrap starts after source inventory intake and stops at handoff before separate closeout approval.

### Worktree Support

The worktree and cross-repo roadmap specs are still useful design references, but core implementation now exists for the first support slice: memory ledger parsing/writing, worktree contract parsing/writing, C-08 contract-aware facts, the C-09 `start`, `attach`, `status`, `closeout`, `direct-closeout`, `integrate`, and `cleanup` command surface, and the C-10 `status`/`adopt` adoption workflow for pre-existing external-memory onboarding. C-00 initializes missing memory roots before C-09 worktree use. C-09 external-memory start blocks dirty source memory repos so a refreshed onboarding pass cannot be accidentally stranded outside the ledgered baseline. C-09 closeout dry-run is the non-mutating preview path before explicit commit approval, and real external-memory closeout commits code first, refreshes affected onboarding verification metadata to that new code commit, then commits memory content and ledger. Direct closeout applies that same code-then-memory-then-ledger order to approved current-checkout micro edits without creating worktree contracts.

## Cross-Repo References

This repository is currently selected into the workspace `/home/mohamedreadone/Projects/ar-coordination` coordinator by path rules in the coordinator settings, but onboarding content should cite same-repo files for repository behavior and task files only as planning references.

| Finding                                                                                                                                                                                                                       | Citations            | Source Path                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------- |
| The source checkout instructions distinguish this repository from the installed runtime, hand sibling-repo work to `ar-coordination/AGENTS.md`, and keep C-08 plus C-02 as the context gate for this repo. | L1-L14; L28-L53 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| The source checkout instructions route repo-specific code quality checks through resolved memory-layer `system/tools.md`, tell agents to run Ruff and Radon after Python implementation work, and use `system/coding-guidelines.md` when present. | L60-L62; L90-L96 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| The README now presents the public front door, the generic quickstart, links to harness install pages, and a compact source/runtime layout.                                                                                                   | L1-L138            | [README.md](agents-remember-md/README.md) |
| The docs index owns the expanded documentation map for start-here docs, install guides, operational guides, and reference pages.                                                                                                   | L1-L39            | [docs/README.md](agents-remember-md/docs/README.md) |
| MCP provider guidance requires Docker-wrapped provider backends instead of host-level services, mirrors GrepAI roots under provider-owned index roots, stores GrepAI artifacts under `providers/runners/grepai/`, stores GrepAI PostgreSQL data under `providers/data/grepai/postgres/`, and treats `.grepai/` in durable memory roots as containment failure. | L79-L99 | [runtime/system/defaults/examples/coordinator/settings.md](agents-remember-md/runtime/system/defaults/examples/coordinator/settings.md) |
| The MCP settings example declares the external authority surface for repositories, provider ids, timeout caps, transcript roots, and package-derived provider runtime paths, replacing the removed coordinator `system/settings.json` provider template. | L1-L31 | [examples/mcp/settings.example.json](agents-remember-md/examples/mcp/settings.example.json) |
| The repository quality configuration leaves Ruff on import/style/static hygiene, delegates branch/statement complexity pressure to Radon, gives tests targeted patched-callable/import-setup ignores, and configures Radon to report `B` through `F` complexity plus maintainability pressure. | L1-L39; L59-L68 | [pyproject.toml](agents-remember-md/pyproject.toml) |
| The coordinator tools example says repo-specific code quality tools belong in the selected memory layer, while the memory-repo tools example provides a `Code Quality` section for lint, format, typecheck, test, build, and smoke-check commands. | L6-L7; L5-L14 | [runtime/system/defaults/examples/coordinator/tools.md](agents-remember-md/runtime/system/defaults/examples/coordinator/tools.md); [runtime/system/defaults/examples/memory-repo/tools.md](agents-remember-md/runtime/system/defaults/examples/memory-repo/tools.md) |

## Build & Dev

- Source-checkout Python implementation work should run Ruff and Radon from the `agents-remember-md/` root; exact command details belong in the resolved memory layer's `system/tools.md`.
- The MCP package tests under `mcp/tests` cover C-08, C-02, C-09, ledger, contract, provider, benchmark, runtime install, and skills install behavior through package modules.
- This onboarding pass intentionally does not modify `system/sources.md` or `system/tools.md`.

## Key Invariants

- Onboarding should describe current repository state; task files describe planned or in-progress future work.
- C-08 owns topology and path resolution facts; it must not perform Git worktree operations.
- C-02 detects file-level, overview, inline, and per-entity fingerprint drift and writes reports under the resolved temporary artifact root; it must not update onboarding itself or write temporary reports into durable memory repos.
- C-05 creates and maintains onboarding artifacts; it must use actual evidence sources rather than citing source registries as proof.
- Task workflows must stop for developer approval before implementation.
- Worktree-backed task workflows must stop again for explicit commit approval before C-09 closeout creates commits.
- C-09 wraps task workflows with worktree lifecycle state and also owns direct closeout for approved current-checkout micro edits; it does not replace W-02, starts external-memory worktrees only from a clean committed memory baseline, does not commit, integrate, or clean up without the relevant explicit approval, refreshes affected onboarding metadata between code and memory commits during external-memory closeout, and runs cleanup only after successful integration.
- C-10 is an adoption wrapper for existing external-memory onboarding; it does not refresh onboarding and it does not overwrite an existing ledger.
- C-03 bootstrap memory must keep durable route-local overviews in the mirrored onboarding hierarchy under the resolved onboarding root, use root `bootstrap/` artifacts as temporary promotion/review artifacts, keep low-confidence claims out of durable fact sections, apply candidate excludes before scouting, and hand file-level onboarding semantics to C-05.
- C-05 file-level onboarding remains strict one-to-one with source files and must not collapse file-specific facts into a generic route overview reference; structural route changes route to C-03 rather than becoming disconnected file edits.
- Route indexes are generated availability metadata, not hand-authored truth; overview `## Hot Path Summary` sections and file sidecars are the maintained inputs, and C-04 should infer missing sidecars from `sourceScope` plus `coveredFiles`.
- Repo entity catalogs use deterministic `git-blob-set-v1` fingerprints over curated load-bearing evidence files so C-02 can flag stale entity memory without semantic guessing.
- The package-owned runtime `AGENTS.md` template set is currently `coordinator`, `skills`, `system`, and `tasks`; memory repos use `system/*` files rather than a root-level `AGENTS.md`.
- Runtime, provider, benchmark, route-index, drift, memory, worktree, and skill-install behavior belongs in MCP package modules; the source checkout no longer keeps parallel `installer/`, top-level `scripts/`, `runtime/scripts/`, skill-local `scripts/`, `_shared`, or skill-local `tests` execution routes.
- Ruff owns source hygiene and Radon owns complexity scouting for this repository; high-complexity results should feed refactor planning and coding-guideline updates rather than being buried through broad local suppressions.
- Managed provider mode should wrap provider databases and daemon infrastructure in Docker instead of requiring host-level PostgreSQL, FalkorDB, OS service managers, launch agents, package-manager services, or global user daemons.
- Provider runtime artifacts are not durable memory or source data: GrepAI config/state/cache/home files and index mirrors belong under `providers/runners/grepai/`, CGC runtime files belong under `providers/runners/codegraphcontext/<repo-id>/.codegraphcontext/`, durable provider database data belongs under `providers/data/`, and logs belong under `providers/logs/`.

## Glossary Terms

| Term                     | Meaning                                                                                                       | Notes                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| onboarding unit          | A deterministic documentation unit for one source file or one repo-level entity catalog.                      | File-level units mirror source paths and carry verification metadata.                                                                               |
| entity fingerprint       | A deterministic hash over the load-bearing files that define a repo entity.                                  | C-05 curates the evidence paths; C-02 recomputes `git-blob-set-v1` and flags drift.                                                                 |
| coordination context     | The resolved root/path/settings facts returned by C-08 for a code repository.                                 | Current implementation exposes `code_repository_name`, `code_repository_root`, `memory_root`, `coordination_root`, repo-specific `task_root`, and `temp_root`. |
| pathRules                | Include/exclude eligibility rules that decide which source paths and file types are managed.                  | Storage and eligibility are separate concepts.                                                                                                      |
| drift report             | A C-02 maintenance artifact that classifies onboarding trust.                                                 | It is temporary evidence under `temp/drift-reports`, not durable repo behavior; explicit memory-root report paths are redirected to temp.           |
| worktree contract        | Local runtime state file for worktree-backed tasks.                                                           | The parser/writer lives in `mcp/src/agents_remember/worktrees/worktree_contract.py`; C-09 creates and consumes contracts beside the task wrapper's `task.md`. |
| worktree integration     | The approved C-09 phase that lands closed task work back onto source branches.                                | `ff-only` requires unchanged source ancestry; `replay` supports parallel non-overlapping work and blocks conflicts before main moves.               |
| direct closeout          | The C-09 current-checkout closeout path for approved small external-memory edits.                               | It dry-runs first, then commits code, refreshes onboarding metadata, commits memory, and commits the ledger without creating worktree contracts.    |
| memory baseline adoption | The one-time action of turning current external-memory onboarding into the first ledgered `memory.md` baseline. | C-10 checks drift first, requires explicit drift acceptance when needed, and delegates ledger creation to C-09.                                     |
| runtime AGENTS template  | A package-owned `AGENTS.md` source under `runtime/agents-md-files/`.                                             | Current templates are coordinator, skills, system, and tasks; there is no memory-repo `AGENTS.md` template or expected memory-repo root instruction file. |
| MCP runtime settings     | A trusted settings file outside the coordinator root that controls the MCP server.                              | It provides `coordinationRoot`, `workspaceRoot`, allowed repos/providers, timeout caps, and optional contract paths; coordinator files do not grant authority. |

## Docs References

Same-repository files remain the direct evidence for Agents Remember's own runtime and memory behavior. Public install pages now also link official harness documentation for volatile skill-location claims.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Claude Code, Cursor, Windsurf, VS Code Copilot, Pi, Hermes, and OpenClaw install pages link official docs for their current instruction and skill discovery behavior. | n/a | [Claude Code skills](https://code.claude.com/docs/en/skills); [Cursor Agent Skills](https://cursor.com/docs/skills.md); [Windsurf Skills](https://docs.windsurf.com/windsurf/cascade/skills); [VS Code Agent Skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills); [Pi Skills](https://pi.dev/docs/latest/skills); [Hermes Context Files](https://hermes-agent.nousresearch.com/docs/user-guide/features/context-files/); [OpenClaw Agent Workspace](https://docs.openclaw.ai/concepts/agent-workspace) |
| No external documentation is needed to prove the repository's own runtime, resolver, drift, onboarding, or workflow structure; same-repository files remain the direct evidence. | n/a | n/a |

## What To Explore Next

| Priority | Area / Path                                                                                                               | Why Next                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| high     | [runtime/skills/U-01-core-skills/C-09-git-worktree-manager](agents-remember-md/runtime/skills/U-01-core-skills/C-09-git-worktree-manager) | External workflow metadata and richer task-intake variables are the next likely worktree lifecycle polish area.     |
| medium   | [runtime/skills/W-01-heavy-task-workflow](agents-remember-md/runtime/skills/W-01-heavy-task-workflow)                                     | Heavy workflow docs may need a separate onboarding pass if worktree-backed task folders become common outside W-02. |
| medium   | [runtime/system/defaults](agents-remember-md/runtime/system/defaults)                                                     | Add richer settings fixtures if cross-repo v2 behavior needs more than the current example files.                   |

## Needs Verification

- The coordinator `ar-coordination/system/tools.md` currently lists checks for `resolve_auto_editor`, not this repo.
- The current source registry is useful as a discovery index but has no direct external domain evidence for this repo's own skill/workflow mechanics.
- External-memory onboarding for `agents-remember-md` is ledgered; future closeouts must keep the code-to-memory mapping current.
- The current root `AGENTS.md` source-checkout reframing is pending final source commit; verification metadata for that onboarding should be refreshed after the code commit lands.
- The README/docs professionalization rewrite is pending final source commit; README onboarding verification metadata should be refreshed after the docs commit lands.
- The route-index package module and moved MCP tests are pending final source commit; their file-level onboarding metadata should be refreshed during closeout.
- The GrepAI workspace/PostgreSQL provider runtime update is pending final source commit; affected file-level onboarding verification metadata remains pinned until closeout refreshes it.
- The quality-pass source changes and this overview update are pending final source/memory commits; affected file-level onboarding verification metadata remains pinned until closeout refreshes it.

## Last Verified

Updated 2026-05-23T22:20+02:00 after the code-quality routing pass added explicit Ruff/Radon guidance, adjusted the Ruff/Radon configuration split, and identified Phase 06 refactor pressure. Verification metadata remains pinned to the last committed source state until closeout commits the source changes.
