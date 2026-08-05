# mcp/tests/test_serving_harness_control_api.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_serving_harness_control_api.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-19T00:06+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

HTTP contract suite for the server-only own-adapter boundary: pre-session capability advertise,
exact-session live advertise/set, reliable whole-message submit, same-id reconciliation, public
normalization, and liveness-first status classification.

## Code Commentary

### Logic

The pre-session route freezes the `ar-harness-capabilities/v1` envelope and forwards explicit
refresh. A failed refresh is `503 control-unavailable` with no stale capability body. Live advertise
returns only the normalized snapshot; the route module is inspected to reject any terminal-paste
dependency.

Model and effort routes pass through honest `SetResult` values, including queued and unsupported,
as HTTP 200 rather than translating them into success claims. Submit preserves the caller's full
multiline string, request id, source, timestamps, and normalized vendor correlation; source, request
id, and expected epoch are asserted off the `ControlSubmission` descriptor the route passes as the
third positional argument to the control client, not off a keyword dict. The test seeds
sensitive-looking private `raw` values and proves neither submit nor reconcile exposes `raw`, argv,
environment, auth, or vendor-specific nested data. The blocking client's UTF-8 JSON encoder is the
transport authority for Unicode; this route case directly pins whole multiline text without
splitting it.

The final status matrix proves ordering: absent or already-stopped rows are 404; a newly observed
dead row is also 404; only then are live plain/legacy rows classified as 409 unsupported; a live
native row reaches its exact-session control helper.

### Conventions

The module registers only the focused routes on a small `FastAPI` app, uses a temporary real
`TerminalCatalog`, and patches the blocking client/liveness seams. Both registration sites pass one
`ConversationRuntime` positionally — carrying `ConversationScope(workspace_root=..., coordination_root=...)`
as the immutable scope plus the harness registry, catalog, host, liveness clock/config, capability
catalog, and a `LocalOperatorAuthorizationResolver.for_workspace(...)` authorization — rather than
the loose keyword run it used before. Assertions compare complete
public JSON where the contract is frozen and explicitly search serialized output for forbidden
private data.

### Invariants And Boundaries

- Public shapes are harness-neutral and omit adapter-private `raw`; normalized vendor correlation
  may remain as acceptance evidence.
- `SetResult` acceptance is passed through honestly, including `queued`, `unknown`, and
  `unsupported`; the route does not simulate a set or paste a command.
- Submit carries one complete caller message and request id to the exact session. Reconciliation
  uses that same id and never resubmits.
- Liveness is established before endpoint-support classification: unknown/stopped/dead is 404,
  live unsupported is 409, and only live native sessions reach IPC.
- Request/response carries command evidence only; existing event/transcript streams remain
  observational.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test source directly freezes the public HTTP boundary; the route and serializers provide the
same-repository implementation evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| The pre-session endpoint forwards refresh and returns the exact normalized envelope. | `test_pre_session_capabilities_freeze_envelope_and_refresh` | mcp/tests/test_serving_harness_control_api.py:129-147 |
| Failed pre-session refresh uses the capability catalog's server-vocabulary error reader instead of stale capabilities. | `readError` | dashboard/src/data/capabilityCatalog.ts:138-152 |
| The shared SetResult contract preserves the exact acceptance vocabulary used by the route outcomes. | `test_set_result_serialization_keeps_the_five_value_acceptance_contract` | mcp/tests/test_harness_capabilities.py:132-156 |
| Submit preserves one whole multiline message and normalized correlation while omitting private raw, argv, and environment data. | `test_submit_preserves_whole_message_request_and_vendor_correlation` | mcp/tests/test_serving_harness_control_api.py:192-227 |
| Reconcile preserves the same request/vendor correlation and strips private vendor/auth details. | `test_reconcile_keeps_the_same_request_correlation` | mcp/tests/test_serving_harness_control_api.py:482-506 |
| Unknown/stopped/dead rows are 404 before live plain/legacy rows become 409; a live native row reaches the control client. | `test_status_order_is_unknown_or_dead_then_live_unsupported_then_native` | mcp/tests/test_serving_harness_control_api.py:677-725 |
| The capability registrar owns exact-session advertise and set routes. | `_register_capability_routes` | mcp/src/agents_remember/serving/harness_control_api.py:220-289 |
| `_register_submission_routes` delegates to `_register_submission_write_routes`, which installs `api_terminal_submit` and `api_terminal_reconcile` with public serializers. | `_register_submission_routes`; `_register_submission_write_routes`; `api_terminal_submit`; `api_terminal_reconcile` | mcp/src/agents_remember/serving/harness_control_api.py:292-298; mcp/src/agents_remember/serving/harness_control_api.py:342-423 |
| Liveness observation precedes live endpoint-support classification. | `_running_control_entry` | mcp/src/agents_remember/serving/harness_control_api.py:633-666 |
| Public receipt and reconciliation serializers retain normalized evidence while intentionally omitting internal `raw`. | `public_receipt_json`; `public_reconciliation_json` | mcp/src/agents_remember/serving/harness_control_models.py:930-941; mcp/src/agents_remember/serving/harness_control_models.py:944-955 |
| The exact-session client encodes Unicode with `ensure_ascii=False` and sends one newline-framed JSON request. | "ensure_ascii=False" | mcp/src/agents_remember/serving/harness_control_client.py:505-505 |

## Cross-Repo References

No sibling repository, Toad host, or ACP transport is involved in this own-adapter HTTP contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

API tests now cover epoch-bound submit, authority/status/withdraw raw-free privacy, 64-id batches,
epoch mismatch/id conflict, invalid batches, certified pre-dispatch retry, post-write unknown, and
the complete reconciliation/status lifecycle matrix. They prove errors are mapped before private
state leaks.

## 260718-CHATS-L5I Current Delta

API regressions now cover the control liveness memo and lifecycle-free interaction-response route, including typed non-pending and epoch failure behavior.

This entry supersedes conflicting earlier coverage notes while retaining their history; source verification metadata is deliberately unchanged until the code commit.

## Update History

- 2026-08-04T15:58:25+02:00 — 260731-EFA-L6 S18-B12 curator: expanded the pre-session success claim to its complete refresh-and-normalized-envelope test owner while retaining the route, serializer, liveness, and exact-session client ownership.
- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired two cross-file route and liveness
  citations after `harness_control_api.py` split its handlers into private registrars. The current
  table carries the generated registrar, serializer, and liveness-owner citations; no claim text
  changed.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator: corrected the registration claim and every
  self-citation. The Conventions sentence asserting that the call "passes the required
  `coordination_root` keyword" is no longer true of the source: both
  `register_harness_control_routes` sites now pass one positional `ConversationRuntime` holding
  `ConversationScope(workspace_root, coordination_root)`, the harness registry, catalog, host,
  liveness clock/config, capability catalog, and a
  `LocalOperatorAuthorizationResolver.for_workspace(...)`,
  so that paragraph was rewritten. Also recorded that the submit case now reads source, request id,
  and expected epoch off the `ControlSubmission` descriptor passed as the third positional argument
  instead of comparing a kwargs dict. Re-anchored the five Repo-Internal citations against the
  current file: pre-session/refresh L129-L160, live capabilities and set routes L161-L191, submit
  L192-L227, reconcile L482-L506, and the liveness-first status matrix L656-L725. No route, privacy,
  or status-ordering behavior changed and no test was added, removed, or renamed. Verification
  metadata remains pinned until closeout stamps the candidate commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: refreshed the regression-coverage record for the current backend/shared behavior and preserved the pre-commit verification stamp.

- 2026-07-19T00:06+02:00 — 260718-CHATS-L0 curator: documented the one-line call-shape follow —
  the focused route registration passes the new required `coordination_root` keyword. No HTTP
  contract, privacy, or status-ordering behavior changed. Verification metadata remains pinned
  until closeout stamps the candidate commit.

- 2026-07-17T21:39+02:00 — FEUI-L5: added public lifecycle, privacy, epoch/conflict, batch-bound,
  retry-certificate, ambiguity, and status-matrix coverage.

- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: created the one-to-one sidecar for the frozen
  pre-session envelope, live normalized advertise/set, honest acceptance, whole multiline submit,
  UTF-8 transport ownership, same-id reconciliation, no-private-raw serialization, no-paste module
  boundary, and liveness-first 404/409/native ordering. The source is new and uncommitted, so
  verification hash and date remain empty until closeout.
