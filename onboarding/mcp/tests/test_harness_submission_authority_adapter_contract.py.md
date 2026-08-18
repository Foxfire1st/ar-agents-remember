# mcp/tests/test_harness_submission_authority_adapter_contract.py

| Field                  | Value                                                             |
| ---------------------- | ----------------------------------------------------------------- |
| repository             | agents-remember                                                   |
| path                   | `mcp/tests/test_harness_submission_authority_adapter_contract.py` |
| doc_type               | `file-level-onboarding`                                           |
| lastUpdated            | 2026-07-31T15:32+02:00                                            |
| lastVerifiedCommitHash | `25841d0ddc2d93c4950abf097168fa24b220c5ad`                        |
| lastVerifiedCommitDate | 2026-08-18T11:30:22+02:00|
| governingOverview      | `overview.md`                                                     |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The authority's **re-verification of whatever an adapter hands back**.

An adapter is a vendor boundary, not a trusted collaborator: it can answer with the wrong
type, acknowledge somebody else's request, or claim an acceptance the contract forbids after
dispatch.

## The Single Outcome

None of those may be projected as a settled outcome — and **none may be projected as a
rejection either**. The adapter method has already returned, so the authority cannot certify
that nothing crossed the wire. Every case therefore ends in the same place: an `unknown`
**blocker** that

- pins the head,
- keeps the successor undispatched, and
- waits for an operator to resolve it.

## Why `VerbatimAdapter` Exists

The shared `_AuthorityAdapter` double stamps the request id back onto every receipt it
returns. That is the right shape for testing the timeline, but it is precisely what hides
the contract under test here. `VerbatimAdapter` answers with **exactly what the test
queued**, with none of the usual repairs, so the authority's own verification is the only
thing standing between a malformed adapter answer and a settled submission.

Helpers: `state_of` reads the resulting state; `dispatched_ids` reports the request ids the
adapter was actually asked to send, once the dispatcher settles — which is how "the
successor stayed undispatched" is asserted rather than assumed.

## Invariants And Boundaries

- A malformed or mis-addressed adapter answer produces `unknown`, never `delivered` and
  never `rejected`.
- The blocker is head-pinning: no successor may be dispatched past an unresolved one.
- Resolution is an operator action; the authority never resolves a blocker itself.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The submission authority under test. | `HarnessSubmissionAuthority` | mcp/src/agents_remember/serving/harness_submission_authority.py:116-1023 |
| The timeline-shaped suite that uses the repairing double. | `HarnessSubmissionAuthorityTests` | mcp/tests/test_harness_submission_authority.py:230-755 |
| Log-side acceptance evidence the authority reads. | `test_claude_non_submission_records_never_prove_delivery` | mcp/tests/test_harness_logs_user_message_readers.py:46-82 |

## Update History

- 2026-08-18T09:05+02:00 — Renamed the atomic 'barrier' concept to 'blocker' throughout (terminology unification; no behavioral change). Verification remains closeout-owned.

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-03T03:03:00+02:00 — 260731-EFA-L6-W3-B01 curator: curated 3 Repo-Internal table citations with exact authority, timeline-suite, and log-reader test anchors. Verification metadata remains unchanged for closeout.

- 2026-07-31T15:32+02:00 — 260731-EFA-L2 curator: created onboarding for the new
  adapter-contract re-verification suite. Verification metadata is pinned to the leaf's
  reformat commit until closeout stamps the code commit.
