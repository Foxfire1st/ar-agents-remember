# mcp/tests/test_changeset_cache.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Pin byte-identical native change-set HTTP reads, conditional reuse and fresh invalidation without mutating the Git index.

## Code Commentary

The real Git/contract fixture serves task, file-diff and master routes. Unchanged reads and ETag 304s count zero Git children; native-input mutations, same-size/restored-mtime edits, object corruption/removal/restoration, attributes and ignore/config sources invalidate retained proofs. Sidecar presence stays live around retained Git lists. Unreadable or racing input generations compute uncached. Result, repository/object, and in-flight observation retention is bounded; unrelated sibling commits and ignored trees do not become relevant inputs. These are fixture-scoped counts and byte comparisons, not installed throughput or universal filesystem freshness.

## Evidence

- Task/file/master routes retain exact native bytes and conditional responses without repeat Git children. [1]
- Working reads detect restored-mtime edits and leave native index bytes and identity unchanged. [2]
- Rename/delete/replace/add/index/HEAD/symlink mutations force fresh native equality. [3]
- Missing commits preserve refusal and later restoration becomes visible. [4]
- Sidecar appearance/disappearance updates live without rerunning Git. [5]
- Unstable or unavailable observations are not retained. [6]
- Growing result histories retain the configured bound and evict least-recent results. [7]
- One long read also bounds pending values and input observations. [8]
- Worktree/info/XDG attributes affect committed native results. [9]
- Unrelated sibling activity and packed-ref removal preserve relevant cached results. [10]
