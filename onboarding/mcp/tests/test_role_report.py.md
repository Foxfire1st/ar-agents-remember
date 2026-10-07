# mcp/tests/test_role_report.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The focused suite proves the one read-only report route's serving, confinement and named refusals.

## Code Commentary

Coverage: every launchable role's report is read unchanged (task-bound and taskless); a caller cannot name a path; missing, unreadable and outside-root reports each answer their own refusal; a rewritten receipt cannot substitute a sibling, handover or nested file; a damaged, non-regular or symlinked receipt answers the report-specific refusal; an absent access alias still serves the canonical file while a retargeted alias gets its own refusal; a FIFO is refused before opening; the read is bounded; another execution or selection cannot read the report.

## Invariants And Boundaries

These are behavioral tests of the route on synthetic receipts and reports. They do not establish a live host, a real report's content, or an acceptance verdict, and the fixture world is built per test.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Reads the deterministic report of every launchable role, task-bound and taskless, and leaves the receipt, report bytes and mtimes unchanged. [1]
- The request model has no path field; a request that tries to carry one cannot select a sibling file. [2]
- A missing report, an unreadable one and a recorded path outside the product root each answer their own named refusal. [3]
- A receipt rewritten to name a sibling, handover or nested file is refused because the served name is launch-derived. [4]
- An absent report-access alias still serves the canonical recorded file; a retargeted alias receives its distinct refusal. [5]
