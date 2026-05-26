# mcp/src/agents_remember/providers/setup_common.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/setup_common.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-25T19:50+02:00                     |
| lastVerifiedCommitHash | `ae9c4e5b6af38eda7f2b29006130c4263e9db62f` |
| lastVerifiedCommitDate | 2026-05-25T19:55:09+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`setup_common.py` owns shared provider setup primitives: explicit settings-file loading, provider enablement checks, stable ID/template helpers, subprocess execution, JSON stdout parsing, and lifecycle command capture.

## Code Commentary

### Logic

The module requires an explicit provider settings path, reads JSON settings, extracts enabled `contextProviders`, applies the GrepAI skip switch during selection, normalizes provider IDs, and runs provider lifecycle commands either as dry-run payloads or through package-local command capture.

### Invariants And Boundaries

- Provider setup must not infer authority from coordinator `system/settings.json`; callers pass `--from-settings` or a typed settings path.
- Child process helpers force UTF-8 and use `stdin=subprocess.DEVNULL` so lifecycle children cannot consume MCP stdio.
- Shared helpers stay provider-agnostic; CGC and GrepAI decisions live in provider-specific setup modules.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The provider setup facade re-exports these helpers for existing callers and tests. | [provider_setup.py](provider_setup.py.md) |
| Lifecycle calls are dispatched through the direct lifecycle facade. | [lifecycle package](lifecycle/__init__.py.md) |

## Update History

- 2026-05-25T19:50+02:00: Created when shared provider setup helpers were extracted out of `provider_setup.py`.
