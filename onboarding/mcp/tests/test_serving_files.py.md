# test_serving_files.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_serving_files.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-06T21:45:53+00:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks the read-only files endpoint through its configured temporary scope: a valid read returns source content and traversal returns 400 bad-path. Catalog, sidecar pairing, binary/oversize and other historical cases are not retained in this file.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Read serves code content | `test_read_serves_code_content` | mcp/tests/test_serving_files.py:70-74 |
| Traversal is 400 bad path | `test_traversal_is_400_bad_path` | mcp/tests/test_serving_files.py:76-82 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T02:57+02:00 — W3-B03 curator: curated 4 table citations for the files API, app factory, runtime config, and serving-test fixture pattern; fixer-generated ranges verified.

- 2026-08-01T09:20+02:00 — 260731-EFA-L4 curator: the whole diff for this file is two type
  annotations — `_write_leaf_contract(..., cleanup: CleanupStatus = "pending")` and
  `CatalogAssemblyTests._enclosure(..., *, cleanup: CleanupStatus = "pending")`, plus the
  `CleanupStatus` import that serves them. No test was added, removed or renamed, and no assertion
  changed. The Conventions section already described `_write_leaf_contract`'s signature, so it was
  the natural home for the one fact a reader would otherwise miss: these fixtures are now inside
  the contract vocabulary pyright checks, which is the leaf's own mechanism reaching the test tree
  (see `test_wire_vocabulary_exhaustiveness.py`, whose `unreadable_contract_writes` rule requires
  every value at a typed contract writer to be statically readable). Everything else on this card —
  the path guard and symlink escape, the oversize multibyte boundary, the null-byte 400, both
  pairing directions, the memory-less degrade, and the `ProjectionCadence(interval=100)` call
  pattern — was re-read against the source and still holds. Verification metadata pinned until
  closeout stamps the L4 commit.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: `create_app` moved its polling
  interval into a `ProjectionCadence` parameter object, so `RouteTests._client` now builds
  `create_app(config, cadence=ProjectionCadence(interval=100))`; the Conventions call pattern this
  card documented was stale and has been rewritten to match. Also recorded that the catalog helper
  `_write_leaf_contract` dropped its `task` argument for the module constant `_CATALOG_TASK`
  because no call site varied it. No test case was added, removed, or renamed, and the path-guard,
  symlink-escape, oversize-boundary, null-byte, and pairing assertions are untouched.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-07T18:40+02:00 — 260703-L18 (review fix batch, finding 5): added
  `test_read_file_oversize_multibyte_boundary_returns_text_not_binary` — an oversize text file with a
  multi-byte char straddling the 2-MiB cap reads back as `text` + non-empty content, pinning the
  codepoint-boundary cut shared with the notes API. Verification metadata pinned until closeout stamps
  the L18 commit.
- 2026-07-06T09:30+02:00 — L9 adversarial-review ride-along: null-byte path regression test added (L9R-1). Verification metadata pinned until closeout stamps the L9 commit.

- 2026-06-30T00:00:00+02:00 — operations-integration L5: documented that the reverse-pairing overview-without-code case
  now also asserts the node's markdown `body` (`"# repo overview\n"`), pinning that the File Viewer can
  render a route overview directly. Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-06-28T22:41+02:00 — Created for operations-integration L1: the `serving/files.py` test suite — pure `FileScope` tests (path guard incl. symlink escape, list/read/drift/binary/oversize, forward+reverse pairing) plus `TestClient` route tests (catalog, unknown-repo 404, traversal 400, not-found 404, read 200, memory-less degrade). Verification metadata pinned until closeout stamps the L1 code commit.
