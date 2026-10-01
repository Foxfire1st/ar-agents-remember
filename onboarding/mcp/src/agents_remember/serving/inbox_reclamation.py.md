# mcp/src/agents_remember/serving/inbox_reclamation.py

## Governing Overview

[serving overview](overview.md)

## Purpose

Pure policy and evidence adapter for reclaiming pending supervisor nudge/escalation inbox rows
whose subject session is positively confirmed gone.

## Code Commentary

### Logic

`plan_confirmed_gone_reclamation` first filters to pending agent-notifier-created `nudge` or
`escalation` rows with `subjectAgentId`, deduplicates subjects, and joins one terminal-catalog
snapshot. Only `terminated` is direct proof. Catalog-absent subjects require one successful
tmux name snapshot; exact `ar-<subject-id>` absence resolves them, while presence or any
indeterminate command failure keeps them. `snapshot_tmux_session_names` treats a known
`no server running` result as positive empty evidence and all other failures as fail-closed.

**260713-TES-L2 landed-row exclusion.** `_eligible` cit:([`_eligible`], mcp/src/agents_remember/serving/inbox_reclamation.py:137-146) additionally excludes
`state_signal_landed(entry)` rows: a landed state-signal is terminal on the relay path and must
never be reclaimed as confirmed-gone. Current landed rows carry terminal `state="landed"`; the old pending/by-rule description belongs to the earlier migration stage.

### Conventions

The module returns a body-free aggregate `InboxReclamationPlan`, stable reason
`subject-session-confirmed-gone`, row counts, unique subject count, and an evidence class. It
does not write the inbox, call the store, or probe once per row; its callback is invoked at most
once per sweep and has a 5-second subprocess timeout.

### Invariants And Boundaries

- Durable/protected, subjectless, model-authored, active, landed, exited, tmux-present, and
  indeterminate rows are retained.
- Catalog absence alone is never proof.
- The exact session-name contract is currently `ar-<subject-id>`; F3 tracks future reuse of the
  canonical terminal naming helper.

### Todos

F3-F6 are non-blocking reviewer residuals: canonical tmux-name derivation reuse; refolding stale
append-mutators under the lock; documenting lock-held read characteristics; and factoring the
duplicated terminal-resolution update shape.

## Evidence

### Docs References

No domain documentation is configured; the task contract and repository source are the direct
evidence for this policy.

### Repo-Internal References

- The aggregate reclamation plan is built from one reconstructed snapshot joined with catalog evidence. [1]
- Terminal catalog entries provide the status and ownership evidence. [2]
- Reconstructed tmux snapshots provide the remaining ownership evidence. [3]
- The agent-notifier imports the inbox-reclamation policy module. [4]

### Cross-Repo References

No meaningful cross-repo references found.
