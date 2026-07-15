# mcp/tests/test_hosted_control_conformance.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_hosted_control_conformance.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05:47+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
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

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase` and `subTest` to apply identical assertions to
all three harness ids. Fixed identities, Unix-socket endpoints, and deterministic fake events keep
the matrix protocol-focused and independent of vendor processes.

### Invariants And Boundaries

- The matrix tests the shared hosted protocol, not vendor-specific panes, logs, catalog parsing, or
  model APIs.
- The empty advertisement is a structural fake only and must never become a production catalog
  fallback.
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
| Every harness identity runs through ready state, immediate/queued delivery, blocked interaction, completion, ambiguity/reconciliation, and shutdown. | L187-L303 | [test_hosted_control_conformance.py](agents-remember/mcp/tests/test_hosted_control_conformance.py) |
| Restart recovery rebinds the same identity and validates protocol incompatibility through the private endpoint. | L305-L372 | [test_hosted_control_conformance.py](agents-remember/mcp/tests/test_hosted_control_conformance.py) |
| The shared adapter protocol requires normalized cached advertisement alongside the existing hosted-control lifecycle. | L31-L48 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |

## Cross-Repo References

No sibling repository is needed for this same-repository conformance matrix.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented the matrix fake's intentionally
  empty normalized advertisement and the boundary that keeps vendor discovery in native-adapter
  suites; preserved existing verification metadata.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: added cross-adapter protocol conformance matrix.
