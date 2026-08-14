# mcp/tests/test_static.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_static.py`                 |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T04:28+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This module pins the static surface in **both** of its legitimate states: a built cockpit bundle,
and an honest absence.

It exists because the bundle left version control (master decision OQ6, 2026-07-31, leaf
260731-EFA-L1). "No bundle" became a normal state for a source checkout rather than a broken
install, and the assertions that used to prove serving worked read the committed bundle straight
out of the repository — which now gives different verdicts before and after a frontend build. Every
test here supplies its own stand-in tree and **never reads the repository's own bundle**, so the
suite is deterministic in a fresh clone, in CI, and after `npm run build` alike.

## Code Commentary

### Logic

`_bundle(root)` is the fixture: a minimal stand-in for what `dashboard/dist` puts on disk — an
`index.html` with the SPA mount point plus one content-hashed asset.

`DashboardStaticDirTests` patches `agents_remember.serving.static.resources.files` to a temp root
and covers the resolver's two answers. The absent case is the load-bearing one:
`importlib.resources` hands back a path that does not exist without complaint, so the test asserts
`dashboard_static_dir()` converts that into `None` rather than raising or returning a phantom path.

`MountedBundleTests._app(static_dir)` builds a FastAPI app with a `GET /api/state` route registered
**before** `mount_static`, then patches `dashboard_static_dir` to the supplied value. Passing a
directory exercises the served path; passing `None` exercises the absent path. What each test pins:

- **Served bundle** — entry HTML returns 200 with `Cache-Control: no-cache`, while the hashed asset
  keeps `StaticFiles`' own caching (explicitly *not* `no-cache`), so the revalidation rule is
  proven to apply to HTML only.
- **Missing bundle** — 503 (unavailable, not "not found"), `text/plain`, `Cache-Control: no-store`,
  and a body containing `BUILD_COMMAND`; the module constant is itself asserted to contain
  `npm --prefix dashboard run build`, so the remedy cannot silently become something else.
- **Named location** — patching `_bundle_location` proves the body reports where the bundle was
  expected, why it is missing ("not committed to the repository"), and what still works (`/api`).
- **No fabricated cockpit** — the 503 body contains neither the SPA mount point nor any HTML, so a
  placeholder cockpit cannot be reintroduced without failing here.
- **API untouched** — `GET /api/state` still returns 200 behind the greedy mount.
- **Method parity (regression)** — for `post`/`put`/`delete`/`patch` on `/api/state`, the
  missing-bundle app and the built-bundle app must return the **same** status, and that status must
  be 405. This is the regression that caught the mount at `/` outranking an API route which matched
  the path but not the method: answering 503 there contradicted the body's own "the API is
  unaffected" and made API method semantics depend on whether a build happened to be present.
- **Greedy coverage** — a deep cockpit route (`/sessions/L1/inspector`) also answers 503, so the
  set of paths that would have been served is exactly the set that now explains itself.

### Conventions

Determinism over realism: the suite patches the two seams (`resources.files` and
`dashboard_static_dir`) instead of arranging real package data. `test_serving.py` owns the
`create_app`-level version of the same two states; this module owns the deterministic unit-level
proof, which is why `test_serving.py::StaticTests` may skip when no build is present and this
module never does.

### Invariants And Boundaries

- No test may read the repository's real `package_data/dashboard`; a build must not change any
  verdict here.
- The absent state is asserted as `None` from the resolver and `503` from the mount — never as an
  exception, a 404, or a fabricated page.
- The absent-bundle mount's non-GET/HEAD behavior is asserted **by comparison** with the real
  `StaticFiles` mount, not against a hard-coded expectation, so the two can never diverge silently.
- `BUILD_COMMAND` is asserted as content of the response *and* as content of itself, so the remedy
  named to operators stays a real command.

### Todos

No task-independent follow-up is recorded for this module.

## Docs References

The resolved Domain Documentation registry (`system/sources.md`) has no entries. This
repository-local serving contract is documented from source and this executable regression.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking the configured sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The resolver's `None`-vs-directory contract and the two mount branches under test. | `dashboard_static_dir`; `mount_static` | mcp/src/agents_remember/serving/static.py:104-109; mcp/src/agents_remember/serving/static.py:112-129 |
| The 503 body, `no-store` header, and GET/HEAD-only method contract under test. | `MissingDashboardBundle`; `BUILD_COMMAND` | mcp/src/agents_remember/serving/static.py:35-38; mcp/src/agents_remember/serving/static.py:53-91 |
| The app-level counterpart covering both states through `create_app`. | `test_root_serves_dashboard_bundle`; `test_root_diagnoses_a_missing_bundle_instead_of_a_bare_404` | mcp/tests/test_serving.py:546-563; mcp/tests/test_serving.py:565-578 |
| The release build step that produces the bundle these tests stand in for. | `sync`; `replace_tree` | scripts/sync-dashboard.py:120-135; scripts/sync-dashboard.py:138-159 |

## Cross-Repo References

No sibling repository evidence is needed for this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 4 citation rows to the static resolver, missing-bundle surface, app tests, and release sync; scoped citation fixing regenerated the source ranges.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: made the `test_serving.py` citation the previous
  entry flagged as approximate exact again. The app-level counterpart is `AppTests` L526-L558:
  `test_root_serves_dashboard_bundle` (a stand-in bundle patched over `dashboard_static_dir`, 200 +
  `cache-control: no-cache`) and `test_root_diagnoses_a_missing_bundle_instead_of_a_bare_404`
  (resolver patched to `None`, 503 + remedy text + `no-store`, with `/api/state` still 200) — both
  built through `create_app`, which is what the claim asserts. Read back verbatim. Note for
  accuracy: the skip described in Conventions belongs to `StaticTests` at L1549-L1559, a different
  class that only exercises `dashboard_static_dir()` directly; the two `create_app` cases above do
  not skip.

- 2026-07-31T16:35+02:00 — No content impact: the only change to `mcp/tests/test_static.py` since
  the L2 base commit is the whole-tree `ruff format` pass in `00e8379`, which re-wrapped 4
  line(s), touching only magic trailing commas and redundant grouping parentheses. Checked by
  parsing both revisions and comparing the abstract syntax trees (identical) and the comment
  tokens (identical), so no symbol, signature, default, decorator, control-flow branch, docstring,
  or assertion this card describes has moved, and every claim this card makes about its own source
  still holds. Noted while checking: the references table also cites line ranges inside
  `test_serving.py`; those ranges shifted because this task edited those files, so treat the cited
  numbers as approximate and the linked cards as authoritative.

- 2026-07-31T04:28+02:00 — Created for 260731-EFA-L1: deterministic coverage of the static surface
  after the cockpit bundle left version control — resolver `None` vs. directory, served-HTML
  revalidation without weakening hashed-asset caching, the 503 diagnostic (location, reason,
  remedy, `no-store`), no fabricated cockpit, an unaffected API, greedy deep-route coverage, and
  the method-parity regression against the real `StaticFiles` mount. Verification metadata pinned
  to the pre-leaf source authority until closeout stamps the code commit.
