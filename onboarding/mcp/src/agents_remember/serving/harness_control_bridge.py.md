# mcp/src/agents_remember/serving/harness_control_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-14T12:00+02:00 |
| lastVerifiedCommitHash | `cff3e8f9a64258ea3e7d3007e2153b22c01e273b` |
| lastVerifiedCommitDate | 2026-07-14T14:23:24+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Hosts one exact harness identity, validates adapter handshake/capabilities, serializes terminal and
durable submissions through one bounded queue, and publishes normalized snapshots/transcripts.

## Code Commentary

Start refuses identity, protocol, readiness, or capability mismatches and force-cleans a rejected
adapter. Submission receipts remain distinct from terminal completion; reconciliation and explicit
unknown resolution handle ambiguous sends. Event reduction and transcript retention are bounded.
Unexpected queue failures publish a loud failed state, resolve active callers, and drain queued
commands; graceful stop therefore cannot strand awaiters.

## Invariants And Boundaries

- The bridge is control authority; pane content is never used to infer readiness or acceptance.
- No automatic resend follows a disconnect after a possible send.
- Unsupported receipts use the bounded submission ledger and remain explicitly unsupported.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Ordered queue and reconciliation ledger. | [harness_control_queue.py](harness_control_queue.py) |
| IPC server/client surface. | [harness_control_ipc.py](harness_control_ipc.py) |
| Terminal rendering/input surface. | [harness_terminal_surface.py](harness_terminal_surface.py) |
| Bridge conformance tests. | [test_harness_control.py](../../../tests/test_harness_control.py) |

### 260713-PHA-L5 Shared Protocol Bridge

The bridge owns adapter lifecycle, exact identity, readiness, correlated immediate/queued/rejected/
unknown receipts, pending interactions, transcript completion, and graceful recovery. It retains
raw vendor detail as evidence without promoting pane diagnostics to authority.

## Update History
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented cross-adapter bridge lifecycle and receipt semantics.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the one-adapter
  bridge, handshake gate, ordered inputs, ambiguous-send recovery, and bounded lifecycle behavior.
