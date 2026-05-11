# Entities

| Field       | Value                 |
| ----------- | --------------------- |
| repository  | agents-remember-md    |
| doc_type    | `repo-entity-catalog` |
| lastUpdated | 2026-05-11T18:34      |
| status      | active                |

## Purpose

This catalog documents load-bearing real entities in `agents-remember-md`. It is not a glossary of every workflow term and it does not catalog task files. Task files remain planning artifacts; this file describes current reusable repository concepts and the boundaries between them.

## Entity Inventory

### Onboarding Unit

| Field                        | Value                                                                                                                                                                                                                                                                                                                                |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Category                     | Documentation artifact                                                                                                                                                                                                                                                                                                               |
| Represents In Reality        | A durable unit of repository knowledge that can be retrieved and verified before an agent relies on it.                                                                                                                                                                                                                              |
| Description                  | File-level onboarding mirrors one concrete source file; repo-level catalogs document recurring entities.                                                                                                                                                                                                                             |
| Canonical Source Of Truth    | C-05 onboarding maintenance rules and the generated onboarding files under the resolved onboarding root.                                                                                                                                                                                                                             |
| Current Naming Drift         | Legacy shared-root onboarding still exists for migration, while current internal topology uses `ar-memory/` as durable memory.                                                                                                                                                                                                       |
| Key Identifiers              | `repository`, `path`, `doc_type`, `lastVerifiedCommitHash`, `lastVerifiedCommitDate`.                                                                                                                                                                                                                                                |
| Parent / Child Relationships | Lives under the onboarding root returned by C-08. File-level units mirror repo-relative source paths.                                                                                                                                                                                                                                |
| Often Confused With          | Task artifacts, roadmap specs, source registries, and temporary drift reports.                                                                                                                                                                                                                                                       |
| Source References            | [README.md](agents-remember-md/README.md) L57-L61; [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) L21-L33; [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) L28-L59 |
| Migration Notes              | The worktree-support stack should preserve one-to-one file-level mapping even as roots are renamed or split.                                                                                                                                                                                                                         |

### Coordination Context

| Field                        | Value                                                                                                                                                                                                                                                                                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Category                     | Resolver output contract                                                                                                                                                                                                                                                                               |
| Represents In Reality        | The resolved topology, roots, settings, storage rules, path rules, and cross-repo allowances for one code repository.                                                                                                                                                                                  |
| Description                  | C-08 produces this context so downstream skills do not rebuild topology rules.                                                                                                                                                                                                                         |
| Canonical Source Of Truth    | `C-08-ar-coordination-context-resolver` skill docs and helper output.                                                                                                                                                                                                                                            |
| Current Naming Drift         | None recorded for the C-08 resolver output contract.                                                                                                                                                                                                                                                   |
| Key Identifiers              | `topology`, `code_repository_name`, `code_repository_root`, `coordination_root`, `memory_root`, `onboarding_root`, `settings_path`, `path_settings_path`, `task_root`, `temp_root`, `pathRules`, `contract_path`, `worktree_group`, `ledger_path`.                                                     |
| Parent / Child Relationships | Consumed by C-02, C-05, C-03, and task workflows.                                                                                                                                                                                                                                                      |
| Often Confused With          | The onboarding root itself or the worktree task contract.                                                                                                                                                                                                                                              |
| Source References            | [C-08 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/SKILL.md) L24-L43; [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) L87-L111; L1087-L1147; L1216-L1264 |
| Migration Notes              | C-08 is now worktree-contract-aware but remains facts-only; C-09 owns mutation.                                                                                                                                                                                                                        |

### Path Rule

| Field                        | Value                                                                                                                                                                                                                               |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Settings and eligibility rule                                                                                                                                                                                                       |
| Represents In Reality        | Include/exclude rules that decide which source paths and file types are eligible for onboarding.                                                                                                                                    |
| Description                  | Path rules are parsed from JSON-first settings where possible and are evaluated separately from storage mode.                                                                                                                       |
| Canonical Source Of Truth    | C-08 settings parser plus README storage guidance.                                                                                                                                                                                  |
| Current Naming Drift         | Shared settings scope path rules per repository; unscoped rules can accidentally read as global defaults.                                                                                                                           |
| Key Identifiers              | `path`, `include.paths`, `include.fileTypes`, `exclude.paths`, `exclude.fileTypes`, `storage`.                                                                                                                                      |
| Parent / Child Relationships | Belongs to coordination context storage settings and influences C-02 classification.                                                                                                                                                |
| Often Confused With          | Storage mode; storage decides where artifacts live, path rules decide eligibility.                                                                                                                                                  |
| Source References            | [README.md](agents-remember-md/README.md) L122-L135; [ar_coordination_context_resolver.py](agents-remember-md/skills/U-01-core-skills/C-08-ar-coordination-context-resolver/scripts/ar_coordination_context_resolver.py) L249-L259; L585-L610 |
| Migration Notes              | Cross-repo/worktree changes should not replace path rules; they remain an eligibility layer.                                                                                                                                        |

### Drift Report

| Field                        | Value                                                                                                                                                                                                                                                                                                     |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Maintenance artifact                                                                                                                                                                                                                                                                                      |
| Represents In Reality        | C-02's report of onboarding trust against source-file verification metadata.                                                                                                                                                                                                                              |
| Description                  | Drift reports classify onboarding units as up to date, drifted, missing verification, missing, orphaned, disabled, or unsupported and are written under the resolved temporary artifact root by default.                                                                                                  |
| Canonical Source Of Truth    | C-02 skill docs and `check_onboarding_drift.py`.                                                                                                                                                                                                                                                          |
| Current Naming Drift         | The report used to default into task folders; current C-02 output places generated drift reports under `temp/drift-reports/<repo-name>/`.                                                                                                                                                                 |
| Key Identifiers              | report path, `classification`, `trust`, onboarding file path, source file path, affected sections, note.                                                                                                                                                                                                  |
| Parent / Child Relationships | Uses the C-08 context and hands actionable maintenance work to C-05.                                                                                                                                                                                                                                      |
| Often Confused With          | Onboarding content itself.                                                                                                                                                                                                                                                                                |
| Source References            | [C-02 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/SKILL.md) L16-L21; L41-L52; L112-L130; [check_onboarding_drift.py](agents-remember-md/skills/U-01-core-skills/C-02-onboarding-drift-detection/scripts/check_onboarding_drift.py) L62-L70; L106-L111; L570-L636 |
| Migration Notes              | Worktree support should preserve C-02 as detection/routing, not content writing.                                                                                                                                                                                                                          |

### File-Level Onboarding Content Model

| Field                        | Value                                                                                                                                                                                                                                                                             |
| ---------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Onboarding schema                                                                                                                                                                                                                                                                 |
| Represents In Reality        | The required section and citation model for one concrete source file's onboarding unit.                                                                                                                                                                                           |
| Description                  | The model includes purpose, code commentary, docs references, repo-internal references, cross-repo references, metadata, and append-only update history.                                                                                                                          |
| Canonical Source Of Truth    | C-05 file-level workflow and template.                                                                                                                                                                                                                                            |
| Current Naming Drift         | Inline onboarding reuses the same semantic content model; only storage adapter behavior differs.                                                                                                                                                                                  |
| Key Identifiers              | Metadata table fields plus required sections.                                                                                                                                                                                                                                     |
| Parent / Child Relationships | File-level units complement repo overview and entity catalog.                                                                                                                                                                                                                     |
| Often Confused With          | Component overviews or task-local findings.                                                                                                                                                                                                                                       |
| Source References            | [file-level workflow](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/workflows/file-level-onboarding-workflow.md) L48-L82; [C-05 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-05-create-or-update-onboarding-files/SKILL.md) L51-L64 |
| Migration Notes              | The content model should survive storage changes from sidecar to inline or shared roots.                                                                                                                                                                                          |

### Light Task Artifact

| Field                        | Value                                                                                                                                                                                                                                                               |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Workflow artifact                                                                                                                                                                                                                                                   |
| Represents In Reality        | A durable single-file plan/checklist for medium-sized work that needs approval and continuity.                                                                                                                                                                      |
| Description                  | W-02 creates or updates one task file under the C-08 resolved task root and uses checkboxes as the live implementation tracker.                                                                                                                                     |
| Canonical Source Of Truth    | W-02 skill docs, workflow, and template.                                                                                                                                                                                                                            |
| Current Naming Drift         | Worktree-backed tasks live beside `contract.md` in repo-scoped task folders; non-worktree W-02 artifacts can still use the resolved flat task root.                                                                                                                 |
| Key Identifiers              | `Status`, `Repo`, `Type`, `Created`, implementation checklist, decision log.                                                                                                                                                                                        |
| Parent / Child Relationships | Task artifacts can lead to onboarding updates, but they do not become onboarding content.                                                                                                                                                                           |
| Often Confused With          | Onboarding overview, entity catalog, and worktree contract.                                                                                                                                                                                                         |
| Source References            | [W-02 SKILL.md](agents-remember-md/skills/W-02-light-task-workflow/SKILL.md) L25-L34; [workflow.md](agents-remember-md/skills/W-02-light-task-workflow/workflow.md) L101-L139; [template.md](agents-remember-md/skills/W-02-light-task-workflow/template.md) L8-L86 |
| Migration Notes              | Worktree support should keep task artifacts as planning state, not durable current-state onboarding.                                                                                                                                                                |

### Shared Memory Ledger

| Field                        | Value                                                                                                                                                          |
| ---------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Memory compatibility artifact                                                                                                                                  |
| Represents In Reality        | The `memory.md` mapping between code commits and shared memory commits.                                                                                        |
| Description                  | The implemented helper parses and writes a fenced `json ar-memory-ledger` metadata block plus newest-first two-column commit table for shared memory branches. |
| Canonical Source Of Truth    | `_shared/agents_remember/memory_ledger.py` plus the worktree/shared-memory design spec.                                                                        |
| Current Naming Drift         | The parser/writer exists in `_shared/agents_remember/memory_ledger.py`; real shared memory repo bootstraps are still operationally new.                        |
| Key Identifiers              | `schema`, `trackedCodeBranch`, `memoryBranch`, `lastVerifiedCodeCommit`, `lastMemoryContentCommit`, table rows.                                                |
| Parent / Child Relationships | Belongs to one shared memory repo branch and is consumed by C-09 and cross-repo resolution.                                                                    |
| Often Confused With          | Drift report or task contract.                                                                                                                                 |
| Source References            | [worktree design spec](agents-remember-md/roadmap/agents-remember-worktree-memory-final-design-spec.md) L451-L557                                              |
| Migration Notes              | Git fixture coverage is still needed for full bootstrap and closeout integration beyond parser-level tests.                                                    |

### Memory Baseline Adoption

| Field                        | Value                                                                                                                                                                                                                                                         |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Shared-memory migration operation                                                                                                                                                                                                                             |
| Represents In Reality        | The explicit one-time conversion of existing shared-memory onboarding into the first ledgered `memory.md` baseline.                                                                                                                                           |
| Description                  | C-10 resolves the shared context, runs C-02 drift, reports ledger status, blocks actionable drift unless the developer accepts it, and then delegates Git initialization and ledger creation to C-09.                                                         |
| Canonical Source Of Truth    | `C-10-adopt-memory-baseline` skill and `adopt_memory_baseline.py`.                                                                                                                                                                                            |
| Current Naming Drift         | This is not onboarding refresh. It is ledger adoption for onboarding the developer already considers factual enough to trust.                                                                                                                                 |
| Key Identifiers              | `status`, `adopt`, `--accept-drift`, `ready`, `blocked-drift`, `already-ledgered`, `adopted`, `would-adopt`, `memory.md`.                                                                                                                                     |
| Parent / Child Relationships | Consumes the C-08 coordination context and C-02 drift rows; calls C-09 bootstrap to create the memory content and ledger commits.                                                                                                                             |
| Often Confused With          | C-05 onboarding maintenance, C-02 drift reports, and C-09 clean-start bootstrap during task worktree creation.                                                                                                                                                |
| Source References            | [C-10 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/SKILL.md) L8-L28; [adopt_memory_baseline.py](agents-remember-md/skills/U-01-core-skills/C-10-adopt-memory-baseline/scripts/adopt_memory_baseline.py) L53-L78; L138-L176 |
| Migration Notes              | When drift is actionable but the developer says the current onboarding is factual, run adoption with `--accept-drift`; otherwise refresh affected onboarding through C-05 first.                                                                              |

### Worktree Contract

| Field                        | Value                                                                                                                                                                                                                                                                         |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Runtime coordination artifact                                                                                                                                                                                                                                                 |
| Represents In Reality        | A local record of task identity, workflow artifact, worktree group, code worktree, memory worktree, ledger path, review state, closeout commits, integration commits, and cleanup state.                                                                                      |
| Description                  | The helper locates contracts under `ar-coordination/tasks/<repo-name>/<task-name>-ar/contract.md` and keeps them out of memory repos and worktrees.                                                                                                                             |
| Canonical Source Of Truth    | `_shared/agents_remember/worktree_contract.py` plus C-09.                                                                                                                                                                                                                     |
| Current Naming Drift         | The parser/writer exists in `_shared/agents_remember/worktree_contract.py`; it is not the same entity as a W-02 task file.                                                                                                                                                    |
| Key Identifiers              | `contract.md`, task id/name, worktree group, code worktree, memory worktree, ledger path, human review state, closeout commits, integration commits, cleanup state.                                                                                                           |
| Parent / Child Relationships | Owned by local coordinator and consumed by C-08/C-09 worktree-aware flows.                                                                                                                                                                                                    |
| Often Confused With          | Task artifact, onboarding unit, or memory ledger.                                                                                                                                                                                                                             |
| Source References            | [worktree_contract.py](agents-remember-md/skills/U-01-core-skills/_shared/agents_remember/worktree_contract.py) L16-L58; L211-L225; [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) L560-L654 |
| Migration Notes              | Task files should remain planning artifacts; contracts should record operational state. Closeout commits and integration commits are separate because replay can change landed SHAs.                                                                                          |

### Worktree Integration

| Field                        | Value                                                                                                                                                                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Worktree lifecycle phase                                                                                                                                                                                                                                                           |
| Represents In Reality        | The approved landing of closed task work from code and memory worktrees back onto their source branches.                                                                                                                                                                           |
| Description                  | C-09 `integrate` requires completed closeout and clean checkouts, supports `ff-only` for unchanged source ancestry, supports `replay` for parallel non-overlapping source movement, regenerates the memory ledger row for landed commits, and blocks conflicts before moving main. |
| Canonical Source Of Truth    | C-09 skill docs and `git_worktree_manager.py`.                                                                                                                                                                                                                                     |
| Current Naming Drift         | Integration is not cleanup. Cleanup is asked after successful integration and remains pending until explicitly approved.                                                                                                                                                           |
| Key Identifiers              | `integrate`, `--strategy ff-only`, `--strategy replay`, `integration.status`, `integrated_code_commit`, `integrated_memory_content_commit`, `integrated_ledger_commit`, `cleanup`.                                                                                                 |
| Parent / Child Relationships | Consumes the worktree contract closeout commits and writes integration result fields back to the same contract.                                                                                                                                                                    |
| Often Confused With          | Closeout commits, manual merge, push, or worktree deletion.                                                                                                                                                                                                                        |
| Source References            | [C-09 SKILL.md](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/SKILL.md) L53-L70; [git_worktree_manager.py](agents-remember-md/skills/U-01-core-skills/C-09-git-worktree-manager/scripts/git_worktree_manager.py) L560-L654                                  |
| Migration Notes              | Replay integration preserves parallel work support by producing new landed SHAs instead of pretending the closeout SHAs are still the source branch tips.                                                                                                                          |

### Branch-Gated Cross-Repo Source

| Field                        | Value                                                                                                                                                                              |
| ---------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Category                     | Cross-repo trust contract                                                                                                                                                          |
| Represents In Reality        | A configured external repository context source that is included only when branch and memory-ledger checks pass.                                                                   |
| Description                  | The resolver parses `crossRepo.allow` as strict v2 objects with `repo`, `expectedBranch`, `includeCode`, and `includeMemory`; legacy strings are excluded with a migration reason. |
| Canonical Source Of Truth    | C-08 resolver settings parsing and the cross-repo mode design spec.                                                                                                                |
| Current Naming Drift         | Legacy string allow entries are not branch-safe and should be treated as invalid in v2.                                                                                            |
| Key Identifiers              | `repo`, `expectedBranch`, `includeCode`, `includeMemory`, result state.                                                                                                            |
| Parent / Child Relationships | Uses committed memory settings, resolver context, worktree context, and memory ledger metadata.                                                                                    |
| Often Confused With          | Local coordinator path hints or implicit repository browsing.                                                                                                                      |
| Source References            | [cross-repo design spec](agents-remember-md/roadmap/agents-remember-cross-repo-mode-design-spec.md) L14-L34; L185-L217; L604-L648; L904-L907                                       |
| Migration Notes              | Cross-repo inclusion must remain read-only toward external repos.                                                                                                                  |

## Cross-Layer Projections

### Onboarding Unit

| Layer              | Representation                                                                         |
| ------------------ | -------------------------------------------------------------------------------------- |
| Repository source  | One concrete source file or repo-level entity set.                                     |
| Onboarding storage | Mirrored Markdown file or repo-level `entities.md` under the resolved onboarding root. |
| Drift detection    | Metadata fields compared against Git history.                                          |
| Agent workflow     | Read alongside source; update through C-05 when durable state changes.                 |

### Coordination Context

| Layer            | Representation                                                                   |
| ---------------- | -------------------------------------------------------------------------------- |
| Settings         | `system/settings.md` plus JSON-first `system/settings.json` when present.        |
| Resolver code    | `CoordinationContext` dataclass and JSON/text output.                            |
| Consumer skills  | C-02, C-03, C-05, and task workflows consume resolved roots instead of guessing. |
| Worktree support | Explicit memory, coordination, task, temp, worktree, contract, and ledger facts. |

### Light Task Artifact

| Layer            | Representation                                                                              |
| ---------------- | ------------------------------------------------------------------------------------------- |
| Planning         | Single Markdown task file under C-08 resolved task root.                                    |
| Implementation   | Checkbox checklist is the live execution state.                                             |
| Onboarding       | Durable current-state findings may be propagated to onboarding through C-05 after approval. |
| Worktree support | Lives beside `contract.md` for worktree-backed tasks.                                       |

### Memory Baseline Adoption

| Layer              | Representation                                                                                          |
| ------------------ | ------------------------------------------------------------------------------------------------------- |
| Developer decision | Current onboarding is either refreshed through C-05 or explicitly accepted despite drift.               |
| C-10 command       | `status` reports drift and ledger state; `adopt` creates the baseline only when allowed.                |
| C-09 mutation      | Bootstrap commits current memory content and writes the initial `memory.md`.                            |
| Future worktrees   | C-09 can use the ledger to decide whether shared memory is compatible with a selected code base commit. |

### Worktree Contract

| Layer             | Representation                                                |
| ----------------- | ------------------------------------------------------------- |
| Current repo      | Shared parser/writer and C-09 command consumer.               |
| Local coordinator | `ar-coordination/tasks/<repo-name>/<task-name>-ar/contract.md`. |
| C-08              | Facts-only contract reader.                                   |
| C-09              | Creator/updater and lifecycle owner.                          |

### Worktree Integration

| Layer              | Representation                                                               |
| ------------------ | ---------------------------------------------------------------------------- |
| Closeout snapshot  | Reviewed code, memory content, and ledger commits recorded in `closeout`.    |
| Integration replay | Optional code rebase and memory-content replay when source branches moved.   |
| Source branches    | Fast-forward only after integrated code and memory ledger commits are ready. |
| Cleanup            | Asked after success; not automatic.                                          |

## Ownership Notes

- This catalog intentionally excludes the eight worktree task files as onboarding subjects.
- Roadmap specs are cataloged only where they define active current design concepts that explain the repository's direction.
- Legacy roadmap specs remain historical context where they disagree with the implemented memory/coordination split.

## Update History

- 2026-05-09T23:55: Added worktree integration as a current lifecycle entity and updated contract fields for integration commits.
- 2026-05-11T19:01: Renamed the resolver entity to coordination context after C-08 moved its semantic API to coordination terminology.
- 2026-05-09T23:22: Updated coordination context and drift report entities after C-08 added `temp_root` and C-02 moved reports under `temp/drift-reports`.
- 2026-05-09T21:15: Created first `agents-remember-md` entity catalog for the preliminary onboarding baseline.
- 2026-05-09T22:10: Refreshed entity wording so ledger, contract, C-09, and cross-repo v2 are described as implemented current state.
- 2026-05-09T22:46: Added memory baseline adoption as the current-state entity introduced by C-10.
