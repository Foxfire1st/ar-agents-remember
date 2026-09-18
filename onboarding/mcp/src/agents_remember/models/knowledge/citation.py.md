# mcp/src/agents_remember/models/knowledge/citation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/citation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T06:05+02:00 |
| lastVerifiedCommitHash | `15fe8678fc0f87eaac4606952f179135ebe392c4` |
| lastVerifiedCommitDate | 2026-09-18T07:49:45+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l18` uncommitted source; base `e963a01c` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../../../overview.md)

## Purpose

The `CitationBinding` vocabulary: what a prose citation binds, and every state one binding
observation resolves to. It declares the **prose owner revision**, the **local citation key as
written**, the **typed target reference** and the **locator inside the target's recorded scope**,
together with the closed nine-member state set, the counts validator, the key-form coverage record
and the closure request/result pair.

## Code Commentary

### Logic

`ProseOwnerRevision` is the memory repository, the document's repository-relative confined POSIX
path and the **recorded Git blob identity** of that document — the shipped `GitBlobIdentity`
convention `models/knowledge/source.py` already uses for "these exact recorded bytes", not a digest
scheme invented here. The identity is *referenced and not minted*: it names an object the memory side
already supplies, and the read path addresses that object rather than hashing whatever the file now
contains.

`ProseCitationKey` stores the key in two halves plus the written source, and `TableRowKeyForm` is the
second, recognized form; `KEY_FORMS` declares both and `COVERED_KEY_FORMS` declares only
`prose_cit_body` — so a table-row key is *present and recognized* and resolves to
`uncovered_key_form` rather than being folded into "absent". `render_local_key` is the one rendering
of either form. `WrittenSource` keeps the prose's own `path:start-end`, which is what makes "target
reference and locator" carried rather than lost.

`CitationTargetReference` is a typed identity (record id, declared kind, optional exact revision),
and `CitationBindingPayload` composes the four facts. `BINDING_STATES` is the closed nine-member
vocabulary; four of its members are *literally* members of the shipped `ANCHOR_RESOLUTIONS` and
`SHIPPED_STATE_FACTS` plus `shipped_literal_for` state that mapping once. `models/knowledge/read.py`
deliberately gains **no** member: the extension is one-directional, so an anchor resolution can never
acquire a citation fact.

`CitationBindingCounts` refuses a report that omits a declared state or whose per-state counts do not
partition the declared selected set — that is the mechanism by which an unresolved key cannot be
dropped from a denominator. `KeyFormCoverage` refuses to leave an uncovered form uncounted, and
`CitationBindingClosureResult` carries limitations and coverage and **no** semantic-completeness
field.

### Invariants And Boundaries

- **Nothing here is a content address, a logical digest or a fingerprint.** `payload_digest` stays on
  the revision aggregate that owns it; a binding is not an identity of the prose it cites. Ambiguity
  ("more than one binding claims one key in one owner revision") is detected by equality over the
  *recorded key text*, which is the fact at issue, not by a computed digest that would have to be
  kept in step with it.
- **The locator is the shipped `SourceLocator` union**, imported rather than reduplicated, so a
  binding-local locator spelling is inexpressible rather than merely unwritten. A recorded locator
  stays readable when no resolver supports it, which is why `unsupported_locator` is a reported state
  and not a write refusal.
- **A rewritten key is a different key.** The key is stored as its parts, not as one flattened
  string, so whether the anchor text, the file or the extent moved stays distinguishable.
- **The state vocabulary is closed and exhaustive.** `BINDING_STATES` names every member; a state
  that cannot be populated today is still a counted member with a zero entry.
- This module holds no store handle and writes nothing: it is the vocabulary the write path, the read
  path and the closure all speak.

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
| **The owner revision as a referenced and not minted identity: repository, confined document path, and the recorded Git blob identity the memory side already supplies.** | `ProseOwnerRevision` | mcp/src/agents_remember/models/knowledge/citation.py:144-192 |
| The written source the prose itself carries, and the ordered-range refusal that keeps it readable. | `WrittenSource` | mcp/src/agents_remember/models/knowledge/citation.py:194-213 |
| **Both key forms, the declaration of which form this increment reads, and the one rendering of either.** | `ProseCitationKey`; `TableRowKeyForm`; `KEY_FORMS`; `COVERED_KEY_FORMS`; `render_local_key` | mcp/src/agents_remember/models/knowledge/citation.py:215-255; mcp/src/agents_remember/models/knowledge/citation.py:257-278; mcp/src/agents_remember/models/knowledge/citation.py:282-289; mcp/src/agents_remember/models/knowledge/citation.py:292-299; mcp/src/agents_remember/models/knowledge/citation.py:301-321 |
| The typed target reference and the authored payload that composes the binding's four facts. | `CitationTargetReference`; `CitationBindingPayload` | mcp/src/agents_remember/models/knowledge/citation.py:323-351; mcp/src/agents_remember/models/knowledge/citation.py:353-374 |
| **The closed nine-member state vocabulary, the four members that ARE shipped literals, and the one mapping that states which fact each reuses.** | `BINDING_STATES`; `SHIPPED_BINDING_STATES`; `SHIPPED_STATE_FACTS`; `shipped_literal_for` | mcp/src/agents_remember/models/knowledge/citation.py:423-439; mcp/src/agents_remember/models/knowledge/citation.py:441-449; mcp/src/agents_remember/models/knowledge/citation.py:451-457; mcp/src/agents_remember/models/knowledge/citation.py:459-486 |
| **The counts validator that refuses a report whose per-state counts do not partition the declared selected set, and the coverage record that refuses to leave an uncovered form uncounted.** | `CitationBindingCounts`; `KeyFormCoverage` | mcp/src/agents_remember/models/knowledge/citation.py:554-590; mcp/src/agents_remember/models/knowledge/citation.py:491-518 |
| The observation, the indivisible closure item, the closure request and the result that carries limitations and no semantic-completeness field. | `CitationBindingObservation`; `CitationBindingItem`; `CitationBindingClosureRequest`; `CitationBindingClosureResult` | mcp/src/agents_remember/models/knowledge/citation.py:520-536; mcp/src/agents_remember/models/knowledge/citation.py:538-552; mcp/src/agents_remember/models/knowledge/citation.py:592-604; mcp/src/agents_remember/models/knowledge/citation.py:606-626 |
| The shipped source identity this vocabulary references instead of minting a second one. | `GitBlobIdentity`; `SourceIdentity` | mcp/src/agents_remember/models/knowledge/source.py:29-36 |
| The one locator union the binding must use, and the shipped anchor vocabulary the four shared literals come from. | `SourceLocator`; `ANCHOR_RESOLUTIONS`; `AnchorResolutionState` | mcp/src/agents_remember/models/knowledge/source.py:76-86; mcp/src/agents_remember/models/knowledge/read.py:112-130 |
| The declared selection bound the closure's refusal names. | `SELECTION_ITEM_LIMIT` | mcp/src/agents_remember/models/knowledge/read.py:96-96 |
| **The cases that measure the closed vocabulary in both directions, the shipped-literal identity, the counts partition and the uncovered-form state.** | `test_the_closed_vocabulary_and_its_facts_agree_in_both_directions`; `test_every_shared_fact_reports_the_identical_shipped_literal`; `test_a_count_report_refuses_an_aggregate_that_dropped_a_key_from_the_denominator`; `test_an_uncovered_key_form_is_a_counted_state_distinct_from_an_absent_key` | mcp/tests/test_knowledge_citation_bindings.py:1-679 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A binding is a fact about a memory
document and a knowledge record, and neither identity space carries a repository boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T06:05+02:00 — 260915-KS-L18 curator (uncommitted change set on `ar/260915-ks-l18`, base `e963a01c`): created this one-to-one card for the `CitationBinding` vocabulary `KS-R18@v1` introduces. It records the four facts a binding names and the decision that shapes all of them — **the owner revision is referenced, never minted**: the recorded identity is the memory side's own Git blob identity for "these exact recorded bytes", so the read path addresses that object instead of hashing whatever the file now holds. It records that both key forms are declared while only the `cit:` body is *read*, so an uncovered form is a counted state with a named coverage limitation rather than a silent gap; that four of the nine states are *literally* shipped `ANCHOR_RESOLUTIONS` members and that `AnchorResolutionState` deliberately gains no member; and that a binding carries **no** content address, digest or fingerprint, with ambiguity decided by the recorded key text. Verification metadata advances to the leaf's base commit `e963a01c` because every cited construct was re-read against the working tree; the code commit does not exist yet and closeout owns that stamp.
