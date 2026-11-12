# mcp/src/agents_remember/cli/role_launch_archive.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Archives the role agents recorded for a closed leaf. It derives the exact canonical leaf selection
from the admitted contract and surviving leaf document, enumerates the leaf's current and historical
launch receipts, marks every validated receipt before any host call, and settles each recorded target
through the existing `agent-archive` bridge command, keeping unresolved work as receipt-owned debt.

## Code Commentary

### Logic

`LeafAgentArchive.archive` resolves the terminal leaf document, builds the canonical task reference,
iterates `receipt_paths` (current `*.json` plus `history/*.json` under the task's
`notes/reports/paseo-native-executions`), and admits only receipts whose `leaf_receipt_ref` names the
same repository and path. Each admitted receipt is recorded by `ArchiveAttempt`.

`ArchiveAttempt.prepare` marks the receipt under the existing receipt lock before host I/O: a marked
receipt makes a not-yet-entered prepared launch refuse through `refuse_retired_start` and makes an
entered creation archive-only. `ArchiveAttempt._recorded_targets` validates the minted own and
predecessor UUIDs and the task-scoped reader binding, and leaves unreadable, conflicting or malformed
records untouched in `leftAlone` with a reason. `ArchiveAttempt._settle_target` settles the
predecessor debt head first and then the receipt's own target, recording outcomes in the bounded
`leafArchive` settlement map (at most two targets per receipt). `ArchiveAttempt._archive` calls the
bridge with the remaining bounded budget; host failure leaves the target `owed`, a host that no
longer knows the agent is `gone`, and a confirmed archive is `archived` or `alreadyArchived`.

`ARCHIVE_BUDGET_SECONDS` (8 s) is the closing pass's host-attempt deadline, and
`ARCHIVE_CALL_SECONDS` (2 s) bounds each bridge call inside it. These are controls on host attempts,
not an unconditional wall-clock bound on the whole operation: receipt traversal, parsing, metadata
locking and writes continue outside the preempted call. The report separates `archived`,
`alreadyArchived`, `gone`, `owed` and `leftAlone`, and an empty recorded selection states that no
role agents were recorded.

### Conventions

The service writes only the launch receipts' archive fields; it never rewrites launch status, the
report or artifact references, or the task document.

### Invariants And Boundaries

- A receipt whose reader binding conflicts with the leaf is left alone, never archived.
- The debt head stays in the receipt; no second queue or store is created.
- A host that does not confirm the archive leaves the target owed; nothing is reported archived that
  was not confirmed.

## Evidence

- The archive service derives the exact leaf reference and enumerates current and historical receipts. [1]
- Receipt marking happens under the existing lock before host I/O. [2]
- A marked start is refused and a returned creation settled. [3]
- Recorded targets are validated and unreadable or conflicting records are named. [4]
- The bounded host call settles debt and outcomes. [5]

- The host-attempt deadline and per-call cap bound host calls; receipt traversal, parsing, locking and writes are not preempted by them. [6]
