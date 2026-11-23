# mcp/pyproject.toml

## Governing Overview

[overview.md](overview.md)

## Purpose

`mcp/pyproject.toml` defines the installable MCP package metadata, PyPI README
metadata, package version, license and project links, runtime dependency boundary, optional development
dependencies, console scripts, and setuptools package discovery root.

The project declares the MIT license and Homepage, Documentation, Repository and Issues links
through `[project.urls]`.

## Current source account

Package data explicitly includes cli/*.mjs in addition to package_data assets, so the installed wheel carries the native JavaScript bridge next to its Python caller. Development sandbox tooling under scripts remains outside this package.

## Code Commentary

### Logic

The package builds with `setuptools`, publishes as `agents-remember-mcp`, uses
`mcp/README.md` as its package README, and supports exactly the Python 3.14 minor line
(`>=3.14,<3.15`).
Runtime dependencies include `mcp`, `pydantic`, `tiktoken`, `fastapi` (built-in
`fastapi.sse`), `uvicorn`, and `websockets`: Pydantic owns public response validation,
tiktoken backs response token accounting, and FastAPI/uvicorn serve the local dashboard. `python-multipart` is also declared as a runtime dependency. `watchfiles` (`>=1.1,<2`) is the native filesystem watcher behind the dashboard's
change-driven projection pacing (`serving/change_watcher.py`); the serving layer degrades
loudly to interval-driven full refreshes when it is missing, so the dependency is core for
adaptive behaviour, not for the daemon to run at all. The webstack is a **core** dependency (not an optional
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
`dashboard`) and `agents-remember-mcp`
(`agents_remember.mcp.__main__:main`, the MCP server). setuptools discovers import
packages from `mcp/src`. The `[tool.setuptools.package-data]` block ships package-owned
runtime assets — `package_data/**/*` plus `package_data/benchmarks/.gitignore` — so
`runtime_install` can reconcile the runtime docs and provider assets into a coordinator
from a pip/uvx install with no source checkout. Skills remain served from the package
rather than being copied into the coordinator. Dotfiles need their
own explicit entry; `**/*` does not match them. The separate `cli/*.mjs` declaration
also carries the native JavaScript bridge beside its Python caller; it is not runtime scaffold
content under `package_data`, and development sandbox tooling under `scripts` stays outside the wheel.

### Classifiers Declare The Supported Floor And Platforms

`classifiers` is not decoration here — it is a place a consumer can read the supported
interpreter line and the supported platforms without cloning. It lists Python 3.14 only
(matching `requires-python = ">=3.14,<3.15"`) and the two operating-system classifiers
`POSIX :: Linux` and `MacOS`. Windows is supported **through WSL**, which presents as Linux to the
interpreter and therefore deliberately carries no separate classifier — the absence is a decision,
not an omission, and the inline comment in the file records it.

The language line agrees with `requires-python` here. The repository-root `[tool.ruff]
target-version` stays `py313` as an explicitly reasoned **non-runtime syntax-rewrite policy**
(one comment line states the reason), while Pyright and the workflows select 3.14. The managed
development runtime, Dagger graph, GitHub packaging workflow, and GitHub deterministic quality
workflow all select exact 3.14.8. Acceptance remains lifecycle-owned; Dagger executes the acceptance profiles, while the
GitHub jobs prove deterministic lint/package behavior under the same runtime and are not
a per-minor interpreter matrix.

### The Dashboard Bundle Is Packaged But Not Committed

`package_data/**/*` is **recursive** (setuptools globs package data with `recursive=True`), so
whatever is present under `package_data` at build time ships. That deliberately includes the
cockpit bundle at `package_data/dashboard/` and its `package_data/dashboard.fingerprint` sidecar,
neither of which is in version control.

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
`server_info` reports, and it stays aligned with
`agents_remember.mcp.SERVER_VERSION` (see invariant below).

### The Parser Wheel Comment Names The Recorded Platforms

The comment above the `tree-sitter` dependency pins states which platform wheels the lock records
cover — manylinux x86_64 and aarch64, musllinux x86_64, and macOS x86_64 and arm64 — and
explicitly records the two absent cells (`tree-sitter` and `tree-sitter-typescript` musllinux
aarch64, which need a source build). The comment is a checked statement about the lock's records,
not a coverage promise.

### The SQLite Binding Is A Binary Wheel With A Build-Time Capability

`apsw==3.53.4.0` is the repository's binary-wheel SQLite binding for the derived knowledge index.
Three facts justify the exact pin:

1. **Why APSW at all.** The index is built and queried through APSW (index build, query and projection
   modules); this surface does not use the standard library's `sqlite3` binding.
2. **Why the pin is exact, not a range.** The index's schema relies on build-time SQLite
   features (STRICT tables, deferrable foreign keys, `RAISE(ABORT)` triggers, recursive CTEs), so the capability belongs to the specific wheel rather than to the APSW project version line. An exact
   pin names the wheel version whose required features must be checked on each supported platform,
   rather than assuming that another resolution has them.
3. **What was actually proven, and what was not.** The leaf's spike installed the pinned release from a prebuilt
   `cp313` manylinux x86_64 wheel (no compiler, no source build, no fallback) and exercised one-row
   changeset attach/diff/apply, an aborting conflict, a consistent WAL-inclusive backup and the leaf's DDL; the
   lock now resolves the pin to `cp314` wheels after the Python 3.14 move. macOS
   wheels exist in the lock (x86_64 and arm64) but **no macOS host executed the spike**, so the macOS
   classifier's support claim remains an unresolved acceptance item for the owning seat — it is disclosed rather
   than narrowed silently.

The pin is recorded in three places that must agree: `dependencies` here, `mcp/requirements.txt`, and the single
`apsw` entry in `mcp/uv.lock`. The in-file comment above the entry is the durable record of the reason, so a
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
  state whose documented remedy is `npm --prefix dashboard ci && npm --prefix dashboard run build && python3 scripts/sync-dashboard.py`.
- The wheel and the sdist must both carry the bundle. The release workflow, not this file, is where
  that is enforced.
- The supported minor line is stated by `requires-python` and the Python classifier here; the
  repository-root `[tool.ruff] target-version` is an explicitly reasoned non-runtime
  syntax-rewrite policy (`py313`) and is not a second runtime declaration. Raising or lowering
  the runtime declarations without the policy comment is a defect; the Dagger acceptance image is
  separate execution provenance, not a substitute for the exact runtime contract.
- The absence of a Windows classifier is deliberate (Windows is supported through WSL). Do not add
  one to "fix" the list.

## Evidence

### Repo-Internal References

- The quality plan composes the selected development tools; coverage and production CRAP remain diagnostic. [1]





- Public response contracts depend on Pydantic and token accounting depends on tiktoken. [3]


- The derived knowledge index uses an exact-pinned SQLite binding, with its schema-feature reason recorded inline above the entry. [4]

- The same exact pin in the checkout requirements manifest, which must agree with this file. [5]

- The locked resolution carries the pin as a direct requirement plus the platform wheel set the exact pin selects. [6]

- Production complexity scoring loads Radon and refuses when its development dependency is unavailable. [7]
- The MCP console entry point resolves through `agents_remember.mcp.__main__`. [8]




- MCP server payloads report `SERVER_VERSION`, resolved by the kernel helper from installed package metadata with the source-checkout release fallback. [9]












- The package README documents the installable MCP command and setup-oriented tool surface for PyPI/package readers: the What you need, Install steps, Start and stop the dashboard and the host, Tools, and More sections. [10]


- `runtime_install` reconciles packaged runtime docs and provider assets into a coordinator; skills remain served from the package. [11]
- The release job builds the frontend, places the bundle, packages with the locked project venv, and then verifies both distributions carry the bundle and its fingerprint sidecar. [12]
- The placement step whose output this recursive glob picks up at build time. [13]
- Both generated dashboard paths are git-ignored, with the reason recorded inline. [14]
- An installation with no bundle reports the absence instead of failing, which is why packaging needs no guard. [15]


- Ruff keeps its syntax target at Python 3.13; this is explicitly independent from runtime requirements and Pyright language configuration. [16]


- Package metadata directly bounds the interpreter line and declares its Python classifier. [17]


- Root pytest configuration selects four workers by default. [2]

- Package data declares the general package-data tree and the canvas Markdown and JavaScript resources. Tests pin the general and Markdown patterns and check the generated capability copy against the source. [18]
