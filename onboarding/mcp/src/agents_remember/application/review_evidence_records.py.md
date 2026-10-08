# mcp/src/agents_remember/application/review_evidence_records.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Composes review evidence from the selected candidate's published curator assessments, retained artifacts and measured binding currentness.

## Code Commentary

A resolved candidate reads the immutable curator authority and its artifact references. The returned channels distinguish an assessment collection from the currentness measurement of its exact dependency binding. Canonical detection, verification-observation and evidence-claim collections are retired and explicitly unavailable; they are not measured empty. An unresolved candidate yields unavailable channels. A task-context read without a selected matrix says not-selected for that collection. The removed `_claim_record` projection is not a current reader.

## Evidence

### Repo-Internal References

- `review_records_for_resolution` owns the current boundary described above. [30]
- `_retired_channel` owns the current boundary described above. [31]
- `without_selected_matrix` owns the current boundary described above. [32]
