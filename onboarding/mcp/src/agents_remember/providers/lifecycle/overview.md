# mcp/src/agents_remember/providers/lifecycle/ - Provider Lifecycle Facade Overview

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| sourceRoute            | `mcp/src/agents_remember/providers/lifecycle/` |
| doc_type               | `route-local-overview`                     |
| lastUpdated            | 2026-08-13T07:53+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[mcp/overview.md](../../../../overview.md)

## Purpose

### 260731-EFA-L23 Route Delta

L23 separates compose planning from executable discovery: dry-run plans render the symbolic `docker` command, while real provider execution still resolves the native executable at the execution boundary.

`lifecycle/` contains the public provider-lifecycle package facade, CLI
entrypoints, watcher aggregation, and shared lifecycle helper modules.
Provider-specific lifecycle implementations now live under
`providers/cgc/lifecycle/` and `providers/grepai/lifecycle/`.

## Hot Path Summary

Start with `cli.py` for parser/action dispatch, `watchers.py` for aggregate
provider start/status/stop orchestration, and the named shared modules for
provider-agnostic lifecycle primitives: `command_runner.py`,
`docker_runtime.py`, `host_ports.py`, `log_capture.py`, `process_status.py`,
`provider_settings.py`, `result_rendering.py`, `runtime_environment.py`, and
`state_files.py`. CGC behavior lives under `../cgc/lifecycle/`; GrepAI
behavior lives under `../grepai/lifecycle/`. Docker helpers now expose
normalized container state, health, and uptime summaries used by provider
current-state reporting. `log_capture.py` trims tool response payloads
recursively so verbose provider command output does not exceed client size limits.
Compose rendering only emits a host `user:` block when `os.getuid` and
`os.getgid` exist and are callable, which keeps non-POSIX hosts from receiving
an invalid UID/GID override.

## Route Model

- Shared lifecycle primitives live in named modules by responsibility.
- CLI construction and top-level provider/action dispatch live in `cli.py`.
- `watchers.py` composes enabled GrepAI and CGC lifecycle results.
- `../cgc/lifecycle/` owns CodeGraphContext settings/layout, backend container,
  install/patch/status, and process actions.
- `../grepai/lifecycle/` owns Docker GrepAI settings, PostgreSQL, Ollama, runner
  image/container, bounded run, install, status, and refresh actions.

## Invariants And Boundaries

- `providers.lifecycle` is the only public facade; implementation belongs here.
- Settings-driven lifecycle commands require an EXPLICIT `--from-settings` path
  (server-generated at runtime). The implicit fallback to
  `<coordination_root>/system/settings.json` was DELETED with 260703-L13 (GQ3):
  that file is the global agentic settings home, and `provider_settings.py`'s
  `require_lifecycle_settings_path` refuses a missing path instead of
  empty-defaulting on absent coordinator state.
- GrepAI is Docker-or-bust: no host GrepAI binary and no host Ollama fallback.
- Shared helpers should stay provider-agnostic; provider-specific branching
  belongs in CGC or GrepAI modules.
- Shared Docker helpers can normalize container facts, but provider readiness
  and current-state aggregation belong in provider-specific modules and
  `providers/current_state.py`.
- Lifecycle service callers should dispatch to implementation functions through
  the `providers.lifecycle` facade, not through CLI subprocess capture.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Public lifecycle exports are collected by the package facade. | `_EXPORT_MODULES` | mcp/src/agents_remember/providers/lifecycle/__init__.py:9-24 |
| Package execution delegates to the lifecycle CLI. | `main` | mcp/src/agents_remember/providers/lifecycle/__main__.py:1-8 |
| CGC lifecycle implementation is grouped under the CGC provider package. | `## Purpose` | onboarding/mcp/src/agents_remember/providers/cgc/lifecycle/overview.md:17-22 |
| GrepAI lifecycle implementation is grouped under the GrepAI provider package. | `## Purpose` | onboarding/mcp/src/agents_remember/providers/grepai/lifecycle/overview.md:17-22 |
| Provider lifecycle tests cover Docker-only GrepAI behavior, CGC bounded run behavior, and watcher aggregation. | `test_grepai_settings_backed_run_uses_docker_without_host_binary` | mcp/tests/test_provider_lifecycle_parser_1.py:109-143 |

## 260731-EFA-L2 — One More Shared Primitive, One Fewer Unused Knob

`compose_runtime.py` now owns `BackendStartReconciliation` (frozen: `network`, optional
`migration`, optional `forced_remove`). Both managed backends reconcile the host before they bring
a container up — adopt the compose-owned network, migrate what an unmanaged project left behind,
force-remove a container whose data mount no longer matches the layout — and all three land
together in the start result's `network`/`commands` payload. It lives here, not in either provider
package, precisely because both providers do it: a third managed backend inherits the shape rather
than re-deriving it. Both `cgc/lifecycle/backend.py` and `grepai/lifecycle/backend.py` import it
from here.

`command_runner.run_command` **no longer accepts an `env` override**. Provider commands have always
run under the sanitized `subprocess_env(...)`, and no caller in the tree ever supplied its own — the
parameter was a way to escape that sanitization that nothing used. Removing it makes the sanitized
environment the only environment. Do not restore the knob: a provider command that needs an extra
variable belongs in `runtime_environment.py`, where the sanitizer can see it.

`log_capture.py`'s recursive trim is unchanged in behaviour but is now two named halves —
`_shrink_logs` (empty captured output on success, cap it to the failure tail otherwise, keys always
present so the response keeps its shape) and `_drop_verbose_plumbing` (drop the always-redundant
mirror, then either drop the debug-only keys outright on success or keep them redacted on failure,
because that detail is what makes a failure debuggable). The success/failure asymmetry is the point
of the module and is now readable at the call site.

## Update History
- 2026-08-13T07:53+02:00 — 260731-EFA-L23 super-line reconciliation: re-reviewed this card and its Repo-Internal citation targets after absorbing the super-integration memory line. Retained claims remain supported by the current tree. Verification is pinned to real code HEAD `1580f92715ff93c988f9a15439ad9bec60ef4c5d`; the new-line memory mapping remains closeout-owned.

- 2026-08-12T15:56+02:00 — 260731-EFA-L23 curator route review: L23 separates compose planning from executable discovery: dry-run plans render the symbolic `docker` command, while real provider execution still resolves the native executable at the execution boundary. Verification provenance remains closeout-owned.

- 2026-08-04T18:23+02:00 — 260731-EFA-L6 S18-B14 curator: repaired 5 citation rows with exact anchors (`_EXPORT_MODULES`, `main`, the sibling-overview `## Purpose` headings, and the named provider-lifecycle tests) and ledger-verified ranges; the CGC/GrepAI overview citations now use the `onboarding/`-prefixed memory path form. Scoped citation recheck is green. Verification metadata remains pinned until closeout.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2: `compose_runtime.py` gained the shared
  `BackendStartReconciliation` bundle both provider backends now pass; `command_runner.run_command`
  lost its never-supplied `env` override, so the sanitized provider environment is the only one;
  `log_capture.py`'s trim split into `_shrink_logs` + `_drop_verbose_plumbing` with no change to
  what is emitted. Route model, facade boundary and the explicit `--from-settings` rule are
  unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-06T23:04+02:00 — 260703-L13 (GQ3): the implicit coordinator `system/settings.json`
  fallback was deleted from `provider_settings.py` (readers now demand the explicit
  `--from-settings`; the `coordination_root` parameter dropped, call sites in `watchers.py`
  and both provider lifecycle cores updated; `cli.py` help text rewritten). Route model
  otherwise unchanged. Verification metadata pinned until closeout stamps the L13 commit.

- 2026-06-08T09:57+02:00: Re-verified the provider lifecycle route after the Compose host-user helper switched to callable `getuid`/`getgid` checks for non-POSIX safety.
- 2026-06-06T12:15: Re-verified against the current shared provider lifecycle package; CLI, watcher aggregation, Docker helpers, result rendering, state files, and log trimming still match.
- 2026-06-01T00:00+02:00 — Added `log_capture.py` to the shared modules listing in Hot Path Summary.
- 2026-05-28T12:32+02:00: Updated after shared Docker helpers began exposing container-state summaries for provider current-state reporting.
- 2026-05-25T21:14+02:00: Updated when provider lifecycle implementation moved to provider-first packages and shared lifecycle helpers were split by responsibility.
- 2026-05-25T19:16+02:00: Updated after the legacy `provider_lifecycle.py` compatibility shim was removed and `providers.lifecycle` became the sole facade.
- 2026-05-25T19:09+02:00: Updated after CGC and GrepAI lifecycle modules moved into `cgc/` and `grepai/` subpackages with prefix-free filenames.
- 2026-05-25T19:01+02:00: Created after provider lifecycle was split out of the monolithic implementation into focused modules.
