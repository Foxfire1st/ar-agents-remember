# mcp/src/agents_remember/install/assets.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/install/assets.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-31T12:30+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`                      |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

## Purpose

`install/assets.py` is the shared package-data access layer for runtime and
benchmark assets. It gives installers and benchmark services a package-owned
source root instead of making normal execution depend on a source checkout
layout.

## Code Commentary

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
| Runtime install uses packaged assets unless tests pass an explicit source root. | `install_runtime_from_config`; `packaged_source_root`; `source_root` | mcp/src/agents_remember/install/runtime.py:556-582 |
| Skill installation reads package-owned runtime skills through the shared asset root. | `install_skills`; `packaged_source_root`; `skills_root` | mcp/src/agents_remember/install/skills.py:58-106; mcp/src/agents_remember/install/skills.py:72-73 |
| Benchmark tooling resolves packaged benchmark cases through the same package-data root. | `benchmark_root_context`; `packaged_source_root` | mcp/src/agents_remember/benchmarks/runner_modules/roots.py:10-17 |

## Update History

- 2026-08-03T10:10+02:00 — 260731-EFA-L6 W3-B07 curator: repaired all 6 assigned citation findings (3 missing anchors and 3 malformed sources), including a source-duplication normalization; final scoped check is clean.

- 2026-05-31T12:30+02:00 — Documented new `long_path()` `resolve=False` mode that absolutizes relative paths against cwd without resolving symlinks (1.0.0 review remediation).
- 2026-05-24T18:10+02:00: Created for F-10 package-data asset discovery; verification metadata must be refreshed after the code closeout commit exists.
