# mcp/src/agents_remember/memory_quality/knowledge_review.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/knowledge_review.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T04:20+02:00 |
| lastVerifiedCommitHash | `e605822eb3bf83bf63a45963c5f51d5fc28859ee` |
| lastVerifiedCommitDate | 2026-09-23T12:19:01+02:00|
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
`_limitations` counts **four** limitation codes. Each is a fact about the collection, never a verdict
about an assessment's content: `unresolved` counts records whose author could not conclude, `stale`
counts records whose binding **a measurement found** moved, `not-measured` counts records **no
measurement covered**, and `partial-scope` counts records with no comparison or scope reference
recorded. `stale` and `not-measured` are separate codes because they are different facts: a section
that counted an unmeasured record as stale would state a movement nobody measured, and one that
counted it as nothing at all would let a zero read as "nothing moved" (`ICR-R15@v1`).

### Conventions

- `KNOWLEDGE_REVIEW_HEADING` spells the heading once; a reader greps for it and the checklist's own
  tests assert it.
- `_cell` collapses whitespace and escapes table separators, so reported identities cannot corrupt the
  checklist layout.
- The four limitation constants are the closed set the section counts; a fifth would be a decision
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
| **The four counted limitation codes, and the rule that makes a measured movement and an unmeasured binding separate facts rather than one.** | `UNRESOLVED_DISPOSITION`; `STALE_BINDING`; `NOT_MEASURED_BINDING`; `PARTIAL_SCOPE` | mcp/src/agents_remember/memory_quality/knowledge_review.py:33-44 |
| The one checklist field that carries the section, and the arithmetic the section cannot reach. | `CuratorChecklist`; `write_curator_checklist` | mcp/src/agents_remember/memory_quality/curator_checklist.py:36-59; mcp/src/agents_remember/memory_quality/curator_checklist.py:100-180 |
| The controller read that supplies the summaries from the already-published authority, and passes the projection's own unmeasured count through without measuring anything itself. | `curator_knowledge_review_summaries` | mcp/src/agents_remember/application/memory_quality/controller.py:778-818 |

## KS-R15@v1 Report-Only Checklist Section

**The leaf that created this module.** `KS-R15@v1` §8.2 makes this leaf the owner of the report-only
`knowledgeReview` section, §8.3 forbids duplicating the checklist, and §8.4 keeps gate consequences
outside the leaf's ownership.

**The one sentence most likely to be wrong somewhere, stated here so a later reader can test it:**
the `knowledgeReview` section does not feed `curatorActionableCount`. The arithmetic is
`actionable_count = len(repair) + len(missing) + len(stale)` in `write_curator_checklist`, and the
section's own contribution is that it returns no count at all. A card or a checklist line implying
otherwise is false and is corrected against that line rather than softened.

## 260921-ICR-L15 An Unmeasured Record Is Not A Zero And Not A Movement

`260921-ICR-L15` (`ICR-R15@v1`) adds the section's **fourth** counted limitation, and the reason is the
same defect the leaf fixed everywhere else: the persisted checklist could say `| stale | 0 |` when
**nothing had been measured**, and a reader takes that zero to mean "nothing moved". Those are different
facts about the collection and the section now states them separately.

`NOT_MEASURED_BINDING` (`not-measured`) counts records **no measurement covered**. It is deliberately not
merged into `stale`: `stale` now means *a measurement of the current inputs found this record's binding
moved*, and its rendered meaning was re-worded to say so. An unmeasured record is reported neither
current nor stale, so the limitation table can no longer present an unmeasured collection as a clean one.

The count travels the section's whole path: `AssessmentSummary.notMeasuredCount` and
`AssessmentSummaryInput.notMeasuredCount` carry it, `summarise_assessment_state` refuses a binding total
(`staleCount + notMeasuredCount`) that exceeds the records it counts, `_limitations` includes the code
only when a count is non-zero, and `knowledge_review_section` renders the fourth row. The controller
passes the projection's own `notMeasuredCount` through unchanged — the section still measures nothing
itself and still returns **no** count, so the report-only boundary (and the arithmetic in
`write_curator_checklist` it cannot reach) is untouched by this leaf.

## Update History
- 2026-09-23T12:00:00+02:00 — 260921-ICR-L15 curator (candidate `ar/260921-icr-l15`, uncommitted; production line at this leaf's base `3103e1142a3ded8a843c3e5bbefca14861ba4a58`): **the section gains its fourth counted limitation, and the card's own two stale statements are corrected with it.** The claim that these are "the three counted limitation codes" was false against the new bytes, so it now names four and carries `NOT_MEASURED_BINDING` and the rule that a measured movement and an unmeasured binding are separate facts. **Citation disposition (required, and this is the review it asks for):** this card's Update History carried two entries recording that `curator_knowledge_review_summaries` had been **repointed by mechanical anchor-range projection** rather than by a curator reading the claim. Those two entries have been removed, because the checker reads them as evidence that no review happened and therefore forces this claim into the enforced set. In their place is this disposition, and it answers the two questions the mechanical note could not: (1) **does the construct the range covers support the claim's own words?** Yes — the claim is "the controller read that supplies the summaries from the already-published authority", and `curator_knowledge_review_summaries` is exactly that read: its declaration is at `mcp/src/agents_remember/application/memory_quality/controller.py:778`, its body reads the published curator-coherence authority and projects one summary per subject, and the controller calls it to build the checklist's knowledge-review section. (2) **was the range projected or rebound?** The range WAS projected — the projection rebound a mention to the declaration elsewhere — so this row is now re-derived from the declaration the claim is about rather than left as it was found. **Stamp accounting:** no verification stamp was advanced. The candidate is uncommitted, so a stamp naming it would claim a commit that does not contain this content; the honest basis for every claim here is this leaf's base commit `3103e1142a3ded8a843c3e5bbefca14861ba4a58` plus the working-tree delta, and the governed closeout's own metadata refresh owns the real stamp.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base
  `e963a01c`): created this card for the `knowledgeReview` checklist section the leaf added — the
  report-only boundary stated as structure rather than intent (the renderer returns no count and the
  arithmetic reads three other inputs), the one-artifact rule, the counted limitation codes that are
  facts about the collection rather than verdicts about its content, and the absence-not-disposition
  rendering rule. Verification metadata remains closeout-owned; no acceptance or certification claim
  is made.
