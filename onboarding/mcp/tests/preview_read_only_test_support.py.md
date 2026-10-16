# mcp/tests/preview_read_only_test_support.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

One shared comparison for registered worktree-start preview proofs: preserve startup/Git state and every observed path outside the checked record of the calls. This is test support, not a production log writer or a blanket exclusion of logs.

## Code Commentary

`PreviewRecordState` pairs a whole-root snapshot with the daily line-file and workspace-river bytes, resolved roots and UTC capture day. `admitted_call_days` admits only dates in the inclusive interval between captures, so a midnight crossing is legitimate but an unrelated old-day record-shaped path is not. Created line/detail/event paths must have the expected file/directory kind; existing record files retain their kind and mode, and previously written details retain their full snapshot.

The comparator rejects removal, unexpected additions and non-record path changes. A kept admitted directory may change its modification time only when an admitted new direct child accounts for the entry creation. The record is checked rather than ignored: earlier line/event bytes stay a prefix; new rows name exactly the tools of the observed calls; new detail files are named by new log lines; and river rows have kind `tool.completed`. Repository refs, worktree lists and index-byte observations are equal.

The caller supplies every log-call tool and the completed-call river tools separately when they differ; `expected_river_tools` defaults to `expected_tools`. Raised calls have a log line but no completed event. The current real-start/second-leaf preview regression uses the workspace Event River without a session lifecycle: it judges that real append and rejects a later mode change. The comparator's `unchanged_except` parameter admits only caller-proved append carve-outs, not blanket metadata permission: the caller must prove kind, mode and append separately. It does not promise ambient lifecycle event routing.

The stock fixture keeps the transcript root inside coordination and pre-creates the empty workspace river lockfile; the lockfile is layout and must remain unchanged. This fresh-fixture proof does not define production log retention or budget-loss semantics. It does not authorize arbitrary calls, provider mutations or a third record type; unexpected product writes remain findings, never a widened allowlist.

## Evidence

No Domain Documentation source is configured. These current source/assertion anchors establish the comparison and its caller contract; they do not attest a test execution.

- Captures pair observed state and record bytes with a UTC day. [1]
- Daily record paths are admitted only within the capture-day interval. [2]
- Path classification binds the record names to admitted days and exact roots. [3]
- Created kinds, kept-path preservation and causal directory-entry checks are wired together. [4]
- A kept directory touch needs an admitted new direct child. [5]
- Daily log lines account for calls and new detail files. [6]
- River rows account for completed calls and retain the completed-event kind. [7]

- The top-level comparator preserves repository state and checks both record channels. [8]

- The current preview regression judges a real workspace-river append without a session lifecycle and rejects a later mode change. [9]
