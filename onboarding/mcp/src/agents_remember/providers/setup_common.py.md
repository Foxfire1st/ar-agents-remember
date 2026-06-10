# mcp/src/agents_remember/providers/setup_common.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/setup_common.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-10T07:30+02:00     |
| lastVerifiedCommitHash | `ab7e21b4ab4b8526adcdad8ea2243657b8aea7a0` |
| lastVerifiedCommitDate | 2026-06-10T08:21:41+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`setup_common.py` owns shared provider setup primitives: explicit settings-file loading, provider enablement checks, template helpers, subprocess execution, JSON stdout parsing, and lifecycle command capture. It re-exports `stable_provider_id` from `providers.identity` (the canonical slug source) for existing callers.

## Code Commentary

### Logic

The module requires an explicit provider settings path, reads JSON settings, extracts enabled `contextProviders`, resolves a single provider's settings block, applies the GrepAI skip switch during selection, and runs provider lifecycle commands either as dry-run payloads or through package-local command capture. Provider ID slugging is delegated to `providers.identity` (re-exported here). `settings_path`/`load_settings` take only `from_settings`; they no longer accept a `coordination_root` argument.

`setup_progress_from(args)` returns the `SetupProgress` sink riding on the
args namespace (set by `run_provider_setup(request, progress)`) or a shared
no-op, so install/prepare functions keep their `(args, settings)` signatures
while announcing phases (GitHub #53).

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

- 2026-06-10T07:30+02:00 — Added `setup_progress_from(args)`: returns the `SetupProgress` sink riding on the args namespace (set by `run_provider_setup(request, progress)`) or a shared no-op, so the install/prepare functions keep their `(args, settings)` signatures while announcing phases (GitHub #53).
- 2026-05-31T12:30+02:00 — `stable_provider_id` slug logic moved to `providers.identity` (now re-exported); added `provider_settings`; dropped unused `coordination_root` arg from `settings_path`/`load_settings` (1.0.0 review remediation).
- 2026-05-25T19:50+02:00: Created when shared provider setup helpers were extracted out of `provider_setup.py`.
