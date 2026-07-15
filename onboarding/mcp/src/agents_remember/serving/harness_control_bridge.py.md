# mcp/src/agents_remember/serving/harness_control_bridge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_bridge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:19+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Hosts one exact harness identity, validates adapter handshake/capabilities, serializes prompts,
interactions, reconciliation, and model/effort mutations through one bounded queue, and publishes
normalized snapshots/transcripts.

## Code Commentary

### Logic

Start refuses identity, protocol, readiness, or capability mismatches and force-cleans a rejected
adapter. `set_model` and `set_effort` require a running bridge and delegate to the same command queue
as prompt submission, interaction response, reconciliation, and stop. Submission receipts remain
distinct from terminal completion; reconciliation and explicit unknown resolution handle ambiguous
sends. Event reduction and transcript retention are bounded. Unexpected queue failures publish a
loud failed state, resolve active callers, and drain queued commands.

### Conventions

The bridge is a lifecycle/state publisher; harness-specific set evidence belongs to the adapter and
generic evidence validation/ordering belongs to the queue.

### Invariants And Boundaries

- The bridge is control authority; pane content is never used to infer readiness or acceptance.
- A model/effort mutation cannot bypass the serialized queue or race a prompt accepted through this
  bridge.
- No automatic resend follows a disconnect after a possible send.
- Unsupported receipts use the bounded submission ledger and remain explicitly unsupported.

### Todos

None known for the L3 bridge seam.

## Docs References

No Domain Documentation source is configured for this repository, so no live
domain-documentation pass was available for this update.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The protocol owns vendor-specific setters; the queue owns order and result validation.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The adapter protocol requires both live setters and supplies explicit unsupported results when no adapter exists. | L31-L48; L157-L173 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The command queue serializes both setters and validates every returned `SetResult`. | L73-L180; L301-L386; L476-L508 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |

## Cross-Repo References

No external repository boundary is implemented by the bridge.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

### 260713-PHA-L5 Shared Protocol Bridge

The bridge owns adapter lifecycle, exact identity, readiness, correlated immediate/queued/rejected/
unknown receipts, pending interactions, transcript completion, and graceful recovery. It retains
raw vendor detail as evidence without promoting pane diagnostics to authority.

## Update History

- 2026-07-16T01:19+02:00 — 260714-ACPUI-L3 curator: documented bridge-level model/effort methods,
  their shared command ordering with prompts and interactions, and the adapter/queue ownership split.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented cross-adapter bridge lifecycle and receipt semantics.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for the one-adapter
  bridge, handshake gate, ordered inputs, ambiguous-send recovery, and bounded lifecycle behavior.
