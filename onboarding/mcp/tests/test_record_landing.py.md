# mcp/tests/test_record_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_record_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-12T00:33+02:00 |
| lastVerifiedCommitHash | `3b552f5a215648274dc5e6e4d5f0a01c2ee80be2` |
| lastVerifiedCommitDate | 2026-09-12T01:54:48+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

Locks the pull-request landing route and the three ways it must refuse. A recording that succeeds
sets the terminal integration cell; a commit that landed nowhere, an unapproved call, and a missing
commit argument each fail without writing the cell. The suite is deliberately self-contained: it
builds its own minimal series contract and Git repository rather than importing the shared
`test_source_lineage` fixture, so this card is owned by the module it exercises instead of inheriting
that suite's whole transitive support closure.

## Code Commentary

### Logic

`_fixture(root)` cit:([`_fixture`], mcp/tests/test_record_landing.py:43-43) creates a real Git
repository with `main`, `super`, and `ar/master`, then builds a series contract over it with
`memory_mode="disabled"` — so no memory repository is needed and the route's own logic is what is
under test. `_commit_on` cit:([`_commit_on`], mcp/tests/test_record_landing.py:67-67) commits on a
named branch and returns the resulting SHA, which is what the route records. `_record`
cit:([`_record`], mcp/tests/test_record_landing.py:75-75) is the approved-call shorthand; it is
explicitly typed rather than `**over: object`, which would erase the argument types the route
validates.

`RecordLandingTests` cit:([`RecordLandingTests`], mcp/tests/test_record_landing.py:91-91) holds six
cases:

- `test_landed_commit_sets_the_terminal_integration_cell` cit:(["test_landed_commit_sets_the_terminal_integration_cell"], mcp/tests/test_record_landing.py:92-92)
  — the happy path; asserts the stored contract reads `completed`, carries the `pr` strategy label,
  and holds the exact landed commit.
- `test_commit_that_landed_nowhere_is_refused` cit:(["test_commit_that_landed_nowhere_is_refused"], mcp/tests/test_record_landing.py:105-105)
  — commits on a side branch that is not merged into either landing target and asserts the refusal
  message plus an untouched `not-started` cell. This is the anti-fabrication guard.
- `test_recording_requires_approval` cit:(["test_recording_requires_approval"], mcp/tests/test_record_landing.py:123-123)
  — an unapproved, non-dry-run call raises before any write.
- `test_a_missing_commit_argument_is_refused` cit:(["test_a_missing_commit_argument_is_refused"], mcp/tests/test_record_landing.py:135-135)
  — the route cannot be invoked without naming the commit that landed.
- `test_dry_run_records_nothing` cit:(["test_dry_run_records_nothing"], mcp/tests/test_record_landing.py:144-144)
  — reports `would-record` and leaves the cell `not-started`.
- `test_recording_twice_is_idempotent` cit:(["test_recording_twice_is_idempotent"], mcp/tests/test_record_landing.py:162-162)
  — a repeat reports `already-recorded` rather than writing again.

### Conventions

The suite is a unittest class, matching the surrounding `mcp/tests` convention, and the cases run in
the ordinary unit population: the route avoids `status_payload`, so no bound worktree services are
needed and no `@pytest.mark.integration` marker is required.

`_git` cit:([`_git`], mcp/tests/test_record_landing.py:32-32) passes the identity via `-c` flags
rather than relying on repository or global Git configuration, so the fixture works on a machine with
no configured user.

### Invariants And Boundaries

- **Keep the fixture self-contained.** Importing `test_source_lineage` drags in its transitive support
  closure, which then has to be declared as a consumer for four artifacts in
  `mcp/tests/evidence-lifecycle.toml`; this suite avoids that coupling on purpose. If a future case
  genuinely needs the shared lineage fixture, that declaration is the price and it must be added in
  the same change.
- **The refusals are the point, not incidental coverage.** Each of the three failure cases protects a
  distinct way the terminal cell could be set wrongly or prematurely.
- **Assert the stored contract, not only the payload.** A payload state can be right while the write
  was skipped or duplicated; the cases reload the contract to check the durable result.

### Todos

None.

## Docs References

No external Domain Documentation source is configured for this memory repo, and these assertions
concern this repository's own contract write, so the retained source is the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The route under test: approval gate, landing targets, ancestry refusal, dry run. | `record_landing_result` | mcp/src/agents_remember/worktrees/modules/record_landing.py:55-117 |
| The shared writer whose cell the happy path asserts. | `record_landed_integration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:27-47 |
| The contract fields the recorded commits land in. | `integration_strategy`; `integrated_code_commit` | mcp/src/agents_remember/worktrees/worktree_contract.py:260-263 |
| The consumer-side guard that reads the cell this route sets. | "integration_status != \"completed\"" | mcp/src/agents_remember/worktrees/modules/cleanup.py:664-664 |
| The artifact catalog entry (one of the four whose consumer list already names the shared lineage fixture) that would have to gain this file as a consumer if the fixture were shared. | "mcp/tests/fixtures/repository_profiles/node/package.json" | mcp/tests/evidence-lifecycle.toml:551-582 |

## Cross-Repo References

These are in-process contract assertions against a fixture repository created in a temporary
directory; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-11T23:05:00+00:00: The consumer-side guard cited the bare backticked expression `integration_status != "completed"`, which is not an anchor, and the catalog row cited `[[artifact]]` with a rangeless Source; both now use double-quoted literal anchors -- the exact guard expression at cleanup.py:664 and one of the four lineage-consumer artifact entries in mcp/tests/evidence-lifecycle.toml -- because `[[artifact]]` resolves many times in that file and no single target could be chosen.

- 2026-09-12T00:33+02:00 — Created by the LOCR-L29 curator pass. Documents the six cases, the
  deliberate self-contained fixture and the evidence-catalog cost that sharing `test_source_lineage`
  would incur, and why these cases run in the unit population. Verification metadata is pinned to the
  leaf base commit and remains closeout-owned.
