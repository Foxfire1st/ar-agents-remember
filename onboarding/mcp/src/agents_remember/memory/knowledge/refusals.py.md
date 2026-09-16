# mcp/src/agents_remember/memory/knowledge/refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T08:24+02:00 |
| lastVerifiedCommitHash | `27242ecbefd79f2e8fbc6db32e02013fa8298ba3`|
| lastVerifiedCommitDate | 2026-09-16T08:41:27+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[memory route overview](../../overview.md)

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
- `unsupported_schema` and `no_change` are declared in the vocabulary but have no factory here; schema failures
  raise `KnowledgeStorageError` instead, and `no_change` is a *result state* rather than a refusal.

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
| The family, anchor and relation factories added with the graph half, one per failure. | `unknown_family_refusal`; `duplicate_family_refusal`; `duplicate_anchor_refusal`; `duplicate_relationship_refusal`; `missing_expected_row_refusal`; `stale_expected_row_refusal`; `referenced_anchor_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:310-324; mcp/src/agents_remember/memory/knowledge/refusals.py:337-358; mcp/src/agents_remember/memory/knowledge/refusals.py:420-441; mcp/src/agents_remember/memory/knowledge/refusals.py:492-513; mcp/src/agents_remember/memory/knowledge/refusals.py:514-530; mcp/src/agents_remember/memory/knowledge/refusals.py:531-552; mcp/src/agents_remember/memory/knowledge/refusals.py:553-567 |
| The write-path rule the descending branch describes, and its post-insert graph scope, now owned by the shared lineage module. | `_require_acyclic_lineage`; `find_cycle` | mcp/src/agents_remember/memory/knowledge/store.py:391-417; mcp/src/agents_remember/memory/knowledge/lineage.py:71-86 |
| The SQLite-error mapping, its caller-supplied failure context, and the trigger-message prefix that steers it. | `map_sqlite_error`; `SqliteFailureContext` | mcp/src/agents_remember/memory/knowledge/refusals.py:609-652; mcp/src/agents_remember/memory/knowledge/refusals.py:596-607 |
| The trigger messages the mapping depends on. | `IMMUTABILITY_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema.py:286-350 |
| The refusal codes these factories must stay within. | `KnowledgeRefusalCode` | mcp/src/agents_remember/models/knowledge/result.py:52-69 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded the L1 account of the SQLite-error mapping and extended the vocabulary to the graph half.** The earlier card described `map_sqlite_error` as taking a bare record id; that signature hard-coded `operation="create_invariant_revision"` and the invariant tables for every caller, so a mapped failure from any other write reported the wrong operation and the wrong row. The card now records the `SqliteFailureContext` signature and the eleven caller-supplied contexts, the two cycle refusals sharing one wording helper so the two lineage graphs cannot describe different rules, the fourteen new relation factories with the code each emits, and the corrected reachability statement (`missing_expected_row` is now produced; `no_change` remains a result state rather than a refusal, and `unsupported_schema` still has no producer). Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed refusal vocabulary. It records that refusals are returned values, that the two cycle branches must be true in their own case, and that the trigger-message prefix is a shared contract with the SQLite-error mapping. The final wording of the descending branch is the round-3 review outcome for sealed finding `RV-4`. Verification metadata remains empty until closeout stamps the code commit.
