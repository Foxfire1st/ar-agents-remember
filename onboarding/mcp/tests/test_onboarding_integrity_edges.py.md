# mcp/tests/test_onboarding_integrity_edges.py

| Field                  | Value                                        |
| ---------------------- | -------------------------------------------- |
| repository             | agents-remember                              |
| path                   | `mcp/tests/test_onboarding_integrity_edges.py` |
| doc_type               | `file-level-onboarding`                      |
| lastUpdated            | 2026-07-31T15:32+02:00                       |
| lastVerifiedCommitHash | `f3115ce8603f83b7b5cbd82aa402f66ec1d8a29d`   |
| lastVerifiedCommitDate | 2026-07-31T19:28:50+02:00|
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

| Finding | Source Path |
| --- | --- |
| The onboarding drift / missing-onboarding checkers under test. | [agents_remember/](agents-remember/mcp/src/agents_remember/) |
| The clean-path suites these edge verdicts complete. | [test_onboarding_drift.py](agents-remember/mcp/tests/test_onboarding_drift.py), [test_missing_onboarding.py](agents-remember/mcp/tests/test_missing_onboarding.py), [test_onboarding_doc.py](agents-remember/mcp/tests/test_onboarding_doc.py) |

## Update History

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  onboarding-integrity edge-verdict suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
