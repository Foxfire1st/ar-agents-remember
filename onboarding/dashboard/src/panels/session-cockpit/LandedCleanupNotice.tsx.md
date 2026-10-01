# dashboard/src/panels/session-cockpit/LandedCleanupNotice.tsx

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Keeps authoritative landed-cleanup outcomes and unavailable-result recovery visible at the Chats
root, independent of the collapsible rail or the command surface that launched cleanup.

## Code Commentary

An unavailable result renders the exact intended `{label,id}` snapshot, retry against the same
targets, and explicit dismissal. A returned result renders closed/skipped truth and reasons. Retrying
cannot be double-triggered and successful authority replaces the failure notice.

## Invariants And Boundaries

No response is not success and not failure: it is unknown authority. Never drop targets, fabricate a
closed count, or hide recovery inside a pane that can collapse.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; it has no configured Domain
Documentation entries. This card was verified from its direct source/tests and the reviewed L8
task/worker/reviewer evidence.

No configured Domain Documentation source exists for this file.

### Cross-Repo References

The notice consumes the repository-local lifecycle authority client/store; no cross-repository implementation governs it.

No applicable cross-repository source was found.

### Repo-Internal References

- Notice store and detailed cleanup. [1]
- Root host. [2]
