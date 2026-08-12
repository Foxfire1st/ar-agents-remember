# mcp/tests/test_checkout_coordination_isolation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_checkout_coordination_isolation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T09:18+02:00 |
| lastVerifiedCommitHash |  `284ddbcd879a0b1ea58c9997ff781fb471982c36`|
| lastVerifiedCommitDate |  2026-08-12T09:23:37+02:00|
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
case proves a manually constructed live target cannot bypass config routing.
Separate cases pin primary-checkout refusal, trusted MCP authority loading, and explicit
test-mode temporary writes. Trusted-config cases retain fail-loud invalid/non-object JSON
parsing while linked checkout mode deliberately ignores the supplied authority file.

### Invariants And Boundaries

- Tests patch the package-source anchor and contain the process declaration with the
  suite's owned-global preservation helper; no environment switch exists in production.
- The incident-shaped row is intentionally candidate-only and lives in a temporary dummy
  coordinator. No test writes the real coordinator.
- Trusted-mode coverage asserts preservation, not a compatibility fallback.

## Update History

- 2026-08-12T09:18+02:00 — 260731-EFA-L20 reopen: the lock-path refusal now asserts the context manager's raising `__enter__` directly, removing an intentionally unreachable body line while preserving the same pre-lock and pre-parent safety contract.
- 2026-08-12T08:41+02:00 — No content impact: 260731-EFA-L20 removed an unreachable context body and the script-only main guard; every checkout-isolation assertion and refusal boundary documented above remains unchanged.
- 2026-08-10T18:31+02:00 — 260731-EFA-L21 quality completion: added explicit incomplete-checkout, installed-package, and trusted malformed-config cases for every changed defensive branch.
- 2026-08-10T18:31+02:00 — 260731-EFA-L21: created with linked/primary resolution, synthetic-config, incident-shaped write, escape-refusal, MCP, and pytest regression cases. Verification metadata remains blank until approved closeout commits the code.
