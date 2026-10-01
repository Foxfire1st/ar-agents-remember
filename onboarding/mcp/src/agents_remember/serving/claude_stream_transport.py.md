# claude_stream_transport.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository; repository code and tests are the authority.

No configured live domain-documentation source was available.

### Repo-Internal References
- The adapter's floor-gated sub-agent-text probe stops the transport and starts the same object again, so a completed stop must release process ownership for the relaunch to launch at all. [1]
- The adapter's own shutdown stops the transport before it cancels the state reader, so ownership release is the final shutdown step rather than an early reset. [2]

#### 260713-PHA-L6 Boundary

Transport startup and framing remain strict and bounded. Compatibility validation belongs to the
correlated structured protocol messages, not a separate CLI version subprocess or pane/log
fallback.

### Cross-Repo References

No meaningful cross-repo references found.

This file implements a repository-local contract.

## 260715-FEUI-L5 Submission Authority Delta

All Claude prompt, response, and setter writes share one transport lock. The caller supplies a final
authority guard, executed immediately before the framed write, so an atomic withdrawal winner emits
zero candidate bytes and unrelated response traffic cannot interleave a control frame.
