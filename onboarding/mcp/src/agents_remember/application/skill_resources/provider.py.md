# mcp/src/agents_remember/application/skill_resources/provider.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/skill_resources/provider.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T12:20+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l4` uncommitted source; base `b00a4ac2daeec7411529d5a5593a3c007fcbf320` |
| governingOverview | `../overview.md` |

## Governing Overview

[application overview](../overview.md)

## Purpose

Declares **where the served skills tree comes from** and, with it, the server identity that publishes
it. The served tree is the package's own runtime skills copy — generated from the repository's
canonical `skills/` tree by the repository's sync script — and publishing that *packaged* copy is what
makes a served revision reproducible: the bytes a client reads belong to exactly one installed build,
so a digest recorded in one exchange still names the same content in the next.

An operator can serve a different tree by supplying the root explicitly, which is how a test drives a
synthetic corpus without touching the shipped one.

## Code Commentary

### Logic

Four constants and two context managers:

- `SHIPPED_SKILL_ORIGIN = "agents-remember/skills"` — the server identity. It is the first two
  skill-path segments of every shipped skill URI **and** the `origin` half of a skill's distinct
  identity, which is what keeps two servers serving one skill name distinct.
- `PACKAGED_SKILLS_DIRECTORY = "runtime/skills"` and
  `PACKAGED_COMPOSITION_ROOT = "l-01-agent-lifecycles"` — the corpus inside that copy, whose own
  directory is the base every source path the composition manifest declares is relative to.
- `PACKAGED_COMPOSITION_MANIFEST = "composition-manifest.json"`.
- `shipped_skill_tree()` yields a `SkillSourceTree(root=..., origin=...)` for the duration of one
  server's registration.
- `shipped_composition_corpus()` yields `(corpus_root, manifest)` as **one value because they are one
  admission**: a corpus root without its manifest, or a manifest read from another root, is a pairing
  that cannot select a source set.

Both managers open `packaged_source_root()` from `install.assets`, which may materialize the package
data for the duration of the call — which is why reads happen inside the context rather than against a
path that could be reclaimed underneath them.

### Conventions

Constants are module-level and documented with the reason they exist, not just their value. The
`origin` is deliberately a path-shaped string because it is both an identity and the URI prefix.

### Invariants And Boundaries

- **`origin` travels with the tree, always.** A corpus root supplied without its publishing origin is
  what makes two servers' same-named skills collapse into one identity — `M2` and the same-name case
  in the test module both depend on the pair being carried together.
- **The served tree is the packaged copy, not the root `skills/` tree.** A reader looking for the
  served bytes must look under `package_data/runtime/skills/`; the root tree is the canonical source
  that the sync script copies from, and editing one without syncing the other is the mistake this card
  exists to prevent.
- The corpus root is a *subdirectory* of the packaged tree (`l-01-agent-lifecycles`), because the
  manifest's declared source paths are relative to that corpus, not to the skills root.
- This module decides no policy: it names a location and an identity. Registration, routing and
  refusal rules live in the catalog, the capsule operation and the registration layer.

### Todos

None recorded.

## Docs References

No external documentation governs the location of this repository's generated package data. The
generation contract is the source checkout's own: root `skills/` is canonical and
`scripts/sync-skills.py` refreshes the package copy. No relevant documentation found after checking
live sources.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The served tree is the packaged runtime skills copy, which is what makes a served revision reproducible. | `PACKAGED_SKILLS_DIRECTORY`; `shipped_skill_tree` | mcp/src/agents_remember/application/skill_resources/provider.py:29-29; mcp/src/agents_remember/application/skill_resources/provider.py:39-47 |
| The corpus root, its manifest and its publishing origin travel together as one admission. | `shipped_composition_corpus` | mcp/src/agents_remember/application/skill_resources/provider.py:50-63 |
| The publishing origin is both the URI prefix and the identity half that keeps two servers' same-named skills distinct. | `SHIPPED_SKILL_ORIGIN` | mcp/src/agents_remember/application/skill_resources/provider.py:26-26 |
| The packaging helper both managers open, which may materialize the package data for the duration of the call. | `packaged_source_root` | mcp/src/agents_remember/install/assets.py:35-47 |
| The generated package-data copy the served tree is read from. | `composition-manifest.json` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/composition-manifest.json:1-30 |
| The canonical skills source tree the package copy is generated from. | `name: l-01-agent-lifecycles` | skills/l-01-agent-lifecycles/SKILL.md:1-3 |
| The consumer obligation stated for a caller supplying a corpus root without its origin. | `CapsuleSourceSelectionRequest` | mcp/src/agents_remember/application/skill_resources/capsule.py:156-170 |
| The case that keeps same-named skills from two servers distinct. | `test_same_named_skills_from_two_servers_remain_distinct` | mcp/tests/test_capsule_serving.py:862-879 |
| The case that demonstrates removing the origin/identity pairing breaks distinctness (coordination-root relative). | `M2-resource-read-grants-a-tool-permission` | tasks/agents-remember/260915_role-capsules-and-native-eve/notes/reports/caps-l4-mutation-probe.json |

## Cross-Repo References

No meaningful cross-repository reference applies.

## Update History

- 2026-09-16T10:40:46+00:00: Generated citation repair: `test_same_named_skills_from_two_servers_remain_distinct` repointed to mcp/tests/test_capsule_serving.py:862-879. No content impact: mechanical anchor-range projection bound to citation source snapshot d000fd9192b3f076fd4f39e5e775a368dd70d71b172c679cb9d28176bdc33096; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T12:25+02:00 — 260915-CAPS-L4 curator, **closing pass, citation work on this document
  alone** (`citation_fix --document mcp/src/agents_remember/application/skill_resources/provider.py.md`):
  `test_same_named_skills_from_two_servers_remain_distinct` repointed to
  `mcp/tests/test_capsule_serving.py:862-879` (the repairs moved it), three ranges normalised to their
  exact definition extents, and one degenerate `:1-1` citation replaced by the actual frontmatter extent
  of the canonical `skills/l-01-agent-lifecycles/SKILL.md`. **Blast radius avoided (defect `D8`):** the
  root-wide form of this tool would have rewritten 188 claims across other leaves' documents; the
  per-document run wrote this file only.

- 2026-09-16T12:20+02:00 — 260915-CAPS-L4 curator, **closing pass**: corrected the served-corpus
  reference set against the settled candidate — the served tree is the generated
  `package_data/runtime/skills/` copy, the corpus that carries the composition manifest is its
  `l-01-agent-lifecycles` subtree, and the publishing origin travels with the tree. Re-anchored the
  provider ranges against the current 73-line source.
- 2026-09-16T11:45+02:00 — 260915-CAPS-L4 curator: created the card for the served-corpus provider.
  Recorded that the served tree is the packaged `runtime/skills` copy rather than the root `skills/`
  tree, that the publishing origin is carried as part of a skill's identity (not just a URI prefix),
  and why the corpus root, its manifest and its origin are one value. Verification metadata remains
  closeout-owned; no acceptance claim is made.
