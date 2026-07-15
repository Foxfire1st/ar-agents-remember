# mcp/tests/test_harness_control.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_harness_control.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-16T01:21+02:00 |
| lastVerifiedCommitHash | `06973f6886276d7b3670c2c1e19cbb76928a7892` |
| lastVerifiedCommitDate | 2026-07-16T01:49:31+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Fake-adapter conformance suite for the protocol-neutral harness control contract, serialized
model/effort setters, bridge, terminal surface, and private IPC boundary.

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

ACPUI-L3 gives the fake explicit model/effort methods and records every launch, setter, and prompt
operation. The new scenarios prove one shared FIFO control queue from launch through a setter into
the following prompt; cancelling a caller while a setter is executing does not terminate that
queue when the adapter later completes. A truth-table test rejects mismatched requested values,
illegal acceptance tokens, `echo-verified` without an effective value, accepted results marked
not-ok, and unknown/unsupported results that falsely claim an effect. Each rejected result leaves
the runner usable for the next prompt. The unregistered adapter remains explicitly unsupported for
both setters.

### Conventions

The module uses `unittest.IsolatedAsyncioTestCase`, fixed timestamps and identities, bounded fake
queues, and deterministic adapter events. Assertions favor whole protocol outcomes and loud error
messages over transport timing heuristics.

### Invariants And Boundaries

- The fake adapter proves the common protocol contract without registering a production driver.
- Its empty capability advertisement is a structural test double only; it must not be interpreted
  as a static default catalog or capability-discovery fallback.
- Launch, model/effort setters, and prompts share one ordered command queue; setter completion or
  caller cancellation cannot bypass or poison later work.
- `echo-verified` requires `ok` plus an effective value; `immediate` and `queued` cannot claim one;
  `unknown` and `unsupported` cannot claim acceptance or effect; no sixth acceptance token is valid.
- An adapter without registered native setter support returns `unsupported`, never a simulated set.
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
advertisement and setter methods it now satisfies.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The fake adapter implements startup, snapshots, an intentionally empty normalized advertisement, prompt submission, and explicit setter results. | L55-L155 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Shared ordering coverage proves launch, model setter, and the following prompt execute in one FIFO sequence. | L286-L311 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| Cancelling a caller while a setter is active does not terminate the command queue when the late adapter completion arrives. | L313-L340 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| The invalid-result matrix rejects dishonest evidence and arbitrary acceptance strings without poisoning the runner; unregistered adapters remain explicitly unsupported. | L342-L379 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| The core conformance path proves ordered terminal/durable acceptance and stable launch ownership. | L263-L284 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| State-event coverage proves running, blocked, settling, completion, readable terminal output, and escape stripping. | L481-L555 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| The delayed-reply IPC regression contains peer loss after accepted dispatch and reconciles the preserved vendor correlation without retry. | L867-L921 | [test_harness_control.py](agents-remember/mcp/tests/test_harness_control.py) |
| `HarnessProtocolAdapter` requires cached advertisement and model/effort setters alongside startup, snapshot, submit, reconciliation, and shutdown. | L31-L53 | [harness_control_adapter.py](agents-remember/mcp/src/agents_remember/serving/harness_control_adapter.py) |
| The shared queue places model and effort commands beside prompts and routes them through the same runner. | L90-L112; L113-L172; L295-L316 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |
| Result validation enforces exact acceptance membership and evidence-shape rules, while late completion skips a caller future that is already cancelled. | L475-L509 | [harness_control_queue.py](agents-remember/mcp/src/agents_remember/serving/harness_control_queue.py) |

## Cross-Repo References

No sibling repository is required to prove this protocol-neutral test suite.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-16T01:21+02:00 — 260714-ACPUI-L3 curator: documented one launch/set/prompt FIFO,
  cancellation-safe late completion, the complete SetResult truth matrix including arbitrary
  acceptance rejection, and explicit unsupported fallback setters. Verification metadata remains
  pinned until closeout stamps the L3 code commit.
- 2026-07-15T20:05:47+02:00 — 260714-ACPUI-L1 curator: documented the fake adapter's intentionally
  empty normalized advertisement and its boundary from vendor catalog discovery; corrected the
  governing overview backlink while preserving existing verification metadata.
- 2026-07-14T17:52:13+02:00 — 260713-PHA-L6 curator: documented delayed-reply peer-disconnect
  regression and bridge reconciliation result with narrow error containment.

- 2026-07-14T12:00+02:00 — 260713-PHA-L1 curator pass: created onboarding for fake-adapter
  conformance, R11 draft preservation, ambiguous-send recovery, bounds, and shutdown coverage.
