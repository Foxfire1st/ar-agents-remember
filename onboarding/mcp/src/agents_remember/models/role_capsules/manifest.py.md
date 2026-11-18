# mcp/src/agents_remember/models/role_capsules/manifest.py

## Governing Overview

[models overview](../overview.md)

## Purpose

Canonical source parsing for the role-capsule composition manifest: it turns the bytes of
`skills/l-01-agent-lifecycles/composition-manifest.json` into typed values **without touching
the filesystem**, so the manifest is inspectable, diffable, and testable on its own.

## Code Commentary

### Logic

The schema constant is cit:([`COMPOSITION_MANIFEST_SCHEMA`], mcp/src/agents_remember/models/role_capsules/manifest.py:41-41) (`ar-role-capsule-composition/v1`), alongside
three refusal codes specific to parsing.

cit:([`parse_composition_manifest`], mcp/src/agents_remember/models/role_capsules/manifest.py:174-221) is the single entry point and drives a set of
per-section parsers: cit:([`_parse_core`], mcp/src/agents_remember/models/role_capsules/manifest.py:259-272), cit:([`_parse_operations`], mcp/src/agents_remember/models/role_capsules/manifest.py:275-308),
cit:([`_parse_roles`], mcp/src/agents_remember/models/role_capsules/manifest.py:311-334) with cit:([`_parse_one_role`], mcp/src/agents_remember/models/role_capsules/manifest.py:337-373), cit:([`_parse_role_order`], mcp/src/agents_remember/models/role_capsules/manifest.py:376-386),
cit:([`_parse_launcher`], mcp/src/agents_remember/models/role_capsules/manifest.py:389-425), cit:([`_parse_specializations`], mcp/src/agents_remember/models/role_capsules/manifest.py:428-460), and cit:([`_parse_skills`], mcp/src/agents_remember/models/role_capsules/manifest.py:463-484). From the
parsed document the value types are built: cit:([`CapsuleCoreEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:48-53),
cit:([`CapsuleOperationEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:57-64), cit:([`CapsuleRoleEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:68-84), cit:([`CapsuleLauncherEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:88-95),
cit:([`CapsuleSkillEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:99-112), cit:([`CapsuleSpecializationEntry`], mcp/src/agents_remember/models/role_capsules/manifest.py:116-121), and the aggregate
cit:([`CapsuleCompositionManifest`], mcp/src/agents_remember/models/role_capsules/manifest.py:125-171) whose lookups are cit:([`skill_entry`], mcp/src/agents_remember/models/role_capsules/manifest.py:144-157), cit:([`composing_roots`], mcp/src/agents_remember/models/role_capsules/manifest.py:159-171).

**The declared vocabulary is authoritative over the manifest, not the other way round.** The
parser is handed the frozen role and operation sets and refuses a manifest that disagrees, so
a manifest edit cannot quietly mint a role or operation outside that declared vocabulary. Three structural rules are
enforced on top of that: cit:([`_require_one_path_serves_one_identity`], mcp/src/agents_remember/models/role_capsules/manifest.py:521-559) refuses routing two identities
at one file, cit:([`_require_operation_applicability_agrees`], mcp/src/agents_remember/models/role_capsules/manifest.py:562-593) refuses an applicability statement that
contradicts itself, and cit:([`_require_role_skills_are_declared`], mcp/src/agents_remember/models/role_capsules/manifest.py:487-514) refuses a role whose declared skill the
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

Earlier card account retained from memory base `81cfe4a89f5ffb222bd09640410d268d3fbef254`, lines 66–67:

> - The compiler vocabulary is closed at ten roles and nine operations, including Bootstrap. A manifest that
>   disagrees fails compilation instead of extending the vocabulary. These compiler populations are not a claim that ten native task roles can be launched.

The current compiler declares eight roles and nine operations; the quoted base account does not define the current vocabulary.

### Conventions

Edit the canonical `skills/l-01-agent-lifecycles/composition-manifest.json` and let
`mcp/.venv/bin/python scripts/renew-instructions.py` renew facts and propagate the declared copies through the `scripts/sync-skills.py` projection owner; never hand-edit a generated copy. A new role, operation,
or source path that the parser rejects is meant to be rejected.

### Invariants And Boundaries

- This module parses bytes; it never opens a file, resolves a root, or reads a source.
- The compiler vocabulary is closed at eight roles and nine operations, including Bootstrap. A manifest that
  disagrees fails compilation instead of extending the vocabulary. Compiler vocabulary does not establish which native task roles can be launched.
- Exactly one source per instruction. Two identities routed at one path is a defect, not a
  deduplication opportunity.
- Filesystem source existence is checked by admission/compilation and the shipped-source test,
  not by this byte parser. Missing required source bytes refuse rather than being skipped.
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

## Current Contract

CapsuleOperationEntry has audience="all" as a direct-construction default, but authored operation parsing now requires a nonblank audience field. Actual all/sections mode and marker validation belong to audiences.py during composition, not to this parser. CapsuleCompositionManifest carries parsed detail_references, default empty for direct construction; parse_composition_manifest obtains them from parse_detail_declarations. The frozen compiler vocabulary contains eight roles and nine operations, including Bootstrap; it is not the native dispatched-task-role roster.  One-source-per-instruction, operation applicability and declared-skill checks remain unchanged. Merely listing ordinary references does not make a launch attachment.

This account is bound to the candidate source, not a claim of a running serving build or a fresh execution/acceptance verdict. Existing historical accounts remain historical.

## Evidence


- Launch copies detail files, substitutes paths, and records frozen revisions. [10]

- Replay validates regular opened files and frozen revisions at deterministic detail names beside the saved handover in its recorded canonical folder, not mutable corpus sources. [11]


- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [13]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [14]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [15]
- File-local implementation of the stated contract; caller-owned effects and governing workflow are separate evidence. [16]

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References


- The frozen vocabulary this parser is validated against. [1]


- The frozen compiler vocabulary declares eight roles and nine operations including Bootstrap; compiler vocabulary and native task-seat dispatch availability are distinct. [17]

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

### Repo-Internal References (continued)

### Repo-Internal References (renewed)

- Per-request detail artifacts use exact admitted bytes beside the handover and write-once publication. Anchor: L114–L129 [12]
