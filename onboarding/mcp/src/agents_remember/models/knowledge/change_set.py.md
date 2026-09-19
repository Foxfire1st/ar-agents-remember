# mcp/src/agents_remember/models/knowledge/change_set.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/change_set.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T10:31+02:00 |
| lastVerifiedCommitHash |  `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate |  2026-09-18T13:43:14+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l13` uncommitted staged source; base `b5a74aee6cdf671c9963f3aba4df6d44b856f697` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

`SemanticChangeSet`: the composed record of authored work, and the views it serves. This module owns the
change set's frozen payload shape and the derived read models — not the write path, and not a table. The
record is an envelope record like the members it composes, so it adds no table for itself, no second
identity mechanism and no second revision aggregate.

## Code Commentary

### Logic

**The declared composition is complete without a second copy of any member's identity.**
`SemanticChangeSetPayload` carries `baseline` and `candidate` (two exact `SnapshotIdentity` values,
copied from the comparison the author worked against), `requirement_revision_refs` (the opaque stored
references of the requirement clause) and `candidate_realization_claim_ids` (exact stored
`realization_claim` identities the change set *records* and does not author, endorse or widen). The
remaining two parts of the declared composition — proposed effects and preservation claims, plus
unresolved questions — are members that declare their **own** `change_set_id`, so the composition is
complete without the change set holding a second copy of an identity one of its members already
declares. Membership is therefore *computed* from the members rather than stored on the change set.

**Naming both sides is this leaf's conservative addition, and it is recorded as such.** A record that
named one side would be unreadable as a comparison, and a change set must not name a moving head — so
both snapshots are stored rather than resolved on read, and the record says what it was authored over
and not what happens to be current when it is read. A baseline and a candidate from two namespaces are
not two sides of one comparison, so `_require_one_namespace` refuses that at construction rather than
storing a change set nobody could read.

**The derived views are where the record group's *unresolved* states become readable.**
`UnresolvedReference` carries the holder (`holder_record_id`, `holder_revision_id`), the `field` the
reference is stored under — a closed four-member set — the reference **verbatim as it was written**, and
a reason. There is deliberately **no field for a resolved value**: this record group reports the absence
and resolves nothing, so a caller that wants the reference's meaning waits for the leaf that owns it.
That is how an unresolved assessment reference, an unresolved requirement-revision reference and an
unresolved preservation subject are all reported without being suppressed, substituted, resolved or
re-pointed.

**`predecessor_change_set_ids` on the view is what makes supersession addressable rather than
overwriting.** The succession edge lives in generation 8's `change_set_predecessor` table and is
inserted inside the successor's own creation batch, so a superseded change set stays readable and
addressable as its own record.

**`AuthoredEffectScope` is the whole namespace's authored work, and every part of it is derived.** Its
`detail` sentence counts what the read produced, and deleting it changes no claim, no question and no
change set — there is no second place for a value to live.

### Conventions

`EffectReadResult` is the typed outcome of one authored-effect read, and its validator enforces exactly
one outcome: a `refused` state carries its `refusal` and **no** scope, a `read` state carries its scope
and no refusal. So a caller never has to ask which half to read.

`EffectReadOperation = Literal["read_effect_scope"]` is declared here, beside the result it belongs to,
so the operation name and the result cannot disagree about which act ran. The change-set kind's
`(kind, schema)` pair is declared beside its model in `CHANGE_SET_PAYLOAD_MODELS`, the same shape every
other record group uses for its registry entry.

Every view is a pure function of rows the caller already read, which is why a rebuild over unchanged
rows reproduces it byte for byte.

### Invariants And Boundaries

- **A change set is superseded by a new record with a predecessor edge.** There is no in-place revision,
  no mutable "current version" pointer and no separately typed successor record: the successor is
  another `SemanticChangeSet` and the edge names the superseded one.
- **There is no field that could hold an inference.** No generated summary, generated narrative,
  computed effect list, severity, or display ordering computed from meaning — `extra="forbid"` is what
  refuses a payload arriving with one. The membership list `ChangeSetMembership` is the membership
  *fact* the design allows code to compute (which records belong to which change set); nothing in it is
  derived from a payload's content, and an empty list means exactly that no member declares this change
  set.
- **A change set is not a decision.** It carries no acceptance, no promotion and no merge verdict; it is
  authored work awaiting a curator's assessment and the Intent Reviewer's display.
- **`lifecycle` on a view is not a truth verdict.** It is the shipped `knowledge_record.lifecycle` state
  — `proposed` for every row this record group writes — and it answers one question only: was this
  stored as a proposal or as an accepted record.
- **A reference declared twice is one reference.** `_require_distinct_references` refuses a repeated
  requirement-revision reference or a repeated candidate realization claim, because a repeated reference
  is one reference stored once.
- **Nothing here writes.** The write path is `memory/knowledge/effects.py`; this module declares shapes
  and derives views, so a card that read it as an authority would be reading the wrong module.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The change set's kind and the one frozen shape it resolves to, declared as the registry's key. | `SEMANTIC_CHANGE_SET_KIND`; `SEMANTIC_CHANGE_SET_SCHEMA`; `CHANGE_SET_PAYLOAD_MODELS` | mcp/src/agents_remember/models/knowledge/change_set.py:66-66; mcp/src/agents_remember/models/knowledge/change_set.py:67-67; mcp/src/agents_remember/models/knowledge/change_set.py:134-136 |
| The record group's one served operation, named beside the result so the two cannot disagree about which act ran. | `EffectReadOperation` | mcp/src/agents_remember/models/knowledge/change_set.py:73-73 |
| The frozen payload: both snapshot identities, the opaque requirement references and the exact realization-claim identities — with no second copy of a member's identity. | `SemanticChangeSetPayload` | mcp/src/agents_remember/models/knowledge/change_set.py:76-136 |
| The two construction refusals: a baseline and candidate from different namespaces, and a reference declared twice. | `_require_one_namespace`; `_require_distinct_references` | mcp/src/agents_remember/models/knowledge/change_set.py:98-112; mcp/src/agents_remember/models/knowledge/change_set.py:114-130 |
| The unresolved-reference fact: the holder, the closed field set, the verbatim reference, and no slot for a resolved value. | `UnresolvedReference` | mcp/src/agents_remember/models/knowledge/change_set.py:139-158 |
| The three member views, each carrying the envelope's own lifecycle, route, provenance and content digest. | `InvariantEffectClaimView`; `PreservationClaimView`; `UnresolvedQuestionView` | mcp/src/agents_remember/models/knowledge/change_set.py:161-182; mcp/src/agents_remember/models/knowledge/change_set.py:185-198; mcp/src/agents_remember/models/knowledge/change_set.py:201-212 |
| The computed membership fact, with an empty list meaning exactly that no member declares this change set. | `ChangeSetMembership` | mcp/src/agents_remember/models/knowledge/change_set.py:215-225 |
| The change set's view, with all six declared parts readable and the stored successor-to-predecessor edges addressable rather than overwritten. | `SemanticChangeSetView` | mcp/src/agents_remember/models/knowledge/change_set.py:228-250 |
| The whole derived scope and the outcome that carries it — the scope or one refusal, never both. | `AuthoredEffectScope`; `EffectReadResult` | mcp/src/agents_remember/models/knowledge/change_set.py:253-267; mcp/src/agents_remember/models/knowledge/change_set.py:270-287 |
| The `extra="forbid"` base these shapes derive from, which is what refuses a generated summary or a severity field. | `model_config` | mcp/src/agents_remember/models/knowledge/base.py:34-37 |
| The snapshot identity both sides of the comparison are stored as, which the envelope does not otherwise carry. | `SnapshotIdentity` | mcp/src/agents_remember/models/knowledge/candidate.py:185-206 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A payload shape and its derived views are
properties of one namespace's stored records.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:31+02:00 — 260915-KS-L13 curator (uncommitted change set on `ar/260915-ks-l13`, base `b5a74aee`): created this one-to-one card for the semantic change set's payload and its derived views. It records the complete declared composition without a duplicated member identity, the computed membership fact, the successor-as-new-record rule, the unresolved-reference shape that has no slot for a resolved value, and the deliberate absences (no generated summary, no severity, no acceptance or promotion verdict). This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. Naming the base commit there would be a verification claim about a tree the code never had; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
