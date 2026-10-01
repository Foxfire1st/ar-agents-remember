# mcp/src/agents_remember/kernel/memory_backfill.py

## Governing Overview

[Nearest governing overview](../../../overview.md)

Committed-source review: inspected at 2026-09-15T03:43 UTC against `7cbda30d9a9a4c2944382fbef46ac58b85329935`.
Normal closeout owns final verification-metadata stamping for this committed source.

## Purpose

Plans and explicitly applies one-time memory-history attribution migration from a selected
historical ledger table. This migration reader is separate from runtime cache derivation.

## Code Commentary

### Logic

`MemoryBackfillRequest` names the memory repository, code repository, tip, historical table path,
rescue ref, and exact refs permitted to move. Planning resolves a branch-name tip to an exact commit
before reading its table, resolves abbreviated memory cells through Git, checks reachability and
code-object existence, and selects the trailers the history can carry.

Selection first seeks distinct code coverage through matching, then fills remaining eligible memory
commits with their own oldest claims. One effective trailer cannot represent two conflicting code
claims for the same memory commit, so skip reasons distinguish missing/unreachable data from
selection declines. Lost claims name the omitted code, contested memory commit, and winner.
`MemoryBackfillPlan` reports eligible rows, rewrites, named code commits, skips, and losses
separately; a plan with lost code claims is not empty, and its digest includes that distinction.

Apply optionally checks the preview digest and returns before rescue checks for an empty plan.
For work to perform, it validates rescue authority, writes and reads back rescue refs, rebuilds
commit objects with their trees, identities, timestamps, and remapped parents, then moves only the
named targets. The identity map includes unchanged commits, making reuse explicit.

`_walk` uses native `git rev-list --reverse --topo-order --all`. The topological ordering,
reversed for replay, visits every parent before its child even with tied or skewed commit dates.
`_rewrite_history` can therefore resolve remapped parent identities before rebuilding descendants;
date order alone is not the parent-ordering contract.

`_move_targets` resolves full ref names and emits one `update <ref> <new> <old>` command per changed
target to a single `update-ref --stdin` call. Commands are separated by one newline and the stream
ends with one newline; no blank command is inserted between targets. That fixes multi-ref apply
while preserving old-object checks and rescue reachability.

`ledger_rows_at` and `carry_ledger_cells` operate on explicit historical migration artifacts.
The carry resolves memory cells before remapping, retains code cells/code base, and updates memory
references and current headers. Carrying such a table is not required to make the runtime reader
find attribution: runtime reads now use the rewritten commit trailers alone.

### Conventions

Planning is a read-only description; applying it is a separate requested rewrite over named refs.
The kernel guarded Git runner carries the explicit input stream and commit identities. The migration
retains its historical-table `relative` input; runtime `read_ledger_source` no longer has one.

### Invariants And Boundaries

- Runtime cache absence never invokes this migration automatically.
- Missing mappings, declines, and losses remain observable rather than collapsed into a success count.
- Rescue refs precede target publication; only named refs may move.
- Multi-ref command framing contains no empty update command.
- Native reversed topological traversal resolves parent identities before rebuilding their children.
- This documentation pass makes no claim that shared history was rewritten or that a migration was approved to run.

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

- Typed request and plan reporting distinguish work, losses, and an empty plan. [1]
- Selection preserves available memory attributions and reports unrepresentable claims. [2]
- Apply orders digest/rescue/rewrite/publication and frames every target update correctly. [3]
- Historical table reads/carry remain explicit migration helpers. [4]
- The apply regression now moves two named refs and verifies the rescue tip. [5]
- Native topological traversal visits parents before their children during replay. [6]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
