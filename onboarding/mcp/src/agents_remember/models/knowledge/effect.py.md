# mcp/src/agents_remember/models/knowledge/effect.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

Declares the closed vocabulary of nine planned semantic-history effects.

## Code Commentary

`ADMITTED_EFFECT_LABELS` and `EffectLabel` declare exactly restore, clarify, introduce, strengthen, weaken, replace, split, merge and retire. There is no preserve label. A comparison does not infer an authored effect from the changes it observes.

A label alone supplies no predecessor or successor relationship; planned/history record models own those conditions. The canonical effect, preservation and unresolved-question payloads and their database writers were retired. The former EffectLabelLiteral name and add/narrow/widen/reincarnate vocabulary are not declarations of this module.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- The declared tuple and EffectLabel carry the exact nine-member vocabulary, with no canonical payload or writer. [13]
