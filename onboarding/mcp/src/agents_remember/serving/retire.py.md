# mcp/src/agents_remember/serving/retire.py

| Field                  | Value                                        |
| ---------------------- | ---------------------------------------------- |
| repository             | agents-remember                                |
| path                   | `mcp/src/agents_remember/serving/retire.py`     |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-08-02T01:42+02:00                           |
| lastVerifiedCommitHash | `7bf564a663bb61f12844dee39538dd09a1633cdb`                                    |
| lastVerifiedCommitDate | 2026-08-10T12:28:42+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`retire.py` owns the single-seat retirement primitive: it optionally stops the
control session, terminates the terminal host session, and persists a
`SeatClosure` through the terminal catalog.

## Code Commentary

### Logic

`retire_entry` accepts a `SeatClosure` rather than separate provenance
keywords. When a control endpoint exists it first calls
`stop_control_session`. A `HarnessControlError` is recorded in
`control_raw["retireControlStopError"]` and the entry is upserted so an
orphaned terminal can still be reaped. The function then calls
`host.terminate` and `catalog.mark_retired` with the closure's four fields.

### Conventions

`TerminalHost` is imported only under `TYPE_CHECKING` (a lazy/type-only import) to avoid a runtime
import cycle — callers pass a real `TerminalHost` instance at call time.

### Invariants And Boundaries

- Transcripts are never touched here — retiring is a catalog-and-tmux operation only; this module
  has no knowledge of transcript storage.
- A graceful control-stop failure is retained on the catalog entry before
  terminal termination continues.
- Exceptions other than the explicitly handled `HarnessControlError` are
  not swallowed by this module.

### Todos

No known follow-up in this file.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
seat-retirement-specific behavior; this file is same-repository runtime plumbing implementing a
developer-ruled cleanup automation, not an external standard.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external/domain document is needed; the module's implementation is the source of truth. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The closure record carries timestamp, reason, edge, and acting session. | `SeatClosure` | mcp/src/agents_remember/serving/retire.py:21-34 |
| Retirement handles graceful control-stop failure, terminal termination, and catalog marking. | `retire_entry` | mcp/src/agents_remember/serving/retire.py:37-71 |
| The control-session stop failure type is handled explicitly. | "except HarnessControlError as exc" | mcp/src/agents_remember/serving/retire.py:55-55 |
| Retirement invokes the control-session stop path when configured. | "stop_control_session(entry)" | mcp/src/agents_remember/serving/retire.py:54-54 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local retire-mechanics module. | — | — |

## Update History
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T08:03:35+02:00 — 260731-EFA-L6 S18-B07 curator: repaired the bounded citation findings from the recovered Avicenna and Kuhn ledgers, splitting or narrowing claims to the frozen source and normalizing scoped citation ranges.
- 2026-08-02T01:42+02:00 — No content impact: corrected Source Path link depth. The link(s) in this document carried one `../` too many and had never resolved from this card's directory — not code moving out from under a citation, the path as written. Enumerating every depth in both trees leaves exactly one that resolves and it is exactly one level shallower, so there was nothing to judge (`memory_quality/style/citations`, `citation_link_depth_wrong`). No claim, range or target document changed. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded `SeatClosure` as the shared terminal-mark provenance for both retirement and landing; authority policy unchanged.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented protocol-aware retirement boundary.

- 2026-07-09T13:36+02:00 — 260707-HFX2-L11 round 2: removed the production-dead
  `retire_seats_for_leaf` helper and documentation-only `RETIRABLE_ROLES` constant after completion
  edges switched to `landing.py`; this sidecar now documents only explicit per-session retire and
  landed archive cleanup use of `retire_entry`. Verification metadata pinned until closeout stamps
  the 260707-HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat lifecycle: retirement, issue #12): the
  shared retire mechanics — `retire_entry` (kill tmux + persist the terminal mark, idempotent),
  `retire_seats_for_leaf` (the automation-hook entry point, scoped by `leaf_key` + `roles`,
  `by_session=None`), `RETIRABLE_ROLES` (documentation-only role census). Shared by the manual
  MCP/serving retire paths (after `check_retire_authority` gates them) and the completion-edge
  automation (which bypasses that policy by design — see Invariants). Verification metadata pinned
  until closeout stamps the HFX-L8 commit.
