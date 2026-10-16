# mcp/src/agents_remember/tasks/launch_review_read.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Context-local launch recovery for unreadable review evidence without weakening ordinary task/review validation or losing raw evidence.

## Current Contract

The default-false ContextVar confines tolerance to explicit launch call scopes. launch_review_fallback returns no fallback unless the value is a mapping and every validation error is rooted solely in reviewState/memoryReviewState. It retains original broken lane values plus diagnostics and supplies a shallow replacement mapping with only those lanes set None for full remaining-document validation. preserve_unreadable_review reinserts raw values according to serialization include/exclude. The context manager resets its token in finally, including exceptional exits. This is context-binding restoration, not mutation rollback, task-identity recovery or permission to rewrite evidence; public task/review readers remain strict.

## Invariants And Boundaries

This is candidate-source onboarding, not execution, CODE/MEMORY acceptance, serving-build currentness or permission to publish. The owning caller retains transaction, host and role authority.


The governing workflow opens an independent memory review after CODE PASS on the same task using begin_review/record_review with reviewKind=memory. It has its own immutable baseline and shrinking IDs, under the same settings limit and extra-round approval rule, and never resets code reviewState. The signed rollout applies only to memory reviews begun after L88 lands; already-underway reviews (L168, L56, L57, L59) finish with their sealed-report workflow, with no migration/backfill. This describes the candidate contract, not a claim that the serving build already supports it.

## Evidence


- Worker/Curator typed review census, record-only exclusion and unknown history. [1]
- Reason admission, threshold and differing-harness/model inheritance boundary. [2]
- Launch scope opts in to review-only tolerance and forwards the same request reason. [3]
- Child start opts into tolerance after root identity validation; context does not cross exec. [4]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [5]
