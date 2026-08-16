# mcp/tests/test_hosted_control_conformance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_control_conformance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-16T09:45+02:00 |
| lastVerifiedCommitHash | `8bf6edad7e7e65e27cf735be0822f604531d0c8a` |
| lastVerifiedCommitDate | 2026-08-16T10:54:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Cross-adapter conformance matrix that runs one deterministic hosted-control scenario under the
Claude, Codex, and Pi harness identities, from ready startup through delivery, interaction,
completion, ambiguity, restart recovery, incompatibility, and shutdown.

## Code Commentary

### Logic

A shared fake adapter and private IPC server are instantiated once per harness identity. The matrix
asserts ready snapshots, immediate and queued delivery, blocked interaction response, terminal
transcript completion, ambiguous transport reconciliation, graceful stop, restart recovery, and
protocol incompatibility through the public hosted-control client helpers. Prompt delivery is driven
as `submit_control_prompt(entry, text, ControlSubmission(source=..., request_id=...))`: the durable
source and the per-harness request id travel inside one `ControlSubmission` parameter object rather
than as loose keyword arguments.

ACPUI-L1 adds the normalized `advertise()` method to this generic fake adapter. It returns an empty
`CapabilitySnapshot` so every matrix row satisfies the expanded protocol boundary without claiming
that the conformance fake can enumerate any vendor's installed/authenticated models. Dynamic
catalog and model-gated effort behavior remains the responsibility of the native-adapter suites.

ACPUI-L3 adds structurally valid `set_model()` and `set_effort()` methods returning `immediate`
without an effective echo. They keep the shared fake conformant to the expanded adapter protocol;
the matrix does not invoke them and therefore does not claim vendor setter acceptance evidence.
Queue ordering, result validation, and harness-specific switching remain covered by their focused
test modules.

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase` and `subTest` to apply identical assertions to
all three harness ids. Fixed identities, Unix-socket endpoints, and deterministic fake events keep
the matrix protocol-focused and independent of vendor processes.

### Invariants And Boundaries

- The matrix tests the shared hosted protocol, not vendor-specific panes, logs, catalog parsing, or
  model APIs.
- The empty advertisement is a structural fake only and must never become a production catalog
  fallback.
- The fake's immediate setter results are protocol scaffolding only; they must not be treated as
  model/effort conformance or effective-value evidence for Claude, Codex, or Pi.
- Durable delivery evidence remains distinct from explicit consumption, and ambiguous delivery is
  reconciled without blind resend.
- Restart must preserve exact identity and protocol compatibility; incompatible protocol requests
  fail loudly.
- The malformed-response fixture accepts one complete request before replying, so the assertion
  deterministically tests malformed JSON rather than a socket-close race.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Anchor | Source |
| --- | --- | --- |


## Repo-Internal References

The matrix source directly proves the shared scenario and the protocol interface defines its new
advertisement requirement.

| Finding | Anchor | Source |
| --- | --- | --- |
| The matrix enumerates the native harness ids and its fake adapter implements startup, snapshots, and advertisement. | `HARNESSES`; `_Adapter`; `advertise` | mcp/tests/test_hosted_control_conformance.py:49-49; mcp/tests/test_hosted_control_conformance.py:52-165 |
| The fake provides model and effort setters at the adapter boundary. | `set_model`; `set_effort` | mcp/tests/test_hosted_control_conformance.py:101-109; mcp/tests/test_hosted_control_conformance.py:111-119 |
| Every harness identity runs through ready state, delivery, blocked interaction, completion, ambiguity/reconciliation, and shutdown. | `test_ready_delivery_blocked_completion_ambiguity_and_shutdown` | mcp/tests/test_hosted_control_conformance.py:214-345 |
| Restart recovery rebinds the same identity and validates protocol incompatibility and malformed replies through the private endpoint. | `test_restart_recovery_and_incompatible_protocol` | mcp/tests/test_hosted_control_conformance.py:351-413 |
| The shared adapter protocol defines normalized advertisement and setters alongside the hosted-control lifecycle. | `HarnessProtocolAdapter`; `LaunchableHarnessProtocolAdapter` | mcp/src/agents_remember/serving/harness_control_adapter.py:32-59; mcp/src/agents_remember/serving/harness_control_adapter.py:78-88 |

## Cross-Repo References

No sibling repository is needed for this same-repository conformance matrix.

| Finding | Anchor | Source |
| --- | --- | --- |


## 260715-FEUI-L5 Submission Authority Delta

Shared hosted fakes now conform to the epoch/full-operation-ref port, including restart generation,
op-aware preflight, guarded write, and exact completion. The matrix prevents one adapter from
quietly retaining native queue or id-only release behavior.

## Update History

- 2026-08-16T09:45+02:00 — Stabilized the malformed-response conformance seam by accepting the request before returning invalid JSON; production behavior and assertions are unchanged.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:32:09+02:00 — 260731-EFA-L6 S18-B02 curator: split the conformance matrix into exact test/protocol owners, removed unsupported cached-claim wording, and generated final citation ranges with the scoped fixer.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 quality gate: the three `submit_control_prompt` call sites
  now pass a `ControlSubmission(source=..., request_id=...)` parameter object instead of loose
  keyword arguments, so Logic now names that object, and the four line ranges this card cites into
  its own source were re-anchored against the current file (fake adapter and empty advertisement
  L49-L86, the model/effort setters L101-L119, the ready/delivery/ambiguity/shutdown matrix
  L214-L345, and the restart/incompatibility test L347-L414).
- 2026-07-17T21:39+02:00 — FEUI-L5: extended conformance to epoch, full refs, guarded preflight/
  write, restart, and exact completion.

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented the generic fake setter methods as
  protocol scaffolding only and preserved the boundary that keeps acceptance evidence in focused
  shared and native-adapter suites. Verification metadata remains pinned until closeout stamps the
  L3 code commit.
- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented the matrix fake's intentionally
  empty normalized advertisement and the boundary that keeps vendor discovery in native-adapter
  suites; preserved existing verification metadata.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added cross-adapter protocol conformance matrix.
