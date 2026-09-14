# test_worktree_sync.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/tests/test_worktree_sync.py`          |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `bb65a2073228c5e143b055a470f39c6c9e2f4d9d`                         |
| lastVerifiedCommitDate | 2026-09-14T19:36:04+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Exercises real code/external-memory synchronization: a pure fast-forward advances both sides and contract, a code merge conflict stays recoverable and can continue, a code tip the official memory line does not map refuses **by name** and succeeds once the pair is completed, and a nonregular journal is renamed/quarantined without following it. A memory work branch that already descends from its source syncs as `already-current` even when its recomputed ledger dropped a row the source carried, because the projection owns that judgement and the sync is not a second place to restate it. Recovery uses the exact contract and ledger pair, not an inferred ambient checkout.

## Code Commentary

### Logic

The retained cases drive the public `sync_result` over `SyncFixture`, one live code/memory worktree
pair per case. `move_official_code` cit:([`move_official_code`], mcp/tests/test_worktree_sync.py:97-99) advances the official
code line and `map_official_memory` cit:([`map_official_memory`], mcp/tests/test_worktree_sync.py:101-110) lands an official memory
content commit plus a ledger row mapping a given code tip, which is how a case builds either half of
the official pair.

The mid-cycle case
cit:([`test_a_code_tip_with_no_attributing_memory_commit_refuses_by_name`], mcp/tests/test_worktree_sync.py:176-204) advances only
the code line and asserts the refusal end to end: return code 2, state `blocked`, the summary
containing `official line is mid-cycle`, and the work branch's HEAD **not** advanced to the admitted
tip — then maps the tip into the official memory ledger and asserts the same call returns `synced`
with the work branch at that tip. The refusal itself is produced by
`sync_transaction_authority.preflight_official_pair`
cit:([`preflight_official_pair`], mcp/src/agents_remember/worktrees/sync_transaction_authority.py:126-158), which reads the
official memory ledger blob at the named ref and resolves the code tip with `find_mapping`; that is
the named-ref read path, and this leaf's change to the *source*-ledger reader does not touch it. The
case is the suite's first coverage of the refusal at all, and it is the regression guard that the
source-reader change left the detection where it was.

A descendant memory ledger that dropped a source row is current, not refused
cit:([`test_a_descendant_memory_ledger_that_dropped_a_source_row_is_current`], mcp/tests/test_worktree_sync.py:206-243). The case
commits a memory content commit and then rewrites `memory.md` so its one row maps the code base to
that newer content commit — the stale-duplicate shape a closeout's recomputed table produces — and
asserts the same call returns `already-current`, that no `dropped parent mapping` text appears
anywhere in the payload, and that the memory work branch did not move. The removed rule required the
resolution to carry every row its source carried, so this case is the regression guard for the ruling
that the ledger is derived state and its rebuild reports the exclusions it cannot resolve; the
projection's own exclusion reporting is pinned in `test_memory_ledger.py`.

The source-listed behavior below is the current evidence boundary. Earlier coverage claims in history
describe prior populations and must not be used to recreate removed tests or claim they still run.
The retained behavior and its fixture limits govern this card.

### Conventions

The table lists retained test definitions, not collected parametrized or subtest counts.
Inspect the cited setup and collaborators before treating a focused result as end-to-end evidence.
The module is registered in the `integration` evidence lane (`mcp/tests/test-evidence-lanes.toml`);
a lane registration says where the module executes, not that any case in it has run.

### Invariants And Boundaries

Preserve exact refusal, identity, and cleanup assertions rather than adding overlapping helper
cases. Coverage percentages are diagnostic and production CRAP 20 prompts review; neither implies
an obligation to restore removed cases. Full suites and whole-candidate review remain master-end
work. This source inspection does not claim a newly executed test or acceptance result.

### Todos

No additional implementation scope is opened by this memory reconciliation.

## Docs References

The repository has no configured Domain Documentation source. These claims concern its own test
fixtures and assertions, so the exact retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

Each current definition below can be inspected in the exact source file. Historical references
to removed methods are superseded by this current inventory.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pure fast forward sync advances both sides and contract | `test_pure_fast_forward_sync_advances_both_sides_and_contract` | mcp/tests/test_worktree_sync.py:117-137 |
| Code merge conflict is retained and can continue | `test_code_merge_conflict_is_retained_and_can_continue` | mcp/tests/test_worktree_sync.py:139-174 |
| A code tip the official memory line does not map refuses by name, leaves the work branch where it was, and succeeds once the pair is completed | `test_a_code_tip_with_no_attributing_memory_commit_refuses_by_name`; `move_official_code`; `map_official_memory` | mcp/tests/test_worktree_sync.py:97-99; mcp/tests/test_worktree_sync.py:101-110; mcp/tests/test_worktree_sync.py:176-204 |
| The refusal this case guards is the named-ref ledger read, not the projected source ledger | `preflight_official_pair`; "def find_mapping(ledger: MemoryLedger, code_commit: str)" | mcp/src/agents_remember/worktrees/sync_transaction_authority.py:126-158; mcp/src/agents_remember/kernel/memory_ledger.py:261-263 |
| A descendant memory ledger that dropped a source row is current, nothing moved, and no `dropped parent mapping` text is reported | `test_a_descendant_memory_ledger_that_dropped_a_source_row_is_current` | mcp/tests/test_worktree_sync.py:206-243 |
| Nonregular journal is renamed without following and quarantined | `test_nonregular_journal_is_renamed_without_following_and_quarantined` | mcp/tests/test_worktree_sync.py:245-264 |
| The evidence lane the module executes in, which is where it runs rather than proof that it ran. | "mcp/tests/test_worktree_sync.py" | mcp/tests/test-evidence-lanes.toml:187-187 |

## Cross-Repo References

This card establishes test behavior, not a separate cross-repository protocol or live installation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external evidence is needed for these assertions. | N/A | N/A |

## Update History

- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the case this card
  documents was added by the frozen change set. Re-read the card: the new case and every cited range
  hold, including `find_mapping` at `memory_ledger.py:261-263`. No wording changed. Verification
  metadata remains closeout-owned.
- 2026-09-14T20:00+02:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (drift re-verification): the source gained the
  descendant-ledger case the card already documents. Re-read the card against the current source:
  every cited range (97-99, 101-110, 117-137, 139-174, 176-204, 206-243, 245-264) still holds. No
  wording changed; verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T13:20+02:00 — Recorded the added dropped-row case: a memory work branch that already
  descends from its source and whose recomputed `memory.md` maps the code base to a newer content
  commit syncs as `already-current` with no `dropped parent mapping` text and no branch movement,
  which is the regression guard for the ruling that the ledger is derived state and the projection
  reports its own exclusions. Added the Purpose and Logic statements, the new reference row, and
  repointed `test_nonregular_journal_is_renamed_without_following_and_quarantined` (206-225 →
  245-264) and the evidence-lane row (182 → 184) after the insertion and the current manifest.
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp
  advanced.

- 2026-09-13T23:09+02:00 — 260913-LCA-L2 curator (uncommitted change set on `ar/260913-lca-l2-ar`):
  recorded the added mid-cycle case — a code tip the official memory line does not map refuses with
  `official line is mid-cycle`, leaves the work branch at its pre-sync head, and syncs once the pair
  is completed — together with the two fixture helpers it drives and the boundary that the refusal
  comes from `sync_transaction_authority.preflight_official_pair`'s named-ref ledger read rather
  than from the source-ledger reader this leaf changed. Repointed the stale citation for
  `test_nonregular_journal_is_renamed_without_following_and_quarantined` (176-195 → 206-225) after
  the insertion shifted it, and recorded the module's `integration` lane registration with the
  statement that registration is not execution evidence. Verification metadata remains
  closeout-owned; no acceptance claim and no verification stamp advanced.

- 2026-09-06T21:45:53+00:00 — Reconciled the retained IAS test/helper population and exact citation ranges, preserving prior history and verification provenance; no tests or review were run.


- 2026-08-26T08:50+02:00 — Rebound the recovery/cancellation reference to the frozen focused
  function names and range.

- 2026-08-26T08:45+02:00 — Restored canonical Docs/Cross-Repo reference sections for this changed
  sync integration suite card.

- 2026-08-26T08:30+02:00 — Restored the required governing-overview link for the frozen public
  sync integration suite.

- 2026-08-26T06:20+02:00 — Reconciled the fixture's exact-ref helper with the production
  `read_ref` API, removing a duplicate interpretation of Git absence. No test-execution claim is
  made.

- 2026-08-26T03:37+02:00 — Replaced obsolete abort/block coverage with the full resumable-sync
  contract: retained code/memory conflicts, continue/cancel, series temporary worktrees, pinned-ref
  cleanup, preview purity, invalid-input pre-admission refusal, raw/opaque quarantine, and partial
  authority manual repair. Verification remains post-Dagger/closeout-owned.

- 2026-08-17T12:30+02:00 — No content impact: L5 coverage-pragma alignment only; the documented sync behavior is unchanged.

- 2026-08-16T02:51+02:00 — L4 default-branch authority: the repository fixture now installs an
  exact remote default ref and symbolic `origin/HEAD`, allowing sync cases to reach their intended
  source and memory assertions without weakening fail-closed authority.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B23 curator: rebased the `sync_log` range; exact
  non-fixing check returns zero findings.

- 2026-08-02T21:14+02:00 — W2-B03 curator: resolved 2 initial citation findings (1 anchor, 0 prose, 1 source); scoped recheck PASS (0 findings). Verification metadata unchanged.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-07-31T16:50+02:00 — 260731-EFA-L2 curator, code-quality hardening sweep.
  No content impact: `SyncFixture` now builds its contract through
  `default_contract(ContractTask(...), leaf=LeafIdentity(...), code=RepoBranchPlan(...),
  memory=RepoBranchPlan(...))` instead of the flat keyword list, and everything else is
  `ruff format` reflow of the two `git worktree add` argument lists, two `assertEqual` calls,
  and the `subprocess.run` inside `git()`. This card names no `default_contract` keyword, and
  the same repo paths, source/work branches, and base commits are still paired, so the eight
  documented sync cases and their assertions are unaffected.
- 2026-06-10T09:56+02:00: Created with issue #54 sub-task D (8 tests over live-worktree fixtures).
