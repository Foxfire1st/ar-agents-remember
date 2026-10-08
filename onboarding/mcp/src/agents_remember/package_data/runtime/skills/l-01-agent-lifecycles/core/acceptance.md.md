# core/acceptance.md

## Governing Overview

[MCP package overview](../../../../../../../overview.md)

## Purpose

The **completion-truth and acceptance** block: the boundary between a mechanical terminal outcome and
an accepted handoff, the per-seat handoff-artifact table, the per-ID acceptance envelope, attempt
lineage, and the durable-evidence promotion hold point.

## Code Commentary

### Logic

The opening statement is the load-bearing negative: a canonical terminal/finalizer outcome of
`completed` means **only that the provider turn ended normally** — it does not attest that the required
artifact exists, is current, or satisfies its requirement. `interrupted` remains an interruption, not a
completed handoff. The relay derives and delivers the state signal but **never** opens, parses, or
evaluates a report, verdict, coherence record, or acceptance envelope; the owner alone validates, and an
artifact defect is owner-detected after wake.

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

| The completion-truth boundary and the relay's artifact-blind behavior. | `# Core — Completion Truth And Handoff Acceptance (one home — this file owns the truth boundary)` | skills/l-01-agent-lifecycles/core/acceptance.md:1-14 |
| The per-seat handoff-artifact and validator table. | `## Which artifact each seat hands over, and who validates` | skills/l-01-agent-lifecycles/core/acceptance.md:27-42 |
| The six-part per-ID acceptance envelope and the reviewer's adjudication duty. | `## Acceptance is per stable ID and version, never aggregate` | skills/l-01-agent-lifecycles/core/acceptance.md:44-77 |
| Revision vs attempt lineage and the two malformed-row outcomes. | `## Requirement revisions and delivery attempts are separate axes` | skills/l-01-agent-lifecycles/core/acceptance.md:79-116 |
| The durable-evidence promotion hold point, which is independent of requirement acceptance. | `## The durable-evidence promotion hold point (a separate concern)` | skills/l-01-agent-lifecycles/core/acceptance.md:126-142 |

### Cross-Repo References

No sibling-repository contract defines this instruction file.

No meaningful cross-repo references found.
