# mcp/src/agents_remember/memory/knowledge/citation_closure.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The selected prose view's citation closure, and the readable per-state enumeration a census counts.
This module reads **recorded bindings and recorded targets**, and nothing else.

## Code Commentary

### Logic

`selected_set_of` takes the exact prose owner revisions a view declares, and `selected_set_key` is the
one addressing of one revision. `load_recorded_bindings` reads the `citation_binding` rows together
with each binding's sealed `record_revision` payload, and `_recorded_binding` rebuilds the whole
recorded fact from them; a binding whose sealed revision is missing raises `_BindingStoreDamage`
rather than being reported as "the target is missing" — that would answer a question about the store
with a claim about the binding while silently dropping an attribution out of a denominator.

`assemble_citation_closure` checks the declared bound **before** emitting any item and returns the
shipped `selection_incomplete` refusal with the bound reached, so no caller ever holds a truncated
closure beside a total it did not compute. Each surviving item is observed once, by `_observe_one`
through the read path, and `_reported_target` plus `_target_facts`/`_revision_facts` resolve the
target's recorded kind, lifecycle, authority home and schema. `_counts` partitions the declared
selected set by state; `_coverage` reports the declared key-form coverage; `_limitations` renders the
`partial_key_form_coverage` limitation for every uncovered form.
`enumerate_recorded_bindings` is the per-binding enumeration L21's census counts — a read path over
the recorded rows, not a second store.

`_binding_order_key` fixes the deterministic order (document path, blob id, key form, binding id) and
`_ambiguous_binding_ids` decides ambiguity by equality over the **recorded key text**.

### Invariants And Boundaries

- **Closure is part of the view**, and counts are over the *declared selected set* — never over all
  history and never over presumed actual prose.
- **A bounded closure refuses rather than truncates**, using the shipped `selection_incomplete`
  refusal, and the refusal precedes any item.
- **Unresolved and stale travel as separate limitations, and the counts partition the set.** An
  unresolved key cannot be dropped from its denominator; a state that totals zero is still a declared
  member.
- **There is no semantic-completeness field.** The result exposes limitations and declared coverage
  instead of presenting itself as complete.
- **A stale binding is readable and attributed, and it is never re-bound.** No resolver here
  relocates a moved line, re-anchors a range, or picks a target by similarity, filename or prose
  search; a curator authors the re-binding.
- Nothing here re-parses the corpus, consults a working tree or `HEAD`, or searches for a plausible
  target. The shipped precedent is the anchor reader's own *no locator search and no line
  re-anchoring*.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The declared selected set and its one addressing, which is what the counts are over.** [1]
- **The read of the recorded bindings plus their sealed revisions, and the store-damage refusal that keeps an attribution out of no denominator.** [2]
- **The closure itself: the bound checked before any item is emitted, the shipped refusal returned with the bound reached.** [3]
- **The per-binding enumeration L21's census counts — a read path, not a second store.** [4]
- The one observation per item, and the target's recorded facts read out of the store. [5]
- **The counts partition, the declared coverage, and the limitations a partial coverage must name.** [6]
- The deterministic order and the ambiguity decision over recorded key text. [7]
- The shipped bound refusal this module returns rather than inventing totals. [8]
- The declared selection bound the refusal names. [9]
- The one observation the closure delegates to. [10]
- **The unit cases that measure the refusal, the absent completeness field, and the one-state-per-binding enumeration.** [11]
- The boundary case that proves a rewritten document leaves the binding stale and never re-bound. [12]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The one object store it touches is the
memory repository, and it touches it only to resolve the recorded identity each binding already holds.

No meaningful cross-repo references found.
