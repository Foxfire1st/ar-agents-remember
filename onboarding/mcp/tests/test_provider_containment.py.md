# test_provider_containment.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Proves that a stale in-memory armed provider snapshot cannot override an unconfigured authority file on
disk. The retained case reloads launch authority and observes the veto. Since `260915-KS-L23` the file
also carries the **truthfulness of the `worktree_start` gate**: what its refusal actually tests, and the
declared-dependency check it never performed. Historical benchmark self-arming, setup-lock and
metrics-parser claims are no longer tests in this file.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

`WorktreeStartGateTruthfulnessTests` (`:93-144`) is the second subject in this file, added by
`260915-KS-L23` item 8 (D-17). It drives `worktree_start_tool` twice: once with a session lifecycle that
is bound and no longer fleeting, and once with the underlying start stubbed to `would-start`. Its two
cases and what they hold are stated in the section below.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Evidence

### Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

No external domain claim is required.

### Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

- Stale armed snapshot is vetoed by disk [1]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.

## KS-R23@v1 The Start Gate States What It Tests, And What It Did Not Check

`260915-KS-L23` item 8 (D-17) added `WorktreeStartGateTruthfulnessTests` (`:93-144`) beside the retained
veto case. `_bound_lifecycle()` (`:28-40`) supplies the session lifecycle a real start leaves behind:
bound, and no longer fleeting.

- `test_the_refusal_states_the_session_binding_rather_than_a_protected_lifecycle` (`:104-121`) — the
  refusal used to read *"worktree_start refuses to repoint the active persistent lifecycle"*, which
  described a protection that does not exist: the check reads only the session's **current** lifecycle
  and only its `fleeting` flag, so no other leaf, enclosure or session can block a start. The case
  asserts `lifecycle-switch-required`, that the summary says the session is already bound to another
  lifecycle, that it says no other leaf, enclosure or session can block the start, and that the
  mis-stated "persistent lifecycle" claim is **gone** rather than paraphrased into the same meaning.
- `test_a_start_result_reports_that_the_declared_dependencies_were_not_checked` (`:123-144`) — the tool
  never checked a leaf's declared `Requires` lines, so a `would-start` preview could be read as "this
  leaf's declared dependencies are satisfied". The case asserts the result's
  `eligibility.requiresCheck == "not-performed"` and that the detail names the `Requires` lines, so the
  check that was **not** performed travels with the answer.

Both cases are about the tool's own truthfulness rather than about provider containment; the retained
veto case and its armed-boot fixture are unchanged.
