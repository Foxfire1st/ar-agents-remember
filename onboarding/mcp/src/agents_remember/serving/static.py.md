# mcp/src/agents_remember/serving/static.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/serving/static.py`  |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-06-14T11:30+02:00                       |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`   |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                |

## Purpose

`static.py` resolves and mounts the shipped dashboard static bundle
(`package_data/dashboard/`). Slice 04 ships a hand-authored placeholder there; slice 05's
built cockpit replaces it.

## Code Commentary

`dashboard_static_dir()` resolves `package_data/dashboard` via
`importlib.resources.files("agents_remember").joinpath(...)` — the same idiom as
`install/assets.py` — returning the `Path` when it is a real filesystem directory (the wheel
and the `mcp/src` source tree both qualify) or `None` otherwise.

`mount_static(app)` mounts that directory at `/` with `StaticFiles(..., html=True)` when it
exists. It is called after the `/api` routes are registered, so the greedy `/` mount only
catches paths the API did not; a missing bundle is non-fatal (the API still serves).

## Invariants And Boundaries

- Resolution goes through `importlib.resources`, not a hard-coded path, so it works from an
  installed wheel and the source tree alike.
- The static mount is registered last; API routes take precedence.
- A missing bundle degrades gracefully (no mount) rather than failing startup.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The package-data resolution idiom mirrored here. | [install/assets.py](agents-remember/mcp/src/agents_remember/install/assets.py) |
| The app that calls `mount_static`. | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| The build → package_data sync bridge for the bundle. | [scripts/sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |

## Update History

- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: `dashboard_static_dir` +
  `mount_static` over `package_data/dashboard/`. Verification metadata pinned until closeout
  stamps the 4a code commit.
