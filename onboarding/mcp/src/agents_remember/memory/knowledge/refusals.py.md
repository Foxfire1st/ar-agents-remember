# mcp/src/agents_remember/memory/knowledge/refusals.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- The defect-report exception versus the internal control-flow exception. [1]
- The facts bundle and the one generic factory every refusal is built through. [2]
- The two-branch cycle refusal whose text must be true in both directions, and the family sibling that shares its wording. [3]
- The family, anchor and relation factories added with the graph half, one per failure. [4]
- The batch-scoped factories, including the two codes this leaf made reachable and the fail-closed task-lane refusal. [5]
- The relabelling factory that preserves a command's own code, record and remedy while naming the batch. [6]
- The builder whose `command` argument carries both the failing position and its kind. [7]
- The context and stale-record refusals that name both digests. [8]
- The write-path rule the descending branch describes, and its post-insert graph scope, now owned by the shared lineage module. [9]
- The SQLite-error mapping, its caller-supplied failure context, and the trigger-message prefix that steers it. [10]
- **The candidate-lifecycle and publication group this leaf added: one factory per observable failure point.** [11]
- **The destination and install failures, including the honest durability code.** [12]
- The trigger messages the mapping depends on. [13]
- The refusal codes these factories must stay within, now including the batch codes and the seven this leaf added. [14]
- The operation that produces the batch codes, and the alias that keeps the earlier lane-check name working. [15]
- The two nodes that reach the batch lane refusals on a real store. [16]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
