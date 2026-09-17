# mcp/src/agents_remember/models/memory_content_excludes.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/memory_content_excludes.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-16T17:59+02:00 |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56` |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
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
| The staging helper that turns each name into `:(top,exclude)<name>` plus an `update-index --force-remove`. | `_excluded_pathspec`; `stage_worktree_content`; `commit_if_dirty` | mcp/src/agents_remember/worktrees/modules/git.py:34-35; mcp/src/agents_remember/worktrees/modules/git.py:191-198; mcp/src/agents_remember/worktrees/modules/git.py:200-208 |
| Producer 1 — baseline adoption consumes the constant on the call that stages. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/memory/baseline.py:239-239 |
| Producer 2 — memory carryover consumes the same constant in its apply path. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/memory/carryover.py:783-783 |
| Producer 3 — external closeout consumes it on the dirty check, the stage and the commit. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/worktrees/modules/closeout_external.py:93-93; mcp/src/agents_remember/worktrees/modules/closeout_external.py:106-106; mcp/src/agents_remember/worktrees/modules/closeout_external.py:110-110 |
| Producer 4 — direct landing consumes it on its memory commit. | `MEMORY_CONTENT_EXCLUDES` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_execution.py:236-236 |
| The two cases that fail if the exclusion becomes inert again. | `test_the_first_baseline_never_commits_bootstrap_scaffolding`; `test_no_memory_content_commit_stages_bootstrap_scaffolding` | mcp/tests/test_memory_branch_authority.py:469-492; mcp/tests/test_memory_branch_authority.py:495-512 |

## Cross-Repo References

No sibling-repository contract defines this exclusion policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **both governing declarations repaired.** The field named `../overview.md` and the body link named `../overview.md`; each resolved card-relatively to nothing, and they did not agree with each other. Both now name `overview.md`, the route-local overview of this card's own directory. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: created this card for the module the leaf added
  (`CAPS-R13@v1`, the absorbed `260820` onboarding-reform obligation that `bootstrap/` is never part
  of a memory commit). It records the two members, the names-not-pathspecs rule the module's own
  docstring states, the four producing seams that read it, and the two cases that fail if the
  exclusion goes inert again. Verification metadata is left at the leaf base commit because the
  source is uncommitted — the governed closeout stamps the real code commit, and no hash or
  fingerprint was invented here.
