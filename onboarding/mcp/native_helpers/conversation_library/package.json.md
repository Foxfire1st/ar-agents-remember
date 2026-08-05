# mcp/native_helpers/conversation_library/package.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/native_helpers/conversation_library/package.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-18T10:55+02:00 |
| lastVerifiedCommitHash |  `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060`|
| lastVerifiedCommitDate |  2026-08-05T12:41:24+02:00|
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

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The lock root repeats the same exact direct dependency and development-tool pins. | `lockfileVersion` | mcp/native_helpers/conversation_library/package-lock.json:4-4 |
| Protocol constants must match the manifest's two runtime dependencies. | "export const PROTOCOL_VERSION" | mcp/native_helpers/conversation_library/src/protocol.ts:13-13 |
| The foundation suite asserts the private flag and exact package/lock dependency tuple. | `test_helper_package_and_lock_select_only_the_exact_repository_dependencies` | mcp/tests/test_conversation_foundation.py:125-136 |

## Cross-Repo References

No neighboring workspace repository is involved.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-05T00:45:16+02:00 — 260731-EFA-L6 S18-B19 curator: replaced the `n/a` table rows with
  exact anchors and fixer-generated ranges; exact non-fixing check returns zero findings.

- 2026-07-18T10:55+02:00 — 260715-FEUI-L9 curator: created the exact helper-manifest sidecar.
  Verification is blank until closeout commits and stamps the new source.
