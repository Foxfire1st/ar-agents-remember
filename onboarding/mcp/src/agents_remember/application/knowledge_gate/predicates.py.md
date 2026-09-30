# mcp/src/agents_remember/application/knowledge_gate/predicates.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_gate/predicates.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:09:38+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**Each registered worklist kind's own satisfying rule over a stored item (MIK-R09 rules 1, 2 and 7).** The gate
decides every item of the recomputed worklist through the predicate registered for its kind beside the kind registry,
never through a generic row lookup: kinds differ in what satisfies them (the carried obligations from L06, L10, L14
and L30, gathered by the start decision 2026-09-30T13:15:47). A predicate takes the item document and a
`GateContext` and returns why the item is still open, or `None` when an authored row (or, for an onboarding item, a
counted change) satisfies it. An item whose kind has no predicate is open.

## Code Commentary

### Logic

- **`GateContext`** holds what a predicate reads: the owner, the leaf's parsed history file in K_C, K_C itself as a
  `KnowledgeSide`, the opened code tree C, and `open_invariants` (the invariants whose invariant item is open, for the
  family rule). `rows_by_subject` maps each row subject to its row ID (the registrants' predicates take that map).
  `entry_state(entry_id)` observes a K_C entry's MIK-R03 state at C through `observe_entry` (`None` when K_C no longer
  holds it) and raises **`GitReadFailed`** when the observation is `read_failed`: an entry whose state could not be
  observed because a Git read failed or timed out is never decided (review R1 F9; the gate turns it into an
  `incomplete` finding).
- **`register_gate_predicate(kind, predicate)`** refuses a kind the MIK-R08 registry (`ITEM_KINDS`) does not know and
  a second registration. **`item_open_reason`** dispatches through `GATE_PREDICATES`; an unregistered kind is open
  ("no gate predicate is registered for the item kind …, so it cannot be answered").
- **Invariant rows (rule 2).** `required_covers` is the set a row must cover: for a `stale_invariant`, every entry
  its facts name (each is stale at base); otherwise every entry whose class is in `COVERING_CLASSES` (`touched`,
  `moved_or_absent`, `stale_at_base`); plus every `added`, `retired` and `reanchored` entry.
  `invariant_row_open` requires an `InvariantRow` about the subject, the required covers, a `revision` equal to the
  invariant's K_C revision, and every covered entry that still exists in K_C `current` at C (`_not_current` names
  each one that is not, with its MIK-R03 reason).
- **Family rows (rule 2).** `family_row_open` requires a `FamilyRow` about the family and then the first failing of:
  `_examined_set_reason` (`examined` equals the union of the family's K_B and K_C members, naming the unexamined and
  the extra), `_moved_members_reason` (every examined revision equals the member's K_C revision, or the member left
  K_C: "INV-BBBBBB (examined at 1, now 2)", D7) and `_uncovered_members_reason` (no member has an open invariant item).
- **The registrants' own predicates.** `family_route_condition` → `_route_condition_open` over
  `family_route_item_open(item, history)`, which finds the row by the item's **subject** `<FAM-ID>#<condition>`, so an
  item ID that changed between recomputes is answered by the same row (L06 review N2); its reason distinguishes a
  family record that does not satisfy MIK-R04 routes from a missing disposition. `onboarding_trace` →
  `onboarding_item_open` (a counted Markdown or sidecar change, or the `no_impact` row: the L30 carry);
  `unexplained_hunk` / `unexplained_file` → `unexplained_item_open`; `planned_untouched` → `planned_item_open`;
  `reconsideration_candidate` → `reconsideration_item_open` (an unanswered candidate blocks closeout, D29). The four
  row-map predicates are wrapped by `_by_rows`.
- Registration happens at import, for all ten kinds; the test asserts `set(GATE_PREDICATES) == set(ITEM_KINDS)`.

### Conventions

- Only authored rows satisfy items (rule 5); nothing here writes, and there is no waiver.
- The predicates check presence and currentness only; whether a disposition is right is the independent reviewer's
  (the packet's Exclusions).

### Invariants And Boundaries

- **Every kind is decided by its own predicate, and an undecidable item is open.** Realized by
  `register_gate_predicate`, `item_open_reason` and the ten registrations; proved by
  `test_every_registered_kind_is_decided_by_its_own_predicate_never_a_generic_lookup` (a counted onboarding change
  passes where `satisfying_row` finds nothing; two item IDs with one subject are answered by one `rerouted` row and
  both open under `no_impact`; an unknown kind is open).
- **Rule 2's currentness.** Proved by the packet's conforming, non-conforming ("covers one of two") and boundary
  ("edit again", "a sibling's revision rises from 3 to 4") examples in `test_knowledge_closeout_gate.py`, and on the
  real converted scratch (`gate-1` to `gate-4`).
- **A read that did not happen decides nothing.** `entry_state` raises `GitReadFailed` for a Git failure only; a code
  object that is persistently unavailable (a missing recorded blob, an unavailable grammar) is simply not `current`
  and keeps the item open with its named reason (review R2-3).

### Todos

- None.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: one predicate per kind, never a generic lookup. | "never through a generic row" | mcp/src/agents_remember/application/knowledge_gate/predicates.py:1-32 |
| What a predicate reads, and the entry state that raises on a failed read. | `GateContext`; `GitReadFailed` | mcp/src/agents_remember/application/knowledge_gate/predicates.py:77-114; mcp/src/agents_remember/application/knowledge_gate/predicates.py:73-74 |
| Registration and dispatch; an unregistered kind is open. | `register_gate_predicate`; `item_open_reason` | mcp/src/agents_remember/application/knowledge_gate/predicates.py:123-131; mcp/src/agents_remember/application/knowledge_gate/predicates.py:134-143 |
| The covers an invariant row must hold, and its currentness. | `required_covers`; `invariant_row_open` | mcp/src/agents_remember/application/knowledge_gate/predicates.py:155-171; mcp/src/agents_remember/application/knowledge_gate/predicates.py:183-202 |
| The family row's three reasons. | `family_row_open`; `_examined_set_reason`; `_moved_members_reason`; `_uncovered_members_reason` | mcp/src/agents_remember/application/knowledge_gate/predicates.py:210-254 |
| The route condition decided by subject. | `_route_condition_open` | mcp/src/agents_remember/application/knowledge_gate/predicates.py:273-279 |
| The ten registrations. | "register_gate_predicate(\"touched_invariant\", invariant_row_open)" | mcp/src/agents_remember/application/knowledge_gate/predicates.py:282-290 |
| The dispatch test. | `test_every_registered_kind_is_decided_by_its_own_predicate_never_a_generic_lookup` | mcp/tests/test_knowledge_closeout_gate.py:596-667 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:09:38+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): created this card for the new file MIK-R09 adds, recording the carried per-kind predicates (L06 Q7, L06 review N2, L10, L14 and D29, L30 review N6; start decision 13:15:47), review R1 F9 (`GitReadFailed`) and R2-3 (a code object that is unavailable is not a Git failure). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
