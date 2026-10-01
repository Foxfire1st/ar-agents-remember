# mcp/src/agents_remember/memory/knowledge/batch_preconditions.py

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
require_facet_generation      # each record group's dataset-generation guard, in turn
require_composition_generation
require_evidence_generation
require_effect_generation
require_census_generation
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

**The census generation precondition, and the target check that reads the payload seam.** `require_census_generation` joins the same run of generation guards, now the fifth of them, in the same position — after the accepted-origin refusal and before `require_insertions_absent`, so it refuses before any row is written. It is free for a batch that declares no census command: `census_commands` filters on `_CENSUS_KINDS`, and only a hit delegates to `census_records.require_census_generation(store)`, which reads the dataset's own recorded generation and refuses one that predates the census's three record tables and their three relations, carrying both numbers as facts and migrating nothing. The three census commands then each dispatch to `_census_check` through `_TARGET_CHECKS`. That check re-states the generation guard, resolves the record kind and frozen schema the command declares from `_CENSUS_DECLARATIONS`, and validates the payload through `record_envelope.validate_record_payload`, so an unregistered kind, a schema inadmissible for its kind or a payload carrying an undeclared field is the shipped `invalid_payload` refusal rather than a storage error. **Reference resolution is deliberately not in that check.** It belongs to the record group's own write step, which runs inside the apply pass in the order the author wrote the commands, so a disposition that links to a claim the same batch creates resolves once that claim's command has run — the same disposition the completed-graph rule takes for lineage, and the reason this check validates shape and generation only.

### Conventions

- Every check raises `KnowledgeRefused`; nothing returns a boolean, so a caller cannot ignore a precondition by
  forgetting to branch.
- The batch refusals name the failing command as `"<index>:<kind>"`, which is why `_require_identity`,
  `_uncreated_predecessor` and `_require_endpoint` build `batch_command_refusal` rather than a per-record
  factory: the caller submitted a batch and needs to know which command in it failed.
- The per-command dispatch is a sequence of `isinstance` guards on the frozen union, each returning early, so
  the order reads as the decision it is. Adding a command kind means adding one guard and one check; a group
  whose commands all share one shape rule adds one entry per command to `_TARGET_CHECKS`, each naming the same
  check, as the three census commands do.
- A check that must validate a command's declared payload shape names that pair once, in a mapping declared
  beside the check (`_CENSUS_DECLARATIONS`), rather than spelling the kind and schema inside the dispatch table:
  the payload seam and the check then cannot disagree about which frozen shape the payload was written against.
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
  (`candidate.py`). A census command's *references* are not checked here either: resolving a claim's evidence,
  its realization attribution or a disposition's links belongs to the record group's own write step, which sees
  the rows the batch creates in command order — so a disposition may link to a claim the same batch creates, and
  a check here could not express that without becoming a second, prefix-ordered rule.
- **Reconsideration.** If body removal semantics change, the anchor removal's missing expected digest is the
  asymmetry to revisit — the other two removals already name the row they expect.

### Todos

None recorded for this slice. One open item this leaf hands on: the `remove_source_anchor` command carries no
expected row digest, unlike the other two removals; nothing unsafe is reachable today (the anchor payload is
immutable by trigger and a repeat removal refuses `missing_expected_row`), but it is a decision for whoever
reworks removals next.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The single entry point and the order it fixes. [1]
- The four rules the module is built on, stated once in its docstring. [2]
- The expectation comparison, including the expected-absence branch. [3]
- The one-authored-act duplicate rule and the accepted-origin refusal. [4]
- The insertion-is-never-an-upsert rule. [5]
- The completed-graph rule stated where the whole-batch pending set is built. [6]
- The lineage pass that hands the batch's own declarations to the shared rule. [7]
- The per-command dispatch and the identity/label check. [8]
- The two aggregate checks, which admit an owner a command in the same batch declares. [9]
- The refusal that states the completed-graph remedy rather than prescribing a reorder. [10]
- **The shared endpoint check: it refuses a missing relation endpoint before any row is written, naming the offending identity in the refusal's `record_id` and the endpoint kind in its `table`.** [11]
- The per-noun remedy wording the shared check reads, so a refusal names the endpoint kind the caller actually supplied. [12]
- The shared lineage rule this pass calls with the batch's declared edges. [13]
- The identity vocabulary this module reads through. [14]
- The one-authored-act duplicate rule and the accepted-origin refusal. [15]
- The insertion-is-never-an-upsert rule. [16]
- The completed-graph rule stated where the whole-batch pending set is built. [17]
- The lineage pass that hands the batch's own declarations to the shared rule. [18]
- The per-command dispatch and the identity/label check. [19]
- The two aggregate checks, which admit an owner a command in the same batch declares. [20]
- The refusal that states the completed-graph remedy rather than prescribing a reorder. [21]
- The shared endpoint check and its per-noun remedy wording. [22]
- The shared lineage rule this pass calls with the batch's declared edges. [23]
- The identity vocabulary this module reads through. [24]
- **The census record group's generation guard: free for a batch that declares no census command, and otherwise the record group's own refusal, read from the open store so both numbers travel as facts.** [25]
- **The closed three-command vocabulary the generation guard's filter is built from.** [26]
- **The census target check: the generation guard restated, then the command's declared kind and frozen schema resolved from the declarations table and validated through the envelope seam, so an unregistered kind or an undeclared field is `invalid_payload` rather than a storage error. Reference resolution is deliberately absent — that belongs to the record group's own write step, in command order.** [27]
- **The dispatch table every command kind carries an entry in, where the three census commands name `_census_check`.** [28]
- **The payload seam the census target check validates through — the one place any write path decides whether a payload is admissible for the kind and schema it declares.** [29]
- The node that proves the completed-graph pass refuses a cycle the operation cannot yet see. [30]
- The node that proves a batch may author its lineage in any order. [31]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
