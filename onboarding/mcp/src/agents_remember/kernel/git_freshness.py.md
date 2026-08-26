# mcp/src/agents_remember/kernel/git_freshness.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/git_freshness.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`                         |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
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
cit:([`freshness_to_packet`], mcp/src/agents_remember/kernel/git_freshness.py:158-169)
projects the dataclass into the context-packet dict, adding `error` only when set.

**This module declares the freshness vocabulary.** cit:([`FreshnessState`], mcp/src/agents_remember/kernel/git_freshness.py:29-38) is
the eight-member alias — four members reporting a comparison that succeeded, four
reporting why one could not be made — with `VALID_FRESHNESS_STATES` derived from
it by cit:([`get_args`], mcp/src/agents_remember/kernel/git_freshness.py:41-41). `BranchFreshness.state` is that alias, not `str`,
cit:([`BranchFreshness`], mcp/src/agents_remember/kernel/git_freshness.py:44-52)
and the computed fold in `_read_branch_freshness` is annotated
cit:(["current"], mcp/src/agents_remember/kernel/git_freshness.py:146-154). `models.context_packet.BranchFreshness.state`
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
runner gained a per-call `timeout` keyword that copy had no reason to exist and
was deleted cit:([`fetch_remote`], mcp/src/agents_remember/kernel/git_freshness.py:67-77). It still passes its own
`DEFAULT_FETCH_TIMEOUT = 30`, cit:([`DEFAULT_FETCH_TIMEOUT`], mcp/src/agents_remember/kernel/git_freshness.py:23-23), which is now *shorter* than the runner's
`GIT_LOCAL_TIMEOUT_SECONDS = 300` default rather than longer than its old 5s:
the fetch is the only network call in this module, and 30s is the point past
which "still fetching" means "not coming back".

**The timeout class is chosen per command, not per module.** No call in this
file inherits the runner's default; each one names a band, and the code comments
carry the reasoning:

| Command | Call site | Bound |
| --- | --- | --- |
| `rev-parse --abbrev-ref <branch>@{upstream}` | `upstream_ref` | `GIT_METADATA_TIMEOUT_SECONDS` (30) — a local ref lookup, constant time |
| `branch --show-current` | `_read_branch_freshness` | `GIT_METADATA_TIMEOUT_SECONDS` (30) — constant time |
| `rev-list --left-right --count <local>...<other>` | `ahead_behind` | `GIT_LOCAL_TIMEOUT_SECONDS` (300) — walks history; how much depends on how far the refs drifted |
| `fetch <remote>` | `fetch_remote` | its own caller-supplied `timeout`, defaulting to `DEFAULT_FETCH_TIMEOUT = 30` — the one network call here |

`git_facts.py` classes its own probes the same way, and
`test_git_command.py::TimeoutClassTests::test_branch_freshness_classes_each_of_its_commands_by_what_it_does`,
cit:([`test_branch_freshness_classes_each_of_its_commands_by_what_it_does`], mcp/tests/test_git_command.py:723-745)
asserts this table per command, so a call site that drops back to the
default fails the suite rather than quietly loosening to 300s.

### Invariants And Boundaries

- The only repository mutation is the optional fetch of remote-tracking refs;
  the working tree and local branches are never touched.
- **cit:([`FreshnessState`], mcp/src/agents_remember/kernel/git_freshness.py:29-38) is the single declaration of this vocabulary.**
  `BranchFreshness.state` is typed with it and the context packet's wire model
  imports it. A ninth member — another degrade reason, most likely — is added
  here and nowhere else; a copy at the wire boundary would only be measured
  against this module when a real repository produced it.
- cit:([`VALID_FRESHNESS_STATES`], mcp/src/agents_remember/kernel/git_freshness.py:41-41) is derived by `get_args`, never listed
  separately, and the exhaustiveness suite asserts produced == declared in both
  directions.
- Errors degrade to data (`state` + `error`), never exceptions escaping to the
  caller — packet assembly must not fail because a remote is unreachable.
- `state="unknown"` (failed fetch) must never be treated as `behind` by
  callers; preflights warn on it but do not block.
- **Every `run_git` call in this file names its timeout; none inherits the
  runner's default.** There are exactly three non-fetch calls —
  `upstream_ref`, cit:([`upstream_ref`], mcp/src/agents_remember/kernel/git_freshness.py:55-64),
  and `branch --show-current` in `_read_branch_freshness`,
  cit:([`_read_branch_freshness`], mcp/src/agents_remember/kernel/git_freshness.py:115-155),
  at `GIT_METADATA_TIMEOUT_SECONDS` (30), and `ahead_behind`,
  cit:([`ahead_behind`], mcp/src/agents_remember/kernel/git_freshness.py:80-95),
  at `GIT_LOCAL_TIMEOUT_SECONDS` (300) — plus the fetch,
  cit:([`fetch_remote`], mcp/src/agents_remember/kernel/git_freshness.py:67-77), on its own 30s caller bound. Whichever bound trips, the result is still
  data, not an exception: `subprocess.TimeoutExpired` is a `SubprocessError`,
  which both `fetch_remote`, cit:([`fetch_remote`], mcp/src/agents_remember/kernel/git_freshness.py:67-77), and
  `read_branch_freshness`, cit:([`read_branch_freshness`], mcp/src/agents_remember/kernel/git_freshness.py:98-112), catch and
  turn into `state="unknown"`/`"unavailable"`.

### Todos

Sub-tasks B/D of the issue #54 series will consume this kernel from the
worktree modules; keep the API free of worktree-specific concepts.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one git runner, used for every command here including the fetch: `run_git` takes a per-call `timeout` and defaults to `GIT_LOCAL_TIMEOUT_SECONDS = 300`. The three bands this file selects from — `GIT_LOCAL_TIMEOUT_SECONDS` / `GIT_REMOTE_TIMEOUT_SECONDS` / `GIT_METADATA_TIMEOUT_SECONDS` — and why the metadata band exists, are in the timeout-class block; the signature and body are in `run_git`. | `run_git`, `GIT_LOCAL_TIMEOUT_SECONDS`, `GIT_REMOTE_TIMEOUT_SECONDS`, `GIT_METADATA_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/git_command.py:71-73; mcp/src/agents_remember/kernel/git_command.py:94-145 |
| The per-command bounds are pinned by test, not by convention: `test_branch_freshness_classes_each_of_its_commands_by_what_it_does` patches `run_git` with a recorder whose `timeout` is a **required** keyword, so a call site that omits it fails the recorder instead of silently recording the default. `TimeoutClassTests` owns the assertions. | `TimeoutClassTests`, `test_branch_freshness_classes_each_of_its_commands_by_what_it_does` | mcp/tests/test_git_command.py:613-723 |
| Style precedent: read-only git facts with dataclass + packet projector, the sibling that classes its four probes the same way, and — since 260731-EFA-L4 — the sibling that declares its own `RepoState` / `VALID_REPO_STATES` for the same reason this file declares `FreshnessState`. | `RepoState`, `VALID_REPO_STATES`, `read_git_facts` | mcp/src/agents_remember/kernel/git_facts.py:22-22; mcp/src/agents_remember/kernel/git_facts.py:26-26; mcp/src/agents_remember/kernel/git_facts.py:40-45 |
| The wire face that imports `FreshnessState` instead of retyping its eight members: `BranchFreshness.state`. | "state: FreshnessState" | mcp/src/agents_remember/models/context_packet.py:98-98 |
| The context packet application entry point is the first consumer (`_freshness_packet`). | `_freshness_packet` | mcp/src/agents_remember/application/context_packet.py:105-132 |
| `test_every_freshness_state_the_git_reader_writes_validates` asserts produced == `VALID_FRESHNESS_STATES`; `test_a_directory_that_is_not_a_repo_crosses_the_freshness_wire` walks a real degrade across the boundary. | `test_every_freshness_state_the_git_reader_writes_validates`, `test_a_directory_that_is_not_a_repo_crosses_the_freshness_wire` | mcp/tests/test_wire_vocabulary_exhaustiveness.py:767-776; mcp/tests/test_wire_vocabulary_exhaustiveness_boundary.py:538-543 |
| Kernel unit tests cover all states against local bare-origin fixtures. | `GitFreshnessTests` | mcp/tests/test_git_freshness.py:20-104 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-03T02:32:19+02:00 — Curator W3-B02 resolved all 31 manifest findings: converted 19 legacy prose line citations, repaired 12 Repo-Internal anchor/source findings, and normalized 4 explanatory timeout-table references. Preserved the source-freeze and verification metadata.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T09:56+02:00 — 260731-EFA-L4 curator: body updated and every self-citation
  re-derived. This module now DECLARES cit:([`FreshnessState`], mcp/src/agents_remember/kernel/git_freshness.py:29-38), the eight-member freshness
  vocabulary, with `VALID_FRESHNESS_STATES` derived by cit:([`get_args`], mcp/src/agents_remember/kernel/git_freshness.py:41-41);
  `BranchFreshness.state`, cit:([`BranchFreshness`], mcp/src/agents_remember/kernel/git_freshness.py:44-52), changed from `str` to that alias and the computed fold is
  annotated cit:(["current"], mcp/src/agents_remember/kernel/git_freshness.py:146-154). `models.context_packet.BranchFreshness.state` imports
  it instead of holding the hand-written eight-member copy it used to — the copy that was most
  exposed of any in the package, because half these members exist only on degrade paths and
  `freshness_to_packet` crosses the boundary as an untyped dict. Added the declaration paragraph
  and two invariants. The file grew 151 → 169 lines and all nine self-citations were re-derived
  against the current source, including cit:([`fetch_remote`], mcp/src/agents_remember/kernel/git_freshness.py:67-77),
  cit:([`upstream_ref`], mcp/src/agents_remember/kernel/git_freshness.py:55-64),
  cit:([`ahead_behind`], mcp/src/agents_remember/kernel/git_freshness.py:80-95),
  cit:([`_read_branch_freshness`], mcp/src/agents_remember/kernel/git_freshness.py:115-155), and
  cit:([`DEFAULT_FETCH_TIMEOUT`], mcp/src/agents_remember/kernel/git_freshness.py:23-23). The shared-runner,
  git-facts, context-packet, wire-model, and exhaustiveness references are recorded in the current
  Repo-Internal table. Verification metadata pinned until closeout stamps the L4 commit.
- 2026-07-31T21:35+02:00 — 260731-EFA-L3 curator, correction on top of the 20:52 entry below. That
  entry added an invariant reading "The **four** non-fetch `run_git` calls **name no timeout and
  so inherit the runner's 300s local default**." Every clause of that is now false, and one was
  false when written: there are **three** non-fetch calls, not four; all three now name a bound
  explicitly; and two of them take the *metadata* band, not the local default. A later fix moved
  the timeout class onto the command rather than the module — `upstream_ref`,
  cit:([`upstream_ref`], mcp/src/agents_remember/kernel/git_freshness.py:55-64), and
  `_read_branch_freshness`'s branch lookup, cit:([`_read_branch_freshness`], mcp/src/agents_remember/kernel/git_freshness.py:115-155),
  now pass `GIT_METADATA_TIMEOUT_SECONDS` (30), while `ahead_behind`,
  cit:([`ahead_behind`], mcp/src/agents_remember/kernel/git_freshness.py:80-95), passes
  `GIT_LOCAL_TIMEOUT_SECONDS` (300) *explicitly*, because `rev-list --left-right --count` walks
  history and is not constant time. Rewrote the invariant to state the three assignments and kept
  the still-true half (`TimeoutExpired` is a `SubprocessError` and degrades to `state` + `error`),
  and added a per-command table to Conventions. The shared-runner and timeout-class test rows were
  re-derived against their current sources. Added a `TimeoutClassTests` row whose
  `test_branch_freshness_classes_each_of_its_commands_by_what_it_does` assertion covers this
  file's three bounds per command.

- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: body updated. The Conventions paragraph said the
  fetch "shells out directly" because it "needs its own longer timeout than `run_git`'s fixed 5s";
  both halves are now false. `fetch_remote`, cit:([`fetch_remote`], mcp/src/agents_remember/kernel/git_freshness.py:67-77),
  calls `run_git(repo_root, ["fetch", remote], timeout=timeout)` — its hand-rolled `subprocess.run`
  was deleted — and its `DEFAULT_FETCH_TIMEOUT = 30` is now shorter, not longer, than the runner's
  `GIT_LOCAL_TIMEOUT_SECONDS = 300` default. Repaired the shared-runner row to use current exact
  anchors and generated source ranges. Added an invariant recording that every call names its
  timeout and that `TimeoutExpired` still degrades to `state` + `error` data.

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
