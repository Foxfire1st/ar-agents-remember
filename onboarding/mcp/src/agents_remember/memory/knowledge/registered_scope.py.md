# mcp/src/agents_remember/memory/knowledge/registered_scope.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/registered_scope.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-18T14:02+02:00 |
| lastVerifiedCommitHash |  `9f88a6de572dc15bbed1802cf08b77c1193fb24c`|
| lastVerifiedCommitDate |  2026-09-18T14:21:49+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l16` uncommitted staged source; base `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

The construction act itself: how one `RegisteredScopeRequest` plus the datasets that actually hold its
declared snapshots become a `RegisteredScopeManifest` or **one** `ScopeConstructionRefusal` naming the
exact input that blocked it. **This module owns the decision order, the lookups and the refusals; it owns
no vocabulary** — every record it returns and every field it fills is a shape the models half declares,
`mcp/src/agents_remember/models/knowledge/registered_scope.py`, the typed refusals are the shipped ones,
and the declared traversal is `KS-R17@v1`'s own call. What a *run over* the scope could not resolve is
`KS-R14@v1`'s half of the split and is deliberately absent here.

## Code Commentary

### Logic

**The construction runs the four declared steps, and each one either resolves or refuses.** The entry
point, `construct_registered_scope`, performs step 1 through `_resolve_sources`, then checks the declared
seeds through `_first_unrecorded_seed`, then runs `_assemble` — steps 2 to 4 — under a `KnowledgeRefused`
guard. **Nothing is raised out of the function**: each failure becomes a
`RegisteredScopeResult(state="refused", …)` carrying the refusal, and `constructed()` is the one
predicate a caller needs. The module docstring's determinism claim is implemented rather than asserted —
every membership tuple and the whole edge list are sorted by recorded identity, so the same declaration
over the same snapshots under the same construction version yields the same scope whatever order rows
came back in.

**Step 1 compares a declaration against bytes, not against a description.** `snapshot_source` reads one
dataset's identity through `dataset_identity`, which opens the file read-only and validates the bound
namespace, and returns a `ScopeSnapshotSource` that keeps the identity beside the handle — so a caller
cannot declare one snapshot and hand over another. `_resolve_sources` builds the supplied map with
`setdefault`, which means **the first supplied handle for a side is the one considered** and a handle for
a side the declaration never names is never consulted; for each declared side it then compares the
handed-over `SnapshotIdentity` and refuses a mismatch, naming the declared logical digest and reporting
the observed digest and schema version in the detail, or refuses a side for which no dataset was
supplied at all. Both go through `_missing_snapshot` with kind `declared_snapshot`, and its detail states
the three things the construction will not do instead: fall back to another dataset, infer membership
from paths, or proceed with a partial scope.

**The seed check refuses a seed no declared snapshot records, instead of dropping it.**
`_first_unrecorded_seed` walks the *sorted* declared seed identities and asks every resolved store whether
that family revision is recorded, returning the first one none of them holds — a deterministic first
offender rather than whichever side happened to be checked last. That seed becomes the `missing_input` of
`_seed_refusal` (kind `seed_family_revision`), whose detail says the traversal has no starting point and
whose next action is to declare a recorded seed or remove it. Dropping the seed and reporting a smaller
scope as the declared one is the outcome this refusal exists to prevent.

**Steps 2 and 3 follow only recorded rows, and each edge keeps the side it was read from.**
`_follow_recorded_links` visits the sides in `_VISIT_ORDER` (`base`, then `candidate`) and, for each, runs
`_follow_changed_paths` over the sorted declared paths. The path lookup is `fetch_realizations_at_path`,
which matches the stored anchor's path by exact equality and matches nothing else, and every returned
claim becomes one `source_to_invariant` `FollowedScopeEdge` carrying `mapping_side` — so the same path on
both sides yields two edges that differ in their provenance, which is the historical-lookup union made
visible. `_collect_claim` also collects the claim's three identities and appends the origin references
the row's own provenance declares. `_follow_memberships` then reads the family memberships of exactly the
revisions *that side* reached and records one `invariant_to_family` edge per returned row, keyed by the
membership row's own identity. No name, prefix, folder or symbol is read anywhere in this path.

**Step 4 calls the declared traversal rather than walking again.** `_follow_composition` runs only when
the declaration names both halves of a policy identity, and its targets are the declared seeds unioned
with the family revisions the recorded links reached, sorted — so a family the changed paths joined is
traversed from as well, still gated on the declared policy. Each target gets exactly one
`follow_composition_scope` call, and **its refusals propagate unchanged**: an unknown policy version, an
edge the policy does not admit and a step past the declared bound stay `KS-R17@v1`'s facts, caught once
by the entry point and wrapped by `_traversal_refusal`, which keeps the inner refusal's code, facts and
next action and adds only the sentence that no scope was constructed. The resolved identity the traversal
returns is what the manifest records. When a policy is declared but nothing was reached to follow, the
scope must still record what it was built under, so `_declared_policy_identity` resolves the declared
version from the same registry the traversal reads and raises the shipped composition-policy refusal when
nobody declared it — never an identity this code spelled itself. `_traversal_source` hands the traversal
the candidate side's dataset when there is one and the base side's otherwise, and that same side becomes
the provenance of every edge the traversal produced, so the two facts cannot disagree.

**The manifest is assembled sorted, deduplicated and complete.** `_assemble` carries the declared
snapshots through, sorts the declared changed paths, wraps the five membership channels as sorted tuples
and orders the collected edges through `_ordered`, which collapses duplicates by value over the immutable
edge records and sorts by `(edge_kind, mapping_side, edge_id, from_record_id, to_record_id)`. The
membership is a required field of the manifest, so a constructed scope always carries the membership it
resolved. `_Collected` is the accumulator: the edge list plus five sets, which is the entire mutable
state one construction keeps while it runs.

**The refusals are the module's own vocabulary of what to do next.** `_seed_refusal` and
`_policy_refusal` name a missing input directly, `_traversal_refusal` wraps a traversal refusal, and all
three are built by `_refusal`, which constructs the shipped `invalid_reference` refusal with
`RefusalFacts(record_id=…, expected=…, observed=…)` and then deletes the request it was handed — the
refusal's facts come from the named input, never from the declaration. `CONSTRUCT_SCOPE_OPERATION` is the
one operation name carried, and the module states its own boundary in the same breath: **no refusal
*code* is added by this leaf anywhere, and the members of the shipped code vocabulary are unchanged**,
because constructing the scope is not a retrieval selection and not a variant of the traversal — it
*calls* that traversal. `_policy_refusal` is reachable only from a branch the loop cannot produce, and
`_composition_endpoints` reports a followed row the store no longer holds the same way: both branches are
marked `# pragma: no cover` rather than left as untested surprises.

### Conventions

The memory half **imports the frozen vocabulary and redeclares no field of it**: the request, the
manifest, the membership, the edge, the side's declaration, the refusal wrapper and both side/kind
literals all come from the models module, and the two helper types declared here — `ScopeSnapshotSource`
and `RegisteredScopeResult` — are frozen dataclasses rather than pydantic models: one carries a live store
handle and the other a two-state outcome, so neither is a stored record.

Every reusable step is the shipped one: `dataset_identity` for identity read from a file,
`follow_composition_scope` for the declared traversal, `get_policy_version` for the policy registry, the
three `read_queries` readers for the recorded rows, and `refusal`/`RefusalFacts`/`KnowledgeRefused` for
the typed refusals. The public surface is exactly `__all__` — `CONSTRUCT_SCOPE_OPERATION`,
`RegisteredScopeResult`, `ScopeSnapshotSource`, `construct_registered_scope`, `snapshot_source` — with
every helper private and prefixed, and the sections of the file are separated by banner comments naming
which step follows. The read-only dataset handle comes in as `OpenedKnowledgeStore`; nothing here opens,
writes or closes a store.

The determinism claim is a property of the code's spelling rather than a comment: the sides are visited
in a declared tuple order, the paths, seeds, targets, membership channels and edges are all sorted at the
point they are consumed, and the accumulator is a set precisely so duplicate contributions from two
sides or two seeds collapse into one member.

### Invariants And Boundaries

- **The retrieval read is not consulted.** No import from `mcp/src/agents_remember/memory/knowledge/read.py`
  appears: this module reads recorded rows through `read_queries`, so the R07 frontier — a selection, a
  count, an advertised expansion — has no path into a construction.
- **A refusal is returned, never raised, and never replaced by a smaller scope.** `construct_registered_scope`
  catches its one internal control-flow exception and returns one outcome carrying either the manifest or
  one refusal; there is no state in which a caller receives a scope holding less than its declaration.
- **Every followed edge names the side whose selection produced it.** The side is set by the walk that
  read the row, and the composition edges are attributed to the same side the traversal ran against.
- **The traversal's refusals keep their own identity.** The wrapper changes the operation's framing and
  adds nothing to the inner code, facts or next action; re-wording another module's refusal is not this
  module's work.
- **A given dataset is compared, not trusted.** The declaration is checked against the identity read from
  the file's bytes, and the first supplied handle per side is the one compared; a surplus handle is
  ignored rather than treated as an error.
- **Ordering is by recorded identity.** Membership tuples and the edge list are sorted, the edge set is
  deduplicated by value, and the sides are visited in `_VISIT_ORDER`, so row/dict iteration order cannot
  change the constructed scope.
- **A policy is recorded even when it was never walked.** A declared policy is resolved from the registry
  when the recorded links reached no family revision, so the manifest never reports a scope whose
  construction policy is unknown.
- **No schema is written and no identity is minted.** This module opens no transaction, adds no table and
  produces no digest or content address of its own; the scope is addressed by the declared `scope_id`.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one operation name a construction refusal carries, its own member of the shipped operation vocabulary, and the statement that no refusal code is added. | `CONSTRUCT_SCOPE_OPERATION`; `KnowledgeRefusalCode`; "def construct_registered_scope(" | mcp/src/agents_remember/memory/knowledge/registered_scope.py:76-81; mcp/src/agents_remember/models/knowledge/result.py:151-151; mcp/src/agents_remember/memory/knowledge/registered_scope.py:130-130 |
| The declared side's dataset as identity plus handle, and the two-state outcome whose `constructed()` is the one predicate. | `ScopeSnapshotSource`; `RegisteredScopeResult`; `constructed` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:88-99; mcp/src/agents_remember/memory/knowledge/registered_scope.py:102-110; mcp/src/agents_remember/memory/knowledge/registered_scope.py:111-114 |
| The identity read from the file's own bytes, read-only and namespace-validated, rather than from a claim. | `snapshot_source`; "return ScopeSnapshotSource(side=side, snapshot=dataset_identity(database_path), store=store)" | mcp/src/agents_remember/memory/knowledge/registered_scope.py:117-127; mcp/src/agents_remember/memory/knowledge/logical.py:153-176 |
| The construction entry point: resolve, check seeds, assemble — returning a refusal instead of raising, and the caller that consumes it. | `construct_registered_scope` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:130-161; mcp/src/agents_remember/application/knowledge_family_integrity.py:177-180 |
| Step 1: every declared side resolved to the dataset that holds it, with the first supplied handle per side winning and a mismatch refused by name. | `_resolve_sources`; `setdefault`; `_missing_snapshot` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:168-190; mcp/src/agents_remember/memory/knowledge/registered_scope.py:193-214 |
| The seed check: the first declared seed no declared snapshot records, looked up through the store reader. | `_first_unrecorded_seed`; "family_revision_is_recorded(source.store.connection, source.store.repository_id, seed)" | mcp/src/agents_remember/memory/knowledge/registered_scope.py:217-230; mcp/src/agents_remember/memory/knowledge/read_queries.py:329-338 |
| The assembly — declared paths sorted, the policy identity carried, the edges ordered — and the accumulator that is the whole of one construction's mutable state. | `_assemble`; `_Collected` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:237-265; mcp/src/agents_remember/memory/knowledge/registered_scope.py:268-277 |
| The recorded-links walk that visits each side in a declared order, and the order itself. | `_follow_recorded_links`; `_VISIT_ORDER` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:280-299; mcp/src/agents_remember/memory/knowledge/registered_scope.py:83-85 |
| Steps 2 and 3: the exact-equality path lookup, the `source_to_invariant` edge per claim with its provenance side, and the family memberships of the revisions that side reached. | `_follow_changed_paths`; `_collect_claim`; `_follow_memberships` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:302-316; mcp/src/agents_remember/memory/knowledge/registered_scope.py:319-339; mcp/src/agents_remember/memory/knowledge/registered_scope.py:342-363 |
| The two shipped readers the recorded lookups are performed through. | `fetch_realizations_at_path`; `fetch_memberships_of_invariants` | mcp/src/agents_remember/memory/knowledge/read_queries.py:226-261; mcp/src/agents_remember/memory/knowledge/read_queries.py:210-223 |
| Step 4: the declared traversal called once per target under the declared policy, and the `KS-R17@v1` scope and entry point it calls rather than re-implements. | `_follow_composition`; "scope: CompositionScope = follow_composition_scope("; "scope: CompositionScope = follow_composition_scope(" | mcp/src/agents_remember/memory/knowledge/registered_scope.py:366-398; mcp/src/agents_remember/memory/knowledge/composition_traversal.py:63-81; mcp/src/agents_remember/memory/knowledge/composition_traversal.py:84-184 |
| A declared policy resolved from the registry when nothing was reached to follow, and the shipped policy refusal raised when no version declares it. | `_declared_policy_identity`; "declared = get_policy_version(store, str(request.policy_id), str(request.policy_version_id))"; `composition_policy_refusal` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:401-426; mcp/src/agents_remember/memory/knowledge/composition_policies.py:162-183; mcp/src/agents_remember/memory/knowledge/refusals.py:1252-1286 |
| The composition edges recorded from the traversal's own reported identities, the endpoints read back from the row, and the candidate-preferred side the traversal runs against. | `_collect_composition_edges`; `_composition_endpoints`; `_traversal_source` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:429-451; mcp/src/agents_remember/memory/knowledge/registered_scope.py:454-467; mcp/src/agents_remember/memory/knowledge/registered_scope.py:470-486 |
| The deterministic edge order with duplicates collapsed, and the origin references read from a row's own provenance rather than inferred. | `_ordered`; `_origin_refs`; "origin_refs: tuple[str, ...] = ()" | mcp/src/agents_remember/memory/knowledge/registered_scope.py:489-503; mcp/src/agents_remember/memory/knowledge/registered_scope.py:506-522; mcp/src/agents_remember/models/knowledge/authorship.py:48-48 |
| The three named refusals a construction can return, each naming the exact missing input. | `_seed_refusal`; `_policy_refusal`; `_traversal_refusal` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:529-541; mcp/src/agents_remember/memory/knowledge/registered_scope.py:544-556; mcp/src/agents_remember/memory/knowledge/registered_scope.py:559-574 |
| The shared refusal builder and the shipped refusal machinery it reuses instead of adding a code. | `_refusal`; `KnowledgeRefused`; `RefusalFacts`; `refusal` | mcp/src/agents_remember/memory/knowledge/registered_scope.py:577-604; mcp/src/agents_remember/memory/knowledge/refusals.py:35-45; mcp/src/agents_remember/memory/knowledge/refusals.py:47-54; mcp/src/agents_remember/memory/knowledge/refusals.py:57-77 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. A construction reads one namespace's own
stored rows through its own opened dataset, and every identity it records — snapshots, revisions,
memberships, policy versions — is store-local.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T14:02+02:00 — 260915-KS-L16 curator (uncommitted change set on `ar/260915-ks-l16`, base `7b1db4e0`): created this one-to-one card for the registered review scope's construction act. It records the four-step decision order and that each step resolves or refuses, the declaration-compared-against-bytes rule with the first-handle-per-side behaviour, the sorted-and-deduplicated assembly that makes the scope a function of its declaration, the single call into `KS-R17@v1`'s traversal whose refusals propagate unchanged, and the deliberate absences (no retrieval-frontier import, no partial scope, no inferred member, no new refusal code, no store write). This card carries **no `lastVerifiedCommitHash`**: every construct it cites exists only in this leaf's uncommitted candidate, so no real commit contains the content a stamp would claim to have verified. The `reviewedWorkingCandidate` row states what was actually read, and closeout owns the stamp once the code commit exists.
