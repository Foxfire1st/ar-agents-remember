# scripts/sync-dashboard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `scripts/sync-dashboard.py`                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-31T04:28+02:00                     |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-dashboard.py` places a freshly built cockpit bundle (`dashboard/dist/`) into
`mcp/src/agents_remember/package_data/dashboard/` so the wheel and sdist ship the cockpit with
no Node build at install time.

**It is a release build step, not a drift check.** The destination is a generated artifact and is
**not under version control** (master decision OQ6, 2026-07-31, leaf 260731-EFA-L1). The release
job runs `npm --prefix dashboard run build` and then this script; `python -m build` then reads
what this script placed. Nothing in the repository can drift from a bundle the repository does not
contain, so the `--check` mode is gone along with its subject.

That removal is the root fix for a chain of downstream defects, and the reason to keep it removed:
a 28 MB generated tree in git produced the fingerprint sidecar's fail-open, the stale-stamping
`sync()`, a pre-commit hook that could not pass on a clean tree, and 45 commits made with
`--no-verify`.

## Code Commentary

### Logic

`SOURCE` is the repo-root `dashboard/dist`; `TARGET` is `package_data/dashboard`; `SOURCE_TREE` is
`dashboard/src`; `FINGERPRINT_FILE` is `dashboard.fingerprint`, a **sibling** of `TARGET` (never
inside it, so the served tree stays a byte-pure copy of `dist`).

`source_inputs()` digests every bundled file under `SOURCE_TREE` — skipping `.test.` / `.spec.` /
`.stories.` modules via `_is_bundled_source`, which Vite never bundles — plus the production config
files in `BUILD_INPUT_FILES` (`index.html`, `vite.config.ts`, the `tsconfig*.json`,
`panda.config.ts`, `postcss.config.cjs`, `package.json`, `package-lock.json`).
`source_fingerprint()` folds those into one SHA-256 over sorted `key\0digest\n` records.

`bundle_is_current(fingerprint)` is the whole freshness proof and the one thing to understand here.
`dashboard/vite.config.ts::dashboardSourceFingerprint` computes the **same** value by the same
algorithm and Vite's `define` substitutes it into the bundle as the `__AR_DASHBOARD_BUILD__` string
literal. So this function simply searches `dist` for that literal: a bundle built from this source
contains it verbatim and a bundle built from any other source cannot. Timestamps would prove
nothing where this runs — a fresh clone or a CI checkout writes every file at once, so "dist is
newer than its inputs" is satisfiable by an artifact that was never built from them.

`sync()` refuses (exit 1, message naming `REBUILD_HINT`) when `dist` is absent, and refuses again
when `dist` does not carry the current fingerprint. Only then does it `replace_tree()` (the
crash-safe copy-then-swap staging pattern shared with `sync-runtime.py`) and write the sidecar —
**after** the tree, never before, so a crash between the two cannot leave a sidecar advertising a
build identity for a bundle that is not there.

`main()` parses an empty argument set and returns `sync()`. Passing `--check` now exits non-zero
with `unrecognized arguments: --check`, which is deliberate: a silently tolerated flag would let a
hook or workflow keep believing a check runs.

### Conventions

The value written to `dashboard.fingerprint` is **read back out of the bundle's own JavaScript**,
never asserted over it. That is what makes it usable as an identity: `serving/build_info.py`
publishes it as `servingBuild.dashboardBuild`, and a live tab compares it against its own
`CLIENT_DASHBOARD_BUILD` to notice it is running stale JS. The previous `sync()` stamped the
current source fingerprint over whatever tree it had just copied, which corrupted exactly the
signal the sidecar exists to carry.

### Invariants And Boundaries

- `package_data/dashboard/` and `package_data/dashboard.fingerprint` are git-ignored
  (`.gitignore`). Do not commit either; do not add a check that compares the repository against
  them.
- There is **no fail-open**. Absent `dist`, a `dist` built from other source, and an absent
  `dashboard/src` all return 1. (An absent source tree yields an empty input set whose fingerprint
  no real bundle carries, so it refuses by construction rather than by a special case.)
- A refusal writes nothing: neither the target tree nor the sidecar is created or modified.
- The fingerprint covers build inputs only. A `.test.` / `.spec.` / `.stories.` edit must never
  demand a rebuild; a bundled-source or production-config edit must.
- `source_fingerprint()` here and `dashboardSourceFingerprint()` in `dashboard/vite.config.ts` are
  one algorithm in two languages. Changing either without the other makes every build refuse.
- The sidecar is written after the tree, and only after both refusals have been cleared.

### Todos

- The two implementations of the fingerprint algorithm (Python here, TypeScript in
  `vite.config.ts`) are kept in step by convention and by the refusal itself; there is no shared
  fixture proving they agree beyond a real build succeeding.

## Docs References

No relevant documentation was found after checking the configured sources (`system/sources.md` has
no entries); the placement contract is proven by repository source, the release workflow, and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation exists for this repository-local build step. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The script refuses an absent or non-current `dist`, places the tree, then writes the sidecar. | `sync`; `replace_tree` | scripts/sync-dashboard.py:120-135; scripts/sync-dashboard.py:138-159 |
| Vite compiles the same fingerprint into the bundle as `__AR_DASHBOARD_BUILD__`, which is the literal `bundle_is_current` searches for. | `dashboardSourceFingerprint`; `__AR_DASHBOARD_BUILD__` | dashboard/vite.config.ts:36-55; dashboard/vite.config.ts:65-65 |
| The release job builds the frontend, runs this script, packages, then asserts both distributions carry the bundle and the sidecar. | "Build dashboard bundle"; "Place dashboard bundle into MCP package data"; "Verify the distributions ship the dashboard bundle" | .github/workflows/publish-mcp-to-pypi.yml:57-120 |
| The suite proves placement, every refusal path, and that `--check` no longer exists. | `BuildPlacementTests`; `test_places_bundle_and_records_the_identity_the_bundle_itself_carries`; `test_refuses_when_dist_is_absent`; `test_refuses_a_dist_built_from_different_source`; `test_refuses_without_a_dashboard_source_tree`; `test_refuses_after_a_source_edit_that_was_never_rebuilt`; `test_refuses_after_a_production_config_edit`; `test_test_modules_are_not_build_inputs`; `test_check_mode_no_longer_exists` | mcp/tests/test_sync_dashboard.py:63-219; mcp/tests/test_sync_dashboard.py:253-268 |
| The serving resolver mounts what this script placed, or answers 503 when nothing was placed. | `dashboard_static_dir`; `mount_static`; `MissingDashboardBundle` | mcp/src/agents_remember/serving/static.py:53-91; mcp/src/agents_remember/serving/static.py:104-109; mcp/src/agents_remember/serving/static.py:112-129 |
| The sidecar this script writes is what the build stamp publishes as `dashboardBuild`. | `dashboardBuild` | mcp/src/agents_remember/serving/build_info.py:61-61 |
| Both generated paths are git-ignored with the reason recorded inline. | "mcp/src/agents_remember/package_data/dashboard/"; "mcp/src/agents_remember/package_data/dashboard.fingerprint" | .gitignore:19-24 |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local build step.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | — | — |

## Update History

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 6 citation rows across the sync implementation, Vite fingerprint, release workflow, regression suite, serving resolver, and ignore rules; scoped citation fixing regenerated the source ranges.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1 rewrote this card. The script is now a release build step,
  not a commit-gate drift check: `--check`, the `dist`↔`package_data` tree comparison, the
  fingerprint re-verification, and the "no `dist` yet" no-op are all removed with the committed
  bundle they described (master decision OQ6). `sync()` refuses an absent or non-current `dist`
  instead of stamping over it, and the sidecar value is read back out of the bundle's compiled
  `__AR_DASHBOARD_BUILD__` literal rather than asserted over the tree. The previous body's
  "the shipped bundle under `package_data/dashboard/` is committed" invariant and its two-gate
  `check()` description are obsolete and were removed rather than annotated. Verification metadata
  is pinned to the pre-leaf source authority until closeout stamps the code commit.
- 2026-07-10T15:07+02:00 — No source impact: 260707-HFX2-L17 recorded the dashboard
  role-selection/binding-role build as a source-fingerprint plus dist/package tree proof at this
  sync boundary. Generated hashed assets remain excluded from onboarding.

- 2026-07-10T13:41+02:00 — 260707-HFX2-L16 reviewed-no-source-change boundary update: recorded the
  final L15+L16 build/sync/package proof, corrected the `/api/task-document` marker attribution, and
  captured the fingerprint sequencing, Python invocation, and atomic hashed-asset staging notes.
  The script itself is unchanged at the L16 base; verification metadata stays pinned until closeout.

- 2026-06-28T16:17+02:00 — Task 35 source-freshness gate: `sync` now fingerprints the dashboard build
  inputs (the `src` tree minus `.test.`/`.spec.`/`.stories.` modules, plus the production config files)
  into a sibling `dashboard.fingerprint`, and `--check` re-verifies it through `fingerprint_check()` so a
  `dashboard/src` change committed without a rebuild is flagged at the commit gate — closing the blind
  spot where the `dist`↔`package_data` digest comparison passes two stale-but-equal copies. Added new
  helpers (`source_inputs`, `source_fingerprint`, `write_fingerprint`, `fingerprint_check`,
  `_is_bundled_source`, `_digest`) and made `check()` a two-gate function. Verification metadata pinned
  until closeout stamps the code commit.
- 2026-06-14T11:30+02:00 — Created for slice 04 commit 4a: the `dashboard/dist` →
  `package_data/dashboard` sync bridge (placeholder-aware no-op until the slice-05 build).
  Verification metadata pinned until closeout stamps the 4a code commit.
