# mcp/src/agents_remember/install/assets.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember-md                         |
| path                   | `mcp/src/agents_remember/install/assets.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-05-24T18:10+02:00                     |
| lastVerifiedCommitHash | `31846c1136f0fe75503a63fb557303a79fa022e8`                      |
| lastVerifiedCommitDate | 2026-05-24T23:07:31+02:00|
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
already have a concrete path.

### Invariants And Boundaries

- Normal runtime and benchmark asset discovery starts from package resources,
  not parent-directory scanning.
- The temporary extraction path belongs only to the context manager lifetime.
- `long_path()` is a concrete Windows path handling helper, not a fallback
  discovery route.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| Runtime install uses packaged assets unless tests pass an explicit source root. | [runtime.py](agents-remember-md/mcp/src/agents_remember/install/runtime.py) |
| Skill installation reads package-owned runtime skills through the shared asset root. | [skills.py](agents-remember-md/mcp/src/agents_remember/install/skills.py) |
| Benchmark tooling resolves packaged benchmark cases through the same package-data root. | [runner.py](agents-remember-md/mcp/src/agents_remember/benchmarks/runner.py) |

## Update History

- 2026-05-24T18:10+02:00: Created for F-10 package-data asset discovery; verification metadata must be refreshed after the code closeout commit exists.
