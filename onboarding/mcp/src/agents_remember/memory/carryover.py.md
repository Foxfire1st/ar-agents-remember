# mcp/src/agents_remember/memory/carryover.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/carryover.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:06 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[Nearest governing overview](../../../overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Plans and applies evidence-backed onboarding carryover after code lands. Selected memory content
is committed in the exact ordinary recovery leaf and attributed to the selected official code tip.
Integration of that leaf remains a separate operation.

## Code Commentary

### Logic

`CarryoverRequest` owns the plan inputs; `CarryoverApplyOptions` contains the intent, explicit
review selections, and memory message. `CarryoverRefs` keeps the base/source/official comparison
frame constant for a plan, and `MemoryOnlyDoc` carries one memory-only candidate's source and target
paths. The former `TargetLedger` handle and ledger message option are retired.

Planning classifies file sidecars, route overviews, memory-only docs, and entity catalogs. Automatic
carry requires proven evidence; exact-landed evidence requires every relevant source-branch commit
to be an ancestor of the official ref. Review-required candidates must be explicitly selected.

Apply verifies configured repository identity and the exact open external-memory leaf. Its code
base and code HEAD must equal the selected official tip, with a clean code checkout. Target memory
must be clean for actual content; `memory.md` is excluded from that check. Explicit target storage
and path-rule authority is resolved before writes and reused for route-index refresh. Source-memory
settings do not grant target write authority.

Copied sidecars receive the official verification metadata. Entity catalog fingerprints are
recomputed against the official code ref and reported; derived route indexes are regenerated on the
target when its code checkout permits that operation. No carried content or no actual content delta
returns `nothing-to-carryover`, refreshes the cache best effort, and creates no commit.

For changed content, cache preparation runs before the shared Git helper commits with
`exclude_paths=("memory.md",)`. The kernel renderer appends attribution to the caller's memory
message without rewriting its body, including when its last paragraph resembles trailer lines.
The result reports `memory_content_commit` and `ledger_cache`. The old `ledger-mapped-head` path,
ledger-only commit, and duplicate local commit helper no longer exist.

### Conventions

The CLI and MCP remain adapters around typed requests and planning/application services. Git
commands use the shared guarded runner and its `GitRunnerOptions` input-text path for patch IDs.
Content committing and identity setup use the shared Git module. Indexes are regenerated rather
than copied, and default read settings cannot substitute for explicit target write authority.

### Invariants And Boundaries

- Only the exact configured recovery-leaf memory checkout may receive carried content.
- Repository identity, open-leaf state, official code tip, and explicit target settings remain checked.
- A missing or malformed cache does not change candidate evidence or admission.
- Nothing-to-carryover cannot invent attribution for a new code state or create a cache-only commit.
- The real memory commit carries the official tip's attribution; cache rows are derived afterward.

### Todos

No new file-local follow-up is established by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

| Finding | Anchor | Source |
| --- | --- | --- |
| Candidate comparison and explicit review selection. | n/a | [mcp/src/agents_remember/memory/carryover.py](mcp/src/agents_remember/memory/carryover.py) |
| Apply owns one content commit and preserves exact leaf/repository authority. | `memory_content_commit` | mcp/src/agents_remember/memory/carryover.py:780-784 |
| Target storage is established from effective explicit settings. | n/a | [mcp/src/agents_remember/memory/carryover_authority.py](mcp/src/agents_remember/memory/carryover_authority.py) |
| Shared committing explicitly excludes the consumer cache. | n/a | [mcp/src/agents_remember/worktrees/modules/git.py](mcp/src/agents_remember/worktrees/modules/git.py) |
| The public carryover test preserves the caller body, verifies attribution, and proves no extra repeat commit. | `test_carryover_attributes_its_memory_content_commit_to_the_official_head` | mcp/tests/test_memory_attribution_producers.py:238-300 |

## Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence is claimed. | — | — |

## Update History

- 2026-09-15T01:06 UTC — Rebound source citation ranges after final shared-helper updates and formatting; current body contracts rechecked against the working candidate. No committed-source hash or execution claim was advanced.


- 2026-09-15T00:51 UTC — Retired TargetLedger, ledger_commit_message, ledger-mapped-head, and standalone ledger commits; documented cache-independent content checks and the shared commit helper while preserving evidence tiers, target authority, and caller-body attribution. Working candidate verified by source inspection; real last-touch commit metadata retained, with no future commit hash or certification claim.

- 2026-09-14T17:20+02:00 — 260913-LCA-L3 (uncommitted change set on `ar/260913-lca-l3-ar`, base
  `7317108b`): `require_git` now calls `run_git(repo, args, GitRunnerOptions(input_text=input_text))`
  and `patch_id` calls `run_git(repo, ["patch-id", "--stable"], GitRunnerOptions(input_text=diff_text))`,
  the runner's keyword arguments having collapsed into one optional `GitRunnerOptions` object; the
  timeout class each site names is unchanged. Rebound the ranges the migration shifted
  (`_apply_carryover_for_request` 760-863 → 768-870, `_require_carryover_authority` 865-901 → 873-909,
  `official_head` 787 → 795, the commit/render pair 846-852 → 854-860, `_nothing_to_carry_result`
  720-757 → 728-765, `load_ledger`/`write_ledger` 202-205/216-238 → 208-211/222-244), and recorded
  that the timeout every carryover call inherits is the `GitRunnerOptions.timeout` default.
- 2026-09-13T23:52+02:00 — 260913-LCA-L4 curator (uncommitted change set on `ar/260913-lca-l4-ar`,
  base `5bb124d4`): carryover became one of the five memory-content producers. `:846-849` now commits
  the caller's `CarryoverCommitMessages.memory` body through
  `kernel.memory_attribution.render_memory_content_message(..., official_head)` — the same
  `official_head` (`:787`) the mapping is prepended against on the next line, so trailer and ledger row
  cannot disagree — and the attribution is appended rather than formatted into the body precisely
  because that body is a public argument that may be several paragraphs long. Recorded the
  trailerless-by-rule sites with their reasons (the ledger leg at `:852`, the ledger-mapped-head branch
  at `:748`, and the `nothing-to-carryover` branch that creates no commit) and the end-to-end case that
  drives the public tool with a hostile multi-paragraph body. Rebound the two stale inline citations
  (`_require_carryover_authority` 856-892 → 865-901, `_apply_carryover_for_request` 759-853 → 760-863).
  Verification metadata remains closeout-owned; no acceptance claim and no verification stamp advanced.
- 2026-09-11T23:05:00+00:00: Curator citation reconciliation: `load_ledger`, `write_ledger` repointed to mcp/src/agents_remember/kernel/memory_ledger.py:202-205, mcp/src/agents_remember/kernel/memory_ledger.py:216-238. No content impact: mechanical anchor-range projection against citation source snapshot b911c7c4c4eb354cf78d2a53e1538fc36a5f9a5e36a3702e5953739b48812830; claim bytes unchanged.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this file's L4 role in task-derived integration authority and protected code/memory boundaries. Verification metadata remains closeout-owned.

- 2026-08-03T03:59:59+02:00 — Curated 10 citation claims (5 table rows, 5 source-form repairs): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-07-31T20:52+02:00 — 260731-EFA-L3 curator: the module's local `run_git` (the only copy that
  accepted `input_text`) was deleted and every git call re-pointed at
  `kernel.git_command.run_git`; `require_git` now just wraps it. Rewrote the MX-FIX-4 note that
  claimed a "local input-bearing Git adapter" scrubs selectors — that adapter no longer exists —
  and recorded what the shared runner adds on top of the deleted copy (300s local timeout,
  `encoding="utf-8"`, `errors="surrogateescape"`). Added a `git_command.py` L24-L96 reference row.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0913` armed with no exemptions):
  added the frozen `CarryoverRefs`, `MemoryOnlyDoc` and `OfficialLedger` parameter objects and
  re-signed `candidate_for_path`, `memory_only_doc_candidates`, `_memory_only_evidence` and
  `_nothing_to_carry_result` onto them. `build_plan_for_request` now builds one `CarryoverRefs` and
  passes it to both candidate builders, so a plan's comparison frame is constructed once instead of
  re-listed per call. Evidence tiers, decisions, reasons, the ledger-mapped-head path and the
  emitted plan/apply payloads are all unchanged. Verification metadata pinned until closeout stamps
  the L2 commit.
- 2026-07-18T20:03+02:00 — FEUI-MX-FIX-4: apply now requires effective official-memory storage
  authority before mutation, reuses it for route-index refresh, and scrubs ambient Git selectors.
- 2026-06-11T15:05+02:00 — Documented `memory-only-doc` and `entity-catalog` candidate kinds,
  evidence helpers, fingerprint validation, and apply reporting.
- 2026-06-10T09:45+02:00 — Issue #54 sub-task C added ff-only memory-main advancement and result
  reporting.
- 2026-06-10T05:50+02:00 — Issue #56 sub-task 3 added route-overview candidates and guarded
  official-side route-index regeneration.
- 2026-06-10T05:30+02:00 — Git children stopped inheriting the MCP stdio protocol pipe.
- 2026-06-02T04:00+02:00 — Apply began mapping an unmapped official code HEAD when nothing is
  actionable to carry.
- 2026-05-31T12:30+02:00 — `exact-landed-commit` began requiring every path-touching source commit
  to be an official-ref ancestor.
- 2026-05-29T18:35+02:00 — Narrowed plan candidates for Pyright; behavior unchanged.
- 2026-05-24T00:35+02:00 — Added carryover request/service entry points for MCP controllers.
- 2026-05-23T13:09+02:00 — Copied into the MCP package and patched to package imports.
