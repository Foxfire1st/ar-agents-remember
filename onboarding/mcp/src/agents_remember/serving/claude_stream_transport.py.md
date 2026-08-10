# claude_stream_transport.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/claude_stream_transport.py` |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-07-30T15:05+02:00 |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb` |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References
| Finding | Anchor | Source |
| --- | --- | --- |
| The adapter's floor-gated sub-agent-text probe stops the transport and starts the same object again, so a completed stop must release process ownership for the relaunch to launch at all. | `_negotiate` | mcp/src/agents_remember/serving/harness_control_claude.py:176-223 |
| The adapter's own shutdown stops the transport before it cancels the state reader, so ownership release is the final shutdown step rather than an early reset. | `finish_reader` | mcp/src/agents_remember/serving/harness_control_claude.py:530-530 |

### 260713-PHA-L6 Boundary

Transport startup and framing remain strict and bounded. Compatibility validation belongs to the
correlated structured protocol messages, not a separate CLI version subprocess or pane/log
fallback.

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| This file implements a repository-local contract. | — | — |

## 260715-FEUI-L5 Submission Authority Delta

All Claude prompt, response, and setter writes share one transport lock. The caller supplies a final
authority guard, executed immediately before the framed write, so an atomic withdrawal winner emits
zero candidate bytes and unrelated response traffic cannot interleave a control frame.

## Update History

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T02:49:11+02:00 — W3-B01 curator: curated 2 Repo-Internal table citations with exact sub-agent-text capability and reader-finish anchors. Verification metadata remains unchanged for closeout.
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
