# test_serving_files.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_serving_files.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:20+02:00                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[../overview.md](../overview.md)

## Purpose

`test_serving_files.py` is the test suite for the operations-integration L1 files
API (`serving/files.py`): the path-confinement security guard, directory listing
with sidecar annotation, file reading (text / oversize / binary / drift), the
forward + reverse onboarding pairing, the repo/enclosure catalog, and the four
`/api/files/*` routes through the real scope resolver.

## Code Commentary

### Logic

L9 review ride-along adds `test_null_byte_path_is_400_bad_path` to RouteTests: the files API answers `400 bad-path` for a null-byte path (same L9R-1 fix as the notes API it seeded).

Two layers, deliberately split so onboarding behavior is testable without standing
up the resolver:

- **Pure tests** build a `FileScope` directly over a temp code+onboarding tree
  (`_make_repo` creates one file with a sidecar and one without). `PathGuardTests`
  pins `_resolve_within`: an empty path is the root, a normal nested path resolves,
  and an absolute path, a `../` traversal, and a **symlink escape** each raise
  `AuthorityError` (the load-bearing security test). `ListAndReadTests` and
  `PairingTests` assert the `hasSidecar` split, the drift metadata, the
  oversize-truncation cap (plus **260703-L18 finding 5**:
  `test_read_file_oversize_multibyte_boundary_returns_text_not_binary` — an oversize text file
  whose multi-byte char straddles the cap reads back as `text` + non-empty content, never empty
  `binary`), the binary marker, the missing-sidecar-is-not-an-error
  result, and both pairing directions (sidecar→code, orphan, overview-without-code).
  The overview-without-code case also asserts the node carries its own markdown
  `body` (`"# repo overview\n"`) so the File Viewer can render a route overview
  directly rather than showing a "no code partner" placeholder (L5).
- **Route tests** (`RouteTests`) drive `/api/files/*` through a real
  `create_app(McpRuntimeConfig(...))` + `TestClient`, covering the catalog, the
  `404 unknown-repo` allow-list rejection, a `400 bad-path` traversal, a
  `404 not-found`, a successful read, and the **memory-less degrade path** (a repo
  with no AR memory still serves code with onboarding `"missing"`).
  `CatalogTests` covers `list_repos` (mainline per allow-listed repo) and that a
  malformed enclosure contract is skipped rather than aborting the catalog.

### Conventions

Mirrors `test_serving.py`: `sys.path.insert(0, str(MCP_SRC))` so imports resolve to
this checkout, `unittest.TestCase` with a `tempfile.TemporaryDirectory` per case,
and `with TestClient(create_app(config, cadence=ProjectionCadence(interval=100))) as client:` for
route tests (`create_app` takes its polling interval inside a `ProjectionCadence` parameter object).
The catalog fixture `_write_leaf_contract` varies only `repo` and `leaf`; the master task name is the
module constant `_CATALOG_TASK`, not an argument.
Since 260731-EFA-L4 its `cleanup` parameter — and the matching one on
`CatalogAssemblyTests._enclosure` — is typed `CleanupStatus` rather than `str`, so the fixtures are
inside the contract vocabulary pyright checks rather than beside it: an off-vocabulary cleanup value
in a fixture is now a type error, not a contract the writer would refuse at runtime.
Run with `PYTHONPATH=mcp/src python -m pytest mcp/tests/test_serving_files.py -q`.

### Invariants And Boundaries

- The pure tests own the onboarding-behavior assertions (they control
  `onboarding_root` directly); the route tests own scope resolution, the
  allow-list, and the traversal guard — kept decoupled so resolver internals do not
  make the onboarding assertions flaky.
- The symlink-escape case must stay: it is the regression guard proving
  confinement resolves real paths, not just literal `..` tokens.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The files API under test (`FileScope`, `list_repos`, `list_dir`, `read_file`, `resolve_onboarding`, `resolve_partner`, `_resolve_within`). | `list_repos`; `list_dir`; `read_file`; `resolve_onboarding`; `resolve_partner` | mcp/src/agents_remember/serving/files.py:92-107; mcp/src/agents_remember/serving/files.py:161-184; mcp/src/agents_remember/serving/files.py:190-213; mcp/src/agents_remember/serving/files.py:232-239; mcp/src/agents_remember/serving/files.py:264-290 |
| The app factory the route tests build. | `create_app` | mcp/src/agents_remember/serving/app.py:226-285 |
| `McpRuntimeConfig` / `RepositoryScope` constructed by the catalog + route tests. | `McpRuntimeConfig`; "class RepositoryScope:" | mcp/src/agents_remember/kernel/primitives/runtime_config.py:113-137; mcp/src/agents_remember/kernel/primitives/runtime_config.py:76-81 |
| The serving test suite whose `_config` / `TestClient` pattern this mirrors. | `_config` | mcp/tests/test_serving.py:95-101 |

## 260718-CHATS-L5I Current Delta

Serving-files regressions now assert that repository discovery is single-pass and TTL-cached while the returned repository/file grouping stays complete.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History
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
