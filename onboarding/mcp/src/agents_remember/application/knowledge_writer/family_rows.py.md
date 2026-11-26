# mcp/src/agents_remember/application/knowledge_writer/family_rows.py

## Governing Overview

[mcp/src/agents_remember/application/overview.md](../overview.md)

## Purpose

Read persisted `reached_family` worklist facts and build family history rows aligned with the knowledge gate's member rules: admitting an empty or omitted `examined` list for an empty family and stamping the base revision for a member that left `K_C`.

## Code Commentary

### Worklist facts extraction

`reached_family_facts` scans the persisted worklist's `items` for entries with `kind == "reached_family"`, a string `subject`, and a list `facts.members`. For each such item, it stores a frozen `ReachedFamilyFacts(empty=not members, base_revisions=_base_revisions(members))` keyed by family ID.

`_base_revisions` maps each mapping entry in `facts.members` whose `id` is a string and whose `base` is an exact `int` (`type(base) is int`, rejecting booleans) with `base >= 1` to that integer base revision. Missing, `None`, boolean, or non-positive base values are ignored.

### Empty-family admission

`build_family_row` first runs `family_effect_refusal(request, row["subject"])`; any effect problem is recorded at `<where>.effect` and returns `None`. It then looks up `family_facts = authoring.reached_family_members.get(row["subject"])`. When `request.examined` is empty (either `[]` or omitted in the hand-off), `_allows_empty_examined(record, family_facts)` admits it only when both:

- `family_facts` is present and `family_facts.empty` is true (`facts.members == []` in the persisted `reached_family` item), and
- the produced family `record.get("members")` is a list or tuple of length 0.

Family status is not part of the check, so active and retired empty families are treated identically. A family with no `reached_family` item, an owner with no worklist (such as a wave), a family with members on either side, or a family that gained a member in the same write batch is refused with `"a family row names every member the curator examined"`.

### Examined member resolution

`_resolve_examined` resolves each requested member name through `authoring.resolve_id(one, where)` and looks it up in `authoring.state.record(member)`:

- If `member` is stored in the candidate as an `"invariant"`, its candidate revision is stamped (`{"id": member, "revision": found[2].get("revision")}`).
- Only when `found is None` (the member is absent from `K_C`) and `family_facts` is present, `_resolve_examined` checks `family_facts.base_revisions.get(member)`. If a base revision `>= 1` exists there, it stamps `{"id": member, "revision": base_revision}`.
- Any other name (unknown ID, stored non-invariant record, or absent member without a base revision `>= 1` in the worklist facts) records `"examined member <one!r> is not a stored invariant"`.

`build_family_row` stamps `row["revision"] = record.get("revision")` and copies `request.effect` when present, returning the row dictionary for `FamilyRow.model_validate` in the caller.

## Relationships

- Called from `HistoryRowAuthoring._family_row` in `authoring_rows.py`, which supplies the produced family record and runs `FamilyRow.model_validate` on the returned dictionary.
- `writer.py` (`write_knowledge`) calls `reached_family_facts(request.worklist)` and passes the map into `Authoring.reached_family_members` in `authoring.py`.
- Delegates effect admission to `family_effect.family_effect_refusal`.
- Aligns writer family-row construction with the unchanged gate predicate (`application/knowledge_gate/predicates.py::family_row_open`) and worklist member facts (`application/knowledge_worklist/compute.py`), without altering the gate, models, or extra non-member invariant admission.

## Evidence

- `reached_family_facts` and `_base_revisions` extract empty-member status and integer `base >= 1` revisions from persisted `reached_family` worklist items. [1]
- `build_family_row` and `_allows_empty_examined` run effect refusal first and admit empty or omitted `examined` only when both worklist `facts.members` and the produced family record have no members. [2]
- `_resolve_examined` stamps candidate invariant revisions first, falls back to persisted worklist base revisions `>= 1` only when absent from `K_C`, and preserves the stored-invariant refusal otherwise. [3]
- `HistoryRowAuthoring._family_row` delegates row construction to `build_family_row` and validates the built `FamilyRow`, while `write_knowledge` wires `reached_family_facts(request.worklist)` into `Authoring`. [4]
