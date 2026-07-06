# mcp/src/agents_remember/serving/build_info.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/src/agents_remember/serving/build_info.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-07-07T05:00+02:00                          |
| lastVerifiedCommitHash | `6ea2a422210b4b9797d2c7c8df5f9994813f9331`      |
| lastVerifiedCommitDate | 2026-07-06T21:07:46+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[serving overview](overview.md)

## Purpose

The serving **build stamp** (260703-L15): resolves ONCE at app creation which code is answering —
package version, best-effort commit short-hash, process boot time — so the cockpit can render it
and a stale serving process (the July-4 ghost-process lesson) is visible at a glance instead of
silently serving an old build.

## Code Commentary

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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The two injection points (`/api/state` body, SSE snapshot `servingBuild`). | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| `SERVER_VERSION` (wheel version, the daemon restart identity). | [mcp/__init__.py](agents-remember/mcp/src/agents_remember/mcp/__init__.py) |
| The muted cockpit render (`data-testid="serving-build"`). | [Cockpit.tsx](agents-remember/dashboard/src/cockpit/Cockpit.tsx) |

## Update History

- 2026-07-07T05:00+02:00 — Created for 260703-L15 S3 (stale-server visibility): boot-time
  `ServingBuild` stamp + best-effort `_git_short_head` + `resolve_serving_build`.
  Verification metadata pinned until closeout stamps the L15 commit.
