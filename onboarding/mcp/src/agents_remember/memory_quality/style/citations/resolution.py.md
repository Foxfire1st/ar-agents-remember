# mcp/src/agents_remember/memory_quality/style/citations/resolution.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/resolution.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T02:22:00+02:00 |
| lastVerifiedCommitHash | `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| lastVerifiedCommitDate | 2026-09-19T18:19:12+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Resolve citation source paths against the code and memory roots, preserving ordinary filesystem lookup and an explicit Git-candidate selection.

## Code Commentary

### Logic

`Trees` carries the roots, optional managed-cache authority, and optional exact candidate tree. Ordinary lookup checks an existing code file before memory. With a candidate tree, code lookup first requires Git membership and verifies that member's current bytes; an absent member can resolve only as a file contained within the memory root. A failed candidate proof propagates instead of selecting different code bytes.

Since 260915-CAPS-L14 `Trees` also carries the **exclusion register** the acquisition will honour —
the parsed `pathRules.exclude` / caller rules, the code root's `.gitignore` patterns, the
`gitignore_authority` the caller established, and the resolved caps — so a consumer receives the rule
set that produced the population together with the population. **`Trees.exclusions` is built with the
default `absent` authority**; the route that actually applied the ignore rules is the one that must
replace it, and the default walk does exactly that through `_gitignore_authority`. The explicit
candidate route records the authority Git's membership actually exercised, so one root gives one
recorded authority on both routes. When the register is not supplied here it is resolved from the
memory layer's `system/settings.json` through `read_citation_index_settings`.

`ours` recognizes a first path component already present under either root so diagnostics can distinguish missing repository paths from external dependencies. It does not establish candidate membership. `operation_trees` binds an operation to the supplied onboarding root and revalidates managed-cache root authority.

### Conventions

An absent `candidate_tree` selects ordinary filesystem semantics. A supplied identity uses the canonical validator in `source_index_state`; `GitSourceCandidate` owns Git census and byte verification. Candidate trees do not allocate additional cache roots.

### Invariants And Boundaries

- Code takes precedence over a colliding memory path.
- Candidate lookup cannot admit an untracked/generated code competitor through the memory branch or a memory symlink escaping to code.
- Resolving sources does not acquire an index lease, publish memory, or grant write authority.
- The register is a value on the lookup, not a global: two operations over one root may carry different caller excludes, and neither changes the other's population.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Root, candidate selection and the exclusion register belong to the same immutable lookup value. | `Trees` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:38-54 |
| Candidate code lookup proves membership and bytes; memory lookup remains contained. | `resolve` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:85-101 |
| Existing top-level names classify unresolved repository paths without proving Git membership. | `ours` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:103-115 |
| Onboarding and managed-cache roots must match the operation's Trees. | `operation_trees` | mcp/src/agents_remember/memory_quality/style/citations/resolution.py:118-130 |
| The three sources the register records. | `EXCLUSION_SOURCES` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:54-61 |
| The register value this lookup carries. | `ExclusionRegister` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:127-172 |
| The two settings blocks a caller's register is resolved from when none is supplied. | `read_citation_index_settings` | mcp/src/agents_remember/memory_quality/style/citations/citation_index_settings.py:56-85 |
| The route that replaces the default `absent` authority with the one it actually exercised. | `_gitignore_authority` | mcp/src/agents_remember/memory_quality/style/citations/source_index.py:934-950 |

## Update History

- 2026-09-17T12:25+02:00 — 260915-CAPS-L14 curator: recorded that `Trees` now carries the **exclusion register** (the parsed rules, the code root's ignore patterns, the caller's `gitignore_authority` and the resolved caps), that its default authority is `absent` and the route that applied the rules must replace it, and that the register is a value on the lookup rather than global state — so two operations over one root may carry different caller excludes. Added the register/settings/authority rows. **Re-derived every range against the 130-line source**: `Trees` was cited as `:30-78`, which no longer contained it, and all four rows were stale. Verification metadata is left at this leaf's synced base `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
