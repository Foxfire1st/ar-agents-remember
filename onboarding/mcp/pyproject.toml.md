# mcp/pyproject.toml

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/pyproject.toml`                       |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-15T22:40+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/pyproject.toml` defines the installable MCP package metadata, PyPI README
metadata, package version, runtime dependency boundary, optional development
dependencies, console script, and setuptools package discovery root.

## Code Commentary

### Logic

The package builds with `setuptools`, publishes as `agents-remember-mcp`, uses
`mcp/README.md` as its package README, and supports exactly the Python 3.13 minor line
(`>=3.13,<3.14`).
Runtime dependencies stay intentionally narrow but now include `mcp`,
`pydantic`, `tiktoken`, and — for the slice-04 dashboard serving layer —
`fastapi` (built-in `fastapi.sse`), `uvicorn`, and — for the slice 6d-2 Mode B2
terminal — `websockets`: Pydantic owns public response validation, tiktoken
backs response token accounting, FastAPI/uvicorn serve the local dashboard, and
`websockets` is uvicorn's WebSocket protocol implementation for the
`/api/terminal/{session}` terminal bridge (plain `uvicorn` ships no WS impl, so a
live WebSocket needs it). Slice 6f adds `python-multipart`, which FastAPI requires to
parse the `multipart/form-data` upload on `POST /api/terminal/{session}/image` (its
`UploadFile`/`File` form support fails without it). 260712-PTS-L3 adds `watchfiles`
(`>=1.1,<2`), the inotify-backed filesystem watcher behind the dashboard's change-driven
projection pacing (`serving/change_watcher.py`) — a decision-logged new runtime dependency
(neither `watchfiles` nor `watchdog` existed in the tree before); the serving layer degrades
loudly to fixed-interval ticking when it is missing, so the dep is core for the adaptive
behaviour, not for the daemon to run at all. The webstack is a **core** dependency (not an optional
extra) so `agents-remember dashboard` works on a plain install. Development-only
quality tools live under the `dev` optional dependency group: Coverage.py, httpx
(the FastAPI `TestClient` backend), pytest, pytest-cov, pytest-xdist, Pyright, Radon, and Ruff.
Ruff is an exact 0.16.1 pin shared with the checkout requirements, so a worktree and a package-dev
environment enforce the same stable rule set instead of interpreting the same configuration under
different Ruff releases.
The xdist range is deliberately bounded to major version 3 because root pytest `addopts` owns
`-n=4`; the dependency supplies that executor while the root configuration governs raw and
wrapped pytest uniformly.

Two console scripts are declared: the umbrella `agents-remember`
(`agents_remember.cli.__main__:main`, the front door for subcommands such as
`dashboard`) and the unchanged `agents-remember-mcp`
(`agents_remember.mcp.__main__:main`, the MCP server — kept standalone because
harness MCP configs launch it by that exact name). setuptools discovers import
packages from `mcp/src`. The `[tool.setuptools.package-data]` block ships the installable
runtime scaffold — `package_data/**/*` (AGENTS.md templates, skills, provider
assets, system defaults) plus the benchmark `package_data/benchmarks/.gitignore`
— so `runtime_install` can reconcile those package-owned assets into a
coordinator from a pip/uvx install with no source checkout. Dotfiles need their
own explicit entry; `**/*` does not match them.

### Classifiers Declare The Supported Floor And Platforms (260731-EFA-L2)

`classifiers` is not decoration here — it is the one place a consumer can read the supported
interpreter line and the supported platforms without cloning. It lists Python 3.13 only
(matching `requires-python = ">=3.13,<3.14"`) and the two operating-system classifiers
`POSIX :: Linux` and `MacOS`. Windows is supported **through WSL**, which presents as Linux to the
interpreter and therefore deliberately carries no separate classifier — the absence is a decision,
not an omission, and the inline comment in the file records it.

The language line is an agreement between `requires-python` here and `[tool.ruff] target-version`
in the repository-root `pyproject.toml` (pinned to `py313`). The managed development runtime,
Dagger graph, GitHub packaging workflow, and GitHub deterministic quality workflow all select exact
3.13.15. Dagger alone owns acceptance; the GitHub jobs prove deterministic lint/package behavior
under the same runtime and are not a per-minor interpreter matrix.

### The Dashboard Bundle Is Packaged But Not Committed (260731-EFA-L1)

`package_data/**/*` is **recursive** (setuptools globs package data with `recursive=True`), so
whatever is present under `package_data` at build time ships. That deliberately includes the
cockpit bundle at `package_data/dashboard/` and its `package_data/dashboard.fingerprint` sidecar,
neither of which is in version control (master decision OQ6, 2026-07-31).

The consequences a packager must know:

- **The release job owns the build.** `publish-mcp-to-pypi.yml` runs `npm run build` and then
  `scripts/sync-dashboard.py` **before** `python -m build`, because package data is read from the
  source tree at build time. It then asserts both the wheel and the sdist contain
  `agents_remember/package_data/dashboard/index.html` and
  `agents_remember/package_data/dashboard.fingerprint`, so "the release quietly shipped no
  dashboard" is a build failure rather than a support ticket.
- **Building from a checkout with no bundle still succeeds.** The glob simply matches nothing.
  Packaging does not fail; the installed server reports the absence itself (`serving/static.py`
  answers 503 naming the build command), which is why no packaging-time guard is needed here.
- **Nothing in this file needs to change when the frontend changes.** The declaration is a glob
  over a directory, not a manifest of assets.

The package `version` tracks the release line. Its exact current value lives in
the source rather than being repeated here; it is the same string
`runtime_install` and `server_info` report, and it stays aligned with
`agents_remember.mcp.SERVER_VERSION` (see invariant below).

### The SQLite Binding Is A Binary Wheel With A Build-Time Capability (260915-KS-L1)

`apsw==3.53.4.0` is the repository's first binary-wheel runtime dependency whose required capability is a
**build-time SQLite option** rather than a Python API. Three facts justify the exact pin:

1. **Why APSW at all.** APSW is the only declared binding that exposes SQLite's session and changeset machinery —
   the operations a later merge leaf needs to capture and apply a candidate's changes. The standard library's
   `sqlite3` module exposes neither session nor changeset, so the choice is not a preference between two bindings
   with the same reach.
2. **Why the pin is exact, not a range.** Session support is compiled in through SQLite's `ENABLE_SESSION` build
   option, so the capability belongs to the specific wheel rather than to the APSW project version line. An exact
   pin makes "this wheel has session support" a proven property of the locked artifact instead of an assumption
   about whatever resolution picks next; a range would silently admit a build without it.
3. **What was actually proven, and what was not.** The leaf's spike installed the pinned release from a prebuilt
   `cp313` manylinux x86_64 wheel (no compiler, no source build, no fallback) and exercised one-row
   changeset attach/diff/apply, an aborting conflict, a consistent WAL-inclusive backup and the leaf's DDL. macOS
   wheels for `cp313` exist in the lock (x86_64 and arm64) but **no macOS host executed the spike**, so the macOS
   classifier's support claim remains an unresolved acceptance item for the owning seat — it is disclosed rather
   than narrowed silently.

The pin is recorded in three places that must agree: `dependencies` here, `mcp/requirements.txt`, and the single
added `apsw` entry in `mcp/uv.lock`. The in-file comment above the entry is the durable record of the reason, so a
later reader does not have to reconstruct it from a report.

### Invariants And Boundaries

- Runtime package dependencies should stay separate from source-development
  quality dependencies; Pydantic and tiktoken are runtime dependencies because
  modeled responses and token metadata are part of normal tool output, and
  FastAPI/uvicorn are runtime dependencies because the dashboard ships in the
  package and must run on a plain install. httpx, by contrast, is dev-only — it
  only backs the FastAPI `TestClient` in tests.
- Release version bumps should keep this project version aligned with
  `agents_remember.mcp.SERVER_VERSION` so installed server payloads report the
  same version that PyPI installs.
- Pyright, CRAP-Calculator, and the source quality wrapper rely on the `dev`
  optional dependency group, not the base MCP runtime dependency set.
- The package discovery root is `src`; package modules should remain under
  `mcp/src/agents_remember/`.
- The installable runtime scaffold is shipped as `package-data` under
  `agents_remember/package_data/`; assets `runtime_install` reconciles into a
  coordinator must live inside that tree to be packaged by a pip/uvx install.
- `package_data/dashboard/` and `package_data/dashboard.fingerprint` are **generated at release
  time and git-ignored**. Do not commit them, do not add them to this file as explicit entries, and
  do not make packaging fail when they are absent — a source build without Node is a supported
  state whose documented remedy is `npm --prefix dashboard run build`.
- The wheel and the sdist must both carry the bundle. The release workflow, not this file, is where
  that is enforced.
- The supported minor line is stated by `requires-python` and the Python classifier here plus
  `[tool.ruff] target-version` in the repository-root `pyproject.toml`. Raising or lowering only
  one of those declarations is a defect; the Dagger acceptance image is separate execution
  provenance, not a substitute for the exact runtime contract.
- The absence of a Windows classifier is deliberate (Windows is supported through WSL). Do not add
  one to "fix" the list.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The quality plan composes the selected development tools; coverage and production CRAP remain diagnostic. | `quality_steps` | mcp/test_support/agents_remember_test_support/code_quality/quality_plan.py:136-168 |
| Root pytest configuration selects four workers by default. | "-n=4" | pyproject.toml:164; pyproject.toml:186-186 |
| Public response contracts depend on Pydantic and token accounting depends on tiktoken. | "pydantic>=2,<3"; "tiktoken>=0.12,<1" | mcp/pyproject.toml:22-23; mcp/pyproject.toml:28-29 |
| The knowledge store's SQLite binding is exact-pinned, with the session/build-option reason recorded inline above the entry. | "apsw==3.53.4.0" | mcp/pyproject.toml:21-26 |
| The same exact pin in the checkout requirements manifest, which must agree with this file. | "apsw==3.53.4.0" | mcp/requirements.txt:2-2 |
| The locked resolution carries the pin as a direct requirement plus the platform wheel set the exact pin selects. | "{ name = \"apsw\", specifier = \"==3.53.4.0\" }"; `apsw` | mcp/uv.lock:43-43; mcp/uv.lock:102-111 |
| Production complexity scoring loads Radon and refuses when its development dependency is unavailable. | `complexity_blocks` | mcp/test_support/agents_remember_test_support/code_quality/crap_calculator.py:221-228 |
| The MCP console entry point resolves through `agents_remember.mcp.__main__`. | "from .server import main" | mcp/src/agents_remember/mcp/__main__.py:5-5 |
| MCP server payloads report `SERVER_VERSION`, resolved by the kernel helper from installed package metadata with the source-checkout release fallback. | `_resolve_server_version` | mcp/src/agents_remember/kernel/primitives/version.py:14-23 |
| The package README documents the installable MCP command and setup-oriented tool surface for PyPI/package readers. | `## Quickstart`, `## Install And Run` | mcp/README.md:15-48; mcp/README.md:66-114 |
| `runtime_install` reconciles the `package_data/` runtime scaffold shipped by this `package-data` declaration into a coordinator. | `runtime_install` | mcp/src/agents_remember/install/runtime.py:880-880 |
| The release job builds the frontend, places the bundle, packages with the locked project venv, and then verifies both distributions carry the bundle and its fingerprint sidecar. | "npm run build"; "mcp/.venv/bin/python scripts/sync-dashboard.py"; ".venv/bin/python -m build"; "agents_remember/package_data/dashboard.fingerprint" | .github/workflows/publish-mcp-to-pypi.yml:82-82; .github/workflows/publish-mcp-to-pypi.yml:91-91; .github/workflows/publish-mcp-to-pypi.yml:95-95; .github/workflows/publish-mcp-to-pypi.yml:111-111 |
| The placement step whose output this recursive glob picks up at build time. | "TARGET = REPO_ROOT"; "def sync() -> int:" | scripts/sync-dashboard.py:38-38; scripts/sync-dashboard.py:46-46; scripts/sync-dashboard.py:138-138; scripts/sync-dashboard.py:153-153; scripts/sync-dashboard.py:227-227 |
| Both generated dashboard paths are git-ignored, with the reason recorded inline. | "/mcp/src/agents_remember/package_data/dashboard/", "/mcp/src/agents_remember/package_data/dashboard.fingerprint" | .gitignore:26-27 |
| An installation with no bundle reports the absence instead of failing, which is why packaging needs no guard. | "no built cockpit bundle in this installation", "No dashboard bundle at %s; serving 503 on the static surface. Build it with: %s" | mcp/src/agents_remember/serving/static.py:73-73; mcp/src/agents_remember/serving/static.py:123-123 |
| The Ruff `target-version` that must track the supported minor declared here lives in the repository-root project file. | "py313" | pyproject.toml:4-4 |
| Package metadata directly bounds the interpreter line and declares its Python classifier. | "requires-python = \">=3.13,<3.14\""; "Programming Language :: Python :: 3.13" | mcp/pyproject.toml:10-18 |


## Update History
- 2026-09-18T01:52:52+00:00: Generated citation repair: "-n=4" repointed to pyproject.toml:186-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "-n=4" repointed to pyproject.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `runtime_install` repointed to mcp/src/agents_remember/install/runtime.py:880-880. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `sync` in the row 179 of this card from scripts/sync-dashboard.py:38-38 to scripts/sync-dashboard.py:153-154, the extent of the construct the claim is about (the checker named line(s) [153] as its live location)
- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `-n=4` in the row 168 of this card from pyproject.toml:160-160 to pyproject.toml:164, the extent of the construct the claim is about (the checker named line(s) [164, 267, 280] as its live location); re-pointed `TARGET = REPO_ROOT` in the row 179 of this card from scripts/sync-dashboard.py:153-154 to scripts/sync-dashboard.py:38, the extent of the construct the claim is about (the checker named line(s) [38] as its live location)
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): recorded the new `apsw==3.53.4.0` runtime dependency — the knowledge store's SQLite binding, the only declared binding that exposes SQLite's session/changeset machinery, exact-pinned because session support is a build-time SQLite option (`ENABLE_SESSION`) rather than a property of the version line. Documented the three places that must agree (this file, `mcp/requirements.txt`, `mcp/uv.lock`), what the leaf's spike actually proved (a prebuilt `cp313` manylinux x86_64 wheel, changeset apply, an aborting conflict, a consistent backup) and what it did not (no macOS execution, carried as an unresolved acceptance item). Corrected the Pydantic/tiktoken citation range, which the six-line insertion shifted from `:22-23` to `:28-29`, and added the pin's three evidence rows. Verification metadata remains closeout-owned.
- 2026-09-13T17:20:55+00:00: Generated citation repair: "-n=4" repointed to pyproject.toml:160-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 27fb62d06e30428d8072f72f17b576fb89ccd41fd08d4f26b1a4a9e383adc055; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: ".venv/bin/python -m build", "agents_remember/package_data/dashboard.fingerprint", "mcp/.venv/bin/python scripts/sync-dashboard.py", "npm run build" repointed to .github/workflows/publish-mcp-to-pypi.yml:111-111, .github/workflows/publish-mcp-to-pypi.yml:82-82, .github/workflows/publish-mcp-to-pypi.yml:91-91, .github/workflows/publish-mcp-to-pypi.yml:95-95. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: "-n=4" repointed to pyproject.toml:145-145. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-07T00:34+02:00 — Reconciled current source anchors and diagnostic/four-worker policy; removed obsolete test-proof claims without altering verification pins.

- 2026-08-29T16:12+02:00 — Migrated package authority from the former 3.11 floor and three-minor
  classifier set to the single supported Python 3.13 line, bounded at `<3.14`, and aligned Ruff,
  Dagger, CI, release, and the managed exact 3.13.15 source build. Verification remains
  closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: removed the stale CI-minor-matrix claim. Package metadata
  still declares Python 3.11-3.13 and a 3.11 floor, while acceptance now runs once in the pinned
  Dagger Ubuntu graph. Verification remains closeout-owned.
- 2026-08-12T20:25+02:00 — L23 curator: re-read package identity after the kernel version helper split and re-anchored the claim to `_resolve_server_version` plus `SERVER_VERSION`; verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T10:08+02:00 — No content impact: bumped the package release identity to `3.0.0rc7`; it remains
  aligned with the kernel `SERVER_VERSION` fallback. No dependency, entry-point, classifier,
  package-data, or discovery contract changed. Verification metadata remains pinned until
  closeout stamps the release commit.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: replaced the permissive Ruff development range
  with the repository's exact 0.16.1 pin so master and leaf lint results are deterministic.

- 2026-08-12T00:20+02:00 — Corrected execution ownership: the development extra supplies
  pytest-xdist, while root pytest `addopts` owns the `-n=auto` default. Verification metadata
  remains pinned until closeout.

- 2026-08-11T23:56+02:00 — Added pytest-xdist to the development quality-tool boundary because
  the repository-owned pytest rail now runs with automatic worker selection. Verification metadata
  remains pinned until closeout stamps the code commit.

- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-03T02:52:34+02:00 — W3-B04 curator: curated 12 table citations (12 total), supplying exact anchors and paths; the scoped fixer generated all final extents.
- 2026-07-31T16:45+02:00 — 260731-EFA-L2 (R13, supported-platform decision of 2026-07-31): added a
  `classifiers` block declaring Python 3.11/3.12/3.13 and the `POSIX :: Linux` / `MacOS` platforms,
  with an inline comment recording that Windows is supported through WSL and therefore carries no
  classifier. Documented the new block, the deliberate absence of a Windows classifier, and the
  three-way floor agreement between `requires-python`, the root `[tool.ruff] target-version` (pinned
  to `py311` by the same leaf), and the CI interpreter matrix; added the two references that
  agreement depends on. No dependency, entry-point, package-data, discovery-root, or version
  contract changed. Verification metadata pinned until closeout stamps the L2 commit.
- 2026-07-31T04:28+02:00 — 260731-EFA-L1: recorded that `package_data/**/*` is recursive and now
  carries a cockpit bundle that is **not** in version control. The release job builds the frontend
  and runs `scripts/sync-dashboard.py` before `python -m build`, then asserts the wheel and sdist
  both contain the bundle and `dashboard.fingerprint`; a checkout with no bundle still packages
  successfully because the glob matches nothing and the server reports the absence itself. No
  dependency, entry-point, discovery-root, or version contract changed. Verification metadata
  pinned to the pre-leaf source authority until closeout stamps the code commit.
- 2026-07-12T20:24+02:00 — 260712-PTS-L3: added `watchfiles` (`>=1.1,<2`) as a **core** runtime
  dependency — the inotify backend for `serving/change_watcher.py`'s change-driven projection
  pacing (decision-logged; no prior watch library in the tree). Missing-wheel behaviour is a loud
  fixed-interval fallback, never a crash. Verification metadata pinned until closeout stamps the
  PTS-L3 commit.
- 2026-07-12T12:07+02:00 — 260712-TRH-L1 bumps version 3.0.0rc4 -> 3.0.0rc5 (PEP 440 prerelease)
  with no dependency, entry-point, package-data, or build-system contract change. Corrected the stale
  `2.9.3` commentary to version-generic wording so later release bumps do not drift it.

- 2026-07-08T15:45+02:00 — No content impact: 260707-HFX2-L7 bumps version 3.0.0rc3 ->
  3.0.0rc4 (PEP 440 prerelease) for the hotfix release tail; no dependency, entry point, package
  data, or build-system contract changed.
- 2026-07-07T21:10+02:00 — No content impact: release 4922146 bumped version 3.0.0rc2 -> 3.0.0rc3 (PEP 440 prerelease); no dependency or build-system change. (Reconciliation: direct owner commit between the L17 and L18 closeouts.)
- 2026-07-03T12:05+02:00 — No content impact: 260703 L4 bumped version 3.0.0rc1 -> 3.0.0rc2 (PEP
  440 prerelease); no dependency or build-system change.
- 2026-07-03T11:20+02:00 — No content impact: L14 bumped version 2.9.3 -> 3.0.0rc1 (PEP 440 prerelease); no dependency or build-system change.
- 2026-06-28T19:10+02:00 — Main-carryover reconciliation (PR #95, code 84e95ad): version reflects the main releases merged onto the series — `2.9.2` (benchmark provider-isolation / hermetic setup) and `2.9.3` (resolve a worktree contract from `worktree_name`); no packaging-contract change, and the documented `version` still tracks `SERVER_VERSION`. Corrected the stale `2.7.0` verification note in the body to `2.9.3`.
- 2026-06-19T20:30 — Task 6 slice 6f: added `python-multipart` (`>=0.0.9,<1`) as a **core** runtime dependency — FastAPI needs it to parse the `multipart/form-data` `UploadFile` on `POST /api/terminal/{session}/image` (the screenshot upload). Verification metadata pinned until closeout stamps the 6f code commit.
- 2026-06-18T16:10+02:00 — Task 6 slice 6d-2: added `websockets` (`>=12,<16`) as a **core** runtime dependency — uvicorn's WebSocket protocol impl for the Mode B2 `/api/terminal/{session}` bridge (plain `uvicorn` ships none). Verification metadata pinned until closeout stamps the 6d-2 code commit.
- 2026-06-14T11:30+02:00 — Slice 04 commit 4a: added `fastapi` + `uvicorn` as **core** runtime dependencies (the dashboard webstack, forced core so `agents-remember dashboard` works on a plain install), `httpx` to the `dev` group (FastAPI `TestClient`), and the umbrella `agents-remember` console script alongside the unchanged `agents-remember-mcp`. Verification metadata pinned until closeout stamps the 4a code commit.
- 2026-06-12T19:06+02:00 — No content impact: version bumped to 2.9.1 for the issue #83 closeout committed-range fix release; packaging contract unchanged.
- 2026-06-11T15:20+02:00 — No content impact: version bumped to 2.9.0 for the carryover artifact coverage release; packaging contract unchanged.
- 2026-06-10T10:26+02:00 — No content impact: version bumped to 2.8.0 for the GitHub #54 release (lifecycle-long stale-base prevention); the packaging contract this sidecar describes is unchanged.
- 2026-06-10T08:15+02:00 — Version bumped to 2.7.0 for the GitHub #53/#58 release (async worktree provider setup + Windows seed fix).
- 2026-06-10T06:05+02:00 — No content impact: version bumped to 2.6.0 for the memory-integrity release (GitHub #56); package metadata semantics unchanged.
- 2026-06-10T05:45+02:00 — Version bumped to 2.5.2 for the carryover response compaction patch (GitHub #52).
- 2026-06-10T05:30+02:00 — Version bumped to 2.5.1 for the tool-reliability release (stdio subprocess hygiene #49, seed stall watchdog, runner-image derivation #50, GrepAI indexing parity, crash-loop readiness, response token budgets).
- 2026-06-09T22:10+02:00 — Version bumped to 2.5.0 for the CGC persistence/readiness release (FalkorDB `dataDestination` mount fix, graph-content readiness probe with `indexing` state, degraded-state propagation, summary `indexing` list, watcher self-heal entrypoint, `--remove-orphans` hygiene).
- 2026-06-09T15:39+02:00: Bumped the documented package `version` to `2.4.2` for the L-01 lifecycle skill consolidation patch release; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-08T12:22+02:00: Bumped the documented package `version` to `2.4.1`
  for the runtime asset sync and provider validation patch release; still
  tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-08T08:33+02:00: Bumped the documented package `version` to `2.4.0` for the harness-local starter renderer and Python hook command rendering release; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-04T23:15+02:00: Bumped the documented package `version` to `2.3.3` for the provider watcher rebind and Docker-safe provider identity patch; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-04T18:52+02:00: Bumped the documented package `version` to `2.3.2` for the runtime skill refresh patch; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-03T19:25+02:00: Bumped the documented package `version` to `2.3.1` for the MCP package README correction patch; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-03T18:58+02:00: Bumped the documented package `version` to `2.3.0` for the harness starter-package / package-first install ergonomics release; still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-03T04:25+02:00: Bumped the documented package `version` to `2.2.0` (mcp 2.2.0 release for the lifecycle collaboration loop and C-09 source-branch contract refresh); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-02T18:35+02:00: Bumped the documented package `version` to `2.1.0` (mcp 2.1.0 release); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-02T05:10+02:00: Bumped the documented package `version` to `2.0.0` (mcp 2.0.0 — the `l-01-session-job-lifecycle` skill lifecycle reshape, a major/breaking release); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-02T03:30+02:00: Bumped the documented package `version` to `1.0.2` (mcp 1.0.2 — git-workflow.md + PR-gated landing); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Bumped the documented package `version` to `1.0.1` (mcp 1.0.1 — worktree cgc DNS-label fix); still tracks `SERVER_VERSION`. Verification metadata pinned until closeout.
- 2026-05-31T12:30+02:00 — Bumped the documented package `version` to `1.0.0` (1.0.0 review remediation); still tracks `SERVER_VERSION`.
- 2026-05-31T01:06+02:00: Bumped the documented package `version` to `0.9.6` (MCP 0.9.6, `w-02-light-task-workflow` skill design section); still tracks `SERVER_VERSION`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T22:29+02:00: Bumped the documented package `version` to `0.9.5` for the S6 token-counter release; still tracks `SERVER_VERSION`. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T21:22+02:00: Realigned to MCP `0.9.4` after the 0.9.0–0.9.4 run; version still tracks `SERVER_VERSION`. Documented the `package-data` runtime-scaffold packaging block (the card body previously described the `0.3.0` release).
- 2026-05-29T21:00+02:00: Bumped the package `version` to `0.3.0` for the MCP `0.3.0` release (act-by-default `dry_run` flip), kept aligned with `SERVER_VERSION`.
- 2026-05-28T19:52+02:00: Updated after Pydantic and tiktoken became MCP runtime dependencies and Pyright joined the dev quality dependency group.
- 2026-05-28T15:43+02:00: Updated while preparing MCP package release `0.2.0`, documenting package/server version alignment, and wiring the dedicated MCP README into package metadata. Verification metadata remains pinned until closeout commits the source change.
- 2026-05-24T06:43+02:00: Created after the MCP package gained explicit development dependencies for the source quality suite.
