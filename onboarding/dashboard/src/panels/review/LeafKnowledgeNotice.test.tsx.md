# dashboard/src/panels/review/LeafKnowledgeNotice.test.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Three standalone worklist-component cases mount `LeafWorklistView` and `SubjectWorklistItems` over the retained `laneReview.trees` capture and explicit read states. This file no longer mounts `LeafKnowledgeNotice` or a held `ReviewSurface` continuity journey.

## Code Commentary

### Component cases

Each of the three current cases mounts worklist components: visible loading/failure/unconverted statuses; all delivered items and file links with identifiers-only disclosure boundaries and click callbacks; and selected-record item filtering, honest empty wording and comparison-mismatch refusal.

### Mounted surface cases

No surviving case mounts a family/invariant surface with a held leaf-wide read. The retained component cases assert a status for pending reads, a next action for unavailable reads, and explicit unconverted-memory wording rather than an empty notice.

### Limits

This is standalone jsdom component/callback evidence, not mounted-surface status-node continuity, browser or screen-reader completion-announcement proof.

## Evidence


- The pending, unavailable and unconverted worklist reads, each shown through a status role. [1]


- The delivered worklist items and file links, with the identifiers-only disclosure and the click callbacks the case invokes. [2]


- Record-specific items, the honest empty wording and the comparison-mismatch refusal. [3]


- The components under test: `LeafWorklistView` and `SubjectWorklistItems`. [4]


- The current worklist-view case renders loading, unavailable and not-converted inputs directly and checks their visible status text. The earlier held-read and mounted-surface continuity account is historical; this case does not assert it. [5]

- Leaf-wide tree fixture for notice states [6]
- Notice mount helper for read states [7]
- Changed paths with items for file links [8]
- Record-only fixture for the honest empty state [9]
