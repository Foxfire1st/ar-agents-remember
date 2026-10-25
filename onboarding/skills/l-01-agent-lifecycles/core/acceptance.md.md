# skills/l-01-agent-lifecycles/core/acceptance.md

## Current L113 source qualification

The following landed account controls only the changed start, launch-setting and completion seams it names. It is carried here from the former distribution-card owner during source-owner reconciliation; the canonical source remains the authority. Older incompatible dispatch, hosted-selector, notifier or capsule-injection wording below is historical, not restored behavior. Unchanged L54 explanations, inherited qualifications, complete reference groups and typed-entry provenance remain preserved. Source declarations and inherited tuples are not a new execution, CODE verdict, MEMORY grade or fresh whole-file anchor qualification. The incoming account's no-todo and live-source-discovery negatives are inherited editorial history, not new searches.

## Purpose

The **completion-truth and acceptance** block: the boundary between a mechanical terminal outcome and
an accepted handoff, the per-seat handoff-artifact table, the per-ID acceptance envelope, attempt
lineage, and the durable-evidence promotion hold point.

## Code Commentary

### Logic

The opening statement is the load-bearing negative: a canonical terminal/finalizer outcome of
`completed` means **only that the provider turn ended normally** — it does not attest that the required
artifact exists, is current, or satisfies its requirement. `interrupted` remains an interruption, not a
completed handoff. The host sends one mechanical line to the parent when an agent’s turn ends without a message to that parent; this is not the removed lifecycle-notifier sweep. It **never** opens, parses, or evaluates a report, verdict, coherence record or acceptance envelope. The owner alone validates, and an artifact defect is owner-detected after wake.

`## Which artifact each seat hands over, and who validates` is the table that gives every role in the
corpus its durable handoff artifact and its validator (worker → turn report + attempt journal, handed to the leaf's Reviewer, validated by the Reviewer for code and the Manager for the gate; curator → structured coherence record + projection, handed to the Reviewer, validated by the Reviewer for memory and the Manager for the gate; reviewer →
verdict, handed to the Worker and, on a pass, the Curator, and validated by the decider of the gate the verdict attaches to; and so on).

`## Acceptance is per stable ID and version, never aggregate` fixes the six-part envelope
(`satisfied` / `blocked` / `approved-change`), forbids general prose as an envelope, and states that the
reviewer adjudicates each manifestation itself. `## Requirement revisions and delivery attempts are
separate axes` keeps `ID@version` distinct from a leaf-local attempt ID, defines when an attempt is
minted, and gives the two malformed-row outcomes. `## The master-level summary is disposable` and
`## The durable-evidence promotion hold point (a separate concern)` close the block.

### Conventions

This file states a boundary that already holds; it changes no approval of requirements, plans, commits,
or integration. Role files state their own seat's side of it.

### Invariants And Boundaries

- Terminal `completed` truth is not acceptance; the owner validates the artifact before advancing state.
- The relay never inspects an artifact, and no seat authors a second model-written completion row.
- Acceptance is per stable ID + version and is never aggregate.
- A `satisfied` block is invalid when any required rationale, citation, or exact evidence is absent.
- A valid stable-contract-or-expiry disposition cannot fill a missing requirement rationale.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation governs this repository-local instruction file; it is canonical
repository prose consumed by the skill router.

No relevant documentation found after checking live sources.

### Repo-Internal References


- The host relays mechanical turn completion without inspecting acceptance artifacts. \[8] [8]


- Each seat has its own artifact and distinct validator. \[2] [9]

- Acceptance is per owned stable ID and version with complete rationale/citations/evidence. \[3] [10]

- Requirement revisions and formal delivery attempts have separate immutable lineage. \[4] [11]

- Stable-contract or expiry evidence promotion is independent of requirement acceptance. \[5] [12]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.

## Preserved L54 canonical account

The following pre-sync account retains its explanations and evidence. Its statements on the specifically superseded seams are historical; other meanings and their original citation identities remain intact.

<details>
<summary>L54 canonical prose and inherited source-epoch custody</summary>

## Governing Overview

[Lifecycle instruction overview](../overview.md)

## Purpose

This retained core document owns the distinction between mechanical completion truth and semantic handoff acceptance. It records the seat/artifact/validator matrix, acceptance of one owned requirement revision, immutable delivery-attempt lineage, the disposable master summary, and the separate durable-evidence promotion hold point.

## Commentary

### Mechanical truth and the owner's gate

`completed` means only that the provider turn ended normally; it proves neither artifact existence nor freshness nor requirement satisfaction. `interrupted` remains an interruption. The lifecycle relay derives turn truth and delivers its state signal to the agent that waits — the structurally current owner — carrying the ended agent's last line, without opening or evaluating reports, verdicts, coherence records, expectation rows or acceptance envelopes. The owner opens the required artifact, candidate identity, evidence and envelope before advancing state. Missing, malformed or stale artifacts are owner-detected defects, not a notifier check; unavailable turn truth is an observer-health problem. Nothing in this boundary changes authority over requirements, plans, commits or integration.

A seat must write its durable artifact before intentionally ending a successful handoff turn, then send it with `role_message` to the agent that waits; a file hands itself over to nobody, and a file on record wakes no one. The artifact carries neither the decider's nor the owner's runtime identity. Peer handovers are direct among Worker, Reviewer and Curator; recipients inspect the exact object and requested stretch, while Manager retains leaf-gate acceptance.

### Artifact responsibilities

Worker supplies a turn report and leaf Requirement Attempt Journal records: Reviewer validates code and Manager the gate. Reviewer supplies a verdict to the decider of its gate. Curator supplies a structured coherence record and generated projection: Reviewer validates memory and Manager the gate. The retained table also assigns the strategist's orchestration-task draft to Architect, the designer's task_doc and designer-limits note to Architect, the investigator's investigation report to its starting parent or developer, Manager's master-handover packet to Orchestrator, and Orchestrator's super-exit packet and demo notes to Architect. These are the source's artifact/validator relationships, not a claim that every named seat is available through every launcher.

### One owned revision and its envelope

Before dispatch, the owner projects the single owned primary stable ID/version, approved packet and durable corpus ruling into the builder brief, separately labeling dependency/preservation context. Adjacent context is a constraint, not something this leaf may claim closed. The builder supplies exactly one block with status `satisfied`, `blocked` or `approved-change`; delivery rationale; implementation citations using code path/symbol or the appropriate non-code deliverable anchor; verification rationale naming demonstrated behavior and the failure it catches; exact verification citations; and the command/result or a durable reference containing them.

`blocked` and `approved-change` additionally explain why unchanged delivery is impossible, describe changed delivery when present, and cite the durable developer approval/ruling. A new blocker awaiting approval is explicitly incomplete and cannot pass. Missing rationale, citations or exact evidence invalidates `satisfied`; aggregate requirements-addressed prose is not an envelope. The independent Reviewer inspects the exact packet and artifacts and returns `accepted` or `rejected` with its own rationale. Missing rationale, unapproved revisions, missing/wrong-class evidence or invalid citations force rejection. A truthful blocked row may be accepted as a handoff but still needs a BLOCK recommendation until delivered or approved as a change.

### Revision, attempt and experiment are different identities

`ID@version` changes semantic intent only through explicit developer approval. A leaf-local attempt identifies one exact candidate handed to independent review for one manifestation of that revision. Only a candidate review handoff or a successor after rejection advances the attempt; internal implementation, tests and evidence reruns remain separate experimental events with candidate, command, result, cause, repair and expected proof.

Before handoff, the worker appends an immutable, fully validated requirement-specific record binding revision, manifestation, predecessor/carried findings when present, exact tree/commit or non-code digest/anchors, status, rationale, citations, findings, failure class and a content-addressed immutable expanded-evidence reference. Expanded evidence holds shared definitions and full commands/results without duplicating complete master envelopes or experimental bodies in every attempt. Append and exact-candidate handoff form one formal boundary. A malformed pre-handoff row is preserved with an append-only `non-attempt-correction`/void reference and consumes no ID; its correction uses the same next ID. A malformed handed-off row is already an attempt, requires independent rejection, and can have a successor only at the next handoff. Worker neither self-rejects nor silently replaces rows.

Reviewer appends a separate immutable record for that exact attempt/candidate, with independent rationale and citations, classifying each rejection as `implementation defect`, `evidence gap`, `requirement contradiction/overconstraint`, `test/tool defect` or `external blocker`. Acceptance never floats to a later candidate. Rejection closes the attempt; a successor cites the predecessor and listed findings. Accepted attempts remain closed. Outside-list regressions, changed routes or changed requirements during successor verification go to the developer without adding findings, reopening resolved items or resetting review. Same-reviewer verification and shrinking findings remain, including through Architect takeover. Contradictions route through Architect for developer-approved revision; builder and Reviewer may propose but never approve or rewrite intent.

### Disposable summary and independent evidence retention

Per-leaf worker/reviewer records are authority. A master summary links those records and reports attempts, rejection history, current state and dominant open failure class per manifestation. It is rebuildable observation, never a requirement contract, lifecycle/closeout gate, queue authority or authoring lock; missing/stale summaries cannot block work.

Every newly created or retained fixture, recording, generator, shared support file or migration proof must name either a registered stable contract identity, real owner, executable evidence node and exact consumers, or an expiry date, executable replacement/removal event, owner and compatibility consequence. The source's `contract:codex-agent-wire-version-matrix`, `2026-09-30` and `node:...::test_replacement` are illustrative, not evidence of an active catalog entry or a current deadline. Useful-later prose is neither disposition, and missing/contradictory catalog rows are implementation work rather than tool blockers. This retention hold point cannot fill missing acceptance rationale/proof, and requirement satisfaction cannot waive durable-evidence metadata.

### Inherited context and limits

The earlier packaged-path card described the same completion boundary, envelope, lineage and independent retention hold point. Its role-routing gloss is retained only as context: this file owns artifacts and validators, while the selected role/operation owns the exact transport. For example, the Worker role explicitly sends its producer-preserving list to Curator after code PASS. The old no-todo statement and assertions about external/live-source discovery and absent sibling-repository contracts are inherited editorial history, not fresh repository-wide searches. This is source-contract documentation, not executed review, launch, provider, quality or acceptance evidence.

## Evidence

The quoted anchors below are literal strings in the canonical source ranges. They establish declarations and selected instruction boundaries, not executed outcomes.


- Mechanical completion, artifact-blind relay, owner validation and unchanged authority. [1]

- Seat/artifact/validator duties and no second completion row. [2]
- One primary revision, six-part envelope and independent adjudication. [3]
- Immutable attempts, malformed-row correction, candidate-specific review and successor rules. [4]
- Leaf journals are authority; summaries cannot gate work. [5]
- Stable contract or expiry disposition remains independent of requirement acceptance. [6]
- Selected Worker transport includes direct freeze handoff and producer-preserving post-PASS Curator list. [7]

</details>
