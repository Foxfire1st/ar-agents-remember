# mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[Nearest governing overview](../overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Owns the durable synchronous coordinator for one direct-landing generation: progress, exact output
projection, completion, input-required reporting, and unchanged-attempt reset.

## Code Commentary

### Logic

`DirectLandingRuntime` locates the canonical operation store. `progress` validates mutation
observations and reported recovery cells, then derives the code/memory recovery projection through
the shared closeout evidence owner. It preserves monotonic output proof and records when a real
commit boundary was crossed. `finish` publishes completion; `require_input` records a recoverable
interruption or a developer-decision surface.

`direct_landing_record` constructs an accepted generation from the typed request candidate and
initial mutation evidence. The existing code commit is recorded immediately. Admission is by the
request's own contract, commit/tree, and messages; the record has no closeout-door publication or
ledger byte intent.

`reconcile_direct_landing` reconciles launched Git commands, derives proven output cells, and asks
the pure classifier whether an omitted memory receipt can be recovered. Only the actual
`memoryContentCommit` is added from that proof. Updates use the current stored record and bounded
compare/update retries. `reset_reconciled_attempt` archives an exactly unchanged attempt before
resetting that leg within the same generation.

### Conventions

Typed mutation observations and recovery cells flow through their shared models. The canonical
root journal and its locator own durable state; mutable task prose and queue rows do not supply
fallback evidence.

### Invariants And Boundaries

- Accepted request identity and already proven output commits stay immutable.
- Missing memory receipts are recovered only from mechanically convergent Git evidence.
- No ledger mutation cell, ledger commit output, or DirectLandingLedgerIntent is published.
- Reconciliation and reset preserve the generation; action-required state must use the lifecycle recovery owner.

### Todos

No new file-local follow-up is established by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Anchor | Source |
| --- | --- | --- |
| None | `DirectLandingRuntime` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py:43-150 |
| None | `direct_landing_record`; `reconcile_direct_landing` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py:157-199; mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py:202-248 |
| Recovery cells are derived from authoritative mutation evidence. | "from authoritative mutation evidence" | mcp/src/agents_remember/worktrees/integration/closeout/recovery_projection.py:1-1 |
| The classifier supplies exact memory output evidence. | `_memory_output_matches_evidence` | mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_recovery_state.py:226-252 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51 UTC — Retired ledger-intent publication and ledger recovery cells from direct runtime coordination; retained canonical journal ownership, request-only admission, bounded reconciliation, and same-generation attempt history. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.


- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the door-free record
  shape this card records is the frozen one. Re-read the card against the source:
  `direct_landing_store` `:165-167` and `direct_landing_record` `:169-213` both hold. No wording
  changed. Verification metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification):
  `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py` changed
  since the recorded verification commit. Re-read the card against the frozen on-disk source and
  re-checked its claims and cited ranges: nothing this card asserts is falsified by the change, so
  no wording changed. Verification metadata remains closeout-owned; no verification stamp advanced.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source moved since
  the recorded verification commit — `closeout_door` left the contract and the integration path.
  Corrected four stale claims: the Logic paragraph, the invariant, the R03 reference row and the
  door-intent section no longer say a direct-landing record carries or declares a door publication
  or a dependency set, and the R03 section now records the removal. Verification metadata remains
  closeout-owned.
- 2026-09-09T02:42:21+02:00 — CCR-L24 inherited/current-source reconciliation 2026-09-09: Re-read the current card claims against the frozen candidate source and repaired exact citation coordinates (direct_landing_store→167-168). Preserved claim prose; source-sha256=ee66d86bd49ae1b5457a9318b77cfa0badd1e6cf9082e0ba25f667f1fcd73e41; verification metadata remains unchanged because commit-owned realization is pending.


- 2026-09-03T17:35+02:00 - 260831-CCR-L27 Gate-5 memory pass (src-a): widened the `direct_landing_record` ranges to 169-213 so the cited ranges hold the declaration line.

- 2026-09-03T12:30+02:00 — 260831-CCR memory curation pass for fbc89847233b1c5959f56475f2cb51f936d5ef0b (CCR-R03@v1/L03): recorded the admitted-door dependency declaration on direct-landing records; prior door-intent and recovery prose preserved.

- 2026-08-26T10:44:52+02:00 — No content impact: reviewed the closeout recovery-projection package relocation; door-bound direct landing and crash convergence are unchanged.

- 2026-08-24T14:43+02:00 — 260821-CLIVE cumulative curation: recorded door-bound direct landing and classifier-authorized crash convergence. Timestamp is the curator host's Europe/Berlin system time; verification remains closeout-owned.

- 2026-08-24T00:27+02:00 — 260821-CLIVE-L2 committed-route reconciliation: moved this preserved sidecar to mirror `mcp/src/agents_remember/worktrees/integration/direct_landing/direct_landing_operation.py`, repointed current source evidence and governing context, and verified the source at code commit `1d446724d099517f6f52d596b47827ae2391a2a4`.

- 2026-08-23T16:08+02:00 — 260821-CLIVE-L2: created from the accepted full L2 candidate. Verification fields remain blank until the architect-owned closeout has a real code commit to stamp.
