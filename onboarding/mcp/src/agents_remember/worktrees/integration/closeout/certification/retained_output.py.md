# mcp/src/agents_remember/worktrees/integration/closeout/certification/retained_output.py

## Governing Overview

[Selected closeout certification overview](overview.md)

## Purpose

Recognizes the selected generation's physically proven code commit while preserving every other original candidate authority.

## Code Commentary

### Logic

`_require_original_code_proof` validates the retained mutation journal and the current physical commit before comparison. `_require_original_prestate` requires both accepted and pre-command snapshots to match the original staged candidate. The outer owner then permits only the exact code-output authority movement.

A successful code commit changes the checkout HEAD and its leaf lineage tip without changing the certified candidate tree. `require_retained_output_currentness` accepts that change only for retained same-generation recovery with a `commit-proven` code mutation, complete accepted/before/observed snapshots, the matching recovery commit, exact repository and original expected output tree.

Both retained pre-states must match the frozen head/ref, original head tree and staged candidate. A fresh physical mutation snapshot must equal the recorded observation, and the existing commit-intent owner must prove the actual commit. Exactly one original leaf code edge may move. The permitted comparison changes only that descendant tip, checkout HEAD and their derived candidate digests; all remaining owner and candidate fields must still equal the frozen admission.

### Conventions

This is a comparison against proven output, not a rewritten selected record. It publishes nothing and leaves original authority records, certificates and provenance intact.

### Invariants And Boundaries

- Unproven commits, altered parents/trees, ambiguous owned lineage edges and unrelated authority movement refuse.
- The admitted exception covers only the physically proven code output. It does not normalize memory/ledger publication, broaden source ownership or authorize finalization.
- Candidate content remains exact even after the logical checkout HEAD advances.

### Todos

None recorded.

## Evidence

### Docs References

The configured Domain Documentation registry has no entries. The source below establishes this repository-owned boundary.

The resolved registry supplies no applicable external Domain Documentation source for this card.

### Repo-Internal References

- The complete proof and closed authority comparison recognize only the selected code output. [1]

### Cross-Repo References

No cross-repository implementation or external protocol is owned here.


No separately configured cross-repository source is used for this card.
