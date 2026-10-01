# mcp/src/agents_remember/memory_quality/style/citations/resolution.py

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

## Evidence

### Repo-Internal References

- Root, candidate selection and the exclusion register belong to the same immutable lookup value. [1]
- Candidate code lookup proves membership and bytes; memory lookup remains contained. [2]
- Existing top-level names classify unresolved repository paths without proving Git membership. [3]
- Onboarding and managed-cache roots must match the operation's Trees. [4]
- The three sources the register records. [5]
- The register value this lookup carries. [6]
- The two settings blocks a caller's register is resolved from when none is supplied. [7]
- The route that replaces the default `absent` authority with the one it actually exercised. [8]
