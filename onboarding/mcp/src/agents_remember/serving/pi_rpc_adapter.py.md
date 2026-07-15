# mcp/src/agents_remember/serving/pi_rpc_adapter.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/pi_rpc_adapter.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T23:00+02:00 |
| lastVerifiedCommitHash | `5fa7026c644edfb4eb884173b64d31c9a14a6585` |
| lastVerifiedCommitDate | 2026-07-15T23:33:30+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Composes Pi's native RPC process/protocol/event seams into the normalized hosted adapter, including
provider-qualified native model/thinking launch flags, echo-verified startup, live capability
advertisement, transient prompt-free discovery, session delivery, interactions, reconnect, and
durable no-resend reconciliation.

## Code Commentary

### Logic

`launch_knobs` emits the installed Pi native flags `--model <provider/id> --thinking <level>` and
declares both as adapter-owned; `pi_rpc_launch` still adds protocol-owned `--mode rpc`. `start`
reads `get_state`, then `get_available_models`, validates the current model/thinking pair, and—when
a typed expected launch is present—requires both effective values to echo exactly before reading the
durable entry cursor. Successful configured startup records `launchAcceptance=echo-verified`.
Failed startup stops transport and resets all partial state. `discover` owns a separate transient
transport and reads state plus available models only; `advertise` revalidates retained state.
Existing steer/follow-up, settlement, extension interaction, reconnect, and post-cursor
reconciliation remain intact.

### Conventions

Internal request ids are monotonically generated per adapter. Model keys are exact
provider-qualified `provider/id` values; bare ids are not launch aliases. Running advertise is
synchronous and no-RPC; discovery is asynchronous because it owns a transient Pi process.

### Invariants And Boundaries

- The current `get_state` model must exist in `get_available_models`, and its thinking level must
  belong to that model's own menu; contradictions fail loudly.
- A configured launch must use the exact provider-qualified catalog key and must echo both model
  and thinking after startup, countering Pi's native silent thinking clamp.
- Discovery sends no prompt and does not read durable entries.
- Failed startup/discovery cannot leak a subprocess or leave the instance half-started.
- `get_state` governs readiness/activity and corroborates settlement; reconnect preserves exact
  session identity.
- Ambiguous submissions remain unresolved without durable post-cursor evidence and are never resent.
- No pane/log fallback, ACP transport, Toad host, or composer-paste capability change is present.

### Todos

L3 adds honest mid-session setters, including explicit evidence for Pi's asymmetric clamp behavior.

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
| Pi protocol parsing provides RPC launch validation, safe state identity, and provider-qualified model-local effort menus. | L114-L130; L176-L234; L383-L427 | [pi_rpc_protocol.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_protocol.py) |
| The launch validator requires exact Pi catalog keys and model-local launch effort before the configured process starts. | L78-L119 | [harness_launch.py](agents-remember/mcp/src/agents_remember/serving/harness_launch.py) |
| The subprocess boundary starts/stops exact launch specs and correlates RPC responses. | L33-L147 | [pi_rpc_process.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_process.py) |
| The event mapper owns normalized state, settlement, and extension interaction projections. | L41-L170 | [pi_rpc_events.py](agents-remember/mcp/src/agents_remember/serving/pi_rpc_events.py) |

## Cross-Repo References

No external repository boundary is implemented by this adapter.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented exact provider-qualified
  `--model`, native `--thinking`, protocol-owned RPC mode, and post-start model/thinking echo
  verification that exposes rather than trusts Pi's clamp behavior.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented state/catalog/entry startup order,
  state-plus-catalog-only discovery, cached current-selection validation, provider-qualified models,
  and fail-clean retry semantics.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: made the version-neutral
  structured Pi contract normative and retained 0.80.6 only as fixture/smoke evidence.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented version-free Pi production startup and retained
  `0.80.6` only as fixture/smoke evidence.
- 2026-07-14T12:17+02:00 — 260713-PHA-L4 curator: created onboarding for L1-backed handshake,
  queue behavior, settlement, extension UI, reconnect, cursor reconciliation, and no-resend policy.
