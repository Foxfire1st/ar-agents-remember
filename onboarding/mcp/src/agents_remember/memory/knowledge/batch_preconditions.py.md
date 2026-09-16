# mcp/src/agents_remember/memory/knowledge/batch_preconditions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/batch_preconditions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

## Purpose

**Every precondition one candidate change batch must satisfy before it may write anything.** The whole module is
*pre*-conditions: it reads, it compares, and it raises `KnowledgeRefused`. **Nothing here writes**, which is what
makes "a refused batch leaves the stored dataset unchanged" a property of the code's shape rather than a promise
about its ordering.

Four rules shape every check, and they are the module's real content:

- **An expectation is a comparison, not a default.** A stated record state that does not match what is stored
  refuses; an identity the caller expected to be absent but that is stored refuses. A missing expectation is
  never read as permission to overwrite whatever is there.
- **An insertion is never an upsert.** A stored identity the caller believed it was creating means its read is
  stale, so the batch refuses and the caller rereads.
- **A command list is one authored act.** The same identity addressed by two *creating* commands refuses,
  because nothing says which of the two the author meant.
- **Validation is over the completed graph, not the request order.** A revision may declare any revision the
  batch creates, wherever in the sequence that command appears. What is checked is the completed graph: every
  declared predecessor must exist once the batch is applied, and a set of declarations that puts a revision on a
  lineage cycle is refused **by name** before any row is written.

## Code Commentary

### Logic

`require_preconditions` is the single entry point and it fixes the order:

```
require_expected_records      # every stated expectation is exactly what is stored
require_distinct_commands     # no two commands create one identity
require_no_accepted_origin    # no command stores accepted-origin data
require_insertions_absent     # no insertion targets an identity that is already stored
require_command_targets       # per-command targets, then the completed-graph lineage pass
```

- `require_expected_records` compares each `ExpectedRecord` through
  `candidate_records.stored_record_digest`. `present` demands the exact digest; `absent` refuses
  `duplicate_identity` when something is stored under that identity.
- `require_distinct_commands` walks `inserted_identities` per command and refuses a second creation of one
  identity. A removal or a label edit may name a row another command creates — that is what
  `inserted_identities` excludes.
- `require_no_accepted_origin` refuses any revision whose `state_at_origin` is not `PROPOSED_STATE` with
  `promotion_not_supported`, before any DML. Storing accepted-origin data would make this operation a promotion
  path, which it deliberately is not.
- `require_insertions_absent` refuses an insertion of an already-stored identity with `stale_precondition`
  naming `expected="<absent>"` — the caller's read is stale, and the alternative would be the operation deciding
  two aggregates are "the same" on the caller's behalf.
- `require_command_targets` builds the batch's **whole** declared identity set
  (`candidate_records.pending_identities`) once, then dispatches each command to its own target check, then runs
  the lineage pass. The docstring states the rule plainly: the order of the commands is how the author wrote
  them down, not the axis the declarations are validated on.
- `require_command_target` dispatches by command family: identity insert or label edit (`_require_identity`),
  new aggregate (`_require_new_invariant_revision` / `_require_new_family_revision`), anchor
  (`_require_anchor`), membership (`_require_membership`), claim (`_require_claim`).
  - `_require_identity` checks an identity insert against the stored row and a label edit against both the
    stored row's existence and the caller's `expected_row_digest`.
  - The two aggregate checks verify the owning identity through `present(...)` (so a batch may add a family and
    a family revision in either order), refuse an already-stored revision identity, and resolve each declared
    predecessor: one a command in this batch declares is admitted from the declaration, otherwise the stored
    revision must exist and belong to the same owning object (`cross_invariant_predecessor_refusal` /
    `cross_family_predecessor_refusal`).
  - `_require_endpoint` is the shared check for the relation endpoints (family revision, invariant revision,
    anchor), and the refusal wording differs per noun because the reader's remedy differs.
  - `_uncreated_predecessor`'s refusal says the predecessor is "neither stored nor declared by any command in
    this batch" and prescribes declaring it **in this batch — its position in the sequence does not matter**.
    That wording is deliberate: the earlier-only remedy was withdrawn with the earlier-only rule.
- **The completed-graph lineage pass.** `require_completed_lineage` gathers the invariant and family edges the
  batch declares (`_declared_edges`), then `_require_declared_acyclic` hands both edge sets to
  `lineage.declared_cycle` — the stored edges as `edges`, the batch's declarations as `declared`, and
  `_wider_edges` as the `extras` callable that supplies each judged revision's *other* declarations. The
  judgement therefore belongs to the shared lineage rule rather than to a second cycle rule grown here, and a
  cycle formed entirely inside one batch is refused by name before any row exists. The pass reports only
  revisions the batch itself creates (`_creators_of`): a stored revision's position was settled when it was
  written.

### Conventions

- Every check raises `KnowledgeRefused`; nothing returns a boolean, so a caller cannot ignore a precondition by
  forgetting to branch.
- The batch refusals name the failing command as `"<index>:<kind>"`, which is why `_require_identity`,
  `_uncreated_predecessor` and `_require_endpoint` build `batch_command_refusal` rather than a per-record
  factory: the caller submitted a batch and needs to know which command in it failed.
- The per-command dispatch is a sequence of `isinstance` guards on the frozen union, each returning early, so
  the order reads as the decision it is. Adding a command kind means adding one guard and one check.
- Nothing in this module takes a lock, opens a transaction or writes; it is called from inside the batch's
  transaction and reads through the store's connection.

### Invariants And Boundaries

- **Read-only, always.** A refusal raised here happens before the first INSERT, and the batch's transaction
  rolls back regardless, so the two mechanisms agree rather than one depending on the other.
- **The completed graph is the validation axis**, and the apply step's own after-integrity pass re-proves the
  same property over the rows that were actually written. This pass exists so the refusal names the batch's own
  declarations. Do not reintroduce a per-command prefix rule, and do not add a second cycle rule.
- **A declared identity is admitted only for the command kinds that create.** Note the deliberate consequence
  recorded in the hand-off: `remove_source_anchor` carries no expected row digest (unlike the other two
  removals), so the anchor's own immutability trigger plus the repeat-removal refusal are what keep it safe.
- **One key digest rule.** `expected_row_digest` is the row digest as the read operations expose it
  (`get_invariant().row_digest`, `get_family().row_digest`), never a re-derived value; for a revision the
  digest is the sealed `payload_digest`.
- **Boundary.** This module decides *what must hold*; it does not decide which statements run
  (`batch_commands.py`), how a refusal is worded (`refusals.py`), or whether the lane is writable at all
  (`candidate.py`).
- **Reconsideration.** If body removal semantics change, the anchor removal's missing expected digest is the
  asymmetry to revisit — the other two removals already name the row they expect.

### Todos

None recorded for this slice. One open item this leaf hands on: the `remove_source_anchor` command carries no
expected row digest, unlike the other two removals; nothing unsafe is reachable today (the anchor payload is
immutable by trigger and a repeat removal refuses `missing_expected_row`), but it is a decision for whoever
reworks removals next.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The single entry point and the order it fixes. | `require_preconditions` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:79-86 |
| The four rules the module is built on, stated once in its docstring. | "Four rules shape the checks" | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1-21 |
| The expectation comparison, including the expected-absence branch. | `require_expected_records` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:89-110 |
| The one-authored-act duplicate rule and the accepted-origin refusal. | `require_distinct_commands`; `require_no_accepted_origin` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:113-129; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:132-144 |
| The insertion-is-never-an-upsert rule. | `require_insertions_absent` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:147-163 |
| The completed-graph rule stated where the whole-batch pending set is built. | `require_command_targets` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:166-178 |
| The lineage pass that hands the batch's own declarations to the shared rule. | `require_completed_lineage`; `_require_declared_acyclic`; `_wider_edges` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:181-204; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:225-253; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:256-264 |
| The per-command dispatch and the identity/label check. | `require_command_target`; `_require_identity` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:282-308; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:311-348 |
| The two aggregate checks, which admit an owner a command in the same batch declares. | `_require_new_invariant_revision`; `_require_new_family_revision` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:366-401; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:404-439 |
| The refusal that states the completed-graph remedy rather than prescribing a reorder. | `_uncreated_predecessor` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:442-454 |
| The shared endpoint check and its per-noun remedy wording. | `_ENDPOINT_NOUN`; `_require_endpoint` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:535-567 |
| The shared lineage rule this pass calls with the batch's declared edges. | `declared_cycle`; `find_cycle` | mcp/src/agents_remember/memory/knowledge/lineage.py:71-105; mcp/src/agents_remember/memory/knowledge/lineage.py:107-131 |
| The identity vocabulary this module reads through. | `present`; `pending_identities`; `inserted_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:145-169 |
| The node that proves the completed-graph pass refuses a cycle the operation cannot yet see. | "test_the_completed_graph_pass_refuses_a_cycle_the_operation_cannot_see_yet" | mcp/tests/test_candidate_batch_transaction.py:561-604 |
| The node that proves a batch may author its lineage in any order. | "test_a_batch_may_author_its_lineage_in_any_order" | mcp/tests/test_candidate_batch_transaction.py:470-516 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the batch precondition module. It records the four shaping rules (expectations are comparisons, an insertion is never an upsert, a command list is one authored act, and validation is over the completed graph), the read-only boundary that makes a refused batch leave the dataset untouched, the whole-sequence pending set that makes a forward reference legal, and the lineage pass that hands the batch's declared edges to the shared rule instead of growing a second cycle rule. Also recorded the carried anchor-removal asymmetry as the open item. Verification metadata remains empty until closeout stamps the code commit.
