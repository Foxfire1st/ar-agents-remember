# mcp/src/agents_remember/serving/codex_app_server_session.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_session.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-27T14:20+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Strict model-page parsing is isolated from session lifecycle, while the adapter consumes retained
catalog and thread evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| `parse_model_page` validates model descriptions, effort menus/defaults, visibility, and identity. | `parse_model_page` | mcp/src/agents_remember/serving/codex_app_server_state.py:156-227 |
| Session-owned desired-model and desired-effort setters stage the next selection. | `set_desired_model`; `set_desired_effort` | mcp/src/agents_remember/serving/codex_app_server_session.py:226-245; mcp/src/agents_remember/serving/codex_app_server_session.py:247-253 |
| Fresh adapter `turn/start` acceptance promotes the submission's captured pair. | `_start_turn`; `_accept_started_turn` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:434-480; mcp/src/agents_remember/serving/codex_app_server_adapter.py:533-568 |
| The factory deliberately leaves a roleless Codex selection empty so this session resolves catalog defaults. | `create_harness_protocol_adapter` | mcp/src/agents_remember/serving/harness_control_factories.py:48-90 |

## Cross-Repo References

No external repository boundary is implemented by this session owner.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Codex session state no longer owns `BusyPolicy` or advertises a native busy queue capability. It
retains discovery/configuration and desired/effective selection state; prompt ordering and active-
operation authority live above the session in `HarnessSubmissionAuthority`.

## 260727-CHATS-IM-L2 Experimental History Opt-In Delta

Initialization now advertises `capabilities.experimentalApi: true`, and the capability snapshot
reports the same fact (L282-L298; L336-L358). This opt-in only makes experimental history methods
callable. It does not assert that either method exists: the connection-local history reader probes
items first, turns second, and treats runtime results—not Codex version text—as authority.

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T16:40:00+02:00 — 260731-EFA-L6 S18-B12 curator correction (reviewer-BLOCK repair): bound `set_desired_model`/`set_desired_effort` to their complete session-owned setter bodies (226-245, 247-253) instead of one-line adapter calls; model-page parsing and adapter turn/start acceptance keep their own owners; the scoped fixer confirmed the final ranges with no writes.
- 2026-07-27T14:20+02:00 — 260727-CHATS-IM-L2 curator: recorded the experimental API opt-in as
  permission to probe bounded history, never as a version/capability assertion. Verification
  metadata remains pinned while the source change is uncommitted.

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
