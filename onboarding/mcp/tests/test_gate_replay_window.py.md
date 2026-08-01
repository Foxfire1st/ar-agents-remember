# mcp/tests/test_gate_replay_window.py

| Field                  | Value                                    |
| ---------------------- | ---------------------------------------- |
| repository             | agents-remember                          |
| path                   | `mcp/tests/test_gate_replay_window.py`   |
| doc_type               | `file-level-onboarding`                  |
| lastUpdated            | 2026-08-01T14:20+02:00                   |
| lastVerifiedCommitHash |                                          `a714114ef94eedb8042fb4caa38d9469f4767dd6`|
| lastVerifiedCommitDate |                                          2026-08-01T18:06:36+02:00|
| governingOverview      | `overview.md`                            |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Proves that **one human approval can be consumed exactly once**, and — more usefully — proves
*what* makes that true, so the durability requirement behind it is derivable rather than asserted.

The entire defence against replaying a closeout approval is **one appended record**.
`worktrees/modules/closeout.py::_mark_closeout_gate_applied` appends an `apply_gate` snapshot, and
`controlplane/enforcement.py::evaluate_gate` has an explicit `applied` branch that refuses. There
is no in-memory flag, no marker file, no timestamp comparison. If that append is lost — which is
what the unlocked `GateStore` did whenever a compaction rewrote the log underneath it — the fold
reverts to the `approved` snapshot, `evaluate_gate` permits again, and the same approval is spent
a second time with no error and no log line.

`test_controlplane_store_durability.py` proves the loss across six record types. This file proves
what that loss costs on the one log that carries authority.

## Code Commentary

### Logic

**Four tests, in increasing order of what they cost to lose.**

`test_a_consumed_approval_cannot_be_replayed_by_a_second_closeout` (L130-L145) is the contract
itself: seed an approved gate, run the real `_enforce_closeout_gate` (permitted, correct gate id),
`_mark_closeout_gate_applied`, confirm the folded snapshot is now `applied`, and require the
second `_enforce_closeout_gate` to raise `RuntimeError` naming "already applied".

`test_the_applied_record_is_the_only_thing_closing_the_window` (L147-L174) is the
**counterfactual**, and is the reason durability is load-bearing here rather than tidy. After a
complete approve-and-apply it filters the log to the lines that do **not** contain
`APPLIED_MARKER` (L48, the literal `"state":"applied"`), asserts exactly two survive (the open and
approved snapshots — so the deletion removed one line and not, say, all of them), rewrites the log
with just those, and then asserts the guard is `permitted` **again**. Its failure message says
what a failure would mean: if this stops holding, the enforcement mechanism changed and the
durability requirement it justifies has to be re-derived.

`test_the_applied_record_survives_a_concurrent_gate_log_compaction` (L176-L205) is the regression.
Two real forked processes: `_compactor_main` (L106-L111) appends a prunable `alarm-ack` gate so
that a compaction actually rewrites, then runs `GateStore.compact` inside `parked_rewrite`
(imported from `_store_durability`), parked between its read and its commit; `_consumer_main`
(L94-L104) waits for the park and drives the real `_enforce_closeout_gate` +
`_mark_closeout_gate_applied`. That is the ordinary interleaving of an MCP tool applying a
closeout while a projection tick reclaims the same log. It then asserts **both** halves: the
folded gate reads `applied`, and the second enforcement raises.

`test_the_gate_fold_refuses_rather_than_skipping_a_torn_approval_record` (L207-L228) appends an
unterminated JSON fragment after a successful apply and requires the fold to surface it rather
than fold back to `approved`. See Todos — the assertion is looser than the claim.

**The fixture is where the honesty is.** `_seed_approved_gate` (L51-L80) builds a real
`closeout-approval` gate and decides it with `GateVerdict(decision="approve", by="developer", …)`.
`decidedBy="developer"` is not decoration: the agent's own `gate_decide` records
`decidedBy="model"`, which `approval_failure_reason` refuses, so only a decision a human actually
made reaches the branch under test. The timestamps are minted fresh rather than fixed because
`gate_keep_ids` drops any gate older than the 24 h interaction TTL — a hard-coded stamp would let
*retention* delete the gate, and the concurrency test would then fail (or, worse, pass) for a
reason unrelated to durability. A fresh gate can only leave this log by being lost.

### Conventions

**Production entry points, not payload builders.** Every test drives
`closeout_mod._enforce_closeout_gate` / `_closeout_gate_guard` / `_mark_closeout_gate_applied`
directly with a `SimpleNamespace(lifecycle_id, coordination_root)` standing in for the contract
(L96, L120-L122) and a bare `WorktreeArgs()`. Those three helpers read the same `GateStore` the
dashboard writes, so the seam under test is the real fold, not a re-implementation of it.

**`_prunable_gate` exists so a compaction has something to do** (L83-L91). Every store in this
family skips the rewrite when nothing is prunable, so a compaction pass over a log holding only
the live gate would never open the window this test forces.

**The forked processes are joined with a bound and the liveness is asserted** (L194-L196):
`process.join(30.0)` then `assertFalse(process.is_alive())`, so a wedged scenario is reported as
a failure rather than hanging the suite.

### Invariants And Boundaries

- The counterfactual must keep deleting **only** the `applied` line. Its `len(surviving) == 2`
  assertion is what stops it from degenerating into "empty the log and observe a gateless permit",
  which would prove nothing about that specific record.
- The seeded approval must stay developer-decided and freshly stamped. Model attribution or a
  fixed old timestamp both make the suite green for reasons that have nothing to do with the
  property.
- These tests spawn real processes via the `fork` context (L186). Threads would not reproduce the
  window: the loss being guarded against is cross-process.
- This file asserts the *consequence* of gate-log durability. The mechanism — the unconditional
  lock, the never-unlinking rewrite — is asserted in `test_controlplane_store_durability.py` and
  `test_durable_store_contract.py`; if those two are ever weakened, this file is where the cost
  shows up.

### Todos

**`test_the_gate_fold_refuses_rather_than_skipping_a_torn_approval_record` (L207-L228) asserts
much less than its docstring claims.** The docstring is about the strict read refusing a torn
line, but the body is `with self.assertRaises(Exception)` followed by
`assertNotIsInstance(raised.exception, AssertionError)`. `assertRaises(Exception)` accepts any
exception — including the `RuntimeError` that `_enforce_closeout_gate` raises for an entirely
different reason (a blocked or already-applied gate), which is exactly the exception the preceding
`_mark_closeout_gate_applied` guarantees on the *next* call. So the test would pass with the torn
line removed altogether. The `assertNotIsInstance(…, AssertionError)` guard is also inert here:
nothing inside the `assertRaises` block can raise `AssertionError`. The sibling suite states the
same property precisely — `TornLinePolicyTests.test_gate_enforcement_fold_refuses_a_torn_line`
requires `ValidationError` from `read` / `current` / `all_current`. Reported, not repaired: this
card does not modify the code worktree.

## Docs References

No Domain Documentation source is configured for this repository; the replay contract is defined
by repository code (`controlplane/enforcement.py` and `controlplane/records.py`).

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

The mechanism this file pins is three functions in two modules plus the store that has to keep one
record. The rows below are each of them, plus the sibling suites that hold the other halves.

| Finding | Citations | Source Path |
| --- | --- | --- |
| The whole defence, in one call: `_mark_closeout_gate_applied` appends an `apply_gate` snapshot and nothing else records the consume. | `_mark_closeout_gate_applied` L435-L440; `_enforce_closeout_gate` L421-L432; `_closeout_gate_guard` L407-L418 | [worktrees/modules/closeout.py](agents-remember/mcp/src/agents_remember/worktrees/modules/closeout.py) |
| The refusal branch that reads that snapshot — "was already applied; open a fresh gate for a new mutation" — and the `approved` branch it falls back to when the record is gone. | `evaluate_gate` L52-L94, with the `applied` branch L82-L87 and the `approved` branch L69-L73 | [controlplane/enforcement.py](agents-remember/mcp/src/agents_remember/controlplane/enforcement.py) |
| The pure snapshot the append carries: same gate id, `state="applied"`, decision attribution carried forward unchanged. | `apply_gate` L224-L233 | [controlplane/records.py](agents-remember/mcp/src/agents_remember/controlplane/records.py) |
| The log that has to keep it: the strict authority read, the last-wins fold the enforcement asks, and the compaction the regression races. | `read`; `current`; `compact` | [controlplane/store.py](agents-remember/mcp/src/agents_remember/controlplane/store.py) |
| The interposition primitive imported to park the compactor between its read and its commit. | `parked_rewrite` L482-L527 | [_store_durability.py](agents-remember/mcp/tests/_store_durability.py) |
| Why the append now survives: the lock is unconditional across append and rewrite, and the rewrite never unlinks. | `exclusive_access`; `rewrite_lines` | [controlplane/durable_store.py](agents-remember/mcp/src/agents_remember/controlplane/durable_store.py) |
| The suite that proves the same loss across all six record types and against the base commit; this file is the authority-level consequence of it. | L97-L168; L270-L310 | [test_controlplane_store_durability.py](agents-remember/mcp/tests/test_controlplane_store_durability.py) |
| The precise version of the torn-line claim this file's fourth test states loosely. | `test_gate_enforcement_fold_refuses_a_torn_line` L191-L210 | [test_controlplane_store_durability.py](agents-remember/mcp/tests/test_controlplane_store_durability.py) |
| The policy tests around the same enforcement fold: `apply_gate` purity, every `evaluate_closeout_gate` branch, and the closeout helpers over a temp `GateStore`. | `ApplyGateTests`, `EvaluateCloseoutGateTests`, `CloseoutEnforcementHelperTests` | [test_controlplane_gates.py](agents-remember/mcp/tests/test_controlplane_gates.py) |

## Cross-Repo References

No meaningful cross-repo references found: the gate log, the enforcement fold and the closeout
helpers are all inside `agents-remember`.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-01T14:20+02:00 — 260731-EFA-L5 curator: created the card for the replay-window suite.
  Recorded the mechanism exactly as the source has it — the defence against spending one human
  approval twice is a **single appended record**, `_mark_closeout_gate_applied`
  (`closeout.py` L435-L440) appending `apply_gate` (`records.py` L224-L233), refused on the next
  fold by `evaluate_gate`'s `applied` branch (`enforcement.py` L82-L87); no flag, no marker file,
  no timestamp comparison — and recorded that the counterfactual test
  (L147-L174) is what makes that falsifiable: it deletes **only** the line containing
  `APPLIED_MARKER` (L48), asserts exactly the two remaining snapshots survive so the deletion
  cannot have been indiscriminate, and then requires the guard to permit again. Recorded the
  concurrency regression (L176-L205) as two forked processes over `parked_rewrite`, with
  `_prunable_gate` (L83-L91) present so a compaction has something to drop and therefore actually
  rewrites, and the fixture's two deliberate choices (`decidedBy="developer"` because a
  model-decided gate is refused before the branch under test; fresh timestamps because the 24 h
  interaction TTL would otherwise delete the gate and produce a green or red run for the wrong
  reason). **Filed one Todo:**
  `test_the_gate_fold_refuses_rather_than_skipping_a_torn_approval_record` (L207-L228) asserts
  `assertRaises(Exception)` plus `assertNotIsInstance(…, AssertionError)`, which accepts the
  `RuntimeError` `_enforce_closeout_gate` raises for an already-applied gate — so it would pass
  with the torn line removed, and the `AssertionError` guard is inert because nothing in the block
  can raise one. The precise form of the same claim lives in
  `test_controlplane_store_durability.py::TornLinePolicyTests::test_gate_enforcement_fold_refuses_a_torn_line`
  (L191-L210), which requires `ValidationError`. Reported, not repaired. **Citations:** every self-citation into this suite was opened and checked against each symbol the claim names, ends included. Rows pointing into `controlplane/durable_store.py`, `store.py`, `attention_dismissals.py`, `expectation_rows.py` and `orchestration_nudges.py` are cited **by symbol name without a line range**: those five modules still carried unstaged edits in the code worktree while this card was written, so any range would have been stale on arrival; the symbol is the durable anchor and the linked file cards are authoritative for line numbers. Verification metadata is
  blank because the source file is new and uncommitted; closeout owns its first stamp.
