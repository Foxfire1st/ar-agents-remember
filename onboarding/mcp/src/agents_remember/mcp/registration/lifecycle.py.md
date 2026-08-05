# mcp/src/agents_remember/mcp/registration/lifecycle.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                               |
| path                   | `mcp/src/agents_remember/mcp/registration/lifecycle.py`       |
| doc_type               | `file-level-onboarding`                                       |
| lastUpdated            | 2026-07-31T15:31+02:00                                        |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`                    |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
| governingOverview      | `overview.md`                                                 |

## Governing Overview

[registration route overview](overview.md)

## Purpose

`register_lifecycle_tools(server, _config)` declares the six session-lifecycle signals an agent
sends about itself: `lifecycle_start`, `lifecycle_resume`, `lifecycle_turn_end_notification`,
`lifecycle_end`, `switch_lifecycle`, `lifecycle_phase`.

## Code Commentary

### Logic

The registrar's parameter is named `_config` and a comment says why: these six payloads act on the
process-wide **ambient** lifecycle installed by `create_server`, not on resolved settings, so the
config is genuinely unused. It stays in the signature so every module in this package matches the
one `ToolRegistrar` shape `TOOL_REGISTRARS` is typed against — and the wiring test asserts
`lifecycle_start_payload` is called with no arguments at all.

The model never handles lifecycle ids. `lifecycle_start` takes none (the server mints and tracks
it) and is guarded — starting while one is already active is rejected with a reminder naming the
active lifecycle. `switch_lifecycle` leaves the current lifecycle and begins a fresh one; a
persistent lifecycle is paused, an unsaved fleeting one needs `on_unsaved='save'` (promote) or
`'discard'` (abandon); resuming an existing lifecycle is `worktree_attach`, not a tool here.

`lifecycle_turn_end_notification(summary)` is the active **NOTIFY-AND-CONTINUE** turn end: notify
the developer and stop — no wait, no gate — with the next AR tool call next turn resuming
automatically. `lifecycle_resume` is the other direction: blocked back to running once the gate or
question is resolved. `lifecycle_end(outcome)` takes `completed` (the human declared done) or
`abandoned`. `lifecycle_phase(phase)` moves the lifecycle along its phase axis, orthogonal to state:
`request` | `trust-checkpoint` | `reframe-research` | `decide` | `build` | `close`.

### Invariants And Boundaries

- Keep the unused `_config` parameter; the uniform registrar signature is what `TOOL_REGISTRARS`
  types against.
- These declarations must call their payloads **without** the config — the auto-dismiss and
  ambient-state behaviour lives in `mcp/tools/lifecycle.py` and the observer ambient.
- No lifecycle id is ever exposed to the model on this surface.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-08-04T13:00:51+02:00 — 260731-EFA-L6 S18-B11 curator: reconciled the frozen-source ledger, split ambient lifecycle and response-tail ownership, and supplied scoped fixer input for generated ranges. Verification metadata unchanged.

- 2026-07-31T15:31+02:00 — 260731-EFA-L2 curator: created with the package. The six lifecycle
  declarations moved out of `server.py`; the registrar takes `_config` unused, by design, to keep the
  uniform registrar signature. Verification metadata pinned to the pre-change commit until closeout
  stamps the L2 code commit.
