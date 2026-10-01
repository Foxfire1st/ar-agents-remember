# review_unchanged_knowledge.py

## Governing Overview

[overview.md](overview.md)

## Purpose

Prepare and retain a legitimate live review for explicitly declared code-only work with unchanged published knowledge.

## Code Commentary

### Logic

freeze_unchanged_knowledge_review resolves the live leaf through `_dataset_resolution` and reads the knowledge dataset at its exact recorded memory base. Since L37 (the L23 F8 carry, MIK-R37 rule 3) `_dataset_resolution` refuses a converted leaf first: a resolution that carries `trees` or `knowledge_unavailable` returns `review_comparison_freeze.tree_comparison_refusal()` before the memory base or any dataset is read, so the frozen database of a converted tree is never selected. The helper is a realization of INV-T9M21FB4. The published dataset and any task halves must have that same identity. A captured snapshot is admitted through prepare_curator_candidate and the existing original-baseline placement owner; freeze_resolved_review then records the normal comparison. Named refusals preserve missing, changed, corrupt and unpublished knowledge distinctions.

### Conventions

Use the existing owner interfaces and exact recorded identities; keep transient task evidence outside durable onboarding.

### Invariants And Boundaries

The operation authors no invariant or assessment and publishes no knowledge dataset. It must preserve the first comparison baseline and may not substitute an empty or current unrelated dataset.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No Domain Documentation source is configured. The implementation-specific account is grounded in the repository source below.

No configured domain source could be checked.

### Repo-Internal References

The named constructs own this behavior; reads and validation use their existing callers and models.

- `freeze_unchanged_knowledge_review` owns the behavior described above. [1]
- `_unchanged_inputs` owns the behavior described above. [2]
- `_place_pair` owns the behavior described above. [3]

- The leaf's dataset pair, or the refusal of an unresolved or converted leaf. [4]
- No read selects the database of a converted tree. [5]

### Cross-Repo References

No independent cross-repository interface is introduced by this source.

No additional cross-repository evidence is required.
