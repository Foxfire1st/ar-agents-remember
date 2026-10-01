# mcp/src/agents_remember/kernel/coordination_context/paths.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

`paths.py` owns path and topology primitives for locating code repositories,
coordination roots, memory roots, settings files, and onboarding roots.

## Code Commentary

### Logic

The module detects installed coordinator roots, derives the source-development
default coordination root, normalizes settings scalars and relative paths,
resolves a code repository by absolute path or by a direct
`<workspace-root>/<name>` join, and infers memory roots/settings paths from
either explicit settings or onboarding roots. `find_code_repository_root` no
longer scans `workspace_root.iterdir()` for name matches, so it cannot raise the
"multiple code repositories" ambiguity error; a non-direct hit yields only the
"was not found" `ValueError`.

**A leaf enclosure's memory worktree is a supported onboarding root (260915-KS-L23, D-34).** The
module now decodes that shape structurally instead of refusing it:

- `memory_worktree_enclosure(onboarding_root)` returns
  `(coordination_root, code_repository_name)` for
  `…/worktrees/<repo>/<group>/memory-<name>/onboarding`, or `None`. Every segment is matched — the
  parent must be literally `worktrees`, the leaf directory must start with `memory-` and be longer
  than the prefix, and no segment may be empty — so a lookalike directory earns no acceptance.
- `infer_topology_from_onboarding_root` answers `"external"` for that root, which is the topology it
  genuinely has: the memory is external to the code repository, and this is the exact root the
  contract-scoped memory-quality route measures (it takes its root from the contract, not from this
  resolver, which is why refusing it here refused a location the product itself uses).
- `infer_settings_path` resolves a memory worktree's governing settings to the **official** memory
  repo's `system/settings.md` (`external_memory_root(coordination_root, name)`), because a memory
  worktree carries no `system/` of its own; when that file is absent it falls through to the previous
  inference, so an unknown worktree reports a missing settings file instead of silently resolving to
  some other repository's.
- The refusal, when it still fires, names **both** supported shapes and the exact root received
  instead of one shape and no value.

The three directory names (`WORKTREES_DIRNAME`, `MEMORY_REPOS_DIRNAME`, `MEMORY_WORKTREE_PREFIX`) are
module constants so the accepted shape and the refusal text cannot drift apart.

### Invariants And Boundaries

- Source-checkout `.env` and `.env.example` are not resolver authority.
- Internal memory resolves under `<code-repository-root>/ar-memory`; external
  memory resolves under `<coordination-root>/memory-repos/ar-<repo>`.
- **A leaf enclosure's memory worktree resolves to `external` too**, and the shape is decoded
  structurally: `<coordination-root>/worktrees/<repo>/<group>/memory-<name>/onboarding`. A directory
  that merely resembles it earns no acceptance, and the refusal names both supported shapes plus the
  received root.
- A memory worktree's settings come from the **official** memory repo of the pair it was cut from; a
  memory worktree carries no `system/` of its own.
- Path helpers do not parse settings content or inspect Git.

## Evidence

### Docs References

No external documentation is needed for this package-local path policy.

No relevant external documentation is needed.

### Repo-Internal References

- Resolver selection uses these path primitives for topology and settings discovery. [1]

### Cross-Repo References

No cross-repository evidence is needed for local path policy.

No meaningful cross-repo references found.
