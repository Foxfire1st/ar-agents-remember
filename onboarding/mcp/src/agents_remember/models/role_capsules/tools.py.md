# mcp/src/agents_remember/models/role_capsules/tools.py

## Governing Overview

[models overview](../overview.md)

## Purpose

Requested tool identities, narrowed against the admitted permission policy. **A capsule
*requests* capabilities; it never grants them.** This module is the whole of that boundary.

## Code Commentary

### Logic

cit:([`narrow_tool_requests`], mcp/src/agents_remember/models/role_capsules/tools.py:24-58) turns the tool identities the compiled sources
declare into cit:([`CapsuleToolRequest`], mcp/src/agents_remember/models/role_capsules/types.py:435-450) values, deduplicated and returned in
**stable tool-id order**, and refuses (`tool-request-not-permitted`) rather than silently
widening when a request falls outside the snapshot an existing AR owner admitted
(cit:([`CapsuleToolPolicy`], mcp/src/agents_remember/models/role_capsules/types.py:181-194)).

The declared identities come from the canonical manifest's per-role `tools` array, read through
the compiled sources and handed here as `(tool_id, authority)` pairs. Nothing in this module can
add a tool the policy did not already permit, *which is why the check is a subset test and not a
merge.*

### Conventions

Order is by tool id, not by declaration order — the capsule's requested-tool list must be
reproducible from the same admitted facts regardless of how the manifest lists them.

### Invariants And Boundaries

- **A request is not a grant.** This module narrows; it never widens, and it never mutates the
  policy snapshot.
- A request outside the admitted policy is a typed refusal, not a dropped entry. Silently
  dropping a declared request would make the capsule differ from its own sources.
- The returned tuple is deduplicated and in stable tool-id order; the semantic digest lists
  these ids in that order.
- The manifest declares *what a role asks for*; the admitted `CapsuleToolPolicy` decides *what is
  permitted*. Do not merge those two authorities into one table.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The admitted policy snapshot and the request/`ToolId` shapes this module works with. [1]
- The refusal code for a request outside the admitted snapshot. [2]
- The compiler step that narrows requests before sealing the digest. [3]
- The architect seat's declared tool requests in the canonical manifest, including the child-seat messaging tool that supplies a declared identity. [4]
- A request inside the policy is carried but not granted; one outside it is refused; every declared id exists in the public tool roster. [5]

### Cross-Repo References

No sibling-repository contract defines this narrowing rule.

No meaningful cross-repo references found.
