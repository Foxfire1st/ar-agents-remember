# mcp/src/agents_remember/serving/retire_policy.py

| Field                  | Value                                                 |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/retire_policy.py`      |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-08T02:43+02:00                                  |
| lastVerifiedCommitHash | `2322ffc15ef803ea29bf900beeae84de19b43019`              |
| lastVerifiedCommitDate | 2026-07-08T03:14:39+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`retire_policy.py` is the server-side authority policy for seat retirement (260707-HFX-L8, issue
#12). It is the single place that decides WHETHER an actor seat may retire a target seat — the
developer-ruled authority split (a manager retires only its own master's worker/reviewer seats; the
orchestrator retires any seat; no seat ever retires itself) is enforced here, not trusted from the
caller, and both the manual `session_retire` MCP tool / `POST /api/terminal/{session}/retire`
endpoint and any future retire entry point must route through `check_retire_authority` before
mutating the catalog.

## Code Commentary

### Logic

`SeatRef` is a frozen dataclass carrying the three retire-policy-relevant facts about one catalog
seat: `session_id`, `role` (the seat's `spawn_role`), and `master` (the master identity the seat
belongs to). `master_of(leaf_key)` derives that master identity from a qualified leaf key
(`repo/master/doc-id`, `leaf_key.split("/", 2)[1]`), returning `None` for an unset/malformed key.
This is uniform across dispatch levels: a worker/reviewer's `leaf_key` names its own leaf under the
master folder, and a manager's own `leaf_key` names the master task-doc itself under the SAME
folder — either way the second path segment is the identity `check_retire_authority` compares.

`check_retire_authority(actor, target)` raises `RetirePolicyError` unless `actor` may retire
`target`, in strict precedence order:
1. **Owner-never-self-retires, checked FIRST and unconditionally** — `actor.session_id ==
   target.session_id` raises before any role branch runs, so no role's authority can ever override
   it (verified directly: even an actor mis-tagged with `role="worker"` retiring itself still hits
   this branch first, per the test matrix in `test_seat_lifecycle.py`).
2. `actor.role == "manager"` — refused unless `target.role` is in `MANAGER_RETIRE_ROLES =
   frozenset({"worker", "reviewer"})` AND `target.master == actor.master`; the raised message names
   both clauses (`"own master"` substring) so a refusal is loud and policy-naming, never a silent
   no-op.
3. `actor.role == "orchestrator"` — always permitted, portfolio-wide.
4. Anything else — refused with `"no retire authority"` in the message.

`RetirePolicyError` subclasses `AgentsRememberError` so it composes with the repo's existing
error-surfacing conventions (caught and translated into a `retire-refused` tool/HTTP status by
callers, never left to propagate as an unhandled exception).

### Conventions

Pure decision logic with no I/O and no catalog access — callers (the MCP tool, the serving
endpoint) are responsible for resolving `SeatRef`s from `TerminalCatalogEntry` rows (via
`entry.id`/`entry.spawn_role`/`master_of(entry.leaf_key)`) before calling this module, and for
turning a raised `RetirePolicyError` into their own response shape.

### Invariants And Boundaries

- Owner-never-self-retires is a hard invariant with NO override path — a manager's own seat can
  never be a worker/reviewer of its own master by construction, so this policy alone guarantees a
  manager (which lives outside the master stack it manages) can never accidentally unseat itself.
- Only the orchestrator has portfolio-wide retire authority; every other role is scoped or refused
  entirely.
- This module never touches `TerminalCatalog` or `TerminalHost` — it is a pure authority check, kept
  separate from `retire.py`'s mechanics so the policy can be unit-tested without any catalog I/O.

### Todos

No known follow-up in this file. The reviewer's Risk 2 disposition (actor identity is
self-declared, not ambiently resolved) is a caller-side concern (see `retire.py` and
`mcp/tools/terminal.py`), not a gap in this policy module itself.

## Docs References

No relevant external documentation found after checking the repo Domain Documentation for
retire-authority-specific behavior; this file is same-repository runtime plumbing implementing a
developer-ruled authority split recorded in the task doc, not an external standard.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No external/domain document defines this authority split; the developer ruling in the leaf task doc and this implementation are the source of truth. | L1-L64 | [retire_policy.py](retire_policy.py) |

## Repo-Internal References

`check_retire_authority` is called from both the manual retire paths and reads `SeatRef`s built
from `TerminalCatalogEntry` fields; the leaf task doc records the developer ruling this file
encodes.

| Finding | Citations | Source Path |
| --- | --- | --- |
| `session_retire_payload` builds actor/target `SeatRef`s from `TerminalCatalogEntry.spawn_role`/`leaf_key` and calls `check_retire_authority` before any catalog mutation, translating `RetirePolicyError` into a `retire-refused` tool status. | `session_retire_payload` | [../../mcp/tools/terminal.py](../../mcp/tools/terminal.py) |
| `POST /api/terminal/{session}/retire` performs the identical authority check before calling `retire_entry`. | `api_terminal_retire` | [app.py](app.py) |
| `TerminalCatalogEntry.spawn_role` and `leaf_key` are the fields `SeatRef`/`master_of` read; `with_retirement` is the terminal mark this policy gates access to. | `spawn_role`; `leaf_key`; `with_retirement` | [terminal_catalog.py](terminal_catalog.py) |
| `retire_entry`/`retire_seats_for_leaf` are the mechanics this policy gates: the manual path calls `check_retire_authority` before `retire_entry`; the automation hooks (`retire_seats_for_leaf`) bypass this policy entirely by design (an automated completion edge is not an actor seat — see that file's Invariants). | `retire_entry`; `retire_seats_for_leaf` | [retire.py](retire.py) |
| The leaf task doc's E1 code example matches `check_retire_authority` near-verbatim; the developer ruling on the authority split (manager lives outside its master stack, orchestrator holds the portfolio view) is recorded there. | Objective; Requirements; E1 | [../../../../../../../../../tasks/agents-remember/260707_hotfix-orchestration-stack/10_seat-retirement-and-chat-cleanup.md](../../../../../../../../../tasks/agents-remember/260707_hotfix-orchestration-stack/10_seat-retirement-and-chat-cleanup.md) |
| Failing-first tests for the exact authority matrix (manager-own-worker/reviewer ✓, other-master ✗, self-retire ✗ checked first, orchestrator-any-role ✓, unprivileged role ✗) and `master_of` segment extraction. | `RetirePolicyMatrixTests` | [../../../tests/test_seat_lifecycle.py](../../../tests/test_seat_lifecycle.py) |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No cross-repo boundary owns or consumes this local retire-authority policy. | — | — |

## Update History

- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat lifecycle: retirement, issue #12): the
  server-side retire authority policy — `SeatRef`, `master_of`, `check_retire_authority`,
  `RetirePolicyError`. Encodes the developer-ruled authority split: owner-never-self-retires
  checked first unconditionally; a manager retires only worker/reviewer seats of its own master
  (matched via `master_of(leaf_key)`); the orchestrator retires any seat. Verification metadata
  pinned until closeout stamps the HFX-L8 commit.
