# mcp/src/agents_remember/providers/setup_common.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`setup_common.py` owns shared provider setup primitives: explicit settings-file loading, provider enablement checks, template helpers, subprocess execution, JSON stdout parsing, and lifecycle command capture. It re-exports `stable_provider_id` from `providers.identity` (the canonical slug source) for existing callers.

## Code Commentary

### 260731-EFA-L2 `LifecycleCommand`

`run_lifecycle(coordination_root, command_spec, *, timeout, dry_run)` takes the frozen
**`LifecycleCommand(provider, action, extra_args=(), native_args=())`**. The split matters because
**the provider CLI puts its arguments on either side of the action**: `extra_args` are
provider-level flags that precede it, `native_args` are the action's own arguments. The three parts
are only ever meaningful together, so they travel as one command. Both are tuples because the
object is frozen; the built argv is `[provider, --coordination-root …, --timeout …, --json,
*extra_args, action, *native_args]` — identical to before. Every provider setup module
(`cgc/setup.py`, `grepai/setup.py`, `provider_setup.py`, `cgc/seed.py`) imports it.

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

## Evidence

### Repo-Internal References

- The provider setup facade re-exports these helpers for existing callers and tests. [1]
- Lifecycle calls are dispatched through the direct lifecycle facade. [2]
