# mcp/tests/test_citation_source_index_membership.py

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

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this file.

No configured `Domain Documentation` source; the population rule is Git's own and is exercised against real `git` invocations rather than documented from an external reference.

### Repo-Internal References

- The acquisition rule and its caps, which these cases exercise. [1]
- The caps themselves, owned by the state module the index imports them from. [2]
- The landed citation cases that the rejected "skip every untracked path" reading re-reds — the reason the uncommitted-but-unignored half is retained. [3]
- The lane row this module carries. [4]

### Cross-Repo References

No external repository boundary is implemented by this test module; every root it builds is local to
the case's temporary directory.

No meaningful cross-repo references found.
