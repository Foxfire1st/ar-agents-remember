# mcp/src/agents_remember/controlplane/supervisor_signals.py

| Field                  | Value                                                          |
| ---------------------- | -------------------------------------------------------------- |
| repository             | agents-remember                                                |
| path                   | `mcp/src/agents_remember/controlplane/supervisor_signals.py`   |
| doc_type               | `file-level-onboarding`                                        |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash |                                                                `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`|
| lastVerifiedCommitDate |                                                                2026-07-10T22:22:16+02:00|
| governingOverview      | `overview.md`                                                  |

## Governing Overview

[overview.md](overview.md)

## Purpose

Persisted cooldown memory for supervisor-owned pane/seat-liveness signals. It prevents the
deterministic supervisor sweep from minting a new owner-addressed inbox row every sweep for the same
target owner, leaf, finding kind, and detail.

## Code Commentary

### 260707-HFX2-L17 Pair-Scoped Cooldown Identity

Signal records and cooldown lookups add `seatRole`, so two roles with the same leaf, finding kind,
and detail retain independent cooldown slots. Existing bounded snapshot/compaction behavior is
unchanged.

### 260707-HFX2-L12 CS-6 Update

`SupervisorSignalCooldownStore` is no longer an unbounded per-finding full-file fold: reads skip malformed rows, `in_cooldown(records=...)` consumes a sweep snapshot, and `compact()` atomically retains only records inside the cooldown window.

### Logic

`SupervisorSignalRecord` is the strict JSONL record shape for one posted supervisor signal. Its
dedupe key is the tuple `_signal_emit` supplies: `targetAgentId`, `targetLifecycleId`,
`targetRole`, `leafKey`, `findingKind`, and `detail`, plus the stored `deliveryState` returned by
the hosted inbox delivery attempt.

`SupervisorSignalCooldownStore(observer_root)` writes `workspace/supervisor-signals.jsonl`.
`append(record)` creates the workspace directory and appends one alias-rendered JSON row. `read()`
parses the current full file into `SupervisorSignalRecord` rows. `last_sent(...)` filters the full
record set to rows matching the dedupe key and returns the newest timestamp. `in_cooldown(...)`
validates `cooldown_seconds` through `inbox_backoff.require_redelivery_floor_seconds`, then compares
the latest matching record's timestamp to `now`; malformed timestamps fail open for that row so the
next valid signal can be posted and persisted.

### Conventions

The store mirrors the control-plane JSONL-store style but is intentionally small: no MCP surface, no
catalog read, and no delivery itself. `serving/supervisor.py` is the production caller that decides
the routed owner, checks this store, posts the inbox row, and appends the cooldown record.

### Invariants And Boundaries

- The cooldown floor is shared with inbox redelivery and cannot be below 900 seconds.
- The key is owner/leaf/kind/detail scoped; different owner addresses or different finding details
  are allowed to post independently.
- This store records supervisor signal cooldown only. It does not consume inbox rows, ack
  expectations, deliver hosted messages, or decide the escalation ladder.

### Todos

Tracked HFX2-L11 gap from the HFX2-L9 reviewer verdict: this store is an unbounded append-only log
with no compactor or retention policy, and `in_cooldown()` currently reaches `read()` through
`last_sent()` once per pane/seat-liveness finding per sweep. That is a CS-6/L7-class scaling defect
on the supervisor hot path. It is a non-blocking deferral while `orchestration.supervisor.enabled`
remains disabled; if the supervisor is re-enabled before L11 bounds this store, the finding should be
treated as blocking.

## Docs References

No external/domain documentation is configured for this repo memory layer. The behavior is internal
supervisor control-plane state.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources; no Domain Documentation entries are configured. | N/A | N/A |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `SupervisorSignalRecord` defines the persisted signal-cooldown key fields and delivery state. | L14-L33 | [supervisor_signals.py](agents-remember/mcp/src/agents_remember/controlplane/supervisor_signals.py) |
| The store appends JSONL rows under `workspace/supervisor-signals.jsonl` and reads the full file back into records. | L36-L59 | [supervisor_signals.py](agents-remember/mcp/src/agents_remember/controlplane/supervisor_signals.py) |
| `last_sent` matches by owner/leaf/kind/detail and `in_cooldown` enforces the shared redelivery floor before comparing elapsed time. | L61-L113 | [supervisor_signals.py](agents-remember/mcp/src/agents_remember/controlplane/supervisor_signals.py) |
| `_signal_emit` checks this cooldown before posting and appends a record after the inbox signal delivery attempt. | L701-L747 | [../serving/supervisor.py](../serving/supervisor.py.md) |
| The serving app imports `SupervisorSignalCooldownStore` and wires `signal_cooldown_seconds` into each supervisor context. | L70; L517-L533 | [../serving/app.py](../serving/app.py.md) |
| The 900-second floor is owned by the shared inbox backoff helper. | L40-L52 | [inbox_backoff.py](inbox_backoff.py.md) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| Same-repository supervisor state only. | N/A | N/A |

## Update History

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: extended persisted cooldown identity with seat role so
  different seats on one leaf do not suppress one another.

- 2026-07-09T19:31+02:00 — 260707-HFX2-L12: documented the CS-6 scaling/reclamation change for this file. Verification metadata pinned until closeout stamps the HFX2-L12 commit.
- 2026-07-09T11:19+02:00 — 260707-HFX2-L9: created for the new persisted supervisor signal
  cooldown store, including the known unbounded-log/no-compactor limitation tracked for HFX2-L11.
  Verification metadata pinned until closeout stamps the 260707-HFX2-L9 commit.
