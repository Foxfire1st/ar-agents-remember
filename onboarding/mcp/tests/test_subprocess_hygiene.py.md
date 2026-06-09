# mcp/tests/test_subprocess_hygiene.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_subprocess_hygiene.py`     |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T05:30+02:00                     |
| lastVerifiedCommitHash | `592274a52cec61d97521771c630272c72240ed01`|
| lastVerifiedCommitDate | 2026-06-10T01:38:42+02:00|
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

| Finding | Source Path |
| --- | --- |
| The proving harness for the bug class this guards. | [test_mcp_stdio_transport.py](agents-remember-md/mcp/tests/test_mcp_stdio_transport.py) |

## Update History

- 2026-06-10T05:30+02:00: Created with the package-wide stdin audit (2.5.1).
