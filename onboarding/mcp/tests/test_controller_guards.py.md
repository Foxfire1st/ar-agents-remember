# mcp/tests/test_controller_guards.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_controller_guards.py`      |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                         |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `../overview.md`                           |

## Purpose

`test_controller_guards.py` is the first direct test coverage for the shared
MCP controller authority guards (F10). The resolve-and-confine checks used to be
copy-pasted across every controller and the rejection path had no dedicated
test; this suite pins both guards in one place so the security boundary is
proven once instead of per-controller.

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
- The tests exercise the guards directly; they do not drive a controller or MCP
  dispatch, and they assert on message substrings, not exact strings.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The two guards under test live in the controllers package. | [_guards.py](agents-remember/mcp/src/agents_remember/controllers/_guards.py) |
| `AuthorityError` is the rejection type and is a `ValueError` subclass via `AgentsRememberError`. | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |
| `McpRuntimeConfig`, `RepositoryScope`, and `path_is_relative_to` define the config and confinement primitives the guards rely on. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |

## Update History

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
