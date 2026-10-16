# mcp/src/agents_remember/worktrees/modules/capture_baseline.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Hold a request-local proof of equal physical snapshots spanning a private-index capture. Reuse requires the same tree and current index/file snapshot, plus current HEAD when the caller supplied a head binding. Memory review supplies the bracketed memory HEAD; the future-code helper omits this optional binding and checks its route identity separately. Unreadable or changed bound operands force re-derivation.

## Code Commentary

The request-local memo scope may also carry an on_capture observer. Nested scopes inherit the current observer unless explicitly replaced; both observer and any newly-created memo dictionary reset in finally. An accepted unchanged before/after capture notifies that observer with the repository path so cache dependencies include the actual capture owner. This adds observation, not longer-lived reuse or stronger physical atomicity.

Hold a request-local proof of equal physical snapshots spanning a private-index capture. Reuse requires the same tree and current index/file snapshot, plus current HEAD when the caller supplied a head binding. Memory review supplies the bracketed memory HEAD; the future-code helper omits this optional binding and checks its route identity separately. Unreadable or changed bound operands force re-derivation.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- Hold a request-local proof of equal physical snapshots spanning a private-index capture. Reuse requires the same tree and current index/file snapshot, plus current HEAD when the caller supplied a head binding. Memory review supplies the bracketed memory HEAD; the future-code helper omits this optional binding and checks its route identity separately. Unreadable or changed bound operands force re-derivation. [1]

## Current source evidence


- Capture dependency observation is request-local and restored on every scope exit. [2]
