# mcp/src/agents_remember/memory/knowledge/diff_attribution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/diff_attribution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T08:30:00+02:00 |
| lastVerifiedCommitHash | `6695a2a12961ef340c8864d56f0a1ce12b51b3c5` |
| lastVerifiedCommitDate | 2026-09-22T09:38:24+02:00|
| reviewedWorkingCandidate | candidate `ar/260921-icr-l4`, uncommitted; base `d80a0513e928ef29a973527d09597c82c96fde87` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The attribution partition: one measured change population, divided once (`ICR-R04@v1`).**
*Attribution* is a recorded relationship between a realization claim and the path it names, so the
question this module answers is a path-level one: of the changes the *source* measurement observed,
which ones does either bound snapshot register an attribution for? The answer is one partition with
three buckets — attributed, confirmed unregistered, undetermined — disjoint and exhaustive over that
measured population by construction. The arithmetic is pure: the caller supplies the observation, the
registered mappings it read from the two snapshots, and each side's inspection state.

## Code Commentary

### Logic

Four rules, each of which is a way a count could otherwise lie:

1. **The denominator is the measurement, not the comparison.** `partition_attribution` takes the
   whole `TreePaths`, not a bare sequence: the population is the observation's own `paths` — the
   paths the *source* measurement measured — which is what makes an unchanged mapped path context
   rather than a change. The observation travels whole because a *partial* one states the scope of
   its own total through `_denominator_scope`: paths whose names cannot be carried as text are
   outside every count here, and the value says so.
2. **A mapping is valid only when the recorded bytes are at the recorded path.** `MappingFact`
   carries the registered claim (`side`, `path`, `claim_id`), its `resolution`, whether it
   `resolved`, and whether the claim's own recorded scope is the selected subject (`subject_link`).
   Only `exact_recorded_blob` resolves. A stale recording, an unresolvable locator and a missing
   path are purported mappings: counted, carried with their own `unresolved_mapping_count`, and
   never promoted to an attribution.
3. **Several links to one path count it once.** `_mappings_by_path` groups by measured path and one
   `ChangedPathAttribution` is built per path, so no duplicate can inflate a total; the model's own
   validator refuses a repeated path and a bucket total that disagrees with its paths.
4. **A side nobody read supports no negative conclusion.** `_LICENSED_ABSENCE` names the two side
   states that license an absence conclusion — `inspected` (a scan that completed) and `known_empty`
   (R05's identified empty first generation, a stronger statement than a scan that found nothing) —
   and `unavailable` licenses nothing. `licenses_absence` is the one predicate read off that table,
   and it is read twice: the partition reads it to decide the confirmed-unregistered bucket, and the
   acquisition owner reads the same function for `subject_scope_complete` — so the two questions
   cannot come to disagree about what "completely inspected" means.

Within the attributed paths, `_link` decides the relation to the selected subject: a known
selected-subject link establishes `selected_subject`; links only outside it are
`outside_selection_complete` only when the subject's own scope was completely inspected, otherwise
`outside_selection_membership_unknown`; with no subject selected the label is `no_subject_selected`.
An attributed path on an incomplete partition carries `_incomplete_suffix`: the attribution is
established, and "these are all the claims that name it" is not.

`unavailable_attribution` is the partition of a measurement that was not made: no total, and the
reason it is not zero — an unmeasured change population has no denominator, so no path can be called
attributed, confirmed unregistered or of undetermined attribution.

### Conventions

- The module docstring states the four rules as the ways a count could lie; the code is the
  implementation of exactly those rules.
- Every `detail` is prose written **for a reader**; nothing in it is parsed by the package, and the
  typed fields (`bucket`, `link`, `mapped_sides`, totals) are what a caller branches on.
- `_closed` closes the producer's detail sentence so the partition's final statement does not run
  into it: two sentences that read as one is exactly the kind of unreadable scope statement the
  function exists to prevent.

### Invariants And Boundaries

- **One implementation, two readers, one predicate.** `partition_attribution` is defined once and
  called once (by `review_attribution`); `licenses_absence` is the one predicate behind both the
  confirmed-unregistered bucket and the exclusive-outside label.
- **No semantic verdict.** The partition has no verdict field and establishes no coverage: a resolved
  path-level mapping establishes that a recorded claim's bytes are at this path and never that every
  change inside it realizes that claim.
- **Boundary.** This module decides arithmetic from supplied values. It reads no snapshot, opens no
  database, observes no anchor and runs no Git command — acquisition belongs to
  `application/review_attribution.py`, and the display seam (`diff_display`) re-exports every name
  here so its importers are unchanged.

### Todos

None recorded. The module was extracted from `diff_display.py` in leaf `260921-ICR-L4`'s fix round
along the established seam policy (one implementation, purpose-named adjacent module, original keeps
re-exporting) when the fix-round additions pushed the display past the 900-line soft rail. The
`family_revision` subject kind is implemented in the acquisition owner but not covered by any
production-composition case — that gap is recorded on this leaf's worker report, not here.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **One recorded claim at one measured path, with its resolution and whether it resolved — stale and unresolved mappings carried, never promoted.** | `MappingFact` | mcp/src/agents_remember/memory/knowledge/diff_attribution.py:56-78 |
| **One bound snapshot's contribution and how completely it was inspected.** | `SideInspection` | mcp/src/agents_remember/memory/knowledge/diff_attribution.py:82-88 |
| **The reader seam: which registered mappings each bound snapshot holds at the measured paths.** | `AttributionReader` | mcp/src/agents_remember/memory/knowledge/diff_attribution.py:91-94 |
| **The partition of a measurement never made: no total, and the reason it is not zero.** | `unavailable_attribution` | mcp/src/agents_remember/memory/knowledge/diff_attribution.py:97-113 |
| **The whole accounting in four steps: measured denominator, resolved-attribution, licensed absence, subject link.** | `partition_attribution` | mcp/src/agents_remember/memory/knowledge/diff_attribution.py:116-178 |
| **The licensing table and the one predicate behind both the bucket and the exclusive-outside label.** | `_LICENSED_ABSENCE`; `_licenses_absence`; `licenses_absence` | mcp/src/agents_remember/memory/knowledge/diff_attribution.py:198-227 |
| **One path's bucket, its link, its mapped sides and the fact that decided it.** | `_path_attribution`; `_link`; `_mapped_sides` | mcp/src/agents_remember/memory/knowledge/diff_attribution.py:230-321 |
| **The incomplete-partition label and the scope sentence that states a partial denominator.** | `_incomplete_suffix`; `_partition_detail`; `_denominator_scope` | mcp/src/agents_remember/memory/knowledge/diff_attribution.py:285-386 |
| **The single caller that supplies the observation, the mappings and the sides.** | `review_attribution` | mcp/src/agents_remember/application/review_attribution.py:181-211 |
| **The value the partition builds, with its disjoint-plus-exhaustive validator.** | `SourceAttribution` | mcp/src/agents_remember/models/knowledge/diff.py:509-620 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every statement runs against values the
caller supplied; no second repository, ledger or coordination path is read.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): created this one-to-one card for the module this leaf introduced as the **partition arithmetic for ICR-R04@v1**. It records the four rules the arithmetic implements (measured denominator with partial-scope statement; only `exact_recorded_blob` resolves; one path counted once; no negative conclusion from an unread side), the one licensing table with its one predicate read twice, the subject-link labels, and the pure-arithmetic boundary against the acquisition owner. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the production line at this leaf's recorded base, because every construct cited here exists only in this leaf's uncommitted candidate; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the real stamp once the code commit exists.
