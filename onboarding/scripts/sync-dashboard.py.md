# scripts/sync-dashboard.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `scripts/sync-dashboard.py`                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-28T16:17+02:00                     |
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

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The sync pattern this mirrors. | [scripts/sync-runtime.py](agents-remember/scripts/sync-runtime.py) |
| The skills gate whose canonical-source hashing the fingerprint mirrors. | [scripts/sync-skills.py](agents-remember/scripts/sync-skills.py) |
| The commit/push gate that runs `--check` (skills + runtime + dashboard). | [.githooks/pre-commit](agents-remember/.githooks/pre-commit) |
| The static mount that serves the synced bundle. | [serving/static.py](agents-remember/mcp/src/agents_remember/serving/static.py) |
| The frontend sub-project home + build/ship contract. | [dashboard/README.md](agents-remember/dashboard/README.md) |

## Update History

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
