# mcp/src/agents_remember/serving/codex_app_server_session.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_session.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns Codex app-server initialization, complete paginated model discovery, dynamic model/effort
resolution, configured thread start/resume, desired-versus-effective mutation state, retained
acceptance evidence, and a separate thread-free discovery path.

## Code Commentary

### Logic

`connect` initializes the app-server, reads every `model/list` page, resolves a model-local effort,
and verifies the opened/resumed thread before retaining the catalog. The session then keeps
`desired_model`/`desired_effort` separate from effective `model`/`effective_effort`.
`set_desired_model` accepts only a dynamic catalog row and rebases an incompatible effort to that
row's dynamic default; `set_desired_effort` validates against the desired row. `has_pending_settings`
compares both pairs. `accept_settings_selection` promotes only the exact catalog model/effort carried
by an accepted prompt submission. A matching settings notification may corroborate the desired
pair; a stale effective echo while a deliberate change is pending is ignored, and unrelated drift
fails loudly. Reconnect retains deliberate overrides while initial thread config remains the launch
authority before any setter.

### Conventions

The runtime user-agent proves the client/opaque-version form, and the token must agree with thread
`cliVersion`. `model` is the normalized model key; descriptions and effort descriptions are retained.
Reasoning effort travels through app-server session config and turn parameters. A roleless pre-L4
open derives both defaults from the authenticated catalog. `settingsPending` exposes comparison
state; it is not acceptance evidence by itself.

### Invariants And Boundaries

- `model/list` pagination includes hidden rows, rejects repeated cursors, and fails on the configured
  page bound rather than returning a partial catalog.
- Cold discovery never starts/resumes a thread or sends a turn.
- Start/resume preserves exact thread, model, cwd, sandbox, approval, config, and effective effort.
- Missing, conflicting, or unadvertised effort fails loudly; no global effort enum is accepted.
- `config.model` and `config.model_reasoning_effort` must agree with the dynamically selected pair;
  before deliberate runtime override, the session never accepts a second launch authority.
- Desired choices are always drawn from the retained dynamic catalog and effort remains model-gated.
- Effective choices change only through an accepted turn selection or a matching deliberate
  settings notification; vendor drift cannot silently become the new desired state.
- Reconnect keeps deliberate desired overrides on the same thread rather than restoring stale
  launch settings.
- Failed connect/discover always stops its transient transport.

### Todos

None known for the L3 desired/effective state owner.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation
pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Strict model-page parsing is isolated from session lifecycle, while the adapter consumes retained
catalog and thread evidence.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Model pages validate descriptions, per-model effort menus/defaults, visibility, and identity; submission evidence captures its selection epoch. | L38-L118; L155-L256 | [codex_app_server_state.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_state.py) |
| Adapter setters mutate desired state and fresh `turn/start` acceptance promotes the submission's captured pair. | L153-L211; L220-L272; L344-L413 | [codex_app_server_adapter.py](agents-remember/mcp/src/agents_remember/serving/codex_app_server_adapter.py) |
| The factory deliberately leaves a roleless Codex selection empty so this session resolves catalog defaults. | L22-L56 | [harness_control_factories.py](agents-remember/mcp/src/agents_remember/serving/harness_control_factories.py) |

## Cross-Repo References

No external repository boundary is implemented by this session owner.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Codex session state no longer owns `BusyPolicy` or advertises a native busy queue capability. It
retains discovery/configuration and desired/effective selection state; prompt ordering and active-
operation authority live above the session in `HarnessSubmissionAuthority`.

## Update History

- 2026-07-17T21:39+02:00 — FEUI-L5: removed obsolete busy-policy/native-queue claims and recorded
  the authority boundary.

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented desired/effective separation,
  model-local effort rebasing, pending comparison, accepted-selection promotion, supplementary
  settings notifications, deliberate reconnect overrides, and vendor-drift refusal.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented settings-selected and roleless
  catalog-default resolution, native thread config for model/effort, duplicate config refusal, and
  retention of the resolved desired effort for later turns.
- 2026-07-15T20:05+02:00 — 260714-ACPUI-L1 curator: documented full retained model metadata,
  include-hidden pagination, no-thread discovery, cached advertise, and fail-clean transport
  ownership.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: replaced the exact-0.144.3
  convention with consumed initialize/thread identity and field validation; fixture pins are
  historical evidence only.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented cross-message Codex capability negotiation and
  loud failure for inconsistent structured identity.
- 2026-07-14T12:30+02:00 — 260713-PHA-L3 curator pass: created onboarding for exact initialize,
  model/effort discovery, thread start/resume, and preserved settings. Verification remains unset
  until closeout stamps the code commit.
