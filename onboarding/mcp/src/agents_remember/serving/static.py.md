# mcp/src/agents_remember/serving/static.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/src/agents_remember/serving/static.py`  |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-31T04:28+02:00                       |
| lastVerifiedCommitHash | `c1dc5056ffa45cc7fe1af66a6d5c38497fbfa5f6`   |
| lastVerifiedCommitDate | 2026-07-31T04:58:22+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[serving overview](overview.md)

## Purpose

`static.py` resolves and mounts the built cockpit bundle at `/` — or says plainly that it is not
there.

The cockpit is a Vite build (`dashboard/dist`) placed into `package_data/dashboard` by the release
job and shipped inside the wheel and sdist. **It is not committed** (master decision OQ6,
2026-07-31, leaf 260731-EFA-L1). A source checkout that has never run a frontend build therefore
legitimately has no bundle, and this module is where that state becomes diagnosable instead of
mysterious.

## Code Commentary

### Logic

`_bundle_root()` is the single place the shipped-bundle path is spelled:
`resources.files("agents_remember").joinpath("package_data", "dashboard")` — the same
`importlib.resources` idiom as `install/assets.py`, so it resolves from an installed wheel and from
the `mcp/src` source tree alike. `_bundle_location()` renders that path for humans whether or not
anything is there. `dashboard_static_dir()` returns the `Path` only when it is a real filesystem
directory, and `None` otherwise — `importlib.resources` will happily hand back a path that does not
exist, so this resolver is what turns that into an answer a caller can act on.

`mount_static(app)` takes one of two branches, both mounted at `/` with equal greed:

- **Bundle present** — `DashboardStaticFiles(directory=..., html=True)`, a `StaticFiles` subclass
  that adds `Cache-Control: no-cache` to successful **HTML** responses only. The entry document
  revalidates its dashboard identity; content-hashed JS/CSS keep ordinary static caching.
- **Bundle absent** — `MissingDashboardBundle`, which answers `503` with a plain-text body naming
  the directory it expected and `BUILD_COMMAND`, the exact chain that produces it
  (`npm --prefix dashboard ci && npm --prefix dashboard run build && python3 scripts/sync-dashboard.py`).
  `Cache-Control: no-store` keeps the diagnostic from outliving the build that fixes it. A warning
  carrying the same two facts is logged at mount time.

`MissingDashboardBundle` raises `HTTPException(405)` for anything but `GET`/`HEAD`
(`SERVED_METHODS`). That is not politeness — it is the method contract `StaticFiles` itself
enforces, and it is load-bearing: the greedy mount at `/` outranks an API route that matched the
path but not the method, so without it a `POST` to a `GET`-only `/api` route would answer `503`,
contradicting the body's own "the API is unaffected" and making the API's method semantics depend
on whether a frontend build happened to be present.

### Conventions

Response-header policy lives at the one static-serving seam (the `StaticFiles` subclass) rather
than in a parallel root route. The missing-bundle surface is a plain ASGI app with the same mount
point and the same greed as the real one, so the set of paths that would have been served is
exactly the set that now explains itself — a deep-linked cockpit route gets the explanation too,
not a bare 404 from an unrouted path.

### Invariants And Boundaries

- Resolution goes through `importlib.resources`, never a hard-coded path.
- The static mount is registered **after** the `/api` routes, so the greedy `/` mount only catches
  paths the API did not.
- A missing bundle is non-fatal: the server starts, the API serves, and the static surface reports
  what is missing. It must never abort startup.
- **There is no placeholder and no fallback UI.** The slice-04 hand-authored placeholder is gone
  and must not return; a stand-in cockpit would misrepresent a broken install as a working one.
- The absent-bundle mount must answer exactly the status codes `StaticFiles` would for non-GET/HEAD
  methods, so `/api` method semantics do not vary with build presence.
- HTML revalidates (`no-cache`); hashed assets keep default caching; the 503 body is `no-store`.

### Todos

No task-independent technical debt is recorded for this module.

## Docs References

No relevant documentation was found after checking the configured sources (`system/sources.md` has
no entries); static-serving behavior is proven by repository source and tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local static mount. | Source discovery checked | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `dashboard_static_dir` resolves the packaged bundle to `Path` or `None`; `mount_static` mounts the bundle or the 503 surface. | L94-L129 | [static.py](agents-remember/mcp/src/agents_remember/serving/static.py) |
| The absent-bundle surface answers 503 on GET/HEAD and 405 on every other method, mirroring `StaticFiles`. | L53-L91 | [static.py](agents-remember/mcp/src/agents_remember/serving/static.py) |
| The release build step places the tree this module resolves; it refuses to place a stale one. | L138-L159 | [sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |
| The serving app registers API routes before the static mount. | L1-L80 | [app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| Both halves of the contract are pinned deterministically, without reading the repository's own bundle. | L29-L143 | [test_static.py](agents-remember/mcp/tests/test_static.py) |
| The end-to-end app tests cover the served bundle and the missing-bundle diagnosis through `create_app`. | L506-L538 | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local static mount.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | Import and task-boundary review | — |

## Update History

- 2026-07-31T04:28+02:00 — 260731-EFA-L1: the shipped bundle left version control (master decision
  OQ6), so "no bundle" became a normal state for a source checkout. Added `MissingDashboardBundle`
  (503 + expected location + `BUILD_COMMAND`, `no-store`, GET/HEAD-only with 405 elsewhere so the
  greedy mount cannot change `/api` method semantics), `BUILD_COMMAND`, `_bundle_root()`, and
  `_bundle_location()`; `mount_static` now always mounts something. Removed this card's obsolete
  claims that slice 04 ships a committed placeholder there and that a missing bundle simply leaves
  the mount absent. Verification metadata is pinned to the pre-leaf source authority until closeout
  stamps the code commit.

- 2026-07-18T12:43+02:00 — FEUI-L9R: documented HTML revalidation without weakening hashed-asset
  caching; verification metadata remains pinned pending candidate closeout.

- 2026-07-10T15:07+02:00 — No source impact: 260707-HFX2-L17 recorded the unchanged serving
  boundary for the synchronized pair-role dashboard; generated asset filenames remain opaque.

- 2026-07-10T13:41+02:00 — No source impact: 260707-HFX2-L16 recorded the verified final combined
  package boundary—landed L15 Python and regenerated L16 dashboard bytes resolve from one worktree
  `agents_remember` package root, with dist/package byte identity and served-marker proof. Verification
  metadata remains pinned because `static.py` did not change.

- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: `dashboard_static_dir` +
  `mount_static` over `package_data/dashboard/`. Verification metadata pinned until closeout
  stamps the 4a code commit.
