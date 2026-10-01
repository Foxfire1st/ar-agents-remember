# mcp/tests/test_application_guards.py

## Governing Overview

[overview.md](../overview.md)

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

## Evidence

### Repo-Internal References

- The two guards under test live in the application layer. [1]
- AuthorityError is the typed repository/path refusal used by application guards. [2]
- All such domain errors inherit ValueError through AgentsRememberError. [3]
- `McpRuntimeConfig`, `RepositoryScope`, and `path_is_relative_to` define the config and confinement primitives the guards rely on. [4]
