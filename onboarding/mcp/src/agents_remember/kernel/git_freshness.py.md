# mcp/src/agents_remember/kernel/git_freshness.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/git_freshness.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `abc7cbcc74921cdcb57a61529445f61641e919e7`                         |
| lastVerifiedCommitDate | 2026-07-31T21:50:08+02:00|
| governingOverview      | `../../../overview.md`                     |

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
projects the dataclass into the context-packet dict, adding `error` only when
set.

### Conventions

Mirrors `git_facts.py`: frozen dataclass + `*_to_packet` projector. Every git
call now goes through the shared `run_git` from `kernel.git_command`,
**including the fetch**. `fetch_remote` used to hold a local `subprocess.run`
copy purely because `run_git`'s timeout was a fixed, unoverridable 5s; once the
runner gained a per-call `timeout` keyword that copy had no reason to exist and
was deleted (`fetch_remote`, L49-L59). It still passes its own
`DEFAULT_FETCH_TIMEOUT = 30` (L23), which is now *shorter* than the runner's
`GIT_LOCAL_TIMEOUT_SECONDS = 300` default rather than longer than its old 5s:
the fetch is the only network call in this module, and 30s is the point past
which "still fetching" means "not coming back".

**The timeout class is chosen per command, not per module.** No call in this
file inherits the runner's default; each one names a band, and the code comments
carry the reasoning:

| Command | Call site | Bound |
| --- | --- | --- |
| `rev-parse --abbrev-ref <branch>@{upstream}` | `upstream_ref` L41-L45 | `GIT_METADATA_TIMEOUT_SECONDS` (30) — a local ref lookup, constant time |
| `branch --show-current` | `_read_branch_freshness` L101 | `GIT_METADATA_TIMEOUT_SECONDS` (30) — constant time |
| `rev-list --left-right --count <local>...<other>` | `ahead_behind` L67-L71 | `GIT_LOCAL_TIMEOUT_SECONDS` (300) — walks history; how much depends on how far the refs drifted |
| `fetch <remote>` | `fetch_remote` L54 | its own caller-supplied `timeout`, defaulting to `DEFAULT_FETCH_TIMEOUT = 30` — the one network call here |

`git_facts.py` classes its own probes the same way, and
`test_git_command.py::TimeoutClassTests::test_branch_freshness_classes_each_of_its_commands_by_what_it_does`
(L599-L621) asserts this table per command, so a call site that drops back to the
default fails the suite rather than quietly loosening to 300s.

### Invariants And Boundaries

- The only repository mutation is the optional fetch of remote-tracking refs;
  the working tree and local branches are never touched.
- Errors degrade to data (`state` + `error`), never exceptions escaping to the
  caller — packet assembly must not fail because a remote is unreachable.
- `state="unknown"` (failed fetch) must never be treated as `behind` by
  callers; preflights warn on it but do not block.
- **Every `run_git` call in this file names its timeout; none inherits the
  runner's default.** There are exactly three non-fetch calls —
  `upstream_ref` (L41-L45) and `branch --show-current` in
  `_read_branch_freshness` (L101) at `GIT_METADATA_TIMEOUT_SECONDS` (30), and
  `ahead_behind` (L67-L71) at `GIT_LOCAL_TIMEOUT_SECONDS` (300) — plus the fetch
  (L54) on its own 30s caller bound. Whichever bound trips, the result is still
  data, not an exception: `subprocess.TimeoutExpired` is a `SubprocessError`,
  which both `fetch_remote` (L55) and `read_branch_freshness` (L91) catch and
  turn into `state="unknown"`/`"unavailable"`.

### Todos

Sub-tasks B/D of the issue #54 series will consume this kernel from the
worktree modules; keep the API free of worktree-specific concepts.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding                                   | Citations | Source Path |
| ----------------------------------------- | --------- | ----------- |
| No relevant external documentation found. | n/a       | n/a         |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The one git runner, used for every command here including the fetch: `run_git` takes a per-call `timeout` and defaults to `GIT_LOCAL_TIMEOUT_SECONDS = 300`. The three bands this file selects from — `GIT_LOCAL_TIMEOUT_SECONDS` / `GIT_REMOTE_TIMEOUT_SECONDS` / `GIT_METADATA_TIMEOUT_SECONDS` — and why the metadata band exists, are at L35-L55; the signature and body at L67-L96. | [git_command.py](agents-remember/mcp/src/agents_remember/kernel/git_command.py) |
| The per-command bounds are pinned by test, not by convention: `test_branch_freshness_classes_each_of_its_commands_by_what_it_does` (L599-L621) patches `run_git` with a recorder whose `timeout` is a **required** keyword, so a call site that omits it fails the recorder instead of silently recording the default. `TimeoutClassTests` spans L543-L653. | [test_git_command.py](agents-remember/mcp/tests/test_git_command.py) |
| Style precedent: read-only git facts with dataclass + packet projector, and the sibling that classes its four probes the same way. | [git_facts.py](agents-remember/mcp/src/agents_remember/kernel/git_facts.py) |
| The context packet controller is the first consumer (`_freshness_packet`). | [context_packet.py](agents-remember/mcp/src/agents_remember/controllers/context_packet.py) |
| Kernel unit tests cover all states against local bare-origin fixtures. | [test_git_freshness.py](agents-remember/mcp/tests/test_git_freshness.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding                                    | Citations | Source Path |
| ------------------------------------------ | --------- | ----------- |
| No meaningful cross-repo references found. | n/a       | n/a         |

## Update History

- 2026-07-31T21:35+02:00 — 260731-EFA-L3 curator, correction on top of the 20:52 entry below. That
  entry added an invariant reading "The **four** non-fetch `run_git` calls (`upstream_ref` L35,
  `ahead_behind` L54, `branch --show-current` L84) **name no timeout and so inherit the runner's
  300s local default**." Every clause of that is now false, and one was false when written: there
  are **three** non-fetch calls, not four (it named three and counted four); all three now name a
  bound explicitly; and two of them take the *metadata* band, not the local default. A later fix
  moved the timeout class onto the command rather than the module — `upstream_ref` (L41-L45) and
  `_read_branch_freshness`'s `branch --show-current` (L101) now pass
  `GIT_METADATA_TIMEOUT_SECONDS` (30), while `ahead_behind` (L67-L71) passes
  `GIT_LOCAL_TIMEOUT_SECONDS` (300) *explicitly*, because `rev-list --left-right --count` walks
  history and is not constant time. Rewrote the invariant to state the three assignments and kept
  the still-true half (`TimeoutExpired` is a `SubprocessError` and degrades to `state` + `error`),
  and added a per-command table to Conventions. Citation repairs — the file grew 140 → 151 lines,
  so every self-citation the earlier entry left behind had slipped: `fetch_remote` L39-L49 →
  L49-L59; `DEFAULT_FETCH_TIMEOUT = 30` L19 → L23; `upstream_ref` L35 → L41-L45 (the `run_git`
  call, `def` at L37); `ahead_behind` L54 → L67-L71 (`def` at L62); `branch --show-current` L84 →
  L101; `fetch_remote`'s `except (OSError, subprocess.SubprocessError)` L45 → L55;
  `read_branch_freshness`'s L74 → L91. The `git_command.py` row's L53-L55; L67-L96 was re-checked
  and still lands on the three constants and on `run_git` — widened to L35-L55 so the comment that
  justifies the metadata band is inside the range. Added a `test_git_command.py` row for
  `TimeoutClassTests` (L543-L653), whose
  `test_branch_freshness_classes_each_of_its_commands_by_what_it_does` (L599-L621) asserts this
  file's three bounds per command.

- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: body updated. The Conventions paragraph said the
  fetch "shells out directly" because it "needs its own longer timeout than `run_git`'s fixed 5s";
  both halves are now false. `fetch_remote` (L39-L49) calls `run_git(repo_root, ["fetch", remote],
  timeout=timeout)` — its hand-rolled `subprocess.run` was deleted — and its
  `DEFAULT_FETCH_TIMEOUT = 30` is now shorter, not longer, than the runner's new
  `GIT_LOCAL_TIMEOUT_SECONDS = 300` default. Repaired 1 citation into a file this leaf changed: the
  repo-internal row read "Shared low-level git runner (5s timeout) used for all non-fetch commands"
  with no range, and now cites `git_command.py` L53-L55 (the three timeout constants) and L67-L96
  (`run_git`'s signature and body). Added an invariant recording that the four non-fetch calls
  inherit the 300s default and that `TimeoutExpired` still degrades to `state`+`error` data.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/src/agents_remember/kernel/git_freshness.py` since the L2 base commit is the whole-tree
  `ruff format` pass in `00e8379`, which re-wrapped 15 line(s), touching only redundant grouping
  parentheses. Checked by parsing both revisions and comparing the abstract syntax trees
  (identical) and the comment tokens (identical), so no symbol, signature, default, decorator,
  control-flow branch, docstring, or assertion this card describes has moved,and every claim this
  card makes about its own source still holds.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 attestation: this file was touched ONLY by the
  whole-tree `ruff format` pass (commit `00e8379`) — line reflow, no behaviour, contract,
  structure or responsibility change. The sidecar was re-read against the current source and
  every claim in it still holds, so it was deliberately not rewritten. Verification metadata
  pinned until closeout stamps the L2 commit.
- 2026-06-10T08:39+02:00: Created as the issue #54 freshness kernel (upstream lookup, bounded fetch, ahead/behind counts, `BranchFreshness` states) consumed by the `context_packet` freshness section.
