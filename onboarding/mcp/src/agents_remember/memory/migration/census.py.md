# mcp/src/agents_remember/memory/migration/census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/migration/census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The read and assembly side of the truth-coverage census: it takes the census records a run wrote
through the shipped candidate operation and produces one `CensusReport`, and it writes nothing.
It computes nothing the record kinds do not already carry, and its one deliberate absence is stated
in its own docstring: there is **no code path here that derives the coverage denominator from the
corpus**. `build_report` takes the reference inventory's size as an argument or the coverage measures
are reported unmeasured. The denominator's own source is a separate, independently reviewed input
(`KS-R21@v1` §5.3) whose author assembles it from code examination, accepted requirements, family
guarantees and incidents — sources outside the corpus being measured — and which someone other than
its author reviews; until that review exists `C / K` is not publishable, and `CR21-6` makes a missing
reviewer seat a **blocked** condition rather than a figure to publish with a placeholder, so the
predicate refuses rather than warns.

## Code Commentary

### Logic

**Assembly from three reads and two numbers, and nothing else.** `build_report` reads the inventory
rows, the claims and (through `disposition_report`) the dispositions — all through
`memory/knowledge/census_records.py` — and populates one `CensusReport`. The module's own comment
says the arithmetic plainly: this function "reads three census tables and takes the denominator as an
argument, and those are the only two sources of a number in it". It never opens a connection, never
issues a write statement, and holds no store of its own; the `OpenedKnowledgeStore` it is handed is
only ever passed to the record group's readers.

**The reviewed inventory is a gate in two forms, so a boolean cannot be forgotten.** `C / K` may be
published only from an inventory that has a reviewer and a reviewer who is not its author;
`require_independent_reviewer` refuses both failures with a raised `ValueError`, and its own
docstring gives the single reason they share — `Doc12:110` requires review by *someone other than its
author*, so an inventory reviewed by its own author has had no independent review whether or not a
name is present. `coverage_is_publishable` is the boolean form that returns `False` for a missing
inventory, for an inventory with no reviewer and for a self-reviewed one; `published_inventory` is the
narrowing form, and `build_report` calls that one so the coverage measures can only ever receive a
reviewed inventory or `None` — never an unreviewed one a later branch could still reach through a
test pyright cannot follow.

**The review state is derived, never passed.** `reference_inventory` computes `reviewed` versus
`awaiting-independent-review` from whether a reviewer is named, so an inventory cannot claim
`reviewed` while naming nobody: the two facts are computed together. The five reference source
classes are a closed vocabulary that deliberately excludes the corpus — `code-examination`,
`accepted-requirement`, `family-guarantee`, `incident`, `other-evidence` — because a denominator drawn
from the thing being measured omits exactly the missing truths the measure exists to find.

**The corpus-derived assertion is declared but never read.** `ReferenceInventory.corpus_derived` is
declared as `Literal[False] = False`, and its docstring says it is "a recorded *assertion* by the
author, not something this module can verify", recorded so that a false one becomes a finding against
a named author. Nothing in the shipped candidate contradicts that intent, but the honest current
state is narrower: the name occurs exactly twice in the package, in that docstring and in the field
default, it is absent from `ReferenceInventoryDraft` — so `reference_inventory` cannot carry a
caller's value through — and no function in this module, this package or the test suite reads it.
The assertion is therefore always `False` and nothing is checked against it.

**The coverage numerator is a literal zero, and the gate is an identity test.** `_represented_truths`
returns `0` when an independently reviewed inventory exists and `None` when it does not; there is no
branch that could count against the corpus, and the function's argument is already the published
inventory, so it cannot be handed an unreviewed one. `_known_realizations` counts the realization
relations the claims stored with `attribution_state == "attributed"` — read out of the records, never
derived from a code reading, because `missing_realization` is a state the census records as visible
rather than one it computes.

**Only recorded associations become slice keys.** `_slice_keys` returns each claim's recorded key on
one axis and nothing derived: `category` is the curator's authored `claim_kind`, and `source_route` is
the envelope's explicit `governing_route_id` — "recorded and never inferred from a path prefix or a
directory name" — while `family` and `consequence` have no carrier in this record group and so report
the `unrecorded` state. The asymmetry is visible in the result rather than hidden: `_slices` iterates
all four axes, but for the two axes with no mapping every member falls to the axis's own unrecorded
key, so those slices are one bulk slice each rather than a breakdown. `_occurrences_of` builds one
`ClaimOccurrence` per extracted claim in stored order, skipping a claim whose text is blank, and
`_slices` is handed the whole claim sequence while `slice_claims` re-applies the cohort filter — so
the slices partition exactly the cohort even though the argument is broader.

**What the report carries out.** `CensusReport` carries the baseline key it was given, the
`Separation`, the six measures, both occurrence counts, the four axes' slices, the inventory counts by
parse outcome, and the reference inventory's id and reviewer (or `None` for both when no inventory was
passed). `disposition_report` returns the migration dispositions by kind through
`disposition_counts`, which is the path that keeps the `unmapped` bucket visible.

### Conventions

The module is dataclasses over imported vocabulary, not a second model layer: `ReferenceTruth`,
`ReferenceRealization`, `ReferenceInventory`, `ReferenceInventoryDraft` are `@dataclass(frozen=True)`
here, while the record shapes it assembles (`CensusReport`, `ClaimOccurrence`, `SliceReport`,
`Separation`, the `SliceAxis` and `CellName` literals, `COHORT_APPLICABILITY`,
`CLASSIFIED_CLAIM_KINDS`) are imported rather than re-declared — the two vocabularies it branches on
come from `models/knowledge/census.py` and it re-spells neither. Everything that is not an intended
export is module-private with a leading underscore (`_occurrences_of`, `_slice_keys`, `_slices`,
`_represented_truths`, `_known_realizations`), and the module declares **no `__all__`**, so its public
surface is every name without a leading underscore in the file. Two axis arguments carry a
`# type: ignore[arg-type]` where the loop variable is a plain string tuple rather than the imported
`SliceAxis` literal — the one place the module crosses its own vocabulary boundary with an explicit
marker rather than a second literal declaration. `census_records` is imported as the module object
(`census_records.read_inventory_rows`) so the reader's owner stays visible at every call site, and
`CensusDispositionKind` is imported purely as the type annotation for the local in
`disposition_counts`.

### Invariants And Boundaries

- **No denominator is ever derived from the corpus.** `build_report` reads three census tables and
  takes the reference inventory's size as an argument; the absence of the inventory's review is
  reported as an unmeasured coverage measure, not as an estimate.
- **An unreviewed inventory is unreachable, not merely unrecommended.** `published_inventory` is the
  only way `build_report` obtains an inventory to measure against, and `_represented_truths` accepts
  nothing but its result, so no coverage figure can be computed from an unreviewed list.
- **Nothing here writes.** The module issues no statement at all: every read is delegated to
  `census_records`, and the only value it produces is a `CensusReport`.
- **No slice key is inferred.** `family` and `consequence` report `unrecorded` rather than being
  derived from a path prefix or a directory name, and the route axis reads the envelope's recorded
  `governing_route_id` association; a slice keyed by a guess would report a scope axis the substrate
  does not have.
- **No semantic verdict is computed.** `T`, `F` and `U` come from a curator's authored assessment as
  recorded on the claim's evidence; this module reads the cell a claim is already in and never
  produces one.
- **A missing reviewer is a refusal, not a warning.** `require_independent_reviewer` raises for a
  settled-seat-less inventory and for one whose reviewer is its own author, and
  `coverage_is_publishable` converts both to `False` rather than to a figure with a caveat.
- **The review state cannot disagree with the reviewer.** `reference_inventory` derives the state from
  the presence of a reviewer, so `reviewed` with no reviewer is not a constructible value.
- **No second identity scheme.** Every row this module reports carries the record id, route id and
  baseline the envelope and the records already store; the module mints no digest and no name.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This module is the census's read and assembly half: it answers the record group's readers and produces
the report the measures module renders, and it owns the one predicate that decides whether a coverage
figure may exist at all. The rows below cite the report assembly and its two numeric sources, the
review gate in both of its forms, the derived review state, the recorded-only slice keys, and the
record vocabulary and readers it imports rather than re-declares.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of its division: the read side of the census, with no code path that derives the coverage denominator from the corpus. | `build_report`; `CensusReport` | mcp/src/agents_remember/memory/migration/census.py:1-17 |
| The reference inventory's closed source vocabulary, which deliberately excludes the corpus the denominator is measured against. | `ReferenceSource`; `REFERENCE_SOURCES` | mcp/src/agents_remember/memory/migration/census.py:51-64 |
| The two states a reference inventory's review seat can be in, and the reason `reviewed` is the only publishable one. | `ReviewState` | mcp/src/agents_remember/memory/migration/census.py:43-46 |
| The corpus-derived assertion the record declares but no shipped path reads: the field exists as a `Literal[False]` default and is absent from the draft, so nothing carries or checks a caller's value. | `ReferenceInventory` | mcp/src/agents_remember/memory/migration/census.py:86-107 |
| The two denominators the inventory owns, read as its truth count and its realization count. | `size`; `realization_count` | mcp/src/agents_remember/memory/migration/census.py:109-119 |
| The reviewer gate: an unsettled review seat and a reviewer who is the author are refused by the same check, because `Doc12:110` requires review by someone other than the author. | `require_independent_reviewer` | mcp/src/agents_remember/memory/migration/census.py:121-138 |
| The boolean form of the gate: false for a missing inventory, a missing reviewer and a self-reviewed one. | `coverage_is_publishable` | mcp/src/agents_remember/memory/migration/census.py:172-186 |
| The narrowing form: the only way to obtain an inventory to measure against is through the gate, so a forgotten boolean test cannot reach an unreviewed one. | `published_inventory` | mcp/src/agents_remember/memory/migration/census.py:189-197 |
| The derivation, rather than acceptance, of the review state: `reviewed` is computed from a named reviewer, so the two facts cannot disagree. | `reference_inventory`; `ReferenceInventoryDraft` | mcp/src/agents_remember/memory/migration/census.py:141-169 |
| The coverage numerator: a literal zero while an independently reviewed inventory is supplied, and no branch that could count over the corpus. | `_represented_truths` | mcp/src/agents_remember/memory/migration/census.py:306-315 |
| The realization attribution count, read out of the claims' stored relations rather than derived from any code reading. | `_known_realizations` | mcp/src/agents_remember/memory/migration/census.py:318-331 |
| One occurrence per extracted claim, built in stored order with the blank-text case skipped. | `_occurrences_of` | mcp/src/agents_remember/memory/migration/census.py:200-213 |
| The recorded-only slice keys: the authored claim kind, the envelope's explicit governing-route association, and the `unrecorded` state for the two axes this record group has no carrier for. | `_slice_keys` | mcp/src/agents_remember/memory/migration/census.py:216-235 |
| The four axes iterated, each slice re-filtered to the cohort inside the slice builder rather than by the caller. | `_slices` | mcp/src/agents_remember/memory/migration/census.py:238-254 |
| The assembly itself, with the published inventory narrowed once and the denominator taken as an argument, and the `unmapped`-visible disposition path on the same module's public surface. | `build_report`; `disposition_report`; `disposition_counts` | mcp/src/agents_remember/memory/migration/census.py:257-303; mcp/src/agents_remember/memory/migration/census.py:334-337; mcp/src/agents_remember/memory/migration/census_measures.py:531-543 |
| The read helpers this module is handed the store for, and the stored-schema check that refuses a row whose envelope disagrees with its declared schema. | `read_inventory_rows`; `read_claims`; `read_dispositions`; `_require_declared_schema` | mcp/src/agents_remember/memory/knowledge/census_records.py:750-778; mcp/src/agents_remember/memory/knowledge/census_records.py:781-829; mcp/src/agents_remember/memory/knowledge/census_records.py:832-891; mcp/src/agents_remember/memory/knowledge/census_records.py:722-731 |
| The eligibility rule and the cell reader the assembly applies, and the report vocabulary it fills from the imported model rather than restating. | `claim_enters_cohort`; `cell_of`; `COHORT_APPLICABILITY`; `CensusClaim`; `CensusInventoryRow` | mcp/src/agents_remember/memory/migration/census_measures.py:265-277; mcp/src/agents_remember/memory/migration/census_measures.py:487-507; mcp/src/agents_remember/models/knowledge/census.py:100-103; mcp/src/agents_remember/models/knowledge/census.py:41-41; mcp/src/agents_remember/models/knowledge/census.py:376-383 |
| The evidence relation that carries a curator's authored verdict and its absence-as-`unassessed` state, which is what makes `P` derivable without being invented. | `CensusClaimEvidence`; `CensusClaimRealization` | mcp/src/agents_remember/models/knowledge/census.py:239-257; mcp/src/agents_remember/models/knowledge/census.py:260-271 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every read it performs goes to the one
knowledge store it is handed, every identity it reports is a store-local row identity or a declared
vocabulary member, and nothing here reaches another repository, another dataset or a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the census's read-and-assembly module. It records the report assembly that reads three census tables through `census_records` and produces one `CensusReport` while issuing no statement of its own, and the two — and only two — sources of a number in it: the reads and the denominator passed as an argument. It records the publishability gate in its three shapes, the raising `require_independent_reviewer`, the boolean `coverage_is_publishable` and the narrowing `published_inventory`, together with the derived-not-passed `reviewed` state and the five closed reference source classes that exclude the corpus. It records the coverage numerator as a literal zero that cannot count over the corpus, the realization count read out of the claims' stored `attributed` relations, the stored-order occurrence builder that skips blank text, and the recorded-only slice keys where `family` and `consequence` honestly report `unrecorded` instead of a derived key. It records the deliberate absences as well: no write, no digest of its own, no inferred route association, no verdict, and no `__all__`. It also records the one honest gap it found — `corpus_derived` is declared as an always-`False` literal, is absent from the draft that `reference_inventory` accepts, and is read by nothing in the package, so the author's assertion is recorded nowhere and checked against nothing. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
