# mcp/src/agents_remember/kernel/git_facts.py

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

cit:([`read_git_facts`], mcp/src/agents_remember/kernel/git_facts.py:41-46) resolves the path and delegates to
cit:([`_read_git_facts`], mcp/src/agents_remember/kernel/git_facts.py:49-104), catching `OSError`/`SubprocessError` into an
`unavailable` `GitFacts`. `_read_git_facts` short-circuits to `unavailable` when
the path is missing, is not a directory, or is not a git work tree; otherwise it
reads HEAD (empty HEAD -> `unavailable`), the current branch, and
`status --porcelain` for the dirty flag. `state` is `available` when a branch is
present and `detached` when HEAD has no branch (L103).
cit:([`git_facts_to_packet`], mcp/src/agents_remember/kernel/git_facts.py:107-118)
projects a `GitFacts` into the context-packet dict, adding `error` only when set.
cit:([`_git_stdout`], mcp/src/agents_remember/kernel/git_facts.py:121-131) returns trimmed stdout or `""` on non-zero exit;
cit:([`_git_error`], mcp/src/agents_remember/kernel/git_facts.py:134-135) picks the most informative of stderr/stdout/default.

**This module declares the repo-availability vocabulary.** `RepoState = Literal["available",
"detached", "unavailable"]` with `VALID_REPO_STATES` derived from it by `get_args`.
`GitFacts.state` is that alias, not `str`, and the one computed assignment is annotated
`state: RepoState` so the checker sees it. The wire face —
`models.context_packet.RepoSummary.state` — **imports** this alias instead of retyping it.
That matters because the packet builds that block as
`RepoSummary.model_validate(git_facts_to_packet(...))` over an untyped dict: a hand-written copy
at the boundary is invisible until a real repo produces the new member, and by then it is a
pydantic `ValidationError` raised inside a tool handler with no `except` for one. That is the
failure mode 165 of the 213 `series-contract.md` files on disk were reproducing across the
package's seven vocabulary gaps.

### Conventions

All git calls go through the shared `run_git` runner imported from
`kernel/git_command.py` (F14) — this module no longer defines its own private
`_run_git`. Callers read `returncode`/`stdout` rather than relying on raises.

**Every call names its timeout class; none of them defaults.** `GitRunnerOptions.timeout`
cit:([`GitRunnerOptions`], mcp/src/agents_remember/kernel/git_command.py:115-128) defaults to
`GIT_LOCAL_TIMEOUT_SECONDS` (300), and inheriting that default is what this module deliberately does
not do: the timeout class belongs to the command, not to the module the call sits in. `_git_stdout`'s
`timeout` is therefore **keyword-only and required** (L121), so no call site here can silently take
the 300s default — a new probe that forgets it is a `TypeError`, not a five-minute hang.

The assignments (cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:149-213)), with the reasoning carried in the code comments:

| Command | Bound | Why |
| --- | --- | --- |
| `rev-parse --is-inside-work-tree` (L79-L83) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time (~1.8ms measured on this repo) |
| `rev-parse HEAD` (L95) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time |
| `branch --show-current` (L99) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time |
| `status --porcelain` (L102) | `GIT_LOCAL_TIMEOUT_SECONDS` (300) | **not** constant time — it stats the whole work tree |

The metadata band exists for exactly these reads because they sit under
`resolve_context`, which runs on essentially every tool call: on the local
default all four probes could hold one MCP call for twenty minutes behind a
stalled mount or a held index lock, with no cancellation path for the client.
`kernel/coordination_context/cross_repo.py` runs `branch --show-current` and
`rev-parse HEAD` at the same metadata bound, so one command means one bound
across these callers. The former cross-module timeout comparison suite was retired;
the current call sites and canonical constants own the contract.

### Invariants And Boundaries

- Read-only: this module never writes to the repository.
- Failure is data, not an exception: every error path returns a `GitFacts` with
  `state="unavailable"` and an `error` message. That still holds for a tripped
  bound: `subprocess.TimeoutExpired` is a `SubprocessError`, which
  `read_git_facts` (cit:([`SubprocessError`], mcp/src/agents_remember/kernel/git_facts.py:45-45)) catches into `state="unavailable"`.
- The git invocation flags, `safe.directory` isolation, the `GIT_DIR`-family
  selector stripping, and the DEVNULL stdin live in the shared `run_git` runner,
  not here. The **timeout class does not** — it is chosen per command at each
  call site in this file, because one number cannot bound both a `rev-parse` and
  a `status` over a large tree.
- `state` is exactly one of `available`, `detached`, or `unavailable`, and that
  is now enforced by a type rather than by prose: cit:([`RepoState`], mcp/src/agents_remember/kernel/git_facts.py:23-23) is the single
  declaration, `GitFacts.state` is typed with it, and the context packet's
  `RepoSummary.state` imports it. **A new degrade path must add its member here,
  not at the wire model** — the whole point is that there is no second set to
  add it to.
- cit:([`VALID_REPO_STATES`], mcp/src/agents_remember/kernel/git_facts.py:27-27) is derived from the alias by `get_args`, never listed
  separately, and the exhaustiveness suite asserts the set this module actually
  produces equals it — which also catches a declared member no writer can emit.

## Evidence

### Docs References

No external documentation is needed for this standard-library git-facts reader.

No relevant external documentation is needed for git-facts assembly.

### Repo-Internal References

The shared git runner and the context-packet consumer are the direct evidence.

- Git invocations are delegated to the shared `run_git` runner rather than a private wrapper. [1]
- The local default bound is 300 seconds. [2]
- The ordinary remote bound is 120 seconds. [3]
- The metadata bound is 30 seconds. [4]
- The shared Git runner applies caller-selected bounds and isolated repository environment. [5]
- The other kernel caller of `branch --show-current` and `rev-parse HEAD` names the same metadata bound, so one command means one bound. [6]

| `git_facts_to_packet` output feeds the context packet's repo summary. | "git_facts = read_git_facts(" | mcp/src/agents_remember/application/context_packet.py:85-85 |
| The wire face that imports `RepoState` instead of retyping it — the untyped-dict boundary this alias exists to close. | "state: RepoState" | mcp/src/agents_remember/models/context_packet.py:26-26 |


### Cross-Repo References

`read_git_facts` runs against whatever `repo_root` it is given, including sibling
code repos and external-memory repos, but its contract is local to this file.

No meaningful cross-repo references found.
