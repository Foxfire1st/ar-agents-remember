# mcp/tests/test_checkout_coordination_isolation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkout_coordination_isolation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T21:38+00:00 |
| lastVerifiedCommitHash | `d36109038b3f2b500c138f9dc1ea9c9f9a247489`|
| lastVerifiedCommitDate | 2026-09-06T22:21:49+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Checkout-local coordination isolation at configuration and store boundaries.

## Code Commentary

### Logic

Loaded source identifies the linked checkout regardless of cwd. Its effective configuration uses the dummy coordination root, disables live providers and services, and writes an incident-shaped inbox only there. Escape writes refuse before parent or lock creation; the admitted report path remains writable.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The rewrite guard also rejects manually constructed live targets. Primary undeclared access fails closed, while explicit temporary test mode retains legitimate temporary writes.

### Todos

No file-local implementation change is requested by this reconciliation.

## Docs References

No Domain Documentation entries are configured in this memory root. These are repository-owned fixture and assertion contracts; no external library behavior is inferred.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain evidence applies to the file-local claims above. | N/A | N/A |

## Repo-Internal References

The retained source anchors below support the fixture roles and assertion boundaries described above. They identify current behavior, not a request to restore historical test counts or percentage targets.

| Finding | Anchor | Source |
| --- | --- | --- |
| Linked checkout is derived from loaded source not cwd. | `test_linked_checkout_is_derived_from_loaded_source_not_cwd` | mcp/tests/test_checkout_coordination_isolation.py:73-85 |
| Checkout config ignores live authority and uses only dummy root. | `test_checkout_config_ignores_live_authority_and_uses_only_dummy_root` | mcp/tests/test_checkout_coordination_isolation.py:87-106 |
| Incident shaped inbox write lands only in leaf dummy root. | `test_incident_shaped_inbox_write_lands_only_in_leaf_dummy_root` | mcp/tests/test_checkout_coordination_isolation.py:110-126 |
| Store guard refuses escape before creating lock or parent. | `test_store_guard_refuses_escape_before_creating_lock_or_parent` | mcp/tests/test_checkout_coordination_isolation.py:130-140 |
| Enclosure report write is allowed without opening coordination escape. | `test_enclosure_report_write_is_allowed_without_opening_coordination_escape` | mcp/tests/test_checkout_coordination_isolation.py:142-151 |
| Rewrite guard refuses a manually constructed live target. | `test_rewrite_guard_refuses_a_manually_constructed_live_target` | mcp/tests/test_checkout_coordination_isolation.py:153-161 |
| Primary checkout undeclared config access fails closed. | `test_primary_checkout_undeclared_config_access_fails_closed` | mcp/tests/test_checkout_coordination_isolation.py:163-170 |
| Explicit test mode preserves temporary store writes. | `test_explicit_test_mode_preserves_temporary_store_writes` | mcp/tests/test_checkout_coordination_isolation.py:172-180 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-06T21:38+00:00 — Reconciled the actual retained source after IAS test simplification at d3610903: corrected fixture/test roles, removed obsolete current-coverage claims and refreshed existing-source citations. Earlier entries remain historical; verification stamps remain closeout-owned.


- 2026-08-24T21:23+02:00 — No content impact: the owned-state context manager moved from the test
  tree to `agents_remember_test_support.testing.global_state`; checkout-isolation behavior is unchanged.

- 2026-08-15T09:10+02:00 — L3 content update: extended isolation coverage to the detached durable
  writer role; verification remains closeout-owned.

- 2026-08-13T00:00+02:00 — 260731-EFA-L23 post-closeout worker-authority repair: added the positive lifecycle-operation boundary, proving live coordination config is admitted only with the explicit worker mode while `declared_daemon_role()` remains empty. The owner reports 46 focused tests across both affected suites, Ruff clean, and diff-check clean. Verification remains closeout-owned.
- 2026-08-12T22:24+02:00 — 260731-EFA-L23 async-closeout follow-up: added the exact enclosure report-write case and its negative sibling-coordination assertion. The owner reports 14/14 checkout-isolation tests green under xdist auto. Verification remains closeout-owned.
- 2026-08-12T09:18+02:00 — 260731-EFA-L20 reopen: the lock-path refusal now asserts the context manager's raising `__enter__` directly, removing an intentionally unreachable body line while preserving the same pre-lock and pre-parent safety contract.
- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 removed an unreachable context body and the script-only main guard; every checkout-isolation assertion and refusal boundary documented above remains unchanged.
- 2026-08-10T18:31+02:00 — 260731-EFA-L21 quality completion: added explicit incomplete-checkout, installed-package, and trusted malformed-config cases for every changed defensive branch.
- 2026-08-10T18:31+02:00 — 260731-EFA-L21: created with linked/primary resolution, synthetic-config, incident-shaped write, escape-refusal, MCP, and pytest regression cases. Verification metadata remains blank until approved closeout commits the code.
