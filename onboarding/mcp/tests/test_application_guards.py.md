# mcp/tests/test_application_guards.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_application_guards.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `0506b57a1a80e0b377e9cc3303e1841d3bd4799a`                         |
| lastVerifiedCommitDate | 2026-09-01T12:17:08+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

`test_application_guards.py` is the first direct test coverage for the shared
MCP application entry point authority guards (F10). The resolve-and-confine checks used to be
copy-pasted across every application entry point and the rejection path had no dedicated
test; this suite pins both guards in one place so the security boundary is
proven once instead of per-entry-point.

## Code Commentary

### Logic

A `_config` helper builds a real `McpRuntimeConfig` rooted under a per-test
`TemporaryDirectory`, with a resolved `coord/` coordination root and a single
allowed `demo` repository scope.

`RequireRepoTests` covers `require_repo`: it returns the matching
`RepositoryScope` for an allowed repo id, and for an unknown id it raises
`AuthorityError` whose message matches "not allowed". That test also asserts
`issubclass(AuthorityError, ValueError)` so existing `ValueError` handlers keep
catching the rejection.

`RequireWithinCoordinationTests` covers `require_within_coordination`: a
relative input resolves against `coordination_root` and returns the joined path,
while both escape vectors are rejected with an `AuthorityError` matching "must
stay inside" — an absolute path pointing outside the root, and a relative
`../escape` traversal. The label argument (`contract_path`) is the value
threaded into the rejection message.

### Conventions

Standard-library `unittest` `TestCase` classes, one class per guard, with
`tempfile.TemporaryDirectory` context managers for filesystem isolation. All
roots are `.resolve()`-d in the fixture so confinement comparisons are made on
canonical paths. Rejection assertions use `assertRaisesRegex` against the stable
substring of each guard's message rather than the full string.

### Invariants And Boundaries

- `require_repo` must reject any repo id absent from MCP settings, and
  `AuthorityError` must remain a `ValueError` subclass so legacy handlers do not
  silently stop catching it.
- `require_within_coordination` must confine resolved paths to
  `coordination_root`, rejecting both absolute paths outside it and relative
  traversal escapes.
- The tests exercise the guards directly; they do not drive an application entry point or MCP
  dispatch, and they assert on message substrings, not exact strings.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two guards under test live in the application layer. | `require_repo`; `require_within_coordination` | mcp/src/agents_remember/kernel/authority.py:16-24; mcp/src/agents_remember/kernel/authority.py:27-35 |
| `AuthorityError` is the rejection type and is a `ValueError` subclass via `AgentsRememberError`. | `AuthorityError`; `AgentsRememberError` | mcp/src/agents_remember/errors.py:18-19; mcp/src/agents_remember/errors.py:68-74 |
| `McpRuntimeConfig`, `RepositoryScope`, and `path_is_relative_to` define the config and confinement primitives the guards rely on. | `McpRuntimeConfig`; `RepositoryScope`; `path_is_relative_to` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:76-81; mcp/src/agents_remember/kernel/primitives/runtime_config.py:123-147; mcp/src/agents_remember/kernel/primitives/runtime_config.py:694-699 |

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T00:22:04+02:00 — 260731-EFA-L6 S18-B05 curator: repaired and normalised mechanical citation findings with current source anchors and fixer-generated ranges; no semantic claim changes. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
