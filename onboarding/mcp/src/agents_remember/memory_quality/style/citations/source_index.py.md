# mcp/src/agents_remember/memory_quality/style/citations/source_index.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/source_index.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `15fa0e2c0bb91d5bb1b2abf4ee8eb54916bd5ed4` |
| lastVerifiedCommitDate | 2026-09-16T22:28:15+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Acquire and lease a persistent citation source index while keeping ordinary filesystem freshness checks and explicit Git-candidate selection distinct.

## Code Commentary

### Logic

`open_repository_index` validates the current generation under a shared lock, upgrades to the existing exclusive publisher lock when needed, and returns a shared-lock `RepositoryIndex` lease. Ordinary acquisition enumerates the eligible filesystem population and stats its files; changed identities cause content checks, a metadata-only manifest refresh when bytes match, or a rebuilt generation when content differs.

When `Trees` carries a candidate tree, `_tree_state` delegates population and working-byte proof to its `GitSourceCandidate`. Ordinary traversal asks **Git** for the population instead of asserting one: `_git_candidate_paths` runs `git ls-files --cached --others --exclude-standard` under a bounded timeout and returns that path set, so the candidate is the tracked population **plus** untracked-but-not-ignored paths, while a **gitignored** scratch tree is not part of the candidate at all. The walk then skips a file outside that set and prunes a directory with no candidate beneath it; VCS marker files and the declared directories/suffixes are excluded as before, including a linked checkout's `.git` file. Dirty, added and renamed **working-tree** bytes are still hashed — the set is Git's membership, not Git's committed content, so a leaf's own uncommitted source remains citable.

The distinction is deliberate and is the D18 boundary: the omitted half is the *ignored* population, not the uncommitted one. Git-assisted, not Git-required — a root outside a work tree, a machine without `git`, or a refused/timed-out command returns `None` and the documented plain walk is kept, because the index must still work on a plain directory.

An explicit `expected_snapshot` opens only the existing matching generation. It reads bounded readiness and database metadata, verifies roots and candidate selection, and performs no source census, manifest deserialization, rebuild, or fallback. This path requires the caller to keep the source wave frozen after an integrity-checked build.

Builds apply the shared source bounds, read stable content, populate and validate a temporary database, reobserve source identities, and publish database/manifest/readiness through the existing publication protocol. The content snapshot hashes indexed paths and content hashes; candidate-tree identity is carried and checked separately. `RepositoryIndex.candidate_tree` exposes that selection to downstream consumers.

### Conventions

`source_index_state` owns source identities, manifests, readiness, errors, and input limits; `source_index_database` owns storage and anchor queries. Unmanaged caches use four fixed slots selected by the code/memory roots. Managed namespace authority remains with `source_index_cache`; candidate trees do not allocate additional cache roots.

### Invariants And Boundaries

- Readiness, manifest, database, and requested roots/candidate selection must agree before a generation is used; equal indexed content does not waive a different candidate-tree identity.
- A shared index lease protects immutable index publication, not source files. An expected snapshot is an explicit frozen-wave assertion.
- Input limits are checked before build-time file-body reads. Candidate Git hashing enforces the same limits in its own owner; it is separate from the Python source-read telemetry recorded here.
- **Default (non-candidate) acquisition is bounded by Git membership, and a machine-local gitignored tree can therefore neither refuse the index nor invalidate a published generation.** The per-file and aggregate caps stay content bounds: a *tracked* oversized file, and an *untracked-but-unignored* one, both still refuse. Removing the ignored population was the point — while it was indexed, the mandated contract-scoped `memory_quality_check` **errored** (not `ok=false`) on any worktree carrying the experiment's `eve_runtime/.eve` dev-host bundles, and the aggregate cap was consumed by machine-local build output.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| A generation is leased with query telemetry and its candidate selection. | `RepositoryIndex` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:156-237 |
| Managed authority or root-keyed fixed slots select cache storage. | `cache_paths` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:249-283 |
| Default acquisition validates, refreshes, or rebuilds under the existing locks. | `open_repository_index` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:323-390 |
| Frozen acquisition uses bounded published metadata and refuses an unavailable expected snapshot. | `_open_expected_generation` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:403-442 |
| Readiness must match both roots and the exact candidate selection. | `_ready_generation` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:522-532 |
| Changed source identities drive content and metadata refresh decisions. | `_validate` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:535-572 |
| A bounded, validated temporary database is tied to repeated source observations before publication. | `_build_once` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:586-664 |
| Candidate census and ordinary filesystem traversal retain separate selection semantics. | `_tree_state` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:810-857 |
| The default walk's population comes from Git, not from what the skip lists happen to not name. | `_git_candidate_paths` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:718-749 |
| A directory with no candidate beneath it is not part of the candidate and is pruned. | `_candidate_directories`; `_walkable_directory` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:752-767; mcp/src/agents_remember/memory_quality/style/citations/source_index.py:789-807 |
| One walked file is indexed only when it is inside the Git-reported candidate set. | `_indexed_file` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:770-786 |
| Snapshot identity hashes indexed paths and content hashes. | `_snapshot_id` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:873-880 |
| The Git population this walk asks for, and the bounded executor it uses. | `run_git`; `GitRunnerOptions`; `GIT_METADATA_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/git_command.py |

## Update History

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: **default acquisition is now bounded by Git
  membership** (defect D18, repaired by this leaf). `_git_candidate_paths` asks Git
  (`ls-files --cached --others --exclude-standard`, bounded by `GIT_METADATA_TIMEOUT_SECONDS`) for the
  code root's own population; `_candidate_directories` / `_indexed_file` / `_walkable_directory` skip a
  file outside it and prune a directory with nothing beneath it; the module docstring's "Default
  acquisition is Git-independent" was corrected to the new rule. The reason is mechanical, not
  stylistic: the old `os.walk` filter consulted neither `.gitignore` nor Git membership, so a
  **gitignored** machine-local scratch tree (`eve_runtime/.eve/**`, 34 files over the per-file cap)
  was ingested and the mandated contract-scoped `memory_quality_check` returned an **error** instead of
  `ok=false` on any worktree carrying it. Both caps keep their teeth: a tracked oversized file and an
  untracked-but-unignored oversized file still refuse, and the aggregate bound still refuses. The
  uncommitted-but-unignored half is deliberately retained — a curator cites code a leaf has written but
  not yet committed, and the shipped rule is Git-*assisted*, with the documented plain walk kept
  outside a work tree. Repair, the falsifiable cases
  (`mcp/tests/test_citation_source_index_membership.py`) and the tip's measured aggregate bound are
  recorded in `notes/reports/260915-CAPS-L16-worker-report.md` §7 and verified in
  `notes/reports/260915-CAPS-L16-verdict-baseline.md` §7. Verification metadata moves to this leaf's
  synced base `8997e184`; the candidate is deliberately uncommitted, so the governed closeout stamps
  the real code commit and no hash or fingerprint was invented here.

- 2026-09-06T02:22:00+02:00 — L30 recovery source review: Documented candidate census acquisition and frozen-generation identity checks while preserving ordinary filesystem freshness, fixed cache slots, and publication ownership. Verified against prepared code commit `97e8ed2e1fae21756c3ad995c30613d4fbfcc503`; source review does not claim Gate-5 execution or recovery acceptance.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
