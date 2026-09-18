# mcp/src/agents_remember/memory/migration/resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/migration/resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

Reference resolution with its three recorded states and the mechanical mismatch report — two rules,
and both are refusals of a capability rather than features of it. Resolution has exactly three states,
`resolved`, `unresolved` and `ambiguous`, and all three are reportable: none is a refusal of the run
and none is silently defaulted (`KS-R21@v1` §3.1). And **no reference is repaired by resemblance**
(§3.2): there is no fuzzy match, no prefix fallback, no canonicalisation step and no function that
creates a row to receive a dangling reference — `resolve_reference` compares exact spellings against a
caller-supplied candidate set and returns one of three values, so a reference that matched nothing
stays unmatched. The same boundary governs the report: a mismatch is reported as the mechanical fact
— which artifact, which reference, which baseline, what was observed to contradict what — and the
report has no field that could hold a semantic verdict. `Doc13:460` gives the four-way distinction
between an implementation defect, incorrect attribution, changed intent needing approval and an
unsupported claim to a **curator**, so §3.4 requires the pipeline to report *that* something is
contradicted and *where*, and never *which* of the four it is.

## Code Commentary

### Logic

**Exact string equality, and a missing kind is a state rather than an error.** `resolve_reference`
looks the reference's `reference_kind` up in the caller's mapping, takes that kind's admitted
spellings, and selects the candidates equal to `reference.reference_text` — no case folding, no
separator normalisation, no prefix test, and the docstring says so explicitly. One match resolves, no
match is `unresolved`, more than one is `ambiguous`. A kind with no entry in the mapping resolves to
`unresolved` rather than raising, because "this census knows nothing about that kind of reference" is
a fact worth reporting rather than an error that stops the run. `resolve_all` maps the same function
over an iterable in order; `count_resolutions` sums the three states into one `ReferenceCounts`.

**A resolution cannot contradict its own candidate set.** `Resolution.__post_init__` refuses three
combinations: `resolved` with anything other than exactly one candidate, `unresolved` carrying any
candidate at all, and `ambiguous` with fewer than two. Each refusal names the disagreement, so a state
and the evidence beside it cannot diverge — the class exists to make that pairing structural rather
than conventional.

**A reference is stored verbatim, with its origin and its baseline.** `Reference` carries the text,
its kind, the artifact path it was read from, the location within the artifact, and the
`FrozenBaseline` it was read at, and its docstring gives the reason the text is not normalised:
lower-casing, trimming separators or resolving a relative form against the artifact's own directory
would be the canonicalisation §3.2 forbids, "because a reference canonicalised into a match is a
reference that was repaired rather than resolved". The baseline type is imported from
`memory/migration/baseline.py`, so the same frozen identity every other census observation carries is
the one a resolution is compared against.

**Two non-resolved states, reported as two different kinds.** `mismatches_from_resolutions` turns an
`unresolved` resolution into a `declared_source_absent` mismatch and an `ambiguous` one into a
`route_reference_ambiguous` mismatch whose `observed` field states how many candidates it named. The
function's docstring gives the reason they are not collapsed: a reference that names nothing is not
the same observation as one that names two things, and collapsing them would hide the second — which
is the one indicating the census's own candidate set is wrong rather than incomplete.

**The packet's worked example, as one function.** `artifact_mismatches` reports
`declared_source_absent` when an artifact's declared source path is not present at the frozen
baseline, and returns nothing when the declaration is absent or the path is present. The comparison is
exact spelling against the set of present sources, and the docstring states that the fact is *not*
classified as a documentation defect or an implementation problem. `metadata_contradiction` returns a
`metadata_contradicts_front_matter` mismatch only when two **declared** values disagree — the path the
card declares and the path the pointed-at artifact declares — and `None` when they agree; nothing
about the code either file describes is read.

**The mismatch record has no verdict field, by construction.** `Mismatch` carries the kind, the
artifact path, the reference text, the baseline, and the `observed`/`expected` pair, and its docstring
states that the four dispositions `Doc13:460` names are a curator's authored work stored as that
curator's record, not here. `render` formats the mechanical fact, truncating both tree ids to twelve
characters so the line stays readable while remaining an exact identity. `render_report` sorts by
artifact path and then reference text before rendering, so two runs over the same corpus produce
byte-identical text and a difference between two reports is a real difference rather than a
reordering.

**One fact whose shape does not participate in the mismatch vocabulary.**
`duplicate_anchor_claims` takes an anchor-to-records mapping and returns the anchors with more than
one distinct claimant, sorted by anchor, as a tuple of `(anchor, records)` pairs. It shares the
module's discipline — it says *which* records disagree, not which of them is right — but it returns
its own shape rather than a `Mismatch`, so the `anchor_claimed_by_two_records` kind it corresponds to
is never constructed anywhere: the four `Mismatch(...)` call sites in the package build
`declared_source_absent`, `route_reference_ambiguous` and `metadata_contradicts_front_matter` only,
and the other three declared kinds (`anchor_claimed_by_two_records`, `cited_revision_absent`,
`artifact_unreadable`) occur exactly twice each in the package, in the `MismatchKind` literal and in
`MISMATCH_KINDS`. `iter_kinds` counts real mismatches over `MISMATCH_KINDS` and yields only the kinds
with a nonzero count, so it iterates the declared order without ever emitting a zero row.

### Conventions

The module is frozen dataclasses and module-level literal pairs: `ReferenceState`/`REFERENCE_STATES`
and `MismatchKind`/`MISMATCH_KINDS` each declare a `Literal` alias beside the runtime tuple of the
same members, and the comment above `ReferenceState` states why the pair exists — the vocabulary is
used at two sites, a single resolution and an aggregate count, and a second literal at the second site
is how two spellings of one state start to drift. Validation lives in `__post_init__` on the value it
protects, so a directly constructed `Resolution` cannot bypass it. Every refusal in the module is a
raised `ValueError` for a value that contradicts itself and a returned `Mismatch` for a fact observed
in a corpus — the two are never mixed. Private helpers carry a leading underscore and there is **no
`__all__`**, so the public surface is every name without one. `FrozenBaseline` is imported rather than
re-declared, and the module holds no store, no connection, no path and no state of its own: every
function is pure over its arguments.

### Invariants And Boundaries

- **No reference is repaired.** Comparison is exact string equality with no case folding, no separator
  normalisation, no prefix test and no canonicalisation, and there is no function anywhere in this
  module that creates a row to receive a dangling reference.
- **Three states, all reportable.** `resolved`, `unresolved` and `ambiguous` are all returned values;
  none raises, none is defaulted, and neither non-resolved state stops a run.
- **A state cannot contradict its candidates.** `Resolution` refuses `resolved` without exactly one
  candidate, `unresolved` with any, and `ambiguous` with fewer than two.
- **Unresolved and ambiguous are different facts.** They are reported as different mismatch kinds, and
  the ambiguous one carries its candidate count, so a wrong candidate set is not hidden inside a
  missing record.
- **No semantic verdict is offered or stored.** `Mismatch` has no field for one, and `render` emits the
  kind, the location, the baseline and the two observations — never one of `Doc13:460`'s four
  dispositions.
- **The report is order-independent.** `render_report` sorts before rendering, so a report's text
  depends on its contents and not on the order the facts arrived in.
- **A reference is never normalised into a match.** `Reference.reference_text` is stored verbatim with
  the artifact and location it was read from, so the observation stays addressable to its original
  text.
- **This module reads no code and no store.** It compares a caller-supplied candidate set against a
  caller-supplied spelling; it opens nothing, and the four mismatch constructors build a value from
  arguments rather than from a corpus they inspected themselves.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

This module is the census's reference half: it decides the three states a reference can be in, reports
the mechanical mismatches, and refuses every repair path. The rows below cite the two closed
vocabularies, the verbatim reference value, the self-checking resolution, the exact-match resolver, the
four mismatch constructors with the kinds they can and cannot build, and the deterministic report
renderers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of its two rules: three reportable states, and a refusal to repair a reference by resemblance. | `ReferenceState`; `MismatchKind`; `resolve_reference` | mcp/src/agents_remember/memory/migration/resolution.py:1-21; mcp/src/agents_remember/memory/migration/resolution.py:34-35; mcp/src/agents_remember/memory/migration/resolution.py:40-55 |
| The three resolution states as one closed vocabulary, kept as one pair because a second literal at the aggregate site is how two spellings drift. | `ReferenceState`; `REFERENCE_STATES` | mcp/src/agents_remember/memory/migration/resolution.py:29-35 |
| The six mechanical mismatch kinds, each a fact two observations disagree about and none a judgement about which is right. | `MismatchKind`; `MISMATCH_KINDS` | mcp/src/agents_remember/memory/migration/resolution.py:37-55 |
| The verbatim reference value with the artifact, the location and the frozen baseline it was read at. | `Reference`; `FrozenBaseline` | mcp/src/agents_remember/memory/migration/resolution.py:58-72; mcp/src/agents_remember/memory/migration/baseline.py:35-48 |
| The reason the reference text is not normalised: a canonicalised reference is one that was repaired rather than resolved. | `reference_text` | mcp/src/agents_remember/memory/migration/resolution.py:61-66 |
| The resolution value and the three refusals that keep a state from contradicting its own candidate set. | `Resolution` | mcp/src/agents_remember/memory/migration/resolution.py:75-98 |
| The mismatch record, which has no verdict field by construction because the four dispositions belong to a curator. | `Mismatch` | mcp/src/agents_remember/memory/migration/resolution.py:101-115 |
| The fact rendering, with both tree ids truncated for readability while the baseline stays an exact identity. | `render`; `code_tree_id` | mcp/src/agents_remember/memory/migration/resolution.py:116-123 |
| The three-state partition and the total that lets a caller check it accounts for every reference read. | `ReferenceCounts`; `total` | mcp/src/agents_remember/memory/migration/resolution.py:126-138 |
| The exact-match resolver: kind lookup, equality only, and an unknown kind resolved as `unresolved` rather than raised. | `resolve_reference` | mcp/src/agents_remember/memory/migration/resolution.py:141-158 |
| The order-preserving map over an iterable of references. | `resolve_all` | mcp/src/agents_remember/memory/migration/resolution.py:161-166 |
| The partition count over a set of resolutions. | `count_resolutions` | mcp/src/agents_remember/memory/migration/resolution.py:169-176 |
| Two non-resolved states reported as two different kinds, with the ambiguous one carrying its candidate count. | `mismatches_from_resolutions`; `declared_source_absent`; `route_reference_ambiguous` | mcp/src/agents_remember/memory/migration/resolution.py:179-212 |
| The packet's worked example as one function: a declared source path absent at the baseline, reported as the mechanical fact and not classified. | `artifact_mismatches`; `declared_source_absent` | mcp/src/agents_remember/memory/migration/resolution.py:215-243 |
| The contradiction between two declared values only, with nothing about either file's subject matter read. | `metadata_contradiction`; `metadata_contradicts_front_matter` | mcp/src/agents_remember/memory/migration/resolution.py:246-269 |
| The duplicate-anchor fact: which records disagree, never which of them is right, returned as its own shape rather than as a `Mismatch`. | `duplicate_anchor_claims` | mcp/src/agents_remember/memory/migration/resolution.py:272-285 |
| The report rendering, sorted by artifact and then reference so two runs over one corpus are byte-identical. | `render_report`; `render` | mcp/src/agents_remember/memory/migration/resolution.py:288-296; mcp/src/agents_remember/memory/migration/resolution.py:116-123 |
| The kind tally, walked in the declared kind order and never yielded at zero. | `iter_kinds`; `MISMATCH_KINDS` | mcp/src/agents_remember/memory/migration/resolution.py:299-305; mcp/src/agents_remember/memory/migration/resolution.py:48-55 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every comparison is between a
caller-supplied spelling and a caller-supplied candidate set, the only identity it reports is the
frozen baseline pair it was handed, and nothing here opens a store, reads a path or reaches another
repository, another dataset or a remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the census's reference-resolution and mismatch-reporting module. It records the two rules the module states as refusals — resolution has three reportable states and none stops a run, and no reference is repaired by resemblance, with no fuzzy match, prefix fallback, canonicalisation or row-creating path anywhere — together with the exact-equality comparison in `resolve_reference` and the unknown-kind case that resolves `unresolved` rather than raising. It records the self-checking `Resolution`, which refuses a state that contradicts its own candidate set in three directions, and the verbatim `Reference`, whose text is deliberately not normalised because a canonicalised reference is one that was repaired. It records the four mismatch constructors and the three kinds they can actually build, and the honest gap that follows: `anchor_claimed_by_two_records`, `cited_revision_absent` and `artifact_unreadable` are declared in `MismatchKind` and iterated by `iter_kinds` but constructed nowhere in the package, while `duplicate_anchor_claims` reports its fact in a shape that is not a `Mismatch` at all. It records the report's order-independence and the absence of any verdict field, since `Doc13:460`'s four dispositions belong to a curator. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
