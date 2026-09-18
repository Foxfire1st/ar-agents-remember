# mcp/src/agents_remember/memory/knowledge/diff.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/diff.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-17T03:15+02:00 |
| lastVerifiedCommitHash | `66f8b9f092eb6f63ec0c5c20d1b7b3e93d9a99be` |
| lastVerifiedCommitDate | 2026-09-18T08:36:40+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l08` uncommitted source; base `1ff1893f44d875073d58af863238501a6be35288` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The two-snapshot union: what the baseline selected, what the candidate selected, and how they
differ.** One claim owns the module, and the packet's hard parts are all consequences of it: **a
comparison is the union of two independently selected sets, with each item retaining the snapshot it
came from.** `compare_selected_scopes` is handed two already-selected scopes and reads nothing else from
either database except the existence questions the union's coverage needs.

## Code Commentary

### Logic

`compare_selected_scopes(before_connection, after_connection, repository_id, before_scope,
after_scope) -> DiffComparison` runs four steps:

1. **One `SideView` per side** — its connection, its `SelectedScope` and its claims keyed by claim
   identity, travelling together because a function handed them separately could be handed them
   crossed.
2. **One `SideLineage` per side** — `fetch_predecessor_edges` over that side's own connection, the
   authored `(successor, predecessor)` pairs the record transition is recognised from.
3. **The union** keyed by `(kind, stored identity)` — a revision id, a family revision id, a membership
   id, a claim id, or `family_revision_id::member_id` for an advertised frontier link (`::` joins the
   pair because neither component can contain it: both are UUIDs).
4. **The declared stream order** — the read stream's own kind order (`invariant`, `family`,
   `membership`, `realization`, `advertised_family`), and within a kind the same stable identity order
   the read uses, built only from stored identifiers.

**Nothing here writes.** Both connections are the caller's, opened read-only by the application seam,
and every statement this module adds is a `SELECT`.

### The record transition, and why it is read from the authored edge

`_record_transition` returns six states. A record both sides hold is `changed` or `unchanged`; a
one-sided item of a **non-supersedable** kind (a claim, an advertised link) is `added` or `removed`.
For the two supersedable kinds (invariant, family revisions) a one-sided item is resolved through the
authored predecessor edge:

- the candidate's own edges name the exact revision it replaced, and **whether the baseline selected
  that revision** decides between `superseding` and `added`;
- a baseline-only revision whose replacement the candidate's edges name is `superseded`, otherwise
  `removed`.

No display version, no label and no insertion order participates, because none of them is a statement
the author made about which revision replaced which. `_replaced_revision` returns the first **sorted**
match among several named predecessors, so the choice is the same on every run.

### The coverage decision: three rules, and the measured reason they are not one

This is the leaf's most-corrected contract, and the direction of each rule was **measured, not argued**
(fix round 2's ablations, on the frozen bytes):

| Rule | The question | What the measurement shows |
| --- | --- | --- |
| **1** | did the other side *select* another exact revision of this record identity? | **Load-bearing alone.** Removing it alone turns a missing selection into a real absence (`absent_from_snapshot` where `present_outside_selection` is owed — variant `A`, two assertion kills) |
| **2** | do the other side's *authored predecessor edges* name this exact revision? | **Cannot decide a state its neighbours do not.** Whenever it fires, rule 3 fires as well, because an authored edge is a foreign key into that snapshot's own revision table (both predecessor tables are `DEFERRABLE INITIALLY DEFERRED` into their own revision table and a dangling edge is refused at COMMIT with `ConstraintError`, measured). It is kept as a **cheap short-circuit over already-loaded lineage** rather than deleted |
| **3** | do the other snapshot's *own tables* hold this record, asked by this item's own key? | **Load-bearing in the direction that forces its answer *present*.** Forcing it present turns a genuinely deleted realization into a missing selection (`present_outside_selection` where `absent_from_snapshot` is owed — variant `C'`, two kills, and `M24` kills the same node by forcing the realization probe true). Forcing it **absent** changes no asserted state on this population (`C`: all 28 nodes survive), because the three items whose absence-answer it gives are all really absent |

**Collapsing the three into one is wrong, and the reason is the reverse of what this leaf first
claimed:** collapsing turns a *missing selection* into a *real absence*. The earlier claim that it
turned a real deletion into a missed selection was **not measured and is withdrawn**; the source
comment now carries the measured direction. A snapshot and a selection are different objects, which is
why the third rule cannot be replaced by the other two — the probe asks the snapshot, and the first two
read what the other side's *selection* already established.

**The one honest gap inside the rule-2 subsumption.** The invariant half of the subsumption **is
asserted**, by `test_a_record_the_other_snapshot_holds_but_the_selection_missed_is_not_an_absence`
through the published read surface (`fetch_predecessor_edges` + the per-table probes), and the case is
split **by table** — each predecessor table asked with its own probe, with the union identity asserted
back against `fetch_predecessor_edges`, because `fetch_predecessor_edges` unions both tables and asking
the invariant probe about a *family* endpoint was a false alarm on a legal snapshot (measured: one
schema-valid family edge made the pre-fix form fail at `:474`). **The family half is unexercised**: the
fixture authors **0 `family_predecessor` rows** (measured census 2 invariant / 0 family before, 4 / 0
after), so the family half rests on the same schema constraint and **not** on that case. That is a
stated gap, not coverage, and adding a family edge to the shared fixture is carried as fixture debt.

### The two change statements, and the source half

`_source_change` builds one claim's typed comparison. Each boolean is a statement about a different
object: `record_field_changed` about the claim's **authored fields** (role, rationale — compared
directly rather than through `FIELD_PROJECTION`, because a claim's substantive difference *is* its
words), `source_observation_changed` about the **anchor observation**, and the two `*_change_only` flags
about which of the two moved while the other did not. A claim only one snapshot holds has **no second
observation**, so nothing about its source *moved*: all four booleans are false and `missing_side` names
the absent side, while the absent side's own observation is still carried so the earlier code stays
inspectable.

`_changed_fields` compares the nine declared field names and compares a field **only when both sides
hold the record**: a record one snapshot holds is reported by its `coverage`, and reporting all nine of
its fields as "changed" would state nine differences where there is one absence.

### Conventions

- `_comparable` normalises a projected value (mappings to sorted key/value tuples, sequences elementwise)
  so two sides compare **by content rather than by identity**.
- `_KIND_BY_READ_ITEM` maps the read's item kinds onto this module's five union kinds; a read kind with
  no mapping is a defect at the call site rather than a silent sixth union kind.
- `DiffItemComparison` keeps `before_projection`/`after_projection` so the typed layer can render each
  changed field's before and after text without re-deriving which fields changed.

### Invariants And Boundaries

- **The union is built from the two selected sets and never from a walk of the candidate.** That is why
  deleting a realization link on the candidate cannot make the baseline's code disappear from the
  comparison — the requirement's own non-conforming example.
- **No relevance is re-decided here.** The module is handed two selected sets; a second selection rule
  is *absent* rather than merely discouraged. See `memory/knowledge/read.py`'s `SelectionQuery` for the
  one policy owner.
- **The known limits, stated rather than implied** (the leaf's own mutation taxonomy, all on this
  module's lines): **`M4`** — `_record_transition`'s `changed`/`unchanged` branch is a **covered gap**
  against this leaf, because this fixture's same-id memberships project equal fields; its closer is a
  same-id `membership` re-provenanced under the same `member_id` in the candidate (a real two-database
  pair produced `changed` + `('provenance',)` intact versus `unchanged` mutated). **`M8`** — the
  existence probe's own mutation *is* variant `C`: the line is reachable (`_recorded` is called **3**
  times by one comparison, all three already answering `False`), so only its *differing* answer is
  unobserved; closer: a one-sided record of a non-supersedable kind that the other snapshot holds
  outside its selection. **`M27`** — `record_change_only` is `True` for **0** of the 22 union items, so
  the boolean's true half is unasserted; closer: a same-id pair whose record moved while its observation
  did not. **`M23`** — `invariant_revision_is_recorded` is called **0** times on this population: that is
  a **non-experiment**, and its reachability bound is carried rather than resolved.
- **Two equivalent mutants are disclosed as equivalences rather than counted as kills.** `M9`
  (`_project`'s narrowing) is unobservable through the public API because `_changed_fields` iterates the
  nine declared names and both sides' key sets are identical (17/17 same-id pairs, 0 differing); it is
  kept so a `ReadItem` field rename has one place to be reflected, so **do not delete it as dead code
  without deciding what happens to `FIELD_PROJECTION`**. `M12` (`_anchor_signature`) is equivalent
  because the two anchors' signatures differ in `observed_source_identity` *and* `resolution`, so
  dropping the first still moves the signature — proved by an identity-free fact multiset over all 22
  union items being identical intact versus mutant. `M21` (`app:319 _binding`) is equivalent on this
  population because the substituted context is refused by the per-side digest verification the mutation
  leaves in place.
- **Boundary.** This module compares. It does not select, does not open a connection, does not resolve
  a source anchor, does not build the display, does not page, and writes nothing.

### Todos

None recorded. The four carried limits above (three covered gaps and one non-experiment) are recorded
here so a successor does not read the comparison as fully covered; they are evidence debt with named
closers, not behavioural defects. The leaf's contested evidence items were carried to `KS-R09`/`L9`
(ledger entries **A9**/**A10**).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The declared field projection: which `ReadItem` field carries each compared record field.** | `FIELD_PROJECTION` | mcp/src/agents_remember/memory/knowledge/diff.py:66-76 |
| **The five anchor fields an observation is compared on, with `detail` deliberately absent.** | `_ANCHOR_FIELDS` | mcp/src/agents_remember/memory/knowledge/diff.py:82-88 |
| The declared union stream order and the read-kind mapping, and the advertised-pair identity. | `_KIND_ORDER`; `_KIND_BY_READ_ITEM`; `ADVERTISED_ID_SEPARATOR`; `advertised_item_id` | mcp/src/agents_remember/memory/knowledge/diff.py:93-117 |
| The per-side view, the per-side lineage and the pair of them as one value. | `SideView`; `SideLineage`; `ComparisonView` | mcp/src/agents_remember/memory/knowledge/diff.py:121-149 |
| **One union item: both payloads, its coverage, its transition, its changed fields, its reachability and its source comparison.** | `DiffItemComparison` | mcp/src/agents_remember/memory/knowledge/diff.py:153-172 |
| **The whole comparison value, including the four per-side selected sets a caller compares the union against.** | `DiffComparison` | mcp/src/agents_remember/memory/knowledge/diff.py:176-197 |
| **The one entry point: the two sides, the two lines, the union, the order and the aggregate counts.** | `compare_selected_scopes` | mcp/src/agents_remember/memory/knowledge/diff.py:200-264 |
| The union construction, its stable key, and the claims map the source half reads. | `_union_items`; `_union_key`; `_claims_by_id` | mcp/src/agents_remember/memory/knowledge/diff.py:267-306 |
| **The per-item comparison: coverage, projection, the record half and the source half.** | `_compare_one` | mcp/src/agents_remember/memory/knowledge/diff.py:309-357 |
| **The six record transitions, recognised from the authored predecessor edge and from nothing else.** | `_record_transition`; `_SUPERSEDABLE_KINDS`; `_replaced_revision`; `_supersedes`; `_selected` | mcp/src/agents_remember/memory/knowledge/diff.py:360-457 |
| **The coverage decision: the three rules, the direction each was measured in, and the family-half caveat.** | `_coverage` | mcp/src/agents_remember/memory/knowledge/diff.py:460-522 |
| **The existence question each kind asks of the other snapshot, by its own key.** | `_recorded` | mcp/src/agents_remember/memory/knowledge/diff.py:525-544 |
| The projection, the field comparison that runs only when both sides hold the record, and the claim's own two authored fields. | `_project`; `_changed_fields`; `_claim_changed_fields` | mcp/src/agents_remember/memory/knowledge/diff.py:547-593 |
| The content comparison and the anchor signature the source half is built on. | `_comparable`; `_anchor_signature` | mcp/src/agents_remember/memory/knowledge/diff.py:596-612 |
| **The source comparison, the four booleans, and `missing_side` as the reason they are all false.** | `_source_change` | mcp/src/agents_remember/memory/knowledge/diff.py:615-656 |
| The reachability labels and the declared stream order's implementation. | `_reached_via`; `_ordered`; `_first_present` | mcp/src/agents_remember/memory/knowledge/diff.py:659-686 |
| The existence probes and the predecessor-edge union this module consumes. | `invariant_revision_is_recorded`; `family_revision_is_recorded`; `membership_is_recorded`; `realization_claim_is_recorded`; `fetch_predecessor_edges` | mcp/src/agents_remember/memory/knowledge/read_queries.py:311-320; mcp/src/agents_remember/memory/knowledge/read_queries.py:323-332; mcp/src/agents_remember/memory/knowledge/read_queries.py:335-342; mcp/src/agents_remember/memory/knowledge/read_queries.py:478-491; mcp/src/agents_remember/memory/knowledge/read_queries.py:455-475 |
| **The node that owns the union-side property the two rules serve, and the removed-realization node whose failing assertion is the load-bearing `assert 'unchanged' == 'removed'`.** | "test_a_record_the_other_snapshot_holds_but_the_selection_missed_is_not_an_absence"; "test_a_realization_the_candidate_removed_keeps_its_baseline_source_in_the_union" | mcp/tests/test_knowledge_diff_scope.py:424-530; mcp/tests/test_knowledge_diff_scope.py:309-342 |
| **The nodes that hold the two change statements apart and measure the record comparison field by field.** | "test_the_two_change_statements_are_separate_fields_and_neither_implies_the_other"; "test_the_record_comparison_reports_exactly_the_payload_field_that_changed"; "test_a_source_only_change_is_reported_as_a_source_observation_and_no_record_field_changed" | mcp/tests/test_knowledge_diff_boundaries.py:510-540; mcp/tests/test_knowledge_diff_boundaries.py:543-597; mcp/tests/test_knowledge_diff_scope.py:177-219 |
| The fixture's two snapshots and the transitions between them that this module's states are measured against. | `build_diff_fixture`; `DiffFixture` | mcp/tests/diff_scope_test_support.py:189-233; mcp/tests/diff_scope_test_support.py:148-186 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The two repositories a comparison names are
**code trees** the caller resolved, and this module reads neither of them: it compares two database
connections the caller opened.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-17T03:15+02:00 — 260915-KS-L8 curator (uncommitted change set on `ar/260915-ks-l08`, base `1ff1893f`): created this one-to-one card for the two-snapshot union. It states the module's single claim — **the comparison is the union of two independently selected sets with each item retaining its snapshot** — and the four steps that build it, then documents the two contracts review corrected most. **The coverage rules are recorded with the measured direction of each rather than as three equal deciders:** rule 1 is load-bearing alone (variant `A`, two assertion kills); rule 2 cannot decide a state its neighbours do not, because an authored edge is a foreign key into the snapshot that declares it, so it is kept as a cheap short-circuit and its **invariant half is asserted while its family half is unexercised** (the fixture authors 0 `family_predecessor` rows — a stated gap, not coverage); and rule 3 is load-bearing in the **forced-present** direction (`C'`, two kills, plus `M24`), while forcing its answer absent changes no asserted state on this population (`C`, 28/28 survivors). The card records that collapsing the three is wrong because it **turns a missing selection into a real absence**, and that the leaf's first statement of that reason was the reverse and is withdrawn. It also records the four carried limits with their named closers (`M4`, `M8`, `M27` covered gaps; `M23` a non-experiment with its bound carried), the three equivalent mutants as **proved equivalences rather than kills** (including the instruction not to delete `_project`'s narrowing without deciding `FIELD_PROJECTION`'s fate), and the source half's `missing_side` semantics. Verification metadata: lastUpdated advanced, the reviewed candidate moved to `ar/260915-ks-l08`, and the commit fields left at the last real commit because the code commit does not exist and closeout owns the stamp.
