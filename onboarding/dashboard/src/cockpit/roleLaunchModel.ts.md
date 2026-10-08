# dashboard/src/cockpit/roleLaunchModel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The pure model carries canonical role/document/request identity and validates advertised agent/model/effort/tier selection.

## Code Commentary

Topology helpers enforce the seven roles' canonical reference needs. Taskless metadata and exact scope comparators preserve active request identity. Role model applies on the role agent, effort on its role model, and service tier on its role agent even for a model override. Fast maps to priority; another agent uses native tier default.

## Invariants And Boundaries

Unavailable values are surfaced rather than substituted. Effort and tier inheritance remain independent; this code does not prove permanent native availability or create an actor.

## Evidence

The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Current source owner or exact assertion described above. [1]
- Current source owner or exact assertion described above. [2]
- Current source owner or exact assertion described above. [3]

## MIK-R95 Bound Selection Helpers

`boundTasklessRequest` lets a bound Projects row adopt an existing saved open request (accepted, running, starting or unknown), marks it pending only when the execution is uncertain (`canRetry` or starting/unknown), and returns an already uncertain current request unchanged so its identity survives reconciliation; an adopted plain accepted/running request stays open, not pending. The document chat reuses this model's topology helpers (`sprintOptionsForDocs`, `masterOptionsForSprint`, `taskOptionsForMaster`, `sameTaskDocumentRef`) to admit exactly the roles a selection can start.

## Investigator scope and request identity

usesRequestReceipts separates per-request execution cardinality from isTasklessRole altitude. Investigator uses exact request identity at Projects and selected sprint/master scopes. Task-bound storage includes canonical selection scope; the earlier Projects system-specialist storage key remains unchanged for original saved retries. Restoring a selected UUID does not choose a newer sibling or manufacture a new request.


- The current source implements this file’s stated Investigator boundary. [4]
