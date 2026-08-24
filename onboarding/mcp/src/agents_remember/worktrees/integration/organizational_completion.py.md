# mcp/src/agents_remember/worktrees/integration/organizational_completion.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/organizational_completion.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-24T14:43+02:00 |
| lastVerifiedCommitHash | `f95487ec993b58d34911bba0206a7fa6ef9684eb` |
| lastVerifiedCommitDate | 2026-08-24T15:28:18+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[governing route overview](overview.md)

## Purpose

Computes and publishes the exact completion proof for a branchless organizational master's final-leaf landing.

## Code Commentary

### Logic

`organizational_completion_plan` resolves the canonical sprint→master→leaf topology, requires
organizational execution, and binds the exact claimed final-leaf door. It loads a confined landing
contract for every sibling and requires each sibling's exact claimed door plus landed
code/memory/ledger pair to be reachable from the current sprint super. The completion fingerprint
binds the master semantic digest, sibling facts, and exact commits. Publication writes the master
completion decision only after protected-ref movement and fingerprint proof agree.

### Invariants And Boundaries

- Task parentage (logical master) and Git parentage (sprint super) stay deliberately separate.
- A sibling contract reached through any symlink or path escape is refused.
- Ledger rows stay one-to-one with the landed code+memory pair; retries cannot publish a stale mapping.
- An already-Completed master that lacks its exact certified marker raises.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Exact final-leaf plan requires sibling code/memory/ledger proof and sprint integrationBranch. | `organizational_completion_plan` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:134-191 |
| Scope validation pins executionNature, owning master, and canonical child. | `_completion_scope` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:194-230 |
| Sibling code ancestry is re-proved against the sprint super. | `_require_landed_sibling` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:486-522 |
| Sibling memory ancestry and unique ledger mapping are enforced. | `_require_landed_sibling_memory`, `_sibling_memory_mappings` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:555-564; mcp/src/agents_remember/worktrees/integration/organizational_completion.py:592-622 |
| Master completion is published only with the exact certified fingerprint. | `publish_organizational_master_completion` | mcp/src/agents_remember/worktrees/integration/organizational_completion.py:336-370 |

## Documentation References

No configured domain-documentation or cross-repository source applies to this file.

## 260821-CLIVE-L2 Current Contract

The current source seams include `OrganizationalCompletionError`, `OrganizationalCompletionPublicationError`, `OrganizationalCompletionPublicationState`. Organizational completion and repair are canonical integration-journal transitions with exact candidate, ref, quality, and cancellation evidence. The queue may schedule a door candidate but does not own failure repair or reopening lifecycle state.

### Reconciled Source Evidence

| Finding | Citations | Source Path |
| --- | --- | --- |
| The current module exposes `OrganizationalCompletionError`, `OrganizationalCompletionPublicationError`, `OrganizationalCompletionPublicationState` at this ownership boundary. | L38-L39; L42-L55; L59-L81 | `mcp/src/agents_remember/worktrees/integration/organizational_completion.py` |

## 260821-CLIVE Door-Based Completion Proof

Final-leaf proof is driven by the exact claimed `CloseoutDoorGeneration` and canonical sibling
contracts. The door itself embeds candidate, master, and sprint binding; sibling-landed checks
require their own exact claimed doors. Absence of a queue row, candidate collection, or mutable
blocker state is never organizational-completion evidence.

## Update History

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: moved final-leaf proof from queue collection to claimed doors and canonical sibling contracts. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: source moved to `mcp/src/agents_remember/worktrees/integration/organizational_completion.py` (new package route); the citation fixer repointed in-body references; import paths updated inside the module. Verified at code commit e5cb139f.


- 2026-08-17T12:09+02:00 — 260815-DAG-L5: created onboarding for the organizational direct-super completion proof.
