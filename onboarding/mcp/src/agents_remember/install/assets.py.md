# mcp/src/agents_remember/install/assets.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/install/assets.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-06T22:15:27+00:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675`                      |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`install/assets.py` is the shared package-data access layer for runtime and
benchmark assets. It gives installers and benchmark services a package-owned
source root instead of making normal execution depend on a source checkout
layout.

## Code Commentary

`long_path` returns the input unchanged outside Windows, preserves an existing extended prefix, and translates UNC paths to the extended UNC form. With resolution disabled it only makes relative paths absolute. `copy_traversable_tree` requires a directory root, recursively creates directories and copies file bytes; extraction lifetime stays with packaged_source_root. cit:([`long_path`, `copy_traversable_tree`], mcp/src/agents_remember/install/assets.py:17-32; mcp/src/agents_remember/install/assets.py:50-62).

### Logic

`packaged_source_root()` resolves `agents_remember/package_data` through
`importlib.resources`. Filesystem-backed installs yield the package-data path
directly. Non-filesystem resources are copied into a temporary directory for the
context lifetime so callers still receive a concrete `Path` for recursive copy
and benchmark discovery code.

`long_path()` normalizes concrete Windows filesystem paths to the extended path
form when needed by recursive copy operations. It is used only after callers
already have a concrete path. By default it resolves the path (`resolve=True`);
callers can pass `resolve=False` to skip symlink resolution and instead absolutize
a relative path against the current working directory before applying the prefix.

### Invariants And Boundaries

- Normal runtime and benchmark asset discovery starts from package resources,
  not parent-directory scanning.
- The temporary extraction path belongs only to the context manager lifetime.
- `long_path()` is a concrete Windows path handling helper, not a fallback
  discovery route.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Runtime install uses packaged assets unless tests pass an explicit source root. | `install_runtime_from_config`; "if request.source_root is None"; "packaged_source_root() if request.source_root is None" | mcp/src/agents_remember/install/runtime.py:829-855 |
| Skill installation reads package-owned runtime skills through the shared asset root. | `install_skills`; `packaged_source_root`; `skills_root` | mcp/src/agents_remember/install/skills.py:58-106; mcp/src/agents_remember/install/skills.py:72-73 |
| Benchmark tooling resolves packaged benchmark cases through the same package-data root. | `benchmark_root_context`; `packaged_source_root` | mcp/src/agents_remember/benchmarks/runner_modules/roots.py:10-17 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-06T22:15:27+00:00 — Preserved actual asset/context semantics from retired test onboarding; verification pins unchanged.

- 2026-08-11T15:20+02:00 — Re-anchored runtime asset selection to the exact application entry
  point, explicit-source branch, and packaged-source branch.
- 2026-08-03T10:10+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 6 assigned citation findings (3 missing anchors and 3 malformed sources), including a source-duplication normalization; final scoped check is clean.

- 2026-05-31T12:30+02:00 — Documented new `long_path()` `resolve=False` mode that absolutizes relative paths against cwd without resolving symlinks (1.0.0 review remediation).
- 2026-05-24T18:10+02:00: Created for F-10 package-data asset discovery; verification metadata must be refreshed after the code closeout commit exists.
