# mcp/tests/test_checkout_coordination_isolation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkout_coordination_isolation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Pin the L19 mixed-version inbox incident's prevention boundary: unpublished linked-
worktree code receives a disposable leaf coordinator, cannot escape it through a live
config or direct durable-log target, and leaves regular MCP and explicit pytest behavior
intact.

## Code Commentary

### Logic

The suite builds repository-shaped temporary primary and linked checkouts without
depending on the real task enclosure. It proves checkout discovery follows the supplied
package source, skips incomplete nested repository shapes, and leaves installed packages
unmodified; invalid/live authority content is never read in linked CLI mode; the
synthetic config binds the candidate checkout and disables providers, dashboard autostart,
benchmarks, and automatic retirement; and an incident-shaped inbox row lands only under
`provider-runtime/dev-ar-coordination`.

The escape regressions call the actual shared durable-store primitives. The lock-path
case enters the returned context manager directly, asserts that entry raises, and proves
refusal happens before either the target parent or sibling lockfile exists; the rewrite
case proves a manually constructed live target cannot bypass config routing. The
operational-artifact case writes a real self-overwriting closeout report through those
same primitives under the exact enclosure `reports/` root, then proves no sibling
`operator-inbox.jsonl` appeared. The positive report target therefore does not widen
coordination authority.
Separate cases pin primary-checkout refusal, trusted MCP authority loading, and explicit
test-mode temporary writes. Trusted-config cases retain fail-loud invalid/non-object JSON
parsing while linked checkout mode deliberately ignores the supplied authority file.
The lifecycle-operation case declares the detached-worker mode before config loading,
then proves live authority is retained while the daemon-role slot remains empty.

### Invariants And Boundaries

- Tests patch the package-source anchor and contain the process declaration with the
  suite's owned-global preservation helper; no environment switch exists in production.
- The incident-shaped row is intentionally candidate-only and lives in a temporary dummy
  coordinator. No test writes the real coordinator.
- Enclosure reports are operational artifacts, not coordination rows; the positive
  report-write regression is paired with an explicit absent sibling inbox assertion.
- Trusted-mode coverage asserts preservation, not a compatibility fallback.
- Lifecycle-operation coverage is deliberately narrower than daemon trust: it proves
  live task-operation authority and simultaneously proves no MCP/dashboard writer role.

## 260815-DAG-L3 Writer-Role Projection

The lifecycle-operation isolation case now also proves `declared_process_role()` returns the
explicit detached writer role while the daemon-role view remains empty, preserving the distinction
between execution/store writer identity and MCP/dashboard daemon ownership.

## Update History

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
