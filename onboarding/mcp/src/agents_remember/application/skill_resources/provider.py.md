# mcp/src/agents_remember/application/skill_resources/provider.py

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

## Evidence

### Docs References

No external documentation governs the location of this repository's generated package data. The
generation contract is the source checkout's own: root `skills/` is canonical and
`scripts/sync-skills.py` refreshes the package copy. No relevant documentation found after checking
live sources.

### Repo-Internal References

- The served tree is the packaged runtime skills copy, which is what makes a served revision reproducible. [1]
- The corpus root, its manifest and its publishing origin travel together as one admission. [2]
- The publishing origin is both the URI prefix and the identity half that keeps two servers' same-named skills distinct. [3]
- The packaging helper both managers open, which may materialize the package data for the duration of the call. [4]
- The generated package-data copy the served tree is read from. [5]
- The canonical skills source tree the package copy is generated from. [6]
- The consumer obligation stated for a caller supplying a corpus root without its origin. [7]
- The case that keeps same-named skills from two servers distinct. [8]

### Cross-Repo References

No meaningful cross-repository reference applies.
