# mcp/tests/test_user_settings_guard.py

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

Protect the shared support's refusal of the user's real settings path without writing any real account. The cases use made-up homes/account-database answers and pytest's existing configuration isolation.

## Code Commentary

The guard cases require a named temporary-XDG remedy, no filesystem creation, moved-folder admission, and truthful fallback provenance. The world case starts a real child with a fake account and no XDG setting. Its explicit `PYTHONPATH` selects this worktree's tests, product source and test support; the child prints its world source and the parent asserts that source, nonzero exit, the guard's error and an empty fake-home tree.

The static scanner recursively enumerates non-`test_*.py` Python modules under `mcp/tests` (except the guard) and every Python module under `mcp/test_support`. It recognizes raw product resolver calls, from-import aliases, attribute-form resolver calls, and literal path rebuilds joining all three settings markers through `/`, `join` or `joinpath`. Guarded calls and guard import aliases pass. Controls parse synthetic modules; they never execute those writes.

## Boundaries

The scanner is a finite syntactic guard, not arbitrary Python data-flow analysis or proof against every dynamically constructed path. New and nested modules join its population without a handwritten module list. The world child is a bounded behavior proof on a fake account, not an installed-host, Windows, full-suite or Dagger certificate. Existing conftest isolation and existing test assertions are unchanged.

## Evidence

- The guard refuses a made-up real path, permits moved XDG, and creates nothing. [1]
- Unreadable-database cases check comparison and truthful observed-home reporting. [2]
- The child executes the reviewed world source, refuses, and leaves the fake home empty. [3]
- The recursive population and syntactic checker hold the shared-support boundary. [4]
- Direct, imported-alias and literal rebuild controls fail, while guarded controls pass. [5]
