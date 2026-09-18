# mcp/src/agents_remember/memory/knowledge/read_bindings.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/read_bindings.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The recorded fact set one observation is made from — the row's own five authored facts as they come back from the store.** | `RecordedBinding` | mcp/src/agents_remember/memory/knowledge/read_bindings.py:98-115 |
| **The one entry point: one binding in, exactly one state out, with the recorded key preserved.** | `observe_binding` | mcp/src/agents_remember/memory/knowledge/read_bindings.py:117-140 |
| **The declared observation order — the owner revision first, then the key form, then the locator and the target.** | `_observe_owner_and_key`; `_observe_locator_and_target` | mcp/src/agents_remember/memory/knowledge/read_bindings.py:142-168; mcp/src/agents_remember/memory/knowledge/read_bindings.py:170-196 |
| **The state-to-fact mapping, and the closed membership the closure counts.** | `STATE_FACTS`; `declared_state_members` | mcp/src/agents_remember/memory/knowledge/read_bindings.py:79-97; mcp/src/agents_remember/memory/knowledge/read_bindings.py:228-232 |
| The two key forms as recorded, and the tally the coverage record is built from. | `decode_local_key`; `key_forms_of` | mcp/src/agents_remember/memory/knowledge/read_bindings.py:247-253; mcp/src/agents_remember/memory/knowledge/read_bindings.py:234-245 |
| The owner-revision resolver this module observes through. | `OwnerRevisionResolver` | mcp/src/agents_remember/memory/knowledge/read_owner_revisions.py:95-153 |
| **The shipped anchor vocabulary the four shared literals must be members of, and the one-directional extension that gives it no citation member.** | `ANCHOR_RESOLUTIONS`; `AnchorResolutionState` | mcp/src/agents_remember/models/knowledge/read.py:112-130 |
| The closed binding vocabulary and its shipped subset. | `BINDING_STATES`; `SHIPPED_BINDING_STATES` | mcp/src/agents_remember/models/knowledge/citation.py:423-449 |
| **The cases that measure the identical shipped literal per shared fact and the one-directional extension, plus the uncovered-form state distinct from an absent key.** | `test_every_shared_fact_reports_the_identical_shipped_literal`; `test_the_binding_vocabulary_extends_the_shipped_one_only_in_one_direction`; `test_an_uncovered_key_form_is_a_counted_state_distinct_from_an_absent_key` | mcp/tests/test_knowledge_citation_bindings.py:201-285 |
| The boundary case that produces the uncovered form on a real store and asserts it distinct from the recorded-blob mismatch. | `test_an_uncovered_key_form_is_counted_and_reported_on_a_real_store` | mcp/tests/test_knowledge_citation_boundaries.py:729-835 |
| The boundary case that measures an unresolvable key keeping its recorded key and its attribution. | `test_a_key_absent_from_its_owner_revision_reports_the_shipped_mismatch_literal` | mcp/tests/test_knowledge_citation_boundaries.py:335-375 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the one-binding observation. It records the three rules that shape it and the reason each exists. **A shared fact reports the shipped literal** — four states are literally `ANCHOR_RESOLUTIONS` members, checked by a case rather than asserted, and the extension is one-directional so an anchor resolution can never acquire a citation fact. **The observation order is the order the facts depend on and it is declared**: the owner revision first (a key cannot be looked for in bytes that were not obtained), the key form next (a form the increment does not read is a fact about the *reader*, which is what keeps it distinct from an absent key), then the locator and the target. And **a key form this increment does not cover is a counted state, not a gap** — it is in the denominator and it makes the coverage partial. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
