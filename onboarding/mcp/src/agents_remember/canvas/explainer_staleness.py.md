# mcp/src/agents_remember/canvas/explainer_staleness.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Which blocks and which parts of a retained page read stale against one target comparison, and the order a trusted view and a judgment sort state them in.

## Code Commentary

- The module is pure: it takes the revision's manifest and claim map, one target comparison and the leaf's grades, and answers data through a small read protocol the caller implements, so no file is written and no Git command is run here.
- `keeps_fingerprint_across_a_line_shift` states the locator rule: a symbol keeps its text across a shift, a line range keeps it while its recorded blob is held, and a file locator moves with any change to the file.
- `BlockFingerprint` is either computed or names why it is not, and constructing one with neither or with both raises, so an unread block cannot be carried as current.
- `basis_stale` answers one sentence per basis kind and treats an unknown kind, or a claim with no basis at all, as stale — nothing is called current because it could not be read.
- `part_staleness` names every part holding a stale claim, and falls back to the whole page for a revision whose part map is absent, does not name its own claim ids, or strands a stale claim outside every part.
- `judgment_order` sorts one subject's blocks by grade, highest first, ties in the order given, and keeps ungraded blocks last under their own count; a stale grade sorts by its value and keeps its mark.

## Evidence

- The locator kind alone decides whether a fingerprint survives a line shift [1]
- A fingerprint carries either a value or the reason it has none, never both and never neither [2]
- An unknown basis kind, or a claim with no basis, is stale whenever any side of the comparison moved [3]
- A revision without a usable part map is stale as a whole, so no part is named that does not hold the claim [4]
- A grade whose block changed or cannot be fingerprinted is stale, with that reason [5]
- Subjects keep their order; inside one, blocks sort by grade with ties kept and ungraded last [6]
