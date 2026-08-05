# mcp/src/agents_remember/serving/retire_policy.py

| Field                  | Value                                                 |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/retire_policy.py`      |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-07-10T15:07+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`retire_policy.py` is the server-side authority policy for seat retirement (260707-HFX-L8, issue
#12). It is the single place that decides WHETHER an actor seat may retire a target seat — the
developer-ruled authority split (a manager retires only its own master's worker/reviewer/curator
seats; the orchestrator retires any seat; no seat ever retires itself) is enforced here, not trusted
from the
caller, and both the manual `session_retire` MCP tool / `POST /api/terminal/{session}/retire`
endpoint and any future retire entry point must route through `check_retire_authority` before
mutating the catalog. Completion-edge `landed` archive marking is not a retire entry point and is
documented in `serving/landing.py`.

## Code Commentary

### 260707-HFX2-L17 Pair-Based Retirement Authority

`SeatRef` now derives its master from binding leaf identity and carries `seat_role`, so retirement
authority follows the seat's current assignment rather than immutable spawn provenance. A manager
may retire worker/reviewer/curator seats in its own master, an orchestrator retains portfolio-wide
authority, and owner-never-self-retires remains first. Unbound failed dispatches recover their
master through `replacementForLeaf`. Reviewer O2 is a trust-model observation: because attach with
role is the operator's role-claim primitive, local callers can deliberately claim authority-bearing
roles; this matches the single-operator product boundary rather than adding hidden authorization.

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

## Repo-Internal References

`check_retire_authority` is called from both the manual retire paths and reads `SeatRef`s built
from `TerminalCatalogEntry` fields; the leaf task doc records the developer ruling this file
encodes.

| Finding | Anchor | Source |
| --- | --- | --- |
| `session_retire_payload` builds actor/target `SeatRef`s from `binding_role`/`binding_leaf_key` and calls `check_retire_authority` before any catalog mutation, translating `RetirePolicyError` into a `retire-refused` tool status. | `session_retire_payload` | mcp/src/agents_remember/mcp/tools/terminal.py:66-83 |
| `POST /api/terminal/{session}/retire` performs the identical authority check before calling `retire_entry`. | `_retire_response`; `_seat_ref` | mcp/src/agents_remember/serving/app.py:1754-1807; mcp/src/agents_remember/serving/app.py:1810-1817 |
| `TerminalCatalogEntry.binding_role` and `binding_leaf_key` are the current identity fields `SeatRef` consumes; `with_retirement` is the terminal mark this policy gates. | `binding_role`; `binding_leaf_key`; `with_retirement` | mcp/src/agents_remember/serving/terminal_catalog.py:359-384; mcp/src/agents_remember/serving/terminal_catalog.py:496-504; mcp/src/agents_remember/serving/terminal_catalog.py:506-510 |
| `retire_entry` is the mechanics primitive this policy gates for manual retire paths; `serving/landing.py` handles completion-edge landed archive marking separately because landing is not retirement. | `retire_entry`; `land_seats_for_leaf` | mcp/src/agents_remember/serving/landing.py:9-28; mcp/src/agents_remember/serving/retire.py:37-71 |
| Failing-first tests for the exact authority matrix (manager-own-worker/reviewer ✓, other-master ✗, self-retire ✗ checked first, orchestrator-any-role ✓, unprivileged role ✗) and `master_of` segment extraction. | `RetirePolicyMatrixTests` | mcp/tests/test_seat_lifecycle.py:103-166 |

## Update History

- 2026-08-04T11:39+02:00 — 260731-EFA-L6 S18-B13 curator: corrected curator-role authority and split retire/landing implementation ownership while removing stale task/domain/cross-repo claims.

- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: keyed authority on binding leaf plus seat role,
  extended own-master manager authority through curator, and made unbound failed dispatches
  master-resolvable through replacement leaf. Preserved reviewer O2 as a ruled trust-model note.

- 2026-07-09T14:05+02:00 — 260707-HFX2-L11 curator correction: clarified that this policy gates
  explicit retire entry points only; completion-edge success now routes through `serving/landing.py`
  and marks seats `landed` rather than bypassing policy through an automation retire helper.
  Verification metadata pinned until closeout stamps the HFX2-L11 commit.
- 2026-07-08T02:43+02:00 — Created for 260707-HFX-L8 (seat lifecycle: retirement, issue #12): the
  server-side retire authority policy — `SeatRef`, `master_of`, `check_retire_authority`,
  `RetirePolicyError`. Encodes the developer-ruled authority split: owner-never-self-retires
  checked first unconditionally; a manager retires only worker/reviewer seats of its own master
  (matched via `master_of(leaf_key)`); the orchestrator retires any seat. Verification metadata
  pinned until closeout stamps the HFX-L8 commit.
