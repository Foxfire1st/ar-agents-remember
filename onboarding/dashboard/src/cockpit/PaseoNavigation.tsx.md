# dashboard/src/cockpit/PaseoNavigation.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

The component displays canonical external chat groups and native actor cues without rewriting launcher selection.

## Code Commentary

Canonical/opaque keys identify groups and rows; every trusted selected actor gets aria-current and click returns that catalog actor. Harness cues come from provider text. Activity precedence is Closed, unavailable, Error, Needs input, Busy/Starting, attention, then Idle. Busy/Starting rotate through the shared keyframe with static reduced-motion glyphs.

## Invariants And Boundaries

Qualification badge requires its exact fixture label. Native idle/reply-ready is no task verdict; glyph rendering does not claim SVG-provider support.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `activity` | `dashboard/src/cockpit/PaseoNavigation.tsx:79-96` |
| Current source owner or exact assertion described above. | `AgentIdentity` | `dashboard/src/cockpit/PaseoNavigation.tsx:98-129` |
| Current source owner or exact assertion described above. | `PaseoNavigation` | `dashboard/src/cockpit/PaseoNavigation.tsx:131-197` |
| Conflicting legacy native membership and duplicate display titles leave canonical sprint/master/leaf groups distinct, with Projects first. | `keeps Projects first and separates duplicate titles by canonical sprint/master/task despite legacy memberships` | `dashboard/src/cockpit/paseoNavigationModel.test.ts:70-100` |
| Subscribed native metadata updates and attention clearing propagate provider, status, permission count, attention and availability through the hierarchy message. | `includes every SDK page, canonical labels and actual host membership, then applies live metadata changes` | `dashboard/src/cockpit/paseoHierarchy.test.ts:93-123` |
