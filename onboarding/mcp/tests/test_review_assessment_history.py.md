# mcp/tests/test_review_assessment_history.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Pins the bounded unavailable-curator-channel detail when many retained evidence artifacts are missing.

## Code Commentary

The one remaining regression constructs a missing-evidence channel and monkeypatches review_curator_records._historical_records to raise its exact missing-artifact error. With 100 paths, the source assertions require unavailable, retain every unreadable path and abbreviate the detail; with ten paths whose detail fits PROSE_MAX_LENGTH, they keep the existing wording exactly.

This is a controlled error-rendering seam in the production channel reader. It does not execute normal assessment capture, cleanup, restart or exact-parent recovery. The former history journey inventory is removed coverage; the module's old broad docstring is not evidence that those tests remain.

### Logic

**The many-missing-artifacts case (MIK-L25 Q8, fixed in MIK-L31).** `_curator_channel` stubs `_historical_records` to raise the owner's own "Bound curator artifacts are unavailable: <paths>" error over a resolved leaf whose reserved owner evidence is missing, and returns the assessments channel. With 100 artifacts the channel is `unavailable`, lists all 100 as `unreadable`, and its detail names "100 bound artifacts" and the first ones, not the last. With 10 artifacts (review F6, strengthened by R2-2 so the two branches write different text) the landed detail fits `PROSE_MAX_LENGTH` and is kept exactly, without the summary phrase; forcing the summarising branch fails the case.

### Conventions

Use the existing typed owners and exact recorded identities. Keep operation evidence and candidate provenance in task notes.

### Invariants And Boundaries

These are disposable production-composition regressions. They do not mutate original L38/L40 records or establish installed-runtime/product acceptance.

### Todos

None recorded.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `_curator_channel` supplies the current fixture or assertion described above. [6]
- `test_a_leaf_binding_many_missing_curator_artifacts_reads_as_unavailable` supplies the current fixture or assertion described above. [7]

The cited owners carry the behavior and failure boundaries described above.

### Docs References

No Domain Documentation source is configured. The repository declarations below support this contract.

No configured domain source could be checked.

- An over-length unreadable-owner detail is summarised; one that fits keeps its landed wording exactly; every artifact is listed either way. [8]

### Cross-Repo References

No separate repository supplies this contract.

No cross-repository reference is required.
