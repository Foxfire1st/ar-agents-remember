# mcp/src/agents_remember/worktrees/modules/git.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/modules/git.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T01:02 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Nearest governing overview](overview.md)

Working candidate verification: source inspected at 2026-09-15T01:02 UTC against the uncommitted L9 candidate.
The commit fields identify the latest real commit touching this source; they do not identify a future commit for the working changes.

## Purpose

Provides shared repository/ref, candidate-tree, cleanliness, staging, committing, and changed-path
operations through the guarded kernel Git runner. Workflow admission remains with callers.

## Code Commentary

### Logic

`require_git` reports failed commands through transport-safe diagnostics while preserving the
runner's raw successful output. The removed local runner is not restored: repository-selector
scrubbing, standard-input ownership, encoding, and timeout policy stay in `kernel.git_command`.
Branch resolution uses explicit local refs, and repository identity uses Git's shared object store.

`worktree_candidate_tree(..., exclude_paths=())` uses a private temporary index per observation. It
seeds from HEAD, removes excluded entries before materialization, stages through an exclusion-aware
pathspec, writes the tree, and removes its scratch directory. The real index remains untouched.
The root cache uses `MEMORY_CACHE_EXCLUDE`; other explicit exclusions use their corresponding root
pathspecs. This avoids treating an ignored cache literal as an explicit add request.

`has_changes`, `worktree_dirty`, and `require_clean` accept the same explicit exclusions.
`contract_has_worktree_changes` excludes `memory.md` only on the memory side. Real content dirt
remains visible.

`stage_worktree_content` removes derived index entries and stages actual content without reading
those paths. `commit_if_dirty` creates an ordinary content commit when its filtered status is dirty.
`commit_verified_staged` operates on the already prepared index, removes explicitly excluded
entries, checks the staged diff, and commits with `--no-verify` without restaging. Neither helper
creates a commit for cache-only dirt. Hook execution remains a separate explicit helper.

Changed-path helpers retain their distinct semantics: existing-file worklists omit deletions, while
`changed_files_with_counts` reports additions/deletions, rename targets, counts, and binary-file
unknown counts for the serving change-set view.

### Conventions

Callers must supply exclusions for an owned derived artifact; this is not a blanket ignore rule for
all repositories. Candidate observations own separate scratch paths. Ordinary staging/committing and
verified-index committing remain deliberately separate APIs.

### Invariants And Boundaries

- All Git execution uses the guarded kernel runner and exact caller-selected repository.
- Cache-only dirt cannot trigger a memory-content commit when the caller supplies its exclusion.
- Real ref, ancestry, repository, and content checks are retained.
- Verified-index commit does not pull in later working-tree changes or rerun hooks.
- Exclusion never grants permission to move a protected ref or bypass workflow authority.

### Todos

No new implementation or live-state operation is authorized by this documentation pass.

## Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain-documentation evidence. | — | — |

## Repo-Internal References

These repository-relative targets and exact ranges were checked against the L9 working source.
Source declarations and test assertions are distinguished from execution and acceptance evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| Ref/repository identity and transport-safe errors have shared implementations. | `_transport_safe_git_diagnostic`; `require_git`; `local_branch_ref`; `repository_identity` | mcp/src/agents_remember/worktrees/modules/git.py:20-31; mcp/src/agents_remember/worktrees/modules/git.py:79-85; mcp/src/agents_remember/worktrees/modules/git.py:100-109 |
| Candidate trees use private indices and exact derived-path exclusions. | `_excluded_pathspec`; `worktree_candidate_tree` | mcp/src/agents_remember/worktrees/modules/git.py:38-68 |
| Filtered status and staging/commit APIs share the exclusion contract. | `_status_args`; `commit_verified_staged` | mcp/src/agents_remember/worktrees/modules/git.py:112-116; mcp/src/agents_remember/worktrees/modules/git.py:221-236 |
| The exact cache pathspec is defined beside the consumer filename. | `LEDGER_RELATIVE_PATH`; `MEMORY_CACHE_EXCLUDE` | mcp/src/agents_remember/kernel/memory_ledger.py:24-27 |
| Changed-file reporting preserves its distinct deletion/rename/count semantics. | `committed_changed_paths`; `changed_files_with_counts` | mcp/src/agents_remember/worktrees/modules/git.py:309-348 |

## Cross-Repo References

The code/memory or fixture-repository boundaries above are established by package-local source.
No additional configured external or sibling-repository evidence is claimed.

| Finding | Anchor | Source |
| --- | --- | --- |
| No additional configured cross-repository evidence. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T01:02 UTC — Documented explicit cache exclusions in status, candidate capture, staging, ordinary commits, and verified-index commits; preserved guarded-runner, real-index isolation, hook separation, and changed-path semantics. Working candidate verified by source inspection; commit metadata records real committed history only.


- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (reopened-claim judgement): the checker reopened
  the `run_git` claim because that construct changed after verification. Re-read the claim against
  `kernel/git_command.py`: the one runner every helper here calls still owns the `GIT_DIR`-family
  scrub, the DEVNULL stdin guard and the timeout classes, with the regenerated range (149-213)
  covering the function. Retained; verification metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 1 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-10T07:33:57+02:00 — CCR-R12@v5 scoped runtime curation against code commit `6f3e3fde75a1ca0202c9b07557cf86a7893e8532`: reconciled the normal transaction boundary and preserved earlier history. This records source documentation only; it makes no acceptance or certification claim.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `gate_staged_code`; `commit_verified_staged` repointed to mcp/src/agents_remember/worktrees/queue/closeout_staged_quality.py:139-165; mcp/src/agents_remember/worktrees/modules/git.py:188-198. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-06T22:41:21+00:00: Generated citation repair: `test_candidate_tree_isolates_concurrent_observers_with_one_scratch_namespace` repointed to mcp/tests/test_git_command.py:135-151. No content impact: mechanical anchor-range projection bound to citation source snapshot 250eac92295fa399589ccf1c9726bfb4cd28a1a0b20dca126769403fba09b52d; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-08-29T12:52+02:00 — MCAR-L02 C009 recovery: documented invocation-owned
  candidate indexes after concurrent queue and dashboard observations exposed deletion of a shared
  scratch index. Verification remains closeout-owned.

- 2026-08-22T10:39+02:00 — 260821-CLIVE-L1 candidate-11 curation rebind: refreshed formatter-moved source coordinates against accepted tree `4241908c`; where applicable, replaced a deleted coordinator anchor with the sole current owner. Verification metadata remains pinned until governed closeout.

- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-21T00:45+02:00 — 260815-DAG master full-gate repair: import paths updated to the moved package locations (`worktrees/queue`, `worktrees/integration`, `application/task_docs`, `models/queue`); reviewed — no content impact on the documented contracts. Verified at code commit e5cb139f.


- 2026-08-15T23:38+02:00 — Reconciled this worktree owner's role in task-derived protected-ref authority, exact named-ref movement, and crash-safe recovery. Verification metadata remains closeout-owned.
- 2026-08-14T05:26Z — L23 final curator: re-anchored the configured-hook/certified-index contract
  after staged quality moved to its cohesive module; Git ownership is unchanged. Verification
  remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T03:31+02:00 — 260731-EFA-L22 closeout repair: preserved surrogateescape inside the
  shared Git runner but escaped invalid bytes at `require_git`'s diagnostic boundary, preventing a
  malformed failed-hook message from crashing MCP response serialization. Added the exact invalid-byte
  hook regression reference. Verification metadata remains pinned until closeout stamps the repair.

- 2026-08-10T12:46+02:00 — L9 closeout-order repair: added the configured-hook runner and the
  exact-index `commit_verified_staged` helper. The latter never restages and uses `--no-verify`
  because the hook was already executed before the pytest-final wrapper. Verification metadata
  stays pinned until closeout stamps the repair commit.

- 2026-07-31T20:50+02:00 — 260731-EFA-L3 curator: the module-local `run_git` was deleted and every
  helper now calls `kernel.git_command.run_git`, so the old Purpose ("Owns the Git subprocess
  adapter") and the old Code Commentary opening ("All Git commands run with
  `stdin=subprocess.DEVNULL` and an explicit `safe.directory` override") were both false — the local
  copy also dropped the `GIT_DIR`-family scrub, the encoding and any timeout. Rewrote both to
  describe the shared runner, the eight `GIT_REPOSITORY_SELECTOR_ENV` names it pops, and the
  `GIT_LOCAL_TIMEOUT_SECONDS = 300` default that now bounds every helper (none passes `timeout=`,
  none catches `subprocess.TimeoutExpired`). Added the `kernel/git_command.py` reference row.
  Verification metadata pinned until closeout stamps the L3 commit.
- 2026-06-29T15:30+02:00 — operations-integration L3: added `changed_files_with_counts(repo, base, head=None)` (+ the `_rename_aware_path` helper), the change-set primitive behind the serving change-set API (`serving/changeset.py`): per-file `{path, insertions, deletions, status}` via `git diff --numstat --name-status --find-renames`, KEEPING deletions, binary→`None` counts, untracked→`A` in worktree mode, rename→post-rename path. Unlike `changed_worktree_paths`/`committed_changed_paths` it does not drop deletions. Verification metadata pinned to the task base until closeout stamps the L3 code commit.
- 2026-06-12T19:06+02:00 — Issue #83: added `committed_changed_paths()` (tree-diff `base..HEAD` ∩ `verified..HEAD`, `is_file`-filtered) and generalized `head_text_or_none` into `commit_text_or_none(repo, ref, rel)` so closeout worklists and body-gate baselines cover pre-committed work.
- 2026-06-10T04:47+02:00 — Added `head_text_or_none()` (`git show HEAD:<rel>`, `None` when absent) for the issue #56 closeout body/history gates.
- 2026-06-10T00:40+02:00 — Added `longest_tracked_path_length()` (`git ls-tree -r --name-only <ref>` with HEAD fallback, 0 for unborn repos) for the worktree-start Windows long-path preflight.
- 2026-05-25T20:41+02:00: Created during worktree manager module extraction.
