# mcp/tests/test_harness_control_claude.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Reusable Claude stream-json fake transport, fixture replay and adapter-operation builders.

## Code Commentary

### Logic

The fake transport queues incoming frames, records writes and launch arguments, invokes the before-write callback before recording a frame, and exposes controlled disconnect/stop. A scripted relaunch drains the stop sentinel and replays the configured startup frames.

Adapter construction injects the transport, fixed clock and correlation sequence. Replay helpers preserve the session while transforming slash-command text to its structured command echo. Setter helpers create a fresh operation reference and preflight it before invoking the adapter. Bounded activity/snapshot waits fail after twenty scheduler yields. The embedded stub speaker supports initialize/model-list responses and emits a deterministic init/result sequence.

### Invariants And Boundaries

This retained module defines support objects and builders; it contains no collected test functions. Its former family-wide coverage narrative is historical. Helper availability is not evidence that a removed scenario still runs.

## Evidence

### Repo-Internal References

- Fake stream ownership, relaunch frames and write ordering. [1]
- Adapter dependencies are injected explicitly. [2]
- Slash-command replay preserves the command/arguments representation. [3]
- Operation identity is unique within the helper sequence. [4]
- Model setters preflight the operation before invocation. [5]
- Activity waits have a bounded failure path. [6]

### Docs References

No external documentation is needed for these source-owned helper facts.

### Cross-Repo References

No separate cross-repository authority is established by this helper module.
