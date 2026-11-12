# mcp/src/agents_remember/application/task_docs/task_review_step_up.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Post-publication step-up advice for successful review recordings; it decorates the answer without changing persisted review state.

## Current Contract

with_review_step_up is active only for ok task_doc.record_review/record_route_review answers with remaining findings. reviewKind chooses the state/role: code Worker or memory Curator. It reads current settings and the typed failed-try census, names unavailable history instead of guessing, and at a configured afterTries threshold says the seat's starter calls role_start anew. It opens/grants no round and starts no actor. A settings AgenticSettingsError or OSError after publication appends a warning and an explicit do-not-repeat-recording recovery nextAction while preserving success and state. Clean/pass answers return before the settings read; other operations return unchanged.

## Invariants And Boundaries

This is candidate-source onboarding, not execution, CODE/MEMORY acceptance, serving-build currentness or permission to publish. The owning caller retains transaction, host and role authority.


The governing workflow opens an independent memory review after CODE PASS on the same task using begin_review/record_review with reviewKind=memory. It has its own immutable baseline and shrinking IDs, under the same settings limit and extra-round approval rule, and never resets code reviewState. The signed rollout applies only to memory reviews begun after L88 lands; already-underway reviews (L168, L56, L57, L59) finish with their sealed-report workflow, with no migration/backfill. This describes the candidate contract, not a claim that the serving build already supports it.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [1]
- Reason admission, threshold and differing-harness/model inheritance boundary. [2]
- Record-only memory identity comes from memory authority, never the sibling code root. [3]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [4]
