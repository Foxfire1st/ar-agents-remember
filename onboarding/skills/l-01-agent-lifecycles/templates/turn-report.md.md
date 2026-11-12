# skills/l-01-agent-lifecycles/templates/turn-report.md

## Report path and ownership

- The retained worker artifact is written at the local report path its handover names and referenced from the leaf task document. Main-loop ownership, immutable requirement-attempt evidence, exact checks and file-based handovers remain. [4]

## Message/file transport

This canonical template requires messages to be short wake-ups naming requested work or a handover and its files. Report, verdict, list and evidence contents travel through file-only `body` or existing-file `attach`, not pasted into message text. Within a shared task, files stay with its record and a leaf workspace exposes the message-folder link. Text uses the effective settings limit without a pinned number. The canonical source and the packaged copy share this contract; transport does not change their existing write/start powers, peer destinations or independent acceptance authority.

## Report contents

The canonical worker report retains exact candidate, immutable requirement-attempt/journal links, measured command/evidence limits, findings and continuation inputs. The retrieval inventory records `read_ar_files` naming, native onboarding reads and route-index inspection. The source provides direct-handover and pending/refusal/recovery slots carrying exact candidate/evidence references; no courier reply or terminal outcome substitutes for the recorded requirement verdict. Completed turns remain distinct from requirement acceptance, and source wording is not new native evidence.

## Current composition and authoring contract

An optional visual walkthrough is governed by the Worker role, which points to `reference/writing/visual-explainers.md` before one is added to the freeze report; it supplements and never replaces required report sections or acceptance. The template's own pointers lead to `core/acceptance.md` sections, `operations/implementation.md#verify-the-final-candidate`, `operations/review.md#boundaries` and `reference/message-handover.md`.

The report remains the Worker's main-loop artifact at the supplied path, not delegated to a helper. Requirement attempt journal anchors, immutable expanded evidence, exact checks, separate durable-evidence hold point, direct handover evidence, harness contributions and respawn state retain their existing contracts. A shorter label, diagram or host turn-end signal proves no semantic acceptance.

## Governing Overview

[overview](../overview.md)

## Purpose

This is the mandatory durable worker handoff. It lets a fresh successor, curator, manager, and
independent reviewer recover the leaf from recorded state without relying on the transcript.

## Code Commentary

### Logic

The report records completed work, one acceptance envelope for the leaf-owned primary revision,
separate preservation checks for adjacent requirements, an explicit command/result table, the
separately governed durable-evidence promotion decision, issues and remaining work, curator inputs,
retrieval evidence, escalations, and respawn state. The primary acceptance block ties a delivery
claim to concrete artifacts and a verification claim to evidence that names the behavior
demonstrated and the regression caught.

The report and journal are distinct. The single physical leaf Requirement Attempt Journal contains
the immutable worker and reviewer record stream; the turn report links the exact worker attempts
appended only at review handoff and does not copy them into a second authority. Each worker record
is a lightweight requirement-specific view binding revision, manifestation, predecessor/findings,
exact candidate, status/rationales/citations/failure class, and a content-addressed frozen expanded-
evidence anchor. The complete acceptance corpus and command body live once in that artifact.
Internal implementation/test/evidence reruns use the separate protocol-event table and never
consume attempt IDs. Prior records are immutable; reviewer rejection advances through a successor
at the next handoff.
The rendered worker-record block is transient authoring input: after append it is removed from the
completed turn report and replaced by the exact authoritative journal anchor.

### Conventions

- Write the report at the local path the handover names, reference it from the leaf `task_doc` and retain its canonical destination.
- Repeat the acceptance block without aggregating or sampling revisions.
- Use code path plus symbol for code and path plus section/anchor for non-code deliverables.
- Record a not-run reason when no check ran instead of omitting the Checks section.

### Invariants And Boundaries

- Only `satisfied`, `blocked`, or `approved-change` are valid worker statuses per requirement.
- A blocked or changed delivery cannot pass without durable developer approval.
- Requirement proof and artifact-lifecycle proof remain different contracts.
- The report records facts and continuity state; it does not decide the review gate.
- Branch names or “latest” are not candidate identities, and the worker record cannot accept itself.

### Todos

None.

## CCR-R12@v5 Handoff Boundary

This template records the exact targeted or scoped checks and their failed or not-run status as handoff evidence. Closeout and integration consume the prepared code, memory-content, and ledger transaction and carry the complete memory-quality result that normal curation always runs; full code quality, full-suite tests, certification, and review are explicit requests rather than automatic template gates.

## Evidence

### Docs References

No external Domain Documentation source governs this report format.

### Repo-Internal References

- Every briefed manifestation receives an immutable candidate-bound worker record that cites its exact requirement anchor in the frozen expanded-evidence artifact, which holds the complete acceptance envelope once. [1]

- Exact commands and outcomes have a first-class report section. [2]

- Artifact lifecycle and task continuity are recorded separately. [3]

### Cross-Repo References

The report shape is generic; each dispatched repository supplies the actual verification command
and durable evidence paths.

## Canonical Source Ownership

The authored file is the canonical contract; its measured byte-equal package copy is a distribution carrier, not an independent role, task or permission authority.

- The authored source owns this contract; the distribution copy is not a separate authority. [5]

- The Worker reads the visual-explainer guidance before adding an optional walkthrough to its freeze report. [6]
