# mcp/src/agents_remember/models/role_capsules/selection.py

## Governing Overview

[models overview](../overview.md)

## Purpose

Explicit role, seat-kind, and operation selection over the canonical manifest. **Selection is a
lookup, not an inference.** The seat and the operation arrive on the admitted binding; the
manifest is asked which blocks that pair composes from. There is no model call, no scoring, no
fallback operation, no nearest-match role, and no combinatorial role-by-phase rule language —
three ordinary lookups and two refusals.

## Code Commentary

### Logic

cit:([`select_scope`], mcp/src/agents_remember/models/role_capsules/selection.py:114-132) is the entry point and returns a
cit:([`CapsuleScope`], mcp/src/agents_remember/models/role_capsules/selection.py:56-113) whose cit:([`declared`], mcp/src/agents_remember/models/role_capsules/selection.py:70-112) method yields the declared instruction units for that
seat. cit:([`_role_scope`], mcp/src/agents_remember/models/role_capsules/selection.py:133-148) resolves the role branch and
cit:([`_require_operation_allowed`], mcp/src/agents_remember/models/role_capsules/selection.py:149-175) enforces applicability.

Two refusals carry most of the weight here, and they are deliberately **distinct** because they
have distinct remedies:

- cit:([`narrow_role`], mcp/src/agents_remember/models/role_capsules/selection.py:191-213) and cit:([`narrow_operation`], mcp/src/agents_remember/models/role_capsules/selection.py:194-206) refuse an unknown role or operation by **exact
  membership** in the frozen vocabulary, so a caller-controlled string can never acquire a role;
- `_require_operation_allowed` refuses an operation the selected role cannot run rather than
  replacing it with a neighbouring one, *because silently substituting a different operation is
  a silent fallback wearing a lookup's clothes*.

The ambient launcher is reached as a seat kind, not a role: it composes `core/launcher.md` plus
`core/authority.md`, and it is refused any operation it does not itself declare. Identity is
therefore never derived from caller text.

### Conventions

`CapsuleScope` is constructed only by `select_scope`, so a caller cannot assemble a scope that
bypassed selection. A new role or operation does not belong here — it belongs in
`vocabulary.py` plus the manifest.

### Invariants And Boundaries

- Selection never infers. An unknown role, an unknown operation, and an operation the role
  cannot run are three separate typed refusals with three separate remedies.
- No fallback operation, no nearest-match role, no default seat. A missing applicability entry is
  a refusal, not an empty composition.
- Membership is exact string equality against `CAPSULE_ROLES` / `CAPSULE_OPERATIONS`; no case
  folding, prefix matching, or alias table exists.
- This module reads no file and calls no model; the manifest arrives already parsed.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The frozen vocabularies membership is tested against: `capsule_role_or_none` answers by exact membership in the frozen registry. [1]
- The three selection refusals this module's callers branch on. [2]
- The parsed manifest and its per-role applicability entries. [3]
- The compiler step that calls this selection first. [4]
- The unknown-role, unknown-operation, non-applicable-operation and launcher cases. [5]

### Cross-Repo References

No sibling-repository contract defines this selection rule.

No meaningful cross-repo references found.
