# dashboard/src/test/fixtures/submitScenarios.ts

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `dashboard/src/test/fixtures/submitScenarios.ts` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-17T21:39+02:00 |
| lastVerifiedCommitHash | `f8196d98982f834d68152d307ff8025ea69440d5` |
| lastVerifiedCommitDate | 2026-07-17T22:08:10+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[dashboard/src overview](../../overview.md)

## Purpose

Provides named, deterministic FEUI-L5 submission scenarios shared by transport, lifecycle, store,
and composer tests.

## Code Commentary

### Logic

Fixtures encode receipt/status/withdrawal shapes and request provenance for accepted, queued,
ambiguous, rejected, authority-loss, dispatch-race, and draft-recovery paths. Centralizing these
records keeps tests aligned to the exact public lifecycle alphabet and epoch/request correlation
instead of inventing subtly incompatible payloads per suite.

### Invariants And Boundaries

- Fixtures contain normalized public evidence only; vendor raw evidence is intentionally absent.
- Request ids, epochs, observation versions, text provenance, and draft revisions are explicit where
  the scenario depends on them.
- Fixtures are test data, not a second implementation of the evidence fold.

## Docs References

No Domain Documentation source is configured for this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live domain-documentation source was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lifecycle algebra defines the vocabulary represented here. | `SubmitPhase` | dashboard/src/data/submitMachine.ts:22-36 |
| The frontend authority client consumes the public status and withdrawal shapes. | `SubmissionStatusWire`, `WithdrawalResultWire` | dashboard/src/data/submissionLifecycleClient.ts:22-29; dashboard/src/data/submissionLifecycleClient.ts:40-46 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixtures are internal to this repository's dashboard tests. | — | — |

## Update History

- 2026-08-03T04:32:19+02:00 — W3-B08 curator: curated 4 citations (citation_anchor_missing=2, citation_prose_not_in_cit_form=0, citation_source_malformed=2); final scoped citation check clean.
- 2026-07-17T21:39+02:00 — Created for 260715-FEUI-L5; documented the shared normalized scenario
  vocabulary and its explicit correlation/privacy boundaries. Verification metadata remains pinned
  to the leaf base until closeout.
