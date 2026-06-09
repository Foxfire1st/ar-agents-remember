# mcp/src/agents_remember/providers/cgc/context/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/providers/cgc/context/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-09T22:10+02:00|
| lastVerifiedCommitHash | `04f736d5fdaf23002b0e4172b7475a1108da0d9e` |
| lastVerifiedCommitDate | 2026-06-09T22:16:49+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/core.py` owns CodeGraphContext runtime layout derivation, Docker runner
layout fields, provider-owned config writing, source artifact detection, and
stale runtime cleanup.

## Code Commentary

### Logic

It defines `CgcRuntimeLayout`, builds layouts from direct parameters or provider
settings, derives FalkorDB host/port from provider settings plus backend state,
derives Docker runner image/build/lock/container paths, tracks the backend
container name and shared Docker network name for runner connectivity, writes
managed `.cgcignore`, config, and `.env` files, detects source-tree CGC
artifacts, and removes only generated or obsolete provider runtime artifacts
inside validated provider roots. Runtime layout no longer exposes a host
`venvRoot` or CGC executable path, and provider settings that still define
`venvRoot` are rejected as stale configuration.

A module-level `to_container_path()` helper maps a host path to the POSIX path
seen inside the Linux provider container by stripping a leading Windows drive
letter (`C:/ew/x` becomes `/ew/x`); it is a no-op on POSIX hosts. The layout
exposes `container_runtime_root` and `container_code_repo_root` properties built
from that helper, and `env()` takes a `for_container` flag: when set it renders
path-valued variables (`HOME`, `LOG_FILE_PATH`, `DEBUG_LOG_PATH`, and the
process-env-template roots) as driveless container paths and omits host-only
Windows variables (`USERPROFILE`, `APPDATA`, `LOCALAPPDATA`). These keep
bind-mount targets and in-container arguments valid on Windows hosts, whose host
paths carry a drive-letter colon Docker's `host:container` mount syntax would
otherwise reject.

### Invariants And Boundaries

- This file is part of the direct `providers.context` facade implementation; there is no `context_providers.py` compatibility fallback.
- Provider runtime paths stay under configured provider roots unless a helper explicitly validates another source path.
- Managed CGC execution is Docker-owned; host venv fields are not parsed,
  created, or used as fallback executable paths.
- Docker runner command builders consume layout-level backend container and
  network names; layout derivation must keep those synchronized with backend
  settings.
- Container-side paths — bind-mount targets, `working_dir`, and in-container
  env/arguments — must be driveless POSIX via `to_container_path` /
  `env(for_container=True)`; only the host side of a bind mount keeps the native
  (possibly drive-lettered) path. The mapping is identity on POSIX hosts, so
  Linux/macOS behavior is unchanged and only Windows hosts are affected.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Lifecycle CGC modules use these layout and cleanup helpers before running or installing CGC. | [core.py](../lifecycle/core.py.md); [installation.py](../lifecycle/installation.py.md); [process_control.py](../lifecycle/process_control.py.md); [runner.py](../lifecycle/runner.py.md) |

## Update History

- 2026-06-09T22:10+02:00 — `_cgc_runner_image()` now appends `CGC_RUNNER_IMAGE_LAYER_REVISION` to the tag (`agents-remember/codegraphcontext:0.4.10-ar1`) so Docker-layer-only changes (e.g. the watch-guard entrypoint) trigger image rebuilds on install.

- 2026-05-29T18:35+02:00: Split `core.py` (668->522): extracted `materialize.py` (runtime dir/config writers) and `cleanup.py` (stale-artifact removal); `core.py` keeps the `CgcRuntimeLayout` dataclass, settings-derived construction, and `to_container_path` (commit `01f503d`).
- 2026-05-29T07:19+02:00: Updated after adding `to_container_path`, the `container_runtime_root` / `container_code_repo_root` properties, and `env(for_container=...)` so CGC bind-mount targets, working dir, and container environment render as driveless POSIX paths on Windows hosts.
- 2026-05-28T13:40+02:00: Updated after CGC layout removed host venv path fields and began rejecting stale `venvRoot` provider settings.
- 2026-05-26T13:58+02:00: Updated after CGC layouts gained backend container and Docker network fields for runner connectivity.
- 2026-05-26T12:51+02:00: Updated after CGC layout gained Docker runner fields and stopped creating host venv directories.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
