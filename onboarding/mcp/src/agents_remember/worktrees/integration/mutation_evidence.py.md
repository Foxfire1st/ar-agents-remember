# mcp/src/agents_remember/worktrees/integration/mutation_evidence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/mutation_evidence.py` |
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

Owns code/memory Git-mutation evidence: accepted snapshots, intent publication, expected-output
binding, exact commit proof, and reconciliation of interrupted attempts. The retired ledger leg is
not part of this evidence vocabulary.

## Code Commentary

### Logic

`initial_closeout_mutation_evidence` creates cells for enabled code and memory legs only.
Mutation entry points check the effective leg and exact contract repository. Intent captures
pre-command evidence; the exact-file variant computes its intended tree before a real file write,
while `bind_expected_output_tree` fills an unbound prepared output before commit launch.

`prove_git_commit` reads the actual repository and requires the bound ref, output tree, commit, and
accepted parent relation before publishing a proven receipt. `reconcile_closeout_mutations` separates
an exactly unchanged attempt from an actual expected output. An unreadable or contradictory
intermediate state leaves intent unresolved for the owning recovery path.

Memory observations pass `memory_cache=True`. Their status, index, and candidate comparisons exclude
the root consumer cache; the snapshot retains actual `head`, `headTree`, and ref/reflog identity and
adds `contentHeadTree` for cache-excluded cleanliness. `snapshot_is_clean_at_head` compares the index
and candidate with that content tree when present. Disposable snapshot work uses isolated index and
object directories. Code snapshots keep their normal full-content semantics.

The former pending-ledger-intent special case and ledger repository/cell mapping are removed.
Recovery/cancellation still depend on actual mutation evidence; a desired output tree alone is not
proof that Git committed it.

### Conventions

The shared snapshot predicate is the only cleanliness definition used by direct execution and
recovery. Progress callbacks can record typed evidence in-process; the caller's operation owner
controls durable publication and generation transitions.

### Invariants And Boundaries

- Enabled leg and exact repository authority are checked before mutation.
- Actual commit/ref/tree and accepted parent evidence remain authoritative.
- Cached bytes, staged cache entries, and cache conflicts do not determine memory cleanliness.
- Only code and memory outputs are modeled; no ledger third-leg exception remains.
- Ambiguity cannot be rewritten into a false unchanged or successful receipt.

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
| Only enabled code/memory legs receive mutation cells. | `initial_closeout_mutation_evidence` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:60-81 |
| Intent, expected-output binding, and commit proof retain their order. | `bind_expected_output_tree` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:246-267 |
| Interrupted attempts are reconciled from actual Git evidence. | `reconcile_closeout_mutations` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:304-360 |
| Cache-excluded snapshots retain actual object/ref identity. | `ephemeral_git_mutation_snapshot` | mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:410-473 |
| The snapshot model declares the separate content comparison tree. | `contentHeadTree` | mcp/src/agents_remember/models/lifecycles/mutation_evidence.py:26-26 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:02 UTC — Reconciled the evidence owner with code/memory-only legs, contentHeadTree and cache-excluded memory observations; removed stale ledger-intent exceptions while preserving actual ref/tree/parent proof and ambiguity handling. Working candidate verified by source inspection; commit metadata records real committed history only.

- 2026-09-11T23:05:00+00:00: Repaired two claims. The card claimed `require_closeout_mutation_authority` made journal authority mandatory for non-preview closeout and listed it as a current module seam; that gate (JOURNALED_CLOSEOUT_REQUIRED plus its five internal call sites, the `modules/closeout.py` call and the CLI refusal) is deleted, and the module now validates an enabled leg and its contract repository through `_require_mutation_leg_authority` (555-567), with `initial_closeout_mutation_evidence` (60-80) and `begin_git_mutation` (83-102) unchanged.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `snapshot_is_clean`; `snapshot_is_clean_at_head` repointed to mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:37-39; mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:42-57. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `begin_git_mutation` repointed to mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:83-102. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `prove_git_commit` repointed to mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:263-292. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-11T22:39:01+00:00: Generated citation repair: `reconcile_closeout_mutations` repointed to mcp/src/agents_remember/worktrees/integration/mutation_evidence.py:295-364. No content impact: mechanical anchor-range projection bound to citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-06T22:00:40+00:00 — Corrected current journal recovery semantics against production source while preserving previous verification pins. Source inspection only.


- 2026-08-27T18:33+02:00 — Centralized the exact clean-snapshot predicate previously duplicated
  by direct execution and recovery state; no mutation or recovery acceptance semantics changed.
- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout-input model package relocation; intent-before-Git mutation evidence and exact reconciliation are unchanged.
- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: reconciled this card with the accepted full L2 candidate; verification metadata remains pinned until architect-owned closeout stamps the real code commit.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1: created from candidate tree `4241908c`; verification metadata remains blank pending landed commit.
