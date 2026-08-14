# mcp/tests/fixtures/model_split_baseline_260731_efa_l9.json

| Field                  | Value                                                                 |
| ---------------------- | --------------------------------------------------------------------- |
| repository             | agents-remember                                                       |
| path                   | `mcp/tests/fixtures/model_split_baseline_260731_efa_l9.json`           |
| doc_type               | `file-level-onboarding`                                               |
| lastUpdated            | 2026-08-08T14:38+02:00                                                |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432`                            |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview      | `overview.md`                                                         |

## Governing Overview

[tests overview](../overview.md)

## Purpose

`mcp/tests/fixtures/model_split_baseline_260731_efa_l9.json` is the pre-change S1.3 baseline for
the 260731-EFA-L9 model split: JSON schema for every public pydantic model in the conversation
modules, dataclass field signatures for every moved `harness_control_models` dataclass, and
serialization samples for the moved wire helpers and representative conversation models.

## Code Commentary

### Logic

The fixture is generated pre-change (2026-08-08) and compared by `test_model_split_baseline.py`;
the `_serialization_samples` section pins wire-helper outputs, and the schema/signature sections
pin declaration equality (R4/R10). Rebuilding the fixture is a deliberate baseline change, never
an automatic fix.

### Invariants And Boundaries

- The fixture must stay byte-stable across the leaf; regenerate only when the wire contract
  intentionally changes (requires review).

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
| The baseline suite consumes the fixture. | `test_conversation_schemas_and_dataclass_fields_match_baseline` | mcp/tests/test_model_split_baseline.py:144-144 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the S1.3 baseline fixture.
  Verification metadata pinned until closeout stamps the L9 code commit.
