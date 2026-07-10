# scripts/sync-dashboard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `scripts/sync-dashboard.py`                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T13:41+02:00                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1` |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`scripts/sync-dashboard.py` copies the built dashboard frontend bundle (`dashboard/dist/`)
into `mcp/src/agents_remember/package_data/dashboard/` so the wheel ships the cockpit with no
Node build at install time — mirroring `sync-runtime.py` / `sync-skills.py`.

It also closes the gap that distinguishes the dashboard from the skill/runtime gates: `dashboard/dist`
is a *generated* artifact, so comparing it against the shipped copy only proves "built bundle == shipped
bundle" — it cannot tell that either still reflects the current source. A `dashboard/src` edit committed
without a rebuild therefore used to slip the gate (both copies stay stale together, or `dist` is simply
absent). `sync` now also fingerprints the dashboard's real build inputs (the `src` tree minus tests,
plus the production config files) into a sibling `dashboard.fingerprint` sidecar, and `--check`
re-verifies that fingerprint — flagging a source change that was never rebuilt the same way a changed
skill is flagged. This is the pre-commit/pre-push `--check` behavior, so the commit gate catches a stale
shipped bundle, not just the push gate.

## Code Commentary

### Logic

`SOURCE` is the repo-root `dashboard/dist`; `TARGET` is the package-data dashboard dir.
`file_digests` SHA-256s every non-ignored file under a root. `replace_tree` is the crash-safe
copy-then-swap (stage to `<target>.ar-sync-new`, rename the live target aside, swap in, then
remove the old tree), matching `sync-runtime.py`.

`check()` now runs **two** gates and returns non-zero if either fails. The built-bundle gate is the
original `file_digests(SOURCE) == file_digests(TARGET)` comparison (skipped as a graceful no-op when
`dist` is absent). The source-freshness gate is `fingerprint_check()`: `SOURCE_TREE` is `dashboard/src`
and `FINGERPRINT_FILE` is the `dashboard.fingerprint` sibling *beside* `TARGET` (never inside it, so the
served tree stays a byte-pure copy of `dist`). `source_inputs()` digests every bundled `src` file
(skipping `.test.`/`.spec.`/`.stories.` modules via `_is_bundled_source`, which Vite never bundles) plus
the production config files in `BUILD_INPUT_FILES` (`index.html`, `vite.config.ts`, the `tsconfig*.json`,
`panda.config.ts`, `postcss.config.cjs`, `package.json`, `package-lock.json`); `source_fingerprint()`
folds those into one stable SHA-256 over sorted `path\0digest` pairs. `fingerprint_check()` compares the
recorded fingerprint to the current one and is skipped (returns 0) until a fingerprint exists (legacy
placeholder) or when no `src` tree is present (a packaged install). `sync()` replaces the target, calls
`write_fingerprint()` to record the current build inputs, then re-checks; `main` exposes `--check`.

### 260707-HFX2-L16 Final Combined Package Proof

The final L16 candidate was rebuilt after synchronizing onto landed L15 base `c8818285`. The shipped
`package_data/dashboard/` tree was byte-identical to `dashboard/dist/`; `--check` passed both its
source-fingerprint and tree-digest gates; the packaged entry asset carried the L16 sprint-rail and R7
reader markers; and worktree package resolution proved the landed L15 Python code plus the rebuilt
L16 bytes ship from one `agents_remember` package root. L15 changed no dashboard or packaged-dashboard
path, so no L15 JavaScript marker exists or should be invented. The `/api/task-document` source marker
belongs to `dashboard/src/data/taskDocuments.ts`, not `DetailPanel.tsx` (reviewer CD-N1 correction).

### Build present vs. absent `dist`

The slice-05 Vite build now exists and the shipped bundle is its output; the `--check` call is wired
into both `.githooks/pre-commit` and `.githooks/pre-push` on the dashboard branch line. When
`dashboard/dist/` is absent (a clean checkout that has not run `npm run build`), the *built-bundle* gate
still no-ops gracefully — it never wipes the committed bundle. The *source-freshness* gate, however, is
independent of `dist`: once a `dashboard.fingerprint` is recorded, `--check` flags a `src`/config change
even with `dist` absent, because the recorded fingerprint is compared against the live source tree, not
against the (possibly missing) build output. The historical placeholder
(`package_data/dashboard/index.html`, no recorded fingerprint) still passes untouched.

### Invariants And Boundaries

- Build output (`dashboard/dist/`) and `node_modules/` are git-ignored; the shipped bundle
  under `package_data/dashboard/` is committed.
- Absent `dist/` is a graceful no-op for the built-bundle gate, never a failure or a destructive wipe
  of the placeholder.
- The source-freshness fingerprint covers only build inputs: the `src` tree minus
  `.test.`/`.spec.`/`.stories.` modules, plus the production config files in `BUILD_INPUT_FILES`. A
  test/spec/story edit must never demand a rebuild; a bundled-source or production-config change must.
- `dashboard.fingerprint` lives *beside* the shipped bundle, never inside `package_data/dashboard/`, so
  the served tree stays a byte-pure copy of `dist` and the built-bundle digest comparison is unaffected.
- The source-freshness gate is skipped (returns 0) without a recorded fingerprint or without a
  `dashboard/src` tree, so legacy placeholders and packaged installs are never falsely failed.

### Todos

- Reviewer D2-N1: `sync()` records the source fingerprint after copying the already-built tree. A
  source edit between build and sync can therefore stamp current source beside stale build output.
  This candidate closes that evidence gap with source-to-served-byte markers; a future build-time
  fingerprint or embedded build manifest would close it mechanically.
- Reviewer CD-N2/D2-N3: generated hashed assets are an atomic replacement set. Closeout must stage
  every new asset together with every deleted asset, `index.html`, and the fingerprint; omitting the
  untracked additions leaves a broken package tree.
- Reviewer D2-N2: run `python3 -m unittest mcp.tests.test_sync_dashboard` from the repo root with
  system Python. The project venv's installed `mcp` package shadows the local `mcp.tests` namespace.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The script digests build inputs, records the sibling fingerprint during sync, and checks fingerprint plus dist/package tree equality. | L30-L52; L79-L130; L151-L179 | [sync-dashboard.py](agents-remember/scripts/sync-dashboard.py) |
| The isolated unit suite covers tree replacement, fingerprint staleness, config inputs, test exclusion, and sync/check round trips. | L24-L210 | [test_sync_dashboard.py](agents-remember/mcp/tests/test_sync_dashboard.py) |
| The static resolver serves the committed package-data directory at the root after API routes. | L18-L35 | [serving/static.py](agents-remember/mcp/src/agents_remember/serving/static.py) |
| The API literal used in the L16 source-to-package marker proof is owned by the dashboard data adapter. | L10-L17 | [taskDocuments.ts](agents-remember/dashboard/src/data/taskDocuments.ts) |

## Update History

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
