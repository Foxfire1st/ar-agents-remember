# docs/workflows.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The workflow page: how a session routes by role, the discipline every build keeps, the three build
modes, and what is worktree-backed. It names modes and owners; the landing flow itself belongs to
the resolved memory's instruction file, which this page points at.

## Code Commentary

The page opens with routing: sessions go through `l-01-agent-lifecycles`, a role agent the product
started follows its handover, and any other session is developer-facing free chat — which answers a
question inline, or for a managed repository creates or resolves the sprint document, writes the
developer's request into it, starts an Architect with `role_start` naming no document, and tells the
developer where the work sits. It states the architect's phase axis (request, trust-checkpoint,
reframe-research, decide, build, close) and says the job type is a lens during reframe-research
rather than a gate, so the only task-format decision is the build-mode step. [1]

Historical source account (detached from live reference 2; docs/workflows.md blob 6e323e36091e8dbd6349c51e15e675f29cfc9149):

Shared Discipline lists the five rules every build keeps: resolve the active context, run drift
detection before planning against onboarding, wait for the developer's approval before
implementation, update onboarding live per completed plan section, and run the checks the resolved
memory's `system/tools.md` lists.

At `decide` the architect picks one of three modes. A research-only exit answers and changes no
code — no worktree, no task file, no closeout. A durable task takes the minimal leaf-task
artifact (`skills/l-01-agent-lifecycles/templates/leaf-task.md`), or the full form under
`ar-coordination/tasks/<repo>/<task-slug>/task.md`, whose checklist is the live execution state.
Work that outgrows one page escalates to a master plus light sub-task series: a wrapper task folder
with a canonical master JSON document and numbered leaf JSON documents rendered to Markdown;
ordinary leaves own paired code and memory worktree enclosures, an explicit direct-execution grant
can select the master checkout instead, and each slice keeps its own approval and landing gates. [3]

Worktree-backed tasks follow the ladder task doc (approved) → branch (intent) → worktree (only what
is built), created by the `worktree_start` tool. The canonical contract is `series-contract.md`, at
the master task folder or at `enclosures/<leaf>/` for a leaf enclosure; ordinary leaves have their
own paired code and memory worktrees, and a direct-execution grant binds a leaf to the master
checkout instead. Closeout and commit approval are separate from implementation approval, and the
landing flow — direct or pull-request gated — is deferred to the repository's
`system/task-publication.md` when present, together with the `landing.workflow` setting that decides
which of the two the repository runs. [4]

The page closes with a table mapping five situations to a build mode. [5]

## Evidence

### Repo-Internal References

- The source describes the routing paragraph as summarized above. [1]
Historical source account (detached from live reference 2; docs/workflows.md blob 6e323e36091e8dbd6349c51e15e675f29cfc9149):

- The source lists the five shared-discipline rules.

- Shared Discipline now puts current card, sidecar and knowledge-record curation against approved changes in the leaf memory worktree before publication, alongside context, drift, implementation approval and configured checks. Knowledge in a Leaf separately requires fresh full quality/worklist/gate evidence and validated coherence without granting Git approval.

- The source names the three build modes and what each produces. [3]

- The source states the worktree ladder and defers landing to `system/task-publication.md` with the `landing.workflow` setting. [4]

- The source's closing table maps situations to build modes. [5]

- Shared Discipline puts current card, sidecar and knowledge-record curation against approved changes in the leaf memory worktree before publication, alongside context, drift, implementation approval and configured checks. Knowledge in a Leaf separately requires fresh full quality/worklist/gate evidence and validated coherence without granting Git approval. [2]
