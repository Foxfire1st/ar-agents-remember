# test_serving_files.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/tests/test_serving_files.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-28T22:41+02:00                     |
| lastVerifiedCommitHash | `ad30dd38c3dcfa13fb85f44b281488499e92519a` |
| lastVerifiedCommitDate | 2026-07-03T08:10:19+02:00|
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

Two layers, deliberately split so onboarding behavior is testable without standing
up the resolver:

- **Pure tests** build a `FileScope` directly over a temp code+onboarding tree
  (`_make_repo` creates one file with a sidecar and one without). `PathGuardTests`
  pins `_resolve_within`: an empty path is the root, a normal nested path resolves,
  and an absolute path, a `../` traversal, and a **symlink escape** each raise
  `AuthorityError` (the load-bearing security test). `ListAndReadTests` and
  `PairingTests` assert the `hasSidecar` split, the drift metadata, the
  oversize-truncation cap, the binary marker, the missing-sidecar-is-not-an-error
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
and `with TestClient(create_app(config, interval=100)) as client:` for route tests.
Run with `PYTHONPATH=mcp/src python -m pytest mcp/tests/test_serving_files.py -q`.

### Invariants And Boundaries

- The pure tests own the onboarding-behavior assertions (they control
  `onboarding_root` directly); the route tests own scope resolution, the
  allow-list, and the traversal guard — kept decoupled so resolver internals do not
  make the onboarding assertions flaky.
- The symlink-escape case must stay: it is the regression guard proving
  confinement resolves real paths, not just literal `..` tokens.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The files API under test (`FileScope`, `resolve_scope`, `list_repos`, `list_dir`, `read_file`, `resolve_onboarding`, `resolve_partner`, `_resolve_within`). | [serving/files.py](agents-remember/mcp/src/agents_remember/serving/files.py) |
| The app factory the route tests build. | [serving/app.py](agents-remember/mcp/src/agents_remember/serving/app.py) |
| `McpRuntimeConfig` / `RepositoryScope` constructed by the catalog + route tests. | [mcp/config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The serving test suite whose `_config` / `TestClient` pattern this mirrors. | [test_serving.py](agents-remember/mcp/tests/test_serving.py) |

## Update History

- 2026-06-30T00:00:00+02:00 — operations-integration L5: documented that the reverse-pairing overview-without-code case
  now also asserts the node's markdown `body` (`"# repo overview\n"`), pinning that the File Viewer can
  render a route overview directly. Verification metadata pinned until closeout stamps the L5 code commit.
- 2026-06-28T22:41+02:00 — Created for operations-integration L1: the `serving/files.py` test suite — pure `FileScope` tests (path guard incl. symlink escape, list/read/drift/binary/oversize, forward+reverse pairing) plus `TestClient` route tests (catalog, unknown-repo 404, traversal 400, not-found 404, read 200, memory-less degrade). Verification metadata pinned until closeout stamps the L1 code commit.
