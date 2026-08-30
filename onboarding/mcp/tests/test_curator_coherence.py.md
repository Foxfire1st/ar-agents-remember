# mcp/tests/test_curator_coherence.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_curator_coherence.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-30T05:55+02:00 |
| lastVerifiedCommitHash |  `346507af24396ab7b491e02511c4af006ccd3dc5`|
| lastVerifiedCommitDate |  2026-08-30T07:51:57+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Provides the focused structural and integration proof for exact curator-coherence publication and
the shared memory/closeout validator boundary.

## Code Commentary

### Logic

The suite checks identity separation; exact missing/extra/duplicate judgment rejection; evidence
path and digest binding; candidate staleness; atomic immutable generation behavior; deterministic
memory-quality bytes; one live authority despite obsolete Markdown files; exact replay after a
pre-pointer crash; malformed-authority CAS recovery; combined memory readiness; and closeout's use
of the same validator.

### Conventions

Pure schema/set tests use narrow values. Publication tests use the established real Git/task/memory
`QueueFixture` so they exercise configured admission, task topology, candidate trees, stable
authority paths, and response conformance together.

### Invariants And Boundaries

- Historical Markdown never affects validation.
- Same-input retries create no second generation.
- A malformed stable pointer is recoverable only with its exact observed digest.
- Memory readiness cannot be combined-ready while closeout would reject coherence.
- Dagger is the certifying execution environment.

### Todos

None recorded.

## Docs References

No configured external documentation applies; this is repository-owned regression evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for the regression matrix. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The exact judgment and evidence matrix rejects all non-exact input classes. | `test_exact_judgment_set_rejects_missing_extra_duplicate_and_bad_evidence` | mcp/tests/test_curator_coherence.py:106-142 |
| Public publication ignores competing historical Markdown and converges across crash replay. | `test_public_tool_publishes_one_live_authority_and_ignores_historical_markdown` | mcp/tests/test_curator_coherence.py:226-293 |
| Malformed canonical bytes remain replaceable through exact CAS. | `test_prepare_and_publish_can_replace_a_malformed_authority_by_exact_cas` | mcp/tests/test_curator_coherence.py:296-338 |
| Memory readiness and closeout invoke the same canonical validator. | `test_memory_quality_never_reports_combined_closeout_readiness_without_coherence`; `test_closeout_memory_preflight_calls_the_same_validator` | mcp/tests/test_curator_coherence.py:370-401; mcp/tests/test_curator_coherence.py:404-432 |

## Cross-Repo References

No meaningful cross-repository reference applies.

| Finding | Anchor | Source |
| --- | --- | --- |
| The suite creates only temporary local repositories and task roots. | — | — |

## MCAR-L03 Acceptance Pair Evidence

Core coherence tests now prove prepare, publish, validate, immutable record, and generated Markdown
all expose the same pair, and the source memory-quality attestation is pair-bound.

## Update History

- 2026-08-30T05:55+02:00 — MCAR-L03 A005: patched the shared closeout pair-evidence API
  rather than a removed module-local validator alias, preserving the one-validator assertion.

- 2026-08-29T21:46+02:00 — MCAR-L03: added end-to-end pair identity assertions across coherence
  publication and validation. Dagger verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Created for MCAR-L02 A005's structured authority, CAS, idempotency,
  evidence, deterministic-attestation, and shared-consumer proof. Verification remains closeout-owned.
