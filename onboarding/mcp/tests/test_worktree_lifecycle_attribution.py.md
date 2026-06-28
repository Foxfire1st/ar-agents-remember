# test_worktree_lifecycle_attribution.py

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/tests/test_worktree_lifecycle_attribution.py`         |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-06-13T18:45+02:00                                     |
| lastVerifiedCommitHash | `84e95ad0379cd864af3cbae21b7ffe3fd2d2b1b1`                 |
| lastVerifiedCommitDate | 2026-06-28T18:49:06+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Covers the slice-2c controller attribution helpers (`_attribute_start`,
`_attribute_attach`): `worktree_start` promotes the active lifecycle (or adopts a
minted id) and `worktree_attach` resumes the contract's lifecycle, driving
promote / adopt / save-gate on a real ambient without standing up git worktrees.

## Code Commentary

### Logic

`AttributeStartTests` assert a `started` result promotes an active lifecycle
(scope = `repo_id`, emits `lifecycle.promoted`), adopts the minted id when none is
active, does nothing for a non-`started` result, and is a no-op when no ambient is
installed. `AttributeAttachTests` assert attach adopts when none is active, raises
`SaveGateRequired` over an unsaved fleeting current, resolves with `discard`, and
no-ops when the result carries no lifecycle id.

### Conventions

Inserts `mcp/src` on `sys.path` (the suite idiom). `_AttributionCase` builds an
`AmbientLifecycle` over a `tempfile` `EventStore` with a long heartbeat and calls
`shutdown()` in cleanup; the helpers are exercised directly with synthetic
snake_case result payloads (no git/provider machinery).

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The controller attribution helpers under test. | [worktree_tools.py](agents-remember/mcp/src/agents_remember/controllers/worktree_tools.py) |
| The ambient lifecycle they drive (`promote`/`attach`). | [ambient.py](agents-remember/mcp/src/agents_remember/observer/ambient.py) |
| The save-gate signal they assert (`SaveGateRequired`). | [save_gate.py](agents-remember/mcp/src/agents_remember/observer/save_gate.py) |

## Series-Contract Notes

Lifecycle-attribution tests verify that controller attribution can use `enclosure_path` while retaining fallback behavior for payloads that still expose `contract_path`.

## Update History

- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: lifecycle attribution tests now use `series-contract.md` enclosure paths and cover the controller fallback from `enclosure_path` to legacy `contract_path`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00: Created for slice 2c — controller promote/adopt/save-gate
  attribution tests. Verification metadata is pinned until closeout stamps the 2c
  code commit.
