# skills/l-01-agent-lifecycles/roles/worker.md

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `skills/l-01-agent-lifecycles/roles/worker.md` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T12:34+02:00 |
| lastVerifiedCommitHash | `f9f92ca793811b6cb738d7e302dfecdf8636e96e`|
| lastVerifiedCommitDate | 2026-08-30T14:26:46+02:00|
| governingOverview | `skills/l-01-agent-lifecycles/roles/overview.md` |

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

- One leaf, one worker seat, one physical attempt journal, and one link-only turn report.
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The worker is one leaf-scoped builder whose terminal state is checks plus report. | "## What This Seat Is" | skills/l-01-agent-lifecycles/roles/worker.md:7-17 |
| Intake binds writes to the named code worktree and report path. | "### 1 — Intake" | skills/l-01-agent-lifecycles/roles/worker.md:35-42 |
| Orientation requires current worktree reads and coding guidelines before edits. | "### 2 — Orient (paired reads before edits)" | skills/l-01-agent-lifecycles/roles/worker.md:44-57 |
| Build produces implementation plus evidence for the separate curator. | "### 3 — Build" | skills/l-01-agent-lifecycles/roles/worker.md:59-69 |
| The worker appends authoritative attempts to the single journal and links them from the mandatory turn report. | `### 6 — The Turn Report (mandatory, your last act)` | skills/l-01-agent-lifecycles/roles/worker.md:175-188 |
| Tool authority excludes lifecycle, gates, task state, and memory writes. | "## Tool Surface (positive statement — this is all of it)" | skills/l-01-agent-lifecycles/roles/worker.md:195-195 |
| The worker records the complete acceptance envelope once for every stable requirement ID. | "### 4 — Per-Requirement Acceptance Envelope" | skills/l-01-agent-lifecycles/roles/worker.md:75-99 |
| Checks have their own explicit reportable step. | "### 5 — Checks (green before you report)" | skills/l-01-agent-lifecycles/roles/worker.md:152-152 |

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

## Update History

- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 classified worker as target-only plus explicit
  ambient-takeover target, corrected ordinary plane ownership to the manager only, and kept
  structural authority outside settings. Verification remains closeout-owned.

- 2026-08-28T14:18+02:00 — Reconciled worker-role citations against the committed PDLS candidate;
  the immutable candidate-bound attempt and one-primary-requirement duties are unchanged.

- 2026-08-28T11:51+02:00 — No content impact: the source now matches this card's existing rule
  that only the leaf-owned primary revision receives an envelope and formal attempt.

- 2026-08-28T11:32+02:00 — No content impact: re-read the v25 role/topology clarification; this
  card already describes one leaf-owned primary revision, adjacent contextual constraints, and
  the source-specific worker/reviewer/manager/curator boundary.

- 2026-08-27T22:15+02:00 — Distinguished pre-handoff non-attempt correction from post-handoff
  reviewer rejection and successor lineage.

- 2026-08-27T21:53+02:00 — M40@v2: formalized review-handoff-only attempt advancement, separate
  protocol-event logging, and lightweight content-addressed worker records.
- 2026-08-27T20:45+02:00 — Distinguished the single physical attempt journal from the
  link-only worker turn report.
- 2026-08-27T19:59+02:00 — M42 clarification: scoped successor creation to unadjudicated changes,
  rejected repairs, and corrections while preserving accepted work across unrelated candidates.
- 2026-08-27T18:06+02:00 — M40/M43: documented before-handoff immutable attempt append, exact
  candidate and predecessor binding, successor repairs, and closed failure classification.
- 2026-08-27T14:04+02:00 — Tightened M39 intake to require an approved version-addressed packet
  carrying its durable corpus ruling before a worker may implement or claim acceptance.
- 2026-08-27T13:32+02:00 — M39@v1: worker intake refuses missing/mismatched requirement versions
  and every acceptance block binds to the exact canonical revision. Verification remains
  closeout-owned.

- 2026-08-27T12:43+02:00 — M38: recorded the per-ID worker evidence envelope, non-code citation
  form, blocked/approved-change approval proof, and explicit Checks section. Verification metadata
  stays pinned until governed closeout stamps the PDLS commit.

- 2026-08-15T04:32+02:00 — 260815-DAG-L2: recorded execution-nature input and the leaf-targeted,
  master-full acceptance boundary. Verification remains closeout-owned.

- 2026-08-14T11:29+02:00 — R39 curator: reconciled canonical worker guidance with generic
  repository-resolved policy. Verification remains closeout-owned.

- 2026-08-11T14:20+02:00 — Rewrote the default body around real-leaf implementation, durable
  evidence, structural escalation, and separate curator ownership.
- 2026-08-09T12:08+02:00 — Fact-relay supervision replaced seat-local watcher/ladder language.
- 2026-08-08T02:00+02:00 — Leaf checks became change-set scoped; full quality remained master-owned.
- 2026-07-05T01:30+02:00 — Established the self-contained worker lifecycle and report terminal state.
