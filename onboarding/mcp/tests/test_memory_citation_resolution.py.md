# mcp/tests/test_memory_citation_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash | `562cef4ca64de5b11712d5165d24e78c9a035312` |
| lastVerifiedCommitDate | 2026-09-19T17:51:43+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.
A later working candidate was inspected on 2026-09-18 by the 260915-KS-L23 curator: the four classes below are new and uncommitted on `ar/260915-ks-l23` (base `c5a74a85`), named in the `reviewedWorkingCandidate` metadata row.

## Purpose

Tests citation range, anchor, path, and provenance resolution, including retained history,
mechanically projected ranges, and Git-based memory-citation provenance independent of cache state.

## Code Commentary

### Logic

The existing grammar cases reject longer-identifier false matches, invalid ranges, absent anchors,
misplaced prose serialization, and parent traversal while retaining valid pooled ranges. Fenced
examples are ignored. Full and selected document walks share validation, and missing code-root
context remains an explicit finding rather than a quiet pass.

Retained prepared provenance distinguishes an admitted retained history from unrelated history.
The added memory case commits code and an attributed memory policy file, then cites that memory
source from an onboarding card. Valid, absent, and malformed consumer caches all leave provenance
checks clean and both repository HEADs unchanged. Changing the actual cited memory source then
surfaces `citation_claim_reopened`.

The mechanical-range cases retain their different support question: a generated projection bullet
for the same claim cannot establish that the newly cited construct supports the prose. That case
is enforced at error severity instead of silently asserting currency. Ordinary or unrelated
history bullets keep the existing warning-level changed-claim behavior.

Four classes added by 260915-KS-L23 cover the repair machinery itself. `InheritedProvenanceDebtTests`
builds a real memory repository with real Git history and pins both halves of the provenance-debt
rule: correcting one unrelated range in a document must not promote the ambiguous row the document
already carried (the demotion keys on the ROW's pre-task revision, so the corrected row is its own
while its untouched sibling stays inherited), a row the task created or edited stays enforced, and a
multiplicity row no edit can discharge is published as `closeoutOwnedFindings` with
`closeoutOwnedCount` rather than billed as repairable debt. `InsertedRegistrationRangeDriftTests`
drives the loader over a lane-registry fixture: an inserted registration leaves the anchor resolving
exactly once one line down, so the row is reported as a STALE BY A MOVE stale range in
`reportOnlyFindings` and never enters `findings`, while an anchor that resolves nowhere or twice keeps
the enforced finding — and its fourth case re-parses the SHIPPED `mcp/tests/test-evidence-lanes.toml`
to assert the append point is line-stable, contrasted with the mid-list insertion that does move a
row. `DecoratedDeclarationCitationTests` pins item 14: a card citing a decorated declaration at the
declaration's own lines is current, the range that includes the decorator line still passes, and a
range beginning inside the body still reopens — so the fix reads the declaration line without
relaxing the rule. `GeneratedHistoryInsertionOrderTests` drives the engine's own `history_edit` and
`rewritten` pair and judges the result with the shipped checker plus a direct read of the instants: a
UTC-stamped bullet older than the block's `+02:00` entries is inserted BELOW them, a genuinely newest
one still lands at the top.

### Conventions

The fixture owns code, memory, onboarding, and real Git history locally. Citation/source changes
and cached projection changes are tested separately. These assertions establish repository-owned
resolution behavior, not external documentation authority or a live verification receipt.

### Invariants And Boundaries

- Valid pooled claims remain valid while unsupported or escaped sources are refused.
- Cache absence/damage cannot invalidate real committed memory provenance.
- Actual cited source changes still reopen the claim.
- A mechanically moved range is not proof that its newly covered construct supports the claim.
- Inherited provenance debt is decided per ROW against the pre-task revision, not per document: a row the task created or corrected is the task's own and stays enforced.
- A multiplicity row is closeout-owned, never curator-repairable, and a pure move is report-only: neither may contribute to `ok` or to the curator-actionable count.
- Missing Git/code context remains explicit.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Grammar and path boundaries retain their dedicated assertion classes. | `test_1_a_word_boundary_is_not_satisfied_by_a_longer_identifier`; `ProseGrammarTests`; `DeletedClassTests` | mcp/tests/test_memory_citation_resolution.py:115-148; mcp/tests/test_memory_citation_resolution.py:151-181; mcp/tests/test_memory_citation_resolution.py:201-211 |
| Selected/full validation and missing-code-root reporting. | `test_without_a_code_root_the_result_says_so_instead_of_passing_quietly`; `test_full_and_selected_walks_share_canonical_document_validation` | mcp/tests/test_memory_citation_resolution.py:214-246 |
| Retained prepared history and cache-independent memory provenance. | `test_retained_prepared_commit_accepts_current_tree_and_rejects_other_history`; `RetainedPreparedProvenanceTests` | mcp/tests/test_memory_citation_resolution.py:249-381 |
| Mechanical projection prompts the support question rather than asserting currency. | `test_a_projected_range_is_enforced_with_the_support_question_not_currency` | mcp/tests/test_memory_citation_resolution.py:954-983 |
| Inherited provenance debt, pure-move reporting, deferred-declaration citation, and history insertion order. | `InheritedProvenanceDebtTests`; `InsertedRegistrationRangeDriftTests`; `DecoratedDeclarationCitationTests`; `GeneratedHistoryInsertionOrderTests` | mcp/tests/test_memory_citation_resolution.py:388-553; mcp/tests/test_memory_citation_resolution.py:554-680; mcp/tests/test_memory_citation_resolution.py:681-780; mcp/tests/test_memory_citation_resolution.py:781-863 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_a_projected_range_is_enforced_with_the_support_question_not_currency` repointed to mcp/tests/test_memory_citation_resolution.py:954-983. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:22+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the four test classes this change adds, which the card did not carry, and added their reference row. `InheritedProvenanceDebtTests` (row-keyed demotion, closeout-owned multiplicity rows), `InsertedRegistrationRangeDriftTests` (a pure move is a report-only stale range; a gone or ambiguous anchor stays enforced; the shipped lane manifest's append point is line-stable), `DecoratedDeclarationCitationTests` (a decorated declaration cited at its own lines is current, the decorator-inclusive range still passes, a range starting in the body still reopens), and `GeneratedHistoryInsertionOrderTests` (a UTC-stamped bullet is inserted by parsed instant, with the newest-bullet case as its control). Added the corresponding invariant bullets: inherited debt is per ROW against the pre-task revision, and neither a multiplicity row nor a pure move may contribute to `ok` or to the curator-actionable count. Documentation only: no test byte was touched by this pass, and no case is claimed as executed here — execution evidence is the seat's, not this card's. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are NOT advanced — these sources are uncommitted, so no commit carries their bytes; the candidate is named in the `reviewedWorkingCandidate` metadata row and the governed closeout owns the real commits.

2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:02 UTC — Added the Git memory-provenance scenario to the card: valid/missing/malformed caches preserve provenance and repository HEADs, while real policy-source changes reopen the citation. Retained grammar, source isolation, and mechanical-projection evidence boundaries. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-13T02:05+02:00 — 260831-LOCR-L33 curator (delta after publish): re-pointed
  `MechanicallyProjectedRangeTests`. The projected item moved from report-only to enforced, so the
  old assertion that it was *surfaced* at `severity: warning` is replaced: the test is renamed
  `test_a_projected_range_is_enforced_with_the_support_question_not_currency` and now asserts
  `surfacedFindings == []`, exactly one enforced finding, `severity == "error"`, `ok is False`, and
  the no-git-view fail-closed fact, while keeping every original message assertion. The companion
  test additionally asserts `findings == []` and `warning` for the ordinary item. Nothing was removed
  or weakened. Verification metadata remains closeout-owned; no acceptance claim.

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded the new `MechanicallyProjectedRangeTests` class and both of its tests — a mechanically projected range is surfaced with the support question ("NOT shown to be current", the generated bullet, the new range, the construct question) instead of a currency assertion, while a history without this claim's bullet keeps the older currency assertion — and noted that severity deliberately stays `warning` because whether a projected range should block is an undecided policy call. Corrected every reference range to the measured source. Verification metadata remains closeout-owned. **Superseded by the entry above: the severity call is now made, and the projected item is enforced.**

- 2026-09-10T00:00+02:00 — CCR-L42 current-candidate curation: added the canonical-walk and retained-prepared-provenance regression coverage to the current test card; verification metadata remains closeout-owned.

- 2026-09-06T21:46+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
