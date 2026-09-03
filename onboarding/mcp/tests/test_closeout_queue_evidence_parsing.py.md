# mcp/tests/test_closeout_queue_evidence_parsing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_closeout_queue_evidence_parsing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `99dc249bd507c20b09ece1169c2b1fa2af8e8c1b` |
| lastVerifiedCommitDate | 2026-09-02T05:53:10+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Proves strict structured curator evidence plus the surviving canonical planning-register Markdown
parsers.

## Code Commentary

### Logic

The cases force strict attestation and record candidate/judgment equality, deterministic generated
projection, shared validator delegation and failure translation, plus exact judgment/priority
section, table-header, separator, digest, and malformed-input behavior.

Since 260831-CCR (commit `99dc249b`) the shared `_record` fixture (line 71-89) binds canonical
task intent on the coherence record (`taskIntent=TaskIntentIdentity(digest="9" * 64)`, line 81)
and the rendered-markdown checks also assert the canonical `task-intent/v1` line when present, so
the structured-parsing suite exercises intent-bound records end to end.

### Conventions

Tests execute production owners and use shared builders only for canonical setup. Scenario-specific
differences remain in the test so fixtures do not become a parallel implementation.

### Invariants And Boundaries

- The suite preserves loud negative cases and exact identity/refusal assertions; it does not obtain
  green through a fallback, allowlist, or weakened production threshold.
- Dagger owns certifying execution. Any direct execution remains bounded diagnostic evidence only.
- Parsed coherence fixtures carry an exact canonical task-intent identity.

### Todos

None recorded.

## Docs References

The configured Domain Documentation registry is empty. No external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain source is required for this repository-owned test contract. | `_contract` | mcp/tests/test_closeout_queue_evidence_parsing.py:28-29 |

## Repo-Internal References

The test file is direct evidence for the production boundary named above.

| Finding | Anchor | Source |
| --- | --- | --- |
| The selected scenarios and assertions implement this test unit's forcing proof. | `_contract` | mcp/tests/test_closeout_queue_evidence_parsing.py:28-29 |
| The shared coherence record fixture binds canonical task intent. | `_record`; `taskIntent` | mcp/tests/test_closeout_queue_evidence_parsing.py:71-89; mcp/tests/test_closeout_queue_evidence_parsing.py:81-81 |

## Cross-Repo References

No cross-repository source is allowed by the resolved settings.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repository reference applies. | `_contract` | mcp/tests/test_closeout_queue_evidence_parsing.py:28-29 |

## MCAR-L03 Structured Pair Shape

Record and attestation fixtures now include one strict complete pair identity, proving the
structured acceptance schemas reject missing or malformed pair evidence.

## CCR-R02@v2 Intent-Bound Coherence Fixtures

Per `requirements/CCR-R02-v2-normative-task-intent-identity.md`, coherence records bind canonical
task intent; the shared fixture here supplies an exact `TaskIntentIdentity` so parsing and render
round-trips exercise current records. Part of the landed L25 candidate `99dc249b`.

## Update History

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for 99dc249bd507 (CCR-R02@v2/L25):
  the shared coherence record fixture now binds an exact `TaskIntentIdentity`; documented the
  intent-bound parsing contract. Verified at code commit 99dc249bd507c20b09ece1169c2b1fa2af8e8c1b.

- 2026-08-29T21:46+02:00 — MCAR-L03: extended structured coherence parsing fixtures with the
  mandatory exact pair. Dagger verification remains closeout-owned.

- 2026-08-29T08:52+02:00 — Replaced curator Markdown parsing tests with strict structured record,
  generated projection, and shared-validator proofs; planning-register parsers remain. Verification
  remains closeout-owned.

- 2026-08-25T15:44+02:00 — Created during PDLS whole-system reconciliation after source and
  requirement review. Verification remains closeout-owned.
