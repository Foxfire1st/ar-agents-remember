# mcp/src/agents_remember/application/review_leaf_facts.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Compose the child run’s two reviewer fact blocks beside its worklist result.

## Code Commentary

`leaf_facts` returns serialized code_changes from code_changes(trees, classification) and item_states from worklist_answers(document, trees, classification). It forwards the same exact run-scoped classification to both existing owners, adds no rule of its own and persists nothing. Their unavailable/undecided or unbound results remain distinct from an empty successful fact set.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. Requirement packets are task authority, not an implementation proof or a fresh acceptance.

### Repo-Internal References

- The child joins the shared code-fact and gate-verdict owners with the same held run context. [1]
