# test_worktree_lifecycle_attribution.py

| Field                  | Value                                                      |
| ---------------------- | ---------------------------------------------------------- |
| repository             | agents-remember                                            |
| path                   | `mcp/tests/test_worktree_lifecycle_attribution.py`         |
| doc_type               | `file-level-onboarding`                                    |
| lastUpdated            | 2026-08-02T01:05+02:00                                     |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                 |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

Covers the slice-2c application entry point attribution helpers (`_attribute_start`,
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

| Finding | Anchor | Source |
| --- | --- | --- |
| The application entry point attribution helpers under test. | "def _attribute_start" | mcp/src/agents_remember/application/worktree_tools.py:180-180 |
| The ambient lifecycle they drive (`promote`/`attach`). | "def promote"; "def attach" | mcp/src/agents_remember/observer/ambient.py:348-348; mcp/src/agents_remember/observer/ambient.py:364-364 |
| The save-gate signal they assert (`SaveGateRequired`). | `SaveGateRequired` | mcp/src/agents_remember/observer/save_gate.py:34-48 |

## Series-Contract Notes

Lifecycle-attribution tests verify that application entry point attribution can use `enclosure_path` while retaining fallback behavior for payloads that still expose `contract_path`.

## Update History

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 4 citation finding(s); scoped recheck clean.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — No content impact: the only change is in `_AttributionCase.setUp`,
  which after the PLR0913 parameter-object pass builds the ambient as
  `AmbientLifecycle(self.store, timing=AmbientTiming(heartbeat_seconds=3600))` and imports
  `AmbientTiming` next to `AmbientLifecycle`. The long-heartbeat tempfile ambient, the
  `shutdown()` cleanup, and every promote / adopt / save-gate assertion described above are
  unchanged, so the Purpose, Logic, and Conventions claims still hold.
- 2026-06-24T06:35+02:00 - Series-contract leaf enclosure slice: lifecycle attribution tests now use `series-contract.md` enclosure paths and cover the controller fallback from `enclosure_path` to legacy `contract_path`. Verification metadata pinned until closeout stamps the code commit.
- 2026-06-13T18:45+02:00: Created for slice 2c — controller promote/adopt/save-gate
  attribution tests. Verification metadata is pinned until closeout stamps the 2c
  code commit.
