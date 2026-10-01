# mcp/src/agents_remember/memory/knowledge/read_bindings.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Observe one recorded citation binding and report **exactly one** state from the closed vocabulary —
nothing dropped, nothing repaired, and the recorded key preserved on every state including the
failures.

## Code Commentary

### Logic

`RecordedBinding` is the recorded fact set as it comes back from the store; `observe_binding` returns
the one `CitationBindingObservation` it resolves to. The observation order is the order the facts
depend on, and it is declared rather than incidental:

1. `_observe_owner_and_key` resolves the **owner revision first**, because a key cannot be looked for
   in bytes that were not obtained; a revision the object store cannot produce reports
   `recorded_object_unavailable`.
2. The **key form** follows, because a form this increment does not read is a fact about the *reader*
   rather than about the corpus — reporting it before any lookup is what keeps `uncovered_key_form`
   distinct from "the key is absent".
3. The **locator** and then the **target** follow, because the locator is a property of the record
   this leaf wrote while the target is a fact about the store it points into.

`STATE_FACTS` states the one mapping from state to fact, and `declared_state_members` exposes the
closed set. `decode_local_key` decodes either recorded key form, and `key_forms_of` tallies the forms
the recorded bindings actually use so the closure's coverage record can be built.

### Invariants And Boundaries

- **A shared fact reports the shipped literal, not a binding-local spelling.** `exact_recorded_blob`,
  `recorded_blob_mismatch`, `recorded_object_unavailable` and `unsupported_locator` are literally
  members of the shipped `ANCHOR_RESOLUTIONS`; cases assert that membership rather than assuming it.
  The vocabulary extends **one-directionally** — `AnchorResolutionState` gains no member.
- **A key form this increment does not cover is a state, not a gap.** `COVERED_KEY_FORMS` declares the
  `cit:` body alone, so a table-row key reports `uncovered_key_form`, counted in the denominator like
  every other unresolved state and making the view's coverage partial.
- **The recorded key is preserved on every state**, which is the shipped rule for a stored
  attribution: a missing source is never a reason to retire one.
- Nothing here re-parses the corpus, searches for a plausible target, relocates a moved line,
  re-anchors a range, or consults a working tree or `HEAD` to fill a gap.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The recorded fact set one observation is made from — the row's own five authored facts as they come back from the store.** [1]
- **The one entry point: one binding in, exactly one state out, with the recorded key preserved.** [2]
- **The declared observation order — the owner revision first, then the key form, then the locator and the target.** [3]
- **The state-to-fact mapping, and the closed membership the closure counts.** [4]
- The two key forms as recorded, and the tally the coverage record is built from. [5]
- The owner-revision resolver this module observes through. [6]
- **The shipped anchor vocabulary the four shared literals must be members of, and the one-directional extension that gives it no citation member.** [7]
- The closed binding vocabulary and its shipped subset. [8]
- **The cases that measure the identical shipped literal per shared fact and the one-directional extension, plus the uncovered-form state distinct from an absent key.** [9]
- The boundary case that produces the uncovered form on a real store and asserts it distinct from the recorded-blob mismatch. [10]
- The boundary case that measures an unresolvable key keeping its recorded key and its attribution. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
