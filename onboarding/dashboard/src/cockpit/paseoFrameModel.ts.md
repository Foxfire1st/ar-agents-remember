# dashboard/src/cockpit/paseoFrameModel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The pure model validates configured frame descriptors, native execution targets and normalized plugin messages.

## Code Commentary

Available descriptors require an http(s) serving origin and server ID. Only paseo-agent host fields supply actor targets, and rejected receipts supply none. Web URLs encode identities. Source-tagged messages enforce typed catalog/activity fields, unique actor IDs, plural selection and complete source-scoped Parent errors.

## Invariants And Boundaries

Native web route spellings are version-sensitive. Parsing cannot establish channel origin/window trust or task acceptance.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

| Finding | Anchor | Source at frozen tree |
| --- | --- | --- |
| Current source owner or exact assertion described above. | `paseoAgentTarget` | `dashboard/src/cockpit/paseoFrameModel.ts:97-127` |
| Current source owner or exact assertion described above. | `agentActivity` | `dashboard/src/cockpit/paseoFrameModel.ts:189-199` |
| Current source owner or exact assertion described above. | `parsePluginMessage` | `dashboard/src/cockpit/paseoFrameModel.ts:233-263` |
| Subscribed native metadata updates and attention clearing propagate provider, status, permission count, attention and availability through the hierarchy message. | `includes every SDK page, canonical labels and actual host membership, then applies live metadata changes` | `dashboard/src/cockpit/paseoHierarchy.test.ts:93-123` |
