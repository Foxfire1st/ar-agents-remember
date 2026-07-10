# mcp/src/agents_remember/serving/static.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/serving/static.py`  |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-10T13:41+02:00                       |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`   |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[serving overview](overview.md)

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

For the final L15+L16 package candidate, a worktree-local `PYTHONPATH=mcp/src` probe resolved
`agents_remember`, landed L15's `serving/harness_logs.py`, and `dashboard_static_dir()` under the
same package root. The returned directory was byte-identical to `dashboard/dist/`, and its entry
asset contained the L16 rail and R7 reader markers. This is the serving boundary that turns the
generated dashboard replacement into release evidence; the generated bundle itself is excluded from
file-level onboarding by path policy.

## Invariants And Boundaries

- Resolution goes through `importlib.resources`, not a hard-coded path, so it works from an
  installed wheel and the source tree alike.
- The static mount is registered last; API routes take precedence.
- A missing bundle degrades gracefully (no mount) rather than failing startup.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `dashboard_static_dir` resolves the package-data dashboard and `mount_static` installs it after API routes. | L18-L35 | [static.py](agents-remember/mcp/src/agents_remember/serving/static.py) |
| The sync bridge copies `dashboard/dist` into the directory this module resolves and records its source fingerprint. | L30-L52; L151-L179 | [sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |
| The serving app owns API registration before the static mount. | L1-L80 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |

## Update History

- 2026-07-10T13:41+02:00 — No source impact: 260707-HFX2-L16 recorded the verified final combined
  package boundary—landed L15 Python and regenerated L16 dashboard bytes resolve from one worktree
  `agents_remember` package root, with dist/package byte identity and served-marker proof. Verification
  metadata remains pinned because `static.py` did not change.

- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: `dashboard_static_dir` +
  `mount_static` over `package_data/dashboard/`. Verification metadata pinned until closeout
  stamps the 4a code commit.
