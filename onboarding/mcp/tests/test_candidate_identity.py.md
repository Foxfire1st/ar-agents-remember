# mcp/tests/test_candidate_identity.py

## Governing Overview

[Test suite](overview.md)

## Purpose

Exercise the candidate-identity resolver using disposable Git fixtures with a committed base. Stable clean input is compared with tracked, staged and untracked mutations; absent/nonrepository roots and failed reads remain unproven.

## Code Commentary

The cases check resolver return values, not an installed host or the complete task-document admission chain. Git/configuration and symlink changes stay inside test fixtures. The diagnostic-phrase regression supplies a real malformed Git configuration; its result must remain unproven rather than a special no-commit token. A repository without a HEAD also remains unproven.

### Invariants And Boundaries

- Failed HEAD, diff, status or untracked-content reads cannot become an equal candidate identity.
- Representation cases distinguish a link from an equal-content regular file, changed link target and changed executable bit. Missing-target links retain their own stable/distinct representation; unreadable regular content is the read-failure case.
- No universal binary/filter, concurrent-mutation or complete filesystem-identity proof is claimed by these assertions.

## Evidence

- Stable clean input and representative tracked, staged and untracked mutations. [1]
- Failed component reads, a real broken-configuration witness and an unborn HEAD yield unproven results. [2]

- The ruled representation cases distinguish link/regular kind, changed target and changed executable bit; missing-target links are stable but distinct by target. [3]
