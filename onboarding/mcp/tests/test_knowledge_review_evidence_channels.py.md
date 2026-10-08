# mcp/tests/test_knowledge_review_evidence_channels.py

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Checks review evidence-channel states and currentness measurement of published immutable curator assessments.

## Code Commentary

The converted fixture publishes assessments through their own authority. Cases distinguish unpublished from corrupt/unreadable authority, not-selected matrix collection, measured binding/currentness axes and stale candidates. Retained immutable generations survive damage to the live authority; an unresolvable candidate leaves collections unavailable. Channel counts are refused when their owner did not measure them. Canonical detection, evidence-claim and verification-observation producers and their former tests are removed; no empty-count replacement or executed run is claimed.

## Evidence

### Repo-Internal References

- `test_the_composition_measures_the_bindings_it_reads` owns the current boundary described above. [18]
- `test_a_retained_curator_generation_survives_a_damaged_live_authority` owns the current boundary described above. [19]
- `test_the_channel_model_refuses_a_count_no_owner_measured` owns the current boundary described above. [20]
- `test_an_unresolvable_candidate_reports_every_collection_unavailable` owns the current boundary described above. [21]
