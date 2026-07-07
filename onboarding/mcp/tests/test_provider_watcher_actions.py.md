# test_provider_watcher_actions.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_provider_watcher_actions.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T16:30+02:00                     |
| lastVerifiedCommitHash | `946ecca65e02faf864ea024ae1056600cd0c8021`                |
| lastVerifiedCommitDate | 2026-07-07T17:26:18+02:00|
| governingOverview      | `../overview.md`                              |

## Governing Overview

[overview.md](../overview.md)

## Purpose

`test_provider_watcher_actions.py` guards the watcher-action naming contract
and its containment edge: `refresh` is rejected with guidance (naming
`restart` and `invalidate-indexes`), unknown actions list `invalidate-indexes`
in the error but not `refresh`, `invalidate-indexes` REFUSES when providers
are disabled on disk (containment R1, 260707-HFX-L1 — the rebuild launches
indexers), and `stop` stays allowed under the same disabled authority.

## Code Commentary

### Logic

A `_config_without_providers()` helper builds a minimal stub config with an
empty `providers` dict — enough to exercise action validation before any real
provider is contacted. `_disk_disabled_config(tmp)` goes one step further
because launch-capable actions re-read the on-disk authority: it writes a REAL
authority file saying `"providers": {}` into a temp dir and stubs a config
whose `config_path` points at it (plus the coordination/workspace roots the
reload parse needs).

`WatcherActionNamingTests` calls `provider_watchers_tool` directly:

- `test_refresh_is_rejected_with_guidance`: passing `action="refresh"` raises
  `ValueError` whose message mentions both `restart` and `invalidate-indexes`.
- `test_unknown_action_lists_invalidate_indexes`: a bogus action raises
  `ValueError` containing `invalidate-indexes` but not `refresh`.
- `test_invalidate_indexes_refused_when_disabled_on_disk`:
  `action="invalidate-indexes"` against a disk-disabled authority raises
  `ConfigError` whose message names `containment R1` and `disabled` — the old
  behavior (dispatch with empty steps) silently honored a stale boot snapshot.
- `test_stop_still_allowed_when_disabled_on_disk`: `action="stop"` with
  `dry_run=True` still returns `operation="provider_watchers"` — the gate must
  never block teardown.

### Conventions

No provider configuration, Docker, or network access required. Validation runs
before provider look-up, so a stub config is sufficient; only the disk-gated
actions need the temp authority file the reload actually reads.

### Invariants And Boundaries

The tests protect that `refresh` cannot silently trigger an index rebuild (it
is now an explicit error), that the error message gives actionable guidance,
that the destructive rebuild path refuses under a disk-disabled authority
instead of dispatching off the boot snapshot (containment R1), and that
stopping is always legal.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `provider_watchers_tool` enforces the action naming guard and the launch-authority gate. | [provider_tools.py](agents-remember/mcp/src/agents_remember/controllers/provider_tools.py) |
| The `require_provider_launch_authority` gate whose refusal these tests observe. | [config.py](agents-remember/mcp/src/agents_remember/mcp/config.py) |
| The broader containment suite (authority reload, worktree veto, benchmark filter, lock, metrics). | [test_provider_containment.py](agents-remember/mcp/tests/test_provider_containment.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-07T16:30+02:00 — 260707-HFX-L1 (provider containment R1): the
  dispatch-with-empty-steps expectation for `invalidate-indexes` is replaced by
  `test_invalidate_indexes_refused_when_disabled_on_disk` (`ConfigError` naming containment R1)
  plus `test_stop_still_allowed_when_disabled_on_disk`; added the `_disk_disabled_config` helper
  that writes a real `providers: {}` authority file because launch-capable actions re-read the
  disk. Verification metadata pinned until closeout stamps the HFX-L1 commit.
- 2026-06-01T00:00+02:00 — Created onboarding for the new watcher-action naming guard tests.
