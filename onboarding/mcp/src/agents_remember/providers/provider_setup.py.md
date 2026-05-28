# mcp/src/agents_remember/providers/provider_setup.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/provider_setup.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-28T14:21:08+02:00                     |
| lastVerifiedCommitHash | `3f09b75461760479b443f1b04b180772724e7a24` |
| lastVerifiedCommitDate | 2026-05-28T15:10:01+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`provider_setup.py` is the provider setup facade. It keeps the typed
`ProviderSetupRequest`, CLI parser, action payload assembly, watcher dispatch,
and public compatibility exports while implementation lives in focused setup
modules.

## Code Commentary

### Logic

The facade imports shared setup helpers from `setup_common.py`, CGC seed and
bundle helpers from `cgc/seed.py` and `cgc/bundle.py`, CGC provider-level setup
from `cgc/setup.py`, and GrepAI provider-level setup from `grepai/setup.py`.
It preserves the public symbols callers and tests already use, including
`run_provider_setup`, `ProviderSetupRequest`, `rewrite_cgc_bundle_paths`,
`isolated_cgc_settings`, and the subprocess helper exports.

During `prepare`, the facade runs install steps, GrepAI refresh, CGC seed or
refresh fallback, and watcher start/status in sequence. CGC seed failure still
does not fail the whole prepare operation when `cgc_refresh_fallback` is enabled
and the fallback refresh path succeeds. Setup payload finalization now delegates
to `setup_reporting.py`, which keeps strict phase `ok`, records separate
readiness from final watcher status, stores failed phases and result counts, and
writes compact summaries under `logs/providers/setup/`.
Workflow-local isolated provider settings are reported through the canonical
`isolatedProviderSettings` payload only; the setup payload no longer emits
per-provider duplicate isolated-settings keys.

### Invariants And Boundaries

- MCP worktree provider setup must pass `--from-settings`; it must not depend on
  coordinator `system/settings.json`.
- `run_provider_setup(ProviderSetupRequest)` is the package service entry point;
  worktree and benchmark callers should not rebuild provider setup CLI `argv`.
- CGC worktree seed uses the original MCP-derived source settings when the seed
  source and target share a coordination root, and isolated target settings for
  the worktree runtime.
- Child subprocess helpers use `stdin=subprocess.DEVNULL` so provider children
  cannot consume the MCP stdio transport.
- This module is a typed provider setup facade; CGC seed, CGC bundle rewrite,
  GrepAI setup, setup reporting, and shared command helpers belong in their own
  modules.
- A failed CGC seed must not fail the whole prepare operation when the existing
  refresh fallback is enabled and then runs.
- Setup summaries record historical setup attempts; current provider truth is
  reported through provider status/current-state files.
- Isolated workflow settings should have one canonical payload shape:
  `isolatedProviderSettings`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Worktree start calls provider setup with MCP-derived provider settings. | [git_worktree_manager.py](agents-remember-md/mcp/src/agents_remember/worktrees/git_worktree_manager.py) |
| Benchmark preparation calls package-local provider setup instead of a source script. | [runner.py](agents-remember-md/mcp/src/agents_remember/benchmarks/runner.py) |
| Provider lifecycle calls are captured through package-local command capture. | [command_capture.py](agents-remember-md/mcp/src/agents_remember/mcp/command_capture.py) |
| CGC seed orchestration and bundle rewriting now live outside the facade. | [seed.py](cgc/seed.py.md); [bundle.py](cgc/bundle.py.md) |
| Provider-specific setup branches live in provider-owned setup modules. | [CGC setup](cgc/setup.py.md); [GrepAI setup](grepai/setup.py.md) |
| Shared settings and command helpers live in the setup common module. | [setup_common.py](setup_common.py.md) |
| Setup payload summaries and failed-phase compaction live in the setup reporting module. | [setup_reporting.py](setup_reporting.py.md) |

## Update History

- 2026-05-28T14:21:08+02:00: Updated after duplicate per-provider isolated
  settings payload keys were removed in favor of canonical
  `isolatedProviderSettings`.
- 2026-05-28T12:32+02:00: Updated after provider setup delegated payload finalization and summary persistence to `setup_reporting.py`.
- 2026-05-25T21:14+02:00: Updated imports after CGC and GrepAI setup modules moved into provider-owned packages.
- 2026-05-25T19:50+02:00: Refactored into a setup facade backed by `setup_common.py`, `cgc_setup.py`, `cgc_seed.py`, `cgc_bundle.py`, and `grepai_setup.py`; targeted Radon CC/MI no longer reports B-or-worse output for the setup slice.
- 2026-05-24T05:48+02:00: Updated after CGC seed failure stopped failing provider prepare payloads when the existing refresh fallback is enabled.
- 2026-05-23T23:46+02:00: Updated after Phase 05 F-05 made provider setup require explicit settings and added the typed `ProviderSetupRequest` service front door.
- 2026-05-23T13:46+02:00: Added when provider setup moved from the deleted source `scripts/` route into the MCP package.
