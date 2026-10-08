# mcp/src/agents_remember/models/knowledge/__init__.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

The explicit shared facade for the retained index-reader vocabulary. It re-exports immutable values and pure digest/read helpers without SQL, Git resolution, write admission or authorization decisions.

## Code Commentary

### Logic

The imports retain authorship and origin states, schema identity, canonical invariant/family payload mappings and digest functions, family/member/invariant values, repository identity, KnowledgeOperation/KnowledgeRefusal/KnowledgeRefusalCode, selective-read seed/context/page/cursor values and source locators.

__all__ is an explicit sorted export list. A consumer may name these shared reader values from the facade; underlying contracts and validators remain owned by their defining modules. Private shared acceptance validation remains in base.py rather than exported here.

### Invariants And Boundaries

- Vocabulary flows to readers and application owners; this facade imports no memory.knowledge storage implementation.
- Export membership is a public vocabulary contract, not proof of reachable mutation or admission authority.
- This module creates no record, snapshot, acceptance or Git state.

### Historical boundary — MIK-R26

Canonical database anchor/realization records, write requests/results, seal-writing helpers, snapshot publication/candidate disposal and composition commands were removed from the facade with their production writer route. require_stored_outcome and require_removal_outcome were retired, not retained hidden helpers. The current export list is the boundary; fixture definitions are not substitute production exports.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The rows below cite the submodules this facade re-exports and the two consumers of the vocabulary.


- The explicit current facade imports and exports retained reader values. [1]


- The current export list contains no retired mutation outcome helpers; the acceptance helper remains at its own base owner. [3]


- The served surface is the retained index-reader vocabulary. [4]


- Retired mutation outcome helpers are absent from the current facade; internal acceptance validation stays in base.py. [6]


- The production store consumes these retained values through read-only operations. [7]


### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
