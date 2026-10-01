# mcp/src/agents_remember/worktrees/integration/closeout/door_evidence.py

| Field | Value |
| --- | --- |
| verificationStatus | working-candidate |

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

## Evidence

### Docs References

No domain-documentation source is configured for this slice. The behavior described here is established by current repository source and the authorized LCA L9 change, rather than an invented external reference.

### Repo-Internal References

These current source spans identify the implementation owners and the specific assertions supporting the file's behavior. A test definition is evidence of its assertions, not an execution or certification receipt.

- The door candidate contains only real candidate/base and review/memory facts. [1]
- Current source bases and cache-excluding memory tree capture. [2]
- Review and task evidence remain independently validated. [3]
- Cache changes leave memory candidate identity stable while real content changes it. [4]

### Cross-Repo References

The operation and fixture boundaries described here are defined by same-repository contracts and Git helpers. No separate cross-repository document is used as evidence for this card.
