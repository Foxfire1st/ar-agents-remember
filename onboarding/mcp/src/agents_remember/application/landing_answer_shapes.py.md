# mcp/src/agents_remember/application/landing_answer_shapes.py

## Governing Overview

[Application overview](overview.md)

## Purpose

Project validated task, landing and role results into the answer the caller can act on, while the complete result remains available to the logging owner. This module owns field selection, not the transaction, task authority, host delivery or generic overflow guard.

## Code Commentary

Landing projections retain the reached state, blockers, executable next-step inputs and produced commits/control values from each tool's declared roster. Since MIK-R124, `worktree_integrate`, `worktree_checkpoint_landing`, `worktree_record_landing` and `direct_landing` also keep `staleDocuments`: the count of documents the landing made stale, the documents it lists and the read that lists them, or the state the operation could not compute. The field is absent when the landing named no document at all — an ordinary landing or a checkpoint that made nothing stale, or a master's end with neither newly nor inherited stale documents; a master's end that names only inherited debt keeps it as `count: 0` beside `alreadyStale`, an uncomputable read answers its `state` and `detail` without a count, while an unverifiable one answers its `state`, its `detail`, the count and the documents — so the count survives an unobservable document, and only an uncomputable staleness removes it. The projection selects the field; it neither computes staleness nor refuses a landing. Unrelated tools return `None` to select the ordinary completion path. An ordinary answered refusal keeps its existing code, or derives one from the producer status, and carries the producer reason in summary (or detail when no summary exists), not the raised-error field. Actual code="raised" answers retain error. Admission tables, duplicate diagnostics and guidance remain in the complete log; the bounded answer keeps its executable next step. This projection changes neither the underlying refusal/check order nor its no-write boundary.

Redundant contract echoes are removed only from copied answer mappings. Preview commit intent/count information remains while additional worktree/ledger locations stay in the whole result. Nested next-step information still reaches the common guidance translation; removing an echo must not remove the arguments needed to act.

A successful role start retains the agent ID, handover location and a meaningful warning. A successful role message retains outcome/status/taken, adds the recipient ID only for role addressing, and keeps a host cancellation warning. A waited reply additionally carries text and actionable wait detail; an oversized reply is fitted to keep its beginning. Refused role operations retain their producer refusal shape.

Task-document writes retain the changed-unit/value phrase, file-input digest when measured, and supplied code/memory review states plus reviewKind on review-changing operations. Only create returns the rendered document location. A successful master sync is omitted, but failure stays visible. A dry run retains loss and a bounded diff, not rendered leaf/master contents; the completion owner settles its cut marker against the report/detail that was actually retained.

## Boundaries

- The validated whole result is not modified by answer-only address or preview-location trimming.
- Projections do not reserve a candidate, accept a requirement, waive a blocker or perform a landing.
- The common completion owner still applies list limits, log outcomes and the delivered-answer guard.
- Ordinary target counts exclude locations recursively; at most two distinct locations are named, while the entire delivered mapping remains subject to its separate bound. This is a measurement/answer contract, not a root-length restriction.

## Current Contract

`project_task_doc_answer` retains any supplied reviewState, memoryReviewState and reviewKind on the three review-changing operations. It does not derive a missing lane or publish a result. Other write/create/dry-run/master-sync projection rules remain intact, and the whole validated result remains separate logging custody. Keeping both states makes a memory publication distinguishable without erasing the passed code state.

This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [6]

- Landing tools select their declared answer fields and preserve producer refusals without altering the transaction. [1]
- A successful start retains the new agent and handover, while failures keep their shape. [2]
- Role-addressed and waited messages retain only the conditional information their caller needs, including cancellation warnings and reply beginnings. [3]
- Writes, dry runs, create, review changes and master-sync failures have distinct task-document projections. [4]


- Ordinary refusals keep producer code and reason without error; raised answers keep error; diagnostic blocks remain in the whole log. [5]
