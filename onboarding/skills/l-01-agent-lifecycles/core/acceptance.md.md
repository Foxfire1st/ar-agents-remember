# skills/l-01-agent-lifecycles/core/acceptance.md

## Purpose

The **completion-truth and acceptance** block: the boundary between a mechanical terminal outcome and
an accepted handoff, the per-seat handoff-artifact table, the per-ID acceptance envelope, attempt
lineage, and the durable-evidence promotion hold point.

## Code Commentary

### Logic

The opening statement is the load-bearing negative: a canonical terminal/finalizer outcome of
`completed` means **only that the provider turn ended normally** — it does not attest that the required
artifact exists, is current, or satisfies its requirement. `interrupted` remains an interruption, not a
completed handoff. The host derives the mechanical seat-state signal and delivers one line to the structurally current owner waiting for the ended agent, carrying its last line. It **never** opens, parses, or evaluates a report, verdict, coherence record or acceptance envelope. The owner alone validates, and an artifact defect is owner-detected after wake.

The table under `## Write and send the handoff artifact` gives each of six seats (Worker, Reviewer, Curator, Investigator,
Manager, Orchestrator) its durable handoff artifact and its validator (worker → turn report + attempt journal, handed to the leaf's Reviewer, validated by the Reviewer for code and the Manager for the gate; curator → structured coherence record + projection, handed to the Reviewer, validated by the Reviewer for memory and the Manager for the gate; reviewer →
verdict, handed to the Worker and, on a pass, the Curator, and validated by the decider of the gate the verdict attaches to; and so on).

`## Bind acceptance to one requirement revision` fixes the six-part envelope
(`satisfied` / `blocked` / `approved-change`) and forbids general prose as an envelope, and
`## Independently judge the exact manifestation` states that the reviewer adjudicates each manifestation itself.
`## Keep requirement revisions and attempts distinct` keeps `ID@version` distinct from a leaf-local attempt ID, defines when an attempt is
minted, and gives the two malformed-row outcomes. `## Keep the master summary rebuildable` and
`## Record how retained evidence will be maintained` close the block; the last also binds Worker, Reviewer and Curator to pack each round's bulk evidence into one archive with a manifest in the report folder.

The gate owner takes closeout trees by filename from the highest-numbered memory `PASS` and landing-check verdict, never from a message. After the findings list is sealed, a finding may be added only through the two routes the review operation's Boundaries define: a valid code finding from the Curator, or a valid finding from an advisory review the Architect commissioned. Other observations outside the list and changed promises go through the parent to the developer without adding or reopening findings or resetting review.

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

- The host relays mechanical turn completion without inspecting acceptance artifacts. [8]

- Acceptance is per owned stable ID and version with complete rationale/citations/evidence. [10]

- Stable-contract or expiry evidence promotion is independent of requirement acceptance. [12]

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.

- Mechanical completion, artifact-blind relay, owner validation and unchanged authority. [1]

- Seat/artifact/validator duties and no second completion row. [2]

- Immutable attempts, malformed-row correction, candidate-specific review and successor rules. [4]

- Leaf journals are authority; summaries cannot gate work. [5]

- Selected Worker transport includes direct freeze handoff and producer-preserving post-PASS Curator list. [7]

- Each seat has its own artifact and distinct validator. [9]

- Requirement revisions and formal delivery attempts have separate immutable lineage. [11]
