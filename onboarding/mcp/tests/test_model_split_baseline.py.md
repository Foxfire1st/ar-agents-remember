# mcp/tests/test_model_split_baseline.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/tests/test_model_split_baseline.py`                      |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated            | 2026-08-08T14:38+02:00                                       |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                   |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                |

## Governing Overview

[tests overview](overview.md)

## Purpose

`mcp/tests/test_model_split_baseline.py` is the 260731-EFA-L9 S4.2 proof: the model split is
zero-drift against the S1.3 baseline fixture (`mcp/tests/fixtures/model_split_baseline_260731_efa_l9.json`).

## Code Commentary

### Logic

`test_conversation_schemas_and_dataclass_fields_match_baseline` (cit:([`test_conversation_schemas_and_dataclass_fields_match_baseline`], mcp/tests/test_model_split_baseline.py:144-144)) compares
JSON schemas and dataclass field signatures for every moved conversation model;
`test_shared_harness_control_symbols_match_baseline` (cit:([`test_shared_harness_control_symbols_match_baseline`], mcp/tests/test_model_split_baseline.py:180-180)) does the same for
the shared harness-control symbols; `test_serialization_samples_match_baseline`
(cit:([`test_serialization_samples_match_baseline`], mcp/tests/test_model_split_baseline.py:211-211)) pins the wire-helper samples;
`test_model_rebuild_ordering_is_complete` (cit:([`test_model_rebuild_ordering_is_complete`], mcp/tests/test_model_split_baseline.py:226-226)) proves the acyclic
import/rebuild order; `test_removed_paths_receive_no_forwarding_shim`
(cit:([`test_removed_paths_receive_no_forwarding_shim`], mcp/tests/test_model_split_baseline.py:239-239)) and
`test_no_repo_file_imports_shared_harness_names_from_old_path`
(cit:([`test_no_repo_file_imports_shared_harness_names_from_old_path`], mcp/tests/test_model_split_baseline.py:266-266)) prove the old paths are gone with no
backwards imports.

### Invariants And Boundaries

- The fixture is generated pre-change and must not be silently regenerated as a fix: schema and
  signature equality is the R4/R10 zero-drift contract.

### Todos

No known follow-up.

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The baseline fixture is the S1.3 serialization/schema snapshot. | `_serialization_samples` | mcp/tests/fixtures/model_split_baseline_260731_efa_l9.json:2-2 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the S4.2 baseline suite.
  Verification metadata pinned until closeout stamps the L9 code commit.
