# mcp/src/agents_remember/providers/setup_common.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/setup_common.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../../overview.md`                     |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The provider setup facade re-exports these helpers for existing callers and tests. | "re-exports only the narrow set of symbols callers and tests still use" | onboarding/mcp/src/agents_remember/providers/provider_setup.py.md:15-18; onboarding/mcp/src/agents_remember/providers/provider_setup.py.md:41-46 |
| Lifecycle calls are dispatched through the direct lifecycle facade. | "Callers import this facade directly" | onboarding/mcp/src/agents_remember/providers/lifecycle/__init__.py.md:19-22; onboarding/mcp/src/agents_remember/providers/lifecycle/__init__.py.md:36-39 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 2 facade rows to
  memory-repo `onboarding/` citations with literal anchors (provider_setup.py.md 15-18 + 41-46,
  lifecycle/__init__.py.md 19-22 + 36-39). Zero findings remain.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `LifecycleCommand` and re-signed `run_lifecycle(coordination_root,
  command_spec, *, timeout, dry_run)`; `provider`/`action`/`extra_args`/`native_args` are no longer
  separate parameters. The built argv is unchanged. Verification metadata pinned until closeout
  stamps the L2 commit.
- 2026-06-10T07:30+02:00 — Added `setup_progress_from(args)`: returns the `SetupProgress` sink riding on the args namespace (set by `run_provider_setup(request, progress)`) or a shared no-op, so the install/prepare functions keep their `(args, settings)` signatures while announcing phases (GitHub #53).
- 2026-05-31T12:30+02:00 — `stable_provider_id` slug logic moved to `providers.identity` (now re-exported); added `provider_settings`; dropped unused `coordination_root` arg from `settings_path`/`load_settings` (1.0.0 review remediation).
- 2026-05-25T19:50+02:00: Created when shared provider setup helpers were extracted out of `provider_setup.py`.
