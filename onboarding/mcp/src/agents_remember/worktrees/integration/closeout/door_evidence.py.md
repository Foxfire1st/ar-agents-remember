# mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:15+00:00 |
| lastVerifiedCommitHash | `4ef4dddc9194930611db2b1dfbb6e02113f2226a` |
| lastVerifiedCommitDate | 2026-09-20T15:00:59+02:00|
| verificationStatus | working-candidate |
| governingOverview | `overview.md` |

The body describes the uncommitted LCA L9 working candidate. The commit fields identify the latest real commit touching this source file; they do not claim that the candidate is committed or accepted.

## Governing Overview

[Nearest governing route overview](overview.md)

## Purpose

Capture the exact code, memory-content, review, and source-base evidence for a closeout-door generation.

## Code Commentary

### Logic

`require_source_bases_current` proves transitive source lineage and exact immediate code/memory source heads before candidate capture. The evidence fingerprint includes code and memory candidate trees, recorded bases, and review/memory provenance. The memory tree is built through the shared private-index helper with root `memory.md` excluded. Ledger bytes, mapping rows, ledger provenance, and a ledger commit are absent from the evidence model and stale checks.

Review provenance still consumes the current route-review record when applicable. No-code-change and explicit atomic deferrals produce non-applicable provenance; an applicable review must match the candidate tree and task intent and must not block. Its fingerprint is the review record digest. Task evidence files remain confined to the task root and their bytes are hashed. External-memory curator evidence retains its own existing provenance boundary.

### Conventions

One evidence snapshot feeds declaration and comparison. The cache exclusion changes only memory candidate identity; source refs, substantive memory content, review evidence, and task intent keep their own checks.

### Invariants And Boundaries

- Cache damage cannot alter a door fingerprint or create a ledger-provenance blocker.
- Real code/memory tree or source-base changes remain stale evidence.
- Review evidence is task-confined and bounded; its record digest remains the provenance identity.
- Disposable projections can describe the generation but cannot replace its evidence.

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
| The door candidate contains only real candidate/base and review/memory facts. | `DoorCandidateEvidence` | mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:37-54 |
| Current source bases and cache-excluding memory tree capture. | `require_source_bases_current`; "memory.md" | mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:57-95; mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:98-107 |
| Review and task evidence remain independently validated. | `_review_provenance`; `_door_task_evidence` | mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:168-247 |
| Cache changes leave memory candidate identity stable while real content changes it. | `test_start_and_memory_candidate_do_not_take_authority_from_the_cache` | mcp/tests/test_worktree_sync.py:581-613 |

## Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.

| Finding | Anchor | Source |
| --- | --- | --- |

## Update History
- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator, **memory-side sync conflict resolved as a UNION; no side dropped.** The memory source branch advanced to `92f444b04` (260915-KS-L45) while this leaf's curation was in flight, so the sync's re-apply conflicted in this file. Both sides were kept because both are true: 260915-KS-L45's landed additions (the Intent-review entry path, the two published half-names `REVIEW_BASELINE_DIRECTORY`/`REVIEW_CANDIDATE_DIRECTORY`, the `missing_dataset_half` pair preflight, the receipt-derived `review_namespace`, and the enumerating reads) and this leaf's 260915-KS-L43 edits (the allocated-identity/derived-citation split, the retry key and its journal, the explicit anchor reuse, and the recovery's journaled decisions with the bounded cycling refusal). Where the two sides carried the same row in different line numbers, the row was re-measured against the moved line rather than picked: L45 curated against `fb719f89` and this leaf's source moves every citation below `:306` of `knowledge_curator_ingest.py` and renumbers `cli/knowledge_ingest.py` entirely, so the surviving ranges are the post-merge measurement for both. One **contradiction** is recorded rather than silently resolved: the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` frontmatter pair is L45's (recorded against the moved line, the newest verification on record), while the `reviewedWorkingCandidate` row is this leaf's reading — two different claims, kept beside each other instead of one overwriting the other. No verification stamp was advanced by this leaf.
- 2026-09-20T12:00:25+00:00: Generated citation repair: `test_start_and_memory_candidate_do_not_take_authority_from_the_cache` repointed to mcp/tests/test_worktree_sync.py:581-613. No content impact: mechanical anchor-range projection bound to citation source snapshot 23094be373d669ad77475ab6ebb610401913ce4b65c82d3b4cc642eb6bb44e43; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T11:53:49+00:00: Generated citation repair: `test_start_and_memory_candidate_do_not_take_authority_from_the_cache` repointed to mcp/tests/test_worktree_sync.py:581-613. No content impact: mechanical anchor-range projection bound to citation source snapshot 0849f052762b22876ef5b9a278767e8b11854dff23a8149d48010a306f68021a; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T03:57:45+00:00: Generated citation repair: `test_start_and_memory_candidate_do_not_take_authority_from_the_cache` repointed to mcp/tests/test_worktree_sync.py:507-539. No content impact: mechanical anchor-range projection bound to citation source snapshot ef4a9932e0393a408ecd0f26b5bc2e0e1e335ad90b9e47a16092ffd6f3403af3; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-20T00:16:01+00:00: Generated citation repair: `test_start_and_memory_candidate_do_not_take_authority_from_the_cache` repointed to mcp/tests/test_worktree_sync.py:274-306. No content impact: mechanical anchor-range projection bound to citation source snapshot b8fe5b3589f1357e836aaad1587e69ed38bbda0d58221eaa2150e96eb0561e93; claim bytes unchanged; generated by ccr-r10@v1.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:15+00:00 — 260913-LCA-L9 working candidate: Removed ledger mapping/provenance fields and cache-byte hashing; memory candidate identity now excludes memory.md while real source, content, review, and curator facts remain. Current source and citation targets were checked; the metadata records the last real file commit, and candidate changes remain uncommitted.
- 2026-09-09T12:22:46+00:00: Generated citation repair: `capture_door_candidate_evidence`; `DoorCandidateEvidence` repointed to mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:167-203; mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py:39-60. No content impact: mechanical anchor-range projection bound to citation source snapshot 06f99a0e57ce8b514dd7ed6685874da5285e3ec2e8c4a3f6a5d768b622094451; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the route-review currentness re-requirement and the record-digest review provenance fingerprint; prior capture and fail-closed prose preserved.

- 2026-08-26T14:32+02:00 — Corrected stale uniqueness wording to match the source's newest-first
  `find_mapping` authority; no door behavior changed. Verification remains closeout-owned.

- 2026-08-25T08:16+02:00 — 260824-PDLS wave 004: moved this preserved sidecar with its behavior-preserving package split, repointed source evidence, and verified the emergency-landed source path at code commit `cb6623775a04cbdeb0509dc26f08a8268189c3f6`; this is onboarding provenance, not Dagger certification.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: created from the final evidence owner. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.
