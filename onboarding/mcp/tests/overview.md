# mcp/tests

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | mcp/tests |
| doc_type | route-local-overview |
| lastUpdated | 2026-07-12T14:20:00+02:00 |
| lastVerifiedCommitHash | `300664e63f2dbb5f0701d37bbc17ff5358960c77`|
| lastVerifiedCommitDate | 2026-07-12T18:11:57+02:00|

## Purpose

L4 regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

The L7 test route additionally proves the projection/landing boundary: slow or failed remote observations do not delay local publication; observer results remain exact-contract and freshness-labeled; stale landing rendering is visible but motion-inert; invalid snapshot reads preserve local status; and a failed refresher does not skip serving shutdown. These are focused leaf regressions; the manager owns the full repository gate.

## Hot Path Summary

260712-TRH-L5 tests prove the narrow confirmed-gone eligibility boundary, terminal and tmux
positive-gone evidence, fail-closed indeterminate behavior, one-fold/one-snapshot boundedness,
same-lock resolve-plus-compact ordering, stale-snapshot non-resurrection, unchanged TTL fallback,
persisted folded-id removal counts, body-free aggregate events, and silence on no-op sweeps.

L4 regression coverage proves exact-session readiness and dispatch, catalog writer composition, copy-mode safety, calibrated submit settling, recovery idempotence, expectation timing, and public tool/doctrine conformance.

## Update History
- 2026-07-12T17:40+02:00 — 260712-TRH-L5 curator: added governing route coverage for the new
  inbox-reclamation regression suite and its final PASS delta tests, including event silence and
  corrected persisted removal semantics. Verification metadata remains pinned until closeout.
- 2026-07-12T17:30+02:00 — 260712-TRH-L7: added route coverage for bounded landing observation, no-wait projection, stale rendering, invalid-snapshot containment, and shutdown after observer failure.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
