# dashboard/src/panels/review/MeaningEffects.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Display the selected record's owner-supplied successive meaning-effect judgments, their reasons and label explanations without inferring a net effect.

## Code Commentary

`meaningBadgeText` preserves the label sequence, abbreviating more than three labels to first/ellipsis/last; MeaningBadge appears only for a steps answer and shrinks with ellipsis inside the one-line row. `meaningFor` joins by the exact record identity.

`RecordedStepsBlock` keeps all steps in supplied order, including attempt, own revision or its unrecorded label, effect, row identifier, authored reason and history-open/closed state. A legacy family step lacking its effect or own revision names the missing value; a missing effect also retains the fixed pre-required-label sentence. Multiple steps are labelled successive judgments. Row/history identifiers have their own disclosure; steps and reasons stay visible. A non-steps answer distinguishes none from the supplied unavailable detail. The native explanation button exposes all effect-label explanations.

A missing meaning_effects field renders failure, including unselected/source-only and unidentified-member branches through MeaningFieldGuard. A present empty field is valid, and a present field that does not cover the requested record renders nothing. The renderer changes no history row, disposition or effect.

## Evidence

- MeaningEffects.tsx current behavior at this source owner. [10]
- MeaningEffects.tsx current behavior at this source owner. [11]
- MeaningEffects.tsx current behavior at this source owner. [12]
- MeaningEffects.tsx current behavior at this source owner. [13]
- MeaningEffects.tsx current behavior at this source owner. [14]
- MeaningEffects.tsx current behavior at this source owner. [15]
