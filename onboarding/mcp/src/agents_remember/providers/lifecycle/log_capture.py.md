# mcp/src/agents_remember/providers/lifecycle/log_capture.py

## Governing Overview

[Provider Lifecycle Modules Overview](overview.md)

## Purpose

`log_capture.py` is the recursive response trimmer that prevents oversized tool
responses caused by verbose provider command output (`pg_dump | psql`, `ollama
pull`, `cgc bundle import`). It strips logs on success, tails them on failure,
always drops the redundant `json` mirror, drops verbose plumbing keys
(`command`, `commands`, `compose`, `migration`) on success, and masks string command-list
items containing `PASSWORD=` (including `PGPASSWORD=`), within the limits below.

## Code Commentary

### 260731-EFA-L2 Two Named Reduction Steps

`summarize_command_logs`'s per-node body is now two helpers, and the split is the rule:

- `_shrink_logs(node, *, succeeded, failure_tail)` — empties this node's captured output on
  success, caps it to the failure tail otherwise. **The keys stay present (as `""`)** so the
  response keeps its shape either way.
- `_drop_verbose_plumbing(node, *, succeeded)` — drops the always-redundant mirror keys, then
  the debug-only keys on success. On failure it keeps the plumbing and applies `_redact_commands`
  only to `command`/`commands`, masking supported `PASSWORD=` string items in command-token lists;
  this is not general secret redaction.

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

`_redact_commands` recurses through dictionary values. For a list it calls `_redact_token`
on each immediate item, not `_redact_commands`: string items containing the case-sensitive
`PASSWORD=` substring are replaced with the text before the first `=` followed by `=***`
(for example, `PGPASSWORD=...` becomes `PGPASSWORD=***`). Non-string list items, including
nested lists/dictionaries, and scalar values passed to `_redact_commands` are unchanged.
This covers flat command-token lists (including those reached through dictionary values),
not arbitrary nested token containers, scalar command strings, logs, or every kind of secret.

### Invariants And Boundaries

- `summarize_command_logs` mutates the payload in place and returns it. It is
  called on a terminal tool-response object; no caller reads the discarded
  content afterwards.
- The `json` key is always dropped (it is a duplicate mirror of `payload`
  attached by `setup_common`); this is not conditional on success/failure.
- On failure, `command`/`commands` are retained for debugging. Their supported command-list
  string items containing `PASSWORD=` are masked before transport; dictionary values recurse,
  but nested list items and scalar strings have no blanket redaction guarantee.
- Success is evaluated per-node, not globally; a parent node being ok does not
  silence a failing child's logs.
- `tail_lines` returns the full text unchanged when the line count is within
  `max_lines`, so short logs are not truncated.

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory repo.

No relevant external documentation found.

### Repo-Internal References


- `worktree_start_payload` applies `summarize_command_logs` to the worktree start tool response. [2]
