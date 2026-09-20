# mcp/tests/test_citation_source_index_membership.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_source_index_membership.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T14:20+02:00 |
| lastVerifiedCommitHash | `4ef4dddc9194930611db2b1dfbb6e02113f2226a` |
| lastVerifiedCommitDate | 2026-09-20T15:00:59+02:00|
| reviewedWorkingCandidate | candidate `ar/260915-ks-l43-ar`, uncommitted; base `fb719f8936d337c4685f2758d4ba3731cd8b7fc5` |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The falsifiable cases for **D18**: the citation source index indexes Git's own population, and both of
its input caps keep their teeth. Seven cases in two classes, each driving the real citation source
index over a disposable code root rather than a mocked walk.

## Code Commentary

### Logic

`GitMembershipSourceIndexTests` (119) pins the four directions of the boundary the repair introduced,
so a later change cannot quietly move it in either:

- a **gitignored, oversized** scratch file is not indexed and the run does **not** refuse — the defect's
  own requirement. Before the repair this case failed with the error verbatim
  (`SourceIndexError: citation source-index input exceeds the 4194304-byte per-file cap`), which is why
  the mandated `memory_quality_check` could not run at all on a worktree carrying the experiment's
  `eve_runtime/.eve` dev-host bundles;
- an **untracked-but-unignored** source **is** still indexed. This is the half a literal "skip every
  untracked path" reading would have broken, and it is deliberate: a curator cites code a leaf has
  written but not yet committed, and that reading re-reds eight landed citation cases;
- a **tracked oversized** file still refuses, and an **untracked-but-unignored oversized** file refuses
  too — the caps are content bounds, not Git ones;
- a **tracked population above the aggregate cap** still refuses (sparse files just under the per-file
  cap crossing the aggregate bound), so the aggregate clause did not lose its teeth either;
- a **root outside a work tree** keeps the documented plain walk — the acquisition is Git-*assisted*,
  not Git-required, because the index must still work on a plain directory.

`ThisCheckoutsCitationIndexBoundsTests` (206) is the tip's own bound: **this** checkout's candidate
population is inside the citation caps and indexes no non-candidate path, so the mandated full-scope
memory-quality check can actually run here rather than being assumed runnable.

### Conventions

Each case builds its own disposable code root and asks the real index for its population; none of them
patches the walk, so the case cannot agree with itself. Oversized inputs are sparse files rather than
real payloads, so the caps are crossed without writing tens of megabytes.

### Invariants And Boundaries

- **The omitted population is the *ignored* one, never the uncommitted one.** A case that made
  untracked-but-unignored sources vanish would break landed curation behaviour; the two cases above
  pin both halves so neither can be traded for the other.
- **The caps are content bounds.** Removing the ignored scratch tree from the population must not
  weaken the per-file or aggregate refusal, and the tracked/untracked pair is what proves it.
- **The non-Git fallback is a contract, not a courtesy.** A root outside a work tree, a machine without
  `git`, or a refused/timed-out command keeps the documented walk.
- This module carries its own `unit-regression` row in `mcp/tests/test-evidence-lanes.toml` and no
  `mcp/tests/evidence-lifecycle.toml` catalog row: it is a test module, not a governed artifact, and
  the catalog's population is deliberately unchanged by this leaf.

## Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source; the population rule is Git's own and is exercised against real `git` invocations rather than documented from an external reference. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The acquisition rule and its caps, which these cases exercise. | `_tree_state`; `_git_candidate_paths`; `_indexed_file`; `_walkable_directory` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:810-857; mcp/src/agents_remember/memory_quality/style/citations/source_index.py:718-749; mcp/src/agents_remember/memory_quality/style/citations/source_index.py:953-1030 |
| The caps themselves, owned by the state module the index imports them from. | `MAX_SOURCE_FILE_BYTES`; `MAX_SOURCE_BYTES` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:23-23; mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:22-22 |
| The landed citation cases that the rejected "skip every untracked path" reading re-reds — the reason the uncommitted-but-unignored half is retained. | `TypeScriptPureMoveTests`; `LiveCitedFileRetargetTests` | mcp/tests/test_memory_citation_grammars.py:26-90; mcp/tests/test_memory_citation_fix_scopes.py:14-110 |
| The lane row this module carries. | "unit-regression" | mcp/tests/test-evidence-lanes.toml:5-5 |

## Cross-Repo References

No external repository boundary is implemented by this test module; every root it builds is local to
the case's temporary directory.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-20T14:20+02:00 — 260915-KS-L43 curator (deterministic-check clearance inside this leaf's change set, uncommitted on `ar/260915-ks-l43-ar`, code base `fb719f89`): **a pre-existing PLC0415 is cleared by moving a function-local import to the top level, plus `ruff format` reflows; no claim on this card changed, and the import move is the one edit here with a content consequence a reader should be told about.** `BoundTreeResolutionTests.test_tree_resolution_honours_the_bound_tree` imported `claim_change_router`, `model` and `range_resolution` inside the method body; the import block is now at the top of the module beside the existing `source_index` import, which is what the deterministic gate requires (PLC0415). The names are the same three modules and the behaviour is identical — an import is a binding, not a decision — but the card should know that the module now binds them at import time rather than at first call, because a reader following the old "imported where it is used" shape would not find it. Four `ruff format` reflows ride along in the same class (`Trees(...)`, `model.Citation(...)` and two assertion calls collapsed or split to fit), and the top-level import block's growth is what moved **every** construct below line 90: the three classes are now `GitMembershipSourceIndexTests` `:172-335`, `ThisCheckoutsCitationIndexBoundsTests` `:338-361` and `BoundTreeResolutionTests` `:364-484`, and the module constants `REPOSITORY_ROOT`/`PER_FILE_CAP`/`AGGREGATE_CAP`/`_ABSENT_MEMORY_ROOT` sit at `:107-112`. **Stamp accounting:** `reviewedWorkingCandidate` now names this leaf's candidate `ar/260915-ks-l43-ar` on base `fb719f89`; the `lastVerifiedCommitHash`/`lastVerifiedCommitDate` pair is retained exactly as recorded, because no commit contains the body as it now stands and no stamp was measured on it. No commit was made.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: created this card for the module this leaf added to
  make D18's repair falsifiable. Records the four boundary directions the cases pin (ignored-oversized
  not indexed and not refused; untracked-but-unignored still indexed; tracked **and**
  untracked-but-unignored oversized still refused; aggregate still refusing; non-Git root keeping the
  plain walk), and the reason the uncommitted half is load-bearing — the literal "skip every untracked
  path" reading costs eight landed citation cases because a curator cites code a leaf has not committed.
  Records the tip's own bound case and the module's lane row, and that the catalog population is
  deliberately unchanged (a test module, not a governed artifact). Verification metadata is pinned to
  this leaf's synced base `8997e184` because the candidate is deliberately uncommitted — the governed
  closeout stamps the real code commit, and no hash or fingerprint was invented here.
