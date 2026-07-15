# mcp/src/agents_remember/serving/pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Composes Pi's native RPC process/protocol/event seams into the normalized hosted adapter, including
live model/thinking advertisement, transient prompt-free discovery, session delivery, interactions,
reconnect, and durable no-resend reconciliation.

## Code Commentary

### Logic

`start` validates the Pi harness id through `pi_rpc_launch`, starts transport, reads `get_state`, then
`get_available_models`, validates the current model/thinking pair against that catalog, and finally
reads `get_entries` for the durable cursor. Failed startup stops transport and resets all partial
adapter state so a later retry is clean. `discover` owns a separate transient transport and reads only
state plus available models—never session entries or a prompt—before forced shutdown. `advertise`
revalidates cached catalog rows against current retained state. Existing busy steer/follow-up,
settlement, extension interaction, reconnect, and post-cursor reconciliation remain intact.

### Conventions

Internal request ids are monotonically generated per adapter. Model keys are provider-qualified
`provider/id` values. Running advertise is synchronous and no-RPC; discovery is asynchronous because
it owns a transient Pi process.

### Invariants And Boundaries

- The current `get_state` model must exist in `get_available_models`, and its thinking level must
  belong to that model's own menu; contradictions fail loudly.
- Discovery sends no prompt and does not read durable entries.
- Failed startup/discovery cannot leak a subprocess or leave the instance half-started.
- `get_state` governs readiness/activity and corroborates settlement; reconnect preserves exact
  session identity.
- Ambiguous submissions remain unresolved without durable post-cursor evidence and are never resent.
- No pane/log fallback, ACP transport, Toad host, or composer-paste capability change is present.

### Todos

L2 wires settings-owned Pi `--model`/`--thinking`; L3 adds honest mid-session setters.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Protocol helpers own launch transformation, state sanitization, catalog mapping, and thinking-level
rules; process/event modules remain transport and event boundaries.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Pi protocol parsing provides RPC launch validation, safe state identity, and provider-qualified model-local effort menus. | L114-L130; L176-L234; L383-L427 | [pi_rpc_protocol.py](pi_rpc_protocol.py) |
| The subprocess boundary starts/stops exact launch specs and correlates RPC responses. | L33-L147 | [pi_rpc_process.py](pi_rpc_process.py) |
| The event mapper owns normalized state, settlement, and extension interaction projections. | L41-L170 | [pi_rpc_events.py](pi_rpc_events.py) |

## Cross-Repo References

No external repository boundary is implemented by this adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented state/catalog/entry startup order,
  state-plus-catalog-only discovery, cached current-selection validation, provider-qualified models,
  and fail-clean retry semantics.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: made the version-neutral
  structured Pi contract normative and retained 0.80.6 only as fixture/smoke evidence.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free Pi production startup and retained
  `0.80.6` only as fixture/smoke evidence.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for L1-backed handshake,
  queue behavior, settlement, extension UI, reconnect, cursor reconciliation, and no-resend policy.
