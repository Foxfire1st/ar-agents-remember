# skills/l-01-agent-lifecycles/roles

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | skills/l-01-agent-lifecycles/roles |
| doc_type | route-local-overview |
| lastUpdated | 2026-07-12T14:20:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|

## Purpose

Role-specific dispatch guidance shares the exact session-id handoff, ready proof, delivered-plus-harness-log-confirmed completion, launch-phase sessionCommands, and post-ready promptKeywords timing.

## Hot Path Summary

Role-specific dispatch guidance shares the exact session-id handoff, ready proof, delivered-plus-harness-log-confirmed completion, launch-phase sessionCommands, and post-ready promptKeywords timing.

### 260713-PHA-L5 Route Contract Review

Hosted role dispatch now relies on exact adapter readiness and correlated delivery evidence. The
durable inbox remains the message root, explicit recipient consume remains acknowledgement, and
pane/log classifiers are diagnostics-only. The packaged role briefs and source lifecycle guidance
must stay aligned with this contract.

### 260731-EFA-L6 Curator Self-Check Impact

`curator.md` now requires the curator to green its own change-set before reporting:
`route_index_refresh`, `memory_quality_check`, and `drift_check` are called with the leaf's
enclosure `contract_path`, and each response's `onboardingRoot` must be the memory worktree.
`templates/curator-brief.md` feeds the same contract-path doctrine to the dispatched curator.
The other role briefs are unchanged.

## Update History

- 2026-08-05T03:47+02:00 — 260731-EFA-L6 route impact: recorded the curator self-check contract
  (`contract_path`-scoped memory tools and `onboardingRoot` confirmation) landed in
  `roles/curator.md` and `templates/curator-brief.md`; other role documents are unchanged.
  Verification metadata pinned until closeout stamps the code commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: reviewed route impact for the accepted hosted cutover.
- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator: established governing route coverage for the final candidate.
