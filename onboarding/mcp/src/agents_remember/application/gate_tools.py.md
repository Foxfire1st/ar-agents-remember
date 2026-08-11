# mcp/src/agents_remember/application/gate_tools.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/gate_tools.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c` |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Application operations for the ``gate_*`` control-plane use cases.

## Code Commentary

### Logic

Module-level surface:

- `_result` (function, lines 88-90) — Return the raw use-case result for the MCP adapter to finalize.
- `_store` (function, lines 93-94)
- `_inbox_store` (function, lines 97-98)
- `_expectation_store` (function, lines 101-102)
- `_gate_policy` (function, lines 105-107) — The active delegation policy; a config-less caller gets the human-only default.
- `_expectation_sla_seconds` (function, lines 110-113)
- `_write_verdict_by_row` (function, lines 116-132) — R2: a gate open atomically writes its ``verdict-by`` expectation row (same call, never a
- `_resolve_gate_lifecycle_id` (function, lines 135-144)
- `_entry_payload` (function, lines 147-148)
- `_decision_payload` (function, lines 151-156)
- `_resolve_deciding_actor` (function, lines 159-170)
- `_cancelled_wait_payload` (function, lines 173-185)
- `GateWait` (class, lines 189-203) — How a caller waits for a gate to resolve.
- `InboxWatch` (class, lines 207-213) — Which operator-inbox entries end a gate wait alongside a decision on the gate itself:
- `GateRaise` (class, lines 217-228) — One ``lifecycle_gate`` raise: which gate to open and what it asks of the developer.
- `gate_create_tool` (function, lines 244-277)
- `_gating_lifecycle` (function, lines 280-293) — The active lifecycle this gate raises against; only a running, matching one may gate.
- `_validated_ask` (function, lines 296-317) — Type-check the free-form ``ask`` mapping into the structured ask's three inputs.
- `_require_raise_and_continue_allowed` (function, lines 320-350) — Refuse a ``wait=false`` raise that policy does not permit.
- `_raised_gate_payload` (function, lines 353-381) — The immediate ``wait=false`` response: the gate is open and its id is the hand-off.
- `lifecycle_gate_tool` (function, lines 384-454)
- `raise_lifecycle_gate` (function, lines 457-479) — Compose the flat transport request into one lifecycle-gate use case.
- `gate_decide_tool` (function, lines 482-509)
- `gate_decide_for_lifecycle_tool` (function, lines 512-546) — Decide the lifecycle's latest still-open gate for an application caller.
- `record_gate_decision` (function, lines 549-568) — Compose transport verdict fields and decide the addressed gate.
- `record_lifecycle_gate_decision` (function, lines 571-590) — Compose transport verdict fields and decide a lifecycle's current gate.
- `gate_wait_tool` (function, lines 593-636) — Bounded wait until the gate leaves ``open`` (or ``timeout_seconds``).
- `gate_response_wait_tool` (function, lines 639-701) — Bounded wait for either a gate decision or a dashboard Chat inbox entry.
- `gate_list_tool` (function, lines 704-730)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the function `_result` (lines 88-90) — Return the raw use-case result for the MCP adapter to finalize.. | `_result` | mcp/src/agents_remember/application/gate_tools.py:92-94 |
| Defines the function `_store` (lines 93-94). | `_store` | mcp/src/agents_remember/application/gate_tools.py:97-98 |
| Defines the function `_inbox_store` (lines 97-98). | `_inbox_store` | mcp/src/agents_remember/application/gate_tools.py:101-102 |
| Defines the function `_expectation_store` (lines 101-102). | `_expectation_store` | mcp/src/agents_remember/application/gate_tools.py:105-106 |
| Defines the function `_gate_policy` (lines 105-107) — The active delegation policy; a config-less caller gets the human-only default.. | `_gate_policy` | mcp/src/agents_remember/application/gate_tools.py:109-111 |
| Defines the function `_expectation_sla_seconds` (lines 110-113). | `_expectation_sla_seconds` | mcp/src/agents_remember/application/gate_tools.py:114-117 |
| Defines the function `_write_verdict_by_row` (lines 116-132) — R2: a gate open atomically writes its ``verdict-by`` expectation row (same call, never a. | `_write_verdict_by_row` | mcp/src/agents_remember/application/gate_tools.py:116-132 |
| Defines the function `_resolve_gate_lifecycle_id` (lines 135-144). | `_resolve_gate_lifecycle_id` | mcp/src/agents_remember/application/gate_tools.py:135-144 |
| Defines the function `_entry_payload` (lines 147-148). | `_entry_payload` | mcp/src/agents_remember/application/gate_tools.py:151-152 |
| Defines the function `_decision_payload` (lines 151-156). | `_decision_payload` | mcp/src/agents_remember/application/gate_tools.py:151-156 |
| Defines the function `_resolve_deciding_actor` (lines 159-170). | `_resolve_deciding_actor` | mcp/src/agents_remember/application/gate_tools.py:159-170 |
| Defines the function `_cancelled_wait_payload` (lines 173-185). | `_cancelled_wait_payload` | mcp/src/agents_remember/application/gate_tools.py:173-185 |
| Defines the class `GateWait` (lines 189-203) — How a caller waits for a gate to resolve.. | `GateWait` | mcp/src/agents_remember/application/gate_tools.py:188-203 |
| Defines the class `InboxWatch` (lines 207-213) — Which operator-inbox entries end a gate wait alongside a decision on the gate itself:. | `InboxWatch` | mcp/src/agents_remember/application/gate_tools.py:206-213 |
| Defines the class `GateRaise` (lines 217-228) — One ``lifecycle_gate`` raise: which gate to open and what it asks of the developer.. | `GateRaise` | mcp/src/agents_remember/application/gate_tools.py:216-228 |
| Defines the function `gate_create_tool` (lines 244-277). | `gate_create_tool` | mcp/src/agents_remember/application/gate_tools.py:244-277 |
| Defines the function `_gating_lifecycle` (lines 280-293) — The active lifecycle this gate raises against; only a running, matching one may gate.. | `_gating_lifecycle` | mcp/src/agents_remember/application/gate_tools.py:280-293 |
| Defines the function `_validated_ask` (lines 296-317) — Type-check the free-form ``ask`` mapping into the structured ask's three inputs.. | `_validated_ask` | mcp/src/agents_remember/application/gate_tools.py:296-317 |
| Defines the function `_require_raise_and_continue_allowed` (lines 320-350) — Refuse a ``wait=false`` raise that policy does not permit.. | `_require_raise_and_continue_allowed` | mcp/src/agents_remember/application/gate_tools.py:320-350 |
| Defines the function `_raised_gate_payload` (lines 353-381) — The immediate ``wait=false`` response: the gate is open and its id is the hand-off.. | `_raised_gate_payload` | mcp/src/agents_remember/application/gate_tools.py:353-381 |
| Defines the function `lifecycle_gate_tool` (lines 384-454). | `lifecycle_gate_tool` | mcp/src/agents_remember/application/gate_tools.py:384-454 |
| Defines the function `raise_lifecycle_gate` (lines 457-479) — Compose the flat transport request into one lifecycle-gate use case.. | `raise_lifecycle_gate` | mcp/src/agents_remember/application/gate_tools.py:457-479 |
| Defines the function `gate_decide_tool` (lines 482-509). | `gate_decide_tool` | mcp/src/agents_remember/application/gate_tools.py:482-509 |
| Defines the function `gate_decide_for_lifecycle_tool` (lines 512-546) — Decide the lifecycle's latest still-open gate for an application caller.. | `gate_decide_for_lifecycle_tool` | mcp/src/agents_remember/application/gate_tools.py:512-546 |
| Defines the function `record_gate_decision` (lines 549-568) — Compose transport verdict fields and decide the addressed gate.. | `record_gate_decision` | mcp/src/agents_remember/application/gate_tools.py:549-568 |
| Defines the function `record_lifecycle_gate_decision` (lines 571-590) — Compose transport verdict fields and decide a lifecycle's current gate.. | `record_lifecycle_gate_decision` | mcp/src/agents_remember/application/gate_tools.py:571-590 |
| Defines the function `gate_wait_tool` (lines 593-636) — Bounded wait until the gate leaves ``open`` (or ``timeout_seconds``).. | `gate_wait_tool` | mcp/src/agents_remember/application/gate_tools.py:593-636 |
| Defines the function `gate_response_wait_tool` (lines 639-701) — Bounded wait for either a gate decision or a dashboard Chat inbox entry.. | `gate_response_wait_tool` | mcp/src/agents_remember/application/gate_tools.py:639-701 |
| Defines the function `gate_list_tool` (lines 704-730). | `gate_list_tool` | mcp/src/agents_remember/application/gate_tools.py:704-730 |

## Update History

- 2026-08-11T19:58+02:00 — No content impact: reviewed the `GateKind`/request-model import move into
  `models.structural.gates`; the application operations, policy, and gate state transitions
  documented here are unchanged.
- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
