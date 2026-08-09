# mcp/src/agents_remember/serving/inbox_reclamation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/inbox_reclamation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-09T01:21+02:00 |
| lastVerifiedCommitHash | `cdca11264fb4d27ee08f5e8b37ac5496e67c0840`|
| lastVerifiedCommitDate | 2026-08-09T07:36:31+02:00|
| governingOverview | `overview.md` |

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
never be reclaimed as confirmed-gone, even though its row state stays `pending` until the L4
schema migration.

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

## Docs References

No domain documentation is configured; the task contract and repository source are the direct
evidence for this policy.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The aggregate reclamation plan is built from one reconstructed snapshot joined with catalog evidence. | `InboxReclamationPlan` | mcp/src/agents_remember/serving/inbox_reclamation.py:84-131 |
| Terminal catalog entries provide the status and ownership evidence. | "class TerminalCatalogEntry:" | mcp/src/agents_remember/serving/terminal_catalog.py:106-220 |
| Reconstructed tmux snapshots provide the remaining ownership evidence. | `TmuxSessionNameSnapshotter` | mcp/src/agents_remember/serving/inbox_reclamation.py:84-131 |
| The agent-notifier imports the inbox-reclamation policy module. | `inbox_reclamation` | mcp/src/agents_remember/serving/agent_notifier.py:81-81 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History

- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the `state_signal_landed` exclusion
  in `_eligible` (landed relay rows are terminal on this path). Verification metadata pinned
  until closeout stamps the 260713-TES-L2 commit.
- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-04T11:42:15+02:00 — 260731-EFA-L6 S18-B04 — same-reviewer semantic correction: removed placeholder findings and narrowed
  reclamation evidence to the snapshot, catalog, policy, and supervisor owners.

- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: created the sidecar for the new policy module,
  recording narrow eligibility, positive-gone/fail-closed evidence, one-snapshot boundedness,
  body-free output, and non-blocking F3-F6 residuals. Verification metadata remains blank until
  the candidate receives a commit.
