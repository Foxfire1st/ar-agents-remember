# mcp/src/agents_remember/providers/cgc/context/core.py

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

## Evidence

### Repo-Internal References

- Lifecycle CGC modules use these layout and cleanup helpers before running or installing CGC. [1]
