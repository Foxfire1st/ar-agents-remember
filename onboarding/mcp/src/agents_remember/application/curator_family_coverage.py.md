# mcp/src/agents_remember/application/curator_family_coverage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/curator_family_coverage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-24T07:54+02:00 |
| lastVerifiedCommitHash | `0d7910f9d646161c414ed6543453536a3c749d49` |
| lastVerifiedCommitDate | 2026-09-24T08:10:24+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The family plane's half of one ingest report: what was authored, what was examined, and what was left
unresolved (ICR-R28@v2).** The report is the product of a curator run, so this module assembles the
family plane's half of it **from what the run measured**. It decides nothing about storage and writes
nothing: it reads the plans `curator_family_planning.py` resolved and the post-batch facts the run read
back, and produces the typed coverage `ImportReport`'s `family` field carries.

**Three states are kept apart and never merge (`:8-15`):**

| State | What it means |
| --- | --- |
| `recorded` | The batch committed and every count here was read from the candidate |
| `projected` | A planning run wrote nothing, and the lists are what it *would* write |
| `not-recorded` | No family row was written, with the sentence naming why |

**Two further pairs are different facts on purpose.** A guarantee is `authored` when this run sealed its
revision and `examined` when the candidate already held it — the reuse case, where the recorded text is
read back and reported rather than restated. `unexamined` names committed entries the curator authored
no family decision for; `unresolved` names entries whose outcome this run could not establish at all.

## Code Commentary

### Logic

**The outcomes are the report's own vocabulary, and each carries the dataset's measurement rather than a
restatement.** `GuaranteeOutcome` (`:41-53`) carries the key, the two identities, the state, the
display version, the guarantee text, `members_recorded`, `unchanged_sibling_members` and the declared
predecessors; the two member counts are `int | None` precisely because a run that did not commit has no
dataset to measure them against. `MembershipOutcome` (`:56-66`) names one membership's exact endpoints,
its identity, its state and the basis that justified it. `NoFamilyOutcome` (`:69-75`) names the exact
revision a deliberate no-family outcome was authored for, with its basis.

**`FamilyCoverage` is the whole result, and its docstring states the distinctions the report depends
on** (`:78-96`). `unexamined` and `unresolved` are separate tuples because they lead to opposite
actions, and `state` is one of the three above with `detail` carrying the run's own sentence.

**`CoverageScope` groups one run's outcome because it is one fact about one run** (`:99-113`):
`state`/`detail` say what the run established about the family plane, `placed` and `unresolved` are the
two entry sets that outcome divides, and `after` is the post-batch read of the candidate that exists
**only** when the batch committed.

**`family_coverage` assembles the four parts from those inputs without deciding any of them**
(`:116-156`). Memberships are read from the placed entries' plans (a retirement is reported through the
same value with `state="retired"`); guarantees come from `_guarantee_outcomes`; `no_family` is built
from the placed entries whose `no_family_basis` is not `None` — so a `None` basis is an absence of the
outcome rather than an empty one; `unexamined` is every placed entry whose plan is **not** `examined`;
and `unresolved` is taken from the scope verbatim rather than recomputed.

**The guarantee outcomes take their text from the store, not from the plan.**
`_guarantee_outcomes` (`:159-226`) collects every guarantee a committed entry cites — **including one
cited only by a retirement**, because a retirement is a membership change and the packet's own rule is
that such a change prompts examination of the affected recorded guarantee. For a guarantee this list
did not declare, `_examined_outcome` (`:238-263`) builds the outcome from the dataset's recorded row
through `StoredFamilyFacts` — text, version and family identity are what the candidate holds. For a
declared one, `reported_text` is the dataset's recorded text when it exists and the declared text
otherwise, and the comment states the ordering rather than leaving it to be inferred: an examined
plan's revision is stored *by construction*, so the declared text is a fallback that is unreachable
while the store holds the row. The state is `examined` for an examined plan, else `authored` when the
run recorded and `projected` when it did not.

**The counts are measurements, and their arithmetic says so.** `members_now` is `None` when there is no
post-batch read; `unchanged_sibling_members` is `max(members_now - added, 0)`, where `added` counts only
the memberships this run placed that were not already stored — so the reported sibling count is the
unchanged remainder, never the total. `_CitedGuarantee` (`:229-235`) exists to carry exactly those two
numbers for the cited-but-undeclared case.

**A stored membership is reported as `reused`, not as `added`** (`_membership_outcome` `:266-275`),
which is the same distinction the planning half makes when it marks a plan `stored`; a retirement is
reported by `_retired_outcome` (`:278-287`) with its two endpoints and the row identity, and with no
family key or basis, because a removal states neither.

### Conventions

This module imports the planning half's values and nothing from the store, the command vocabulary or the
CLI. It computes no refusal of its own: a run's failures arrive as the `state`/`detail` pair and as the
`unresolved` set the operation built, so the report has one source for each fact. Every count it emits
is either read from the candidate or `None`; it never substitutes a zero for an unmeasured value.

### Invariants And Boundaries

- `recorded` / `projected` / `not-recorded` are three states and never merge.
- The two member counts are `None` when the run did not commit; a zero would read as a measured empty
  family and is never substituted.
- A guarantee this list did not declare is reported from the dataset's recorded row, not from an
  expectation.
- `unexamined` and `unresolved` are different facts and stay in different tuples.
- A retirement is a membership change and therefore brings its guarantee into the outcomes.
- This module writes nothing and decides nothing about storage.

### Todos

None recorded.

## Docs References

No configured Domain Documentation source applies; this is the typed coverage of one curator run's own
result.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is required for assembling the family coverage. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the three non-merging states and of `unexamined` versus `unresolved`.** | "Three states are kept apart and never merge"; "are different facts on purpose" | mcp/src/agents_remember/application/curator_family_coverage.py:1-16 |
| The published surface: the three outcome values, the coverage, the scope and the one entry point. | `__all__` | mcp/src/agents_remember/application/curator_family_coverage.py:31-38 |
| **One guarantee outcome, whose two member counts are nullable because an uncommitted run has no dataset to measure them against.** | `GuaranteeOutcome`; "members_recorded" | mcp/src/agents_remember/application/curator_family_coverage.py:41-53 |
| One membership this run added, found already recorded, or retired, with the basis that justified it. | `MembershipOutcome` | mcp/src/agents_remember/application/curator_family_coverage.py:56-66 |
| **One deliberate no-family outcome: the exact revision it was authored for, and its basis.** | `NoFamilyOutcome` | mcp/src/agents_remember/application/curator_family_coverage.py:69-75 |
| **The whole family result, with `unexamined` and `unresolved` in separate tuples and the state's own sentence beside them.** | `FamilyCoverage`; "class FamilyCoverage:" | mcp/src/agents_remember/application/curator_family_coverage.py:78-96 |
| **One run's outcome grouped as one value, where `after` exists only when the batch committed.** | `CoverageScope`; "after: StoredFamilyFacts" | mcp/src/agents_remember/application/curator_family_coverage.py:99-113 |
| **The assembly, where `unexamined` is every placed entry whose plan is not examined and `unresolved` is taken verbatim rather than recomputed.** | `family_coverage`; "unexamined=tuple(entry for entry in placed if not authoring[entry].examined)" | mcp/src/agents_remember/application/curator_family_coverage.py:116-156 |
| **The guarantee outcomes: a cited guarantee enters through a retirement too, because a membership change prompts examination of the affected guarantee.** | `_guarantee_outcomes`; "A guarantee enters here when a committed entry cites it" | mcp/src/agents_remember/application/curator_family_coverage.py:159-226 |
| **The recorded text is what is reported for an examined plan, with the declared text an unreachable fallback rather than a second claim.** | "reported_text = plan.joint_guarantee if stored_text is None else stored_text" | mcp/src/agents_remember/application/curator_family_coverage.py:201-210 |
| The two numbers a cited-but-undeclared guarantee is reported with. | `_CitedGuarantee` | mcp/src/agents_remember/application/curator_family_coverage.py:229-235 |
| **A guarantee this list did not declare, reported from the dataset's own recorded row rather than from an expectation.** | `_examined_outcome` | mcp/src/agents_remember/application/curator_family_coverage.py:238-263 |
| A membership the candidate already recorded is reported `reused` rather than `added`. | `_membership_outcome`; "reused" | mcp/src/agents_remember/application/curator_family_coverage.py:266-275 |
| A retirement reported by its two endpoints and the row identity, with no family key or basis. | `_retired_outcome` | mcp/src/agents_remember/application/curator_family_coverage.py:278-287 |
| The plans and the measured facts this module reports, owned by the planning half rather than restated here. | `DeclarationPlan`; `MembershipPlan`; `RetirementPlan`; `StoredFamilyFacts`; `CuratorFamilyAuthoring` | mcp/src/agents_remember/application/curator_family_planning.py:326-338; mcp/src/agents_remember/application/curator_family_planning.py:483-493; mcp/src/agents_remember/application/curator_family_planning.py:496-504; mcp/src/agents_remember/application/curator_family_planning.py:204-222; mcp/src/agents_remember/application/curator_family_planning.py:507-533 |
| The report value this coverage becomes a field of, and the operation that assembles it after the batch. | `IngestReport`; `_report` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:451-499; mcp/src/agents_remember/application/knowledge_curator_ingest.py:3737-3814 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The coverage is assembled from one candidate
dataset's own rows and one list's own plans.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-24T07:54+02:00 — 260921-ICR-L28 curator (uncommitted change set on `ar/260921-icr-l28`, base
  `63b476297708f779de8ed5c0bf3555b9d1de70c2`): created this one-to-one card for the module
  `ICR-R28@v2` introduced as **the family plane's report half**. The stamp basis is the leaf's base
  commit, because the module is untracked there. The thing a reader must not lose: the coverage is
  assembled from **what the run measured**, so `recorded` means the batch committed and every count was
  read back from the candidate, `projected` means a planning run wrote nothing, and `not-recorded` names
  the run that wrote no family row — and a run that did not commit reports `None` for the two member
  counts rather than a zero that would read as a measured empty family. `unexamined` (a committed entry
  the curator authored no decision for) and `unresolved` (an entry whose outcome the run could not
  establish) are different facts and stay in different tuples. No verification stamp beyond the leaf's
  base is advanced: the candidate is uncommitted and the governed closeout owns the real commit.
