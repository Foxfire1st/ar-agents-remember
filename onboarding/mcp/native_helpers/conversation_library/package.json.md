# mcp/native_helpers/conversation_library/package.json

## Governing Overview

[Locked native conversation-library helper overview](overview.md)

## Purpose

Declares the private repository-owned helper package, its supported Node floor, its verification
commands, and the exact direct Claude/Pi native-library dependency versions.

## Code Commentary

### Logic

Marks the package private and ESM, requires Node 20+, exposes strict typecheck/test scripts, pins
Claude Agent SDK 0.3.207 and Pi Coding Agent 0.80.7 without ranges, and pins the development tools.

### Conventions

All version strings are exact. Changes must keep the lockfile and protocol constants aligned.

### Invariants And Boundaries

- Never publish this package.
- Never replace exact dependencies with ranges or ambient resolution.
- Dependency selection alone does not enable a history capability.

### Todos

None; operation behavior is intentionally outside the manifest.

## Evidence

### Docs References

No Domain Documentation source is configured; the manifest and lock are the direct version truth.

No configured domain documentation was available.

### Repo-Internal References

- The lock root repeats the same exact direct dependency and development-tool pins. [1]
- Protocol constants must match the manifest's two runtime dependencies. [2]

### Cross-Repo References

No neighboring workspace repository is involved.

No meaningful cross-repo references found.
