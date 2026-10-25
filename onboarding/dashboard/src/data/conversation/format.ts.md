# dashboard/src/data/conversation/format.ts

## Governing Overview

[data/conversation overview](overview.md)

## Purpose

The surviving presentation convention is `humanizeDuration(ms)`, a pure display helper used by the serving build stamp. It implements absent-duration and fixed-readable-duration rules; this module is no longer a broad Chats chip/ID/freshness/truncation library.

## Code Commentary

The private `ABSENT` glyph is an em-dash. Negative or non-finite input returns it. Below one second the helper rounds milliseconds; otherwise it floors to seconds and displays the two most significant units: seconds, minutes/seconds, hours/minutes or days/hours. It must not display raw minutes or six-decimal seconds. There are no SEP, joinChips, shortId, humanizeAge, freshnessTone, truncateMiddle or harnessLabel exports. The reducer does not call presentation helpers. No notifier heartbeat, rail, library or timeline consumer is implied.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries are
configured. This one-to-one card therefore relies on its direct agents-remember source/tests and the
reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- Source tests assert absent-duration glyph and fixed readable durations, not the removed chip/ID/freshness helpers. [1]

- ServingBuildStamp uses humanizeDuration for uptime; no notifier consumer remains. [3]

The developer visual-findings §A rules this module encodes (task-note pointer: `260720-developer-dashboard-visual-findings.md`).

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
