# mcp/tests/test_knowledge_file_formats.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_knowledge_file_formats.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `overview.md` |

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
  (including `incidental`, own-file `path`, route-index fields on a route sidecar).
- `test_locations_follow_the_layout_and_the_slug_is_display_only`.

### Conventions

- `_record(kind, **overrides)`, `_sidecar`, `_anchor` and `_realization` build minimal valid
  documents; `_refused(document, match)` asserts a `ValidationError`.
- Fixture blobs are the real blobs at base `b7ef73f8`; content hashes are illustrative.

### Invariants And Boundaries

- The golden IDs are the contract MIK-R24 must reproduce; do not regenerate them to make a change pass.
- §4.7 (history files) is MIK-R07's and is not encoded.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The cases exercise every public model of the package.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture list and the byte-for-byte round trip. | `test_doc14_worked_examples_validate_and_round_trip_byte_for_byte` | mcp/tests/test_knowledge_file_formats.py:131-139 |
| Doc14's verbatim spellings are refused. | `test_doc14_verbatim_illustrative_shapes_are_refused` | mcp/tests/test_knowledge_file_formats.py:142-150 |
| Every kind round-trips and refuses a foreign prefix and foreign relations. | `test_every_record_kind_parses_round_trips_and_refuses_a_foreign_prefix` | mcp/tests/test_knowledge_file_formats.py:272-295 |
| Second-owner fields are refused on an invariant. | `test_records_refuse_second_owners_and_malformed_record_fields` | mcp/tests/test_knowledge_file_formats.py:323-353 |
| Sidecar, reference and anchor refusals. | `test_sidecars_references_and_anchors_refuse_malformed_shapes` | mcp/tests/test_knowledge_file_formats.py:406-446 |
| Lane registration. | "mcp/tests/test_knowledge_file_formats.py" | mcp/tests/test-evidence-lanes.toml:97-97 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is exercised. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
