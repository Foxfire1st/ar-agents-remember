# mcp/src/agents_remember/install/assets.py

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

## Evidence

### Repo-Internal References

- Runtime install uses packaged assets unless tests pass an explicit source root. [1]
- Skill installation reads package-owned runtime skills through the shared asset root. [2]
- Benchmark tooling resolves packaged benchmark cases through the same package-data root. [3]
