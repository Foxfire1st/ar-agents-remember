# dashboard/src/panels/review/ReviewRecordPanes.tsx

## Governing Overview

[review route overview](overview.md)

## Purpose

Render the selected answer's non-authored changed-field facts, remaining counts and submission boundary, and supply its compact record identities to Technical details.

## Code Commentary

`RecordFacts` removes authored statement/applicability/conditions/exclusions/guarantee fields from the generic transition list. Other fields use explicit absent versus recorded-empty labels and readable token words. Only knowledge.unresolved and source.unresolved feed the visible unresolved-reference list; recorded references remain reason content.

`ReviewMainFacts` uses the held lane attribution facts for recognized source.remaining populations, with explicit unknown when no lane read exists and the supplied value/reason wording for other counts. Non-current staleness stays visible. The submission state is labelled read-only with the supplied reason and next action. This block contains no All changes action.

`ReviewRecordIdentities` supplies comparison reference/policy, retained revision groups, expansion reference/command, judgment row/history identifiers, proof identifiers and admitted disposition names. Empty judgment/proof lists and a missing judgment pane are labelled distinctly. Those identities do not manufacture a judgment outcome, and the dispositions are explicitly not publication approval. The parent TechnicalDetails owns disclosure placement and pending/unavailable guards.

## Evidence

- ReviewRecordPanes.tsx current behavior at this source owner. [19]
- ReviewRecordPanes.tsx current behavior at this source owner. [20]
- ReviewRecordPanes.tsx current behavior at this source owner. [21]
