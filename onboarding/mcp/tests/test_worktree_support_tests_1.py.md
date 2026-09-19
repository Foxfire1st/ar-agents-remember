# mcp/tests/test_worktree_support_tests_1.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_worktree_support_tests_1.py` |
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

Exercises master/leaf start, attach, early binding refusal, queue projection, and leaf abandon
while preserving the parent series. The single retained scenario uses real temporary repositories
and task/worktree artifacts.

## Code Commentary

### Logic

The scenario creates a sprint with an atomic master and leaf, starts that leaf with external
memory, and checks the exact series/leaf branch and parent-contract relationships. It verifies the
leaf document's lifecycle/enclosure references and checks that reattach preserves them.

The early-closeout helper alters binding facts to prove refusal, then restores the task document.
The queue helper uses normalized code/memory messages and checks that the one member points to the
expected canonical leaf task. It no longer supplies a ledger message. Finally, abandon removes the
leaf enclosure while the parent series contract and its branch remain.

### Conventions

The card describes this retained method rather than restoring earlier split-family tests from
history. Shared support builds the repositories and typed inputs; the case checks public behavior
at its stated boundaries and does not stand in for every closeout route.

### Invariants And Boundaries

- Starting/attaching the leaf preserves canonical parent and document binding.
- Invalid binding is still refused before closeout work.
- Queue fixture intent uses only code and memory outputs.
- Abandoning the leaf must not remove the parent series contract or branch.

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
| The fixture queue and early refusal helpers retain typed inputs and exact bindings. | `_publish_and_read_leaf_queue`; `_assert_early_closeout_binding_refusals` | mcp/tests/test_worktree_support_tests_1.py:44-124; mcp/tests/test_worktree_support_tests_1.py:127-174 |
| The retained lifecycle scenario preserves the parent through start/attach/abandon. | `test_master_start_and_abandon_preserve_parent_series` | mcp/tests/test_worktree_support_tests_1.py:178-343 |
| Shared closeout arguments normalize the two real content messages. | `closeout_worktree_args`; `closeout_operation_input` | mcp/tests/closeout_input_test_support.py:417-438; mcp/tests/closeout_input_test_support.py:390-414 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:02 UTC — Documented the queue helper input after ledger-message retirement while retaining the one start/attach/refusal/abandon scenario and exact parent-series preservation checks. Working candidate verified by source inspection; commit metadata records real committed history only.

- 2026-09-09T12:22:46+00:00: Generated citation repair: `test_master_start_and_abandon_preserve_parent_series` repointed to mcp/tests/test_worktree_support_tests_1.py:179-344. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.

- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the closeout_args switch in worktree support tests 1.


- 2026-08-29T21:46+02:00 — MCAR-L03: added exact-pair reporting assertions to closeout preview.
  Dagger verification remains closeout-owned.

- 2026-08-26T14:32+02:00 — Moved the ledger round-trip scenario into the focused kernel test
  module, reducing this legacy omnibus below its structural limit without losing coverage.
  Verification remains closeout-owned.
- 2026-08-25T15:44+02:00 — PDLS whole-system reconciliation updated the implementation summary
  above after source and requirement review. Verification remains closeout-owned.


- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the test only repoints `start_contract` to its moved startup package. Verified at code commit `1d446724`.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: curated relationship changes against accepted candidate tree `4241908c`; verification metadata remains pinned until governed closeout.

- 2026-08-16T04:06+02:00 — Dagger fixture repair: memory-start previews patch the sole production `start.ensure_worktree` owner after its public-facade export was retired.
- 2026-08-15T23:38+02:00 — Reconciled the suite's L4 fixture and forcing role for protected integration branches, durable operation authority, external-memory parity, and recovery. Verification metadata remains closeout-owned.
- 2026-08-14T06:40+02:00 — L23 final candidate review: this split support suite retains start,
  status, and durable-operation regressions under canonical task identity. Verification remains
  closeout-owned.
- 2026-08-12T20:10+02:00 — L23 curator: documented refusal of standalone build topology without a master edge; verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-07T22:45:00+02:00 — 260731-EFA-L7 curator: created this file-level onboarding card for the split module; content derived from the current worktree source. Verification metadata pinned until closeout stamps the 260731-EFA-L7 commit.
## Docs References

No external Domain Documentation source is configured for this internal route; task `260821-CLIVE-L1` and the cited repository source/tests govern this curation.

## Cross-Repo References

This file owns no ambient cross-repository authority. Any external-memory repository it reaches remains explicitly contract-addressed.
