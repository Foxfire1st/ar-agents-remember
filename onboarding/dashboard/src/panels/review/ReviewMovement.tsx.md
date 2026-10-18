# dashboard/src/panels/review/ReviewMovement.tsx

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

Present synchronization and external Git movement together without measuring either channel or hiding their reasons in comparison metadata.

## Code Commentary

`movementState` uses the selected subject's read status, not the movement object's normality. Pending reads say `being read` for both owners and failed reads say `unavailable`; after an answer, each supplied owner contributes its `binding_state`, with `not-measured` for a missing owner. `ReviewMovementStatus` draws the compact joint line and marks its actual root as `data-review-content="movement-state"`.

`ReviewMovementFacts` renders nothing while that subject has no answer or when both owner objects are absent. Otherwise it serializes the **complete supplied objects**, including statements, absence reasons, recovery actions and owner-specific fields, under a wrapping `pre` marked `data-review-content="movement-facts"`. An answered subject may still have an unavailable measurement. The actual `ReviewScopeHeader` mount is an open sibling of the state line, outside `ScopeMetadata`; only comparison identities/read provenance remain in that separate closed container. Normal movement objects also contain statements, so normality is not a license to close or duplicate this complete dump.

## Invariants And Boundaries

- Never show a previous subject's movement facts as the next unanswered subject's result. The parent passes the same read status to both renderers.
- Missing owners do not acquire fabricated reasons or measurements. Full supplied facts are retained rather than reduced to the open state words.
- Required semantic roots stay marked and outside default-closed disclosures, including repeated renderings. The old closed placement is superseded, not an exception.
- This is source/wiring documentation, not fresh runtime, native classifier, browser geometry, timing or MEMORY acceptance.

## Evidence

- The subject-read guard replaces both movement labels while pending or unavailable; answered missing owners fall back to not-measured. It does not measure or classify movement. [1]
- The compact sync/external state line is a marked semantic root, not an identity or a movement-reason display. [2]
- The marked facts root preserves complete supplied owner objects as wrapped JSON only for an answered read with at least one owner; it is not a filtered technical-metadata projection. [3]
- The actual header mounts status and a single complete facts block openly before FamilyScope and outside ScopeMetadata; comparison identity provenance remains separate. [4]
