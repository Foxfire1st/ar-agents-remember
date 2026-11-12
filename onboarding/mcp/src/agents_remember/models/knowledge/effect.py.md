# mcp/src/agents_remember/models/knowledge/effect.py

## Governing Overview
[models route overview](../overview.md)

## Purpose
Declares the closed vocabulary of nine planned semantic-history effects.

## Code Commentary
`ADMITTED_EFFECT_LABELS` and `EffectLabel` declare exactly restore, clarify, introduce, strengthen, weaken, replace, split, merge and retire. There is no preserve label. A comparison does not infer an authored effect from the changes it observes.

A label alone supplies no predecessor or successor relationship; planned/history record models own those conditions. The canonical effect, preservation and unresolved-question payloads and their database writers were retired. The former EffectLabelLiteral name and add/narrow/widen/reincarnate vocabulary are not declarations of this module.

### Logic

**The effect vocabulary is closed, and it is spelled once.** `ADMITTED_EFFECT_LABELS` names the nine
labels in the source document's own order — `restore`, `clarify`, `introduce`, `strengthen`, `weaken`,
`replace`, `split`, `merge`, `retire` — and `EffectLabel` is the literal type built from exactly that
tuple, with a case asserting the two agree. So a synonym, a compound label, a free-text label and a
tenth member are **all the same refusal**: the payload does not validate. Code never derives a label
from anything — a comparison that observes a condition set growing does not make the effect
`strengthen`, and no field here could receive such a derivation.

## Evidence
### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- The declared tuple and EffectLabel carry the exact nine-member vocabulary, with no canonical payload or writer. [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file. A payload shape is a property of one
namespace's stored records, and every reference it carries is a store-local identity or opaque text.

No meaningful cross-repo references found.

- The nine admitted labels, in one declaration, and the literal type built from exactly that tuple. [15]
