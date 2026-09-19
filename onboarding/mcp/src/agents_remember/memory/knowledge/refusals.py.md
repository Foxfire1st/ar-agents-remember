# mcp/src/agents_remember/memory/knowledge/refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:10+02:00 |
| lastVerifiedCommitHash | `47570cd827428c171613c8cb01e01f0b1cb26f73`|
| lastVerifiedCommitDate | 2026-09-20T01:58:41+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

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

**The candidate-lifecycle and publication factories this leaf added.** Seven factories, one per observable failure
point, so a caller branches on a code rather than on prose. All seven share one property stated once in the group's
own comment: **nothing in this group removes, replaces or repairs a database, a receipt or a published snapshot to
make a later step succeed.** The existing bytes are preserved in every case.

- `selected_input_unavailable_refusal` — `selected_input_unavailable` (new). One explicitly selected input is
  absent or unreadable. A missing input is an **input error, never an empty dataset**: the alternative — answering
  an absent selection with a fresh schema — is how a reader comes to report "no knowledge" for a candidate whose
  file simply was not there. Its `next_action` states that nothing falls back to `HEAD`, a branch name or Markdown.
- `candidate_binding_changed_refusal` — `candidate_binding_changed` (new). The candidate's recorded binding is not
  the admission's. This is the restart and branch-switch refusal, and it is also how an ambiguous or unbound
  namespace is reported; the working database is preserved exactly as it was, because the authored work it holds is
  not reproducible from the new baseline.
- `candidate_snapshot_unpublished_refusal` — `candidate_snapshot_unpublished` (new). A read whose runtime
  candidate is not the dataset the closed snapshot holds. It is a **report, not a repair**: the publication is a
  separate explicit operation owned by the caller, and no read publishes rows or attaches them to an older
  snapshot. It carries both digests plus the destination reference.
- `snapshot_incomplete_refusal` — `snapshot_incomplete` (new). A private stage that was not completed, verified or
  durably flushed. **Both halves use this one code** — a closed snapshot that could not be frozen *and* a candidate
  whose receipt or database could not be sealed in its private stage — because in both cases nothing outside the
  operation's own stage exists afterwards, so the caller has one decision to make (stop, or retry from the same
  expected input) and the destination or admitted path was never touched.
- `destination_stale_refusal` — `destination_stale` (new). The admitted destination is not the destination that is
  there. It names what was found (`<unreadable: …>` or the observed digest) and `expected` as `<absent>` when the
  caller admitted absence, and its remedy is to reread and republish against the identity that is actually there.
- `publication_failed_refusal` — `publication_failed` (new). The install or the readback did not complete: the
  atomic replacement raised, or the installed file does not carry the identity that was frozen. No success is
  reported for bytes this operation did not install.
- `publication_durability_unconfirmed_refusal` — `publication_durability_unconfirmed` (new). **The honest code for
  a success-shaped outcome that cannot be confirmed:** the replacement completed but the destination could not be
  re-read. The complete new file may already be at the destination, and saying so is the point — claiming the old
  file was restored would be false, and claiming success from an unverified readback would be unchecked. Its
  remedy tells the caller to reopen the destination directly rather than restore the previous file blindly.

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
- `no_change` is declared in the vocabulary but has **no factory and no producer** here; the *result state*
  `MutationResult.state == "no_change"` and the *publication state* `SnapshotPublicationResult.state ==
  "no_change"` are the reachable vocabulary, and they drive different branches. **This is a carried limitation,
  not a gap this leaf left open.** The refusal *code* remains the L1/L2 owner-ruled reservation, so a consumer must
  not branch on it. Every batch-scoped refusal names a `next_action` that tells the caller to reread and author a
  new explicit batch; none of them silently rebases.
- `unsupported_schema` still has **no factory in this module**, but since this leaf it *is* reachable as a produced
  code: `materialization.publication_state` and the candidate lifecycle build it directly through the generic
  `refusal(...)` factory for a file or baseline that is not a database of this schema. It is therefore no longer
  accurate to describe the code as unreachable — only as factory-less, which is a deliberate split (the schema
  failures that this package's own open path hits stay `KnowledgeStorageError`, because they are defects in a file
  the caller handed us, while a *selected input* that is not this schema is an expected failure with a remedy).
- **A lifecycle or publication refusal preserves existing bytes.** The seven factories this leaf added state one
  rule between them: none of them removes, replaces or repairs a database, a receipt or a published snapshot to
  make a later step succeed. A caller that retries does so against the same explicitly selected input.

### Todos

None recorded.

### 260915-KS-L17 — The Three Composition Refusal Factories

This leaf added three factories beside the shipped ones, and each restates a **modelled** failure as a
typed `KnowledgeRefusal` rather than letting an exception escape:

- `composition_policy_refusal` — an unknown policy identity, an unknown version of a known identity, a
  malformed declaration and a scope a policy may not widen. The identity, the version and, for the
  version case, the versions the identity **does** declare all travel in the refusal's facts, so a
  caller branches on data rather than on message text.
- `composition_traversal_refusal` — a not-permitted edge and a step past the declared bound. The
  bound case is the one that must never be reported as a scope: a truncated traversal presented as a
  scope is a false statement about what was reached.
- `family_composition_cycle_refusal` — a cycle found by the shipped shared lineage rule, carrying the
  revision ids on the cycle so the caller can name them.

**They are factories, not a new vocabulary.** No new `KnowledgeRefusalCode` member was minted for the
composition half: each factory restates through the shipped codes, which is why the code union's
membership is unchanged by this leaf while the *operation* union gained three names.

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
| The write-path rule the descending branch describes, and its post-insert graph scope, now owned by the shared lineage module. | `require_acyclic_lineage`; "def find_cycle("; "def declared_cycle(" | mcp/src/agents_remember/memory/knowledge/store.py:698-728; mcp/src/agents_remember/memory/knowledge/lineage.py:97-130; mcp/src/agents_remember/memory/knowledge/lineage.py:133-157 |
| The SQLite-error mapping, its caller-supplied failure context, and the trigger-message prefix that steers it. | `map_sqlite_error`; `SqliteFailureContext` | mcp/src/agents_remember/memory/knowledge/refusals.py:828-871; mcp/src/agents_remember/memory/knowledge/refusals.py:815-826 |
| **The candidate-lifecycle and publication group this leaf added: one factory per observable failure point.** | `selected_input_unavailable_refusal`; `candidate_binding_changed_refusal`; `candidate_snapshot_unpublished_refusal`; `snapshot_incomplete_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:882-902; mcp/src/agents_remember/memory/knowledge/refusals.py:904-928; mcp/src/agents_remember/memory/knowledge/refusals.py:930-949; mcp/src/agents_remember/memory/knowledge/refusals.py:951-974 |
| **The destination and install failures, including the honest durability code.** | `destination_stale_refusal`; `publication_failed_refusal`; `publication_durability_unconfirmed_refusal` | mcp/src/agents_remember/memory/knowledge/refusals.py:976-999; mcp/src/agents_remember/memory/knowledge/refusals.py:1001-1018; mcp/src/agents_remember/memory/knowledge/refusals.py:1020-1039 |
| The trigger messages the mapping depends on. | `IMMUTABILITY_TRIGGERS` | mcp/src/agents_remember/memory/knowledge/schema.py:286-350 |
| The refusal codes these factories must stay within, now including the batch codes and the seven this leaf added. | "KnowledgeRefusalCode = Literal[" | mcp/src/agents_remember/models/knowledge/result.py:161-161 |
| The operation that produces the batch codes, and the alias that keeps the earlier lane-check name working. | `change_candidate`; `require_writable_lane`; `require_candidate_lane` | mcp/src/agents_remember/memory/knowledge/candidate.py:61-80; mcp/src/agents_remember/memory/knowledge/candidate.py:83-102; mcp/src/agents_remember/memory/knowledge/candidate.py:110-110 |
| The two nodes that reach the batch lane refusals on a real store. | "test_a_baseline_lane_is_refused_as_a_non_candidate_target"; "test_a_task_candidate_lane_is_refused_until_its_binding_can_be_resolved" | mcp/tests/test_candidate_batch_transaction.py:374-393; mcp/tests/test_candidate_batch_transaction.py:1162-1188 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-19T22:33+02:00 — 260918-TSIP-L11 curator (memory worktree `fd1a024e`, code `7879f5b2`): cleared the inherited citation debt on 1 claim(s) by RE-READING each claim against the merged tree and RE-DERIVING every cited range from the construct's real extent in the file the claim cites (`extents.anchor_extents`), never by adding a delta to an old number and never through the mechanical projection (no generated citation-repair bullet is written, so no claim is reopened by this edit). Claims re-read: `refusals.py.md:223` (`change_candidate`, `require_writable_lane`, `require_candidate_lane`).
- 2026-09-18T12:07:24+00:00: Generated citation repair: "KnowledgeRefusalCode = Literal[" repointed to mcp/src/agents_remember/models/knowledge/result.py:161-161. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:00+02:00 — 260915-KS-L17 curator (uncommitted change set on `ar/260915-ks-l17`, base `e963a01c`): recorded the **three composition refusal factories this leaf added** and the fact that they add no vocabulary: each restates a modelled failure through the *shipped* refusal codes, so the code union's membership is unchanged while the operation union gained three names. The section names what each factory carries — the policy identity and version (and, for an unknown version, the versions the identity does declare); the not-permitted edge and the exceeded bound, the latter because a truncated traversal reported as a scope is a false statement about what was reached; and the cycle's own revision ids for the family-composition cycle refusal. Verification metadata is **not** advanced; the code commit does not exist yet and closeout owns that stamp.
- 2026-09-17T22:33:10+00:00: Generated citation repair: `KnowledgeRefusalCode` repointed to mcp/src/agents_remember/models/knowledge/result.py:95-160. No content impact: mechanical anchor-range projection bound to citation source snapshot 82f9228826d64da5e61d4da1a77adecab55752bad9f20116de62f870f7abd93f; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T11:30+02:00 — 260915-KS-L4 curator (uncommitted change set on `ar/260915-ks-l04`, base `76c7697c`): **recorded the seven factories the candidate lifecycle and publication boundary added, and corrected this card's reachability claim for `unsupported_schema`.** The new group is `selected_input_unavailable`, `candidate_binding_changed`, `candidate_snapshot_unpublished`, `snapshot_incomplete`, `destination_stale`, `publication_failed` and `publication_durability_unconfirmed`, one per observable failure point, and the card states the rule they share: none of them removes, replaces or repairs a database, a receipt or a published snapshot to make a later step succeed. Two of them carry distinctions a later reader must not flatten — `snapshot_incomplete` covers **both** the closed-snapshot freeze and a candidate's private-stage seal, because in both cases nothing outside the operation's own stage exists afterwards and the caller has one decision to make; and `publication_durability_unconfirmed` is the **honest** code for a replacement that completed but could not be re-read, which is neither a failure to claim nor a success to claim. The card also corrects the earlier statement that `unsupported_schema` "has no producer": it has no *factory* here, but since this leaf the publication gate and the candidate lifecycle produce it through the generic factory for a selected input that is not a database of this schema — a deliberate split, since this package's own open path still reports its own schema mismatches as `KnowledgeStorageError` defects. `no_change` remains a reservation with no producer, and the reachable `no_change` values are the *result state* and the *publication state*. Verification metadata remains empty until closeout stamps the code commit. The candidate-change operation composes the single-record operations, so its refusals are built here: two codes this leaf made reachable (`target_not_candidate` for a non-candidate lane, `promotion_not_supported` for accepted-origin data), the fail-closed `unauthorized_scope` refusal for a `task-candidate` lane whose resolved binding this operation cannot check, the two-digest context and stale-record refusals, the batch lineage restatement, and the two builders — `batch_refusal`, which relabels one command's refusal while **preserving** its code, record and remedy, and `batch_command_refusal`, whose `command` argument is the `"<index>:<kind>"` pair the caller needs. The card now states as a carried limitation that the refusal *code* `no_change` still has no producer and must not be branched on, while the *result state* `MutationResult.state == "no_change"` is the reachable vocabulary Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-16T10:10+02:00 — 260915-KS-L3 curator (uncommitted change set on `ar/260915-ks-l03`, base `27242ecb`): **recorded the batch-scoped refusal vocabulary and separated the result state from the refusal code.** The candidate-change operation composes the single-record operations, so its refusals are built here: two codes this leaf made reachable (`target_not_candidate` for a non-candidate lane, `promotion_not_supported` for accepted-origin data), the fail-closed `unauthorized_scope` refusal for a `task-candidate` lane whose resolved binding this operation cannot check, the two-digest context and stale-record refusals, the batch lineage restatement, and the two builders — `batch_refusal`, which relabels one command's refusal while **preserving** its code, record and remedy, and `batch_command_refusal`, whose `command` argument is the `"<index>:<kind>"` pair the caller needs. The card now states as a carried limitation that the refusal *code* `no_change` still has no producer and must not be branched on, while the *result state* `MutationResult.state == "no_change"` is the reachable vocabulary — the distinction the worker's earlier report got wrong on the report side and the handoff states correctly. Verification metadata remains closeout-owned.
- 2026-09-16T08:24+02:00 — 260915-KS-L2 curator (uncommitted change set on `ar/260915-ks-l02`, base `60e0820e`): **superseded the L1 account of the SQLite-error mapping and extended the vocabulary to the graph half.** The earlier card described `map_sqlite_error` as taking a bare record id; that signature hard-coded `operation="create_invariant_revision"` and the invariant tables for every caller, so a mapped failure from any other write reported the wrong operation and the wrong row. The card now records the `SqliteFailureContext` signature and the eleven caller-supplied contexts, the two cycle refusals sharing one wording helper so the two lineage graphs cannot describe different rules, the fourteen new relation factories with the code each emits, and the corrected reachability statement (`missing_expected_row` is now produced; `no_change` remains a result state rather than a refusal, and `unsupported_schema` still has no producer). Verification metadata remains empty until closeout stamps the code commit.
- 2026-09-15T22:40+02:00 — 260915-KS-L1 curator (uncommitted change set on `ar/260915-ks-l01`, base `67b21aeb`): created this one-to-one card for the new typed refusal vocabulary. It records that refusals are returned values, that the two cycle branches must be true in their own case, and that the trigger-message prefix is a shared contract with the SQLite-error mapping. The final wording of the descending branch is the round-3 review outcome for sealed finding `RV-4`. Verification metadata remains empty until closeout stamps the code commit.
