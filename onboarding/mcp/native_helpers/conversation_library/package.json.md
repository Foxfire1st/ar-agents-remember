# mcp/native_helpers/conversation_library/package.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/package.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `91e1f59b5eb7d9a88c8fd59dca1c996abcb2ed1b`|
| lastVerifiedCommitDate |  2026-07-18T11:10:09+02:00|
| governingOverview | `overview.md` |

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

## Docs References

No Domain Documentation source is configured; the manifest and lock are the direct version truth.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The lock root repeats the same exact direct dependency and development-tool pins. | L1-L21 | [package-lock.json](agents-remember/mcp/native_helpers/conversation_library/package-lock.json) |
| Protocol constants must match the manifest's two runtime dependencies. | L1-L7; L92-L118 | [protocol.ts](agents-remember/mcp/native_helpers/conversation_library/src/protocol.ts) |
| The foundation suite asserts the private flag and exact package/lock dependency tuple. | L63-L77 | [test_conversation_foundation.py](agents-remember/mcp/tests/test_conversation_foundation.py) |

## Cross-Repo References

No neighboring workspace repository is involved.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the exact helper-manifest sidecar.
  Verification is blank until closeout commits and stamps the new source.
