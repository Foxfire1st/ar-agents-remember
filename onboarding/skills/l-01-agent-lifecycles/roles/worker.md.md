# skills/l-01-agent-lifecycles/roles/worker.md

## Governing Overview

[roles overview](overview.md)

## Purpose

The worker is one short-lived implementation seat on one canonical leaf document. It reads its
complete brief and leaf task document, changes code in the named worktree, runs prescribed
leaf-scoped checks, and writes the mandatory builder turn report. Its terminal state is checks green
plus report written.

## Logic

The worker orients by pairing current worktree reads with onboarding and coding guidelines before
the first edit. It implements the approved leaf, fills only small unambiguous gaps, and records
changed paths, diff summary, tests, retrieval evidence, escalations, and onboarding observations in
the turn report. Observations are evidence for a separate curator; the worker does not write
accepted onboarding.

Beside the report the worker emits **the curator hand-off list** — every requirement-shaped item of
the leaf in the shape `../templates/curator-handoff-list.md` owns, one entry per item with its own
statement, kind, target, `found_at`, disposition and evidence, while `resolution`, `validated_at`,
`record_action` and `supersedes` stay `null` because they are the curator's to fill. That list is the
hand-off rather than a summary of one: items name where each thing lives — path plus the construct
inside it, from one resolution act — and keep the worker's own wording, because a re-worded statement
destroys the evidence the curator compares against the code.

Worker intake opens each version-addressed canonical packet and verifies the exact ID/version,
approved state, and durable corpus-ruling citation before implementation. A missing, unapproved,
or mismatched packet is a refusal, not permission to infer the requirement from leaf prose.

For every stable requirement ID in the brief, the report contains one acceptance envelope with
status, delivery rationale/citations, verification rationale naming both the proven behavior and
the failure caught, verification citations, and exact command/result or durable evidence. A
blocked or approved-change row additionally explains why unchanged delivery is unavailable and
cites the durable developer ruling. Non-code requirements cite the deliverable path and stable
section/anchor. The explicit Checks section records commands and outcomes rather than leaving the
brief-only obligation implicit.

The worker advances a delivery attempt only when an exact candidate is handed to independent
review, or after reviewer rejection when a successor is handed off. Internal implementation,
test, and evidence reruns are protocol events rather than attempts and retain candidate identity,
command, result, failure cause, repair, and expected next proof. Each formal attempt is an
immutable lightweight requirement-specific record containing status, rationales, citations,
findings/failure class, exact candidate, and a content-addressed anchor into frozen expanded
evidence. It does not duplicate the complete master envelope or protocol-event body.

Those records live in one physical leaf journal shared as an ordered append-only stream with the
independent reviewer. The separate worker turn report links newly appended attempt anchors and
does not duplicate their authority.

Closeout, integration, finalization, gates, task-document status, and memory quality belong to the
owning seat/curator chain. The worker communicates upward with structural `message_parent`; the
control plane derives the current parent occupant. Completion follows the durable report plus
terminal/finalizer truth, not a runtime-addressed model post.

The role table classifies worker as target-only. Only its manager is the ordinary plane-hosted
dispatch caller; an orchestrator or architect plane seat cannot dispatch a worker directly. An
identity-free developer launcher may target the leaf worker only for an explicit task-seat
takeover. The worker has no `dispatch_agent` caller authority or ambient recovery path, and its
dispatch/tools rows are structural documentation rather than settings keys.

## Conventions

- One leaf, one worker seat, one physical attempt journal, one link-only turn report, and one
  curator hand-off list.
- Native reads in the actual worktree are the edit precondition.
- Read/search fan-out may assist, but the main worker owns edits and the report.
- Fix rounds resume the same worker when possible and append round evidence.
- A plan delta beyond blank filling escalates one rung to the owning seat.

## Invariants And Boundaries

- Worker identity is the canonical leaf document plus `worker` role.
- Worker never commits, closes out, integrates, decides gates, or mutates accepted memory.
- Worker never absorbs manager, reviewer, curator, architect, orchestrator, or strategist work.
- No seat-local watcher or polling loop substitutes for the agent-notifier fact relay.
- Runtime session and lifecycle ids remain private control-plane correlation.
- An aggregate “requirements addressed” statement is never terminal evidence.
- Internal pre-review candidate changes never consume attempt IDs. A reviewer-rejected handoff
  advances through an immutable successor; unrelated post-acceptance movement does not reopen
  accepted work. A failed journal append makes only that handoff incomplete and cannot lock
  unrelated task work.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full quality, full tests, certification, and independent review are explicit operations only; curation is the standing exception — the curator always runs it complete — and it is not this seat's to run. Requested reviews retain the sealed finding list and monotonic three-round limit.

## Evidence

### Repo-Internal References

- The worker is one leaf-scoped builder whose terminal state is checks plus report. [1]
- Intake binds writes to the named code worktree and report path. [2]
- Orientation requires current worktree reads and coding guidelines before edits. [3]
- Build produces implementation plus evidence for the separate curator. [4]
- The worker appends authoritative attempts to the single journal and links them from the mandatory turn report. [5]
- The worker emits its requirement-shaped items as one curator hand-off list in the shared producer shape. [6]
- Tool authority excludes lifecycle, gates, task state, and memory writes. [7]
- The worker records the complete acceptance envelope once for every stable requirement ID. [8]
- Checks have their own explicit reportable step. [9]
- The worker builds one leaf in one session and delivers one scoped change set plus one report. [10]

## R39 Generic Worker Doctrine

The canonical worker role requires the brief to carry the repository-resolved acceptance
environment and evidence. Workers do not select a host runner or compatibility fallback; leaf
closeout and master integration own the only acceptance runs.

## 260815-DAG-L2 Leaf Quality Altitude

The worker brief now carries the leaf's execution nature and nature-appropriate source edge. A leaf
receives one repository-defined change-set-scoped acceptance at closeout and no integration rerun.
The repository's full suite belongs to master completion: against the exact proposed final
organizational super candidate before it lands, or against the completed atomic block during its
single landing.

## 2026-08-27 Attempt Boundary Clarification

Attempt publication is phase-sensitive: validate before append, and treat append plus the exact
review handoff as one formal boundary. A malformed row that never reached review is preserved by a
non-attempt correction/void record without consuming the next attempt ID; after handoff, only an
independent reviewer rejection permits a successor.
