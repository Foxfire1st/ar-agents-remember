# mcp/src/agents_remember/memory/knowledge/diff.py

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
after_scope) -> DiffComparison` runs three steps:

1. **One `SideView` per side** — its connection, its `SelectedScope` and its claims keyed by claim
   identity, travelling together because a function handed them separately could be handed them
   crossed.
2. **The union** keyed by `(kind, stored identity)` — a revision id, a family revision id, a membership
   id, a claim id, or `family_revision_id::member_id` for an advertised frontier link (`::` joins the
   pair because neither component can contain it: both are UUIDs).
3. **The declared stream order** — the read stream's own kind order (`invariant`, `family`,
   `membership`, `realization`, `advertised_family`), and within a kind the same stable identity order
   the read uses, built only from stored identifiers.

**Nothing here writes.** Both connections are the caller's, opened read-only by the application seam,
and every statement this module adds is a `SELECT`.

### The record transition: four states, no succession

`_record_transition` returns four states. A record both sides hold is `changed` or `unchanged`; a
one-sided item is `added` or `removed`. A revised statement — the old revision only the baseline
holds and the new revision only the candidate holds — reads as a removal beside an unrelated
addition: text records hold no predecessor edge naming one as the other's replacement (MIK-R74
rule 1), so no succession the author did not record is ever stated.

### The coverage decision: two rules, and the measured reason they are not one

A one-sided item is covered by two ways of establishing that the other snapshot holds the record —
**not two independent deciders**, and the difference was measured rather than argued:

- the other side *selected* another exact revision of the same identity (`_selected_another_revision_of`,
  recognised by identity alone — never by which version looks newer). Load-bearing alone: removing it
  turns a missing selection into a real absence;
- the other side's *tables* hold the record, asked by this item's own key (`_recorded`). Load-bearing
  in the direction that forces its answer *present*: forcing present turns a genuinely deleted
  realization into a missing selection, while forcing absent changes no asserted state.

**Collapsing the two into one is wrong, and the reason is the reverse of what was first
claimed:** collapsing turns a *missing selection* into a *real absence*. A snapshot and a selection are different objects, which is
why the second rule cannot be replaced by the first — the probe asks the snapshot, and the first reads what the other side's *selection* already established. A claim and a frontier link never take the first route (`_REVISABLE_KINDS` is invariant and family only): a claim's identity is the claim, so they are never reported as present-but-unselected on that ground.

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The declared field projection: which `ReadItem` field carries each compared record field.** [1]
- **The five anchor fields an observation is compared on, with `detail` deliberately absent.** [2]
- The declared union stream order and the read-kind mapping, and the advertised-pair identity. [3]
- The per-side view and the pair of them as one value. [4]
- **One union item: both payloads, its coverage, its transition, its changed fields, its reachability and its source comparison.** [5]
- **The whole comparison value, including the four per-side selected sets a caller compares the union against.** [6]
- **The one entry point: the two sides, the union, the order and the aggregate counts.** [7]
- The union construction, its stable key, and the claims map the source half reads. [8]
- **The per-item comparison: coverage, projection, the record half and the source half.** [9]
- **The four record transitions, with no succession stated.** [10]
- **The coverage decision: the two rules and the measured reason they are not one.** [11]
- **The existence question each kind asks of the other snapshot, by its own key.** [12]
- The projection, the field comparison that runs only when both sides hold the record, and the claim's own two authored fields. [13]
- The content comparison and the anchor signature the source half is built on. [14]
- **The source comparison, the four booleans, and `missing_side` as the reason they are all false.** [15]
- The reachability labels and the declared stream order's implementation. [16]
- The existence probes this module consumes. [17]
- **The node that owns the union-side property the two rules serve, and the removed-realization node whose failing assertion is the load-bearing `assert 'unchanged' == 'removed'`.** [18]
- **The nodes that hold the two change statements apart and measure the record comparison field by field.** [19]
- The fixture's two snapshots and the transitions between them that this module's states are measured against. [20]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The two repositories a comparison names are
**code trees** the caller resolved, and this module reads neither of them: it compares two read-only
index connections the caller opened.

No meaningful cross-repo references found.
