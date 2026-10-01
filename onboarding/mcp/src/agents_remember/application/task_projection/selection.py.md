# mcp/src/agents_remember/application/task_projection/selection.py

## Governing Overview

[application overview](../overview.md)

## Purpose

The explicit projection read plan: how much a bound seat reads, and which channels it gets. This
module is the single place where "a worker must not receive the sprint's whole decision history"
is encoded as declared data rather than as a filter applied after loading everything.

## Code Commentary

### Logic

Two declared tables carry the whole decision:

- **`_READ_ALTITUDES`** is keyed by `(own altitude, parent bucket)` and is **total** over the nine
  pairs, so there is no default branch and no pair that silently falls back to a wider read. The
  `_PARENT_BUCKETS` vocabulary is `master`/`sprint`/`none`, where `none` covers a standalone leaf,
  a standalone master and every sprint.
- **`_OPERATION_CHANNELS`** maps each of the eight frozen `CapsuleOperation` members to the channel
  set that operation's projection carries. `operation_channels` **raises**
  `projection-operation-unsupported` for an unknown operation rather than returning an empty tuple:
  an operation with no channels would be indistinguishable from a seat with no obligations.

One rule is load-bearing and must not be relaxed: **a leaf-altitude seat never reads a
sprint-altitude ancestor.** A leaf reads its own document plus its immediate parent when that parent
is a **master**; when the immediate parent is a sprint, the leaf reads its own document only and the
sprint is reached by expansion reference instead. Ancestor decision logs are *referenced with their
entry count* — never injected — so "the smallest complete task projection" cannot become "the whole
series".

`_PORTFOLIO_FACTS` says whether a seat admits its own document's portfolio facts (a sprint's
commanded masters, seats and execution topology, or a master's series index). A leaf never does.
`read_plan` then removes the `portfolio` channel from any seat that is not entitled to it, so a
declared channel and an admitted channel are separate facts.

`_LAUNCHER_CHANNELS` is the launcher seat's whole projection — `objective` and `scope` only. The
ambient launcher is a **seat kind, not a tenth role**: it carries no decision history, no
preservation dossier and no handoff obligation it does not have.

### Invariants And Boundaries

- `_READ_ALTITUDES` must stay total over `(altitude, bucket)`. Adding a "convenient" extra read
  there breaks the altitude rule; seeded mutations `M01`/`M03` in the leaf's falsifiability probe
  target exactly that.
- A leaf never reads a sprint ancestor. This is a structural property of the table, not a runtime
  filter — do not replace it with one.
- `_OPERATION_CHANNELS` has exactly one entry per member of `CAPSULE_OPERATIONS`. A new operation
  in the frozen vocabulary without a channel set is a refusal, not an empty projection.
- The `portfolio` channel is filtered by `_PORTFOLIO_FACTS`, never by the operation table alone.
- `read_plan` takes no defaults for `altitude` or `operation`; a caller must state the binding.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking the configured sources.

### Repo-Internal References

The two tables, the refusal that guards the operation vocabulary, and the enforcement point that
consumes the plan.

- The total altitude table — the load-bearing rule that a leaf never reads a sprint. [1]
- Who admits portfolio facts, and the launcher's thin channel set. [2]
- The per-operation channel table and the refusal that guards it. [3]
- The plan builder that resolves the plan with no default branch. [4]
- The frozen operation and role vocabularies this table must cover exactly. [5]
- The single enforcement point that hands the projection only the planned documents. [6]
- The case that proves sprint history reaches an orchestrator but never a leaf. [7]
- The case that proves each frozen operation selects its own channels and its own document. [8]

### Cross-Repo References

No sibling-repository contract consumes this read plan.

No meaningful cross-repo references found.
