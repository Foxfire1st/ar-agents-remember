# mcp/src/agents_remember/serving/master_net_generation.py

| Field                  | Value                                                        |
| ---------------------- | ------------------------------------------------------------ |
| repository             | agents-remember                                              |
| path                   | `mcp/src/agents_remember/serving/master_net_generation.py`  |
| doc_type               | `file-level-onboarding`                                      |
| lastUpdated | 2026-09-22T11:00:00+02:00 |
| lastVerifiedCommitHash | `2edad477bcd9127a90e4618d345ce34ef7e6a6d9`                   |
| lastVerifiedCommitDate | 2026-09-23T00:33:19+02:00|
| governingOverview      | `overview.md`                                                |

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

## Docs References

The curator checked the memory repository's `system/sources.md`; no Domain Documentation entries
are configured. This one-to-one card therefore relies on its direct agents-remember source/tests and
the reviewed task evidence for any current behavioral claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured Domain Documentation source exists for this file. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one scope the selection ever serves, and the three-state request contract (live / pinned / absent) with the digest and currentness rules. | `MASTER_NET_SCOPE` | mcp/src/agents_remember/serving/master_net_generation.py:67-67 |
| The named refusal for a missing master endpoint, as the committed-range vocabulary applied to the master's base and result. | `MasterEndpointAbsent` | mcp/src/agents_remember/serving/master_net_generation.py:73-81 |
| The explicit generation selector: exact commits, never branch names; empty means the declared integrated result. | `MasterNetPins` | mcp/src/agents_remember/serving/master_net_generation.py:86-97 |
| The exact `base -> tip` commits one net comparison is computed over, and the resolved selection with its identity, scope and currentness. | `MasterNetEndpoints`; `MasterNetSelection` | mcp/src/agents_remember/serving/master_net_generation.py:101-107; mcp/src/agents_remember/serving/master_net_generation.py:111-117 |
| Master task-root confinement and series-contract loading moved here from `changeset.py`. | `master_task_root`; `load_master_contract` | mcp/src/agents_remember/serving/master_net_generation.py:120-125; mcp/src/agents_remember/serving/master_net_generation.py:128-139 |
| The integration-branch head with deliberately no source-branch fallback. | `integrated_tip` | mcp/src/agents_remember/serving/master_net_generation.py:142-155 |
| The deterministic generation identity over the four endpoints. | `master_net_digest` | mcp/src/agents_remember/serving/master_net_generation.py:158-168 |
| The selector: `None` for an unknown master, named refusal for missing code endpoints, memory degradation for an absent leg. | `select_master_net` | mcp/src/agents_remember/serving/master_net_generation.py:171-200 |
| Independent half resolution: required code pair vs degradable memory leg, and the `cat-file` resolve check with its two broken-state kinds. | `_code_endpoints`; `_memory_endpoints`; `_require_resolves` | mcp/src/agents_remember/serving/master_net_generation.py:203-226; mcp/src/agents_remember/serving/master_net_generation.py:229-255; mcp/src/agents_remember/serving/master_net_generation.py:258-272 |
| Currentness measured against the live integrated tips in the same call. | `_currentness` | mcp/src/agents_remember/serving/master_net_generation.py:281-295 |
| The thin delegating entry that consumes the selection and publishes `generation` + `currentness` + `scope`. | `master_changeset` | mcp/src/agents_remember/serving/changeset.py:247-323 |
| The committed-range refusal vocabulary this module subclasses, with its three absence kinds. | `RecordedEndpointAbsent`; `NOT_RECORDED` | mcp/src/agents_remember/serving/changeset_endpoints.py:68-125 |
| The nine cases that measure the selection (eight plus the F1 diff-failure case) through real contracts, repos and routes. | `test_two_leaves_that_add_then_remove_a_file_net_to_exactly_zero`; `test_a_diff_failure_after_validation_is_refused_never_reported_as_zero` | mcp/tests/test_master_net_generation.py:237-265; mcp/tests/test_master_net_generation.py:472-488 |

## Cross-Repo References

This card maps a repository-local agents-remember source. Import and task-boundary review found no
cross-repository implementation source that governs its behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No applicable cross-repository source was found. | — | — |

## Update History
- 2026-09-23T00:45:00+02:00 — 260921-ICR-L10 curator: **removed a verification metadata row for a field that does not exist.** The developer ruled that field out on 2026-09-22 — it has no purpose and had spread by copy-paste — and this pass deleted it here and reworded the sentences that referred to it. The fact it carried (this card describes an uncommitted candidate whose base the verification pair names) is stated in the history entries around it. No content impact: no claim about the source changed.
- 2026-09-22T11:00:00+02:00 — 260921-ICR-L13 curator (candidate `ar/260921-icr-l13`, uncommitted; base `6695a2a12961ef340c8864d56f0a1ce12b51b3c5`): **created.** The module is new in this leaf and this is its one-to-one card. It records the selection/diff split (this module selects, `changeset.py` diffs), the three request states, the deterministic digest and same-call currentness, the independent half resolution with its refusal-vs-degradation table, the R03/R11/R16 reuse and the R24/R12/R25 boundaries, and the exact-when-served/refusal-when-unreadable invariant with the F1 fix. **Stamp accounting:** the verification pair names the **production line at this leaf's base** `6695a2a12961ef340c8864d56f0a1ce12b51b3c5` (2026-09-22T09:38:24+02:00) — the line this candidate sits on — while what was actually read is this leaf's **uncommitted** working tree at that base: this leaf's **uncommitted** candidate, the only tree that contains this module. No commit contains these bytes, so closeout owns the stamp.
