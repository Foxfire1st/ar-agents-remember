# dashboard/src/panels/review/FamilyGuarantees.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Render the selected family's supplied before/after guarantee comparison, keeping authored text and each side's recorded state distinct from its identifiers.

## Code Commentary

`GuaranteeComparisonBlock` first uses the tree-comparison word-diff owner when it supplies a text change. Otherwise `guaranteeComparison` chooses unrecorded, one-sided, unchanged-revision, identical-text or changed-text rendering. Unrecorded names the composition's reason. One-sided keeps the available guarantee and explicitly names the missing other revision; identical text appears once with compact revision labels.

`GuaranteeBlock` leaves the joint guarantee and state at origin visible; family/revision/version/acceptance references are in its identifiers disclosure. A changed non-word-diff guarantee uses the existing DiffPane with caller layout, collapse off and `fit`, so its content contributes its full height to the reading column. This component displays the delivered comparison and authors no guarantee or judgment.

## Evidence

- FamilyGuarantees.tsx current behavior at this source owner. [4]
- FamilyGuarantees.tsx current behavior at this source owner. [5]
