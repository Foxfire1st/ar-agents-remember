# test_read_ar_files.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Checks paired source reading: exact ranges and full bytes, binary omission, traversal and symlink confinement, first-read overview attachment, unchanged-onboarding deduplication, changed/refresh reservation, compact-marker reset and committed-source payload reading. Since 260921-ICR-L19 the same module is also the suite for the route's **published-intent half** (ICR-R19@v1): the ordinary read resolves the repository's published knowledge dataset from its coordination context and reads the recorded intent about each requested path at that dataset's own snapshot — or names, by its exact binding, why it could not. Since MIK-R24 the ordinary read of unconverted memory is `legacy-format`, so these cases measure the database block beside the read rather than inside it (see Logic). It does not claim the removed broad served-ledger durability or facts-packet suites remain here.

## Current source account

The added equal-overview case constructs a second code/onboarding root with identical overview text. Each root receives its first repository/route overviews and then deduplicates its own repeat, proving served-overview state is isolated by roots rather than suppressing one root because another served equal bytes.

## Code Commentary

### Logic

The current evidence boundary is the source-listed behavior below. Earlier coverage claims in
history describe prior populations and must not be used to recreate removed tests or claim they
still run. The retained behavior and its fixture limits, described above, govern this card.

The published-intent half is two classes. `PublishedIntentRouteTests` drives the application entry point
with a real dataset written at the memory layer's own name: the identity round trip, the four named
absences and refusals, the source-pair observation, an identity-seeded page, and one carrier-parity case
that derives the payload's field spellings from a real page rather than restating them.
`PublishedIntentMountedRouteTests` drives the **mounted** `read_ar_files` route over a real coordination
tree, so the block is measured through the call an agent actually makes rather than only beside it.

**Since MIK-R24 (rule 9) both classes run on unconverted memory, which `read_ar_files` now reads as
`legacy-format`.** `PublishedIntentRouteTests._read` asserts that the payload's block is
`legacy-format`, then replaces it with `published_intent_block(context, paths)`. So the ICR-R19 cases still
measure the database publication route itself, directly rather than through the tool. The carrier-parity
case measures the unrequested block the same way. The two mounted cases were rewritten: one asserts that
an unconverted memory tree holding a database and a card returns `legacy-format`, with the memory root,
a detail naming the crossing sync, and the source bytes. The other asserts `legacy-format` before anything
is published. The converted-tree knowledge section is asserted through `read_ar_files` in
`test_knowledge_conversion_toolchain.py`, and at block level by MIK-R23's index tests; the reviewer
accepted this as equivalent coverage (architect ruling).

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

- Range request returns exact slice [1]
- Full read is not truncated [2]
- Binary source is omitted [3]
- Path confinement rejects escape [4]
- Symlink file escape rejected [5]
- Symlink dir escape rejected [6]
- First read attaches overview and route chain [7]
- Second read dedups unchanged pieces [8]
- Changed overview is reserved [9]
- Refresh forces reserve [10]
- Compact marker resets served [11]
- Payload reads committed source [12]
- **The published-intent half's headline case: the ordinary read returns the repository's published intent at its exact identities, and the source bytes ride in the same payload.** [13]
- **The carrier-parity case: the payload's real field spellings are derived from a real page, and the camelCase variants are rejected.** [14]
- **The four named absences and refusals: nothing published, bytes that are not a dataset, a directory at the publication path, and a seed that is not a typed seed.** [15]
- **The four selection and identity refusals: another repository's dataset, a path the snapshot records nothing about, an identity the snapshot does not hold, and a path no recorded anchor could carry.** [16]
- **The source pair and the identity seed: the resolved pair is what recorded anchors are observed against, and an identity-seeded page carries the exact retained revisions.** [17]
- **The mounted route, which is the call an agent actually makes: on unconverted memory it returns no knowledge section and names the legacy format, with and without a database.** [18]
- The route-class read helper asserts `legacy-format`, then measures the database block directly. [19]
- The published-intent fixtures, including the `_selection()` narrowing helper the type-checked call sites need. [20]

### Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

No external evidence is needed for these assertions.
