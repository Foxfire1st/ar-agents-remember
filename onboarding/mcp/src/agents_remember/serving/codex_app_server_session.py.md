# mcp/src/agents_remember/serving/codex_app_server_session.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/codex_app_server_session.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:15+02:00 |
| lastVerifiedCommitHash | `34f818a190c35238dca33552d586ea2ace5d9e06` |
| lastVerifiedCommitDate | 2026-09-16T14:33:47+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l5-ar` uncommitted source; base `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Owns Codex app-server initialization, complete paginated model discovery, dynamic model/effort
resolution, configured thread start/resume, desired-versus-effective mutation state, retained
acceptance evidence, and a separate thread-free discovery path. Since 260915-CAPS-L5 it also owns the
one place an admitted role capsule is applied: `CodexAppServerSettings.capsule_delivery`, the refresh
decision that respects the installed protocol's instruction boundaries, and the legacy-chain switch
scoped to a capsule launch.

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

**CAPS-L5's capsule path (only when `settings.capsule_delivery` is set).** `connect` computes a
`RefreshPlan` before the open call and passes it into `_thread_params`. `_capsule_refresh_plan`
refuses to guess: a resume of a thread this session did not itself open has an unknown applied
revision and becomes a **bounded fresh thread**; a thread this session did open is compared through its
**recorded** binding identity and digest (`CapsuleBindingIdentity.from_report`), never by substituting
the incoming binding — an unreadable record is likewise a fresh thread. `_thread_params` then applies
the legacy switch (`project_doc_max_bytes: 0` on the existing per-thread `config`) and the single
instruction parameter; on a refusal or a fresh-thread decision it **drops `threadId`** rather than
restating instructions onto a thread that already carries another revision or another binding.
`_capsule_report` builds the provenance published on the thread-open evidence
(`capsuleRefresh.mode` + reason, the binding report, and the legacy switch report) — no instruction
prose. Plain Python: read the module's own docstrings for the exact decision table.

### Conventions

The runtime user-agent proves a Codex Desktop host-first product with the exact client name/version
suffix sent in `clientInfo`; the primary product version must
agree with thread `cliVersion`. `model` is the normalized model key; descriptions and effort descriptions are retained.
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
- `_initialize` gives response validation the same client name/version values it sent, so a
  host-first response cannot claim a different Agents Remember client identity.
- **A capsule-free launch is byte-for-byte the previous launch.** With `capsule_delivery=None` the
  session adds no instruction parameter, no suppression key and no report, and the thread-open
  parameters are identical to base. A future editor must not make any of the three unconditional.
- **One capsule per admitted binding, applied at a thread-open boundary.** The installed protocol has
  no `turn/start` instruction field, so an ordinary user message cannot re-apply the corpus; a second
  revision is never stacked onto a live thread — the session drops `threadId` and opens a fresh,
  bounded thread instead.
- **The recorded revision is compared, never assumed.** `_capsule_refresh_plan` reads the binding and
  digest from the session's own previous report; a mismatched binding or an unreadable record is a
  fresh thread, and a refusal plan yields **no** instruction parameters.
- **The legacy-chain observation is published, not invented.** `thread.instruction_sources` is the
  host's own list of loaded instruction documents and is reported verbatim on the thread-open
  evidence; `project_doc_max_bytes: 0` rides the existing per-launch `config` object and is applied
  only when a capsule is delivered.
- **Declared limits, not gaps.** The vendor-side effect of re-sending `developerInstructions` on
  `thread/resume` is unmeasured on the pinned `0.151.0` (no rollout persists until a real turn runs),
  so `IN_PLACE` is schema- and unit-proven only; `FORK_THREAD` has no production caller; and no live
  end-to-end spawn through `terminal_opener` was exercised.

### Todos

None known for the L3 desired/effective state owner. The capsule seam's own open items are declared
limits (vendor resume effect, `FORK_THREAD` in production, the payload size bound routed as `D12`).

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
| `parse_model_page` validates model descriptions, effort menus/defaults, visibility, and identity. | `parse_model_page` | mcp/src/agents_remember/serving/codex_app_server_state.py:172-243 |
| Session-owned desired-model and desired-effort setters stage the next selection. | `set_desired_model`; `set_desired_effort` | mcp/src/agents_remember/serving/codex_app_server_session.py:257-276; mcp/src/agents_remember/serving/codex_app_server_session.py:278-284 |
| Fresh adapter `turn/start` acceptance promotes the submission's captured pair. | `_start_turn`; `_accept_started_turn` | mcp/src/agents_remember/serving/codex_app_server_adapter.py:484-530; mcp/src/agents_remember/serving/codex_app_server_adapter.py:583-618 |
| The factory deliberately leaves a roleless Codex selection empty so this session resolves catalog defaults, and it is the only producer of these settings. | `create_harness_protocol_adapter` | mcp/src/agents_remember/serving/harness_control_factories.py:120-167 |
| Initialize sends and then reuses the exact client identity when validating the host response. | `_initialize` | mcp/src/agents_remember/serving/codex_app_server_session.py:390-413 |
| The capsule carrier on the settings is consumed here and nowhere else; the value type and the refresh rules live in their own module. | `CodexAppServerSettings`; `CodexCapsuleDelivery`; `plan_refresh` | mcp/src/agents_remember/serving/codex_app_server_session.py:73-119; mcp/src/agents_remember/serving/capsule_delivery.py:169-273; mcp/src/agents_remember/serving/capsule_delivery.py:399-440 |
| The refresh decision compares the recorded binding and digest and never substitutes the incoming one. | `_capsule_refresh_plan`; `_capsule_report` | mcp/src/agents_remember/serving/codex_app_server_session.py:435-474; mcp/src/agents_remember/serving/codex_app_server_session.py:476-491 |
| The instruction parameter and the scoped legacy switch are applied on the thread-open parameters; a refusal drops `threadId`. | `_thread_params` | mcp/src/agents_remember/serving/codex_app_server_session.py:493-558 |
| The host's own loaded instruction documents are parsed from the thread-open response and published verbatim. | `_instruction_sources`; `CodexThreadEvidence` | mcp/src/agents_remember/serving/codex_app_server_state.py:274-294; mcp/src/agents_remember/serving/codex_app_server_state.py:59-75 |

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

## 260915-CAPS-L5 Capsule Delivery And Refresh Lifetime

`CodexAppServerSettings.capsule_delivery` is the carrier this session consumes; an owner above
`serving` fills it (`create_harness_protocol_adapter`, the sole producer). Nothing in this module
renders, selects, re-orders or re-derives capsule content: the applied bytes are the compiler's own
`render_instructions()` output, carried by `CodexCapsuleDelivery`.

The lifetime rule the installed protocol forces, stated once: instruction fields exist on
`thread/start`, `thread/resume` and `thread/fork` and **not** on `turn/start`. Therefore
(1) one capsule per admitted binding; (2) an ordinary second turn cannot restate it; (3) a changed
revision on a live thread opens a bounded fresh thread (or a fork when the caller offers one), never a
stacked second revision; (4) an unsupported refresh is reported through the plan's reason, never faked.
The pre-existing operation identity, receipts, cancellation, approvals, model/effort selection,
transcript and native subagent demultiplexing are untouched.

## Update History

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: documented the capsule path this session now owns —
  the settings carrier, the refresh decision that compares the **recorded** binding and digest and
  opens a bounded fresh thread on an unknown revision, the scoped legacy-chain switch on the existing
  per-thread `config`, the published `instructionSources` observation, and the rule that a capsule-free
  launch keeps byte-identical thread-open parameters. Recorded the three declared limits (unmeasured
  vendor `thread/resume` effect, `FORK_THREAD` unexercised in production, no live opener spawn).
  Re-anchored five stale cross-file ranges and added the capsule rows. Verification metadata moves to
  the last committed source `c1dbebf8`; closeout re-stamps the real code commit.

- 2026-08-12T04:15+02:00 — 260731-EFA-L22 Codex Desktop repair: bound initialize-response client
  suffix validation to the exact `clientInfo` name/version sent by this session while retaining
  primary host-version agreement with the opened thread; the old CLI-shaped form is intentionally
  outside this project's runtime contract.

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
