# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_operation_location.py

## Governing Overview

[Lifecycle operation integration overview](overview.md)

## Purpose

Owns the canonical locator-to-enclosure-manifest-to-lifecycle-journal address chain, including the manifest entry that records an enclosure generation's outside scratch root and the creation of that root after publication.

## Code Commentary

### Logic

It reserves and publishes new/successor/legacy enclosure locations, resolves and inspects locators, validates contract bindings, publishes terminal locations, recovers interrupted publication, carries the contract's recorded outside scratch root into the manifest, and creates that root once the contract text is durable.

### Conventions

Typed records and refusal payloads remain owned at the narrowest stable boundary. Callers consume
the public function or model instead of re-deriving its lower-level state machine.

### Invariants And Boundaries

- The independent locator is the stable address; manifest and journal identity must match exact repository/task/generation/digests; no directory scan or task-file fallback is permitted.
- Missing, unreadable, ambiguous, or conflicting authority fails loudly; this file does not add a
  fallback or compatibility shadow.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.


### Repo-Internal References

The source file is the direct evidence for this unit; its governing overview records adjacent owners.


### Cross-Repo References

No cross-repository source is allowed by the resolved settings, and this unit owns no external
protocol claim.

- No external domain source is required to establish this repository-owned implementation. [1]
- The module's concrete API, control flow, and validation boundary are implemented here. [2]
- No meaningful cross-repository reference applies. [3]

## 260928-MIK-L198 — Manifest records the root, directory follows the contract

`prepare_enclosure_publication` now takes the generation's outside scratch root from `outside_scratch.recorded_root(contract)` and writes it into `LifecycleEnclosureManifest.outsideScratch`, so the record sits inside the manifest text whose digest the locator pins. It never computes an identity of its own: `_outside_scratch_record` only reads the record the contract already carries. The directory is a separate step, and it comes after the contract text: `_materialise_outside_scratch` calls `outside_scratch.ensure_root` after `_publish_successor_contract` in `reserve_new_lifecycle_operation_location`, and after `_publish_or_prove_contract` and `_prove_contract` in `publish_enclosure_location`. A crash between the two therefore leaves a recorded generation with no directory, which the next publication of that generation recreates from the record; `resume_new_lifecycle_operation_location` reaches the same step through `publish_enclosure_location`. An enclosure that records no root makes the record `None` and every added step returns without touching the disk. A materialisation failure is raised as the `operation-location-outside-scratch-unavailable` location error, with the root and the reason in `observed`.
