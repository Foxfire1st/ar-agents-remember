# mcp/tests/test_citation_census_inputs.py

## Governing Overview

[mcp tests overview](overview.md)

## Purpose

`test_citation_census_inputs.py` protects the receipt's own claim: the identities it reports are the captured bytes it parsed and resolved, not whatever the pair holds when the answer is read. A census that silently re-reads a moving tree is not reproducible, so the module drives a change made in the middle of a read and a quiet capture over the same two shapes of pair.

## Code Commentary

The world is built twice per case — a plain directory pair and two real Git repositories committed once — and the read is intercepted by patching `reference_anchors.census` to rewrite both the cited source and the sidecar before delegating to the original. The answer's `artifactInputIdentities`, the stored artifact's `inputIdentities` and the digest all stay at the pre-change pair; `artifactPairStableDuringRead` is true only where the change was undone before the census returned, and every target's `actualBlob` is the original bytes' blob. On a Git pair the captured tree identities replay: re-running the census over `worktreeTree` of both sides yields the same targets. The quiet case requires `measured_census` to agree with `pair_identities`, and a failed `run_git_with_index` capture raises `KnowledgeTreeReadError` instead of turning a partial scratch index into the measured tree.

## Evidence

- A change made during the read cannot rebind the captured census, over a directory pair and a Git pair [1]
- A quiet pair has reproducible identities, and a failed capture refuses instead of measuring a partial index [2]
