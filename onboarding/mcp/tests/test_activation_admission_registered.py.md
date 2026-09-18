# mcp/tests/test_activation_admission_registered.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_activation_admission_registered.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-08T19:24:00+02:00 |
| lastVerifiedCommitHash | `b281bcd68261866be306cc80a48241921b6dd0d2` |
| lastVerifiedCommitDate | 2026-09-16T14:24:58+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Registered FastMCP proof for actionable atomic-series activation admission and read-only status
evidence. The admission payload is contract-scoped: it explains the addressed contract's own state and
never names a foreign master as the blocker.

## Code Commentary

### Logic

`RegisteredActivationAdmissionTests` builds temporary code/coordination roots and calls the real
registered `worktree_status`, `worktree_sync`, and `worktree_start` tools. It reuses
`ActivationFixture`'s two sprint-commanded masters, so the fixture's two contracts share one protected
source pair — the shape that used to make the second selection name the first master as
`atomic-series-paused-by:`.

The cases prove that status exposes an active contract's own activation fact without mutating record
bytes, that the sync refusal addresses **only the addressed contract's own state**, that vacant and
unreadable activation snapshots remain distinct corrective evidence, that oversized unreadable
diagnostics retain a bounded parser-error prefix, and that persisted master edge mismatches retain
expected/observed branch facts across both the initial and authoritative reread paths. The
unreadable-contract case also proves that a malformed parser's 9099-character reason remains bounded in
top-level and nested refusal detail while its source bytes remain unchanged. The fixture is disposable;
it does not prove a live control-plane run or acceptance.

The refusal case is the contract-scoping forcing test. With contract A vacant and contract B live, the
`worktree_sync` refusal for A asserts that the admission carries no `classification`, `blocking`,
`sourcePair` or `sourcePairFingerprint` key, that `admission["contractFingerprint"]` equals A's own
fingerprint and differs from B's, that the status action binds A's contract path, that the retry
precondition is A's own "not sufficient to continue", that B's task path never appears in the response
text, and that A's record bytes are unchanged. A foreign live master is therefore never a retry
precondition or a scheduling block. The redirected-reread and unreadable-contract helpers assert the
same absence directly on the admission dict.

### Conventions

This file is integration evidence because it crosses the registered MCP transport. Its assertions
describe response shape and byte-preservation boundaries; collected counts and focused passes remain
worker evidence rather than Gate 5 certification. Cases assert on the public JSON payload rather than
importing projection helpers, so a payload key that regains a foreign-master concept is caught here.

### Invariants And Boundaries

- Selector/status projections remain read-only in the status and refusal paths.
- An admission refusal describes the addressed contract only: it carries no `classification`,
  `blocking` or `sourcePair*` key and never names another master as blocker or precondition.
- A logical `active` or `reconciling` selection is not treated as proof of a live process.
- Temporary fixture state cannot establish production scheduler, Dagger, or master-aggregate behavior.

## Docs References

No Domain Documentation entries are configured for this repository-owned integration fixture
(`system/sources.md` declares no entries).

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain evidence applies. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Registered status projects activation without mutation. | `test_registered_status_projects_activation_without_mutation` | mcp/tests/test_activation_admission_registered.py:155-176 |
| The sync refusal addresses only the addressed contract's own state: no `classification`/`blocking`/`sourcePair*` key, this contract's fingerprint and status action, and a foreign live master named nowhere. | `test_registered_sync_refusal_addresses_only_this_contracts_own_state` | mcp/tests/test_activation_admission_registered.py:178-221 |
| Vacant and unreadable snapshots remain distinct and unchanged. | `test_registered_sync_refusal_distinguishes_vacant_and_unreadable` | mcp/tests/test_activation_admission_registered.py:223-266 |
| Oversized unreadable detail is bounded in both status and sync projections without changing source bytes. | `test_registered_status_and_sync_bound_oversized_unreadable_detail` | mcp/tests/test_activation_admission_registered.py:268-320 |
| Startup edge mismatch retains expected and observed branch evidence. | `test_registered_start_refusal_reports_contract_edges` | mcp/tests/test_activation_admission_registered.py:322-369 |
| Authoritative startup reread preserves edge evidence when the contract drifts after upstream refresh. | `test_registered_start_reread_refusal_preserves_edges_and_guidance` | mcp/tests/test_activation_admission_registered.py:371-423 |
| Unreadable startup contracts retain the concrete parser reason in refusal and observed evidence, including bounded oversized parser detail and unchanged source bytes. | `test_registered_start_unreadable_contract_keeps_parser_reason` | mcp/tests/test_activation_admission_registered.py:425-497 |
| The shared admission explainer no longer emits `classification`/`blocking`, and keys the refusal to the observed contract fingerprint. | "def atomic_series_admission_projection(" | mcp/src/agents_remember/worktrees/activation/atomic_series_admission.py:33-75 |

## Cross-Repo References

No cross-repository implementation evidence is required for this disposable registered fixture.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture does not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-13T14:20:09+02:00 — Rebound the registered proof to the contract-scoped admission: renamed the refusal case to `test_registered_sync_refusal_addresses_only_this_contracts_own_state`, recorded that the admission payload no longer carries `classification`/`blocking`/`sourcePair`/`sourcePairFingerprint` and keys `contractFingerprint` to the addressed contract, re-pointed all seven case ranges to their current lines, and added the projection row. No acceptance claim; verification stamps remain closeout-owned.
- 2026-09-08T19:24:00+02:00 — CCR-L38 CQ04 preparation reconciled the registered oversized-parser proof and helper extraction into the seven current source cases, rebinding all test anchors to the current file. The public-boundary result is preparation evidence only; verification remains closeout-owned with no acceptance claim.
- 2026-09-08T18:54:49+02:00 — CCR-L38 CQ01/CQ04 preparation rebound the registered fixture to its seven current source cases: bounded oversized activation detail, authoritative reread edge refusal, and concrete unreadable-contract parser evidence. Focused worker checks are retained as preparation evidence only; verification remains closeout-owned and no acceptance claim is made.
- 2026-09-08T16:05:21+02:00 — CCR-L38 source-grounded candidate pass: created the one-to-one sidecar for the frozen registered activation/admission proof. Verification metadata remains closeout-owned; no Gate 5 or acceptance claim.
