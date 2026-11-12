# mcp/src/agents_remember/application/knowledge_worklist/marks.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The two worklist kinds the marks raise (MIK-R118 rule 7, MIK-R124 rule 5).** When a task changes the
code a weakness is anchored to, its worklist holds one `weakness_anchor` row asking whether the weakness
still stands, and the row is answered by the leaf's own record row about the weakness. When a task
changes a document that has a dependent record, its worklist holds one `changed_document` row, and only
the confirmed record answers it: a `no_impact` row does not. Both items are raised from the memory base,
so a weakness or a dependent this task itself records is new and raises nothing.

## Code Commentary

### Logic

- **`weakness_anchor_items`** walks the base tree's weakness records, keeps the open ones whose anchor
  path this task changed, and emits one item per weakness carrying the path, the weakness kind, the
  recorded anchor content and the question. A closed weakness raises no fresh maintenance obligation.
- **`changed_document_items`** walks the base tree's dependents and emits one item for each whose
  document this task changed. With the candidate's own file map, a document the candidate no longer holds
  raises nothing, while a document renamed from its recorded path keeps its identity and the item names
  the path it now stands at.
- **Registration.** Both kinds register their subject pattern, their facts, the row that satisfies them
  and their owner in the item-kind registry; the package `__init__` imports this module, so the kinds
  exist wherever the worklist does.
- **`mark_items`** returns both kinds' items for one run, each raised once.

### Conventions

- A `weakness_anchor` item is **advisory**: it is information for the curator and a gate does not refuse
  for it. A `changed_document` item is not advisory: a changed document whose record is not confirmed is
  an open obligation like any other.
- An item's identity is derived from the record's revision and the path it concerns, so a second run over
  an unchanged base produces the same item rather than a new one.

### Invariants And Boundaries

- **A weakness refuses nothing.** No row of this kind refuses a review, a gate, a quality check or a
  closeout, and an open weakness is not a finding.
- **A document's item is answered only by its confirmation.** A `no_impact` row leaves it open, because
  the obligation is that the record was confirmed at this task's tip, not that the change was judged
  irrelevant.

### Todos

- None.

## Evidence

- The two kinds are registered with their satisfying row and their owner, and the advisory flag is stated
  on the weakness kind alone.
