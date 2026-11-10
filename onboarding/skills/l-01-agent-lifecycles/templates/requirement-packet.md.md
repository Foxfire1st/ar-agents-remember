# skills/l-01-agent-lifecycles/templates/requirement-packet.md

## Governing Overview

[overview](../overview.md)

## Purpose

The scaffold requirement authors use for one version-addressed canonical requirement packet.

## Code Commentary

Before authoring, the author reads the task prose-field rules in `reference/tasks/document-authoring.md`; before seeking approval, `operations/planning.md#prepare-requirements-and-recover-approval`. The packet title is `<stable identifier> @ <version> — <observable outcome>` with a field table (stable ID, version, state at packet freeze, developer approval citation, supersedes). Sections are Normative Requirement (an independently falsifiable promise), Problem, Required Behavior, Rationale, Scope, Preservation Boundaries, Forbidden Overreach, Failure And Recovery Behavior, Planned Structure (placement and skeleton before code is written), Examples (conforming, violating and boundary cases), Expected Evidence, Authority And Provenance, Dependencies, Open Truth Gaps and Revision History.

## Evidence

- Authors read the prose-field rules before authoring and the planning operation before seeking approval. [1]
- The packet header records stable ID, version, freeze state, approval and supersession. [2]
- The normative requirement is an independently falsifiable promise. [3]
- Planned Structure gives placement and skeleton before code; Examples give conforming, violating and boundary cases. [4]
- The Architect reads this template before writing a requirement packet. [5]
