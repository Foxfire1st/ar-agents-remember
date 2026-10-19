# mcp/src/agents_remember/canvas/__init__.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

Names the package's four decisions and points each at the module that owns it — the isolation policy, the admitted document and its channel, the narrow protocol, and the presenter. It re-exports nothing at import time, so reading the package cannot start work.

## Code Commentary

- The docstring maps each decision to one module, so a reader can find the refusing code instead of inferring it.
- Importing the package constructs nothing: no session, no policy read, no presenter.

## Evidence

- The package names its four decisions and the module that owns each. [1]
