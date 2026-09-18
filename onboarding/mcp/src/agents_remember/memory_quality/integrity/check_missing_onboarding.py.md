# mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview      | `../../../../overview.md`                  |

## Governing Overview

[overview.md](../../../../overview.md)

## Purpose

`check_missing_onboarding.py` checks only the current Git worktree additions
for eligible source files that do not yet have their required onboarding pair.

## Code Commentary

### Logic

The script derives one isolated add-all candidate tree and diffs it against
`HEAD`, then resolves each added, copied, or renamed target through the same
storage/path-rule helpers used by drift detection. This makes the preflight
match the tree closeout would commit: a staged add that was later deleted does
not remain a false onboarding obligation, while untracked files still enter the
candidate. For CLI runs it derives the canonical repository name from Git's
common directory, so a linked worktree can be named after the task without
changing external-memory resolution. It intentionally does not scan the whole
historical repository.

`missing_onboarding_for_source` is now a three-way router (260731-EFA-L2): `disabled` returns
`None`, sidecar storage delegates to `_missing_sidecar_onboarding(onboarding_root, source_file,
storage_mode)`, `inline` delegates to `_missing_inline_onboarding(code_repository_root,
source_file, storage_mode)`, and anything else falls through to the single `unsupported` row. The
two helpers own one storage mode each: the sidecar one reports the mirrored path when that file
does not exist; the inline one reports `unsupported` on a `UnicodeDecodeError` and `missing` when
no inline block is found. Every `MissingOnboarding` state, `expected_onboarding` value and note
string is byte-identical to the pre-split version.

`main()` passes `--topology` / `--coordination-root` / `--settings-path` / `--onboarding-root`
to `resolve_coordination_context` inside a `CoordinationHints(...)`, matching the resolver's
current signature.

**The tree it measures now comes from the caller, not from the resolver (260915-KS-L23, D-34).** The
check splits the two inputs the way the contract-scoped memory-quality route already does: the
**settings** come from the resolved context, while the **measured tree** comes from
`--onboarding-root` when the caller supplied one and from `context.onboarding_root` otherwise. Before
the change the resolver's own root was used unconditionally, so an explicitly requested tree could be
silently replaced by the official memory repo and the command would answer confidently about the
wrong root. The two coincide for an official memory repo and differ for a leaf enclosure's memory
worktree, whose settings live in the official repo the enclosure was cut from; `--onboarding-root`'s
help text now states both supported shapes and the settings rule, and the `does not exist` refusal
names the root actually measured.

Since 260731-EFA-L3 the module runs no git subprocess of its own. It imports `run_git` from
`agents_remember.kernel.git_command` and keeps one helper, `require_git`, which adds the module's
contract that any git failure is fatal and — unlike the `require_git` helpers elsewhere — returns
the `CompletedProcess` instead of stripped text, because `worktree_added_sources` and
`code_repository_name_from_git` read NUL-delimited (`-z`) output that a `.strip()` would corrupt:

```python
def require_git(repo_root: Path, args: list[str]) -> subprocess.CompletedProcess[str]:
    result = run_git(repo_root, args)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"git {' '.join(args)} failed")
    return result
```

Raise-on-failure is unchanged behaviour: the deleted local copy already raised, it was just named
`run_git`. What the module gains is what its copy was missing — `env=git_environment()`, so an
ambient `GIT_DIR` cannot make `git diff --cached` / `git ls-files --others` answer out of a
different repository and report "no new files"; `timeout=GIT_LOCAL_TIMEOUT_SECONDS` (300s) instead
of no bound at all; and explicit `encoding="utf-8"` with `errors="surrogateescape"`, so a
non-UTF-8 filename in the `-z` listing decodes instead of raising.

### Conventions

The module is a pre-code-commit closeout helper. Agents run it while new files
are still visible in the worktree, create any reported sidecars, then commit
code and refresh the new sidecars to the real code commit hash.

### Invariants And Boundaries

- Disabled path-rule matches are ignored.
- The measured tree is the caller's `--onboarding-root` when one was supplied, and the resolved
  context's root only when it was not; the **settings** always come from the resolved context. The
  command must not silently substitute the official memory root for a tree the caller named, and it
  must not resolve settings from the measured worktree (which carries no `system/` of its own).
- Sidecar storage is detected by the boolean `is_sidecar_storage(storage_mode)`
  predicate (re-exported by the resolver), not by a truthy label string.
- Sidecar-managed files require `onboarding/<source-path>.md`.
- Inline-managed files require an inline onboarding block.
- Unsupported storage modes are reported instead of guessed.
- Candidate discovery uses `worktree_candidate_tree` with an isolated temporary index and never
  reads the real staged and unstaged layers as independent authorities.
- Git subprocesses use `stdin=subprocess.DEVNULL` and a scrubbed repository-selection environment.
  Both belong to `kernel.git_command.run_git`; this module must not grow a second runner.
- Linked-worktree basenames are not repository identifiers; the Git common
  directory is the repository identity source for CLI resolution.
- Sidecar existence and inline source reads use the shared filesystem helper so
  long Windows paths are checked consistently.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Drift helpers provide sidecar path construction and inline block parsing. | "def classify_source" | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py:163-163 |
| Resolver helpers provide storage/path-rule decisions. | "def resolve_coordination_context" | mcp/src/agents_remember/kernel/coordination_context_resolver.py:134-134 |
| The checker owns source/onboarding absence classification; deleted case inventories are not current coverage evidence. | `check_missing_onboarding` | mcp/src/agents_remember/memory_quality/integrity/check_missing_onboarding.py:50-77 |
| The kernel filesystem helper handles long-path sidecar and source probes. | "def absolute_path" | mcp/src/agents_remember/kernel/filesystem.py:10-10 |
| `run_git` — the single runner `require_git` wraps — owns the selector scrubbing, the DEVNULL stdin and the timeout classes. | `run_git` | mcp/src/agents_remember/kernel/git_command.py:149-213 |

## Update History
- 2026-09-18T19:20+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the CLI's corrected root selection (D-34). `main()` now splits the two inputs the contract-scoped route already splits — the measured tree from the caller's `--onboarding-root` (falling back to the resolved context only when none was supplied) and the storage settings from the resolved context — and the `--onboarding-root` help plus the non-existent-root refusal now name both supported shapes and the exact root measured. Without that split the resolver silently substituted the official memory root, so the command answered confidently about a tree the caller had not named; a leaf enclosure's memory worktree is a supported onboarding root now that `kernel/coordination_context/paths.py` decodes that shape. Corrected the Logic paragraph that described `main()`'s relationship to the resolver as if the resolved root were always the measured one, and added the corresponding invariant. Nothing else in this card was falsified: the isolated add-all candidate tree, the three-way storage router, the `require_git` contract and the linked-worktree identity rule are unchanged.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "def resolve_coordination_context" repointed to mcp/src/agents_remember/kernel/coordination_context_resolver.py:134-134. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (reopened-claim judgement): the citation checker
  reopened the `run_git` claim because that construct changed after verification. Re-read the claim
  against the current `kernel/git_command.py`: `run_git` is the single runner this module wraps, it
  owns the DEVNULL stdin guard and selects the three timeout classes through `GitRunnerOptions`, and
  it scrubs the selector environment by calling `git_environment()` — the wording stands, and the
  regenerated range (149-213) is the function itself. Retained, not re-stamped; verification
  metadata remains closeout-owned.
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 0 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-08-29T11:00+02:00 — Candidate discovery now diffs one isolated add-all tree against
  `HEAD`. This removes stale index residue from the missing-onboarding decision while preserving
  untracked and rename-target coverage; the real worktree index remains untouched.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B21 curator: replaced the `n/a` rows with exact
  anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-31T20:53+02:00 — 260731-EFA-L3 curator: the module-local `run_git` copy was removed; the
  helper is now `require_git`, wrapping `kernel.git_command.run_git`. Documented the rename, why it
  still returns a `CompletedProcess` (NUL-delimited `-z` output), and the three guards the copy was
  missing (environment scrubbing, 300s timeout, explicit UTF-8/surrogateescape decoding). The
  `stdin=subprocess.DEVNULL` invariant was re-pointed at the runner that now enforces it.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `PLR0911` armed with no exemptions):
  `missing_onboarding_for_source` was split into per-storage-mode helpers
  `_missing_sidecar_onboarding` and `_missing_inline_onboarding`; `main()` was updated for the
  resolver's `CoordinationHints` signature. Every reported state/path/note is unchanged.
  Verification metadata pinned until closeout stamps the L2 commit.
- 2026-05-31T12:50+02:00 — Source swapped the `sidecar_storage_label(storage_mode)` truthy-label check for the boolean `is_sidecar_storage(storage_mode)` resolver predicate (import and call site); recorded the predicate in Invariants And Boundaries (1.0.0 review remediation).
- 2026-05-24T18:51+02:00: Updated after the CLI began deriving repository identity from Git common directories and using long-path-safe filesystem probes.
- 2026-05-24T03:24+02:00: Refreshed verification metadata after the source commit landed.
- 2026-05-24T03:22+02:00: Created before the source commit so the new file has an onboarding pair before closeout.
