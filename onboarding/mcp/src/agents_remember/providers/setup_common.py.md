# mcp/src/agents_remember/providers/setup_common.py

## Current operative account — MIK-R112

The current source facts below replace the former operative inventory. The separately labelled superseded claims describe only the pre-repair card. Original paragraphs, dated closures, evidence and citation identities remain intact in the explicitly historical section; they grant no current call, restored route or fresh execution acceptance.

- Current provider_enabled always returns False for codegraphcontext-code and grepai-memory.

### Superseded inventory

- Pre-repair card claim: Card describes ordinary settings-driven enablement without the retirement override. This is superseded archival wording, not a current prescription.
- Pre-repair card claim: Card names providers.identity as stable_provider_id owner; current import is kernel.primitives.identity. This is superseded archival wording, not a current prescription.

### Source and authority bounds

- Source comparison: `mcp/src/agents_remember/providers/setup_common.py:81 (def provider_enabled)`.
- Source comparison: `mcp/src/agents_remember/providers/setup_common.py:15 (from agents_remember.kernel.primitives.identity)`.

Source inspection supplies no new test, native-host, whole-build, landing or memory acceptance. Retained internal services and historical fixtures do not re-advertise deleted MCP tools. Numbered references retain historical custody and may include disclosed inherited stale targets; currentness or proof truth is not inferred from them.

## Historical original card — preserved, not the current operative account

<details>
<summary>Retained original source accounts and producer history</summary>

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

- The provider setup facade re-exports these helpers for existing callers and tests. 
- Lifecycle calls are dispatched through the direct lifecycle facade. 

</details>
