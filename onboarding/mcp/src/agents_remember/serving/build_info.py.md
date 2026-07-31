# mcp/src/agents_remember/serving/build_info.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/src/agents_remember/serving/build_info.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-07-31T04:28+02:00                          |
| lastVerifiedCommitHash | `c1dc5056ffa45cc7fe1af66a6d5c38497fbfa5f6`      |
| lastVerifiedCommitDate | 2026-07-31T04:58:22+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[serving overview](overview.md)

## Purpose

The serving **build stamp** (260703-L15): resolves ONCE at app creation which code is answering —
package version, best-effort commit short-hash, process boot time — so the cockpit can render it
and a stale serving process (the July-4 ghost-process lesson) is visible at a glance instead of
silently serving an old build.

## Code Commentary

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

`ServingBuild(version, commit, booted_at)` is a frozen dataclass; `payload()` returns the
camelCase wire form (`{"version", "bootedAt", "commit"?}`) with a `None` commit OMITTED — the
stamp never fakes a hash it could not resolve.

`resolve_serving_build(*, anchor=None)` composes the stamp: `version` from
`agents_remember.mcp.SERVER_VERSION` (the same identity the daemon's restart-on-version-mismatch
uses), `commit` via `_git_short_head` (a `git rev-parse --short HEAD` subprocess anchored at the
installed package directory — git walks up to the enclosing checkout), `booted_at` from
`observer.events.now_iso()`. `_git_short_head` is best-effort by construction: fixed argv, 2 s
timeout, every exception suppressed to `None` — from an installed wheel (no git metadata) the
stamp serves version-only, never a crash.

## Invariants And Boundaries

- **Boot-time only** — `create_app` calls `resolve_serving_build()` once; no per-request work
  and no per-tick work rides the stamp.
- **Never faked** — `commit` is `None` (and omitted from the payload) whenever the resolve
  fails; the payload's `version` alone then carries the identity.
- The stamp is **app-layer, not reducer truth**: it is injected onto `/api/state` and the SSE
  `snapshot` (`serving/app.py`), never onto `WorkspaceProjection` or the persisted
  `latest-state.json`.

### Logic

Resolution combines package version, best-effort checkout commit, boot time, and the optional
packaged dashboard fingerprint into one immutable boot stamp.

### Conventions

Internal names are snake_case dataclass fields; `payload()` is the sole camelCase wire serializer.

### Invariants And Boundaries

Unavailable commit or fingerprint evidence is omitted, never guessed, and the fingerprint is read
from package resources rather than recomputed at request time.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

No relevant documentation was found after checking the configured sources; packaged-build behavior
is proven by repository source and tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local build stamp. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The two injection points (`/api/state` body, SSE snapshot `servingBuild`). | L195-L202 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| `SERVER_VERSION` supplies the wheel version in the daemon restart identity. | L1-L20 | [mcp/__init__.py](agents-remember/mcp/src/agents_remember/mcp/__init__.py) |
| The cockpit compares and renders the serving/client identity. | L619-L657 | [Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |
| The fingerprint sidecar this module reads is generated at release time beside the generated bundle, and is written only after a build that carries the same value. | L138-L159 | [sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |
| The release job fails if either the bundle or this sidecar is missing from the wheel or sdist. | job `build`, step "Verify the distributions ship the dashboard bundle" | [publish-mcp-to-pypi.yml](agents-remember/.github/workflows/publish-mcp-to-pypi.yml) |
| The payload test asserts `dashboardBuild` present-or-omitted rather than indexing it unconditionally. | L923-L929 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local build stamp.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | Import and task-boundary review | — |

## 260718-CHATS-L5I Current Delta

Serving build identity now distinguishes a proven dirty checkout from an unprovable one. Only a successful `git status --porcelain` with output emits `dirty`; probe failure omits the claim instead of fabricating a clean build state.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History

- 2026-07-31T04:28+02:00 — 260731-EFA-L1: the dashboard bundle and its `dashboard.fingerprint`
  sidecar left version control and are now generated by the release job, so `dashboardBuild` is
  routinely absent in a source checkout and routinely present in an installation. Corrected the
  docstring-derived reading that `None` means "legacy bundle". No behavioral change to this
  module beyond its docstring. Verification metadata pinned to the pre-leaf source authority until
  closeout stamps the code commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the packaged dashboard fingerprint and honest
  omission fallback; verification metadata remains pinned pending candidate closeout.

- 2026-07-07T05:00+02:00 — Created for 260703-L15 S3 (stale-server visibility): boot-time
  `ServingBuild` stamp + best-effort `_git_short_head` + `resolve_serving_build`.
  Verification metadata pinned until closeout stamps the L15 commit.
