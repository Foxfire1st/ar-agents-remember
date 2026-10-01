# mcp/tests/test_memory_backfill.py

## Governing Overview

[Nearest governing overview](overview.md)

Committed-source review: inspected at 2026-09-15T03:43 UTC against `7cbda30d9a9a4c2944382fbef46ac58b85329935`.
Normal closeout owns final verification-metadata stamping for this committed source.

## Purpose

Exercises explicit historical-memory attribution migration with disposable real repositories:
selection and loss accounting, message/object replay, rescue and named-ref safety, table-artifact
carry, and the actual CLI path.

## Code Commentary

### Logic

The plan cases check that carryable memory pairings receive attribution, conflicts follow the
recorded order rather than hash order, and losses name their winners. Missing objects, unreachable
commits, code commits absent from their repository, abbreviated cells, stable digests, and digests
that distinguish lost claims are separate assertions.

Apply cases read real trailers, prove a second run changes no refs, compare trees/identities/dates,
and require a total rewritten-ID map. The trailer-only proof now calls the ordinary
`read_ledger_source` directly: that runtime API has no table fallback, so the old fabricated absent
`relative` path is no longer needed.

`test_the_rescue_ref_holds_the_original_tip_before_the_rewrite` now creates two named target refs,
applies to both in the same request, verifies the rescue still holds the original tip, and checks
both targets moved to the returned new tip. This exercises the newline-framed multi-ref stdin batch.
Other cases retain rescue collision/namespace and stale-preview-digest refusals.

Historical table-reading cases intentionally permit a disagreeing header while refusing an absent
migration table. Table carry checks resolved abbreviations, unchanged code cells/code base, and
updated memory IDs. Those are migration-artifact contracts, not runtime cache authority. CLI cases
exercise a branch-name tip and retry after apply through the real argument/command functions.

The existing CLI branch-name/retry case also creates `ar/peer` and passes two explicit `--ref`
arguments to apply. It verifies that the peer reaches the same rewritten tip as the leaf, reads the
retained rescue tip and both attributions, then repeats apply with the same target set while
checking that the rescue ref and leaf tip stay unchanged. This extends the retained CLI case;
it adds no new test definition.

### Conventions

Each class builds disposable repositories with explicit identities and cleanup. The test module
uses actual object IDs and Git readers rather than treating returned strings as proof. Historical
cache commits and rescue refs are fixture data; no shared repository is rewritten by these tests.

### Invariants And Boundaries

- Multi-ref apply must update every named target while retaining the original rescue tip.
- Unrepresentable claims and data holes remain observable.
- The runtime proof reads only committed trailers; historical tables are used only by explicit migration cases.
- Tree/identity/date preservation and same-history idempotence stay asserted.
- Test source and focused results are not authorization or evidence of a live backfill.

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

- Plan selection distinguishes conflict outcomes, missing data, and stable/loss-sensitive digests. [1]
- The actual two-ref apply regression retains the original rescue tip. [2]
- Runtime proof uses the ordinary Git-only reader. [3]
- Historical table read/carry and real CLI boundaries stay covered. [4]
- The production target-update stream emits exactly one newline between commands. [5]
- The existing CLI case applies two named refs and retries the same target set. [6]
- The committed implementation uses native reversed topological traversal. [7]

### Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

No additional configured cross-repository evidence.
