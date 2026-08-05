# mcp/src/agents_remember/kernel/authority.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/authority.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                         |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../overview.md`                     |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `RepositoryScope`, `McpRuntimeConfig`, `allowed_repo_ids`, `coordination_root`, and `path_is_relative_to` are defined here. | `RepositoryScope` | mcp/src/agents_remember/mcp/config.py:68-73; mcp/src/agents_remember/mcp/config.py:113-133; mcp/src/agents_remember/mcp/config.py:635-640 |
| `AuthorityError` is the authority-violation error type raised by both guards. | `AuthorityError` | mcp/src/agents_remember/errors.py:17-23 |
| Worktree application entry points consume these guards for repo resolution and path confinement. | `require_repo` | mcp/src/agents_remember/application/worktree_tools.py:10-10; mcp/src/agents_remember/application/worktree_tools.py:90-90; mcp/src/agents_remember/application/worktree_tools.py:250-256 |
| Provider application entry points route repo validation through `require_repo`. | `require_repo` | mcp/src/agents_remember/application/provider_tools.py:11-11; mcp/src/agents_remember/application/provider_tools.py:438-438; mcp/src/agents_remember/application/provider_tools.py:468-468 |
| Authority guard returning the repository scope for a configured `repo_id` or raising `AuthorityError`. | `require_repo` | mcp/src/agents_remember/kernel/authority.py:16-24 |
| Authority guard resolving and confining a caller value to the coordination root. | `require_within_coordination` | mcp/src/agents_remember/kernel/authority.py:27-35 |

## Update History

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: developer-directed
  retarget of this card's subject: the guards now live in
  `kernel/authority.py` (they were removed from `application/_guards.py` in the
  wave), so this card moved with them; path metadata, the governing-overview
  link, prose, and subject-file citation rows follow. Verification metadata
  pinned until closeout stamps the code commit.
- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 3 citation rows
  (config.py, worktree_tools.py, provider_tools.py) to plain anchored sources. Recorded as a
  Tier-3 report item: the subject file `application/_guards.py` no longer exists in the frozen
  source — both guards now live in `kernel/authority.py` — so retargeting or retiring this card's
  subject is a developer decision; the citation mechanics here are green regardless. Zero findings
  remain.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — 260731-EFA-L6 curator: source moved. `mcp/src/agents_remember/controllers/` was renamed to `application/`, so this sidecar moved with its source; path metadata and every in-body path follow, and the prose adopts "the application layer" / "an application entry point" for what it used to call a controller. Behavior is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-05-31T12:30+02:00 — Created during the 1.0.0 review remediation.
