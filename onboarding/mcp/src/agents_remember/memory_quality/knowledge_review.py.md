# mcp/src/agents_remember/memory_quality/knowledge_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T04:20+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l15` uncommitted source; base `e963a01c6804570d597e451eaa069eaba66bd3ec` |
| governingOverview | `overview.md` |

## Governing Overview

[memory quality overview](overview.md)

## Purpose

**The factual `knowledgeReview` section of the curator's one checklist artifact.** The section reports
what the curator-coherence authority holds: the comparison and scope references an assessment
recorded, and the counted limitations of the collection.

**The section is report-only, and that is structural rather than promised.**
`knowledge_review_section` returns lines and limitations and returns **no count**; it cannot reach
`write_curator_checklist`'s `curatorActionableCount`, whose arithmetic is `len(repair) + len(missing)
len(stale)` — repairable findings, missing onboarding and stale route indexes, and nothing else. An
unresolved family signal therefore raises no gate and adds no finding per detector match. The section
also renders into the **same** `curator-memory-quality.md` file the shipped renderer already
atomically replaces: there is no second checklist, no second attestation and no parallel count.

## Code Commentary

### Logic

`AssessmentSummary` is one subject's stored assessment history as the checklist reports it, and every
field is a count or an identity. There is deliberately **no `verdict` field**: a summary carrying one
would be the checklist inventing a conclusion the curator authored.

`knowledge_review_section` renders the section for the summaries the caller passes in. It reports
recorded assessments, reviewed subjects and counted limitations; when the collection is empty it
renders an explicit *no rows* statement rather than a favourable default, reusing the shipped
renderer's own `None.` spelling for an empty section. A subject with no assessment is **not** rendered
as a disposition — it is simply not a knowledge-review link, and the section says how many assessments
exist rather than how many subjects were cleared.

`summarise_assessment_state` builds one summary from an `AssessmentSummaryInput`, and
`_limitations` counts the three limitation codes. Each is a fact about the collection, never a verdict
about an assessment's content: `unresolved` counts records whose author could not conclude, `stale`
counts records whose binding moved, and `partial-scope` counts records with no comparison or scope
reference recorded.

### Conventions

- `KNOWLEDGE_REVIEW_HEADING` spells the heading once; a reader greps for it and the checklist's own
  tests assert it.
- `_cell` collapses whitespace and escapes table separators, so reported identities cannot corrupt the
  checklist layout.
- The three limitation constants are the closed set the section counts; a fourth would be a decision
  rather than a formatting change.

### Invariants And Boundaries

- **Report-only, structurally.** No input of this module reaches `curatorActionableCount`; the
  arithmetic lives in `write_curator_checklist` and reads only repairable findings, missing onboarding
  and stale route indexes.
- **One artifact.** The section is rendered into the existing checklist artifact; duplicating the
  checklist is what the design forbids.
- **Facts, not verdicts.** Every reported number is a count of records that exist. No field here
  carries a conclusion, and nothing here reads a disposition to decide an outcome.
- **Gate consequences are not this module's.** Raising a finding per unresolved signal is an explicit
  design/authority decision owned by a later requirement, not by this section.
- **The authority is read, not decided.** The summaries come from the already-published
  curator-coherence authority through the controller's own read; this module neither reads nor writes
  that authority.

## Docs References

| Finding | Anchor | Source |
| --- | --- | --- |
| The report-only boundary as recorded in the module's own contract: the rendered section states it in one sentence inside the artifact. | "Report-only. This section records what the curator-coherence authority holds; it adds no " | mcp/src/agents_remember/memory_quality/knowledge_review.py:82-82 |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The section renderer, its empty-collection spelling, and the counts it reports. | `knowledge_review_section` | mcp/src/agents_remember/memory_quality/knowledge_review.py:70-135 |
| The summary shape, which carries counts and identities and deliberately no verdict. | `AssessmentSummary` | mcp/src/agents_remember/memory_quality/knowledge_review.py:42-57 |
| The three counted limitation codes. | `UNRESOLVED_DISPOSITION`; `STALE_BINDING`; `PARTIAL_SCOPE` | mcp/src/agents_remember/memory_quality/knowledge_review.py:37-41 |
| The one checklist field that carries the section, and the arithmetic the section cannot reach. | `CuratorChecklist`; `write_curator_checklist` | mcp/src/agents_remember/memory_quality/curator_checklist.py:36-59; mcp/src/agents_remember/memory_quality/curator_checklist.py:100-180 |
| The controller read that supplies the summaries from the already-published authority. | `curator_knowledge_review_summaries` | mcp/src/agents_remember/application/memory_quality/controller.py:778-817 |

## KS-R15@v1 Report-Only Checklist Section

**The leaf that created this module.** `KS-R15@v1` §8.2 makes this leaf the owner of the report-only
`knowledgeReview` section, §8.3 forbids duplicating the checklist, and §8.4 keeps gate consequences
outside the leaf's ownership.

**The one sentence most likely to be wrong somewhere, stated here so a later reader can test it:**
the `knowledgeReview` section does not feed `curatorActionableCount`. The arithmetic is
`actionable_count = len(repair) + len(missing) + len(stale)` in `write_curator_checklist`, and the
section's own contribution is that it returns no count at all. A card or a checklist line implying
otherwise is false and is corrected against that line rather than softened.

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `curator_knowledge_review_summaries` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:778-817. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `curator_knowledge_review_summaries` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:707-746. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the `knowledgeReview` checklist section the leaf added — the
  report-only boundary stated as structure rather than intent (the renderer returns no count and the
  arithmetic reads three other inputs), the one-artifact rule, the counted limitation codes that are
  facts about the collection rather than verdicts about its content, and the absence-not-disposition
  rendering rule. Verification metadata remains closeout-owned; no acceptance or certification claim
  is made.
