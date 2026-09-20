# mcp/src/agents_remember/application/tool_response.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/tool_response.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-19T19:52+02:00 |
| lastVerifiedCommitHash | `7879f5b22c34a912f939e27868786818463c3b9c` |
| lastVerifiedCommitDate | 2026-09-19T20:18:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[overview](overview.md)

## Purpose

Complete one tool result at the application boundary.

## Code Commentary

### Logic

Module-level surface:

- `_agent_notifier_banner` (function, lines 22-31) — Return the stale-supervisor banner without blocking a tool response.
- `_attach_lifecycle_tail` (function, lines 34-44)
- `complete_tool_response` (function, lines 47-61) — Validate, enrich, count, and observe one application result.

The registered response model is selected and validated before final output. Lifecycle hints
and notifier banners are attached as model fields through the finalizer’s enrichment callback,
then token counting and serialization cover the complete emitted response. Explicit producer
recovery guidance takes precedence; cross-task guidance is omitted. Observer tool completion
receives that same finalized payload rather than an independently reconstructed response.

cit:([`complete_tool_response`], mcp/src/agents_remember/application/tool_response.py:131-145)
cit:([`_attach_lifecycle_tail`], mcp/src/agents_remember/application/tool_response.py:112-128)

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
| Defines the function `_agent_notifier_banner` (lines 22-31) — Return the stale-supervisor banner without blocking a tool response.. | `_agent_notifier_banner` | mcp/src/agents_remember/application/tool_response.py:100-109 |
| Defines the function `_attach_lifecycle_tail` (lines 34-44). | `_attach_lifecycle_tail` | mcp/src/agents_remember/application/tool_response.py:112-128 |
| Defines the function `complete_tool_response` (lines 47-61) — Validate, enrich, count, and observe one application result.. | `complete_tool_response` | mcp/src/agents_remember/application/tool_response.py:131-145 |

## L23 Final Candidate Disposition

The response completion boundary continues to normalize bounded task-addressed payloads only. L23's
operation phase and report evidence can pass through the existing response contract, while private
operation keys, worker PIDs, leases, and resume tokens remain absent.

## CCR-R18@v1 Task-Addressed Next-Step Bounding

260831-CCR-L18 added `bound_next_step(response, step)` (line 30): before a lifecycle tool response advertises `nextStep`, any guidance whose `nextArgs` name a task address (`contract_path` / `enclosure_path` / camel-case variants) is checked against the response's own exact address (`contractPath` / `enclosurePath`). Guidance that names a different task address — or whose response is ambiguously addressed across multiple paths — is omitted (step becomes None), while exact-address and address-free/external guidance survives unchanged. `_attach_lifecycle_tail` now routes both the producer-supplied `nextStep` and the ambient-derived step through this guard before publishing the envelope, so a cross-task recovery edge can never be offered from another contract's response.

## 260918-TSIP-L6 The Guidance Guard Binds Guidance To The Response's Own Address

`bound_next_step` (`:58-99`) is the only thing connecting guidance derived from the
*process-global* ambient lifecycle (`application/next_step.py::next_step_for` reads
`LifecycleState.enclosure`) to the response that carries it. `260918-TSIP` `T54` recorded a closed
closeout for one leaf shipping a `nextStep` naming **another master's** contract, and the guard
fired on neither of its two exits. Both are repaired:

- a response that declares **no** contract path of its own cannot be validated, and its guidance is
  now withheld rather than emitted unchecked. The old form returned the step here
  (`if not response_paths: return step`), which is exactly the hole `T54` came through;
- every path spelling the guidance carries must name the response's own place, so one stale
  spelling is enough to withhold the hint. The old form required the guidance's path set to be
  exactly `{expected}`, which let a hint carrying both spellings through whenever only one of them
  was stale.

`_names_the_same_place` (`:31-57`) is the comparison, and its tolerance is exactly the immediate
container: the contract file, or `dirname(file)`. Both spellings are set to the contract FILE by
every producer (`worktrees/modules/guidance.py:171-176` and `:443-444`,
`application/lifecycle/start_result.py:121`, `application/lifecycle/reopen.py:104`). An earlier,
wider form of this function accepted *any* ancestor directory — wider than the rule it claimed —
and was narrowed in the same leaf; the behaviour is pinned at its own level by
`mcp/tests/test_response_address_binding.py` (4 cases), and the producer half — the closed payload
declaring its own `contractPath` in the envelope's spelling — is pinned there and driven end to
end by `mcp/tests/test_transaction_only_worktree_delivery.py:275-284`.

## Update History
- 2026-09-19T19:52+02:00 — 260918-TSIP-L6 (uncommitted change set on `ar/260918-tsip-l6-ar`, base `a1351504`): recorded `T54`'s guard repair — unvalidatable guidance is withheld and any disagreeing path spelling withholds the hint — and `_names_the_same_place`'s narrowed tolerance (the contract file, or its immediate container). Every citation range re-derived against the repaired file. Verification metadata stays closeout-owned.

- 2026-09-04T10:05+02:00 — 260831-CCR-L18 Gate-5 memory pass: recorded the `bound_next_step` task-address guard on lifecycle tool responses (cross-task guidance omitted). Verified at code commit f93ac631ca161e5880db3a937728cb256686b13b.

- 2026-08-24T00:51+02:00 — No content impact: 260821-CLIVE-L2 the source only repoints `finalize_tool_response` to its moved `models.tools` package. Verified at code commit `1d446724`.
- 2026-08-14T06:30+02:00 — No contract expansion: L23 keeps tool-response completion bounded while
  carrying the existing task-addressed lifecycle-operation projection; private recovery identity
  remains excluded. Verification stays closeout-owned.

- 2026-08-08T22:10+02:00 — 260713-TES-L1 completion round (curator): refreshed this sidecar body for the supervisor -> agent-notifier rename (module paths, identifiers, settings keys, wire keys, prose) and the compat seams; verification metadata pinned until closeout stamps the 260713-TES-L1 commit.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
