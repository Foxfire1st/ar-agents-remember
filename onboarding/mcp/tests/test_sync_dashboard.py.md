# mcp/tests/test_sync_dashboard.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_dashboard.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T23:30+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Pins that **`scripts/sync-dashboard.py --check` reports drift and writes nothing.**

The write path is a *release build step* and cannot be a pre-commit gate: it copies, renames and
rewrites the fingerprint sidecar. A gate needs the one question the write path cannot answer — whether
what is placed **still** matches the source — and it has to be answerable without changing the tree it
is measuring, or running the check is what makes the tree dirty.

Measured defect (S6a of `260915-CAPS-L21`): the script had no read-only mode at all. Its only two write
sites (`shutil.rmtree` of the staged and the retired copies) are unconditional on the write path, so
there was no way to ask the question.

The three cases below are the three answers that must stay distinguishable: a current tree passes, a
drifted tree fails, and a tree that **cannot be verified at all fails as drift rather than passing
green** — the conflation the deleted check mode was removed for.

## Code Commentary

### Logic

`DashboardCheckTests` (44) loads the script as a module and re-points its own path constants
(`SOURCE`, `TARGET`, `SOURCE_TREE`, `FINGERPRINT_FILE`) at a throwaway fixture root, so the real
`main()` runs against a tree the case owns. `write_bundle` (68) places `dist` and the target bundle
byte-identical with a chosen fingerprint; `run_check` (75) invokes `main()` with `--check` on
`sys.argv` and returns the exit code plus combined output; `snapshot` (86) records every file under the
fixture.

- **All three answers, and nothing written in any of them** —
  `test_the_check_reports_all_three_answers_and_writes_nothing_any_of_them` (91) walks one fixture
  through current → drifted → unbuildable. Clean exits 0 and names `matches dashboard/dist`; a
  tampered placed bundle exits 1 and names which file differs between `dashboard/dist` and the placed
  bundle; a missing `dashboard/dist` exits 1 and says so. **Every arm snapshots the whole fixture before
  and after**, so "writes nothing" is a measurement rather than an assertion — which is the property
  that makes the mode usable as a gate.
- **The third answer is the load-bearing one.** "Nothing has been built or placed" is *not* a pass, and
  the docstring states that this case refuses to let it become one again.
- **The write path is unchanged** — `test_the_write_path_still_places_the_bundle` (123) calls `sync()`
  and requires the placed bundle, the fingerprint file and the exit code to be exactly what the release
  path produced before. `--check` is additive: it adds a question, it does not become a second writer.

### Conventions

- The module is loaded by path (`load_sync_dashboard`) rather than imported, because the script is not
  a package module.
- Path constants are re-pointed on the loaded module (`self.module.SOURCE = ...`) instead of being
  monkeypatched per call, so the code under test is the shipped code path with a different root.
- Exit codes are asserted explicitly (0 clean, 1 drifted, 1 unverifiable), so the mode's contract is
  the process contract a build pipeline reads.

### Invariants And Boundaries

- **A check mode never writes.** The two `shutil.rmtree` sites stay on the write path; a check that
  mutates the tree it measures would dirty the working tree simply by being run.
- **Unverifiable is a failure, not a pass.** This is the boundary the module exists to hold.
- **`--check` does not replace the release write path.** The fingerprint sidecar is still written only
  by the build step, and the bundle is still placed only there.

## Docs References

No Domain Documentation source is configured for this repository; the script and the bundle it places
are repository-owned.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source applies; the subject is the repository's own build script. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The script whose check mode this module pins. | `main` | scripts/sync-dashboard.py:251-262 |
| The entry point the case invokes with `--check`. | `main` | scripts/sync-dashboard.py:251-262 |
| The write path that `--check` must leave unchanged. | `sync` | scripts/sync-dashboard.py:227-248 |
| The fingerprint the check recomputes from the source tree. | `source_fingerprint` | scripts/sync-dashboard.py:99-112 |
| The predicate that decides whether the placed bundle is still current. | `bundle_is_current` | scripts/sync-dashboard.py:115-125 |
| The path constants the fixture re-points, and the fingerprint sidecar the write path owns. | `SOURCE`; `TARGET`; `SOURCE_TREE`; `FINGERPRINT_FILE` | scripts/sync-dashboard.py:45-45; scripts/sync-dashboard.py:46-46; scripts/sync-dashboard.py:52-52; scripts/sync-dashboard.py:53-53 |

## Cross-Repo References

No external repository boundary is exercised; the fixture root is a throwaway directory the case owns.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T23:30+02:00 — 260915-CAPS-L21 curator: created this card for a source file **new in this
  leaf** (S6a's read-only `--check` mode). The anchor set is the script's own entry points and the
  module-level path constants the case re-points; `bundle_is_current` is quoted as an anchor because it
  is the predicate that answers the check's question. Anchors and ranges were read from the current
  worktree source; the file is untracked at this tip, so verification metadata is pinned to this leaf's
  code base commit `997305a9` and the governed closeout stamps the real code commit. No hash or
  fingerprint was invented here.
