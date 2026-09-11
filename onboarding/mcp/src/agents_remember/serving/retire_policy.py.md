# mcp/src/agents_remember/serving/retire_policy.py

| Field                  | Value                                                 |
| ---------------------- | ------------------------------------------------------ |
| repository             | agents-remember                                        |
| path                   | `mcp/src/agents_remember/serving/retire_policy.py`      |
| doc_type               | `file-level-onboarding`                                 |
| lastUpdated            | 2026-08-31T04:50+02:00 |
| lastVerifiedCommitHash | `f2b7c648f540efb9d64ceea22e11e651cb5cc914` |
| lastVerifiedCommitDate | 2026-08-31T15:32:32+02:00|
| governingOverview      | `overview.md`                                           |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

`retire_policy.py` is the server-side authority policy for seat retirement (260707-HFX-L8, issue
#12). It is the single place that decides WHETHER an actor seat may retire a target seat — the
developer-ruled authority split (a manager retires its own leaf execution seats and master-exit
reviewer; an architect retires only its architect-stamped plan reviewer; the orchestrator retires
any seat; no seat ever retires itself) is enforced here, not trusted from the
caller, and both the manual `session_retire` MCP tool / `POST /api/terminal/{session}/retire`
endpoint and any future retire entry point must route through `check_retire_authority` before
mutating the catalog. Completion-edge `landed` archive marking is not a retire entry point and is
documented in `serving/landing.py`.

## Code Commentary

### 260707-HFX2-L17 Pair-Based Retirement Authority

`SeatRef` carries the current document+role binding and the generation-bound reviewer-parent pair,
so retirement follows the task plane that owns the exact generation rather than immutable spawn
ancestry. A manager may retire worker/reviewer/curator seats on its leaves plus its same-master
reviewer. An architect may retire a same-sprint reviewer only when that reviewer explicitly names
the architect as structural parent; it cannot retire the orchestrator-owned super-exit reviewer at
the same canonical sprint address. The orchestrator retains portfolio-wide authority, and
owner-never-self-retires remains first.

### Logic

`SeatRef` is a frozen dataclass carrying the retirement-relevant structural facts about one catalog
seat: runtime generation, canonical document+role binding, and optional reviewer-parent
document+role. `check_retire_authority` resolves containment through `TaskDocumentTopology`; it does
not derive authority from path-string segments.

`check_retire_authority(actor, target)` raises `RetirePolicyError` unless `actor` may retire
`target`, in strict precedence order:
1. **Owner-never-self-retires, checked FIRST and unconditionally** — `actor.session_id ==
   target.session_id` raises before any role branch runs, so no role's authority can ever override
   it (verified directly: even an actor mis-tagged with `role="worker"` retiring itself still hits
   this branch first, per the test matrix in `test_seat_lifecycle.py`).
2. `actor.seat_role == "manager"` — permitted only for worker/reviewer/curator seats on direct
   leaves or the reviewer on the manager's own master.
3. `actor.seat_role == "architect"` — permitted only for a same-sprint reviewer whose generation
   is stamped with that architect as structural parent.
4. `actor.seat_role == "orchestrator"` — always permitted, portfolio-wide.
5. Anything else — refused with `"no retire authority"` in the message.

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
- The shared sprint reviewer address does not blur plan and super ownership: the current
  generation's structural-parent stamp decides which plane may retire it.
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
| `POST /api/terminal/{session}/retire` performs the identical authority check before calling `retire_entry`. | "def _retire_response("; "def _seat_ref(entry: TerminalCatalogEntry) -> SeatRef:" | mcp/src/agents_remember/serving/_app_terminal_routes.py:572-572; mcp/src/agents_remember/serving/_app_terminal_routes.py:632-632 |
| `TerminalCatalogEntry.binding_role` and `binding_task_document_ref` are the current structural identity fields `SeatRef` consumes; `with_retirement` is the terminal mark this policy gates. | "def binding_role(self) -> str:"; "def binding_task_document_ref"; "def with_retirement(" | mcp/src/agents_remember/models/terminal_catalog.py:420-420; mcp/src/agents_remember/models/terminal_catalog.py:558-558; mcp/src/agents_remember/models/terminal_catalog.py:568-568 |
| `retire_entry` is the mechanics primitive this policy gates for manual retire paths; `serving/landing.py` handles completion-edge landed archive marking separately because landing is not retirement. | `retire_entry`; `land_seats_for_task` | mcp/src/agents_remember/serving/landing.py:13-32; mcp/src/agents_remember/serving/retire.py:37-71 |


## Update History

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: replaced the obsolete
  path-segment authority description with topology-backed document/role ownership, added the
  architect-only plan-review rule, and recorded why the orchestrator-owned super reviewer is not
  architect-retirable. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `retire_policy.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
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
