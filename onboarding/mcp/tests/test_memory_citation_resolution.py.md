# mcp/tests/test_memory_citation_resolution.py

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.
A later working candidate was inspected on 2026-09-18 by the 260915-KS-L23 curator: the four classes below are new and uncommitted on `ar/260915-ks-l23` (base `c5a74a85`), named in the the recorded working candidate metadata row.

## Purpose

Tests citation range, anchor, path, and provenance resolution, including retained history,
mechanically projected ranges, and Git-based memory-citation provenance independent of cache state.

## Code Commentary

### Logic

The existing grammar cases reject longer-identifier false matches, invalid ranges, absent anchors,
misplaced prose serialization, and parent traversal while retaining valid pooled ranges. Fenced
examples are ignored. Full and selected document walks share validation, and missing code-root
context remains an explicit finding rather than a quiet pass.

Retained prepared provenance distinguishes an admitted retained history from unrelated history.
The added memory case commits code and an attributed memory policy file, then cites that memory
source from an onboarding card. Valid, absent, and malformed consumer caches all leave provenance
checks clean and both repository HEADs unchanged. Changing the actual cited memory source then
surfaces `citation_claim_reopened`.

The mechanical-range cases retain their different support question: a generated projection bullet
for the same claim cannot establish that the newly cited construct supports the prose. That case
is enforced at error severity instead of silently asserting currency. Ordinary or unrelated
history bullets keep the existing warning-level changed-claim behavior.

Four classes added by 260915-KS-L23 cover the repair machinery itself. `InheritedProvenanceDebtTests`
builds a real memory repository with real Git history and pins both halves of the provenance-debt
rule: correcting one unrelated range in a document must not promote the ambiguous row the document
already carried (the demotion keys on the ROW's pre-task revision, so the corrected row is its own
while its untouched sibling stays inherited), a row the task created or edited stays enforced, and a
multiplicity row no edit can discharge is published as `closeoutOwnedFindings` with
`closeoutOwnedCount` rather than billed as repairable debt. `InsertedRegistrationRangeDriftTests`
drives the loader over a lane-registry fixture: an inserted registration leaves the anchor resolving
exactly once one line down, so the row is reported as a STALE BY A MOVE stale range in
`reportOnlyFindings` and never enters `findings`, while an anchor that resolves nowhere or twice keeps
the enforced finding — and its fourth case re-parses the SHIPPED `mcp/tests/test-evidence-lanes.toml`
to assert the append point is line-stable, contrasted with the mid-list insertion that does move a
row. `DecoratedDeclarationCitationTests` pins item 14: a card citing a decorated declaration at the
declaration's own lines is current, the range that includes the decorator line still passes, and a
range beginning inside the body still reopens — so the fix reads the declaration line without
relaxing the rule. `GeneratedHistoryInsertionOrderTests` drives the engine's own `history_edit` and
`rewritten` pair and judges the result with the shipped checker plus a direct read of the instants: a
UTC-stamped bullet older than the block's `+02:00` entries is inserted BELOW them, a genuinely newest
one still lands at the top.

### Conventions

The fixture owns code, memory, onboarding, and real Git history locally. Citation/source changes
and cached projection changes are tested separately. These assertions establish repository-owned
resolution behavior, not external documentation authority or a live verification receipt.

### Invariants And Boundaries

- Valid pooled claims remain valid while unsupported or escaped sources are refused.
- Cache absence/damage cannot invalidate real committed memory provenance.
- Actual cited source changes still reopen the claim.
- A mechanically moved range is not proof that its newly covered construct supports the claim.
- Inherited provenance debt is decided per ROW against the pre-task revision, not per document: a row the task created or corrected is the task's own and stays enforced.
- A multiplicity row is closeout-owned, never curator-repairable, and a pure move is report-only: neither may contribute to `ok` or to the curator-actionable count.
- Missing Git/code context remains explicit.

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

- Grammar and path boundaries retain their dedicated assertion classes. [1]
- Selected/full validation and missing-code-root reporting. [2]
- Retained prepared history and cache-independent memory provenance. [3]
- Mechanical projection prompts the support question rather than asserting currency. [4]
- Inherited provenance debt, pure-move reporting, deferred-declaration citation, and history insertion order. [5]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
