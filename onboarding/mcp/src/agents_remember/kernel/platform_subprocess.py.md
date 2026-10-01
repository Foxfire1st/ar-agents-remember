# mcp/src/agents_remember/kernel/platform_subprocess.py

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

This kernel module is the fail-closed POSIX subprocess boundary for WSL-hosted automation. It classifies Windows paths and shims, sanitizes inherited PATH and temp state, resolves a native executable explicitly, and refuses cross-OS execution instead of guessing.

## Code Commentary

### Logic

`windows_interop_reason` recognizes UNC, drive, mounted-Windows, Windows-suffix, and resolved-symlink cases. `native_subprocess_environment` combines a native-only PATH with enclosure-selected POSIX scratch. `resolve_native_executable` and `native_command` make the actual program path explicit before process launch.

### Conventions

Callers pass an environment and receive a normalized copy. Native Windows is preserved unchanged because interop rejection applies only to POSIX runners.

### Invariants And Boundaries

- WSL must not execute `.exe`, `.cmd`, `.bat`, or `.com` shims or use mounted-Windows scratch.
- An empty native PATH and an unresolved executable are hard errors.
- The module selects process compatibility, not product policy or fallback behavior.

### Todos

None.

## Evidence

### Docs References

No external Domain Documentation source is configured for this platform boundary.

No configured external document is required to prove the repository's fail-closed policy.

### Repo-Internal References

- Interop classification covers path syntax, mounted filesystems, executable suffixes, and resolved paths. [1]
- Environment and command construction refuse non-native execution inputs. [2]

### Cross-Repo References

This is an operating-system boundary rather than a sibling-repository integration.

- The boundary prevents a Linux process from crossing into Windows tools or storage. [3]
