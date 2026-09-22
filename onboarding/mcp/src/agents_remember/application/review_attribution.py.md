# mcp/src/agents_remember/application/review_attribution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_attribution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-22T08:30:00+02:00 |
| lastVerifiedCommitHash | `6695a2a12961ef340c8864d56f0a1ce12b51b3c5` |
| lastVerifiedCommitDate | 2026-09-22T09:38:24+02:00|
| reviewedWorkingCandidate | candidate `ar/260921-icr-l4`, uncommitted; base `d80a0513e928ef29a973527d09597c82c96fde87` |
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The acquisition half of the attribution accounting (`ICR-R04@v1`): which of a review's measured
source changes each bound snapshot registers an attribution for.** This module reads the registered
mappings of the two bound snapshots — through the memory layer's own registered-path lookup and its
own anchor resolver — and hands them to the arithmetic
(`diff_display.partition_attribution`, owned by `memory/knowledge/diff_attribution.py`). Neither
half decides anything about a change's meaning, and neither is a second owner of the records.

## Code Commentary

### Logic

`review_attribution(observed, *, sides, subject)` partitions one observed change population. The
observation is the caller's own — the same value its inventory was rendered from — so the denominator
is the measurement the response publishes and not a second one. An observation that was not made
returns `unavailable_attribution`: no total, and the observation's own reason.

Four rules make the acquisition truthful, and each is a way the numbers could otherwise lie:

1. **The mapping is looked up by exact path equality, in the snapshot.** The one primitive is
   `fetch_realizations_at_path` — the same primitive `registered_scope.py` reads — so a review's
   attribution and a scope's edges cannot come to disagree about what "registered here" means. The
   lookup is not restricted to the selected subject, which is exactly the case ICR-R04 refuses to
   report as globally unregistered: a change attributed to another invariant is *found* rather than
   assumed absent.
2. **A mapping is valid only when the recorded bytes are at the recorded path.**
   `_RESOLVED_MAPPINGS` is exactly `{"exact_recorded_blob"}` — the only value read as *resolved*.
   `recorded_blob_mismatch` is the shipped **stale** state, and `path_absent`,
   `unsupported_locator`, `entry_not_blob` and an observation the resolver never made are
   **unresolved** purported mappings: carried with their own resolution, counted as unresolved, and
   never promoted. This is the packet's own precedence sentence, and the shipped vocabulary agrees
   (`resolved` is `exact_recorded_blob` in `read_owner_revisions`; `stale` is
   `recorded_blob_mismatch` in `citation_closure`).
3. **A snapshot that was not read supports no negative conclusion.** A side whose dataset is absent,
   damaged or unopenable is `unavailable`, and every path without a resolved mapping is then of
   undetermined attribution rather than confirmed unregistered. `_damaged_half` consults R05's own
   damage reader before binding a before side, so a half whose recorded origin disagrees with its
   bytes is unavailable with that reader's own reason. The one exception is a *legitimately
   known-empty* side: the before half of a leaf whose recorded origin identifies an explicitly empty
   first generation, checked against its bytes (`_identified_first_generation`), is `known_empty`
   and counts as completely inspected for absence — ICR-R05 owns that record, this module only
   consumes it.
4. **Every count states its scope.** The denominator is the caller's own source observation, the
   granularity is the changed path, and each side's inspection state travels beside them.

`AttributionSideInput` is one bound snapshot the partition is decided from: the read context that
already binds one side's tree (exactly as the comparison opened it), the already-open read-only
handle when the caller has one (the comparison does; this module closes only what it opened), and —
for a side that never became readable — `context=None` with `unreadable` saying why. Such a side is
a fact of the *pair*, carried rather than omitted: a dropped side would leave the ones that remain
looking complete.

`selected_subject` narrows the review selector to the subject the membership question needs —
invariant identity or one of its exact revisions, family identity or one of its exact revisions —
never a display label, a path or a version. A path selector names no invariant or family and yields
`None`. `_subject_matcher` answers per claim row: invariant subjects directly from the row, family
subjects from the family's own membership rows; a family whose memberships cannot be read yields
`established=False`, so its links are still counted and attributed while the *label* degrades to
membership-unknown rather than claiming an exclusive-outside conclusion no read supported. The
`family_revision` kind (a family *revision* seed) is implemented and **not covered by any
production-composition case** — the one coverage gap this leaf leaves, recorded on its worker
report.

`subject_scope_complete` is decided by one predicate plus one condition: `licenses_absence` (the
partition owner's own rule) plus every side having answered the membership question. The second,
independent tuple membership this module used to carry is deleted — one table, one predicate, two
readers.

### Conventions

- Read errors stay values: `_read_side` turns storage, OS and decode failures into `unavailable`
  sides with their own reasons rather than raising out of the composition.
- A resolver that observed nothing at all is carried as `unsupported_locator` rather than dropped:
  a registered claim that produced no observation is still a claim this snapshot registers at this
  path.

### Invariants And Boundaries

- **No second owner of the records.** Mappings are read through the memory layer's own lookup and
  anchors through its own resolver; this module decides no arithmetic (the partition does) and no
  meaning.
- **No HEAD/current-knowledge fallback, no parallel authority.** Only reads: the shipped
  `fetch_realizations_at_path`, `observe_anchor`/`anchor_resolver_for`, and `read_before_half`. No
  write, no new store, no new authority.
- **Boundary.** This module acquires; `memory/knowledge/diff_attribution.py` computes. The
  comparison supplies the reader over its own two open snapshots (`_registered_mapping_reader` in
  `knowledge_diff.py`); the task-context route measures its own pair (`pair_attribution` in
  `review_task_context.py`).

### Todos

None recorded in this module. The `family_revision` production-composition coverage gap is tracked
on leaf `260921-ICR-L4`'s worker report (§4, "Not run, and why").

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The one anchor resolution that establishes a registered mapping, with stale and unresolved states named as purported.** | `_RESOLVED_MAPPINGS` | mcp/src/agents_remember/application/review_attribution.py:92-107 |
| **The subject the membership question needs, narrowed per seed kind rather than reached through `getattr`.** | `SelectedSubject`; `selected_subject` | mcp/src/agents_remember/application/review_attribution.py:111-178 |
| **One bound snapshot: its binding, its handle, and the carried reason when it never became readable.** | `AttributionSideInput` | mcp/src/agents_remember/application/review_attribution.py:124-149 |
| **The entry point: the caller's own observation partitioned by the bound snapshots' mappings.** | `review_attribution` | mcp/src/agents_remember/application/review_attribution.py:181-211 |
| **One side's mappings read by exact path equality with each anchor observed, or the reason it could not be read.** | `_read_side`; `_registered_mappings` | mcp/src/agents_remember/application/review_attribution.py:214-285 |
| **The per-row subject predicate, with family membership from the family's own rows and degradation to membership-unknown.** | `_subject_matcher`; `_family_revision_ids` | mcp/src/agents_remember/application/review_attribution.py:288-331 |
| **Completely inspected versus legitimately known-empty, claimed only for a checked first-generation before half.** | `_inspection_state`; `_identified_first_generation` | mcp/src/agents_remember/application/review_attribution.py:334-389 |
| **A present-but-not-what-it-claims before half is unavailable with R05's own reason, and supports no negative conclusion.** | `_damaged_half` | mcp/src/agents_remember/application/review_attribution.py:359-379 |
| **The same lookup the registered-scope construction reads, so the two cannot disagree.** | `fetch_realizations_at_path` | mcp/src/agents_remember/memory/knowledge/read_queries.py:226-226 |
| **The comparison's reader over its own two open snapshots — no second open, no second namespace.** | `_registered_mapping_reader` | mcp/src/agents_remember/application/knowledge_diff.py:451-486 |
| **The task-context route's own pair measurement, for a review that compares no dataset.** | `pair_attribution` | mcp/src/agents_remember/application/review_task_context.py:227-285 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Reads stay inside the two bound snapshots
of the pair under review; no second repository, ledger or coordination path is read.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-22T08:30:00+02:00 — 260921-ICR-L4 curator (uncommitted change set on `ar/260921-icr-l4`, base `d80a0513e928ef29a973527d09597c82c96fde87`): created this one-to-one card for the module this leaf introduced as the **acquisition half of the ICR-R04@v1 accounting**. It records the four truthfulness rules (exact-path lookup through the shared primitive; only `exact_recorded_blob` resolves with stale/unresolved carried; unread sides support no negative conclusion with R05's damage and empty-generation readers consumed, not re-decided; caller-owned denominator), the subject narrowing with the family-membership degradation, the single `licenses_absence` predicate shared with the partition, and the no-second-owner boundary. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the production line at this leaf's recorded base, because every construct cited here exists only in this leaf's uncommitted candidate; the `reviewedWorkingCandidate` row states what was actually read, and closeout owns the real stamp once the code commit exists.
