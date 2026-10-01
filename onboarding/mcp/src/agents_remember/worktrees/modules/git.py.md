# mcp/src/agents_remember/worktrees/modules/git.py

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Provides shared repository/ref, candidate-tree, cleanliness, staging, committing, and changed-path
operations through the guarded kernel Git runner. Workflow admission remains with callers.

## Code Commentary

### Logic

`require_git` reports failed commands through transport-safe diagnostics while preserving the
runner's raw successful output. The removed local runner is not restored: repository-selector
scrubbing, standard-input ownership, encoding, and timeout policy stay in `kernel.git_command`.
Branch resolution uses explicit local refs, and repository identity uses Git's shared object store.

`worktree_candidate_tree(..., exclude_paths=())` uses a private temporary index per observation. It
seeds from HEAD, removes excluded entries before materialization, stages through an exclusion-aware
pathspec, writes the tree, and removes its scratch directory. The real index remains untouched.
The root cache uses `MEMORY_CACHE_EXCLUDE`; other explicit exclusions use their corresponding root
pathspecs. This avoids treating an ignored cache literal as an explicit add request.

`has_changes`, `worktree_dirty`, and `require_clean` accept the same explicit exclusions.
`contract_has_worktree_changes` excludes `memory.md` only on the memory side. Real content dirt
remains visible.

`stage_worktree_content` removes derived index entries and stages actual content without reading
those paths. `commit_if_dirty` creates an ordinary content commit when its filtered status is dirty.
`commit_verified_staged` operates on the already prepared index, removes explicitly excluded
entries, checks the staged diff, and commits with `--no-verify` without restaging. Neither helper
creates a commit for cache-only dirt. Hook execution remains a separate explicit helper.

Changed-path helpers retain their distinct semantics: existing-file worklists omit deletions, while
`changed_files_with_counts` reports additions/deletions, rename targets, counts, and binary-file
unknown counts for the serving change-set view.

### Conventions

Callers must supply exclusions for an owned derived artifact; this is not a blanket ignore rule for
all repositories. Candidate observations own separate scratch paths. Ordinary staging/committing and
verified-index committing remain deliberately separate APIs.

### Invariants And Boundaries

- All Git execution uses the guarded kernel runner and exact caller-selected repository.
- Cache-only dirt cannot trigger a memory-content commit when the caller supplies its exclusion.
- Real ref, ancestry, repository, and content checks are retained.
- Verified-index commit does not pull in later working-tree changes or rerun hooks.
- Exclusion never grants permission to move a protected ref or bypass workflow authority.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- Ref/repository identity and transport-safe errors have shared implementations. [1]
- Candidate trees use private indices and exact derived-path exclusions. [2]
- Filtered status and staging/commit APIs share the exclusion contract. [3]
- The exact cache pathspec is defined beside the consumer filename. [4]
- Changed-file reporting preserves its distinct deletion/rename/count semantics. [5]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
