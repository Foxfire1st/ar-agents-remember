# mcp/src/agents_remember/application/tool_response.py

## Governing Overview

[overview](overview.md)

## Purpose

Complete one tool result at the application boundary.

## Code Commentary

### Logic

Module-level surface:

- `_attach_contract_guidance` — Preserve explicit producer recovery; otherwise derive only exact-contract guidance and the two argument-bound preview stops.
- `complete_tool_response` — Validate the whole result, shape or receive its status projection, log, measure final delivery, and observe one application result.

The registered response model is selected and validated before final output. Contract-bounded operational hints
are attached as model fields through the finalizer's enrichment callback; the removed notifier contributes no banner,
then whole-result serialization retains that finalized payload. An explicit caller-sized `answer`
projection wins when supplied. Without it, `_select_shaped_answer` applies the task/landing/role
projectors only to their owned tools; unrelated tools retain the stripped whole result. That default selection invokes `truncate_lists`. An explicit `answer` is instead dict-copied and does not pass through that default list-cap function; an under-bound explicit mapping returns unchanged by the token guard. Both paths retain whole-result validation/logging and the final delivered-token guard, whose short form is not a universal per-list cap.
Explicit producer recovery guidance takes precedence; cross-task guidance is omitted. Observer
completion receives the finalized whole payload with the delivered answer count, not a rebuilt result.

Caller diffs are separate readable reports: `_attach_caller_diff_report` attempts to retain the
complete diff independently of the investigation detail. A cut diff names that report when it
exists, otherwise the available detail or an honest not-retained marker. Waited role replies are
fitted to keep their beginning after log attachment and again after a late line error, before the
generic guard. These answer changes preserve one workspace completed-call event and do
not supply Git, task or review acceptance.

### 260928-MIK-L114 Event River Feed At The Completion Choke

`complete_tool_response` always records the call once in the workspace river through
`record_tool_completed`, with the finalized whole payload and delivered answer count.
There is no ambient lifecycle branch, session-adoption prerequisite or second event stream. The tool answers as if the
event had been written even when the write is counted as dropped.

### MIK-R108 answer boundary and log wiring

`complete_tool_response` now finalizes through the answer choke (`models/tools/tool_answer`): the
envelope count fields are stripped, over-bound answers leave as the measured short form, and the
whole result is filed beside the daily log. `_write_delivered_line` re-runs the guard after every
late line failure and keeps the short-form ceiling once the answer is cut; the observer and the log
line count the delivered answer, and `_canonical_json` is the canonical form used for whole-result
byte accounting.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence


- Whole-result validation/logging and explicit or default tool-specific projected-answer guarding remain distinct. [4]


### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Exact-contract enrichment preserves explicit recovery guidance, with guarded preview stops from the call argument. [2]


- The completion choke validates the whole, selects the answer, retains available caller diff reports, measures final delivery and emits one event through its existing owner. [3]


## L23 Final Candidate Disposition

The response completion boundary continues to normalize bounded task-addressed payloads only. L23's
operation phase and report evidence can pass through the existing response contract, while private
operation keys, worker PIDs, leases, and resume tokens remain absent.

## Historical CCR-R18@v1 Task-Addressed Next-Step Bounding

**Historical producer account, not the present ambient-state architecture.** The retained account below records the earlier guard and its original coordinates. The current owner is `_attach_contract_guidance`: it preserves explicit recovery, uses only response-bound contract guidance or the same-call summary-only approval stops, and retains the response-address comparison. Removed ambient producers and their old source/test coordinates below are provenance, not current implementation or fresh execution evidence.

260831-CCR-L18 added `bound_next_step(response, step)` (line 30): before a lifecycle tool response advertises `nextStep`, any guidance whose `nextArgs` name a task address (`contract_path` / `enclosure_path` / camel-case variants) is checked against the response's own exact address (`contractPath` / `enclosurePath`). Guidance that names a different task address — or whose response is ambiguously addressed across multiple paths — is omitted (step becomes None), while exact-address and address-free/external guidance survives unchanged. `_attach_lifecycle_tail` now routes both the producer-supplied `nextStep` and the ambient-derived step through this guard before publishing the envelope, so a cross-task recovery edge can never be offered from another contract's response.

## Historical 260918-TSIP-L6 Guidance-Guard Defect And Repair

The following source-bound defect/repair account is retained as historical evidence. Its ambient source, producer paths, line numbers and case counts do not describe the current contract-only producer; the current active guard is described and cited above.

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
