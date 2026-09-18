# mcp/src/agents_remember/memory/knowledge/candidate.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/candidate.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be`|
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

**The one admitted candidate-change operation: a validated batch, or nothing at all.** Everything else in the
substrate mutates through here (`KS-R03@v1`). The operation is deliberately narrow, and each of its three
properties is a shape rather than a promise:

- **It writes candidates only.** The batch's lane must be a writable candidate. A historical or accepted
  snapshot is refused by name before a statement runs, and the command union contains no promotion of any
  kind, so "this operation never accepts knowledge" is a property of the vocabulary.
- **It is all-or-nothing.** The preconditions, the commands and the integrity passes all run inside one
  `BEGIN IMMEDIATE` transaction under the candidate's one resource lock. A refusal rolls that transaction
  back, so a batch whose last command fails leaves the dataset exactly as it was — including the rows its
  earlier commands had already inserted.
- **Its receipts are facts.** `MutationResult` reports the logical identity before and after, the exact rows
  written or removed and, on failure, the typed refusal. It has no field that could carry a semantic judgement,
  an approval or an acceptance.

Two things it deliberately does **not** offer: there is no retry (a caller that loses the response rereads the
candidate and reconciles its own explicit proposal), and there is no arbitrary SQL.

## Code Commentary

### Logic

`change_candidate(store, batch, *, authorship)` is the entry point and its order is the whole contract:

```
require_writable_lane(batch.expected)          # BEFORE the lock: a property of the request
  -> store.exclusive_candidate_lock("change_candidate")
    -> store.immediate_transaction()           # one BEGIN IMMEDIATE
      -> _require_bound_context                # namespace, context digest, logical digest, schema version
        -> require_preconditions                # expectations, distinct commands, proposed origin,
                                                # insertions absent, command targets, completed-graph lineage
          -> apply_commands                     # the only writes
            -> require_after_integrity          # deferred FKs, every revision seal, both lineage graphs
              -> _bound_snapshot (after) -> COMMIT
```

- `require_writable_lane` is the fail-closed lane check. Two rules, both evaluated before the lock because both
  are properties of the request: a lane outside `CANDIDATE_LANES` refuses `target_not_candidate`, and
  `task-candidate` refuses `unauthorized_scope` until a resolved, owner-validated task binding can be required
  **and checked**. The operation cannot resolve a task contract, so accepting the lane on the strength of a
  caller-supplied reference would be the fail-open the packet's task-authority sentence forbids; the refusal
  names the missing binding rather than pretending the lane is unsupported. `require_candidate_lane` is kept as
  an alias of the newer name so an existing caller keeps working and the earlier spelling does not silently
  acquire the weaker meaning.
- `_require_bound_context` performs the four comparisons, each a refusal rather than a repair: the store's bound
  namespace, the presented context's **own** digest (so a context whose fields were edited after it was resolved
  is refused instead of being compared field by field), the logical dataset digest with both identities named,
  and the schema version.
- `_mapped_failure` translates a surviving `apsw.Error` using the position and kind the apply loop **observed**;
  when the failure arrived outside the loop it reports `outside_the_apply_loop` rather than naming a command the
  batch merely happened to declare last.
- `_refused_result` reports `after := before`, which is what makes "a refusal never describes a partially applied
  batch" true by construction. A refusal raised before the dataset was read (`_unbound_snapshot`) reports the
  context's own identity, because it cannot report a digest it never observed.
- `_success_result` returns `state="no_change"` when the committed logical identity equals the starting one, and
  otherwise builds the receipt from the ledger. `_changed_result` passes the ledger straight through: a dataset
  that moved with no entry at all is a defect the result model refuses, not an outcome this function invents.

### Conventions

- **The lock is taken once and outside the transaction.** `exclusive_candidate_lock` is the package's shared
  plumbing (`store.py`); the batch never takes a second lock, and `immediate_transaction()` exists precisely
  because `within_immediate` owns one transaction per action and a batch spans many.
- **`authorship` is a keyword parameter, never a batch field.** It comes from the admitted destination, so no
  part of a submitted payload can become the stored author, authorization or instant.
- **A defect is not an outcome.** A `KnowledgeStorageError` propagates: a caller could "handle" it as a refusal,
  which would report a defect as an expected result.
- Module docstring states the three properties above; the file is deliberately a boundary with no concept
  knowledge of its own.

### Invariants And Boundaries

- **One writer, one transaction, one lock.** This module constructs the only multi-record transaction in the
  package; every single-record operation still takes its own lock and `within_immediate`.
- **Validation order and execution order are different axes.** The preconditions judge the *completed* graph the
  batch declares (a predecessor may be created by any command in the batch, wherever it sits), while execution
  applies in the declared order and a later failure rolls back the earlier commands' rows.
- **The lane check is fail-closed in both directions.** `baseline` cannot be written and `task-candidate` cannot
  be written until its binding is resolvable; the increment writes the `draft-candidate` lane only.
- **No carried value is proof.** The context's tree ids and commit ids are recorded resolved facts; this module
  re-verifies only the namespace, the schema version, the context digest and the logical digest.
- **Boundary.** This module decides lane admissibility, the transaction boundary, the refusal mapping and the
  receipt state. Which conditions must hold *inside* the batch belongs to `batch_preconditions.py`, which
  statements run to `batch_commands.py`, and the wording of every refusal to `refusals.py`.
- **Reconsideration.** The `task-candidate` refusal is a deliberate interim contract: a later leaf that
  implements task admission must replace it with a required, checked binding, not simply drop it.

### Todos

None recorded for this slice. The disclosed cost is the logical body being computed three times per batch
(context re-derivation, before, after) — a deliberate cost for the pilot, which a later leaf may cache only
after demonstrating equivalent conformance.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The entry point, its pre-lock lane check and its one lock and one transaction. | `change_candidate` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80 |
| The two fail-closed lane rules and the alias that keeps the earlier spelling working. | `require_writable_lane`; `require_candidate_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:83-102; mcp/src/agents_remember/memory/knowledge/candidate.py:107-107 |
| The four in-transaction comparisons against the candidate actually held open. | `_require_bound_context` | mcp/src/agents_remember/memory/knowledge/candidate.py:148-183 |
| The transaction boundary and the observed-position mapping, including the no-position case. | `_within_batch_transaction`; `_apply_within_transaction`; `_mapped_failure` | mcp/src/agents_remember/memory/knowledge/candidate.py:110-125; mcp/src/agents_remember/memory/knowledge/candidate.py:128-145; mcp/src/agents_remember/memory/knowledge/candidate.py:251-267 |
| The three result builders, including the after-equals-before rule for refusals. | `_success_result`; `_changed_result`; `_refused_result` | mcp/src/agents_remember/memory/knowledge/candidate.py:186-222 |
| The receipt model that makes the no-moved-dataset-without-an-entry case unrepresentable, and the operation's own builder for it. | "class MutationResult("; `_changed_result` | mcp/src/agents_remember/models/knowledge/candidate.py:546-561; mcp/src/agents_remember/memory/knowledge/candidate.py:196-209 |
| The preconditions this operation runs inside the transaction. | "def require_preconditions(store: OpenedKnowledgeStore, batch: ChangeBatch) -> None:" | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:139-139 |
| The only writing step and the after-integrity re-proof. | `apply_commands`; `require_after_integrity` | mcp/src/agents_remember/memory/knowledge/batch_commands.py:165-165; mcp/src/agents_remember/memory/knowledge/batch_commands.py:727-727 |
| The lock the operation takes once, outside its transaction — declared on the opened store. | `exclusive_candidate_lock` | mcp/src/agents_remember/memory/knowledge/store.py:509-526 |
| The transaction wrapper the operation takes directly, because it spans many commands — also declared on the opened store. | ``immediate_transaction`` | mcp/src/agents_remember/memory/knowledge/store.py:491-498 |
| The task-lane refusal wording, which names the missing binding rather than the unsupported lane. | `batch_task_binding_unresolved_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:620-649 |
| The composed-path case that drives this operation through the admitted destination. | "test_a_late_invalid_command_rolls_back_every_earlier_insert_in_the_batch" | mcp/tests/test_candidate_batch_transaction.py:62-110 |
| The lane refusals' own nodes. | "test_a_baseline_lane_is_refused_as_a_non_candidate_target"; "test_a_task_candidate_lane_is_refused_until_its_binding_can_be_resolved" | mcp/tests/test_candidate_batch_transaction.py:374-394; mcp/tests/test_candidate_batch_transaction.py:1162-1188 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The operation writes one SQLite file inside the
worktree it was opened against; it resolves no Git object, writes no ledger row and addresses no sibling
repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T22:33:10+00:00: Generated citation repair: `require_preconditions` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:118-126. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the new candidate-change operation. It records the one-lock/one-immediate-transaction boundary, the pre-lock fail-closed lane check (baseline refused by name, `task-candidate` refused until a checkable binding exists), the four in-transaction comparisons, the observed-position refusal mapping, the after-equals-before rule for refusals, and the disclosed cost of computing the logical body three times per batch. Verification metadata remains empty until closeout stamps the code commit.
