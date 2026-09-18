# mcp/tests/test_checkout_coordination_isolation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkout_coordination_isolation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:56+02:00 |
| lastVerifiedCommitHash | `0dd04d6adbca3e8ba61849b605ece3137005829e`|
| lastVerifiedCommitDate | 2026-09-18T15:05:30+02:00|
| reviewedWorkingCandidate | `ar/260918-tsip-l3-ar` uncommitted source (`mcp/tests/test_checkout_coordination_isolation.py` **180 → 241 lines**, 8 → **10** cases); base `a12c511f6e76bd1188719cad0a9104d78d46920c` |
| governingOverview | `overview.md` |

## Governing Overview

[Test suite overview](overview.md)

## Purpose

Checkout-local coordination isolation at configuration and store boundaries.

## Code Commentary

### Logic

Loaded source identifies the linked checkout regardless of cwd. Its effective configuration uses the dummy coordination root, disables live providers and services, and writes an incident-shaped inbox only there. Escape writes refuse before parent or lock creation; the admitted report path remains writable.

Since `260918-TSIP-L3` the suite also holds **two pins on the execution-mode boundary, and they assert today's behaviour on purpose** (`T30`/`T28`): `declare_execution_mode` is one assignment with no caller identity, PID or parent check, environment proof, signature or operation record, so the boundary checks only *was any mode declared* — `checkout_cli_location` and `require_durable_write_target` both test `is not None`. The first pin is a two-arm case: **arm A** is the plane's real refusal of an undeclared primary checkout and of a write outside any checkout, and **arm B** is that one `declare_execution_mode("mcp")` lifts both and makes `load_config` read the **live** authority settings (`direct_execution_enabled` true) rather than the synthetic non-authority config. Arm A is the positive control — without it a case that passes after the declaration could be passing because the refusal never fired. The second pin drives `declare_lifecycle_operation_process()`, whose docstring reserves the mode to a plane-owned operation record while the function itself is a bare declaration with **zero callers** in `mcp/src` or `mcp/tests`, and shows `durable_store.declared_process_role()` reporting it as a declared writer of every store `mcp` owns. Both are **pins, not endorsements**: authentication is deliberately not implemented (registered as `D-L3-1` in `notes/defect-index.md`), so a future leaf that authenticates the declaration will red these cases and should read the register before repairing them.

### Conventions

This card describes the retained source at IAS `d3610903`. Historical entries below record earlier test populations; they do not require restoring removed cases. Source inspection is memory preparation and does not claim a test run or acceptance.

### Invariants And Boundaries

The rewrite guard also rejects manually constructed live targets. Primary undeclared access fails closed, while explicit temporary test mode retains legitimate temporary writes. The two mode pins above are the deliberate exception to this file's usual posture: they assert a **declared-but-unenforced** boundary as it is, so that making it enforced is a visible test change rather than a silent one.

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
| Linked checkout is derived from loaded source not cwd. | `test_linked_checkout_is_derived_from_loaded_source_not_cwd` | mcp/tests/test_checkout_coordination_isolation.py:75-87 |
| Checkout config ignores live authority and uses only dummy root. | `test_checkout_config_ignores_live_authority_and_uses_only_dummy_root` | mcp/tests/test_checkout_coordination_isolation.py:89-108 |
| Incident shaped inbox write lands only in leaf dummy root. | `test_incident_shaped_inbox_write_lands_only_in_leaf_dummy_root` | mcp/tests/test_checkout_coordination_isolation.py:112-128 |
| Store guard refuses escape before creating lock or parent. | `test_store_guard_refuses_escape_before_creating_lock_or_parent` | mcp/tests/test_checkout_coordination_isolation.py:132-142 |
| Enclosure report write is allowed without opening coordination escape. | `test_enclosure_report_write_is_allowed_without_opening_coordination_escape` | mcp/tests/test_checkout_coordination_isolation.py:144-153 |
| Rewrite guard refuses a manually constructed live target. | `test_rewrite_guard_refuses_a_manually_constructed_live_target` | mcp/tests/test_checkout_coordination_isolation.py:155-163 |
| Primary checkout undeclared config access fails closed. | `test_primary_checkout_undeclared_config_access_fails_closed` | mcp/tests/test_checkout_coordination_isolation.py:165-172 |
| Explicit test mode preserves temporary store writes. | `test_explicit_test_mode_preserves_temporary_store_writes` | mcp/tests/test_checkout_coordination_isolation.py:174-182 |
| Any mode declaration lifts the primary refusal and the write confinement, with the refusal itself as the positive control. | `test_any_mode_declaration_lifts_the_primary_refusal_and_confinement` | mcp/tests/test_checkout_coordination_isolation.py:184-218 |
| The reserved lifecycle-operation mode is declarable by any caller, and reports as a writer of every store `mcp` owns. | `test_the_reserved_lifecycle_operation_mode_is_declarable_by_any_caller` | mcp/tests/test_checkout_coordination_isolation.py:220-241 |

## Cross-Repo References

No cross-repository implementation evidence is required for these local test and fixture claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| Fixture repositories and protocol doubles do not establish a live external integration. | N/A | N/A |

## Update History

- 2026-09-18T14:56+02:00 — 260918-TSIP-L3 curator (uncommitted change set on `ar/260918-tsip-l3-ar`,
  base `a12c511f`): this file is one of the leaf's five changed paths, so the card gained a **body**
  update rather than a restamp. The leaf added **two cases that pin the execution-mode boundary as
  it is** (`T30`/`T28`): a two-arm case whose arm A is the plane's real refusal (the positive control)
  and whose arm B shows one unauthenticated `declare_execution_mode("mcp")` lifting the refusal *and*
  switching `load_config` to the live authority settings, plus a case that drives
  `declare_lifecycle_operation_process()` — reserved in words to a plane-owned operation record and
  called by nothing — and observes `durable_process_role` reporting it as a store writer. The card
  states they are pins rather than endorsements and points at `D-L3-1`. **All eight retained rows
  moved +2** (two three-line insertions above them: the `declared_process_role` import and the
  `direct_execution_enabled` kwarg/payload), each re-derived from the new bytes and each verified to
  cover the same definition; **two rows were added** for the new cases. This card's source changed
  only after the code side was reviewed and repaired, so no earlier pass measured these numbers.
  `lastUpdated` advances with this body edit; `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are
  deliberately unchanged because the candidate is uncommitted and the governed closeout owns the real
  code commit.

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
