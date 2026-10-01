# mcp/src/agents_remember/models/role_capsules/resolution.py

## Governing Overview

[models overview](../overview.md)

## Purpose

Resolving each declared instruction identity to **exactly one** source block. Three outcomes
are permitted; the difference between them is the whole point of this module, and anything
else stops compilation.

## Code Commentary

### Logic

| Outcome | Meaning | Recorded as |
| --- | --- | --- |
| **One source** | the ordinary case; the block is composed once | a plain candidate |
| **Duplicate identity that collapses** | two admitted sources carry the same identity with byte-identical content | `duplicate-identity` collapse, exactly one block survives |
| **Explicit supersession** | the admitted binding names an override | the superseded identity is replaced wholesale, provenance preserved |
| **Contradiction at equal authority** | two different contents claim one identity with no declared winner | `equal-authority-contradiction` — **compilation stops** |

The stop is the module's reason to exist: *picking by filename, by path order, or by "last one
wins" would make the delivered instructions depend on an accident nobody wrote down.*

cit:([`gather_candidates`], mcp/src/agents_remember/models/role_capsules/resolution.py:93-134) collects every admitted source that claims a declared
identity, tiered by composition root through cit:([`_TIER`], mcp/src/agents_remember/models/role_capsules/resolution.py:49-52).
cit:([`resolve_instructions`], mcp/src/agents_remember/models/role_capsules/resolution.py:135-191) reduces each identity to its winner and returns them in
cit:([`_ordered`], mcp/src/agents_remember/models/role_capsules/resolution.py:192-204) contract order. cit:([`Candidate`], mcp/src/agents_remember/models/role_capsules/resolution.py:55-61) and
cit:([`ResolvedInstruction`], mcp/src/agents_remember/models/role_capsules/resolution.py:64-91) are the working shapes, the latter exposing
cit:([`tier`], mcp/src/agents_remember/models/role_capsules/resolution.py:76-78) and cit:([`block`], mcp/src/agents_remember/models/role_capsules/resolution.py:79-91).

Overrides are validated rather than trusted: cit:([`override_winners`], mcp/src/agents_remember/models/role_capsules/resolution.py:205-220) maps each superseded
identity to its winner, cit:([`_supersessions`], mcp/src/agents_remember/models/role_capsules/resolution.py:262-284) fans an override out to the identities it
supersedes, and cit:([`_require_override_target`], mcp/src/agents_remember/models/role_capsules/resolution.py:285-335) refuses an override that targets something
unselected or that pulls an earlier tier over a later one — an override may only replace a
block from the same or a later tier, so provenance cannot be used to smuggle authority
backwards. cit:([`_require_one_identity`], mcp/src/agents_remember/models/role_capsules/resolution.py:221-261) is the equality-conflict gate.

### Conventions

A collapse and a supersession are both **recorded**, not silent: the diagnostic manifest gets
the collapse or the override's provenance. A refusal is a typed `CapsuleCompilationError`, and
a stopped conflict carries structured conflict rows.

### Invariants And Boundaries

- Exactly one block per identity survives. Two surviving blocks for one identity is a bug.
- A byte-identical duplicate collapses; a different body at the same identity with no declared
  winner **stops compilation**. Never resolve it by filename, path order, or recency.
- Composition-root tier order is fixed. An override may replace a block from the same or a
  later tier; it may not pull an earlier tier over a role block.
- An override that supersedes an identity which is not selected, or that two overrides claim
  for one identity without an orderable winner, is refused as such.
- Override provenance is preserved into the manifest; the winner is named explicitly.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The override and selection-reason value types this module consumes. [1]
- The stopped-conflict code the equal-authority case resolves to. [2]
- The compiler step that calls gathering and resolution in this order. [3]
- The declared plan and admitted sources this module reduces over. [4]
- The collapse, stop, override-provenance and override-ordering cases. [5]

### Cross-Repo References

No sibling-repository contract defines this resolution rule.

No meaningful cross-repo references found.
