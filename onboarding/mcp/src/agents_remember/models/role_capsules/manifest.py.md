# mcp/src/agents_remember/models/role_capsules/manifest.py

## Governing Overview

[models overview](../overview.md)

## Purpose

Canonical source parsing for the role-capsule composition manifest: it turns the bytes of
`skills/l-01-agent-lifecycles/composition-manifest.json` into typed values **without touching
the filesystem**, so the manifest is inspectable, diffable, and testable on its own.

## Code Commentary

### Logic

The schema constant is cit:([`COMPOSITION_MANIFEST_SCHEMA`], mcp/src/agents_remember/models/role_capsules/manifest.py:37-37) (`ar-role-capsule-composition/v1`), alongside
three refusal codes specific to parsing.

cit:([`parse_composition_manifest`], mcp/src/agents_remember/models/role_capsules/manifest.py:168-216) is the single entry point and drives a set of
per-section parsers: cit:([`_parse_core`], mcp/src/agents_remember/models/role_capsules/manifest.py:252-267), cit:([`_parse_operations`], mcp/src/agents_remember/models/role_capsules/manifest.py:268-302),
cit:([`_parse_roles`], mcp/src/agents_remember/models/role_capsules/manifest.py:303-328) with cit:([`_parse_one_role`], mcp/src/agents_remember/models/role_capsules/manifest.py:329-367), cit:([`_parse_role_order`], mcp/src/agents_remember/models/role_capsules/manifest.py:368-380),
cit:([`_parse_launcher`], mcp/src/agents_remember/models/role_capsules/manifest.py:381-419), cit:([`_parse_specializations`], mcp/src/agents_remember/models/role_capsules/manifest.py:420-454), and cit:([`_parse_skills`], mcp/src/agents_remember/models/role_capsules/manifest.py:455-478). From the
parsed document the value types are built: cit:([`CapsuleCoreEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:44-52),
cit:([`CapsuleOperationEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:53-62), cit:([`CapsuleRoleEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:63-82), cit:([`CapsuleLauncherEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:83-93),
cit:([`CapsuleSkillEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:94-110), cit:([`CapsuleSpecializationEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:111-119), and the aggregate
cit:([`CapsuleCompositionManifest`], mcp/src/agents_remember/models/role_capsules/manifest.py:120-167) whose lookups are cit:([`skill_entry`], mcp/src/agents_remember/models/role_capsules/manifest.py:138-152), cit:([`composing_roots`], mcp/src/agents_remember/models/role_capsules/manifest.py:153-158), and the role/operation accessors beside them.

**The declared vocabulary is authoritative over the manifest, not the other way round.** The
parser is handed the frozen role and operation sets and refuses a manifest that disagrees, so
a manifest edit cannot quietly mint a new role or a ninth operation. Three structural rules are
enforced on top of that: cit:([`_require_one_path_serves_one_identity`], mcp/src/agents_remember/models/role_capsules/manifest.py:513-553) refuses routing two identities
at one file, cit:([`_require_operation_applicability_agrees`], mcp/src/agents_remember/models/role_capsules/manifest.py:554-601) refuses an applicability statement that
contradicts itself, and cit:([`_require_role_skills_are_declared`], mcp/src/agents_remember/models/role_capsules/manifest.py:479-508) refuses a role whose declared skill the
manifest cannot resolve.

The manifest is authored metadata and contains **no instruction prose of its own** — the
corpus's "exactly one source per instruction" rule. A role entry also declares **two distinct
channels of capability metadata, and they are not narrowed the same way**:

- **`tools`** — the tool identities the role's compiled sources request. These **are** narrowed:
  `tools.narrow_tool_requests` is the only policy-narrowing path, and it applies to tool ids
  alone, testing each against the admitted `CapsuleToolPolicy` snapshot and refusing
  (`tool-request-not-permitted`) rather than widening.
- **`skills`** — the skill references the role declares. These are **carried, not narrowed**:
  `compiler.skill_references` builds one `CapsuleSkillReference` per declared skill from the
  skill's `identity`/`origin`/`uri` and the content `revision` of its admitted root file, and
  makes **no** `tool_policy`/`permits` call. A skill reference is a pointer to separately
  delivered content — never an activation and never a permission grant — so there is nothing for
  a permission snapshot to narrow.

The distinction matters operationally: a tool request outside the admitted policy is a refusal,
while a skill reference is always emitted for a declared skill and instead must resolve to an
admitted root file (see `_require_role_skills_are_declared`, and `_require_declared_skills_present`
in `source_set.py`).

### Conventions

Edit the canonical `skills/l-01-agent-lifecycles/composition-manifest.json` and let
`scripts/sync-skills.py` propagate it; never hand-edit a generated copy. A new role, operation,
or source path that the parser rejects is meant to be rejected.

### Invariants And Boundaries

- This module parses bytes; it never opens a file, resolves a root, or reads a source.
- The role registry is closed at nine and the operation vocabulary at eight. A manifest that
  disagrees fails compilation instead of extending the vocabulary.
- Exactly one source per instruction. Two identities routed at one path is a defect, not a
  deduplication opportunity.
- An entry naming a source that does not exist is an error, not a skip.
- A declared tool identity is a **request**. Nothing in this module or its parse result grants
  a capability; the policy snapshot in `CapsuleToolPolicy` is what permits.
- **The two declared channels are narrowed differently, and the difference is a contract, not an
  implementation detail.** Tool ids are policy-narrowed (`tool-request-not-permitted` on a
  request outside the admitted snapshot). Skill references are **carried**, verified against the
  admitted source set rather than against a policy — so a "policy" is the wrong mental model for
  a skill reference, and a skill reference must never be described as narrowed or granted.
- A declared skill the manifest cannot resolve is refused here
  (`_require_role_skills_are_declared`); it is never silently dropped.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The frozen vocabulary this parser is validated against. [1]
- The canonical authored metadata this module parses. [2]
- The tracked generated copy under the governed `mcp/**` surface, produced by the propagation owner. [3]
- Tool identities declared here are narrowed against the admitted policy, never granted. [4]
- **Skill references declared here are carried, not narrowed** — no `tool_policy`/`permits` call is made for them. [5]
- The skill identity helper and the skill entry a reference is built from. [6]
- A declared skill must resolve, and its root file must be admitted, or compilation refuses. [7]
- The shipped-manifest agreement and structural-refusal cases. [8]
- Every tool identity the shipped manifest requests exists in the public roster. [9]

### Cross-Repo References

No sibling-repository contract is consumed by this parser.

No meaningful cross-repo references found.
