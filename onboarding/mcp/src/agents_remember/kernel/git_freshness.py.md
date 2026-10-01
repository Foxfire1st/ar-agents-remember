# mcp/src/agents_remember/kernel/git_freshness.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`git_freshness.py` answers one lifecycle-long question for issue #54: is a
local branch current with its upstream? It is the shared freshness kernel
consumed by the `context_packet` freshness section (lifecycle-start
checkpoint) and intended for the `worktree_start` stale-base preflight and
`worktree_status`/`worktree_sync` (mid-task detection and sync) in the same
series.

## Code Commentary

The removed bare-origin test card adds no independent production rule: the source still handles no-branch/no-upstream, fetch errors, stale comparison counts, and current/ahead/behind/diverged outcomes explicitly. Source: mcp/src/agents_remember/kernel/git_freshness.py:120-164.

### Logic

`read_branch_freshness(repo_root, branch=None, *, fetch=True, fetch_timeout=30)`
resolves the branch (default: the checked-out branch), looks up its
remote-tracking ref via `upstream_ref` (`rev-parse --abbrev-ref
<branch>@{upstream}`), optionally runs one bounded `git fetch <remote>` via
`fetch_remote`, counts `ahead/behind` with `git rev-list --left-right --count
<local>...<upstream>`, and folds the result into a frozen `BranchFreshness`
dataclass with `state` one of: `current`, `behind`, `ahead`, `diverged`,
`no-upstream`, `no-branch` (detached HEAD), `unknown` (fetch failed or counts
unresolvable — counts from the stale tracking ref are still reported when
computable), or `unavailable` (git/filesystem error). `freshness_to_packet`
cit:([`freshness_to_packet`], mcp/src/agents_remember/kernel/git_freshness.py:167-178)
projects the dataclass into the context-packet dict, adding `error` only when set.

**This module declares the freshness vocabulary.** cit:([`FreshnessState`], mcp/src/agents_remember/kernel/git_freshness.py:30-39) is
the eight-member alias — four members reporting a comparison that succeeded, four
reporting why one could not be made — with `VALID_FRESHNESS_STATES` derived from
it by cit:([`get_args`], mcp/src/agents_remember/kernel/git_freshness.py:42-42). `BranchFreshness.state` is that alias, not `str`,
cit:([`BranchFreshness`], mcp/src/agents_remember/kernel/git_freshness.py:45-53)
and the computed fold in `_read_branch_freshness` is annotated
cit:(["current"], mcp/src/agents_remember/kernel/git_freshness.py:155-165). `models.context_packet.BranchFreshness.state`
**imports** it rather than keeping the hand-written eight-member copy it used to
hold. The asymmetry is what made that copy dangerous: `freshness_to_packet` hands
the wire boundary a plain dict, and half this vocabulary exists only on degrade
paths, so a copy would have been the last thing to hear about a new one — at
which point the mismatch surfaces as a pydantic `ValidationError` inside the
`context_packet` handler, which catches nothing.

### Conventions

Mirrors `git_facts.py`: frozen dataclass + `*_to_packet` projector. Every git
call now goes through the shared `run_git` from `kernel.git_command`,
**including the fetch**. `fetch_remote` used to hold a local `subprocess.run`
copy purely because `run_git`'s timeout was a fixed, unoverridable 5s; once the
runner gained a per-call timeout that copy had no reason to exist and
was deleted cit:([`fetch_remote`], mcp/src/agents_remember/kernel/git_freshness.py:68-82). It still passes its own
`DEFAULT_FETCH_TIMEOUT = 30`, cit:([`DEFAULT_FETCH_TIMEOUT`], mcp/src/agents_remember/kernel/git_freshness.py:24-24), which is now *shorter* than the runner's
`GIT_LOCAL_TIMEOUT_SECONDS = 300` default rather than longer than its old 5s:
the fetch is the only network call in this module, and 30s is the point past
which "still fetching" means "not coming back".

**The timeout class is chosen per command, not per module, and since 260913-LCA-L3 it travels
inside a `GitRunnerOptions` object** cit:([`GitRunnerOptions`], mcp/src/agents_remember/kernel/git_command.py:115-128)
rather than as a `timeout=` keyword. No call in this
file inherits the runner's default; each one names a band, and the code comments
carry the reasoning:

| Command | Call site | Bound |
| --- | --- | --- |
| `rev-parse --abbrev-ref <branch>@{upstream}` | `upstream_ref` | `GIT_METADATA_TIMEOUT_SECONDS` (30) — a local ref lookup, constant time |
| `branch --show-current` | `_read_branch_freshness` | `GIT_METADATA_TIMEOUT_SECONDS` (30) — constant time |
| `rev-list --left-right --count <local>...<other>` | `ahead_behind` | `GIT_LOCAL_TIMEOUT_SECONDS` (300) — walks history; how much depends on how far the refs drifted |
| `fetch <remote>` | `fetch_remote` | its own caller-supplied `timeout`, defaulting to `DEFAULT_FETCH_TIMEOUT = 30` — the one network call here |

`git_facts.py` classes its probes the same way. These explicit source arguments preserve the command-specific timeout boundary; the former timeout census test is no longer retained.

### Invariants And Boundaries

- The only repository mutation is the optional fetch of remote-tracking refs;
  the working tree and local branches are never touched.
- **cit:([`FreshnessState`], mcp/src/agents_remember/kernel/git_freshness.py:30-39) is the single declaration of this vocabulary.**
  `BranchFreshness.state` is typed with it and the context packet's wire model
  imports it. A ninth member — another degrade reason, most likely — is added
  here and nowhere else; a copy at the wire boundary would only be measured
  against this module when a real repository produced it.
- cit:([`VALID_FRESHNESS_STATES`], mcp/src/agents_remember/kernel/git_freshness.py:42-42) is derived by `get_args`, never listed
  separately. The removed vocabulary census is not current execution evidence.
- Errors degrade to data (`state` + `error`), never exceptions escaping to the
  caller — packet assembly must not fail because a remote is unreachable.
- `state="unknown"` (failed fetch) must never be treated as `behind` by
  callers; preflights warn on it but do not block.
- **Every `run_git` call in this file names its timeout; none inherits the
  runner's default.** There are exactly three non-fetch calls —
  `upstream_ref`, cit:([`upstream_ref`], mcp/src/agents_remember/kernel/git_freshness.py:56-65),
  and `branch --show-current` in `_read_branch_freshness`,
  cit:([`_read_branch_freshness`], mcp/src/agents_remember/kernel/git_freshness.py:120-164),
  at `GIT_METADATA_TIMEOUT_SECONDS` (30), and `ahead_behind`,
  cit:([`ahead_behind`], mcp/src/agents_remember/kernel/git_freshness.py:85-100),
  at `GIT_LOCAL_TIMEOUT_SECONDS` (300) — plus the fetch,
  cit:([`fetch_remote`], mcp/src/agents_remember/kernel/git_freshness.py:68-82), on its own 30s caller bound. Whichever bound trips, the result is still
  data, not an exception: `subprocess.TimeoutExpired` is a `SubprocessError`,
  which both `fetch_remote`, cit:([`fetch_remote`], mcp/src/agents_remember/kernel/git_freshness.py:68-82), and
  `read_branch_freshness`, cit:([`read_branch_freshness`], mcp/src/agents_remember/kernel/git_freshness.py:103-117), catch and
  turn into `state="unknown"`/`"unavailable"`.

### Todos

Sub-tasks B/D of the issue #54 series will consume this kernel from the
worktree modules; keep the API free of worktree-specific concepts.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

No relevant external documentation found.

### Repo-Internal References

- The local default bound is 300 seconds. [1]
- The ordinary remote bound is 120 seconds. [2]
- The metadata bound is 30 seconds. [3]
- The shared Git runner applies caller-selected bounds and isolated repository environment. [4]
- Style precedent: read-only git facts with dataclass + packet projector, the sibling that classes its four probes the same way, and — since 260731-EFA-L4 — the sibling that declares its own `RepoState` / `VALID_REPO_STATES` for the same reason this file declares `FreshnessState`. [5]
- The wire face that imports `FreshnessState` instead of retyping its eight members: `BranchFreshness.state`. [6]
- The context packet application entry point is the first consumer (`_freshness_packet`). [7]

### Cross-Repo References

No meaningful cross-repo references found.

No meaningful cross-repo references found.
