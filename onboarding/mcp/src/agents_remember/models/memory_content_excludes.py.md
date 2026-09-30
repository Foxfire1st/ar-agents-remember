# mcp/src/agents_remember/models/memory_content_excludes.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/memory_content_excludes.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-30T20:16:46+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea` |
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview      | `overview.md` |

## Governing Overview

[models overview](overview.md)

## Purpose

The one declaration of **what a memory-content commit never contains**. Four seams create
memory-content commits — baseline adoption, memory carryover, external closeout and direct
landing — and every one of them used to spell its own inline exclusion tuple. This module is the
lowest layer all four can read, so a fifth exclusion is added once instead of being missed in
three places.

The two members are real policy, not implementation detail:

- `memory.md` is the **computed ledger cache**, derived from the memory content and committed by
  its own transaction, so it is never carried along with the content it was computed from;
- `bootstrap/` is **transient bootstrap scaffolding** and is never part of a memory commit —
  neither the first baseline nor any later one.

## Code Commentary

### Logic

Three module constants and nothing else. `LEDGER_CACHE_RELATIVE_PATH` is `"memory.md"` and
`BOOTSTRAP_SCAFFOLDING_RELATIVE_PATH` is `"bootstrap"`; `MEMORY_CONTENT_EXCLUDES` is the
two-tuple every producing seam passes as `exclude_paths=`.

**They are worktree-relative path *names*, not Git pathspecs.** That distinction is the whole
reason this docstring exists and is the defect it was written from: the staging helpers take
names and build the pathspec themselves. `stage_worktree_content` runs
`git add -A -- . :(top,exclude)<name>` for each entry *and* `git update-index --force-remove --
<name>`; a pathspec string passed in here would be mangled into
`:(top,exclude):(exclude)bootstrap` and would silently match nothing.

The exclusion is only real because it rides the call that actually stages. `commit_if_dirty`
re-stages the whole worktree, so an exclusion applied to a bare `git add` *before* it is inert
and the file lands in the commit anyway — that was this leaf's baseline defect, and
`test_memory_branch_authority.py::test_the_first_baseline_never_commits_bootstrap_scaffolding`
fails if the old spelling returns.

### Conventions

- Adding an exclusion is a one-line change here plus no seam edit: the four producers already
  read this constant. That is the property the module exists to create.
- The declared name is the worktree-relative name. Never store a `:(...)` pathspec, and never
  store a glob.
- Exclusion means **excluded from the commit**, not deleted from the worktree: the developer's
  transient files stay on disk and show up as untracked content afterwards.

### Invariants And Boundaries

- A memory-content commit contains no `memory.md` and no `bootstrap/` path, on all four
  producing seams — first baseline, carryover, external closeout and direct landing.
- The constant is the only sanctioned source of those names. A literal `("memory.md",)` at a
  content-staging seam is the drift this module removes.
- Non-content staging seams (candidate-tree digests, cleanliness gates) keep their own narrower
  exclusions deliberately: widening them would change what "the memory worktree is clean" means
  for every other task.
- The staging helper takes names; this module must not start producing pathspecs.

### Todos

None recorded.

## Docs References

No external or domain documentation governs this repository-local exclusion policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The declared policy: the ledger cache, the bootstrap scaffolding, and their one tuple. | `LEDGER_CACHE_RELATIVE_PATH`; `BOOTSTRAP_SCAFFOLDING_RELATIVE_PATH`; `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/models/memory_content_excludes.py:26-26; mcp/src/agents_remember/models/memory_content_excludes.py:29-29; mcp/src/agents_remember/models/memory_content_excludes.py:32-35 |
| The staging helper that turns each name into `:(top,exclude)<name>` plus an `update-index --force-remove`. | `_excluded_pathspec`; `stage_worktree_content`; `commit_if_dirty` | mcp/src/agents_remember/worktrees/modules/git.py:34-35; mcp/src/agents_remember/worktrees/modules/git.py:191-197; mcp/src/agents_remember/worktrees/modules/git.py:200-207 |
| Producer 1 — baseline adoption consumes the constant on the call that stages. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/memory/baseline.py:239-239 |
| Producer 2 — memory carryover consumes the same constant in its apply path. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/memory/carryover.py:783-783 |
| Producer 3 — external closeout consumes it on the dirty check, the stage and the commit. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:159-159; mcp/src/agents_remember/worktrees/modules/closeout_external.py:178-178; mcp/src/agents_remember/worktrees/modules/closeout_external.py:182-182 |
| Since MIK-R09 the mandatory gate's exact-tree captures use it too (the closeout's `_refuse_invalid_memory_commit`, direct landing's `_memory_content_tree`), so the tree the gate validates is the tree the commit records. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:120-120; mcp/src/agents_remember/worktrees/direct_landing.py:610-610 |
| Producer 4 — direct landing consumes it on its memory commit. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:236-236 |
| The two cases that fail if the exclusion becomes inert again. | `test_the_first_baseline_never_commits_bootstrap_scaffolding`; `test_no_memory_content_commit_stages_bootstrap_scaffolding` | mcp/tests/test_memory_branch_authority.py:474-497; mcp/tests/test_memory_branch_authority.py:500-516 |

## Cross-Repo References

No sibling-repository contract defines this exclusion policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-30T20:16:46+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): No content impact on the constant: this card's own source is unchanged. MIK-R09 (260928-MIK-L09) moved `worktrees/modules/closeout_external.py`: the Producer-3 row, which the installed fixer could not project (its first line sits inside a changed hunk), was re-measured to the three consuming lines (`159`, `178`, `182`; the dirty check, the stage and the commit). **One row added:** the gate's exact-tree captures in the closeout and in direct landing consume the constant too, so the validated tree is the committed tree. No verification stamp was advanced.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **both governing declarations repaired.** The field named `../overview.md` and the body link named `../overview.md`; each resolved card-relatively to nothing, and they did not agree with each other. Both now name `overview.md`, the route-local overview of this card's own directory. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: created this card for the module the leaf added
  (`CAPS-R13@v1`, the absorbed `260820` onboarding-reform obligation that `bootstrap/` is never part
  of a memory commit). It records the two members, the names-not-pathspecs rule the module's own
  docstring states, the four producing seams that read it, and the two cases that fail if the
  exclusion goes inert again. Verification metadata is left at the leaf base commit because the
  source is uncommitted — the governed closeout stamps the real code commit, and no hash or
  fingerprint was invented here.
