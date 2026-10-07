# mcp/src/agents_remember/kernel/coordination_context/paths.py

## Governing Overview

[coordination_context overview](overview.md)

## Purpose

Path rules of the coordination context: where the coordination root, a repository's memory root, its
settings file and an onboarding card live, and which onboarding roots are supported memory locations. The
functions derive paths and probe the file system; they parse no settings content and start no Git command.

## Code Commentary

### Roots and settings

- `resolve_coordination_root_hint(hint)` resolves an explicit hint. Without one it takes the root found by
  `agents_repo_from_script()` when that directory has `skills`, `system`, `memory-repos` and `tasks`
  (`looks_like_installed_coordination_root`), and otherwise the sibling `../ar-coordination`
  (`DEFAULT_AR_COORDINATION_ROOT`).
- `external_memory_root(coordination_root, name)` is the resolved path of
  `<coordination root>/memory-repos/ar-<name>`.
- `settings_path_for_roots(memory_root, coordination_root)` returns the memory root's `system/settings.md`
  when it exists, else the coordination root's when that exists, else the memory root's path.
- `memory_roots_from_settings(settings_path, name)` derives `(coordination root, memory root)` from the
  resolved settings path. A settings file inside `memory-repos/ar-<name>` gives that repository and the
  coordination root two levels above it. A settings file under a directory named `ar-memory` is refused as
  the removed mode `internal`, naming the file. Any other location is taken as a coordination root.
- `path_settings_path_for` is the same path with the suffix `.json`.

### What is recorded

The resolutions in `resolve_coordination_root_hint` (explicit hint and sibling default),
`external_memory_root` and `memory_roots_from_settings` go through `observed_resolve`, and the two probes
of `settings_path_for_roots` through `observed_exists`. Inside a recording block each resolution leaves a
`resolve:` row keyed by the unresolved absolute path, and each missing settings file leaves an `absent`
row. A result kept with these rows is recomputed when a root link is retargeted or when a settings file
with higher priority appears. Outside a recording block the functions record nothing and return what
`Path.resolve()` and `Path.exists()` return. `agents_repo_from_script`, `find_code_repository_root`,
`memory_worktree_enclosure` and `infer_topology_from_onboarding_root` use plain path calls and record
nothing. `infer_settings_path` probes with a plain `exists()`; the only row it can leave is the resolution
inside `external_memory_root`.

### Onboarding roots

- `mirror_onboarding_path(onboarding_root, source_file)` is `<root>/<normalized source path>.md`.
- `memory_worktree_enclosure(onboarding_root)` recognizes
  `<coordination root>/worktrees/<repository>/<group>/memory-<name>/onboarding` segment by segment and
  returns `(coordination root, repository name)`, or `None`.
- `infer_topology_from_onboarding_root` answers `external` for
  `<...>/memory-repos/ar-<name>/onboarding` and for a memory worktree of that shape. A root whose parent is
  `ar-memory` is refused as the removed mode. Every other root raises `ValueError` naming both supported
  shapes and the root received.
- `infer_settings_path` gives a memory worktree the official memory repository's `system/settings.md` when
  that file exists. Otherwise the answer is `system/settings.md` in the directory that holds the
  `onboarding` directory.
- `find_code_repository_root` accepts an existing absolute path or the direct child
  `<workspace root>/<name>`; anything else raises `ValueError`.

### Scalars

`clean_scalar` strips whitespace, one pair of backticks and one pair of quotes. `normalize_rel_path` turns
backslashes into slashes and strips surrounding slashes. `extract_yaml_blocks` returns the bodies of fenced
blocks that are marked `yaml`, `yml` or unmarked.

## Evidence

- The coordination root from a hint, the installed root or the sibling default. [2]
- The external memory root is a recorded resolution. [3]
- The settings file priority, with each probe recorded. [4]
- The two admitted settings locations and the refusal of the removed layout. [5]
- The memory worktree shape, matched segment by segment. [6]
- The settings path of an onboarding root. [7]
- The supported onboarding roots and the refusal that names both shapes. [8]
- The one-to-one card path. [9]
- An absent memory root, a retargeted root link and an equal-bytes retarget each recompute a kept view. [10]
- A higher-priority settings file that appears is a change of the recorded set. [11]
