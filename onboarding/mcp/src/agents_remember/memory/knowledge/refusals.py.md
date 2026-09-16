# mcp/src/agents_remember/memory/knowledge/refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `76c7697ca275a8d2764729145c950c166f3f9ec3`|
| lastVerifiedCommitDate | 2026-09-16T10:27:28+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[memory route overview](../../../overview.md)

## Purpose

The typed refusal vocabulary, the two exceptions that carry it, and the SQLite-error mapping. Every refusal in
the package is built by one of the factories here, so the codes, the offending record and the advertised next
action live in one place instead of being spelled out per call site.

## Code Commentary

### Logic

Two exception types: `KnowledgeStorageError` (a storage failure no contract code describes — a defect report,
not an expected outcome) and `KnowledgeRefused` (internal control flow that carries a typed refusal out of a
transaction so the operation can roll back and return it).

`RefusalFacts` is the optional identifying bundle (`table`, `record_id`, `expected`, `observed`), and the generic
`refusal(...)` factory builds one `KnowledgeRefusal`.

One factory per case: `scope_refusal` (returns `None` when the namespaces match), `invalid_payload_refusal`,
`duplicate_revision_refusal`, `duplicate_invariant_refusal`, `repository_rebind_refusal`,
`unknown_invariant_refusal`, `dangling_predecessor_refusal`, `cross_invariant_predecessor_refusal`,
`lineage_cycle_refusal`, `lock_capability_refusal`, `candidate_busy_refusal`.

**The relation factories this package's graph half added.** One per failure, each emitting exactly one code:
`family_lineage_cycle_refusal` (`lineage_cycle`), `unknown_family_refusal` (`unknown_family` — a code
introduced with the family half), `invalid_family_payload_refusal` (`invalid_payload`),
`duplicate_family_refusal` and `duplicate_family_revision_refusal` and `duplicate_anchor_refusal` and
`duplicate_relation_identity_refusal` (`duplicate_identity`, each carrying the expected and observed digests
or labels), `dangling_family_predecessor_refusal` and `cross_family_predecessor_refusal` and
`missing_relation_endpoint_refusal` (`invalid_reference`), `duplicate_relationship_refusal` and
`referenced_anchor_refusal` (`relationship_constraint`), `missing_expected_row_refusal`
(`missing_expected_row` — declared in L1, first produced here), and `stale_expected_row_refusal`
(`stale_precondition` — a code introduced with the removal contract).

The two relations share one refusal **shape** through the factories' keyword-only context
(`operation`, `table`, `record_id`) rather than through duplicated code, which is what lets a membership
refusal and a realization refusal be worded identically without being the same call.

**The batch-scoped factories this leaf added.** The candidate-change operation composes the single-record
operations, so its refusals are built here rather than by the per-record factories: a caller that submitted
one batch needs to know **which command** in it failed, and the code has to name the batch as the operation
it addressed. Two of them introduce codes this leaf made reachable:

- `batch_target_not_candidate_refusal` — `target_not_candidate` (new). A lane that is not a writable
  candidate is refused by name before the lock is taken.
- `batch_task_binding_unresolved_refusal` — `unauthorized_scope`. A `task-candidate` lane is refused until a
  resolved, owner-validated task binding can be required **and checked**; the refusal names the missing
  binding (`expected` = "a resolved, owner-validated task binding", `observed` = the caller's reference or
  `<no task reference supplied>`) rather than pretending the lane is unsupported, and it cannot be satisfied
  by a caller asserting its own `task_ref`.
- `batch_promotion_not_supported_refusal` — `promotion_not_supported` (new). Accepted-origin data is refused
  before any DML: storing it would make this operation a promotion path.
- `batch_absent_target_refusal`, `batch_duplicate_expectation_refusal` — `duplicate_identity`, for an
  expectation of absence that does not hold and for one identity addressed by two creating commands.
- `batch_stale_record_refusal`, `batch_context_refusal`, `batch_context_digest_refusal` —
  `stale_precondition`, for a stored record that differs from the stated expectation, a dataset identity
  that differs from the batch's context (both digests named), and a context whose sealed digest does not
  seal it.
- `batch_lineage_cycle_refusal` — `lineage_cycle`, restated for the batch because the caller needs to know
  which graph came out cyclic.
- `batch_refusal` — the relabelling factory: it takes one command's own refusal and returns it as a refusal
  of the batch, **preserving** the inner code, the offending record and the remedy while adding the command's
  index and kind to the detail and setting `operation="change_candidate"`. A batch failure therefore reads
  exactly like the single-record failure it is.
- `batch_command_refusal` — the builder for the batch conditions the per-record factories cannot express;
  its `command` argument is `"<index>:<kind>"`, so one string carries both the position the caller has to
  look at and the kind of command that was there.

`lineage_cycle_refusal` and its family sibling `family_lineage_cycle_refusal` share
`_lineage_cycle_wording`, so the two graphs cannot drift into describing different rules; only the object
noun, the operation and the edge table differ. Both have two branches and the message names which applied,
because the remedy differs. `candidate_on_cycle=True` states the predecessors would put the revision on a
cycle ("it would be reachable from itself") and names resolving the cycle at that revision. The descending
branch states the predecessors descend from a revision already on a lineage cycle, names the ancestor cycle
in `observed`, and says explicitly that the candidate is **not itself on that cycle** — claiming
self-reachability there would be false, because nothing points at the candidate.

`map_sqlite_error` maps a surviving `apsw.Error` by message: an `immutable_revision`-prefixed message to
`immutable_revision`, a foreign-key message to `invalid_reference`, any other constraint message to
`relationship_constraint`, and everything else to `invalid_payload`. It takes a `SqliteFailureContext`
(`operation`, `table`, `record_id`) rather than a bare record id, because a constraint failure carries no
operation identity of its own. This too is a repair of an L1 defect: the earlier signature hard-coded
`operation="create_invariant_revision"` and the invariant tables for **every** caller, so a mapped failure
arising from a repository, invariant, family, anchor, membership or claim write reported the wrong operation
and sent the caller to the wrong row. The operation and table now come from the caller-supplied context at
all eleven call sites.

### Conventions

A refusal is a **returned value**, not an exception: callers branch on a code instead of parsing a message. The
exceptions exist only for the two cases a return value cannot express — an unclassifiable storage failure, and a
refusal raised from inside a transaction that must be rolled back first.

### Invariants And Boundaries

- A reachable expected failure returns a `KnowledgeRefusal` with one of the contract codes; `KnowledgeStorageError`
  means the caller has found a defect, not an outcome to handle.
- The trigger text `immutable_revision: …` is the steering signal that maps a trigger-originated SQLite error to
  the right code, so the schema's trigger messages and this mapping are one contract.
- **A mapped failure must name the operation and table it actually came from.** The mapping cannot know either
  one, so the caller supplies them; a hard-coded pair is wrong for every operation but one.
- **A code names one failure.** Two failures that need different remedies get different codes even when they
  arrive at the same factory shape — which is why a dangling predecessor and a cross-family predecessor are both
  `invalid_reference` while a stale row and an absent row are `stale_precondition` and `missing_expected_row`.
- Every refusal names a `next_action`; guidance for the descending-cycle branch names both remedies (author an
  acyclic successor, and resolve the ancestor cycle reported in `observed`), and the anchor-lifetime refusal says
  explicitly that an anchor is never removed because its source disappeared.
- `unsupported_schema` and `no_change` are declared in the vocabulary but have **no factory and no producer**
  here; schema failures raise `KnowledgeStorageError` instead. **This is a carried limitation, not a gap this
  leaf left open.** The refusal *code* `no_change` remains the L1/L2 owner-ruled reservation, so a consumer must
  not branch on it; what the candidate-change batch makes reachable is the *result state*
  `MutationResult.state == "no_change"` (an empty or net-zero batch), which is a different vocabulary driving a
  different branch. Every batch-scoped refusal above names a `next_action` that tells the caller to reread and
  author a new explicit batch; none of them silently rebases.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The defect-report exception versus the internal control-flow exception. | `KnowledgeStorageError`; `KnowledgeRefused` | mcp/src/agents_remember/memory/knowledge/refusals.py:27-44 |
| The facts bundle and the one generic factory every refusal is built through. | `RefusalFacts`; `refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:48-56; mcp/src/agents_remember/memory/knowledge/refusals.py:57-79 |
| The two-branch cycle refusal whose text must be true in both directions, and the family sibling that shares its wording. | `lineage_cycle_refusal`; `family_lineage_cycle_refusal`; `_lineage_cycle_wording` | mcp/src/agents_remember/memory/knowledge/refusals.py:238-264; mcp/src/agents_remember/memory/knowledge/refusals.py:265-286; mcp/src/agents_remember/memory/knowledge/refusals.py:290-309 |
| The family, anchor and relation factories added with the graph half, one per failure. | `unknown_family_refusal`; `duplicate_family_refusal`; `duplicate_anchor_refusal`; `duplicate_relationship_refusal`; `missing_expected_row_refusal`; `stale_expected_row_refusal`; `referenced_anchor_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:310-323; mcp/src/agents_remember/memory/knowledge/refusals.py:337-357; mcp/src/agents_remember/memory/knowledge/refusals.py:420-440; mcp/src/agents_remember/memory/knowledge/refusals.py:492-512; mcp/src/agents_remember/memory/knowledge/refusals.py:514-529; mcp/src/agents_remember/memory/knowledge/refusals.py:531-551; mcp/src/agents_remember/memory/knowledge/refusals.py:553-566 |
| The batch-scoped factories, including the two codes this leaf made reachable and the fail-closed task-lane refusal. | `batch_target_not_candidate_refusal`; `batch_task_binding_unresolved_refusal`; `batch_promotion_not_supported_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:605-618; mcp/src/agents_remember/memory/knowledge/refusals.py:620-649; mcp/src/agents_remember/memory/knowledge/refusals.py:651-664 |
| The relabelling factory that preserves a command's own code, record and remedy while naming the batch. | `batch_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:743-763 |
| The builder whose `command` argument carries both the failing position and its kind. | `batch_command_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:791-813 |
| The context and stale-record refusals that name both digests. | `batch_context_refusal`; `batch_context_digest_refusal`; `batch_stale_record_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:713-726; mcp/src/agents_remember/memory/knowledge/refusals.py:728-741; mcp/src/agents_remember/memory/knowledge/refusals.py:696-711 |
| The write-path rule the descending branch describes, and its post-insert graph scope, now owned by the shared lineage module. | `require_acyclic_lineage`; `find_cycle`; `declared_cycle` | mcp/src/agents_remember/memory/knowledge/store.py:674-705; mcp/src/agents_remember/memory/knowledge/lineage.py:107-131; mcp/src/agents_remember/memory/knowledge/lineage.py:71-105 |
| The SQLite-error mapping, its caller-supplied failure context, and the trigger-message prefix that steers it. | `map_sqlite_error`; `SqliteFailureContext` | mcp/src/agents_remember/memory/knowledge/refusals.py:828-871; mcp/src/agents_remember/memory/knowledge/refusals.py:815-826 |
| The trigger messages the mapping depends on. | `IMMUTABILITY_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema.py:286-350 |
| The refusal codes these factories must stay within, now including the two this leaf added. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:55-75 |
| The operation that produces the batch codes, and the alias that keeps the earlier lane-check name working. | `change_candidate`; `require_writable_lane`; `require_candidate_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/memory/knowledge/candidate.py:83-102; mcp/src/agents_remember/memory/knowledge/candidate.py:107-107 |
| The two nodes that reach the batch lane refusals on a real store. | "test_a_baseline_lane_is_refused_as_a_non_candidate_target"; "test_a_task_candidate_lane_is_refused_until_its_binding_can_be_resolved" | mcp/tests/test_candidate_batch_transaction.py:374-393; mcp/tests/test_candidate_batch_transaction.py:1162-1188 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): **recorded the batch-scoped refusal vocabulary and separated the result state from the refusal code.** The candidate-change operation composes the single-record operations, so its refusals are built here: two codes this leaf made reachable (`target_not_candidate` for a non-candidate lane, `promotion_not_supported` for accepted-origin data), the fail-closed `unauthorized_scope` refusal for a `task-candidate` lane whose resolved binding this operation cannot check, the two-digest context and stale-record refusals, the batch lineage restatement, and the two builders — `batch_refusal`, which relabels one command's refusal while **preserving** its code, record and remedy, and `batch_command_refusal`, whose `command` argument is the `"<index>:<kind>"` pair the caller needs. The card now states as a carried limitation that the refusal *code* `no_change` still has no producer and must not be branched on, while the *result state* `MutationResult.state == "no_change"` is the reachable vocabulary — the distinction the worker's earlier report got wrong on the report side and the handoff states correctly. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded the L1 account of the SQLite-error mapping and extended the vocabulary to the graph half.** The earlier card described `map_sqlite_error` as taking a bare record id; that signature hard-coded `operation="create_invariant_revision"` and the invariant tables for every caller, so a mapped failure from any other write reported the wrong operation and the wrong row. The card now records the `SqliteFailureContext` signature and the eleven caller-supplied contexts, the two cycle refusals sharing one wording helper so the two lineage graphs cannot describe different rules, the fourteen new relation factories with the code each emits, and the corrected reachability statement (`missing_expected_row` is now produced; `no_change` remains a result state rather than a refusal, and `unsupported_schema` still has no producer). Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed refusal vocabulary. It records that refusals are returned values, that the two cycle branches must be true in their own case, and that the trigger-message prefix is a shared contract with the SQLite-error mapping. The final wording of the descending branch is the round-3 review outcome for sealed finding `RV-4`. Verification metadata remains empty until closeout stamps the code commit.
