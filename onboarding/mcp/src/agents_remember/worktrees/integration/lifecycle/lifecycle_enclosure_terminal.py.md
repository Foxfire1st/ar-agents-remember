# mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:53 |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80`|
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Validates external terminal archive/receipt proof and the exact predecessor authority required to
publish a successor enclosure.

## Code Commentary

### Logic

A restartable predecessor must have no code or memory closeout/integration outputs. The terminal proof no longer tests retired ledger output cells; exact archive, receipt, locator, and predecessor evidence still governs successor publication.

Archive paths are fixed by the publication request and must be outside the old enclosure root.
Digest, receipt, and the pre-deletion locator must match. A surviving terminal contract may advance
only from archive-ready to the exact cleanup-completed state; restart requires a restartable
tombstone and exact terminal predecessor identity.

### Conventions

Accepted input, exact Git facts, and typed owner results stay distinct from disposable projections.

### Invariants And Boundaries

- A missing or deleted enclosure is never sufficient successor evidence.
- Archive, receipt, locator, and predecessor proofs must agree byte-for-byte.
- Successor publication is part of the terminal enclosure transaction, not a standalone WAL.

### Todos

None recorded for the ledger-retirement boundary.

## Docs References

No external Domain Documentation source is configured for this slice. The current behavior is repository-owned and is supported by the source references below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external source applies. | — | — |

## Cross-Repo References

No separately configured cross-repository implementation governs this file; any external-memory repository is addressed by the task contract.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional cross-repository evidence applies. | — | — |

## Repo-Internal References

The following current source boundaries establish the ledger-retirement behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| `restartable_predecessor_contract` requires a terminal restartable contract without recorded code/memory outputs. | `restartable_predecessor_contract` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py:407-435 |
| `require_successor_generation` validates exact terminal predecessor and successor identities. | `require_successor_generation` | mcp/src/agents_remember/worktrees/integration/lifecycle/lifecycle_enclosure_terminal.py:343-368 |

## Update History
- 2026-09-20T00:57+02:00 — 260915-KS citation residue clearance (uncommitted change set on memory base `66b2ae8adebea11bc2300d2d51822f321a128657`): hand-read the one enforced row this slice carries and cleared it (`citation_anchor_absent_from_range`). The row's claim and anchor both spelled `_restartable_predecessor_contract`, which exists nowhere in the tree; reading `lifecycle_enclosure_terminal.py` shows the construct the claim describes — a restartable tombstone whose recorded code/memory outputs are all empty — declared as `restartable_predecessor_contract` at `407-435`. Only the leading underscore and the range were corrected so the anchor names the declaration the claim is about and the range holds it; no wording changed meaning, no range was dropped to silence a finding, and no verification stamp was advanced. No commits.

- 2026-09-15T00:53 UTC — LCA-L9 working-candidate curation: retired ledger Git authority in this file-specific boundary; preserved real Git and lifecycle safeguards and prior history. Source and diff reviewed, source-sha256=a92a727ad3fc82423b4e531f64c1059ef6135c9e082a22f1358ba1ae77d185dd. Existing verification commit/date remain unchanged until an actual source commit is available; no test or acceptance claim.


- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final terminal-enclosure authority. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
