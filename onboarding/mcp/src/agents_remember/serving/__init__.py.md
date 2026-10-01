# mcp/src/agents_remember/serving/__init__.py

## Governing Overview

[overview.md](overview.md)

## Purpose

`serving/__init__.py` marks the dashboard serving package. It is a docstring only — it
exports nothing — so that `serving.delta` and `serving.projector` stay importable without
pulling in FastAPI (only `app` and `static` import the web stack).

## Code Commentary

No runtime code beyond the module docstring and `from __future__ import annotations`. The
package's surface is reached through its submodules (`app.create_app`, `projector.Projector`,
`delta.diff_projection`, `static.mount_static`).

## Invariants And Boundaries

- Keep this import-free: importing the package must not import FastAPI, so the pure modules
  (`delta`, `projector`) remain testable and importable on their own.

## Evidence

### Repo-Internal References

- The serving route overview. [1]
