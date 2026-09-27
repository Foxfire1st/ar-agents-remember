# dashboard/src/panels/review/familyPaging.captured.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/panels/review/familyPaging.captured.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-27T01:04:07+00:00 |
| lastVerifiedCommitHash | `a5bec6c3b3b413cd3066d0e8d302b4854d1b513a`|
| lastVerifiedCommitDate | 2026-09-27T03:38:17+02:00|
| governingOverview | `dashboard/src/panels/overview.md` |

## Governing Overview

[panels route overview](../overview.md)

## Purpose

Retain complete real HTTP review responses for a bounded two-sided family walk, so mounted client regressions consume the production wire shape.

## Code Commentary

### Logic

The document identifies one selected subject and family, then stores three before-walk and three after-walk bodies. They were captured through the public-authored family scenario and real HTTP continuation helper at page size four. Content, memberships and claims can appear on different pages; another side's response can repeat its first page. Those are the cases the read-cycle test must preserve.

### Conventions

Regenerate through the existing scenario and HTTP walk helper when the wire contract changes. Do not hand-edit successful response bodies to manufacture an expected display. Deliberate negative mutations belong in the consuming test and are explicitly asserted as failures.

### Invariants And Boundaries

These are regression fixture records, not the project's published knowledge database, a new selection authority or installed-browser evidence. The complete response keeps comparison, subject, family, source and evidence dimensions available to the real client.

### Todos

None recorded.

## Docs References

No Domain Documentation source is configured; the capture's producer and consumer are repository source.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain source could be checked. | — | — |

## Repo-Internal References

The document's identifiers and walks are paired with the existing real-route producer and mounted consumer.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture names its exact selected family, subject and before walk. | "family_id"; "subject_id"; "before" | dashboard/src/panels/review/familyPaging.captured.json:1-5 |
| The second collection holds the after-side walk. | "after" | dashboard/src/panels/review/familyPaging.captured.json:3183-3184 |
| The producer follows published HTTP cursors under one fixed bound. | `walk_responses` | mcp/tests/test_review_family_context_population.py:376-398 |
| The consumer reads the complete captured bodies before mounting the actual read cycle. | "familyPaging.captured.json" | dashboard/src/panels/review/ReviewReadCycle.family.test.tsx:12-30 |

## Cross-Repo References

No external repository boundary is introduced.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repository reference is required. | — | — |

## Update History

- 2026-09-27T01:04:07+00:00 — Created the fixture card with public-authoring/HTTP provenance and its bounded regression purpose. It confers no live-knowledge or product-acceptance authority; verification hash/date remain blank until real closeout.

