# mcp/src/agents_remember/serving/build_info.py

## Governing Overview

[serving overview](overview.md)

## Purpose

The serving **build stamp** resolves once per Python process which exact runtime is answering:
package version, Python-source content digest, interpreter, package root, best-effort checkout
commit, boot time, dashboard fingerprint, and proven-dirty state. Dashboard and MCP surfaces share
that one immutable value so a stale or equal-version candidate is visible rather than guessed.

## Code Commentary

### 260731-EFA-L4 Current Delta — `payload()` Returns A Declared Model

`ServingBuild.payload()` cit:(["def payload(self) -> ServingBuildPayload:"], mcp/src/agents_remember/serving/build_info.py:59-59) no longer hand-builds a `dict[str, Any]`. It returns
**`ServingBuildPayload`**, owned by `models/core.py`, a strict `BaseModel` carrying
`version`, `bootedAt`, `sourceDigest`, `pythonExecutable`, `packageRoot`, `commit`,
`dashboardBuild`, and `dirty`. A model
rather than an untyped dict because this object is now a *field* of the served state contract
(`served_state.ServedWorkspaceProjection.servingBuild`), and a contract whose members are
untyped dicts only pretends to be one.

**The honest-unknown rule moved from a chain of `if` statements into `None` + the caller's
`exclude_none=True`, and it is the same rule.** The old `payload()` appended `commit`,
`dashboardBuild` and `dirty` only when each was set; the new one always constructs them and
declares them optional, and every caller serializes with
`model_dump(mode="json", exclude_none=True)` (`served_state.served_state_tail`), so an
unresolvable commit, an unbuilt dashboard bundle and an unprovable tree are all OMITTED exactly
as before. The one conditional that survives in code is the dirty collapse — `dirty=True if
self.dirty else None` — because the tri-state must not leak: proven-clean (`False`) and
unprovable (`None`) both drop out, so the wire never fabricates a "clean" fact. Absence is not a
pristine claim.

The current `payload` method returns the declared serving-build model (mcp/src/agents_remember/serving/build_info.py:59-73).
The earlier test helper was retired; no present test execution is inferred from this serializer contract.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### 260731-EFA-L1 Current Delta — `dashboardBuild` Is Now Routinely Absent

`_dashboard_build_fingerprint()` reads `package_data/dashboard.fingerprint`, and that sidecar is a
**generated artifact written next to the generated bundle** by `scripts/sync-dashboard.py` during
the release build. Neither is in version control (master decision OQ6, 2026-07-31). The two are
therefore absent together and present together:

- An **installation** (wheel or sdist) carries a cockpit and stamps which sources produced it. The
  release job asserts both files are in the distributions, so a published artifact always has it.
- A **source checkout** that never ran a frontend build carries neither, and `dashboardBuild` is
  simply omitted from the wire.

`None` therefore does **not** mean "legacy bundle" any more — it means no bundle was built here.
Omission follows the same honest-unknown rule as `commit` and `dirty`: never report a build
identity for a bundle that is not being served. Callers must treat `dashboardBuild` as optional;
`test_serving.py::BuildInfoTests` asserts present-or-omitted rather than indexing it.

The value itself is meaningful only because `sync-dashboard.py` reads it back out of the bundle's
own compiled `__AR_DASHBOARD_BUILD__` literal instead of stamping it over the tree, which is what
makes the cockpit's `CLIENT_DASHBOARD_BUILD` comparison a real staleness signal.

### FEUI-L9R Reviewed Candidate Delta

`ServingBuild` carries optional `dashboard_build`, serialized as `dashboardBuild`. Resolution
reads the packaged `dashboard.fingerprint` once at serving boot through `importlib.resources`.
Missing, unreadable, undecodable, or empty fingerprint data yields `None` and omission from the wire
rather than a fabricated identity; version, commit, and boot-time behavior is unchanged.

`ServingBuild(version, commit, booted_at, ...)` is a frozen dataclass; `payload()` returns the
camelCase wire form — since **260731-EFA-L4** the declared `ServingBuildPayload` model rather
than a hand-built dict, with unavailable facts dropped by the caller's `exclude_none=True`. The
stamp never fakes a hash or digest it could not resolve.

`resolve_serving_build(*, anchor=None)` composes the stamp: `version` from
`agents_remember.mcp.SERVER_VERSION` (the same identity the daemon's restart-on-version-mismatch
uses), `commit` via `_git_short_head` (`git rev-parse --short HEAD` anchored at the installed
package directory — git walks up to the enclosing checkout), `booted_at` from
`observer.events.now_iso()`. `_git_short_head` is best-effort by construction: fixed argv, a 2 s
bound, every exception suppressed to `None`. From an installed wheel with no Git metadata the
commit is omitted, while readable package source still yields content digest, interpreter, and
package-root identity; failure remains omission, never a crash.

### 260731-EFA-L3 — Both Probes Run On The One Git Runner

This module no longer spawns git itself. cit:([`_git_short_head`], mcp/src/agents_remember/serving/build_info.py:104-118) and `_git_worktree_dirty`
cit:(["def _git_worktree_dirty("], mcp/src/agents_remember/serving/build_info.py:121-121) each call `run_git` from `agents_remember.kernel.git_command` — the package's single
runner — with the module's own bound:

```python
_PROBE_TIMEOUT_SECONDS = 2
...
result = run_git(
    anchor, ["rev-parse", "--short", "HEAD"], GitRunnerOptions(timeout=_PROBE_TIMEOUT_SECONDS)
)
```

Two things change for the stamp, both in its favour:

- **The stamp now describes the checkout the server was started from.** The removed local
  `subprocess.run` passed no `env=`, so an exported `GIT_DIR` (worktree tooling, hooks, a wrapping
  git invocation) selected the repository and the probe would stamp *that* repository's HEAD and
  dirtiness onto this process. `run_git` strips the whole `GIT_DIR` family before every call.
- **`safe.directory` is no longer a failure mode.** `run_git` always passes
  `-c safe.directory=<repo_root>`, so a checkout owned by another user resolves instead of failing
  the probe into an honest-but-avoidable `None`.

`_PROBE_TIMEOUT_SECONDS` is kept deliberately tighter than the runner's general
`GIT_LOCAL_TIMEOUT_SECONDS` (300): this probe rides app creation, so a git that does not answer in
two seconds must read as "unstampable" like any other failure rather than delay boot. Everything
else is unchanged — fixed argv, stdin `DEVNULL` (the runner's default, so the probe can never touch
the MCP stdio protocol pipes), and every exception still suppressed to the honest `None`/`None`.

## Invariants And Boundaries

- **Boot-time only** — `process_serving_build()` caches one `resolve_serving_build()` result for
  both app and MCP composition; no per-request or per-tick probe rides the stamp.
- **Never faked** — `commit` is `None` (and omitted from the payload) whenever the resolve
  fails. `sourceDigest` is likewise omitted if package source cannot be read; a version string is
  never promoted to exact-candidate evidence.
- The stamp is **app-layer, not reducer truth**: it rides `/api/state` and the SSE `snapshot`
  (`serving/app.py`), never `WorkspaceProjection` or the persisted `latest-state.json`. Since
  **260731-EFA-L4** it is no longer *injected* into an undeclared dict either — the
  `servingBuild` key is declared on `served_state.ServedWorkspaceProjection`, the serving-layer
  subclass that exists precisely so this app-layer fact never becomes a projection field.

### Logic

Resolution combines package version, path-stable Python-source digest, exact interpreter and
package root, best-effort checkout commit, boot time, and the optional packaged dashboard
fingerprint into one immutable process stamp. The digest hashes sorted relative `.py` paths and
bytes while excluding `__pycache__`, so relocating identical source does not change identity and
changing source does.

### Conventions

Internal names are snake_case dataclass fields; `payload()` is the sole camelCase wire serializer.

### Invariants And Boundaries

Unavailable source, commit, or fingerprint evidence is omitted, never guessed, and the dashboard
fingerprint is read from package resources rather than recomputed at request time.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Evidence

### Docs References

No relevant documentation was found after checking the configured sources; packaged-build behavior
is proven by repository source and tests.

No relevant external or domain documentation was found for this repository-local build stamp.

### Repo-Internal References

- The two merge points: the SSE snapshot and the `/api/state` body, both now via `served_state_tail` onto a copy of the memoized projection dump. [1]
- The declaration of the `servingBuild` key, and the tail builder that applies this module's honest-unknown rule with `exclude_none=True`. [2]
- `SERVER_VERSION` supplies the wheel version in the daemon restart identity through the kernel resolver, which uses installed package metadata with a source-checkout literal fallback (kernel-owned since L9). [3]
- The cockpit compares and renders the serving/client identity. [4]
- The fingerprint sidecar this module reads is generated at release time beside the generated bundle, and is written only after a build that carries the same value. [5]
- The release job fails if either the bundle or this sidecar is missing from the wheel or sdist. [6]
- The serving payload carries optional dashboard build identity; omission does not fabricate a built or clean state. [7]
- The canonical selector list identifies inherited Git variables to remove. [8]
- The Git environment removes canonical repository selectors before execution. [9]
- The shared Git runner applies caller-selected bounds and isolated repository environment; both probes here pass their 2s bound as `GitRunnerOptions(timeout=...)`. [10]


### Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local build stamp.

The reviewed behavior is wholly repository-local.

## 260718-CHATS-L5I Current Delta

Serving build identity now distinguishes a proven dirty checkout from an unprovable one. Only a successful `git status --porcelain` with output emits `dirty`; probe failure omits the claim instead of fabricating a clean build state.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
