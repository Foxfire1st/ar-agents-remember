# mcp/tests/test_knowledge_file_formats.py

## Governing Overview

[tests route overview](overview.md)

## Purpose

**MIK-R21's model, ID and location cases.** It proves the text knowledge format's shapes accept the
Doc14 §4 worked examples (as fixtures in `fixtures/knowledge_files/`, adapted to the packet's
normative shape) and refuse the non-conforming ones, pins the ID derivation with golden values, and
checks the layout paths. Registered in the `unit-regression` lane.

## Code Commentary

### Logic

- IDs: `test_minted_ids_are_random_crockford_with_their_kind_prefix` (2000 mints, `INV-0143`
  refused) and `test_derived_ids_are_eight_characters_and_deterministic` (golden `FAM-SEQNTS6C`,
  `INV-SEQNTS6C`, `RLZ-0QYX992Q`, the last recomputed from its literal material string).
- Doc14: `test_doc14_worked_examples_validate_and_round_trip_byte_for_byte` parses all nine
  fixtures to their expected model and re-serializes them to identical bytes;
  `test_doc14_verbatim_illustrative_shapes_are_refused` keeps Doc14's verbatim `supersedes: null` and
  `{code:{symbol}}` and proves they are refused, so the adaptation is deliberate.
- Kinds: `test_every_record_kind_parses_round_trips_and_refuses_a_foreign_prefix` is parametrized
  over all ten kinds (foreign prefix, undeclared field, every out-of-vocabulary relation refused);
  `test_facet_records_carry_todays_payload_fields_plus_links` compares facet fields with
  `models/knowledge/facet.py`.
- Refusals: `test_records_refuse_second_owners_and_malformed_record_fields`,
  `test_links_carry_their_relation_rules`, `test_sidecars_references_and_anchors_refuse_malformed_shapes`
  (including `incidental`, own-file `path`, route-index fields on a route sidecar). Its
  unknown-schema probe now uses `ar-census/v1`, because MIK-R07 made `ar-history/v1` a known schema.
- `test_locations_follow_the_layout_and_the_slug_is_display_only`.

### Conventions

- `_record(kind, **overrides)`, `_sidecar`, `_anchor` and `_realization` build minimal valid
  documents; `_refused(document, match)` asserts a `ValidationError`.
- Fixture blobs are the real blobs at base `b7ef73f8`; content hashes are illustrative.

### Invariants And Boundaries

- The golden IDs are the contract MIK-R24 must reproduce; do not regenerate them to make a change pass.
- §4.7 (history files) is MIK-R07's and is covered by `test_knowledge_history_files.py`, not here.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The cases exercise every public model of the package.

- The fixture list and the byte-for-byte round trip. [1]
- Doc14's verbatim spellings are refused. [2]
- Every kind round-trips and refuses a foreign prefix and foreign relations. [3]
- Second-owner fields are refused on an invariant. [4]
- Sidecar, reference and anchor refusals. [5]
- Lane registration. [6]

### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is exercised.
