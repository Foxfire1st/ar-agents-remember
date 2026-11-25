# dashboard/src/cockpit/roleLaunchModel.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The pure model carries canonical role, document and request identity and the explicit mode. It validates advertised agent, model, effort and service-tier choices.

## Code Commentary

Entry option helpers follow server-ordered children and exact references for the seven roles' canonical reference needs; they do not rebuild topology from documents and series. `masterOptionsFor` answers a chosen sprint's masters, or the masters the served tree places outside every sprint when no sprint is chosen; `sprintRequiredForLaunch` requires a sprint only for the Orchestrator, while every master-naming role may start without one. Taskless metadata and exact scope comparators preserve active request identity. Role model applies on the role agent, effort on its role model, and service tier on its role agent even for a model override. Choice matching accepts host IDs or labels without case; there is no built-in fast-to-priority alias. Another agent uses native tier default. Model rows carry host-offered `features` with permission-bearing marks and agents carry `modes` and their advertised `defaultModeId`. Defaults carry `mode`, `featureValues` and per-choice sources. `RoleAgentOverride` can carry an explicit `modeId`. `roleAgentOverrideFor` retains that value independently of model, effort and feature values. Selection equality compares the mode and sorted feature entries.

## Invariants And Boundaries

Known unsupported catalog choices for agent, model, effort or service tier are surfaced. The launcher carries an explicit mode ID to the host, which owns applicability. Unknown catalog/model/effort/tier parts leave configured values unchecked for the host, including a tier when no model resolves; a successful empty offer remains a refusal. Discovery fields distinguish fresh, timestamped saved and unknown answers. Effort and tier inheritance remain independent; this code does not prove permanent native availability or create an actor.

## Current Contract

RoleDefaults has optional configured stepUp model/harness; RoleScopedExecution has optional reported stepUp model/source and can carry top-level observed mode. RoleLaunchSelection carries the requested reason string. These are distinct configured, observed and requested facts. Taskless restoration canonicalizes the saved role for matching but preserves its saved spelling, trims a string reason, retains it only when nonblank, and retains the agent override and original UUID/pending bit. Architect and Investigator keep existing storage slots, including Investigator's legacy system-specialist slot. Document/options scope remains independent of the reason. No model availability, count or permission authority is inferred from these types.


This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence



The current source and test assertions below establish the documented ownership; test citations do not claim a rerun in this pass.


- Current source owner or exact assertion described above. [1]



- Launch validation uses host agent, model, effort and tier catalog data. It leaves mode applicability to the host. [2]
- Override construction retains a named mode and removes an empty override that restates the role. [12]



- Service-tier validation matches known host offers without a fast alias; unknown models or tiers leave the configured tier unchecked. [3]



## MIK-R95 Bound Selection Helpers

`boundTasklessRequest` lets a bound Projects row adopt an existing saved open request (accepted, running, starting or unknown), marks it pending only when the execution is uncertain (`canRetry` or starting/unknown), and returns an already uncertain current request unchanged so its identity survives reconciliation; an adopted plain accepted/running request stays open, not pending. `masterOptionsFor` replaces `masterOptionsForSprint` and falls back to the masters the served tree places outside every sprint when no sprint is chosen; `taskOptionsForMaster` still follows the chosen master. The document chat and launcher use `sprintOptionsForEntries`, `masterOptionsFor`, `taskOptionsForMaster` and exact reference equality to admit only roles allowed by the served entry hierarchy.

## Investigator scope and request identity

usesRequestReceipts separates per-request execution cardinality from isTasklessRole altitude. Investigator uses exact request identity at Projects and selected sprint/master scopes. Task-bound storage includes canonical selection scope; the earlier Projects system-specialist storage key remains unchanged for original saved retries. Restoring a selected UUID does not choose a newer sibling or manufacture a new request.




- The launcher model keys selected Investigator executions by request and preserves the original Projects storage slot. [4]




- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [5]


- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [6]




- The backend checks the explicit reason and the configured failed-review threshold. A step-up reads mode from its own settings row. Other launch fields follow the same-harness and model inheritance rule. [8]


- Saved taskless UUID/pending plus trimmed reason/override restoration keeps the legacy Investigator storage slot. [9]


- The same start-only reason enters saved retry payload and POST body. [10]

- The launcher model carries the requested step-up reason, an explicit mode override, and optional receipt choice metadata with a distinct observed-mode field. [11]

- Completed typed rounds supply the worker and curator counts. Incomplete history is reported, and a record-only correction revises its existing round. [7]
