# mcp/src/agents_remember/kernel/git_facts.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/git_facts.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00 |
| lastVerifiedCommitHash | `c9ae4dbd8adb650f116b9d4f86343b496c3e5f32`                         |
| lastVerifiedCommitDate | 2026-08-12T17:53:40+02:00|
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

cit:([`read_git_facts`], mcp/src/agents_remember/kernel/git_facts.py:40-45) resolves the path and delegates to
cit:([`_read_git_facts`], mcp/src/agents_remember/kernel/git_facts.py:48-101), catching `OSError`/`SubprocessError` into an
`unavailable` `GitFacts`. `_read_git_facts` short-circuits to `unavailable` when
the path is missing, is not a directory, or is not a git work tree; otherwise it
reads HEAD (empty HEAD -> `unavailable`), the current branch, and
`status --porcelain` for the dirty flag. `state` is `available` when a branch is
present and `detached` when HEAD has no branch (L100).
cit:([`git_facts_to_packet`], mcp/src/agents_remember/kernel/git_facts.py:104-115)
projects a `GitFacts` into the context-packet dict, adding `error` only when set.
cit:([`_git_stdout`], mcp/src/agents_remember/kernel/git_facts.py:118-124) returns trimmed stdout or `""` on non-zero exit;
cit:([`_git_error`], mcp/src/agents_remember/kernel/git_facts.py:127-128) picks the most informative of stderr/stdout/default.

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

**Every call names its timeout class; none of them defaults.** The runner's
`timeout` keyword defaults to `GIT_LOCAL_TIMEOUT_SECONDS` (300), and inheriting
that default is what this module deliberately does not do: the timeout class
belongs to the command, not to the module the call sits in. `_git_stdout`'s
`timeout` is therefore **keyword-only and required** (L118), so no call site here
can silently take the 300s default — a new probe that forgets it is a
`TypeError`, not a five-minute hang.

The assignments (cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:85-151)), with the reasoning carried in the code comments:

| Command | Bound | Why |
| --- | --- | --- |
| `rev-parse --is-inside-work-tree` (L78-L80) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time (~1.8ms measured on this repo) |
| `rev-parse HEAD` (L92) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time |
| `branch --show-current` (L96) | `GIT_METADATA_TIMEOUT_SECONDS` (30) | constant time |
| `status --porcelain` (L99) | `GIT_LOCAL_TIMEOUT_SECONDS` (300) | **not** constant time — it stats the whole work tree |

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
  `read_git_facts` (cit:([`SubprocessError`], mcp/src/agents_remember/kernel/git_facts.py:44-44)) catches into `state="unavailable"`.
- The git invocation flags, `safe.directory` isolation, the `GIT_DIR`-family
  selector stripping, and the DEVNULL stdin live in the shared `run_git` runner,
  not here. The **timeout class does not** — it is chosen per command at each
  call site in this file, because one number cannot bound both a `rev-parse` and
  a `status` over a large tree.
- `state` is exactly one of `available`, `detached`, or `unavailable`, and that
  is now enforced by a type rather than by prose: cit:([`RepoState`], mcp/src/agents_remember/kernel/git_facts.py:22-22) is the single
  declaration, `GitFacts.state` is typed with it, and the context packet's
  `RepoSummary.state` imports it. **A new degrade path must add its member here,
  not at the wire model** — the whole point is that there is no second set to
  add it to.
- cit:([`VALID_REPO_STATES`], mcp/src/agents_remember/kernel/git_facts.py:26-26) is derived from the alias by `get_args`, never listed
  separately, and the exhaustiveness suite asserts the set this module actually
  produces equals it — which also catches a declared member no writer can emit.

## Docs References

No external documentation is needed for this standard-library git-facts reader.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed for git-facts assembly. | n/a | n/a |

## Repo-Internal References

The shared git runner and the context-packet consumer are the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Git invocations are delegated to the shared `run_git` runner rather than a private wrapper. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:85-151 |
| The three timeout bands this file selects from, and the `run_git` signature whose `timeout` defaults to `GIT_LOCAL_TIMEOUT_SECONDS = 300`. | `GIT_LOCAL_TIMEOUT_SECONDS`; `GIT_REMOTE_TIMEOUT_SECONDS`; `GIT_METADATA_TIMEOUT_SECONDS`; `run_git` | mcp/src/agents_remember/kernel/git_command.py:71-73; mcp/src/agents_remember/kernel/git_command.py:94-145 |
| The other kernel caller of `branch --show-current` and `rev-parse HEAD` names the same metadata bound, so one command means one bound. | `git_branch`; `git_head_or_empty` | mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:21-29; mcp/src/agents_remember/kernel/coordination_context/cross_repo.py:32-38 |
| The per-command bounds are asserted, not left to whichever module holds the call — including the cross-module comparison that fails on re-divergence. | `TimeoutClassTests`; `test_read_git_facts_bounds_its_three_ref_reads_at_the_metadata_band`; `test_one_command_means_one_bound_across_the_kernel` | mcp/tests/test_git_command.py:613-723 |
| `git_facts_to_packet` output feeds the context packet's repo summary. | "git_facts = read_git_facts(" | mcp/src/agents_remember/application/context_packet.py:85-85 |
| The wire face that imports `RepoState` instead of retyping it — the untyped-dict boundary this alias exists to close. | "state: RepoState" | mcp/src/agents_remember/models/context_packet.py:26-26 |
| `test_every_repo_state_the_git_facts_reader_writes_validates` asserts produced == `VALID_REPO_STATES`; `test_an_absent_repo_crosses_the_wire_as_unavailable` walks a real degrade through `RepoSummary`. | `ProducedLiteralTests`; `ProducerWireCrossingTests` | mcp/tests/test_wire_vocabulary_exhaustiveness.py:632-817; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:447-474 |

## Cross-Repo References

`read_git_facts` runs against whatever `repo_root` it is given, including sibling
code repos and external-memory repos, but its contract is local to this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-03T02:49:35+02:00 — W3-B05 curator: resolved 15 Tier-2 prose findings into 12 exact prose citations with exact source paths; fixer generated all ranges.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:52+02:00 — 260731-EFA-L4 curator: body updated and every self-citation
  re-derived. This module now DECLARES `RepoState = Literal["available", "detached",
  "unavailable"]` with `VALID_REPO_STATES` derived by `get_args`; `GitFacts.state`
  changed from `str` to that alias and the computed assignment is annotated
  `state: RepoState`. `models.context_packet.RepoSummary.state` imports it rather than
  keeping the hand-written copy it used to hold — the copy that could only ever be measured
  against this module when a real repo produced a new member, as a `ValidationError` inside a
  tool handler with no `except` for one. The card's `state` invariant asserted the three values
  in prose; it now names the type that enforces them and says where a fourth member must be
  added. Citations: the file grew 116 → 128 lines and everything below the new alias block moved
  +12, so all eleven self-citations were re-derived — `read_git_facts` L28-L33 → L40-L45,
  `_read_git_facts` L36-L89 → L48-L101, `git_facts_to_packet` L92-L103 → L104-L115, `_git_stdout`
  L106-L112 → L118-L124 (and its required-keyword `timeout` L106 → L118), `_git_error` L115-L116
  → L127-L128, the assignments block L58-L87 → L70-L99, `rev-parse --is-inside-work-tree`
  L66-L68 → L78-L80, `rev-parse HEAD` L80 → L92, `branch --show-current` L84 → L96,
  `status --porcelain` L87 → L99, and the degrade-catch L32 → L44. The `run_git` import row
  (cit:([`run_git`], mcp/src/agents_remember/kernel/git_command.py:85-151)) was re-checked and still lands. The `context_packet.py` row gained
  `read_git_facts` L77 / the `model_validate` call L81, and rows were added for
  `models/context_packet.py` (L9, L27) and the exhaustiveness suite. Verification metadata
  pinned until closeout stamps the L4 commit.
- 2026-07-31T21:20+02:00 — 260731-EFA-L3 curator: body corrected. The Invariants section said "the
  git invocation flags, `safe.directory` isolation, and **the 5-second timeout** live in the shared
  `run_git` runner, not here" — the 5s is gone (the runner's `timeout` keyword now defaults to
  `GIT_LOCAL_TIMEOUT_SECONDS = 300`), and the timeout no longer lives in the runner *for this file*
  at all: every call site names its own band. `_git_stdout` was re-signed to
  `(repo_root, args, *, timeout: float)` — keyword-only and **required** (L106) — so no call here can
  take the default by omission. Recorded the four assignments as a table: `rev-parse
  --is-inside-work-tree`, `rev-parse HEAD` and `branch --show-current` at
  `GIT_METADATA_TIMEOUT_SECONDS` (30) (cit:([`GIT_METADATA_TIMEOUT_SECONDS`], mcp/src/agents_remember/kernel/git_command.py:73-73)); `status --porcelain` at `GIT_LOCAL_TIMEOUT_SECONDS`
  (300) (cit:([`GIT_LOCAL_TIMEOUT_SECONDS`], mcp/src/agents_remember/kernel/git_command.py:71-71)) because it stats the whole work tree. Added the surviving degrade-to-data note
  (`TimeoutExpired` is a `SubprocessError`, caught at L32). Citations: the Logic paragraph gained
  line ranges for all five functions (`read_git_facts` L28-L33, `_read_git_facts` L36-L89,
  `git_facts_to_packet` L92-L103, `_git_stdout` L106-L112, `_git_error` L115-L116) — the file grew
  from 98 to 116 lines this leaf; and three reference rows were added, pinning
  `git_command.py` L35-L55 (the three bands) + L67-L96 (`run_git`), `cross_repo.py` L21-L39
  (`git_branch`/`git_head_or_empty` at the same metadata bound), and `test_git_command.py`
  `TimeoutClassTests` L543-L653. Verification metadata pinned until closeout stamps the L3 commit.
- 2026-05-31T12:45+02:00 — Created during the 1.0.0 review remediation; git calls now go through the shared `kernel/git_command.run_git` runner (F14) instead of a private `_run_git`. (Pre-existing onboarding gap: this file had no sidecar before.)
