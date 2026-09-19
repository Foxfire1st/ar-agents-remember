# mcp/src/agents_remember/memory/knowledge/citation_closure.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/citation_closure.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The declared selected set and its one addressing, which is what the counts are over.** | `selected_set_of`; `selected_set_key` | mcp/src/agents_remember/memory/knowledge/citation_closure.py:125-134; mcp/src/agents_remember/memory/knowledge/citation_closure.py:136-140 |
| **The read of the recorded bindings plus their sealed revisions, and the store-damage refusal that keeps an attribution out of no denominator.** | `load_recorded_bindings`; `_BindingStoreDamage` | mcp/src/agents_remember/memory/knowledge/citation_closure.py:142-155; mcp/src/agents_remember/memory/knowledge/citation_closure.py:327-340 |
| **The closure itself: the bound checked before any item is emitted, the shipped refusal returned with the bound reached.** | `assemble_citation_closure` | mcp/src/agents_remember/memory/knowledge/citation_closure.py:182-232 |
| **The per-binding enumeration L21's census counts — a read path, not a second store.** | `enumerate_recorded_bindings` | mcp/src/agents_remember/memory/knowledge/citation_closure.py:157-180 |
| The one observation per item, and the target's recorded facts read out of the store. | `_observe_one`; `_reported_target`; `_target_facts`; `_revision_facts` | mcp/src/agents_remember/memory/knowledge/citation_closure.py:234-269; mcp/src/agents_remember/memory/knowledge/citation_closure.py:271-295; mcp/src/agents_remember/memory/knowledge/citation_closure.py:297-304; mcp/src/agents_remember/memory/knowledge/citation_closure.py:306-313 |
| **The counts partition, the declared coverage, and the limitations a partial coverage must name.** | `_counts`; `_coverage`; `_limitations` | mcp/src/agents_remember/memory/knowledge/citation_closure.py:378-396; mcp/src/agents_remember/memory/knowledge/citation_closure.py:398-408; mcp/src/agents_remember/memory/knowledge/citation_closure.py:410-436 |
| The deterministic order and the ambiguity decision over recorded key text. | `_binding_order_key`; `_ambiguous_binding_ids` | mcp/src/agents_remember/memory/knowledge/citation_closure.py:467-481; mcp/src/agents_remember/memory/knowledge/citation_closure.py:438-459 |
| The shipped bound refusal this module returns rather than inventing totals. | `selection_incomplete_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:159-176 |
| The declared selection bound the refusal names. | `SELECTION_ITEM_LIMIT` | mcp/src/agents_remember/models/knowledge/read.py:96-96 |
| The one observation the closure delegates to. | `observe_binding` | mcp/src/agents_remember/memory/knowledge/read_bindings.py:117-140 |
| **The unit cases that measure the refusal, the absent completeness field, and the one-state-per-binding enumeration.** | `test_a_bound_closure_refuses_with_selection_incomplete_and_the_bound_reached`; `test_the_closure_states_no_semantic_completeness_and_reports_its_declared_coverage`; `test_the_enumeration_returns_every_recorded_binding_with_exactly_one_state` | mcp/tests/test_knowledge_citation_bindings.py:433-552 |
| The boundary case that proves a rewritten document leaves the binding stale and never re-bound. | `test_a_rewritten_document_leaves_the_binding_stale_and_never_re_bound` | mcp/tests/test_knowledge_citation_boundaries.py:248-305 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The one object store it touches is the
memory repository, and it touches it only to resolve the recorded identity each binding already holds.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: `test_a_rewritten_document_leaves_the_binding_stale_and_never_re_bound` repointed to mcp/tests/test_knowledge_citation_boundaries.py:248-305. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the closure read. It records the five properties the module enforces rather than documents, because each is a way a closure could lie: counts are over the **declared selected set** rather than over history or presumed prose; the bound is checked **before any item is emitted**, so a refusal never arrives beside a truncated closure; `unresolved` and `stale` are separate limitations and the per-state counts must partition the set, so an unresolved key cannot leave its denominator; there is **no semantic-completeness field**, only declared coverage and a `partial_key_form_coverage` limitation; and a stale binding stays readable and attributed and is **never re-bound** — no resolver here relocates a line or picks a target by similarity. The card also records that a binding whose sealed revision is missing is a *store defect* that raises rather than being reported as a missing target, because that report would silently drop an attribution out of a denominator. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
