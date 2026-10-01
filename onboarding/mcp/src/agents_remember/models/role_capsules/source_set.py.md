# mcp/src/agents_remember/models/role_capsules/source_set.py

## Governing Overview

[models overview](../overview.md)

## Purpose

Validation of an admitted source set against the manifest's declared plan — in **both
directions**. This module is what makes "a required block is missing" a falsifiable statement
rather than a vacuous one.

## Code Commentary

### Logic

The compiler never derives the file list from the manifest. *Deriving it would make "a required
block is missing" unfalsifiable — the compiler would only ever see the subset the manifest asked
for, so the check could not fail.* Instead the plan is locked first
(cit:([`CapsuleDeclaredInstruction`], mcp/src/agents_remember/models/role_capsules/sources.py:32-49)), the admitted paths are supplied explicitly, and
cit:([`admit_source_set`], mcp/src/agents_remember/models/role_capsules/source_set.py:91-108) proves the two agree both ways through five gates:

| Gate | Source | Direction | Refuses |
| --- | --- | --- | --- |
| `_require_manifest_admitted` | mcp/src/agents_remember/models/role_capsules/source_set.py:109-136 | manifest → admitted | the manifest itself was not admitted |
| `_require_identities_agree` | mcp/src/agents_remember/models/role_capsules/source_set.py:137-173 | admitted → declared | a path admitted as an identity the manifest does not route it from, or read from the wrong composition root |
| `_require_declared_present` | mcp/src/agents_remember/models/role_capsules/source_set.py:174-194 | manifest → admitted | a path the manifest routes **to** that was never admitted — the missing mandatory block |
| `_require_declared_skills_present` | mcp/src/agents_remember/models/role_capsules/source_set.py:195-228 | manifest → admitted | a **declared skill whose root file was never admitted**, so its revision would be a fiction |
| `_require_specializations_admitted` | mcp/src/agents_remember/models/role_capsules/source_set.py:229-250 | binding → admitted | a repository specialization selected without being admitted on the binding |

The skill gate is checked for **every declared skill, not only the selected seat's**, because a
skill file is a declared source like any other and admitting an incomplete source set is the
condition this module exists to refuse. The compiler additionally refuses a *referenced* skill
that is missing, so the metadata plane and the compiled plane both fail closed.

cit:([`sources_by_path`], mcp/src/agents_remember/models/role_capsules/source_set.py:50-64) and cit:([`identity_index`], mcp/src/agents_remember/models/role_capsules/source_set.py:65-90) build the two lookup maps the gates
consume.

The both-directions property is the whole design: a one-directional check would accept a set
that is merely "mostly right", **and a source set that is merely "mostly right" is exactly the
state that produces a capsule missing mandatory material.** Every refusal is a typed value.

### Conventions

A new gate belongs here rather than in the loader or the compiler, because this is the only
module that holds both the declared plan and the admitted set at once.

### Invariants And Boundaries

- Both directions are checked. Removing either direction silently converts a mandatory-block
  defect into a successful compilation.
- The admitted set is never used to *define* the plan. The plan comes from the manifest.
- A source whose declared composition root disagrees with the root it was routed from is refused;
  so is a specialization that the binding never admitted.
- **A declared skill's root file must be admitted**, or its content-addressed revision would be a
  fiction. This is checked for every declared skill, not only the selected seat's, because a skill
  file is a declared source like any other. Both planes fail closed: this gate refuses the missing
  bytes, and the compiler refuses the missing reference.
- Refusals are typed `CapsuleCompilationError` values; nothing here repairs, skips, or
  substitutes a source.
- This module holds no filesystem access — it validates already-admitted `CapsuleSource` values.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The locked plan and admitted-source shapes this module compares. [1]
- The refusals this module raises. [2]
- The compiler step that runs this validation before resolution. [3]
- The YAML-free source of the declared plan: the parsed canonical manifest. [4]
- Missing mandatory material and wrongly-rooted/undeclared sources are refused rather than omitted. [5]
- **The declared-skill gate** and its two directions: an incomplete admitted set refuses, and a referenced-but-missing skill refuses. [6]

### Cross-Repo References

No sibling-repository contract defines this validation.

No meaningful cross-repo references found.
