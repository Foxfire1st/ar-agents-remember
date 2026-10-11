# dashboard/src/panels/review/MeaningEffects.tsx

## Governing Overview

[Owning route](../overview.md)

## Purpose

Render backend-recorded meaning judgments as a compact tree badge and an always-visible reading-area block, with keyboard-operable vocabulary explanations.

## Code Commentary

The badge joins step labels in attempt order; more than three use first, ellipsis and last. It shrinks within the one-line navigation rail rather than widening the page. The reading block retains every step, its attempt and own revision, reason, closed/open status and row identifier; a disclosure may hold the full row/history path, never the Recorded steps block itself. Legacy family omissions render both unrecorded labels and the fixed historical sentence.

The explanations toggle is a native button. No label or overall effect is computed from record text. Missing meaning_effects is a current-response failure on selected and unselected/source-only branches; a present empty collection is valid. An uncovered record renders nothing, rather than retaining a previous subject’s steps.

## Evidence

- Badge text preserves the sequence while abbreviating long step lists. [1]
- The complete step block distinguishes recorded steps, readable absence and unavailable reasons. [2]
- Unselected branches reject a missing required field without rejecting an empty one. [3]
