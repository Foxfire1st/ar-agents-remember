# dashboard/src/panels/review/familyPaging.captured.json

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retain complete real HTTP review responses for a bounded two-sided family walk, so mounted client regressions consume the production wire shape.

## Code Commentary

### Logic

The document identifies one selected subject and family, then stores three before-walk and three after-walk bodies. They were captured through the public-authored family scenario and real HTTP continuation helper at page size four. **MIK-L31 re-captured them from the current route** (MIK-R31 rule 6, the L44-R1-F5 remainder; L44's producer, first build accepted, one attempt; the receipt's `mik_l31_recapture` row, requests `paging1-paging-before-0` to `paging1-paging-after-2`), so the member sources now carry `locator`, `resolved_ranges` and `locator_state`. On this draw the before walk reads 11 items in three bodies (the last with nothing remaining) and the after walk 9. Family order follows the stored identities each build draws afresh, so the late-source case of `ReviewReadCycle.family.test.tsx` opens the subject inside this document's own `family_id` explicitly. Content, memberships and claims can appear on different pages; another side's response can repeat its first page. Those are the cases the read-cycle test must preserve.

### Conventions

Regenerate through the existing scenario and HTTP walk helper when the wire contract changes. Do not hand-edit successful response bodies to manufacture an expected display. Deliberate negative mutations belong in the consuming test and are explicitly asserted as failures.

### Invariants And Boundaries

These are regression fixture records, not the project's published knowledge database, a new selection authority or installed-browser evidence. The complete response keeps comparison, subject, family, source and evidence dimensions available to the real client.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured; the capture's producer and consumer are repository source.

No configured domain source could be checked.

### Repo-Internal References

The document's identifiers and walks are paired with the existing real-route producer and mounted consumer.

- The fixture names its exact selected family, subject and before walk. [1]
- The second collection holds the after-side walk. [2]
- The receipt row for this document in the MIK-L31 re-capture. [3]
- The producer follows published HTTP cursors under one fixed bound. [4]
- The consumer reads the complete captured bodies before mounting the actual read cycle. [5]

### Cross-Repo References

No external repository boundary is introduced.

No cross-repository reference is required.
