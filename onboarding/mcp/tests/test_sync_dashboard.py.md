# test_sync_dashboard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_sync_dashboard.py`         |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T04:28+02:00                     |
| lastVerifiedCommitHash | `a89a6fc88d9330eb2749c87b3dcc3f6c4e46c4bd` |
| lastVerifiedCommitDate | 2026-08-14T12:44:51+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

This module pins the contract of `scripts/sync-dashboard.py` as a **release build step**, which is
what it became when the bundle left version control (master decision OQ6, 2026-07-31, leaf
260731-EFA-L1).

Its one non-negotiable property, exercised from every angle: the script cannot place an artifact
that was not built from the dashboard source as it stands right now. The previous suite asserted
the *opposite* in three places — absent `dist` passes, absent fingerprint sidecar passes, absent
`dashboard/src` passes — and each of those tests was replaced by its inversion. Two of the
replacements carry docstrings naming the fail-open they encode, so the history cannot be re-adopted
by accident.

## Code Commentary

### Logic

`load_sync_dashboard()` loads the script through `importlib.util` because its filename contains a
hyphen. `seed_source(root)` builds a minimal dashboard checkout: a `src` tree plus one production
config file (`vite.config.ts`).

`emit_bundle(root, build_identity)` stands in for `vite build`: it writes a `dist` whose JavaScript
contains the identity **verbatim**. That is the faithful part — Vite's `define` substitutes
`__AR_DASHBOARD_BUILD__` with a string literal, and that literal is the entire handshake
`bundle_is_current()` relies on. Tests patch `SOURCE`, `SOURCE_TREE`, `TARGET`, and
`FINGERPRINT_FILE` onto temp paths, so nothing reads or writes the real tree.

`BuildPlacementTests`:

- **Places and records** — `sync()` returns 0, the tree lands, and the sidecar holds the 64-hex
  value that is also present inside the emitted JS. That last assertion is the point: the sidecar
  `serving/build_info.py` publishes is a value read *out of* the bundle, so a live tab's
  `CLIENT_DASHBOARD_BUILD` comparison is meaningful.
- **Refuses when `dist` is absent** — replaces `test_check_noops_without_a_build`. That old test
  encoded the defect: with no `dashboard/dist` the old `check()` printed "shipped placeholder
  retained" and exited 0, so on every fresh clone the gate certified an artifact nobody had built.
- **Refuses a `dist` built from other source** — and writes nothing: no sidecar may advertise a
  bundle that was never placed, and no stale tree may ship under a fresh stamp.
- **Refuses without a `dashboard/src` tree** — replaces `test_gate_skipped_without_a_source_tree`.
  `source_inputs()` still returns `{}` there, but the empty input set now yields a fingerprint no
  real bundle carries, so the refusal falls out of the algorithm rather than from a special case.
- **Refuses after an unrebuilt source edit** and **after a production-config edit** — place
  successfully, mutate an input, then require the next `sync()` to return 1.
- **Test modules are not build inputs** — editing `Foo.test.tsx` leaves placement succeeding;
  editing the `Foo.tsx` it covers makes it refuse.

`ReplaceTreeTests` covers the crash-safe copy-then-swap in isolation: the source lands, a stale
target file is dropped, and ignored names (`.DS_Store`) are omitted.

`PlacementSurfaceTests` pins the paths (`dashboard/dist` → `package_data/dashboard`, sidecar
**beside** the target, never inside it) and asserts `--check` no longer exists. That last one runs
through a real `subprocess` **on purpose**: the process boundary is where the old fail-open lived,
because hooks and CI invoked `--check` and read its exit status. A silently tolerated flag would
let a caller keep believing a check runs, so the flag must fail loudly.

### Conventions

Every test patches the module globals onto temporary paths; none reads the real repository tree,
and none requires a frontend build to have happened. Refusal tests assert not only the exit code
but that **nothing was written** — target absent, sidecar absent — since a partial write is the
failure mode that would matter in a release job.

### Invariants And Boundaries

- The suite must contain no test in which an absent or non-current `dist` yields success.
- `emit_bundle` must keep embedding the fingerprint verbatim; weakening it to a stub would make
  every placement test vacuous.
- The `--check` regression must stay at the process boundary, not at the function boundary.
- The script only ever writes `package_data/dashboard` and its sibling `dashboard.fingerprint`.
- Cache/junk names (`__pycache__`, `.DS_Store`) are ignored during placement.
- The fingerprint excludes `.test.` / `.spec.` / `.stories.` modules, so test edits never demand a
  rebuild.

### Todos

The `GeneratedDashboardWhitespacePolicyTests` class was removed with the committed bundle it
policed: root `.gitattributes` scoped a `blank-at-eol` exception to
`package_data/dashboard/assets/*.js`, a path that is no longer tracked, so the regression had no
subject. If that attribute rule is ever re-scoped to a tracked generated path, the regression
should return with it.

## Docs References

The resolved Domain Documentation registry (`system/sources.md`) has no entries. This
repository-local build-step contract is documented from source and this executable regression.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation found after checking the configured sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite loads the hyphenated script and reproduces Vite's compiled-fingerprint handshake in its fixtures. | `load_sync_dashboard`, `emit_bundle` | mcp/tests/test_sync_dashboard.py:26-33; mcp/tests/test_sync_dashboard.py:46-60 |
| Placement succeeds only for a current bundle; every refusal path writes nothing. | `BuildPlacementTests` | mcp/tests/test_sync_dashboard.py:63-219 |
| The path contract and the process-boundary proof that `--check` is gone. | `PlacementSurfaceTests` | mcp/tests/test_sync_dashboard.py:244-268 |
| The script under test: refuse-absent, refuse-stale, place, then record. | `sync` | scripts/sync-dashboard.py:138-159 |
| Vite compiles the fingerprint the fixtures embed. | `__AR_DASHBOARD_BUILD__` | dashboard/vite.config.ts:65-65 |
| The release job is the only caller, and it runs the frontend build immediately before. | "npm run build" | .github/workflows/publish-mcp-to-pypi.yml:61-61 |

## Cross-Repo References

No sibling repository evidence is needed for this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-02T16:44:57+02:00 — L6 W1-B02 curator: repaired 6 repository-internal references for the dashboard sync fixtures, placement surface, sync script, Vite fingerprint define, and release workflow; scoped citation verification follows.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 rewrote this card for the suite's inversion. The three
  fail-open tests (`test_check_noops_without_a_build`,
  `test_gate_skipped_until_a_fingerprint_is_recorded`, `test_gate_skipped_without_a_source_tree`)
  and the whole `SourceFingerprintTests` / `--check` round-trip framing were replaced by refusal
  tests plus a process-boundary proof that `--check` no longer exists;
  `GeneratedDashboardWhitespacePolicyTests` was removed with the committed bundle its
  `.gitattributes` exception policed. Removed this card's obsolete claims that `--check` runs two
  gates and that an absent `dist` is a graceful no-op. Verification metadata pinned to the pre-leaf
  source authority until closeout stamps the code commit.
- 2026-07-18T21:05+02:00 — FEUI-MX-FIX-5 added the real-Git generated-whitespace policy
  regression: the temporary repository copies the checked-out root attribute, permits a significant
  tab-only line in a direct shipped JavaScript template literal, and still rejects trailing spaces in
  authored `dashboard/src/main.tsx`. Recorded the Vite/raw-sync ownership boundary and corrected the
  card's governing link to the nearest `mcp/tests` overview. Verification metadata remains pinned to
  the last committed source authority until closeout stamps the candidate commit.
- 2026-06-28T16:17+02:00 — Task 35: added `SourceFingerprintTests` for the source-freshness gate (unbuilt source/config change fails `--check`, test/spec/story edits do not, gate skipped without a recorded fingerprint or a source tree, `sync` records and re-verifies a 64-hex fingerprint) and made the existing dist-focused tests hermetic by also patching `FINGERPRINT_FILE`/`SOURCE_TREE`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-14T15:52+02:00 — Created for slice 5a: onboarding for the `scripts/sync-dashboard.py` tests (digests, copy-then-swap replace, check/sync round-trip, no-op-without-build, path contract). Verification metadata pinned until closeout stamps the 5a code commit.
