# mcp/src/agents_remember/serving/inbox_reclamation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/inbox_reclamation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-12T17:40+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`|
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[serving overview](overview.md)

## Purpose

Pure policy and evidence adapter for reclaiming pending supervisor nudge/escalation inbox rows
whose subject session is positively confirmed gone.

## Code Commentary

### Logic

`plan_confirmed_gone_reclamation` first filters to pending supervisor-created `nudge` or
`escalation` rows with `subjectAgentId`, deduplicates subjects, and joins one terminal-catalog
snapshot. Only `terminated` is direct proof. Catalog-absent subjects require one successful
tmux name snapshot; exact `ar-<subject-id>` absence resolves them, while presence or any
indeterminate command failure keeps them. `snapshot_tmux_session_names` treats a known
`no server running` result as positive empty evidence and all other failures as fail-closed.

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

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain source was available. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The eligibility, catalog/tmux evidence join, and aggregate plan are defined here. | L52-L105; L108-L157 | [inbox_reclamation.py](agents-remember/mcp/src/agents_remember/serving/inbox_reclamation.py) |
| Terminal catalog statuses and tmux ownership provide the evidence inputs. | L1-L30 | [terminal_catalog.py](agents-remember/mcp/src/agents_remember/serving/terminal_catalog.py) |
| The supervisor invokes the policy before compaction and redelivery. | L1127-L1161 | [supervisor.py](agents-remember/mcp/src/agents_remember/serving/supervisor.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| None. | N/A | N/A |

## Update History

- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: created the sidecar for the new policy module,
  recording narrow eligibility, positive-gone/fail-closed evidence, one-snapshot boundedness,
  body-free output, and non-blocking F3-F6 residuals. Verification metadata remains blank until
  the candidate receives a commit.
