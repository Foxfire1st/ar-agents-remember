# mcp/src/agents_remember/worktrees/integration/mutation_evidence.py

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

`ephemeral_git_mutation_snapshot` copies the repository's index with `kernel.git_command.copy_git_index`, which
keeps the index file's modification time. Git compares a file by content when it may have been rewritten in the
second its index was written, and it knows that from the index file's own time. A plain copy has a new time, under
which Git trusts every entry's recorded stat data; with the time kept, a same-size rewrite in that second enters
the snapshot's candidate tree with its new blob (INV-656CYW). The closeout's judged-tree check reads this snapshot.

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

- Only enabled code/memory legs receive mutation cells. [1]
- Intent, expected-output binding, and commit proof retain their order. [2]
- Interrupted attempts are reconciled from actual Git evidence. [3]

- Cache-excluded snapshots retain actual object/ref identity. [4]

- The snapshot model declares the separate content comparison tree. [5]

- The disposable snapshot copies the index with its time. [6]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
