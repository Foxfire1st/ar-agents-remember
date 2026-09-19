# mcp/src/agents_remember/models/knowledge/census.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/census.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T17:00+02:00 |
| lastVerifiedCommitHash |  `2dcacb27446ecbaba01b69ee32e2ac40a1713b09`|
| lastVerifiedCommitDate |  2026-09-18T17:26:34+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l21` uncommitted staged source; base `a7076008db4772554123794392f84b51143004ec` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

The truth-coverage census's frozen record vocabulary: the inventory row, the claim and the disposition,
with the three typed relations a claim or a disposition resolves through. This module owns the three
census record kinds' payload shapes **and nothing else** — it is a `models/` module because these shapes
cross the wire: a census row is read back by the census's own reporting surface and by the reviewer
surface that presents it. The docstring names three load-bearing properties, each a property of the
declared fields rather than of a rule a caller remembers: **there is no field that could hold an
inference** (no classification the parser could have computed, no verdict, no mismatch class, no derived
status), **provenance is a required stored value rather than a report note**, and **no record carries an
identity of its own beyond its key** — there is no content address, no logical digest and no fingerprint
field here, and the schema declares no such column, because the census mints no second identity
authority and the content digest stays on `record_revision` where the record envelope puts it. A
semantic status such as *supported*, *contradicted* or *unresolved* is a curator's authored assessment,
"read by the census and never written by it".

## Code Commentary

### Logic

**Six stable names, and one registry key per record kind.** Three pairs of constants spell the envelope's
typed kind and the frozen schema it resolves to — `census_inventory_row` /
`census-inventory-row/v1`, `census_claim` / `census-claim/v1` and `census_disposition` /
`census-disposition/v1` — and the comment beside them records that the names are "this implementation's
reading of `Doc12:49-55` rather than quotations of doc-defined type names, which the packet records as a
fact about itself". `CENSUS_PAYLOAD_MODELS` is the `(kind, record_schema) -> frozen model` mapping this
group contributes, **declared here rather than beside the write path** because "a payload shape is
vocabulary: the registry that decides admissibility reads it, and the record group that stores it reads
the same declaration rather than a second one that could drift"; `record_envelope.PAYLOAD_MODELS`
unpacks it. `CENSUS_COMMAND_KINDS` is the three command names as one `frozenset` and
`CENSUS_RECORD_KINDS` the three record kinds as another, so a registry case names the group instead of
restating its literals. `CENSUS_WRITABLE_TABLES` is the eight tables a census command writes — the two
envelope tables plus the three record tables and the three relations — each declared by the generation
that registers the census's kinds; `candidate_records` subtracts the envelope pair to append the group's
own six to the batch's writable-table union.

**Twelve closed vocabularies, and the one member that is an absence rather than a kind.** Twelve
`Literal` aliases are declared in one block — `CensusArtifactKind`, `CensusParseOutcome`,
`CensusInventoryState`, `CensusClaimKind`, `CensusApplicability`, `CensusDispositionKind`,
`CensusDispositionState`, `CensusEvidenceState`, `CensusAssessmentDisposition`,
`CensusRealizationState`, `CensusLinkKind` and `CensusTargetState` — and their values are spelled here
while `schema_v9` declares the matching tuples the DDL renders into `CHECK ... IN` lines, so the two
are the same set of admitted values by construction. `CensusClaimKind` is the one that carries five
members: `unclassified`, `current_behavior`, `accepted_invariant`, `historical_rationale` and
`realization_attribution`. `CLASSIFIED_CLAIM_KINDS` is "`Doc12:65-70`'s taxonomy as the four kinds the
taxonomy actually names, in the doc's own order", and `unclassified` "is deliberately not a member: it is
the *absence* of a kind", so a caller that asked for "one of the four" is never handed the state that
means none of them. `COHORT_APPLICABILITY` is the single applicability value that enters the claim
cohort `N` — `assessable` — and the comment states why it is a named constant: the eligibility rule is
required to be stated so that `Doc12`'s Example 3 and requirement 5.2 read alike.

**Provenance is required on every record, and it carries the baseline by identity.** `CensusProvenance`
is the one provenance shape all three record kinds declare: `artifact_path` repository-relative and
stored verbatim (normalising it "would be the census editing its own evidence"), `location` as the
address within the artifact — "a line for a claim, a section heading for a piece of a route overview" —
which is what makes a claim addressable to its original text, a required `baseline`, an optional
`observed_content_digest`, and an optional `author`. `baseline` is a `SnapshotIdentity` rather than two
loose strings "because the frozen baseline *is* one" — the exact code revision and exact memory revision
recorded by identity — and it is required rather than optional because "an observation with no baseline
is an observation against a moving target": two artifacts examined at two baselines are two observations,
which is why the baseline is part of the record rather than a parameter of the run that produced it.

**Two construction refusals, each closing a way a row could look like coverage without being it.**
`_require_relative_artifact_path` refuses an absolute path or one containing a backslash, and refuses any
path with an empty, dot or traversal segment, on the ground that such a spelling "is not a second
spelling of one artifact -- it is a path this census never observed, and admitting it would put a machine
location in a durable record".
`_require_unparsed_content_with_a_failed_parse` ties the parse outcome to the evidence in both
directions: a parsed artifact carrying `unparsed_content` is refused because "a stored unparsed remainder
on a parsed artifact would report a section as unread that was read", and an outcome other than `parsed`
with no content is refused because "an outcome with no evidence is indistinguishable from no row". The
payload it guards exists for exactly that reason: `unparsed_content` is "the exact observed content the
parser could not interpret", stored on the row rather than in a side channel because "a silent skip is
indistinguishable from coverage".

**The relation shapes record states rather than deriving them.** `CensusClaimEvidence` carries
`evidence_state` defaulting to `unassessed` and an optional `assessment_disposition`; `unassessed` "is
derivable because no assessment row exists", while the other two states "are not derived by anything in
the pipeline — they are set only where a curator's authored assessment resolves the reference", and the
module "deliberately offers no function that computes one from an import outcome". The absent
`assessment_disposition` is the unassessed state "rather than a fourth disposition", so a claim with no
assessment is `P` and never a claim whose verdict defaulted to something.
`CensusClaimRealization` is what the realization-coverage measure counts, and `missing_realization` "is
the state that measure exists to make visible, and it is recorded rather than computed so that 'the
realization is absent' stays distinguishable from 'nobody looked'".
`CensusDispositionLink` makes `Doc12:55`'s "links to the resulting new records, including claims that
are split, combined, retired, or corrected" four link kinds rather than a prose note, and carries
`target_state` verbatim, so "a link to a record that does not exist is reported as `unresolved` and is
never repaired by resemblance or satisfied by creating a record to receive it".

**The commands carry no author, no instant and no verdict; the read-back types carry the envelope's
facts.** Each of the three commands names its own `kind` literal, a `record_id` and a `revision_id`, its
payload, and an optional `governing_route_id` — optional on purpose, because "an inventory row exists for
a surface whether or not the substrate has a `Route` record for it, and an absent route is the recorded
`absent` state rather than a reason the row cannot exist", and "that asymmetry is what lets the census
see a route with no onboarding -- the row is the finding". `CensusClaimCommand` additionally carries the
claim's `evidence` and `realizations` tuples, and `CensusDispositionCommand` its `links` tuple, because
"the links travel inside the creation batch rather than through a second operation, so a disposition and
the records it produced are written whole or not at all". `CensusInventoryRow`, `CensusClaim` and
`CensusDisposition` are the read-back shapes: the records' own `record_id` and payload plus the
envelope's `lifecycle` (`Literal["proposed", "accepted"]`) and `governing_route_id`, with the relations
attached for the claim and the disposition.

### Conventions

Every shape is a `KnowledgeModel` subclass, so `extra="forbid"` and `frozen=True` inherited from
`models/knowledge/base.py` are what refuse a payload arriving with an undeclared field — which is the
mechanism the docstring names when it says no census payload can hold an inference. Bounded text reuses
the base constants rather than literals: `REFERENCE_MAX_LENGTH` for a path, an evidence or realization
reference, a target reference and an observed content digest, `LABEL_MAX_LENGTH` for a location, a claim
or disposition id and a governing route id, and `PROSE_MAX_LENGTH` for a claim's original text, the
unparsed content and a rationale. Declarations that must agree are one declaration:
`COHORT_APPLICABILITY` is the single literal that spells the cohort value and `CensusClaimPayload`
defaults its `applicability` to it; `CENSUS_PAYLOAD_MODELS` is the one mapping from `(kind, schema)` to
model, and the six kind/schema constants it is built from are the same ones the registry keys on;
`CENSUS_COMMAND_KINDS` and `CENSUS_RECORD_KINDS` are each declared once as a `frozenset` derived from the
literals the commands and kinds already spell; and `CENSUS_WRITABLE_TABLES` is the group's own table list
declared here rather than beside the write path. The one shape from another module is imported rather
than re-declared: `SnapshotIdentity` from `models/knowledge/candidate.py`, with `Authorship` from
`models/knowledge/authorship.py`. The module declares **no `__all__`**; its public surface is the
constants, the twelve vocabulary aliases, the seven payload-or-relation models, the three commands, the
three read-back records and the three group declarations, and its only private member is the validator
`_require_relative_artifact_path`.

### Invariants And Boundaries

- **No field here could hold an inference.** `claim_kind` admits only `unclassified` and the four kinds
  `Doc12:65-70` closes the taxonomy at; `disposition` admits the seven migration states; none of them is
  a verdict about whether a claim is true, and `extra="forbid"` refuses a payload arriving with one.
- **A semantic status is not this module's to write.** `CensusClaimEvidence.assessment_disposition` is
  optional and "stored verbatim from the curator's own record", and no function here computes one from an
  import outcome; its absence is the unassessed state, never a fourth disposition.
- **No record carries an identity beyond its key.** There is no content-address, logical digest or
  fingerprint field, and no such column is declared; the content digest stays on `record_revision`.
- **Provenance is required on all three record kinds.** A `CensusProvenance` names the artifact, the
  location within it and the frozen baseline, and the baseline is a `SnapshotIdentity` rather than two
  loose strings.
- **No machine location enters a durable record.** `_require_relative_artifact_path` refuses an absolute
  or backslash spelling and any empty, dot or traversal segment.
- **An unparsed outcome must carry what was not parsed, and a parsed one must carry nothing.**
  `_require_unparsed_content_with_a_failed_parse` closes both directions, so an outcome with no evidence
  cannot pass for a row that was examined.
- **A route is optional and an absence is never conflated with a missing route.** All three commands
  default `governing_route_id` to `None` rather than requiring one, which is what lets an inventory row
  exist for a surface the substrate has no `Route` record for.
- **The command carries no author and no instant.** Authorship "comes from the admission, so no part of a
  submitted payload can become the claim's author", and `claim_kind` starts at `unclassified` for every
  extracted claim because assigning one of the four classified kinds is authored work with an author and
  an instant.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below ground the card's claims in the declarations themselves: the six kind-and-schema names,
the closed vocabularies with the cohort value and the classified-kind tuple, the provenance every record
requires, the two construction refusals, the relation shapes, the three commands, the read-back records
and the three group declarations the registry and the batch consume.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of its three load-bearing properties: no field that could hold an inference, provenance as a required stored value, and no identity of its own beyond a record's key. | `CensusProvenance`; `SnapshotIdentity` | mcp/src/agents_remember/models/knowledge/census.py:1-31 |
| The mapping this group contributes to the envelope's payload registry, built from the six kind-and-schema constants and declared beside the vocabulary rather than beside the write path, so admissibility and storage read one declaration. | `CENSUS_PAYLOAD_MODELS`; `CENSUS_INVENTORY_ROW_KIND`; `CENSUS_CLAIM_KIND`; `CENSUS_DISPOSITION_KIND` | mcp/src/agents_remember/models/knowledge/census.py:339-350; mcp/src/agents_remember/models/knowledge/census.py:49-58 |
| The command-kind and record-kind sets, each derived once so a registry case names the group rather than restating its three literals, and the eight tables a census command writes, declared beside the commands rather than beside the write path. | `CENSUS_COMMAND_KINDS`; `CENSUS_RECORD_KINDS`; `CENSUS_WRITABLE_TABLES` | mcp/src/agents_remember/models/knowledge/census.py:352-354; mcp/src/agents_remember/models/knowledge/census.py:356-360; mcp/src/agents_remember/models/knowledge/census.py:362-373 |
| The closed vocabularies, declared in one block so a value added here is a value the schema's own CHECK already admits. | `CensusArtifactKind`; `CensusParseOutcome`; `CensusInventoryState`; `CensusClaimKind`; `CensusApplicability`; `CensusDispositionKind`; `CensusDispositionState`; `CensusEvidenceState`; `CensusAssessmentDisposition`; `CensusRealizationState`; `CensusLinkKind`; `CensusTargetState` | mcp/src/agents_remember/models/knowledge/census.py:60-88 |
| The four classified kinds in the design's own order, with `unclassified` deliberately excluded because it is the absence of a kind rather than a fifth one. | `CLASSIFIED_CLAIM_KINDS` | mcp/src/agents_remember/models/knowledge/census.py:90-98 |
| The one applicability value that enters the cohort, named once so the eligibility rule and the payload default cannot disagree. | `COHORT_APPLICABILITY` | mcp/src/agents_remember/models/knowledge/census.py:100-103 |
| The provenance every census record requires, with its repository-relative artifact path, its location within the artifact and its frozen baseline carried by identity rather than as two loose strings. | `CensusProvenance`; `baseline` | mcp/src/agents_remember/models/knowledge/census.py:106-122 |
| The refusal of an absolute, backslash or traversal artifact spelling, so a machine location cannot enter a durable record. | `_require_relative_artifact_path` | mcp/src/agents_remember/models/knowledge/census.py:124-144 |
| The inventory row: what the artifact claims to describe beside whether that source is present, and the parse outcome carried as the row's own evidence. | `CensusInventoryRowPayload`; `declared_source_path`; `inventory_state` | mcp/src/agents_remember/models/knowledge/census.py:147-171 |
| The refusal that keeps a failed parse from becoming an outcome with no evidence, in both directions. | `_require_unparsed_content_with_a_failed_parse` | mcp/src/agents_remember/models/knowledge/census.py:173-192 |
| The claim: original text stored verbatim, a kind that starts unclassified, and the applicability field the cohort rule reads. | `CensusClaimPayload`; `claim_kind`; `applicability` | mcp/src/agents_remember/models/knowledge/census.py:195-219 |
| The disposition and the recorded-versus-applied distinction that exists because this leaf prepares a migration and executes no cutover. | `CensusDispositionPayload`; `disposition_state` | mcp/src/agents_remember/models/knowledge/census.py:222-236 |
| The two claim relations: the evidence reference whose unassessed state is derivable from the absence of an assessment row and whose verdict is stored verbatim from the curator's own record, and the realization attribution the coverage measure counts, with `missing_realization` recorded so "nobody looked" stays distinguishable. | `CensusClaimEvidence`; `evidence_state`; `assessment_disposition`; `CensusClaimRealization`; `attribution_state` | mcp/src/agents_remember/models/knowledge/census.py:239-257; mcp/src/agents_remember/models/knowledge/census.py:260-271 |
| The disposition link whose four kinds are the design's split, combine, retire and correction, with the target's resolution state carried verbatim and never repaired by resemblance. | `CensusDispositionLink`; `link_kind`; `target_state` | mcp/src/agents_remember/models/knowledge/census.py:274-287 |
| The three commands, each carrying no author and no instant, with the optional governing route that lets an inventory row exist for a surface the substrate has no route record for. | `CensusInventoryRowCommand`; `CensusClaimCommand`; `CensusDispositionCommand` | mcp/src/agents_remember/models/knowledge/census.py:290-303; mcp/src/agents_remember/models/knowledge/census.py:306-320; mcp/src/agents_remember/models/knowledge/census.py:323-336 |
| The three read-back shapes: the record's own identity and payload beside the envelope's lifecycle and governing route, with the relations attached where the record owns them. | `CensusInventoryRow`; `CensusClaim`; `CensusDisposition` | mcp/src/agents_remember/models/knowledge/census.py:376-382; mcp/src/agents_remember/models/knowledge/census.py:385-393; mcp/src/agents_remember/models/knowledge/census.py:396-403 |
| Where the group's payloads become admissible: the registry unpacking this module's mapping beside every other record family's. | `PAYLOAD_MODELS` | mcp/src/agents_remember/memory/knowledge/record_envelope.py:133-187 |
| Where the group's table set joins the batch's writable-table union, as its own named constant rather than an edit inside another leaf's list. | `CENSUS_ONLY_WRITABLE_TABLES`; `CENSUS_WRITABLE_TABLES` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:106-112; mcp/src/agents_remember/memory/knowledge/candidate_records.py:114-122; mcp/src/agents_remember/models/knowledge/candidate.py:182-192 |
| The two consumers of the vocabulary's own members: the cohort predicate that reads the named applicability value, and the claim-kind census that counts `unclassified` beside the four classified kinds. | `claim_enters_cohort`; `claim_kind_counts` | mcp/src/agents_remember/memory/migration/census_measures.py:265-277; mcp/src/agents_remember/memory/migration/census_measures.py:521-529 |
| Where the read side asserts the schema tuples and this vocabulary agree, and the schema's own declared vocabularies that the stored-value decoder checks against, so the model and the DDL cannot drift into two different sets of admitted values. | `CENSUS_ARTIFACT_KINDS`; `CENSUS_PARSE_OUTCOMES`; `CENSUS_CLAIM_KINDS`; `CENSUS_DISPOSITION_KINDS` | mcp/src/agents_remember/memory/migration/parse.py:45-52; mcp/src/agents_remember/memory/migration/parse.py:112-113; mcp/src/agents_remember/memory/migration/inventory.py:115-119; mcp/src/agents_remember/memory/knowledge/schema_v9.py:70-115; mcp/src/agents_remember/memory/knowledge/census_records.py:186-200 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. These are frozen in-process payload shapes: a
census row names one repository-relative artifact path and one location inside it, its baseline is a
`SnapshotIdentity` of one code revision and one memory revision recorded by identity, and nothing here
opens a connection, reaches a filesystem path, or addresses another repository, dataset or remote.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T17:00+02:00 — 260915-KS-L21 curator (uncommitted change set on `ar/260915-ks-l21`, base `a7076008`): created this one-to-one card for the census's frozen record vocabulary. It records the six kind/schema names and the one `(kind, record_schema) -> model` mapping this group contributes to the envelope's payload registry, the twelve closed vocabularies with `CLASSIFIED_CLAIM_KINDS` deliberately excluding `unclassified` and `COHORT_APPLICABILITY` naming the single value that enters the cohort `N`, and the required `CensusProvenance` whose baseline is a `SnapshotIdentity` rather than two loose strings. It states the two construction refusals that keep a row from looking like coverage without being it — the relative-artifact-path rule and the outcome-versus-unparsed-content rule that closes both directions — together with the relation shapes that record rather than compute their states: an absent `assessment_disposition` is the unassessed state and never a fourth disposition, `missing_realization` is recorded so "nobody looked" stays distinguishable from "the realization is absent", and an unresolved link target is reported rather than repaired. It also records the deliberate absences: no field that could hold an inference, no content address, logical digest or fingerprint, no author or instant on any command, and no `__all__`. This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
