# mcp/src/agents_remember/providers/lifecycle/log_capture.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/lifecycle/log_capture.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00                     |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`                |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`log_capture.py` is the recursive response trimmer that prevents oversized tool
responses caused by verbose provider command output (`pg_dump | psql`, `ollama
pull`, `cgc bundle import`). It strips logs on success, tails them on failure,
always drops the redundant `json` mirror, drops verbose plumbing keys
(`command`, `commands`, `compose`, `migration`) on success, and redacts
`PGPASSWORD=` tokens from command-line arguments.

## Code Commentary

### 260731-EFA-L2 Two Named Reduction Steps

`summarize_command_logs`'s per-node body is now two helpers, and the split is the rule:

- `_shrink_logs(node, *, succeeded, failure_tail)` — empties this node's captured output on
  success, caps it to the failure tail otherwise. **The keys stay present (as `""`)** so the
  response keeps its shape either way.
- `_drop_verbose_plumbing(node, *, succeeded)` — drops the always-redundant mirror keys, then
  either the debug-only keys (on success) or the secrets inside them (on failure, via
  `_redact_commands`). A failing node keeps the plumbing, redacted, **because that detail is what
  makes the failure debuggable**.

`summarize_command_logs` still mutates in place, still recurses into dict values and list items,
and still returns the same payload.

### Logic

`tail_lines(text, max_lines)` keeps only the last `max_lines` lines of a string
and prepends a count of how many lines were dropped.

`summarize_command_logs(payload, failure_tail=30)` walks the response tree
recursively (dict nodes, then list items). For each dict node it decides success
by `ok is True` or `returncode == 0`. On success: `stdout`/`stderr` are set to
`""` (schema preserved) and the keys in `_DROP_ON_SUCCESS` (`command`,
`commands`, `compose`, `migration`) are popped. On failure: `stdout`/`stderr`
are tailed to `failure_tail` lines and `command`/`commands` are passed through
`_redact_commands`. The `json` key is always popped regardless of success. Each
node is evaluated independently so a failing child inside a successful parent
retains its tail.

`_redact_commands` walks list/dict values recursively. `_redact_token` replaces
any string containing `PASSWORD=` with `<prefix>=***`, hiding credentials
embedded inline in provider clone command arguments.

### Invariants And Boundaries

- `summarize_command_logs` mutates the payload in place and returns it. It is
  called on a terminal tool-response object; no caller reads the discarded
  content afterwards.
- The `json` key is always dropped (it is a duplicate mirror of `payload`
  attached by `setup_common`); this is not conditional on success/failure.
- On failure, `command`/`commands` are retained for debugging but credential
  tokens are redacted before the response reaches the client.
- Success is evaluated per-node, not globally; a parent node being ok does not
  silence a failing child's logs.
- `tail_lines` returns the full text unchanged when the line count is within
  `max_lines`, so short logs are not truncated.

## Docs References

No external Domain Documentation source is configured for this memory repo.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `provider_watchers_payload` applies `summarize_command_logs` to every watcher tool response. | `provider_watchers_payload` | mcp/src/agents_remember/mcp/tools/providers.py:73-87 |
| `worktree_start_payload` applies `summarize_command_logs` to the worktree start tool response. | `worktree_start_payload` | mcp/src/agents_remember/mcp/tools/worktree.py:44-54 |
| Unit tests verify per-node success/failure behaviour, `json` always-dropped, secret redaction, and recursive step trimming. | `SummarizeCommandLogsTests` | mcp/tests/test_log_capture.py:31-104 |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B22 curator: replaced the three `n/a`-anchor
  table citations with exact anchors and fixer-generated ranges; exact non-fixing check returns
  zero findings.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0912` armed with no
  exemptions): extracted `_shrink_logs` and `_drop_verbose_plumbing` from `summarize_command_logs`.
  Identical reduction: same keys emptied, same keys dropped, same redaction on failure.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-01T00:00+02:00 — Created onboarding for the new log-capture response trimmer module.
