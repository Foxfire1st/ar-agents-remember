# mcp/src/agents_remember/application/review_recorded_selection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_recorded_selection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-23T02:30+02:00 |
| lastVerifiedCommitHash | `870701b43039cd205a8c98e418382729510c3de3` |
| lastVerifiedCommitDate | 2026-09-23T03:12:21+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The recorded population one review selection reaches** (`ICR-R26@v1`). A record's applicability turns
on two questions, and this module answers both from recorded facts: *which identity did the request
select, and which revisions does the selection record for it*, and *which other identities do the
recorded relationships of that selection reach*.

**It reads from two places, and the reason is the whole point of the module.** The comparison's own
union items, ICR-R07's recorded revision selection and ICR-R08's traversal of the recorded before/after
relationship union say what the comparison **displayed** — and they are a bounded page (`ICR-R10`), so
on their own they would make a record's *meaning* depend on the page the caller asked for. The
snapshots' own owners therefore answer the page-independent half — the selected identity's recorded
revisions, the realizations recorded under them, the families that directly contain them and those
families' recorded members — and the two are merged so the recorded population only ever **grows** past
what the page showed. Nothing the page returned is replaced.

The module opens the two snapshot files read-only for that read and nothing else: it selects no
subject of its own (it calls `ICR-R07`'s own narrowing), widens no frontier, resolves no reference and
writes nothing. It is its own module because "what does this selection reach" is a different
responsibility from "which records may be displayed" (the classifier in
[`review_record_applicability.py`](review_record_applicability.py.md)), and because the review adapter
is over the repository's soft file-size rail.

A path seed names no identity at all, and that is a **state** rather than a failure: the population
then carries no subject, and every record of that review is classified by the recorded relationship
that reaches it instead of by a subject it never had.

## Code Commentary

### Logic

**`RecordedSelection` is the population as the classifier reads it, and it keeps two facts that look
alike deliberately apart.** `subject` is the identity the request's own seed named (absent for a path
seed); `subject_revisions` are the revisions the selection **records** for it — the selected identity's
recorded revisions as the two snapshots' own owners list them, page-independent, together with every
revision the comparison's page selected for that identity; and `published_retained` is ICR-R07's own
retained list **for the page this request asked for**, computed by the existing `_retained_revisions`
and deliberately *separate* from `subject_revisions`. The separation is a truthfulness rule rather than
a cache: a label may cite R07's published list only where that list really carries the matched
revisions, because at a bounded page it is narrower than the recorded population. The remaining
mappings are one recorded fact each: `revision_identity` (which identity records a revision),
`relationship_ids` and `relationship_identity` (which relationship rows are recorded and which identity
each sits under), `path_identity` (a recorded address), and `related` — the identity → relationship
**spelling** that reached it.

**`selected_subject_population` is the one public entry, and it merges the two halves under the page
facts.** It narrows the seed through `selected_subject` (the shipped spelling per seed kind), resolves a
*revision* seed's identity through the union item that carries that revision (a revision seed names a
revision; the subject is the identity the snapshot records it under), reads the recorded population
from the snapshots, and then builds the value with the union that only grows:
`subject_revisions = recorded | snapshots`, identity maps merged with the snapshots' own rows taking
their place under the traversal's, and `related` assembled from **three fixed tiers** — the snapshots'
own relationship rows first (they say *how* an identity is reached and do not depend on the page), the
traversal's relationship rows next, and the comparison's own selection of an identity last (the weakest
statement of how it was reached). The order is fixed so that **two page sizes render the same related
identity with the same spelling**, which is what a measurement of the page-size series checks.

**`_Population` is the mutable accumulator, and its one rule is that an association identity is never a
revision.** `reach` records a relationship row's spelling and its identity mapping, and `_reach_revision`
records a revision under an identity; the F-V1 finding of this leaf's first verification round was
exactly this distinction — an association's own identity was entering the revision index, so an
assessment that carried the selected invariant's *identity* where a revision belongs intersected the
subject's revisions and read `direct`. The fix keeps the two apart at the source: an identity enters
the revision index only where a revision is what was recorded.

**The snapshot half is read defensively and contributes nothing it could not establish.**
`_snapshot_population` opens each side read-only and, for a side that cannot be opened or read
(`OSError`, `apsw.Error`, `KnowledgeStorageError`, `ValueError`), contributes nothing rather than failing
the review — a review whose knowledge half is unreadable is a state the surface already reports
elsewhere, and nothing is inferred from a side that could not be read. `_read_recorded_reach` reads the
subject's recorded revisions through `fetch_revision_ids` and then branches by subject kind: an
invariant's realizations and containing families (`_read_realizations`,
`_read_containing_families`), or a family's own members (`_read_family_members`).
`_read_containing_families` is the module's own statement of what "related family/closure context"
means here: every family that **directly** contains one of the subject's revisions, each member
identity recorded with the membership row's own spelling, and the member revision indexed under the
*member's* identity rather than under the family it sits in. `_read_family_members` takes `subject` as
the selected identity when the selection *is* a family (there the members are what the selection
reaches) and `None` when the family was reached from an invariant (there the member identities are the
context the selection reaches through it).

**Read cost is stated, not hidden.** The population comes from one extra read-only pass over the two
snapshots per selected-subject review, and a record that names a subject the selection does not reach
triggers the lazily read known-subject catalogue in the classifier — never here.

### Conventions

`__all__` publishes the five names its one consumer uses: `ApplicabilitySources`, `ComparisonFacts`,
`RecordedIdentity`, `RecordedSelection` and `selected_subject_population`. The three dataclasses are
frozen; `_Population` is the single mutable accumulator and never leaves the module. The module reads
the snapshots through the existing read owners (`open_read_only_database`, `fetch_revision_ids`,
`fetch_realizations_for_invariants`, `fetch_memberships_of_invariants`, `fetch_family_ids_for_revisions`,
`fetch_memberships_of_families_full`, `fetch_invariant_revisions`) rather than through new SQL of its
own, and it declares no model: every value it returns is built from
[`models/knowledge/review.py`](../../models/knowledge/review.py.md)'s own types.

### Invariants And Boundaries

- **The recorded population only grows past the page.** The snapshots' answer is merged *under* the
  comparison's facts; a page size can narrow what is displayed and never change what a record means.
- **A page is never fetched here.** The module reads the two snapshot files read-only; R10's bound still
  decides what the panes display.
- **An association identity is not a revision.** Only a recorded revision enters the revision index,
  which is what keeps a malformed binding from being matched against the selection.
- **R07's published retained list is carried beside the recorded population, never in place of it.**
  The two facts exist separately because they are true of different populations.
- **A side that cannot be read contributes nothing.** The module never infers from an unread side and
  never raises out of the review read.
- **A path seed has no subject, and that is a state.** Its records are classified by recorded
  relationship rather than by a subject the selection never had.
- **Read-only, and no store of its own.** Two snapshot files, opened and closed; no write, no cache, no
  second copy of a relationship union.

### Todos

None recorded. The three-tier `related` ordering is a fixed rule rather than a preference: a later
reader who reorders it changes which spelling two page sizes render for the same identity.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the two questions it answers, the two places it reads and the reason: a page must not decide a record's meaning.** | "A review's applicability classification turns on two questions"; `RecordedSnapshots` | mcp/src/agents_remember/application/review_recorded_selection.py:1-27; mcp/src/agents_remember/application/review_recorded_selection.py:145-157 |
| **The population as the classifier reads it, with the recorded revisions and ICR-R07's page-bound retained list kept deliberately apart.** | `RecordedSelection`; `published_retained` | mcp/src/agents_remember/application/review_recorded_selection.py:78-125; mcp/src/agents_remember/application/review_recorded_selection.py:105-105 |
| **The one public entry, which reads the snapshots' half and merges it under the comparison's page facts so the union only grows.** | `selected_subject_population` | mcp/src/agents_remember/application/review_recorded_selection.py:176-222 |
| **The three fixed tiers of relationship spelling, ordered so two page sizes render the same related identity the same way.** | `selected_subject_population` | mcp/src/agents_remember/application/review_recorded_selection.py:176-222 |
| **The one identity a review seed names, in the union's own kind vocabulary, with a revision seed resolved through the item that carries it.** | `_subject_identity` | mcp/src/agents_remember/application/review_recorded_selection.py:225-236; mcp/src/agents_remember/application/review_attribution.py:160-178 |
| **The mutable accumulator whose one rule is that an association identity is never a revision.** | `_Population`; `reach`; `_reach_revision` | mcp/src/agents_remember/application/review_recorded_selection.py:267-305; mcp/src/agents_remember/application/review_recorded_selection.py:292-305; mcp/src/agents_remember/application/review_recorded_selection.py:357-369 |
| **The page-independent half read from both snapshots' own owners, contributing nothing from a side that could not be read.** | `_snapshot_population`; `_read_recorded_reach` | mcp/src/agents_remember/application/review_recorded_selection.py:483-508; mcp/src/agents_remember/application/review_recorded_selection.py:511-532 |
| **What "related family/closure context" means here: a directly containing family, its recorded members, and each member indexed under its own identity.** | `_read_containing_families`; `_read_family_members`; `_read_realizations` | mcp/src/agents_remember/application/review_recorded_selection.py:550-580; mcp/src/agents_remember/application/review_recorded_selection.py:583-617; mcp/src/agents_remember/application/review_recorded_selection.py:535-547 |
| **The comparison facts the classification must not mix across comparisons, carried as one measurement.** | `ComparisonFacts` | mcp/src/agents_remember/application/review_recorded_selection.py:129-141 |
| **The sources one classification is assembled from, with the known-subject catalogue a reader rather than a value.** | `ApplicabilitySources` | mcp/src/agents_remember/application/review_recorded_selection.py:161-173 |
| **The read owners this module composes instead of writing SQL of its own.** | `fetch_revision_ids`; `fetch_memberships_of_invariants`; `fetch_family_ids_for_revisions`; `fetch_memberships_of_families_full`; `fetch_invariant_revisions`; `fetch_realizations_for_invariants`; `open_read_only_database` | mcp/src/agents_remember/memory/knowledge/read_queries.py:64-75; mcp/src/agents_remember/memory/knowledge/read_queries.py:96-107; mcp/src/agents_remember/memory/knowledge/read_queries.py:153-175; mcp/src/agents_remember/memory/knowledge/read_queries.py:178-191; mcp/src/agents_remember/memory/knowledge/read_queries.py:210-223; mcp/src/agents_remember/memory/knowledge/read_queries.py:263-297; mcp/src/agents_remember/memory/knowledge/connection.py:52-63 |
| **The one consumer, and the port its panes read.** | `review_applicability`; `AppliedRecords` | mcp/src/agents_remember/application/review_record_applicability.py:183-214; mcp/src/agents_remember/application/review_record_applicability.py:134-180 |
| **The case that measures the page-independence this module exists for: identical treatments, context and summaries at every page size.** | `test_every_page_size_classifies_the_same_records_the_same_way` | mcp/tests/test_knowledge_review_subject_isolation.py:361-397 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one repository's own two snapshot
files and names no boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-23T02:30:00+02:00 — 260921-ICR-L26 curator (candidate `ar/260921-icr-l26`, uncommitted; production line at this leaf's base `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`, confirmed from the enclosure contract): created this one-to-one card for the module this leaf introduced to hold **one selection's recorded population** (`ICR-R26@v1`). The card records what the module reads and from which two places, why the snapshots' half exists (a bounded page must not decide a record's meaning), the deliberate separation of the recorded revisions from ICR-R07's page-bound retained list, the fixed three-tier relationship-spelling order, the rule that an association identity is never a revision (this leaf's F-V1 fix, stated as current behaviour), the defensive snapshot read that contributes nothing from a side it could not open, and the read-only boundary. **Stamp accounting:** the verification pair names the production line at this leaf's base — the last real commit the reading was taken against — because every construct this card cites exists only in this leaf's uncommitted candidate; the governed closeout owns the real stamp once the code commit exists.
