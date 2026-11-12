# mcp/src/agents_remember/application/master_architect_record.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The master-to-architect record — which hosted architect seat owns one master — together with the report custody it feeds: the report log, the held-message store, execution-receipt reads and the host ports the CLI injects.

## Code Commentary

- The record is three facts at one address and has exactly two writers, a Manager start and a `claim`; `write_record` refuses any other act and replaces the file whole through the kernel's atomic write, so a reader sees the old record or the new one and never half of either.
- Reading never creates anything: an oversized, unreadable or malformed record is simply a master no seat is named for, and `_segment` refuses a repository or master name that is empty, `.`, `..`, carries a separator or exceeds 128 characters, so a caller never chooses a path.
- Report state is appended one JSON line at a time under an exclusive file lock with an fsync. Log reads are bounded at 4 MiB and skip symlinks; `foreign_logged_report_ids` names IDs present in other masters' logs so the control layer can refuse them during custody transfer.
- The held-message store refuses a twenty-first message per recipient with `HeldStoreFull` and never drops one to make room; re-holding the same attempted message id answers with that existing row instead of a duplicate.
- `withdraw_message` refuses a row another sender owns and a row already being delivered (`HeldMessageCommitted`), and `store_path_for` accepts only a canonical AR UUID as an agent id.
- Host behaviour is injected from the CLI half through `bind_explainer_control_host`; with no ports bound the host factory answers `None` and the bridge send raises rather than pretending a send happened.

## Evidence

- An act other than a Manager start or a claim is refused before any write [1]
- A record that cannot be read or validated names no seat instead of raising [2]
- A recipient already holding the bound refuses a further message rather than dropping one [3]
- A message already committed for delivery cannot be withdrawn [4]
- Only a canonical AR UUID names a held-message store file [5]

- A process with no bound host ports raises RuntimeError before a bridge send [6]
