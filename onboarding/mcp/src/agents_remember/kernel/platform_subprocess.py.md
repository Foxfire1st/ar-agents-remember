# mcp/src/agents_remember/kernel/platform_subprocess.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/platform_subprocess.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-12T15:19+02:00 |
| lastVerifiedCommitHash |  `1580f92715ff93c988f9a15439ad9bec60ef4c5d`|
| lastVerifiedCommitDate |  2026-08-13T00:18:59+02:00|
| governingOverview | `../../../overview.md` |

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

## Docs References

No external Domain Documentation source is configured for this platform boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external document is required to prove the repository's fail-closed policy. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Interop classification covers path syntax, mounted filesystems, executable suffixes, and resolved paths. | `windows_interop_reason` | mcp/src/agents_remember/kernel/platform_subprocess.py:11-36 |
| Environment and command construction refuse non-native execution inputs. | `native_subprocess_environment` | mcp/src/agents_remember/kernel/platform_subprocess.py:39-111 |

## Cross-Repo References

This is an operating-system boundary rather than a sibling-repository integration.

| Finding | Anchor | Source |
| --- | --- | --- |
| The boundary prevents a Linux process from crossing into Windows tools or storage. | `windows_interop_reason`; `resolve_native_executable` | mcp/src/agents_remember/kernel/platform_subprocess.py:16-36; mcp/src/agents_remember/kernel/platform_subprocess.py:81-111 |

## Update History

- 2026-08-12T15:19+02:00 — Created for L23's deterministic WSL/UNC subprocess refusal; verification provenance remains closeout-owned.
