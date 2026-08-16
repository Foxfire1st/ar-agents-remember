# mcp/tests/test_subprocess_hygiene.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_subprocess_hygiene.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a`|
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

Package-wide AST guard: every `subprocess.run/Popen/check_*` call in
`agents_remember` must say what happens to stdin (`stdin=`, `input=`, or an
explicit `**kwargs` spread). Under the stdio MCP transport the server's
stdin/stdout ARE the JSON-RPC stream; an inheriting child wedges tool calls
(GitHub #49, proven by `test_mcp_stdio_transport.py`).

## Code Commentary

### Logic

Walks every package `.py` AST (skipping `package_data` Docker/runtime assets,
which run outside the MCP process), finds `subprocess.<spawn>` calls, and
fails with `file:line` for any call without stdin handling. A `**kwargs`
spread is accepted as a deliberate choice (e.g. `command_runner`).

### Invariants And Boundaries

- New subprocess call sites cannot regress to inherited stdin without failing
  CI; this is the structural fence for the #49 bug class.
- Only attribute-style calls on the `subprocess` module name are matched; an
  aliased import would evade the guard — keep imports as `import subprocess`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The proving harness for the bug class this guards. | `StdioTransportTests` | mcp/tests/test_mcp_stdio_transport.py:142-179 |

## Update History

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired the proving-harness reference to the exact `StdioTransportTests` class; scoped citation verification follows.

- 2026-07-31T16:35+02:00 — No content impact: the only change to
  `mcp/tests/test_subprocess_hygiene.py` since the L2 base commit is the whole-tree `ruff format`
  pass in `00e8379`, which re-wrapped 2 line(s) with no token change whatsoever. Checked by
  parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds.

- 2026-06-10T05:30+02:00: Created with the package-wide stdin audit (2.5.1).
