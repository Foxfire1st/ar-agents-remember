# agents-remember-md — Onboarding Overview

> **Status:** active baseline

## What This Repo Is

`agents-remember-md` is the source repository for the Agents Remember workflow system. It defines the doctrine, skills, helper scripts, task workflows, and design references that agents use to maintain durable onboarding knowledge beside code. The core idea is one-to-one onboarding: source files have deterministic onboarding units that can be verified against Git history before an agent relies on them.

The current checked-in guidance distinguishes `ar-memory/` as durable internal memory from `ar-management/` as local coordination. C-08 exposes that split through `memory_root` and `coordination_root`, C-09 owns worktree lifecycle mutation plus integration back to source branches, and C-10 provides the adoption path for existing shared-memory onboarding that needs an initial `memory.md` ledger.

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

shared ar-management/
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

| Area | Path | Purpose |
| --- | --- | --- |
| Agent doctrine | [AGENTS.md](agents-remember-md/AGENTS.md) | Defines high-transparency collaboration, task routing, onboarding gates, and no-code-before-approval behavior. |
| Public documentation | [README.md](agents-remember-md/README.md) | Explains one-to-one onboarding, setup, storage modes, agent wiring, shared roots, and repository contents. |
| Core skills | [skills/U-01-core-skills](agents-remember-md/skills/U-01-core-skills) | Resolver, drift detection, repo bootstrap, onboarding maintenance, and related support skills. |
| Task workflows | [skills/W-02-light-task-workflow](agents-remember-md/skills/W-02-light-task-workflow) and [skills/W-01-heavy-task-workflow](agents-remember-md/skills/W-01-heavy-task-workflow) | Durable task artifact workflows for medium and high-risk work. |
| Phase skills | [skills/P-00-creation](agents-remember-md/skills/P-00-creation) through [skills/P-99-review](agents-remember-md/skills/P-99-review) | Heavy workflow phase packages and review gates. |
| Roadmap and specs | [roadmap](agents-remember-md/roadmap) | Design specs, migration notes, and historical task plans. These are references, not onboarding substitutes. |
| System examples | [system](agents-remember-md/system) | Example settings, sources, and tools files used as scaffolding material. |

## Functional Areas

### Repository Doctrine

`AGENTS.md` is the authoritative behavioral contract for agents operating in this repository. It requires explicit framing for non-trivial work, C-08 resolution plus C-02 drift detection before relying on onboarding, and C-05 propagation when durable current-state knowledge changes.

### Core Resolver And Drift Gate

C-08 resolves the active management context: topology, target repo, `coordination_root`, `memory_root`, onboarding/docs/system roots, settings paths, task root, temporary artifact root, contract path, worktree group, ledger path, storage settings, path rules, and branch-gated cross-repo allowances. C-02 consumes that context and verifies file-level onboarding metadata against the current source state.

### Onboarding Maintenance

C-05 owns file-level onboarding and repo-level entity catalogs. It is the maintenance path for creating or updating onboarding artifacts; C-02 detects drift but does not rewrite onboarding content.

### Task Workflows

W-02 is the compact durable-task workflow used by the current worktree-support task stack. It creates a single task file, stops for approval, then treats the checklist, onboarding propagation, and checks as one implementation cycle.

### Worktree Support

The worktree and cross-repo roadmap specs are still useful design references, but core implementation now exists for the first support slice: shared ledger parsing/writing, worktree contract parsing/writing, C-08 contract-aware facts, the C-09 `start`, `attach`, `status`, `bootstrap-memory`, `closeout`, and `integrate` command surface, and the C-10 `status`/`adopt` adoption workflow for pre-existing shared-memory onboarding.

## Cross-Repo References

This repository is currently selected into the shared `C:\ew\ar-management` coordinator by path rules in the shared settings, but onboarding content should cite same-repo files for repository behavior and task files only as planning references.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Workspace rules require C-08 resolution and C-02 drift detection before relying on onboarding, and C-05 handles onboarding refresh when needed. | L332-L336; L397-L410 | [AGENTS.md](agents-remember-md/AGENTS.md) |
| The README presents C-08 as the active context resolver and C-02 as the drift classifier rather than the topology resolver. | L424-L430 | [README.md](agents-remember-md/README.md) |

## Build & Dev

- No `agents-remember-md`-specific build or test command is currently listed in the resolved shared [system/tools.md](ar-management/system/tools.md).
- The C-08, C-02, C-09, ledger, contract, and worktree-support test helpers use Python standard-library code and can be invoked directly with Python.
- This onboarding pass intentionally does not modify `system/sources.md` or `system/tools.md`.

## Key Invariants

- Onboarding should describe current repository state; task files describe planned or in-progress future work.
- C-08 owns topology and path resolution facts; it must not perform Git worktree operations.
- C-02 detects drift and writes reports under the resolved temporary artifact root; it must not update onboarding itself.
- C-05 creates and maintains onboarding artifacts; it must use actual evidence sources rather than citing source registries as proof.
- Task workflows must stop for developer approval before implementation.
- C-09 wraps task workflows with worktree lifecycle state; it does not replace W-02, does not integrate without explicit approval, and asks before cleanup after successful integration.
- C-10 is an adoption wrapper for existing shared-memory onboarding; it does not refresh onboarding and it does not overwrite an existing ledger.

## Glossary Terms

| Term | Meaning | Notes |
| --- | --- | --- |
| onboarding unit | A deterministic documentation unit for one source file or one repo-level entity catalog. | File-level units mirror source paths and carry verification metadata. |
| management context | The resolved root/path/settings facts returned by C-08 for a target repository. | Current implementation exposes `memory_root`, `coordination_root`, and `temp_root`; `management_root` remains only as a compatibility alias. |
| pathRules | Include/exclude eligibility rules that decide which source paths and file types are managed. | Storage and eligibility are separate concepts. |
| drift report | A C-02 maintenance artifact that classifies onboarding trust. | It is temporary evidence under `temp/drift-reports`, not durable repo behavior. |
| worktree contract | Local runtime state file for worktree-backed tasks. | The parser/writer lives in `_shared/agents_remember/worktree_contract.py`; C-09 creates and consumes contracts. |
| worktree integration | The approved C-09 phase that lands closed task work back onto source branches. | `ff-only` requires unchanged source ancestry; `replay` supports parallel non-overlapping work and blocks conflicts before main moves. |
| memory baseline adoption | The one-time action of turning current shared-memory onboarding into the first ledgered `memory.md` baseline. | C-10 checks drift first, requires explicit drift acceptance when needed, and delegates ledger creation to C-09. |

## Docs References

No relevant external domain documentation was found for this repository's own workflow mechanics. The resolved `Domain Documentation` registry is currently biased toward `resolve_auto_editor` technologies such as Resolve, Gemini, FastAPI, Pydantic, OTIO, FFmpeg, SQLite, and related libraries; those sources are not direct evidence for `agents-remember-md` repository behavior.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external documentation is needed to prove the repository's own current workflow structure; same-repository files are the direct evidence. | n/a | n/a |

## What To Explore Next

| Priority | Area / Path | Why Next |
| --- | --- | --- |
| high | [skills/U-01-core-skills/C-09-git-worktree-manager](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager) | Cleanup removal after successful integration still needs a helper path. |
| medium | [skills/W-01-heavy-task-workflow](agents-remember-md/skills/W-01-heavy-task-workflow) | Heavy workflow docs may need a separate onboarding pass if worktree-backed task folders become common outside W-02. |
| medium | [system](agents-remember-md/system) | Add richer settings fixtures if cross-repo v2 behavior needs more than the current example files. |

## Needs Verification

- The shared `ar-management/system/tools.md` currently lists checks for `resolve_auto_editor`, not this repo.
- The current source registry is useful as a discovery index but has no direct external domain evidence for this repo's own skill/workflow mechanics.
- Shared-memory onboarding for `agents-remember-md` is ledgered; future closeouts must keep the code-to-memory mapping current.

## Last Verified

Updated 2026-05-09T23:55 after adding C-09 integration for ff-only and replay landing of closed worktrees.
