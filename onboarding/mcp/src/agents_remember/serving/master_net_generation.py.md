# mcp/src/agents_remember/serving/master_net_generation.py

## Governing Overview

[serving overview](overview.md)

## Purpose

`master_net_generation.py` is the **master-net selection owner** for `ICR-R13@v1` (260921-ICR-L13):
which exact Git objects one master NET change-set binds, and what to say when one is absent.
It owns the *selection* the net-diff computation runs over — the declared integrated result for
a live request, or the exact recorded endpoints a pinned request names — while the diff itself
stays where it is (`serving/changeset.py`'s `base -> tip` diff over
`worktrees/modules/git.changed_files_with_counts`). It is the new sibling beside
`serving/changeset.py` that the packet's Scope authorizes ("new internal modules belong beside
those owners"), holding the logic moved out of `changeset.py`'s deleted `_master_task_root`,
`_load_master_contract`, `_series_tip` and `_net_changed`.

## Code Commentary

### Logic

Three request states, one scope. `MASTER_NET_SCOPE` is the literal `"integrated"`:
the active master net is the declared integrated result, and any in-flight preview travels
under its own label elsewhere, never silently inside it. cit:([`MASTER_NET_SCOPE`], mcp/src/agents_remember/serving/master_net_generation.py:67-67)

- **Live (no pins).** The selection is the series contract's recorded base plus the live head
  of its integration branch, for code and for memory. Per-leaf liveness rides beside the net
  on the breakdown rows (`serving/changeset.py`'s `_leaf_state`), never mixed into it.
- **Pinned.** The caller names the generation a listing published (`MasterNetPins`: exact
  commits, never branch names; empty means unpinned). Both endpoints must resolve in their
  repository or the read is refused by name — a completed master's URL keeps working after
  its source branch advances because the recorded endpoints still resolve. cit:([`MasterNetPins`], mcp/src/agents_remember/serving/master_net_generation.py:86-97)
- **Absent.** A missing endpoint is never substituted with a later branch tip: no
  source-branch fallback, no worktree `HEAD`, no current knowledge. The code side — the side
  the view *is* — raises `MasterEndpointAbsent`; the memory side degrades to nothing to show.
  cit:([`MasterEndpointAbsent`], mcp/src/agents_remember/serving/master_net_generation.py:73-81)

`select_master_net` returns `None` for an unknown master (no series contract — the caller
keeps degrading that to empty lists rather than refusing it) and raises `MasterEndpointAbsent`
when the contract exists but the code side has no resolvable base or result. cit:([`select_master_net`], mcp/src/agents_remember/serving/master_net_generation.py:171-200)
`integrated_tip` is the live head of the integration branch or `None` — deliberately with no
fallback to the source branch, whose later tip is other work and must never be labelled this
master's net. cit:([`integrated_tip`], mcp/src/agents_remember/serving/master_net_generation.py:142-155)
`master_net_digest` is the deterministic content id over the four endpoint commits (no wall
clock, no branch names), so two selections of the same generation share one id. cit:([`master_net_digest`], mcp/src/agents_remember/serving/master_net_generation.py:158-168)

The two halves resolve independently. `_code_endpoints` requires both base and tip and
refuses a missing pair with kind `not-recorded`; `_memory_endpoints` returns `None` (no
memory half shown) for an absent leg on an unpinned request, and refuses an explicit memory
pin that does not resolve. cit:([`_code_endpoints`], mcp/src/agents_remember/serving/master_net_generation.py:203-226) cit:([`_memory_endpoints`], mcp/src/agents_remember/serving/master_net_generation.py:229-255)
`_require_resolves` checks both commits with `git cat-file -e` (`_resolves`) and refuses
with `no-repository` (the contract names no repository for that side) or `unresolvable`
(a recorded commit this checkout does not hold). cit:([`_require_resolves`], mcp/src/agents_remember/serving/master_net_generation.py:258-272)
`_currentness` compares the selection against the live integrated tips measured in the same
call: `current`, `superseded`, or `unmeasured` (no live line to compare against — an unknown
master, or a live tip that is gone). cit:([`_currentness`], mcp/src/agents_remember/serving/master_net_generation.py:281-295)

`MasterEndpointAbsent` subclasses the committed-range refusal (`RecordedEndpointAbsent` from
`serving/changeset_endpoints.py`) because it *is* the same vocabulary — the same 404 idiom
on the routes, the same three kinds a caller acts on — applied to the master's declared base
and selected result rather than to one leaf's landed range. Only `NOT_RECORDED` may leave a
half with nothing to show, and only on the memory side.

### Conventions

Purpose-named adjacent module: master task-root/contract loading (`master_task_root`,
`load_master_contract`), tip resolution without fallback, pins/endpoints/selection
dataclasses, deterministic digest, one selector. cit:([`master_task_root`], mcp/src/agents_remember/serving/master_net_generation.py:120-125) cit:([`load_master_contract`], mcp/src/agents_remember/serving/master_net_generation.py:128-139)
The diff primitive stays in `changeset.py` — one implementation, no duplication. Refusal
messages name the endpoint and the substitution that was refused, so the caller can act on
the kind.

### Invariants And Boundaries

- **The net is exact when served, refusal when unreadable.** `_net_diff` (in
  `serving/changeset.py`) degrades to `[]` ONLY for an empty endpoint pair — a degraded leg
  with nothing selected. A diff that fails *after* endpoint validation raises
  `MasterEndpointAbsent(kind="unresolvable")` carrying the reason, reaching the caller as a
  refused outcome (404 over HTTP), never as an exact-looking zero. A missing repository with
  selected endpoints raises `kind="no-repository"`. (F1 fix round, measured by
  `test_a_diff_failure_after_validation_is_refused_never_reported_as_zero`.)
- **No silent fallback, ever.** No HEAD/current-knowledge/browser-dataset/semantic-verdict
  substitution anywhere; pins are validated by `cat-file`.
- **Leaf-history drill-down is R24's, not closed here.** This module selects the net; the
  catalogue, drill-down UI and stable generation links are R24's obligation using R12 views.
  This leaf only exposes `leaves[].state`, pinned params and per-view `generation` for R24
  to build on. The browser-class journeys belong to R25.
- **R03/R11/R16 idioms reused, not duplicated.** R03's listing-pinned expansion idiom for
  the master range, R11's custody (stateless pins reference the same Git objects custody
  retains; nothing extended), R16's refusal idiom (`RecordedEndpointAbsent` subclass plus
  the shared 400/404 mapping).
- **`knowledge_review.py` untouched.** The over-limit adapter is not this leaf's
  responsibility — this leaf's work is transport/serving, so no adapter extraction was owed.

## Evidence

### Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

No configured Domain Documentation source exists for this file.

### Repo-Internal References

- The one scope the selection ever serves, and the three-state request contract (live / pinned / absent) with the digest and currentness rules. [1]
- The named refusal for a missing master endpoint, as the committed-range vocabulary applied to the master's base and result. [2]
- The explicit generation selector: exact commits, never branch names; empty means the declared integrated result. [3]
- The exact `base -> tip` commits one net comparison is computed over, and the resolved selection with its identity, scope and currentness. [4]
- Master task-root confinement and series-contract loading moved here from `changeset.py`. [5]
- The integration-branch head with deliberately no source-branch fallback. [6]
- The deterministic generation identity over the four endpoints. [7]
- The selector: `None` for an unknown master, named refusal for missing code endpoints, memory degradation for an absent leg. [8]
- Independent half resolution: required code pair vs degradable memory leg, and the `cat-file` resolve check with its two broken-state kinds. [9]
- Currentness measured against the live integrated tips in the same call. [10]
- The thin delegating entry that consumes the selection and publishes `generation` + `currentness` + `scope`. [11]
- The committed-range refusal vocabulary this module subclasses, with its three absence kinds. [12]
- The nine cases that measure the selection (eight plus the F1 diff-failure case) through real contracts, repos and routes. [13]

### Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

No applicable cross-repository source was found.
