# mcp/src/agents_remember/kernel/git_facts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/git_facts.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:45+02:00|
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7`                         |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`git_facts.py` reads read-only Git facts for context-packet assembly: the repo's
branch, HEAD commit, dirty flag, and an availability state. It never mutates the
repository and degrades gracefully — any git or filesystem problem becomes a
`GitFacts` with `state="unavailable"` and an `error` string rather than an
exception escaping to the caller.

## Code Commentary

### Logic

`read_git_facts(repo_id, repo_root)` (L28-L33) resolves the path and delegates to
`_read_git_facts` (L36-L89), catching `OSError`/`SubprocessError` into an
`unavailable` `GitFacts`. `_read_git_facts` short-circuits to `unavailable` when
the path is missing, is not a directory, or is not a git work tree; otherwise it
reads HEAD (empty HEAD -> `unavailable`), the current branch, and
`status --porcelain` for the dirty flag. `state` is `available` when a branch is
present and `detached` when HEAD has no branch. `git_facts_to_packet` (L92-L103)
projects a `GitFacts` into the context-packet dict, adding `error` only when set.
`_git_stdout` (L106-L112) returns trimmed stdout or `""` on non-zero exit;
`_git_error` (L115-L116) picks the most informative of stderr/stdout/default.

### Conventions

All git calls go through the shared `run_git` runner imported from
`kernel/git_command.py` (F14) — this module no longer defines its own private
`_run_git`. Callers read `returncode`/`stdout` rather than relying on raises.

**Every call names its timeout class; none of them defaults.** The runner's
`timeout` keyword defaults to `GIT_LOCAL_TIMEOUT_SECONDS` (300), and inheriting
that default is what this module deliberately does not do: the timeout class
belongs to the command, not to the module the call sits in. `_git_stdout`'s
`timeout` is therefore **keyword-only and required** (L106), so no call site here
can silently take the 300s default — a new probe that forgets it is a
`TypeError`, not a five-minute hang.

The assignments (L58-L87), with the reasoning carried in the code comments:

| Command | Bound | Why |
| --- | --- | --- |
| `rev-parse --is-inside-work-tree` (L66-L68) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time (~1.8ms measured on this repo) |
| `rev-parse HEAD` (L80) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time |
| `branch --show-current` (L84) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time |
| `status --porcelain` (L87) | `GIT_LOCAL_TIMEOUT_SECONDS` (300) | **not** constant time — it stats the whole work tree |

The metadata band exists for exactly these reads because they sit under
`resolve_context`, which runs on essentially every tool call: on the local
default all four probes could hold one MCP call for twenty minutes behind a
stalled mount or a held index lock, with no cancellation path for the client.
`kernel/coordination_context/cross_repo.py` runs `branch --show-current` and
`rev-parse HEAD` at the same metadata bound, so one command means one bound
across `kernel/` — asserted by
`test_git_command.py::TimeoutClassTests::test_one_command_means_one_bound_across_the_kernel`.

### Invariants And Boundaries

- Read-only: this module never writes to the repository.
- Failure is data, not an exception: every error path returns a `GitFacts` with
  `state="unavailable"` and an `error` message. That still holds for a tripped
  bound: `subprocess.TimeoutExpired` is a `SubprocessError`, which
  `read_git_facts` (L32) catches into `state="unavailable"`.
- The git invocation flags, `safe.directory` isolation, the `GIT_DIR`-family
  selector stripping, and the DEVNULL stdin live in the shared `run_git` runner,
  not here. The **timeout class does not** — it is chosen per command at each
  call site in this file, because one number cannot bound both a `rev-parse` and
  a `status` over a large tree.
- `state` is exactly one of `available`, `detached`, or `unavailable`.

## Docs References

No external documentation is needed for this standard-library git-facts reader.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation is needed for git-facts assembly. | n/a | n/a |

## Repo-Internal References

The shared git runner and the context-packet consumer are the direct evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Git invocations are delegated to the shared `run_git` runner rather than a private wrapper. | imports `run_git` (L10-L14) | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| The three timeout bands this file selects from, and the `run_git` signature whose `timeout` defaults to `GIT_LOCAL_TIMEOUT_SECONDS = 300`. | `GIT_LOCAL_TIMEOUT_SECONDS` / `GIT_REMOTE_TIMEOUT_SECONDS` / `GIT_METADATA_TIMEOUT_SECONDS` L35-L55; `run_git` L67-L96 | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| The other kernel caller of `branch --show-current` and `rev-parse HEAD` names the same metadata bound, so one command means one bound. | `git_branch` / `git_head_or_empty` L21-L39 | [coordination_context/cross_repo.py](agents-remember/mcp/src/agents_remember/kernel/coordination_context/cross_repo.py) |
| The per-command bounds are asserted, not left to whichever module holds the call — including the cross-module comparison that fails on re-divergence. | `TimeoutClassTests` L543-L653; `test_read_git_facts_bounds_its_three_ref_reads_at_the_metadata_band` L575-L597; `test_one_command_means_one_bound_across_the_kernel` L623-L647 | [test_git_command.py](agents-remember/mcp/tests/test_git_command.py) |
| `git_facts_to_packet` output feeds the context packet's repo summary. | `read_git_facts` / `git_facts_to_packet` | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |

## Cross-Repo References

`read_git_facts` runs against whatever `repo_root` it is given, including sibling
code repos and external-memory repos, but its contract is local to this file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-31T21:20+02:00 — 260731-EFA-L3 curator: body corrected. The Invariants section said "the
  git invocation flags, `safe.directory` isolation, and **the 5-second timeout** live in the shared
  `run_git` runner, not here" — the 5s is gone (the runner's `timeout` keyword now defaults to
  `GIT_LOCAL_TIMEOUT_SECONDS = 300`), and the timeout no longer lives in the runner *for this file*
  at all: every call site names its own band. `_git_stdout` was re-signed to
  `(repo_root, args, *, timeout: float)` — keyword-only and **required** (L106) — so no call here can
  take the default by omission. Recorded the four assignments as a table: `rev-parse
  --is-inside-work-tree` (L66-L68), `rev-parse HEAD` (L80) and `branch --show-current` (L84) at
  `GIT_METADATA_TIMEOUT_SECONDS` (30); `status --porcelain` (L87) at `GIT_LOCAL_TIMEOUT_SECONDS`
  (300) because it stats the whole work tree. Added the surviving degrade-to-data note
  (`TimeoutExpired` is a `SubprocessError`, caught at L32). Citations: the Logic paragraph gained
  line ranges for all five functions (`read_git_facts` L28-L33, `_read_git_facts` L36-L89,
  `git_facts_to_packet` L92-L103, `_git_stdout` L106-L112, `_git_error` L115-L116) — the file grew
  from 98 to 116 lines this leaf; and three reference rows were added, pinning
  `git_command.py` L35-L55 (the three bands) + L67-L96 (`run_git`), `cross_repo.py` L21-L39
  (`git_branch`/`git_head_or_empty` at the same metadata bound), and `test_git_command.py`
  `TimeoutClassTests` L543-L653. Verification metadata pinned until closeout stamps the L3 commit.
- 2026-05-31T12:45+02:00 — Created during the 1.0.0 review remediation; git calls now go through the shared `kernel/git_command.run_git` runner (F14) instead of a private `_run_git`. (Pre-existing onboarding gap: this file had no sidecar before.)
