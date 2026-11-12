# dashboard/src/panels/review/FamilyReviewCenter.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Compose the selected family's or invariant's own statement/guarantee, recorded meaning steps, judgment and supplied resolution context in the reading column.

## Code Commentary

`FamilyReviewCenter` supplies the wording-diff scope and resolves the chosen family/revision only within this payload's family context. An addressed invariant gets its own member content even without a family entry; a family selection gets its own guarantee content. A member whose canonical invariant identity is missing gets an explicit unavailable-member context with continuation, without borrowing a judgment. A missing family selection uses the unselected/source-only branch and its required-meaning-field guard.

`CenterParts` places the primary content under the subject heading and the remaining context after the subject's code, or renders both when no code section follows. Family content orders guarantee word diff, own recorded steps and own family judgment. Invariant content orders its selected statement, own recorded steps and own subject judgment; a followed marker's unknown membership remains its own visible line. Prose keeps a reading measure unless the wording owner uses side-by-side layout.

Family details retain guarantee change facts, member-population breakdown, every loaded distinct member revision, paired carried statements and explicit roster counts/continuations. Completeness requires every applicable side to be recorded with a complete page, the recorded membership total present, and recorded member content. Distinct revision counts, cumulative read-item counts and measured membership rows remain separate. Under ReadingContext the member list follows the shared change-set model's family-member order; the outline/semantic ordering path supplies its initial order and remains the fallback outside that page context.

Family realization details describe only loaded claims. `familyExpressionExcerpts` supplies the deduplicated address/recorded-byte excerpts, with all membership occurrences, roles and per-side resolutions retained. Missing or unreturned claims are not called unchanged. Listed measured paths open the comparison page; an unlisted path stays plain text, with partial inventory distinguished from measured absence.

Member details keep the optional family guarantee, shared-membership references, the selected member's own change facts, realization claims and attributed paths, followed by selected-record worklist knowledge and roster continuation. `IndependentFacts` matches the selected subject's revision selection and retained revisions for statement/membership/source facts; it explicitly separates those facts from authored judgment. `subjectRows` keeps before and after member rows separate for SelectedStatement. SubjectKnowledge receives only the matching addressed subject and supplied leaf-wide tree read. Source blocks themselves belong to the page's shared card model.

## Evidence

- FamilyReviewCenter.tsx current behavior at this source owner. [41]
- FamilyReviewCenter.tsx current behavior at this source owner. [42]
- FamilyReviewCenter.tsx current behavior at this source owner. [43]
- FamilyReviewCenter.tsx current behavior at this source owner. [44]
- FamilyReviewCenter.tsx current behavior at this source owner. [45]
