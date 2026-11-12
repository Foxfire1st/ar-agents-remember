# mcp/src/agents_remember/application/tool_response.py

## Governing Overview

[overview](overview.md)

## Purpose

Complete one tool result at the application boundary.

## Code Commentary

### Logic

Module-level surface:

- `_attach_contract_guidance` — Attach a stale installed build's currentness reading; preserve explicit producer recovery; otherwise derive only exact-contract guidance and the two argument-bound preview stops.
- `complete_tool_response` — Validate the whole result, shape or receive its status projection, log, measure final delivery, and observe one application result.

The registered response model is selected and validated before final output. Contract-bounded operational hints,
and the `buildCurrentness` reading of a call served by a stale installed build, are attached as model fields through the finalizer's enrichment callback;
whole-result serialization then retains that finalized payload. An explicit caller-sized `answer`
projection wins when supplied. Without it, `_select_shaped_answer` applies the task/landing/role
projectors only to their owned tools; unrelated tools retain the stripped whole result. That default selection invokes `truncate_lists`, except for a `server-build-stale` refusal, which keeps its stripped whole result without projection or list cap. Whichever answer is shaped, a finalized `buildCurrentness` is copied onto it. An explicit `answer` is instead dict-copied and does not pass through that default list-cap function; an under-bound explicit mapping returns unchanged by the token guard. Both paths retain whole-result validation/logging and the final delivered-token guard, whose short form is not a universal per-list cap.
Explicit producer recovery guidance takes precedence; cross-task guidance is omitted. Observer
completion receives the finalized whole payload with the delivered answer count, not a rebuilt result.

Caller diffs are separate readable reports: `_attach_caller_diff_report` attempts to retain the
complete diff independently of the investigation detail. A cut diff names that report when it
exists, otherwise the available detail or an honest not-retained marker. Waited role replies are
fitted to keep their beginning after log attachment and again after a late line error, before the
generic guard. These answer changes preserve one workspace completed-call event and do
not supply Git, task or review acceptance.

### Event River Feed At The Completion Choke

`complete_tool_response` always records the call once in the workspace river through
`record_tool_completed`, with the finalized whole payload and delivered answer count.
There is no ambient lifecycle branch, session-adoption prerequisite or second event stream. The tool answers as if the
event had been written even when the write is counted as dropped.

### Answer boundary and log wiring

`complete_tool_response` finalizes through the answer choke (`models/tools/tool_answer`): the
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

- The enrichment sets `buildCurrentness` on the validated envelope only when the call carries a stale installed-build reading. [5]
- A `server-build-stale` refusal keeps its stripped whole result, without a tool projection or list cap. [6]
- Whichever answer is shaped, the finalized `buildCurrentness` is copied onto it. [7]
