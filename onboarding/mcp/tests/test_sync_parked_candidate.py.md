# mcp/tests/test_sync_parked_candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_sync_parked_candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Exercise the parked worktree candidate inside the existing sync transaction and prove its return, retained conflicts, cancellation, and recovery.

## Code Commentary

### Logic

The six cases reuse SyncFixture's real repositories and contracts. Clean code carry restores modified/untracked WIP and advances the recorded base. The external-memory case now includes staged cache data beside a real onboarding draft: only the draft appears in parked WIP, and the draft returns with no remaining stash.

Other cases preserve a genuine reapply conflict and its wipRestore marker, return the candidate on cancel, resume a crash before restoration, continue a staged source conflict without losing parked content, and refuse a pre-existing genuine unmerged index without creating a stash. The module validates the public resolution projection as well as the dictionary so producer/model drift is visible.

### Conventions

Intentional fault injection stops restoration once; native Git creates the genuine conflict. Assertions cover exact payload state, candidate bytes, stash identity/emptiness, and recorded bases. These are transaction-level scenarios, not a full closeout acceptance claim.

### Invariants And Boundaries

- Real parked content must return; a memory cache is not part of that candidate.
- A genuine reapply conflict retains the stash until resolution or cancellation.
- Resume must return an already-parked candidate without inventing another merge.
- Pre-existing real conflicts still refuse admission.
- Code-domain files keep ordinary semantics.

### Todos

No new file-local follow-up is identified by this source reconciliation.

## Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

| Finding | Anchor | Source |
| --- | --- | --- |

## Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

| Finding | Anchor | Source |
| --- | --- | --- |
| Code and memory WIP return, with cache excluded from the memory candidate. | `test_parked_candidate_is_carried_and_returned`; `test_parked_memory_candidate_is_carried_and_returned` | mcp/tests/test_sync_parked_candidate.py:30-54; mcp/tests/test_sync_parked_candidate.py:56-78 |
| Genuine reapply conflict and cancellation preserve candidate content. | `test_parked_candidate_reapply_conflict_is_retained_and_cancel_returns_it` | mcp/tests/test_sync_parked_candidate.py:80-115 |
| Crash recovery and retained-source continuation return parked work. | `test_resume_returns_the_candidate_a_crash_left_parked`; `test_resolving_a_retained_merge_returns_the_parked_candidate` | mcp/tests/test_sync_parked_candidate.py:117-144; mcp/tests/test_sync_parked_candidate.py:146-171 |
| Pre-existing genuine conflicts remain a refusal. | `test_unmerged_index_entries_still_refuse_the_sync` | mcp/tests/test_sync_parked_candidate.py:173-188 |
| Production parked-content boundary and exact restore proof. | `park_worktree_wip`; `prove_parked_wip_restored` | mcp/src/agents_remember/worktrees/sync_transaction_git.py:144-163; mcp/src/agents_remember/worktrees/sync_transaction_git.py:198-216 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Extended the existing memory-WIP case with staged cache data and an exact real-path assertion; retained the six clean, conflict, cancel, crash/resume, continuation, and pre-existing-conflict scenarios. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the shared sync fixture
  and park/restore owners are the frozen ones. Re-checked every case and helper range: they hold. No
  wording changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 7 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). 1 claim(s) were declined as ambiguous or not the subject
  and were left for a reading curator. No claim wording changed; every rewritten range was read back
  at its current position. Verification metadata remains closeout-owned.
- 2026-09-10T15:06+02:00 — Created for the parked-candidate change: the six transaction-level cases proving a dirty closeout candidate is parked, carried, and returned (with restore on completion, resume, and cancel, and the kept unmerged-index refusal). The new module has no committed identity yet, so verification remains closeout-owned.
