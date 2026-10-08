# mcp/src/agents_remember/mcp/tools/knowledge.py

## Governing Overview

[mcp/tools route overview](overview.md)

## Purpose

Payload builders for three mounted knowledge operations over converted trees.

## Code Commentary

### Logic

Read selects the tree's derived index and delegates through bounded paging, carrying tree/index state, currentness and applicable proofs. Named source roots with no commit refuse; resolution is complete or absent. [1]

Diff compares knowledge/onboarding Git files, or privately captures working memory when afterRevision is absent. It groups records/entries and cards/sidecars, bounds patches and names every omitted/cut portion; no effect label is inferred. [2]

Integrity runs the knowledge validator and returns the latest leaf worklist for a contract, not a canonical detection run or compatibility verdict. Legacy roots and database files refuse before an open; change/project and selected-run fields are removed. [3] [51] [56]

### Invariants And Boundaries

- A partial index is never complete.
- Unheld selectors refuse rather than implying no change.
- Each public payload uses the shared response-model choke point.

## Evidence

### Repo-Internal References


- Read paging/source resolution. [1]


- Bounded Git knowledge diff. [2]


- Validator/worklist integrity answer. [3]


- Only admitted views carry proofs. [4]


- Current validator/worklist response, without selected-run identities. [51]


- Legacy selections open no database; partial read stays incomplete. [56]


### Cross-Repo References

No cross-repository contract is established by this file.
