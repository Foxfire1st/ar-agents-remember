# mcp/src/agents_remember/models/knowledge/merge.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/merge.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `9f88a6de572dc15bbed1802cf08b77c1193fb24c` |
| lastVerifiedCommitDate | 2026-09-18T14:21:49+02:00|
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The common-base merge vocabulary: explicit inputs, coverage facts and one structural outcome.** A merge is a *structural* operation over three datasets that already exist — an explicit common base, two sides derived from it, and a private candidate produced from the first side.

**Nothing in this module can carry a judgement about whether the merged knowledge is *correct*.** There is no compatibility, acceptance, approval or "harmless" field, and the one non-refusal state is named `MERGE_STATES = ("structurally_merged",)` because that is the entire claim it makes. This is the shape requirement `KS-R05@v1` names for the result, and it is enforced at construction rather than by convention: the model validators make the mixed states unrepresentable.

## Code Commentary

### Logic

Three splits are load-bearing, and each is a place where a weaker model would have permitted a guess:

- **An explicit input versus a resolved one.** `MergeInput` names a dataset *and* the exact logical identity the caller admitted for it (`role`, `database`, `identity`, `reference`). A caller cannot hand over a path and let the operation decide which dataset it meant: the identity is re-read and compared before any byte is copied. `reference` is the caller's own durable anchor (a Git tree, a commit pair, a snapshot reference) and is carried as a fact, never resolved here — this layer does not read Git objects to decide what a dataset is.
- **A base claim versus a base fact.** The claim is a closed union of `SuppliedGitBase` (the caller resolved the base itself and names the exact commit and tree) and `ResolvedGitBase` (the caller claims one commit is the *unique* common base and asks for the evidence). There is no third member — "the operation may pick one" is not expressible, which is what keeps an arbitrary `git merge-base` result out of reach. `MergeBaseResolution` records which of the two applied: `git_base_commit` is the exact admitted commit or `None`, and `uniqueness_checked` distinguishes "the history had one common base" from "the caller said which commit it was" without re-deriving it from the claim.
- **A measurement versus a verdict.** `MergeCoverage` reports which tables the changeset touched, which tables the replay proved covered, and how many operations of each kind were materialised. `MergeOutcome` reports the identities it observed. Neither can express an opinion about the data.

`MergeRequest` restates the datasets' paths beside the resolution's identities rather than carrying them inside it, because they are local operation facts: a dataset *identity* is what the resolution proves, and the file it is read from is an input this request names. It is a dataclass rather than a third model member so the paths cannot be serialized into anything durable. `destination` is optional on purpose: a caller may run the merge and inspect the structural outcome without publishing anything.

`TableCoverage` separates two facts that a return code conflates: `table_changed` is read from the two datasets (whether the side's rows differ from the base's for this table) while `operations` counts the materialised changeset operations. A table that changed but contributed no operation is the silent omission the coverage exists to catch, and `replayed` records whether applying the changeset to a fresh copy of the base reproduced the side's whole logical dataset. `MergeCoverage` covers **every** canonical table, including unchanged ones, because "this table was examined and had nothing to carry" is a different fact from "this table was never attached".

`MergeConflict` carries exactly the facts SQLite supplied, in two shapes that are not interchangeable:

- a **row-level** conflict, where SQLite hands the callback the operation in hand: `attribution` is `engine_attributed` and `table`, `operation` and `record_id` are all present. `record_id` is the exact key of the row the engine refused, copied out of the change the callback received and therefore read from the operation's **old** values — a changeset supplies only the columns an operation changes, and an `UPDATE` leaves its key columns unchanged, so a key read from the new side would be the not-supplied marker rather than a row.
- a **foreign-key** conflict, where SQLite hands the callback **no change at all** and reports only that the application could not be completed: `attribution` is `engine_reported_without_row`, the row fields are absent, and `detail` says so.

Nothing is fabricated to fill either gap. A row-level conflict whose change carried no readable key columns reports no `record_id` and must say so in `detail` rather than substitute a row identity, and **no violation count is reported for the foreign-key shape**: the pinned binding raises `ConstraintError` with no count in its arguments, so a number there would be the operation's own inference rather than the engine's report.

### Conventions

- `MergeBaseRequest._require_one_input_per_role` and `MergeRequest._require_every_role` refuse a request whose roles are not exactly one of each, which is why `MergeBaseRequest.input_for(role)` has an answer for every member of the union and needs no failure branch.
- `MergeCoverage._require_every_canonical_table` refuses a coverage record that omits a table, so "not attached" cannot be silently reported as "nothing to carry".
- `MergeConflict._require_consistent_conflict_facts` and `MergeOutcome._require_consistent_merge_outcome` refuse the mixed states at construction, so an inconsistent outcome is caught at the returning call site rather than by a caller's branch.
- `MergeCoverage.changed_tables()` and `table_operations()` are derived readers rather than a second stored field, so a coverage record cannot disagree with itself.

### Invariants And Boundaries

- **No field can carry a verdict.** The forbidden tokens are absent from `model_dump(mode="json")`, and the validators refuse `structurally_merged` without an identity and coverage, and refuse a conflict on a merged outcome.
- **A refusal still carries what was proven.** `MergeOutcome`'s refused state keeps the coverage measured *before* application, so a caller can see that the inputs were read completely even though nothing was published.
- **`MergeRequest` is not durable.** Its paths are a dataclass field precisely so they cannot be serialized into a stored value.
- **Boundary.** This module declares vocabulary. It performs no I/O, resolves no Git claim, applies no changeset and publishes nothing.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one non-refusal state name, which is the entire claim the operation makes. | `MERGE_STATES` | mcp/src/agents_remember/models/knowledge/merge.py:78-78 |
| The closed two-member base claim. | `SuppliedGitBase`; `ResolvedGitBase` | mcp/src/agents_remember/models/knowledge/merge.py:81-86; mcp/src/agents_remember/models/knowledge/merge.py:89-101 |
| The explicit input that carries the identity a caller admitted and a reference that is never resolved here. | `MergeInput` | mcp/src/agents_remember/models/knowledge/merge.py:110-121 |
| The base-resolution request and its exactly-one-input-per-role rule. | `MergeBaseRequest`; `input_for` | mcp/src/agents_remember/models/knowledge/merge.py:124-154; mcp/src/agents_remember/models/knowledge/merge.py:146-154 |
| The resolution that records which of the two base claims applied. | `MergeBaseResolution` | mcp/src/agents_remember/models/knowledge/merge.py:157-186 |
| The complete merge request, including the optional destination and why the paths are a dataclass. | `MergeRequest` | mcp/src/agents_remember/models/knowledge/merge.py:189-215 |
| The two coverage records that separate "changed" from "carried an operation" and cover every canonical table. | `TableCoverage`; `MergeCoverage` | mcp/src/agents_remember/models/knowledge/merge.py:218-240; mcp/src/agents_remember/models/knowledge/merge.py:243-284 |
| The conflict record's two shapes, the old-side key rule and the deliberately absent foreign-key row and count. | `MergeConflict` | mcp/src/agents_remember/models/knowledge/merge.py:293-346 |
| The outcome that carries identities, coverage and publication state and no verdict. | `MergeOutcome` | mcp/src/agents_remember/models/knowledge/merge.py:349-391 |
| The two operation names and twelve refusal codes this vocabulary is keyed by. | `KnowledgeOperation`; `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:36-36; mcp/src/agents_remember/models/knowledge/result.py:117-117; mcp/src/agents_remember/models/knowledge/result.py:116-116; mcp/src/agents_remember/models/knowledge/result.py:133-133; mcp/src/agents_remember/models/knowledge/result.py:220-221; mcp/src/agents_remember/models/knowledge/result.py:151-151; mcp/src/agents_remember/models/knowledge/result.py:161-191 |
| The node that confirms the published result carries no forbidden field and reports the coverage record. | "test_disjoint_edits_from_both_sides_survive_in_a_closed_published_candidate" | mcp/tests/test_knowledge_guarded_merge.py:248-312 |
| The boundary node that holds the conflict record to the engine's own row identity. | "test_the_conflict_record_prefers_the_old_side_and_reports_a_missing_key_as_such" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:165-184 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new merge vocabulary. It records the three load-bearing splits — an explicit input rather than a path the operation interprets, a base *claim* as a closed two-member union rather than a base the operation may pick, and a measurement rather than a verdict — plus the coverage distinction that makes the silent-omission class observable (`table_changed` read from the datasets versus `operations` counted from the changeset, over **every** canonical table) and the conflict record's two shapes. Two facts a consumer must not flatten are stated as the contract: a same-ID independent insert is a conflict even when the payloads are byte-identical, and the foreign-key shape reports no row and no violation count because the engine supplies neither. Verification metadata remains empty until closeout stamps the code commit.
