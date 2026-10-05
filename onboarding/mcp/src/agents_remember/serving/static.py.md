# mcp/src/agents_remember/serving/static.py

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

Mounts the shipped dashboard bundle or the existing honest missing-bundle notice.

## Code Commentary

### Logic

`_bundle_root()` is the single place the shipped-bundle path is spelled:
`resources.files("agents_remember").joinpath("package_data", "dashboard")` — the same
`importlib.resources` idiom as `install/assets.py`, so it resolves from an installed wheel and from
the `mcp/src` source tree alike. `_bundle_location()` renders that path for humans whether or not
anything is there. `dashboard_static_dir()` returns the `Path` only when it is a real filesystem
directory, and `None` otherwise — `importlib.resources` will happily hand back a path that does not
exist, so this resolver is what turns that into an answer a caller can act on.

`mount_static(app)` wraps either static branch with `UnknownApiPathsAreNotFound` before mounting at
`/`. An exact `/api` path or descendant with no non-Mount route match returns 404 for every method
before either static surface. Paths outside that API rule take one of the two branches:

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
exactly the non-API static path set that now explains itself — a deep-linked cockpit route gets the explanation too,
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

### Role Runtime and Scope

UnknownApiPathsAreNotFound precedes both static surfaces: exact /api or descendants matching no non-Mount route return 404 independently of method. Known routes with wrong methods and non-API/static paths retain their prior behavior. No former native host endpoint receives a static alias.

## Evidence

### Docs References

No relevant documentation was found after checking the configured sources (`system/sources.md` has
no entries); static-serving behavior is proven by repository source and tests.

No relevant external or domain documentation was found for this repository-local static mount.

### Repo-Internal References

- `dashboard_static_dir` resolves the packaged bundle to `Path` or `None`; `mount_static` mounts the bundle or the 503 surface. [1]
- After the unknown-API guard, the absent-bundle static surface answers 503 on GET/HEAD and 405 on other methods, mirroring `StaticFiles`. [2]
- The release build step places the tree this module resolves; it refuses to place a stale one. [3]
- The serving app registers API routes before the static mount. [4]




### Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local static mount.

The reviewed behavior is wholly repository-local.

### Runtime Source References

- Frozen implementation of UnknownApiPathsAreNotFound supporting the stated file behavior. [5]
- Frozen implementation of mount_static supporting the stated file behavior. [6]
- Checks unknown API roots/descendants return 404 for GET/HEAD/POST/PUT/DELETE with and without bundle; known route wrong method stays 405. [7]
- Composed app former four host paths have no route and answer Not Found for GET/POST/PUT/DELETE. [8]
