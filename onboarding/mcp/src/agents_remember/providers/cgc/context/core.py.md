# mcp/src/agents_remember/providers/cgc/context/core.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/providers/cgc/context/core.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T00:00+02:00     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                     |

## Governing Overview

[overview.md](overview.md)

## Purpose

`cgc/core.py` owns CodeGraphContext runtime layout derivation, Docker runner
layout fields, provider-owned config writing, source artifact detection, and
stale runtime cleanup.

## Code Commentary

### 260731-EFA-L2 Layout Parameter Objects

`cgc_runtime_layout(repo, *, instance=DEFAULT_CGC_INSTANCE, watcher=DEFAULT_CGC_WATCHER,
backend=DEFAULT_CGC_BACKEND)` replaces the previous nineteen keywords. The four frozen dataclasses
are defined here and split along what each fact is *about*, not where it happens to be used:

- **`CgcRepo(coordination_root, repo_id, code_repo_root, cgcignore_patterns=())`** — the repository
  one CGC instance indexes and the root that owns the instance. `cgcignore_patterns` belongs here
  because it is about which parts of *this repository* the graph covers, not about how the provider
  is deployed. This is the only required argument.
- **`CgcInstance(runtime_root, requirements_file, patches_root, state_file)`** — where the instance
  lives on disk and what it is pinned to.
- **`CgcWatcher(image, build_root, lock_file, container_name, process_env_template, watch_cwd,
  watch_log_file)`** — one process, described once: the runner image, the build inputs it comes
  from, the container it runs as, its environment, and the cwd/log of the `cgc watch` it hosts.
- **`CgcBackend(root, data_root, state_file, container_name, network_name)`** — the managed
  FalkorDB backend.

**Every field of the last three is an override, so the empty instance IS the convention.** That is
why `DEFAULT_CGC_INSTANCE` / `DEFAULT_CGC_WATCHER` / `DEFAULT_CGC_BACKEND` exist as module-level
frozen singletons and serve as the defaults: omitting a bundle means "conventional placement under
`providers/runners/codegraphcontext/<repoId>`", exactly as omitting each keyword did.

### Logic

It defines `CgcRuntimeLayout`, builds layouts from direct parameters or provider
settings, derives FalkorDB host/port from provider settings plus backend state,
derives Docker runner image/build/lock/container paths, tracks the backend
container name and shared Docker network name for runner connectivity, writes
managed `.cgcignore`, config, and `.env` files, detects source-tree CGC
artifacts, and removes only generated or obsolete provider runtime artifacts
inside validated provider roots. The public `cgc_runner_image()` is the single
source of truth for the runner image tag
(`repository:version-layerrevision`); `providers/settings.py` and a regression
test depend on it, because an independent derivation there shipped the 2.5.0
upgrade-path bug where cached-image hosts kept a guard-less image (GitHub #50).
Bump `CGC_RUNNER_IMAGE_LAYER_REVISION` whenever the runner Docker layer changes
without a cgc version change. Runtime layout no longer exposes a host
`venvRoot` or CGC executable path, and provider settings that still define
`venvRoot` are rejected as stale configuration.

`to_container_path()` (host path → in-container POSIX path, Windows drive letter
stripped, no-op on POSIX) is re-exported here for existing importers; its
canonical home is `providers/context_common.py` since the GitHub #58 fix needed
it from `cgc/seed.py`, which cannot import the `cgc.context` package facade
without tripping the star-import diamond. The layout
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

| Finding | Anchor | Source |
| --- | --- | --- |
| Lifecycle CGC modules use these layout and cleanup helpers before running or installing CGC. | "return cgc_runtime_layout("; "cleanup_cgc_runtime_artifacts("; "cleanup_cgc_runtime_artifacts("; `cgc_install_preflight`; `cgc_start_preflight`; "def cgc_runner_image_build(" | mcp/src/agents_remember/providers/cgc/lifecycle/core.py:50-50; mcp/src/agents_remember/providers/cgc/lifecycle/core.py:300-300; mcp/src/agents_remember/providers/cgc/lifecycle/installation.py:136-149; mcp/src/agents_remember/providers/cgc/lifecycle/installation.py:185-185; mcp/src/agents_remember/providers/cgc/lifecycle/process_control.py:162-172; mcp/src/agents_remember/providers/cgc/lifecycle/runner.py:37-37 |

## Update History

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 1 citation item; scoped citation check now passes.

- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  `cgc_runtime_layout` was re-signed onto `CgcRepo` + the optional `CgcInstance` / `CgcWatcher` /
  `CgcBackend` bundles (with `DEFAULT_CGC_*` frozen singletons as defaults). The resolved
  `CgcRuntimeLayout` is unchanged. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-06-10T07:05+02:00 — `to_container_path` moved to `providers/context_common.py` (canonical home); this module keeps a commented re-export so existing `cgc.context.core`/facade importers are unchanged (GitHub #58).
- 2026-06-10T05:30+02:00 — `_cgc_runner_image` is now public `cgc_runner_image()` with a docstring naming it the single source of truth (GitHub #50); `providers/settings.py` and a regression test depend on it.
- 2026-06-09T22:10+02:00 — `_cgc_runner_image()` now appends `CGC_RUNNER_IMAGE_LAYER_REVISION` to the tag (`agents-remember/codegraphcontext:0.4.10-ar1`) so Docker-layer-only changes (e.g. the watch-guard entrypoint) trigger image rebuilds on install.
- 2026-05-29T18:35+02:00: Split `core.py` (668->522): extracted `materialize.py` (runtime dir/config writers) and `cleanup.py` (stale-artifact removal); `core.py` keeps the `CgcRuntimeLayout` dataclass, settings-derived construction, and `to_container_path` (commit `01f503d`).
- 2026-05-29T07:19+02:00: Updated after adding `to_container_path`, the `container_runtime_root` / `container_code_repo_root` properties, and `env(for_container=...)` so CGC bind-mount targets, working dir, and container environment render as driveless POSIX paths on Windows hosts.
- 2026-05-28T13:40+02:00: Updated after CGC layout removed host venv path fields and began rejecting stale `venvRoot` provider settings.
- 2026-05-26T13:58+02:00: Updated after CGC layouts gained backend container and Docker network fields for runner connectivity.
- 2026-05-26T12:51+02:00: Updated after CGC layout gained Docker runner fields and stopped creating host venv directories.
- 2026-05-25T19:16+02:00: Created when `context_providers.py` was split into `context.py` plus provider-specific context modules.
