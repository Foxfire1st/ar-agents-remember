# dashboard/src/cockpit/roleLaunchModel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The pure model carries canonical role/document/request identity and validates advertised agent/model/effort/mode/feature selection.

## Code Commentary

Entry option helpers follow server-ordered children and exact references for the seven roles' canonical reference needs; they do not rebuild topology from documents and series. Taskless metadata and exact scope comparators preserve active request identity. Role model applies on the role agent, effort on its role model, and service tier on its role agent even for a model override. Fast maps to priority; another agent uses native tier default. Model rows carry host-offered `features` with permission-bearing marks and agents carry `modes`; defaults carry `mode`, `featureValues` and per-choice sources. `agentId` is optional so defaults can stand without an explicit selection, `roleAgentOverrideFor` preserves explicit speed values through model and effort changes, and selection equality compares sorted feature entries.

## Invariants And Boundaries

Unavailable values are surfaced rather than substituted. Effort and tier inheritance remain independent; this code does not prove permanent native availability or create an actor.

## Current Contract

RoleDefaults has optional configured stepUp model/harness; RoleScopedExecution has optional reported stepUp model/source; RoleLaunchSelection carries the requested reason string. These are distinct configured, observed and requested facts. Taskless restoration canonicalizes the saved role for matching but preserves its saved spelling, trims a string reason, retains it only when nonblank, and retains the agent override and original UUID/pending bit. Architect and Investigator keep existing storage slots, including Investigator's legacy system-specialist slot. Document/options scope remains independent of the reason. No model availability, count or permission authority is inferred from these types.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence



The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.

- Current source owner or exact assertion described above. [1]
- Current source owner or exact assertion described above. [2]
- Current source owner or exact assertion described above. [3]

## MIK-R95 Bound Selection Helpers

`boundTasklessRequest` lets a bound Projects row adopt an existing saved open request (accepted, running, starting or unknown), marks it pending only when the execution is uncertain (`canRetry` or starting/unknown), and returns an already uncertain current request unchanged so its identity survives reconciliation; an adopted plain accepted/running request stays open, not pending. The document chat and launcher use `sprintOptionsForEntries`, `masterOptionsForSprint`, `taskOptionsForMaster` and exact reference equality to admit only roles allowed by the served entry hierarchy.

## Investigator scope and request identity

usesRequestReceipts separates per-request execution cardinality from isTasklessRole altitude. Investigator uses exact request identity at Projects and selected sprint/master scopes. Task-bound storage includes canonical selection scope; the earlier Projects system-specialist storage key remains unchanged for original saved retries. Restoring a selected UUID does not choose a newer sibling or manufacture a new request.


- The current source implements this file’s stated Investigator boundary. [4]

- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [5]

- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [6]

- Worker/Curator typed review census, record-only exclusion and unknown history. [7]

- Reason admission, threshold and differing-harness/model inheritance boundary. [8]

- Saved taskless UUID/pending plus trimmed reason/override restoration keeps the legacy Investigator storage slot. [9]

- The same start-only reason enters saved retry payload and POST body. [10]

- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [11]
