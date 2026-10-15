# skills/c-08-ar-coordination-context-resolver/SKILL.md

## Governing Overview

[overview.md](../../overview.md)

## Purpose

The authored resolver skill explains how a configured repository acquires one external-memory coordination context and where downstream consumers obtain roots, settings and metadata. It separates internal/package context facts from the slim mounted context_packet answer and excludes scaffolding and worktree mutation from resolution.

## Commentary

### Repository identity and explicit inputs

The normal input is code_repository_name, with optional workspace/root/settings/topology/contract/task selectors for explicit cases. Task-name lookup excludes 0_archive; root contracts use <task>/series-contract.md and leaf contracts use <task>/enclosures/<leaf-id>/series-contract.md. parent_task disambiguates nested names and leaf_id selects an enclosure. With no task name, task_root is the repository task namespace. These names describe source contracts, not a request to resolve this workspace or infer a live task.

### External topology and fail-closed roots

Only external is supported. Resolution validates an explicit onboarding override under the named external memory root, applies contract coordination before memory validation, and uses explicit/installed/development coordination inputs as documented. Removed internal or repository-local ar-memory artifacts refuse by name, without falling through to external. A missing external root produces a named missing-memory error; the skill’s suggestion to seek initialization approval is not automatic creation. Each repository binds its own memory rather than moving siblings.

### Mounted roots versus source-bound settings

The normal installed route is context_packet; resolve_context is removed. A canonical leaf supplies task_document_ref and contract_path so admitted enclosure roots identify its code and memory worktrees. The compact answer names roots, task/master, action states, serving build and pair identity, not full settings blocks. system/settings.md and its preferred sibling JSON carry settings/storage/pathRules/crossRepo; server_info is the metadata route for code roots and build identity. Read the named authorities rather than reconstructing a parallel resolver from a checkout path.

### Read side effects and authority boundaries

include_freshness fetches remotes and therefore can write; include_drift measures anchors. Context resolution itself reads settings/filesystem and has no provider prerequisite. Delegation policy lives in the user’s own settings, not a coordinator policy-file prerequisite. Fixed paths derive from admitted roots only; the source explicitly permits no invented settings or ledger paths when source-bound locations are needed.

### Consumers and non-mutation boundary

MQC consumes context and owns quality checks; bootstrap/retrieval/onboarding/task workflows consume roots; c-09 owns Git/worktree lifecycle mutation. The skill tree is instruction-only and package/MCP routes implement resolution. The old example todo, crossRepo-v2 wording, .env exclusion and private implementation reference remain scoped inheritance, not newly inspected implementation facts or a claim that worktree examples are still missing.

### Scoped inherited commentary and evidence

The following inherited account is retained for commentary, migration history, todos and evidence meaning. It is not wholesale re-certified. Its uses of “current”, “now”, dates, milestones, tool names, command examples, topology descriptions, implementation claims or verification stamps describe that inherited account only. The source-grounded account above and evidence table below own newly authored claims. Historical reference numbers are not converted reference identities: original reference identities remain historical, not freshly allocated identities for the current evidence. This retained body creates no role, task, permission, live-build or execution authority.

> **Inherited heading: c-08-ar-coordination-context-resolver/SKILL.md**
>
> **Inherited heading: Current source contract evidence**
>
> - Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance.
>
> **Inherited heading: Purpose**
>
> This skill defines `c-08-ar-coordination-context-resolver` skill, the authoritative facts-only resolver for memory roots, coordination roots, settings, path rules, task roots, temporary artifact roots, worktree contract fields, ledger paths, and branch-gated cross-repo allowances.
>
> **Inherited heading: Code Commentary**
>
> **Inherited heading: Logic**
>
> For installed MCP callers, `resolve_context` is removed: request `context_packet` with repo_id and optional drift/freshness/task_context. A canonical leaf passes task_document_ref plus contract_path; admitted roots bind its code/memory worktrees. The slim answer names roots, task/master, actions, serving build and pair commits, not settings/storage/pathRules/crossRepo blocks. Read those source-bound settings files (JSON preferred, Markdown fallback); use server_info for metadata/code roots. Private package resolution still owns topology and full CoordinationContext facts. `include_freshness` can fetch/write and is not evidence of a purely read-only tool.
>
> The skill tells agents to resolve context once and pass the resulting facts downstream instead of re-deriving topology in every workflow. It documents `code_repository_name`, `code_repository_root`, `coordination_root`, `memory_root`, `task_root`, `temp_root`, optional contract/worktree fields, JSON-first settings, path rules, storage settings, and cross-repo v2 result states. Without `task_name`, `task_root` is the repo-specific task namespace under `ar-coordination/tasks/<code-repository-name>/`; with `task_name` or a contract, it is the concrete task folder. Normal installed workflows resolve the coordination root from MCP settings; package-local resolver calls use explicit input, an installed runtime root, or the source-development `../ar-coordination` default. Source-checkout `.env` and `.env.example` files are not resolver inputs. Resolution validates supported memory locations and fails with a missing-memory error instead of inventing an empty context.
>
> **Inherited heading: Conventions**
>
> `c-08-ar-coordination-context-resolver` skill is facts-only. It may report worktree-related context from a contract, but creation or mutation of worktrees belongs to `c-09-git-worktree-manager` skill.
>
> **Inherited heading: Invariants And Boundaries**
>
> Consumers should rely on `c-08-ar-coordination-context-resolver` skill for paths and topology. They should not infer onboarding roots from current working directory names. `c-08-ar-coordination-context-resolver` skill does not create onboarding content, drift reports, or worktree state.
>
> **Inherited heading: Todos**
>
> Add more examples after the first real worktree-backed task contract exists in the workspace.
>
> **Inherited heading: Docs References**
>
> No external domain documentation applies to this repository-local skill contract.
>
> No relevant external documentation found.
>
> **Inherited heading: Evidence**
>
> **Inherited heading: Repo-Internal References**
>
> `c-08-ar-coordination-context-resolver` skill is the base dependency for `c-02-memory-quality-control` skill, `c-03-repo-bootstrap` skill, `c-04-retrieval-strategy-router` skill, `c-05-create-or-update-onboarding-files` skill, and task workflows.
>
> - The skill accepts `code_repository_name`, optional `code_repository_root`, and `task_name`; no-task-name contexts resolve the repo task namespace, while task-name contexts resolve current wrapper task folders and persisted `*-ar` contract folders.
> - The skill returns topology, code repository identity/root, settings paths, repo/task-specific task roots, temp/docs/system roots, worktree fields, ledger path, path rules, and cross-repo data.
> - Resolution rules validate explicit onboarding roots, load worktree contract coordination first, use MCP settings or explicit/installed/default package roots for coordination, require supported memory roots, and fail clearly when no memory exists. A removed `internal` request or a repo-local `ar-memory/` root is refused by name with `memory-mode-unsupported`, never falling through to the external root; `external` is the only supported topology.
> - Consumers include `c-02-memory-quality-control` skill, `c-03-repo-bootstrap` skill, c-04-retrieval-strategy-router, `c-05-create-or-update-onboarding-files` skill, task workflows, and `c-09-git-worktree-manager` skill; boundaries keep `c-08-ar-coordination-context-resolver` skill out of mutation work.
> - The private package context retains code_repository_name/code_repository_root and the full resolver facts; the mounted context_packet exposes slim roots/actions, with settings from file reads and metadata from server_info.
>
> **Inherited heading: Cross-Repo References**
>
> `c-08-ar-coordination-context-resolver` skill may read coordinator settings, but no external repository behavior is required to understand this skill's current contract.
>
> No meaningful cross-repo references found for current skill semantics.
>
> **Inherited heading: Series-Contract Notes**
>
> The packaged resolver skill now teaches active task-name lookup, optional `parent_task` disambiguation, optional `leaf_id` selection, and root/leaf `series-contract.md` paths so installed runtimes do not look for `contract.md`.

### Scoped inherited companion commentary

These are the old companion’s explanatory notes, retained as historical evidence descriptions rather than freshly validated targets. Original anchor objects, source paths, blobs, digests and locator values remain unchanged in input custody; they are not re-authored here.

> The skill accepts `code_repository_name`, optional `code_repository_root`, and `task_name`; no-task-name contexts resolve the repo task namespace, while task-name contexts resolve current wrapper task folders and persisted `*-ar` contract folders.

> The skill returns topology, code repository identity/root, settings paths, repo/task-specific task roots, temp/docs/system roots, worktree fields, ledger path, path rules, and cross-repo data.

> Resolution rules validate explicit onboarding roots, load worktree contract coordination first, use MCP settings or explicit/installed/default package roots for coordination, require supported memory roots, and fail clearly when no memory exists. A removed `internal` request or a repo-local `ar-memory/` root is refused by name with `memory-mode-unsupported`, never falling through to the external root; `external` is the only supported topology.

> Consumers include `c-02-memory-quality-control` skill, `c-03-repo-bootstrap` skill, c-04-retrieval-strategy-router, `c-05-create-or-update-onboarding-files` skill, task workflows, and `c-09-git-worktree-manager` skill; boundaries keep `c-08-ar-coordination-context-resolver` skill out of mutation work.

> The package implementation exposes the same `code_repository_name` and `code_repository_root` fields through `CoordinationContext`, context construction, and MCP/JSON output.

> Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance.

## Evidence

The following references support the source-contract commentary, not fresh runtime acceptance. Canonical authored source owns the contract; the inspected package copy is an equal distribution twin only. Root overview ownership context is onboarding/overview.md, especially its construction/ownership and retained naming-versus-reading doctrine. The description of a source contract is not runtime acceptance or permission to execute its operations.

- Identity and normal repository-name contract [1]
- Inputs, series-contract layout and JSON preference [2]
- Full context outputs and distinct settings/metadata sources [3]
- External-only rules, named refusals and per-repository roots [4]
- Normal context_packet route and freshness write caveat [5]
- Admitted roots, compact answer and removed resolver [6]
- Delegation policy location and instruction-only tree [7]
- Downstream quality, retrieval and worktree consumers [8]
- Single resolver ownership and creation/mutation exclusions [9]
