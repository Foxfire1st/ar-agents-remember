# mcp/src/agents_remember/controllers/_guards.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/controllers/_guards.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `c20a3292e667d227a3be0c1fb276f8a701df814f`                         |
| lastVerifiedCommitDate | 2026-05-31T14:17:11+02:00|
| governingOverview      | `overview.md`                              |

## Purpose

`_guards.py` is the single home for the shared authority guards that MCP
controllers use to resolve a caller-named repository and to confine
caller-provided paths to the coordinator root. Both checks used to be copied
verbatim into every controller; collapsing them here means the security
boundary is written, reviewed, and tested once -- the copy you forget to update
is the vuln.

## Code Commentary

### Logic

Two module-level helpers operate on an `McpRuntimeConfig`:

- `require_repo(config, repo_id)` returns the `RepositoryScope` for `repo_id` by
  indexing `config.repositories`. A missing key is turned into an
  `AuthorityError` whose message lists `config.allowed_repo_ids` (or `<none>`),
  chained from the original `KeyError`.
- `require_within_coordination(config, value, label)` resolves `value` to a
  `Path` and confines it to `config.coordination_root`. Relative inputs resolve
  against `coordination_root`; the path is then `resolve()`d and checked with
  `path_is_relative_to`. A path that escapes the root raises an `AuthorityError`
  using `label` to name the offending input. The resolved, confined `Path` is
  returned on success.

### Invariants And Boundaries

- MCP settings are the authority for which repo IDs are allowed; only IDs
  present in `config.repositories` resolve, and every disallowed ID raises
  `AuthorityError`.
- A returned path is always absolute, `resolve()`d, and provably inside
  `coordination_root`; any input that would escape the root raises rather than
  returns.
- These guards only validate and confine. They do not read, create, or mutate
  filesystem state, and they hold no I/O or service logic -- callers own that.
- Failures surface exclusively as `AuthorityError`; this module raises no other
  exception type for an authority violation.

### Conventions

- The module is leading-underscore private (`_guards`): it is a controller-local
  helper, not part of the public tool surface.
- Both functions follow the `require_*` naming convention -- they return the
  validated value or raise, never returning a sentinel.
- Error messages are caller-facing and name the rejected value (`repo_id`) or
  the input role (`label`) so controllers do not need to wrap them.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `RepositoryScope`, `McpRuntimeConfig`, `allowed_repo_ids`, `coordination_root`, and `path_is_relative_to` are defined here. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| `AuthorityError` is the authority-violation error type raised by both guards. | [errors.py](agents-remember/mcp/src/agents_remember/errors.py) |
| Worktree controllers consume these guards for repo resolution and path confinement. | [worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| Provider controllers route repo validation through `require_repo`. | [provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py) |

## Update History

- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
