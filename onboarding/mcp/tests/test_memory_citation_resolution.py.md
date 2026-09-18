# mcp/tests/test_memory_citation_resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_memory_citation_resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

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

### Conventions

The fixture owns code, memory, onboarding, and real Git history locally. Citation/source changes
and cached projection changes are tested separately. These assertions establish repository-owned
resolution behavior, not external documentation authority or a live verification receipt.

### Invariants And Boundaries

- Valid pooled claims remain valid while unsupported or escaped sources are refused.
- Cache absence/damage cannot invalidate real committed memory provenance.
- Actual cited source changes still reopen the claim.
- A mechanically moved range is not proof that its newly covered construct supports the claim.
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
| Mechanical projection prompts the support question rather than asserting currency. | `test_a_projected_range_is_enforced_with_the_support_question_not_currency` | mcp/tests/test_memory_citation_resolution.py:474-503 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
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
