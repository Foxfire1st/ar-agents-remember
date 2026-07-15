# mcp/tests/test_harness_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-15T20:05:47+02:00 |
| lastVerifiedCommitHash | `fc2e8b22abf09cd1b6d8c547bca25e59877b34aa` |
| lastVerifiedCommitDate | 2026-07-15T21:46:02+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-adapter conformance suite for the protocol-neutral harness control contract, bridge, terminal
surface, and private IPC boundary.

## Code Commentary

### Logic

The suite drives exact identity and capability handshakes, normalized snapshots/events, immediate
and queued acceptance, blocked/settling/completion states, disconnect ambiguity, reconciliation
without resend, bounded retention, draft custody, and graceful/forced shutdown. IPC scenarios cover
private endpoint permissions, exact identity, malformed requests, and peer loss after accepted
dispatch without losing the preserved vendor correlation.

ACPUI-L1 adds the normalized `advertise()` method to the deterministic fake adapter. It returns an
empty `CapabilitySnapshot`, allowing the shared bridge conformance suite to continue satisfying the
expanded `HarnessProtocolAdapter` boundary without pretending that this generic fake owns a vendor
catalog. Vendor-specific discovery and catalog assertions remain in the Claude, Codex, and Pi test
modules.

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase`, fixed timestamps and identities, bounded fake
queues, and deterministic adapter events. Assertions favor whole protocol outcomes and loud error
messages over transport timing heuristics.

### Invariants And Boundaries

- The fake adapter proves the common protocol contract without registering a production driver.
- Its empty capability advertisement is a structural test double only; it must not be interpreted
  as a static default catalog or capability-discovery fallback.
- Tests assert bounded-time loud failure rather than allowing stranded awaits.
- Accepted-dispatch IPC peer loss contains only the documented broken-pipe/reset paths; identity,
  protocol, validation, dispatch, and unrelated failures remain loud.
- Ambiguous sends remain reconcilable and are never blindly retried; draft-preservation tests keep
  surface ownership and whole-message ordering explicit.

### Todos

None known for this leaf.

## Docs References

No Domain Documentation category is configured for this repository, so no live documentation
source was available for this test-file curation pass.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured Domain Documentation source was available to cite. | — | — |

## Repo-Internal References

The test module directly proves the fake-adapter bridge contract; the adapter protocol defines the
new advertisement method it now satisfies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The fake adapter implements startup, snapshots, and an intentionally empty normalized advertisement before its event and submit behavior. | L54-L100 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| The core conformance path proves ordered terminal/durable acceptance and stable launch ownership. | L218-L239 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| State-event coverage proves running, blocked, settling, completion, readable terminal output, and escape stripping. | L341-L414 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| The delayed-reply IPC regression contains peer loss after accepted dispatch and reconciles the preserved vendor correlation without retry. | L727-L780 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| `HarnessProtocolAdapter` now requires cached capability advertisement alongside startup, snapshot, submit, reconciliation, and shutdown. | L31-L48 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |

## Cross-Repo References

No sibling repository is required to prove this protocol-neutral test suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented the fake adapter's intentionally
  empty normalized advertisement and its boundary from vendor catalog discovery; corrected the
  governing overview backlink while preserving existing verification metadata.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: documented delayed-reply peer-disconnect
  regression and bridge reconciliation result with narrow error containment.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for fake-adapter
  conformance, R11 draft preservation, ambiguous-send recovery, bounds, and shutdown coverage.
