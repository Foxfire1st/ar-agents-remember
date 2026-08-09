# mcp/src/agents_remember/serving/dispatch_brief.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | mcp/src/agents_remember/serving/dispatch_brief.py |
| doc_type | file-level-onboarding |
| lastUpdated | 2026-08-09T01:21+02:00 |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484`|
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview | mcp/src/agents_remember/serving/overview.md |

## Governing Overview

Governing overview: mcp/src/agents_remember/serving/overview.md

## Purpose

Policy and performer-layer collaborators for one readiness-gated durable dispatch brief. This
file absorbed the tool-layer orchestration that lived in the deleted `mcp/tools/dispatch_brief.py`
and now owns the delivery seams, the expectation clocks, and the exact-session readiness gate for
dispatch-brief delivery.

## Code Commentary

### Logic

`DispatchBriefGate` remains the exact-session protocol readiness gate: it accepts only a catalog
entry whose identity matches and whose adapter snapshot is ready, with no recovery/compatibility
path. `HostedDelivery` (with `HOSTED_DELIVERY` / `NO_HOSTED_DELIVERY` singletons) carries the
delivery collaborators — catalog, host, paster, readiness probe, and gate — so a durable row can
be pushed into its recipient's live hosted session or, with `enabled=false`, merely persisted.
`require_dispatch_target` refuses before persistence unless the exact agent session is ready.
`expectation_store` / `expectation_sla_seconds` resolve the observer-root expectation store and
its per-kind SLA from agentic settings (falling back to `DEFAULT_EXPECTATION_SLA_SECONDS`);
`start_dispatch_expectations` starts the `briefed-by` clock from the one durable row's timestamp
and id, skipping rows already present. The `turn-report-by` clock is retired (260713-TES-L2):
completion truth comes from the catalog turn projection, never from artifact/clock inference.

## 260713-TES-L2 Current Delta — Turn-Report-By Retired

`start_dispatch_expectations` cit:([`start_dispatch_expectations`], mcp/src/agents_remember/serving/dispatch_brief.py:133-167) now writes exactly one expectation kind (`briefed-by`)
instead of two; no `turn-report-by` row is minted at dispatch. `KNOWN_EXPECTATION_KINDS` and
`DEFAULT_EXPECTATION_SLA_SECONDS` in `kernel/_agentic_settings_core.py` dropped
`turn-report-by`; the record Literal in `controlplane/expectation_rows.py` keeps the value for
legacy-row parse compatibility until the L4 schema migration.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.
`fulfill_dispatch_expectation` / `fulfill_briefed_expectation` mark the briefed clock met only
from delivered evidence. `with_prompt_keywords` prepends settings-owned prompt keywords as one
line, and `delivery_is_briefed` / `dispatch_stays_on_exact_session` keep the pending row on its
exact agent id.

### Invariants And Boundaries

Canonical lifecycle doctrine owns canonical skill content; generated copies are synchronization
outputs. Dispatch proof remains exact-session and fail-closed: no durable row is created without
prior exact-session readiness, no adapter is contacted for a caller that never committed, and a
pending dispatch row never enters a ladder that can readdress its exact agent id.

## Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

## Repo-Internal References

Worker source inventory, reviewer verdict, and governing route overview.

## Cross-Repo References

No meaningful cross-repo references.

### 260713-PHA-L5 Exact Protocol Readiness

Dispatch readiness checks the exact catalog session's adapter snapshot and requires ready control
plus an accepting state. Copy mode, pane text, placeholders, and recovery paste are not authority.

### 260731-EFA-L6 Tool-Layer Move Into Serving

This leaf deleted `mcp/tools/dispatch_brief.py` and moved its orchestration into this file:
`HostedDelivery`, `HOSTED_DELIVERY`, `NO_HOSTED_DELIVERY`, `expectation_store`,
`expectation_sla_seconds`, `require_dispatch_target`, `start_dispatch_expectations`, and
`fulfill_dispatch_expectation` now live beside `DispatchBriefGate`. The caller
(`mcp/tools/operator_inbox.py::operator_inbox_post_payload`) still follows the same
readiness-gated, exact-session contract; the durable row remains the root, and expectation
clocks still start from that one row's timestamp and id.

## Update History
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: recorded the turn-report-by retirement —
  dispatch writes briefed-by only; no new turn-report-by rows. Verification metadata pinned
  until closeout stamps the 260713-TES-L2 commit.
- 2026-08-05T03:47+02:00 — 260731-EFA-L6 curator: rewrote this card for the current source after
  `mcp/tools/dispatch_brief.py` moved into serving — the delivery seams and expectation-clock
  helpers are now owned here, exact-session readiness still refuses before persistence, and the
  test suite pins the same contract. Verification metadata pinned until closeout stamps the code
  commit.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: replaced pane/log readiness with exact adapter handshake evidence.

- 2026-07-12T14:20:00+02:00 — 260712-TRH-L4 curator refresh: final candidate onboarding; exact-session dispatch and serialized-writer/lock-free-reader concurrency recorded.
