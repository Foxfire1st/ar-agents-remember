# test_provider_watcher_actions.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/tests/test_provider_watcher_actions.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-06-01T00:00+02:00                     |
| lastVerifiedCommitHash | `4117c3d98eadb4265af6e55f3dd8f2552e8589a0`                |
| lastVerifiedCommitDate | 2026-06-01T20:31:44+02:00|
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`test_provider_watcher_actions.py` guards the watcher-action naming contract:
`refresh` is rejected with guidance (naming `restart` and `invalidate-indexes`),
unknown actions list `invalidate-indexes` in the error but not `refresh`, and
`invalidate-indexes` dispatches correctly under its new name.

## Code Commentary

### Logic

A `_config_without_providers()` helper builds a minimal stub config with an
empty `providers` dict — enough to exercise action validation before any real
provider is contacted.

`WatcherActionNamingTests` calls `provider_watchers_tool` directly:

- `test_refresh_is_rejected_with_guidance`: passing `action="refresh"` raises
  `ValueError` whose message mentions both `restart` and `invalidate-indexes`.
- `test_unknown_action_lists_invalidate_indexes`: a bogus action raises
  `ValueError` containing `invalidate-indexes` but not `refresh`.
- `test_invalidate_indexes_dispatches_under_new_name`: `action="invalidate-indexes"`
  with `dry_run=True` returns `operation="provider_watchers"`,
  `action="invalidate-indexes"`, and a `steps` list.

### Conventions

No provider configuration, Docker, or network access required. Validation runs
before provider look-up, so a stub config is sufficient.

### Invariants And Boundaries

The tests protect that `refresh` cannot silently trigger an index rebuild (it
is now an explicit error), that the error message gives actionable guidance, and
that the destructive rebuild path is available only under its unambiguous name.

## Docs References

No external documentation is needed for these standard-library unit tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant external documentation found. | n/a | n/a |

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| `provider_watchers_tool` enforces the action naming guard. | [provider_tools.py](agents-remember-md/mcp/src/agents_remember/controllers/provider_tools.py) |

## Cross-Repo References

No sibling repository evidence is needed for these tests.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-06-01T00:00+02:00 — Created onboarding for the new watcher-action naming guard tests.
