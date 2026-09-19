# mcp/src/agents_remember/kernel/coordination_context/paths.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/kernel/coordination_context/paths.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:50+02:00                     |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview      | `overview.md`                              |

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

## Docs References

No external documentation is needed for this package-local path policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external documentation is needed. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Resolver selection uses these path primitives for topology and settings discovery. | `resolve_coordination_context`, `_selection_roots`, `_selection_from_settings` | mcp/src/agents_remember/kernel/coordination_context/resolver.py:74-83; mcp/src/agents_remember/kernel/coordination_context/resolver.py:86-101; mcp/src/agents_remember/kernel/coordination_context/resolver.py:148-164; mcp/src/agents_remember/kernel/coordination_context/resolver.py:129-145; mcp/src/agents_remember/kernel/coordination_context/resolver.py:85-94 |

## Cross-Repo References

No cross-repository evidence is needed for local path policy.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-18T19:20+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): recorded the second onboarding-root shape this module now accepts (D-34). It refused a leaf enclosure's memory worktree (`…/worktrees/<repo>/<group>/memory-<name>/onboarding`) even though the contract-scoped memory-quality route measures that exact root, so the CLI and the tool that wraps it disagreed about the same tree. Added the new `memory_worktree_enclosure` structural decoder, the `"external"` topology it implies, the settings resolution that follows from it (a memory worktree has no `system/` of its own, so its settings are the official repo's), the three module constants, and the two-shape refusal that now names the received root. Two invariants were added; nothing previously stated in this card was falsified — the existing external/internal resolution rules and the "no scanning, no ambiguity error" statement still hold. Existing citation ranges were left for the citation pass.
- 2026-09-06T22:00:40+00:00 — Preserved production knowledge while retiring deleted test-owner citations and reconciling current testing configuration. Previous verification commit/date and history remain unchanged; no test execution or acceptance claim.


- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: re-anchored the worktree-support test
  row after the source file shifted: `test_resolver_uses_installed_runtime_root_as_coordination_root`
  at 2326-2346 and `test_resolver_ignores_dot_env_example_at_runtime` at 2348-2369. Zero findings
  remain.

- 2026-08-02T20:47+02:00 — 260731-EFA-L6 W2-B01 curator: anchored 2 citation rows; scoped citation fixing regenerated the source ranges.
- 2026-05-31T12:50+02:00 — `find_code_repository_root` dropped its `workspace_root.iterdir()` name-match scan and the "multiple code repositories" `ValueError`, leaving only absolute-path and direct-join resolution; corrected the Logic section to describe direct-join-only resolution and the removed ambiguity error (1.0.0 review remediation).
- 2026-05-25T20:57+02:00: Created by extracting `c-08-ar-coordination-context-resolver` skill path and topology helpers from the monolithic resolver.
