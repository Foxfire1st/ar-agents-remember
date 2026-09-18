# mcp/src/agents_remember/memory/knowledge/batch_preconditions.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/batch_preconditions.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[memory route overview](../overview.md)

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

**The evidence generation precondition, and the target check that goes with it.** `require_evidence_generation` is called from `require_preconditions` beside the facet generation check and before any row is written: it compares the dataset's own recorded generation with the one that registers the supporting-record tables and refuses with both versions as facts, so a version-1 dataset — or any dataset older than this leaf's tables — is not migrated, repaired or extended in place. `evidence_commands` is the filter that makes the check free for a batch that declares no supporting-record command. The command-union, mutable-table and target-check lists this module owns were extended for the two appended commands; each carries its own target check, so the union case's `set(_TARGET_CHECKS) == kinds` assertion still holds and a command without a check still fails.

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
| The single entry point and the order it fixes. | "def require_preconditions(store: OpenedKnowledgeStore, batch: ChangeBatch) -> None:" | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:156-156 |
| The four rules the module is built on, stated once in its docstring. | "Four rules shape the checks" | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1-21 |
| The expectation comparison, including the expected-absence branch. | `require_expected_records` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:165-186 |
| The one-authored-act duplicate rule and the accepted-origin refusal. | `require_distinct_commands`; `require_no_accepted_origin` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:193-209; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:212-232 |
| The insertion-is-never-an-upsert rule. | `require_insertions_absent` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:326-342 |
| The completed-graph rule stated where the whole-batch pending set is built. | `require_command_targets` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:345-357 |
| The lineage pass that hands the batch's own declarations to the shared rule. | `require_completed_lineage`; `_require_declared_acyclic`; `_wider_edges` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:292-319; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:393-429; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:423-449; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:325-328; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:361-362; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:462-468 |
| The per-command dispatch and the identity/label check. | `require_command_target`; `_require_identity` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:457-493; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:513-565; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:162-162 |
| The two aggregate checks, which admit an owner a command in the same batch declares. | `_require_new_invariant_revision`; `_require_new_family_revision` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:583-619; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:621-657; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:619-619 |
| The refusal that states the completed-graph remedy rather than prescribing a reorder. | `_uncreated_predecessor` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:780-792 |
| **The shared endpoint check: it refuses a missing relation endpoint before any row is written, naming the offending identity in the refusal's `record_id` and the endpoint kind in its `table`.** | `_require_endpoint` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:955-1034 |
| The per-noun remedy wording the shared check reads, so a refusal names the endpoint kind the caller actually supplied. | "_ENDPOINT_NOUN: dict[str, str] = {" | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1237-1237 |
| The shared lineage rule this pass calls with the batch's declared edges. | `declared_cycle`; `find_cycle` | mcp/src/agents_remember/memory/knowledge/lineage.py:71-105; mcp/src/agents_remember/memory/knowledge/lineage.py:107-131 |
| The identity vocabulary this module reads through. | `inserted_identities`; `pending_identities`; `present` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:324-331; mcp/src/agents_remember/memory/knowledge/candidate_records.py:332-340; mcp/src/agents_remember/memory/knowledge/candidate_records.py:341-442; mcp/src/agents_remember/memory/knowledge/candidate_records.py:468-482; mcp/src/agents_remember/memory/knowledge/candidate_records.py:485-486 |
| The one-authored-act duplicate rule and the accepted-origin refusal. | `require_distinct_commands`; `require_no_accepted_origin` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:193-209; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:212-232 |
| The insertion-is-never-an-upsert rule. | `require_insertions_absent` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:326-342 |
| The completed-graph rule stated where the whole-batch pending set is built. | `require_command_targets` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:345-357 |
| The lineage pass that hands the batch's own declarations to the shared rule. | `require_completed_lineage`; `_require_declared_acyclic`; `_wider_edges` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:328-353; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:429-457; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:460-468; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:361-362; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:493-501 |
| The per-command dispatch and the identity/label check. | `require_command_target`; `_require_identity` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:493-501; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:564-601; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:526-530; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:649-655 |
| The two aggregate checks, which admit an owner a command in the same batch declares. | `_require_new_invariant_revision`; `_require_new_family_revision` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:619-654; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:657-692; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:704-708 |
| The refusal that states the completed-graph remedy rather than prescribing a reorder. | `_uncreated_predecessor` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:780-792 |
| The shared endpoint check and its per-noun remedy wording. | "_ENDPOINT_NOUN: dict[str, str] = {"; `_require_endpoint` | mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:767-783; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:786-1152; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:749-749; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1230-1237 |
| The shared lineage rule this pass calls with the batch's declared edges. | `declared_cycle`; `find_cycle` | mcp/src/agents_remember/memory/knowledge/lineage.py:71-105; mcp/src/agents_remember/memory/knowledge/lineage.py:107-131 |
| The identity vocabulary this module reads through. | `present`; `pending_identities`; `inserted_identities` | mcp/src/agents_remember/memory/knowledge/candidate_records.py:190-195; mcp/src/agents_remember/memory/knowledge/candidate_records.py:198-433; mcp/src/agents_remember/memory/knowledge/candidate_records.py:207-442; mcp/src/agents_remember/memory/knowledge/candidate_records.py:476-486; mcp/src/agents_remember/memory/knowledge/candidate_records.py:468-473 |
| The node that proves the completed-graph pass refuses a cycle the operation cannot yet see. | "test_the_completed_graph_pass_refuses_a_cycle_the_operation_cannot_see_yet" | mcp/tests/test_candidate_batch_transaction.py:561-604 |
| The node that proves a batch may author its lineage in any order. | "test_a_batch_may_author_its_lineage_in_any_order" | mcp/tests/test_candidate_batch_transaction.py:470-516 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T10:45:13+00:00: Generated citation repair: "def require_preconditions(store: OpenedKnowledgeStore, batch: ChangeBatch) -> None:" repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:156-156. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_uncreated_predecessor` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:780-792. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "_ENDPOINT_NOUN: dict[str, str] = {" repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1237-1237. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `_uncreated_predecessor` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:780-792. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "def require_preconditions(store: OpenedKnowledgeStore, batch: ChangeBatch) -> None:" repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:155-155. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_insertions_absent` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:326-342. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_command_targets` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:345-357. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "_ENDPOINT_NOUN: dict[str, str] = {" repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1206-1206. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_insertions_absent` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:326-342. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: `require_command_targets` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:345-357. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "def require_preconditions(store: OpenedKnowledgeStore, batch: ChangeBatch) -> None:" repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:152-152. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `require_expected_records` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:165-186. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `require_insertions_absent` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:294-310. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `require_command_targets` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:313-325. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `_uncreated_predecessor` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:695-707. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: "_ENDPOINT_NOUN: dict[str, str] = {" repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:1152-1152. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `require_insertions_absent` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:294-310. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `require_command_targets` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:313-325. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `require_completed_lineage`; `_require_declared_acyclic`; `_wider_edges` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:328-353; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:429-457; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:460-468. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `require_command_target`; `_require_identity` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:493-501; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:564-601. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `_require_new_invariant_revision`; `_require_new_family_revision` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:619-654; mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:657-692. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:21:19+00:00: Generated citation repair: `_uncreated_predecessor` repointed to mcp/src/agents_remember/memory/knowledge/batch_preconditions.py:695-707. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 6 generated projection bullet(s) by hand while resolving the memory sync** — `require_preconditions`, `require_expected_records`, `require_insertions_absent`, `require_command_targets`, `_uncreated_predecessor`, `present`, `pending_identities`, `inserted_identities`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T05:00:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read every claim this leaf's additions moved, re-cited each by hand, and retired the one generated projection bullet that had rewritten a range mechanically.** The leaf added the declared-graph composition cycle pass, four target checks and the generation guard; the shared endpoint check was re-scoped so the offending identity travels as `record_id` and the endpoint kind as `table`. Rows were split wherever one claim named several anchors across several extents, so each row's anchor now resolves inside a range that holds it. The endpoint claim was **sharpened** rather than softened: it now states the naming behaviour the construct has. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:55:00+00:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): **re-read the `_require_endpoint` claim against the construct as it now stands, sharpened it and re-cited it by hand, and removed the generated projection bullet that had rewritten its range mechanically.** The construct genuinely changed: this leaf made the shared endpoint check name the offending identity in the refusal's `record_id` and the endpoint kind in its `table`, so the claim now states that instead of only "the shared endpoint check". The range is the declaration's own extent (`:1034`), an agent's read rather than a projection. A mechanically projected range is unverified evidence. Verification metadata is **not** advanced over unreviewed content; the code commit does not exist yet and closeout owns that stamp.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 7 generated projection bullet(s) by hand** — `require_preconditions`, `require_expected_records`, `require_insertions_absent`, `require_command_targets`, `_uncreated_predecessor`, `_ENDPOINT_NOUN`, `_require_endpoint`, `present` and 2 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **re-read every citation this card carries against the current source and repaired the ranges this leaf's addition moved.** This entry recorded the evidence generation precondition and the per-command target check, both refusing before any row is written. Verification metadata is unchanged and the code commit does not exist yet; closeout owns that stamp.

- 2026-09-16T08:10:00+00:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): created this one-to-one card for the batch precondition module. It records the four shaping rules (expectations are comparisons, an insertion is never an upsert, a command list is one authored act, and validation is over the completed graph), the read-only boundary that makes a refused batch leave the dataset untouched, the whole-sequence pending set that makes a forward reference legal, and the lineage pass that hands the batch's declared edges to the shared rule instead of growing a second cycle rule. Also recorded the carried anchor-removal asymmetry as the open item. Verification metadata remains empty until closeout stamps the code commit.
