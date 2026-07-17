# mcp/tests/test_hosted_control_conformance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_control_conformance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
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
protocol incompatibility through the public hosted-control client helpers.

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

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The matrix source directly proves the shared scenario and the protocol interface defines its new
advertisement requirement.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The matrix enumerates the three native harness ids, and its fake adapter implements startup, snapshots, and an intentionally empty advertisement. | L47-L84 | [test_hosted_control_conformance.py](agents-remember/mcp/tests/test_hosted_control_conformance.py) |
| The generic fake implements structurally valid immediate model/effort setters without claiming an effective value; the matrix does not exercise them. | L95-L107 | [test_hosted_control_conformance.py](agents-remember/mcp/tests/test_hosted_control_conformance.py) |
| Every harness identity runs through ready state, immediate/queued delivery, blocked interaction, completion, ambiguity/reconciliation, and shutdown. | L201-L317 | [test_hosted_control_conformance.py](agents-remember/mcp/tests/test_hosted_control_conformance.py) |
| Restart recovery rebinds the same identity and validates protocol incompatibility through the private endpoint. | L319-L386 | [test_hosted_control_conformance.py](agents-remember/mcp/tests/test_hosted_control_conformance.py) |
| The shared adapter protocol requires normalized cached advertisement and setters alongside the existing hosted-control lifecycle. | L31-L53 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |

## Cross-Repo References

No sibling repository is needed for this same-repository conformance matrix.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

Shared hosted fakes now conform to the epoch/full-operation-ref port, including restart generation,
op-aware preflight, guarded write, and exact completion. The matrix prevents one adapter from
quietly retaining native queue or id-only release behavior.

## Update History

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
