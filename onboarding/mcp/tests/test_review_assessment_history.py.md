# mcp/tests/test_review_assessment_history.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Pins the bounded unavailable-curator-channel detail when many retained evidence artifacts are missing.

## Code Commentary

The one remaining regression constructs a missing-evidence channel and monkeypatches review_curator_records._historical_records to raise its exact missing-artifact error. With 100 paths, the source assertions require unavailable, retain every unreadable path and abbreviate the detail; with ten paths whose detail fits PROSE_MAX_LENGTH, they keep the existing wording exactly.

This is a controlled error-rendering seam in the production channel reader. It does not execute normal assessment capture, cleanup, restart or exact-parent recovery. The former history journey inventory is removed coverage; the module's old broad docstring is not evidence that those tests remain.

## Evidence

### Docs References

No Domain Documentation source is configured for this slice.

### Repo-Internal References

- `_curator_channel` supplies the current fixture or assertion described above. [6]
- `test_a_leaf_binding_many_missing_curator_artifacts_reads_as_unavailable` supplies the current fixture or assertion described above. [7]
