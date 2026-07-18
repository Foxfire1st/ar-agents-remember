# mcp/src/agents_remember/serving/build_info.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/src/agents_remember/serving/build_info.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-07-18T12:43+02:00                          |
| lastVerifiedCommitHash | `82f2de40a666ea00754f364cfe764cea9294235f`      |
| lastVerifiedCommitDate | 2026-07-18T13:07:00+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[serving overview](overview.md)

## Purpose

The serving **build stamp** (260703-L15): resolves ONCE at app creation which code is answering —
package version, best-effort commit short-hash, process boot time — so the cockpit can render it
and a stale serving process (the July-4 ghost-process lesson) is visible at a glance instead of
silently serving an old build.

## Code Commentary

### FEUI-L9R Reviewed Candidate Delta

`ServingBuild` now carries optional `dashboard_build`, serialized as `dashboardBuild`. Resolution
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

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local build stamp.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | Import and task-boundary review | — |

## Update History

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the packaged dashboard fingerprint and honest
  omission fallback; verification metadata remains pinned pending candidate closeout.

- 2026-07-07T05:00+02:00 — Created for 260703-L15 S3 (stale-server visibility): boot-time
  `ServingBuild` stamp + best-effort `_git_short_head` + `resolve_serving_build`.
  Verification metadata pinned until closeout stamps the L15 commit.
