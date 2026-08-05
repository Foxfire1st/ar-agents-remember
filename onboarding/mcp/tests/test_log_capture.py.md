# test_log_capture.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_log_capture.py`            |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_log_capture.py` verifies the provider response log-summarizer that
prevents oversized tool responses. It protects: log-drop on success, log-tail
on failure, secret redaction, always-drop of the `json` mirror, per-node
independent evaluation, and recursive descent into nested result trees.

## Code Commentary

### Logic

`TailLinesTests` covers `tail_lines`: short text passes unchanged; text longer
than `max_lines` produces a header noting how many lines were omitted and ends
with the last line.

`SummarizeCommandLogsTests` covers `summarize_command_logs`:

- `test_success_drops_stdout_and_stderr`: `ok=True` → `stdout`/`stderr` become `""`.
- `test_returncode_zero_counts_as_success`: `returncode=0` is treated as success.
- `test_failure_keeps_only_the_tail`: `ok=False` → stdout tailed; omission header present.
- `test_redacts_password_in_command_list`: on failure, `PGPASSWORD=secret` in a nested `commands` dict value becomes `PGPASSWORD=***`.
- `test_recurses_into_nested_steps`: a list of steps is recursed; successful step logs dropped, failing step logs tailed.
- `test_each_node_evaluated_independently`: a failing child inside a successful parent retains its stderr.
- `test_success_drops_duplicate_json_and_verbose_plumbing`: `json`, `command`, `compose`, `migration` all popped on success; a non-plumbing key (`seededFrom`) survives.
- `test_json_dropped_even_on_failure_but_command_kept`: on failure `json` is still dropped; `command` is retained with credential tokens redacted.

### Conventions

No Docker, filesystem, or network access. Tests call functions directly with
synthetic dicts.

### Invariants And Boundaries

The tests protect that: success evaluation is per-node not global; `json` is
always dropped; credentials never survive into a failure response; recursive
descent covers both nested dicts (steps) and lists.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module under test. | "def summarize_command_logs" | mcp/src/agents_remember/providers/lifecycle/log_capture.py:36-36 |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: replaced the `n/a` row with an exact
  anchor and fixer-generated range; exact non-fixing check returns zero findings.

- 2026-06-01T00:00+02:00 — Created onboarding for the new log-capture tests.
