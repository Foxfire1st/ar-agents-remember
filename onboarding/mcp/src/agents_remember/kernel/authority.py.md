# mcp/src/agents_remember/kernel/authority.py

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`kernel/authority.py` is the single home for the shared authority guards that MCP
application entry points use to resolve a caller-named repository and to confine
caller-provided paths to the coordinator root. Both checks used to be copied
verbatim into every application entry point; collapsing them here means the security
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

- The module lives in the kernel (`kernel/authority.py`): it is the lower-layer owner
  of the authority guards, not part of the public tool surface.
- Both functions follow the `require_*` naming convention -- they return the
  validated value or raise, never returning a sentinel.
- Error messages are caller-facing and name the rejected value (`repo_id`) or
  the input role (`label`) so application entry points do not need to wrap them.

## Evidence

### Repo-Internal References

- `RepositoryScope`, `McpRuntimeConfig`, `allowed_repo_ids`, `coordination_root`, and `path_is_relative_to` are defined here. [1]
- `AuthorityError` is the authority-violation error type raised by both guards. [2]
- Worktree application entry points consume these guards for repo resolution and path confinement. [3]
- Provider application entry points route repo validation through "from agents_remember.kernel.authority import require_repo". [4]
- Authority guard returning the repository scope for a configured `repo_id` or raising `AuthorityError`. [5]
- Authority guard resolving and confining a caller value to the coordination root. [6]
