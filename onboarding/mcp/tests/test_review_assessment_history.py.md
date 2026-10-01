# mcp/tests/test_review_assessment_history.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Exercise normal owner assessment capture, cleanup/restart reading and explicit exact-parent recovery through production entry points.

## Code Commentary

### Logic

Fixtures publish two different exact-subject judgments through the guarded curator operation, invoke the public comparison command, remove disposable worktree state and read history through a fresh process. Later source or canonical-pointer movement must not replace the pinned objects or provenance.

The cases keep other channels available when a bound artifact is corrupted, distinguish measured-empty from uncaptured history, and prove explicit generation 2-to-3 recovery with unchanged parents and exact retry. Invalid parent/digest/source selection and reserved-owner impersonation refuse.

**The many-missing-artifacts case (MIK-L25 Q8, fixed in MIK-L31).** `_curator_channel` stubs `_historical_records` to raise the owner's own "Bound curator artifacts are unavailable: <paths>" error over a resolved leaf whose reserved owner evidence is missing, and returns the assessments channel. With 100 artifacts the channel is `unavailable`, lists all 100 as `unreadable`, and its detail names "100 bound artifacts" and the first ones, not the last. With 10 artifacts (review F6, strengthened by R2-2 so the two branches write different text) the landed detail fits `PROSE_MAX_LENGTH` and is kept exactly, without the summary phrase; forcing the summarising branch fails the case.

### Conventions

Use the existing typed owners and exact recorded identities. Keep operation evidence and candidate provenance in task notes.

### Invariants And Boundaries

These are disposable production-composition regressions. They do not mutate original L38/L40 records or establish installed-runtime/product acceptance.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured. The repository declarations below support this contract.

No configured domain source could be checked.

### Repo-Internal References

The cited owners carry the behavior and failure boundaries described above.

- Normal capture survives cleanup and later pointer/source movement. [1]
- Damaged expected artifacts isolate the affected channel. [2]
- Empty and uncaptured history remain different facts. [3]
- An over-length unreadable-owner detail is summarised; one that fits keeps its landed wording exactly; every artifact is listed either way. [4]
- Explicit successor recovery preserves parent bytes and judgments. [5]

### Cross-Repo References

No separate repository supplies this contract.

No cross-repository reference is required.
