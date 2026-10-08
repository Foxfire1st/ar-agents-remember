# mcp/src/agents_remember/application/knowledge_gate/predicates.py

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
  each one that is not, with its MIK-R03 reason). Since L37 (INV-XN0FG8) it also asks
  `changed_record_row_violation` with the item's `facts.record.baseRevision`: while the invariant's revision on the
  parent line differs from its K_C revision, the governing row is the `changed` row of that change, or the `deleted`
  row that retires it. A later `no_impact`, `moved` or `extended` row leaves the item open, and the reason says to
  restate the changed row.
- **Family rows (rule 2).** `family_row_open` requires a `FamilyRow` about the family and then the first failing of:
  `_hidden_guarantee_reason` (L37: when the item's `reachedBy` holds `guarantee-changed`, the row is `changed` or
  `retired`; a `no_impact`, `assigned` or `rerouted` row does not answer a family whose guarantee the leaf changed),
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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: one predicate per kind, never a generic lookup; while a record's revision differs from the parent line's, only its changed row governs. [1]

- What a predicate reads, and the entry state that raises on a failed read. [2]
- Registration and dispatch; an unregistered kind is open. [3]

- The covers an invariant row must hold, and its currentness. [4]
- The family row's four reasons: a hidden guarantee change, the examined set, moved members and uncovered members. [5]

- The route condition decided by subject. [6]
- The ten registrations. [7]
- The dispatch test. [8]

- An invariant the leaf changed is answered only by its changed row. [9]
- A family whose guarantee the leaf changed is answered only by its changed row. [10]

- Leaf-owned changed records retain their changed governing row across attempts. [11]


- A family guarantee changed by the leaf remains governed by that changed row. [12]


### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is crossed by this file.
