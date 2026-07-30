# claude_stream_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_transport.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-30T15:05+02:00 |
| lastVerifiedCommitHash | `2b47ed9520a770b9858e8af1f112f58745dcf473` |
| lastVerifiedCommitDate | 2026-07-30T16:00:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview
[serving overview](overview.md)

## Purpose
Provides bounded stdio subprocess transport for the Claude structured stream-json handshake. Exact
Claude package strings such as 2.1.207 are fixture/smoke evidence only; this transport does not
define production compatibility by CLI version probing.

## Code Commentary
Starts stream-json, reads frames, drains/discards stderr, and force-cleans blocked readers. The
adapter decides compatibility from the consumed structured initialize/system-init messages.
`stop` owns one bounded shutdown — forced kill or stdin close, a timeout-bounded wait that escalates
to kill, then the stderr drain — and releases the owned process and stderr task only after that work
completes, so the object is reusable rather than single-use.

## Invariants And Boundaries
Process bounds prevent hangs/deadlocks but never infer readiness or terminal meaning; sensitive process output is not retained.
The transport owns at most one process at a time: `start` refuses while a process is owned, and a
completed `stop` clears that ownership so the same object may start again. Ownership release is the
last step of shutdown, never an early reset that would abandon a live process or an undrained stderr
task. After a completed stop the not-started guard governs again, so `returncode` reports `None`
rather than the previous process's exit status.

## Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References
| Finding | Citations | Source Path |
| --- | --- | --- |
| The adapter's floor-gated sub-agent-text probe stops the transport and starts the same object again, so a completed stop must release process ownership for the relaunch to launch at all. | `L106-L131` | [harness_control_claude.py](harness_control_claude.py) |
| The adapter's own shutdown stops the transport before it cancels the state reader, so ownership release is the final shutdown step rather than an early reset. | `L437-L444` | [harness_control_claude.py](harness_control_claude.py) |

### 260713-PHA-L6 Boundary

Transport startup and framing remain strict and bounded. Compatibility validation belongs to the
correlated structured protocol messages, not a separate CLI version subprocess or pane/log
fallback.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

All Claude prompt, response, and setter writes share one transport lock. The caller supplies a final
authority guard, executed immediately before the framed write, so an atomic withdrawal winner emits
zero candidate bytes and unrelated response traffic cannot interleave a control frame.

## Update History

- 2026-07-30T15:05+02:00 — 260727-CHATS-IM-L4: documented the single-process ownership contract —
  a completed stop releases the process and stderr task so the adapter's probe relaunch can reuse the
  object, while a live start still refuses. Corrected the transport-lifecycle citation, which pointed
  at `L1-L30` instead of the relaunch and shutdown seams that consume this contract.
- 2026-07-17T21:39+02:00 — FEUI-L5: documented shared write serialization and the final guarded-
  byte seam.
- 2026-07-14T17:00:00+02:00 — 260713-PHA-L6 master-exit correction: removed the obsolete
  version-probing contract from Purpose and Logic; exact package values are fixture/smoke evidence.
- 2026-07-14T16:30:00+02:00 — 260713-PHA-L6 curator: documented that production startup no longer performs an
  exact CLI-version preflight; the transport remains the structured stream boundary.
- 2026-07-14T12:45:11+02:00 — 260713-PHA-L2 source-tip reconciliation: refreshed verification
  metadata to accepted candidate `acb308c50072d8cde0015c4828e39d12480872ed`.
- 2026-07-14T12:30+02:00 — 260713-PHA-L2 curator: created sidecar.
