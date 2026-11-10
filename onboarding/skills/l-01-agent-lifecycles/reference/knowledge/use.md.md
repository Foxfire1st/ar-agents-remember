# skills/l-01-agent-lifecycles/reference/knowledge/use.md

## Governing Overview

[overview](../../overview.md)

## Purpose

Explains how all eight roles combine attributed repository knowledge with direct code inspection at their working step, with additional sections for the Architect, Investigator, Worker and Reviewer.

## Code Commentary

A read starts from text search or `knowledge_read` (which needs a seed, file path or identifier) and uses both knowledge and code: attributions find what search misses, code reads fill stale or missing memory, and stale memory may orient only when labelled stale and checked against code. Reads bind `memoryRoot`, `repositoryRoot` and the exact inspected `codeTreeId` from the handover, or the selected repository's resolved pair for a taskless investigation. Callers page `source_context` through `continuation` until enumeration is complete, then open the named record files, sibling realizations, proofs, code and tests themselves; governing families named with `role="chain"` are expanded with `familyRevisionId`. A recorded proof describes what a test demonstrates, not a fresh passing run; refusals, partial indexes and unverified currentness are reported as gaps, and unresolved-anchor and currentness counts prove neither coverage nor correctness. A setting fact is read from its authority (`server_info`, resolved memory settings, user settings), never inferred from a compact packet's omitted fields.

The Architect uses attribution with code reads to diagnose before proposing a repair; the Investigator separates recorded claims, observations and hypotheses; the Worker reads attributed records before editing and the recorded `proves` links when a test fails, and does not change a sibling outside its scope; the Reviewer uses attribution to check every changed file and compares backing proofs with runs on the exact candidate. Attribution adds a review dimension and filters nothing. The Reviewer role links its section when inspecting changes.

## Evidence

- Knowledge and code reads are used together, and stale memory is labelled. [1]
- Reads bind the selected memory and code pair, page to completion and open named records, siblings, proofs and code. [2]
- Recorded proofs are not passing runs, and gaps and counts are reported without claiming completeness. [3]
- Setting facts come from their owning source. [4]
- Role sections apply attribution to diagnosis, investigation, editing, failing tests and review without filtering the diff. [5]
- The Reviewer role links the Reviewer section when inspecting changes. [6]
