# agents-remember-md — Onboarding Overview

> **Status:** active baseline

## What This Repo Is

`agents-remember-md` is the source repository for the Agents Remember workflow system. It defines the doctrine, skills, helper scripts, task workflows, and design references that agents use to maintain durable onboarding knowledge beside code. The core idea is one-to-one onboarding: source files have deterministic onboarding units that can be verified against Git history before an agent relies on them.

The current checked-in guidance distinguishes `ar-memory/` as durable internal memory from `ar-coordination/` as local coordination. C-08 exposes that split through `code_repository_name`, `code_repository_root`, `memory_root`, and `coordination_root`, C-09 owns worktree lifecycle mutation, direct current-checkout closeout for approved micro edits, and integration back to source branches, and C-10 provides the adoption path for existing external-memory onboarding that needs an initial `memory.md` ledger.

## Architecture At A Glance

```text
agents-remember-md/
  AGENTS.md
    workspace doctrine, task routing, onboarding gates
  README.md
    public setup and conceptual model
  skills/
    W-* task workflows
    U-* core maintenance and resolver skills
    P-* heavy workflow phase skills
  roadmap/
    design specs and historical planning notes
  system/
    example settings, sources, and tools files

workspace ar-coordination/
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
| Agent doctrine       | [AGENTS.md](agents-remember-md/AGENTS.md)                                                                                                                                       | Defines high-transparency collaboration, task routing, onboarding gates, and no-code-before-approval behavior. |
| Public documentation | [README.md](agents-remember-md/README.md) and [docs/FAQ.md](agents-remember-md/docs/FAQ.md)                                                                                       | Explains one-to-one onboarding, setup, storage modes, path-derived memory, agent wiring, coordination roots, and repository contents. |
| Core skills          | [skills/U-01-core-skills](agents-remember-md/skills/U-01-core-skills)                                                                                                           | Resolver, drift detection, repo bootstrap, onboarding maintenance, and related support skills.                 |
| Task workflows       | [skills/W-02-light-task-workflow](agents-remember-md/skills/W-02-light-task-workflow) and [skills/W-01-heavy-task-workflow](agents-remember-md/skills/W-01-heavy-task-workflow) | Durable task artifact workflows for medium and high-risk work.                                                 |
| Phase skills         | [skills/P-00-creation](agents-remember-md/skills/P-00-creation) through [skills/P-99-review](agents-remember-md/skills/P-99-review)                                             | Heavy workflow phase packages and review gates.                                                                |
| Roadmap and specs    | [roadmap](agents-remember-md/roadmap)                                                                                                                                           | Design specs, migration notes, and historical task plans. These are references, not onboarding substitutes.    |
| System examples      | [system](agents-remember-md/system)                                                                                                                                             | Example settings, sources, and tools files used as scaffolding material.                                       |

## Functional Areas

### Repository Doctrine

`AGENTS.md` is the authoritative behavioral contract for agents operating in this repository. It requires explicit framing for non-trivial work, C-08 resolution plus C-02 drift detection before relying on onboarding, C-05 propagation when durable current-state knowledge changes, and C-09 direct closeout for approved small current-checkout edits in external-memory mode.

### Core Resolver And Drift Gate

C-08 resolves the active coordination context: topology, code repository, `coordination_root`, `memory_root`, onboarding/docs/system roots, settings paths, task root, temporary artifact root, contract path, worktree group, ledger path, storage settings, path rules, and branch-gated cross-repo allowances. Path-rule defaults in `system/settings.json` now carry the standard generated/vendor/build/cache/IDE/env/Zone.Identifier excludes. For worktree-backed task names, C-08 resolves current wrapper folders first and persisted `*-ar` task folders second. C-02 consumes that context and verifies file-level onboarding metadata against the current source state. Drift reports are temporary coordination artifacts under `temp_root`; even explicit report paths inside the durable memory repo should be redirected back to coordination temp.

### Onboarding Maintenance

C-05 owns file-level onboarding and repo-level entity catalogs. It is the maintenance path for creating or updating onboarding artifacts; C-02 detects drift but does not rewrite onboarding content. File-level onboarding now records the nearest governing `overview.md` when route-local overview coverage exists, while remaining self-sufficient for the concrete source file. C-05 also detects route-level create, refresh, move, and deletion cleanup cases and routes those structural changes to C-03 `existing-memory-slice-maintenance`.

### Task Workflows

W-02 is the compact durable-task workflow used by the current worktree-support task stack. It creates a task wrapper folder and `task.md` once task class and naming are clear, stops for implementation approval, then treats the checklist, onboarding propagation, checks, and worktree-backed commit approval handoff as one implementation cycle. When refreshed external-memory onboarding is part of intake, the memory content and ledger are committed before C-09 starts worktrees.

### Bootstrap Memory Build

C-03 now treats the root repo overview as the minimum successful bootstrap and scales through route-local overview construction pillars, evidence packs, file cards, onboarding waves, curator reviews, and handoff artifacts. Its templates live beside the skill under `skills/U-01-core-skills/C-03-repo-bootstrap/templates/` and define the shape of input ledgers, state files, coverage plans, governing route maps, overview cards, route-local overviews, docs packs, boundary packs, file cards, wave manifests, curator reviews, and final handoffs. Route-local overviews are durable memory in the mirrored onboarding hierarchy directly under the resolved onboarding root, not detached area appendices, and file-level onboarding links back to the nearest governing overview. Existing-memory slice maintenance handles added, moved, deleted, refreshed, and newly important routes without pretending the repo is blank; automated bootstrap starts after source inventory intake and stops at handoff before separate closeout approval.

### Worktree Support

The worktree and cross-repo roadmap specs are still useful design references, but core implementation now exists for the first support slice: memory ledger parsing/writing, worktree contract parsing/writing, C-08 contract-aware facts, the C-09 `start`, `attach`, `status`, `bootstrap-memory`, `closeout`, `direct-closeout`, `integrate`, and `cleanup` command surface, and the C-10 `status`/`adopt` adoption workflow for pre-existing external-memory onboarding. C-09 external-memory start blocks dirty source memory repos so a refreshed onboarding pass cannot be accidentally stranded outside the ledgered baseline. C-09 closeout dry-run is the non-mutating preview path before explicit commit approval, and real external-memory closeout commits code first, refreshes affected onboarding verification metadata to that new code commit, then commits memory content and ledger. Direct closeout applies that same code-then-memory-then-ledger order to approved current-checkout micro edits without creating worktree contracts.

## Cross-Repo References

This repository is currently selected into the workspace `C:\ew\ar-coordination` coordinator by path rules in the coordinator settings, but onboarding content should cite same-repo files for repository behavior and task files only as planning references.

| Finding                                                                                                                                                                                                                       | Citations            | Source Path                               |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------- | ----------------------------------------- |
| Workspace rules require C-08 resolution and C-02 drift detection before relying on onboarding, C-05 handles onboarding refresh when needed, and C-09 `direct-closeout` handles approved current-checkout micro-edit closeout. | L332-L338; L397-L410 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| The README presents C-08 as the active context resolver and C-02 as the drift classifier rather than the topology resolver.                                                                                                   | L424-L430            | [README.md](agents-remember-md/README.md) |

## Build & Dev

- No `agents-remember-md`-specific build or test command is currently listed in the resolved coordinator [system/tools.md](ar-coordination/system/tools.md).
- The C-08, C-02, C-09, ledger, contract, and worktree-support test helpers use Python standard-library code and can be invoked directly with Python.
- This onboarding pass intentionally does not modify `system/sources.md` or `system/tools.md`.

## Key Invariants

- Onboarding should describe current repository state; task files describe planned or in-progress future work.
- C-08 owns topology and path resolution facts; it must not perform Git worktree operations.
- C-02 detects drift and writes reports under the resolved temporary artifact root; it must not update onboarding itself or write temporary reports into durable memory repos.
- C-05 creates and maintains onboarding artifacts; it must use actual evidence sources rather than citing source registries as proof.
- Task workflows must stop for developer approval before implementation.
- Worktree-backed task workflows must stop again for explicit commit approval before C-09 closeout creates commits.
- C-09 wraps task workflows with worktree lifecycle state and also owns direct closeout for approved current-checkout micro edits; it does not replace W-02, starts external-memory worktrees only from a clean committed memory baseline, does not commit, integrate, or clean up without the relevant explicit approval, refreshes affected onboarding metadata between code and memory commits during external-memory closeout, and runs cleanup only after successful integration.
- C-10 is an adoption wrapper for existing external-memory onboarding; it does not refresh onboarding and it does not overwrite an existing ledger.
- C-03 bootstrap memory must keep durable route-local overviews in the mirrored onboarding hierarchy under the resolved onboarding root, use root `bootstrap/` artifacts as temporary promotion/review artifacts, keep low-confidence claims out of durable fact sections, apply candidate excludes before scouting, and hand file-level onboarding semantics to C-05.
- C-05 file-level onboarding remains strict one-to-one with source files and must not collapse file-specific facts into a generic route overview reference; structural route changes route to C-03 rather than becoming disconnected file edits.

## Glossary Terms

| Term                     | Meaning                                                                                                       | Notes                                                                                                                                               |
| ------------------------ | ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| onboarding unit          | A deterministic documentation unit for one source file or one repo-level entity catalog.                      | File-level units mirror source paths and carry verification metadata.                                                                               |
| coordination context     | The resolved root/path/settings facts returned by C-08 for a code repository.                                 | Current implementation exposes `code_repository_name`, `code_repository_root`, `memory_root`, `coordination_root`, and `temp_root`.                 |
| pathRules                | Include/exclude eligibility rules that decide which source paths and file types are managed.                  | Storage and eligibility are separate concepts.                                                                                                      |
| drift report             | A C-02 maintenance artifact that classifies onboarding trust.                                                 | It is temporary evidence under `temp/drift-reports`, not durable repo behavior; explicit memory-root report paths are redirected to temp.           |
| worktree contract        | Local runtime state file for worktree-backed tasks.                                                           | The parser/writer lives in `_shared/agents_remember/worktree_contract.py`; C-09 creates and consumes contracts beside the task wrapper's `task.md`. |
| worktree integration     | The approved C-09 phase that lands closed task work back onto source branches.                                | `ff-only` requires unchanged source ancestry; `replay` supports parallel non-overlapping work and blocks conflicts before main moves.               |
| direct closeout          | The C-09 current-checkout closeout path for approved small external-memory edits.                               | It dry-runs first, then commits code, refreshes onboarding metadata, commits memory, and commits the ledger without creating worktree contracts.    |
| memory baseline adoption | The one-time action of turning current external-memory onboarding into the first ledgered `memory.md` baseline. | C-10 checks drift first, requires explicit drift acceptance when needed, and delegates ledger creation to C-09.                                     |

## Docs References

No relevant external domain documentation was found for this repository's own workflow mechanics. The resolved `Domain Documentation` registry is currently biased toward `resolve_auto_editor` technologies such as Resolve, Gemini, FastAPI, Pydantic, OTIO, FFmpeg, SQLite, and related libraries; those sources are not direct evidence for `agents-remember-md` repository behavior.

| Finding                                                                                                                                      | Citations | Source Path |
| -------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ----------- |
| No external documentation is needed to prove the repository's own current workflow structure; same-repository files are the direct evidence. | n/a       | n/a         |

## What To Explore Next

| Priority | Area / Path                                                                                                               | Why Next                                                                                                            |
| -------- | ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| high     | [skills/U-01-core-skills/C-09-git-worktree-manager](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager) | External workflow metadata and richer task-intake variables are the next likely worktree lifecycle polish area.     |
| medium   | [skills/W-01-heavy-task-workflow](agents-remember-md/skills/W-01-heavy-task-workflow)                                     | Heavy workflow docs may need a separate onboarding pass if worktree-backed task folders become common outside W-02. |
| medium   | [system](agents-remember-md/system)                                                                                       | Add richer settings fixtures if cross-repo v2 behavior needs more than the current example files.                   |

## Needs Verification

- The coordinator `ar-coordination/system/tools.md` currently lists checks for `resolve_auto_editor`, not this repo.
- The current source registry is useful as a discovery index but has no direct external domain evidence for this repo's own skill/workflow mechanics.
- External-memory onboarding for `agents-remember-md` is ledgered; future closeouts must keep the code-to-memory mapping current.
- The current bootstrap-template and FAQ path-model expansion is pending final source commits; verification metadata for new/changed onboarding should be refreshed after the code commit lands.

## Last Verified

Updated 2026-05-14T21:38 after skill frontmatter cleanup and moving the standard exclusion baseline into `settings.json` path-rule defaults while keeping the C-03 list as a settings review example. Verification metadata remains pinned to the last committed source state until the follow-up is approved for commit.
