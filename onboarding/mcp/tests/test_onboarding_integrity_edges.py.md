# mcp/tests/test_onboarding_integrity_edges.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/tests/test_onboarding_integrity_edges.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-31T15:32+02:00                       |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`   |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `overview.md`                                |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Onboarding-integrity verdicts for the states **a healthy repository does not reach**.

Two checkers own the "is this file's onboarding trustworthy?" question, and both have
verdicts that only appear when something is wrong:

- a sidecar whose verification stamp is absent, whose source has been deleted, or whose
  recorded commit is no longer in history;
- a newly added file whose onboarding lives **inline in the source** rather than beside it,
  or under a storage mode neither checker can verify.

The clean paths are already covered. These are the verdicts that matter, because each is a
distinct **instruction to the developer reading the report** — so each is pinned to the
classification, trust level and note it produces, rather than to "something was returned".

## Classes

| Class | Checker |
| --- | --- |
| `ExternalSidecarClassificationTests` | `classify_external_onboarding` verdicts before and around the source diff. |
| `MissingOnboardingStorageModeTests` | Which onboarding a newly added file is expected to carry, per storage mode. |

## Method

Real git repositories, built per test: `initialize_repo`, `run_git`, `head_hash`.
`write_sidecar` writes a file-level onboarding sidecar **in the table format the drift
checker parses**, so a change to that format is caught here rather than being papered over
by a hand-built dict.

## Invariants And Boundaries

- Each verdict must carry its own classification, trust level **and** note; two verdicts
  that collapse to the same report text are indistinguishable to the developer acting on
  them.
- A commit no longer in history is a distinct verdict from a missing stamp and from a
  deleted source.
- The sidecar format the fixtures write must stay the format the parser reads.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The onboarding drift / missing-onboarding checkers under test. | `classify_external_onboarding`; `check_missing_onboarding` | mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:46-73; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/sidecar.py:33-112 |
| The clean-path suites these edge verdicts complete. | `InlineOnboardingTests`; `MissingOnboardingTests`; `MeaningfulBodyTests` | mcp/tests/test_missing_onboarding.py:22-154; mcp/tests/test_onboarding_doc.py:41-71; mcp/tests/test_onboarding_drift.py:62-121 |

## Update History

- 2026-08-02T22:15+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 2 citation rows; scoped citation check now passes.
- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  onboarding-integrity edge-verdict suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
