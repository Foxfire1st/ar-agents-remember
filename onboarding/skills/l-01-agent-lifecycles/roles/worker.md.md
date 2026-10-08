# skills/l-01-agent-lifecycles/roles/worker.md

## Governing Overview

[roles overview](overview.md)

## Purpose

This canonical Worker implements one selected leaf’s approved primary requirement and explicit preservation constraints in its paired code worktree. The handover names the task/packet revision, code root, read-only memory root, contract and report. It leaves one truthful uncommitted candidate/report with failed and unrun checks visible; a finished turn is not AR acceptance.

## Logic

Resolve apparent missing task facts through the named canonical task/packet with supplied exact arguments, extensionless slug and returned canonical path. Read selected assignment documents and target source before editing, confirm paired roots, and make the smallest complete change within approved scope. Do not infer another task or load the complete hierarchy by default. Run relevant brief/repository checks and report exact outcomes; source observations remain evidence for the separate Curator.

The following producer/evidence/attempt constraints are preserved related task/review contracts; they do not expand the leaf’s single primary requirement or grant the Worker semantic acceptance.

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

Closeout, integration, task acceptance and admitted memory remain with their owning AR/Curator seats. Worker leaves the code candidate uncommitted and writes the exact canonical report, then freezes the candidate and sends it directly to the leaf's Reviewer; after code PASS it sends its structured hand-off list to the Curator. The Manager receives no routine report notice and relays no freeze, finding, verdict or memory change. A question for the developer goes to the parent named in the handover; a Worker without a parent asks in its own chat.

The Manager starts the Worker and Reviewer together and the Curator at the first freeze; no seat starts the one that checks it. Worker starts no role. Unknown results and compaction recover the same task/agent/report rather than inventing a new owner.

## Conventions

- One leaf, one worker seat, one physical attempt journal, one link-only turn report, and one
  curator hand-off list.
- Native reads in the actual worktree are the edit precondition.
- Worker owns edits and the report; native role-start authority is not granted to this role.
- Fix rounds resume the same worker when possible and append round evidence.
- New scope or a missing decision returns to the actual task owner/developer through the admitted own-chat or bound-parent route.

## Invariants And Boundaries

- Worker identity is the canonical leaf document plus `worker` role.
- Worker never commits, closes out, integrates, decides gates, or mutates accepted memory.
- Worker never absorbs manager, reviewer, curator, architect, orchestrator, or strategist work.
- No duplicate owner or background poller substitutes for canonical task and bound host facts.
- Use actual returned/handed-over agent IDs; do not invent a parent, recipient or delivery result.
- An aggregate “requirements addressed” statement is never terminal evidence.
- Internal pre-review candidate changes never consume attempt IDs. A reviewer-rejected handoff
  advances through an immutable successor; unrelated post-acceptance movement does not reopen
  accepted work. A failed journal append makes only that handoff incomplete and cannot lock
  unrelated task work.


## CCR-R12@v5 Transaction Boundary

This role card follows the transaction-only lifecycle boundary: the role reports its own targeted or scoped evidence with failed and not-run states visible and leaves closeout/integration to the authorized code, memory-content, and ledger Git transaction. Full quality, full tests, certification, and independent review are explicit operations only; curation is the standing exception — the curator always runs it complete — and it is not this seat's to run. Requested reviews retain the sealed finding list and monotonic three-round limit.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The Worker now freezes its candidate and sends it directly to the leaf's Reviewer with `role_message`, names the candidate head and change hash from its report, and asks for the Reviewer's whole next stretch; it sends its structured hand-off list directly to the Curator after code PASS, and runs the supported leaf sync itself, sending a memory-file conflict to the Curator and asking the Manager only for the staging step. It gains the harness-freedom paragraph and keeps its no-role-start and no-commit boundaries.

## 260928-MIK-L93 — a question for the developer goes up the chain

With a parent the Worker sends every developer question to it with `role_message` on `agents-remember-task`, saying what it holds back and recommends, and keeps working without ending its turn on the question. A busy or permission-prompt refusal stays pending under **Pending developer questions** in its report and is retried before the turn ends; only an unreachable parent opens the own chat, and having no work left does not. A relayed answer counts only with the developer's quoted words and the receiving agent's id, recorded where the role requires a record. The retired own-chat sentence is registered against return.

## Evidence

### Repo-Internal References

- Worker provides one truthful leaf report and uncommitted candidate; checks and turn ending are evidence, not AR acceptance. [1]
- Intake binds writes to the named code worktree and report path. [2]
- Orientation requires current worktree reads and coding guidelines before edits. [3]
- Build produces implementation plus evidence for the separate curator. [4]
- The worker appends authoritative attempts to the single journal and links them from the mandatory turn report. [5]
- The worker emits its requirement-shaped items as one curator hand-off list in the shared producer shape. [6]
- Tool authority excludes lifecycle, gates, task state, and memory writes. [7]
- The worker records the complete acceptance envelope once for every stable requirement ID. [8]
- Checks have their own explicit reportable step. [9]
- The worker builds one leaf in one session and delivers one scoped change set plus one report. [10]

## Historical R39 Generic Worker Doctrine

The canonical worker role requires the brief to carry the repository-resolved acceptance
environment and evidence. Workers do not select a host runner or compatibility fallback; leaf
closeout and master integration own the only acceptance runs.

## Historical 260815-DAG-L2 Leaf Quality Altitude

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
