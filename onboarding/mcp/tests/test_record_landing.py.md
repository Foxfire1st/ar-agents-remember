# mcp/tests/test_record_landing.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_record_landing.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T19:00+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
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

`_fixture(root)` cit:([`_fixture`], mcp/tests/test_record_landing.py:44-65) creates a real Git
repository with `main`, `super`, and `ar/master`, then builds a series contract over it with
`memory_mode="disabled"` — so no memory repository is needed and the route's own logic is what is
under test. `_commit_on` cit:([`_commit_on`], mcp/tests/test_record_landing.py:68-73) commits on a
named branch and returns the resulting SHA, which is what the route records. `_record`
cit:([`_record`], mcp/tests/test_record_landing.py:76-89) is the approved-call shorthand; it is
explicitly typed rather than `**over: object`, which would erase the argument types the route
validates.

`RecordLandingTests` cit:([`RecordLandingTests`], mcp/tests/test_record_landing.py:92-195) holds seven
cases:

- `test_landed_commit_sets_the_terminal_integration_cell` cit:(["test_landed_commit_sets_the_terminal_integration_cell"], mcp/tests/test_record_landing.py:93-93)
  — the happy path; asserts the stored contract reads `completed`, carries the `pr` strategy label,
  and holds the exact landed commit.
- `test_commit_that_landed_nowhere_is_refused` cit:(["test_commit_that_landed_nowhere_is_refused"], mcp/tests/test_record_landing.py:106-106)
  — commits on a side branch that is not merged into either landing target and asserts the refusal
  message plus an untouched `not-started` cell. This is the anti-fabrication guard.
- `test_recording_requires_approval` cit:(["test_recording_requires_approval"], mcp/tests/test_record_landing.py:124-124)
  — an unapproved, non-dry-run call raises before any write.
- `test_a_missing_commit_argument_is_refused` cit:(["test_a_missing_commit_argument_is_refused"], mcp/tests/test_record_landing.py:136-136)
  — the route cannot be invoked without naming the commit that landed.
- `test_dry_run_records_nothing` cit:(["test_dry_run_records_nothing"], mcp/tests/test_record_landing.py:145-145)
  — reports `would-record` and leaves the cell `not-started`.
- `test_recording_twice_is_idempotent` cit:(["test_recording_twice_is_idempotent"], mcp/tests/test_record_landing.py:163-163)
  — a repeat reports `already-recorded` rather than writing again.
- `test_a_checkpointed_series_is_not_upgraded_into_a_reclaimable_integration` cit:(["test_a_checkpointed_series_is_not_upgraded_into_a_reclaimable_integration"], mcp/tests/test_record_landing.py:173-173)
  — 260831-LOCR-L30 follow-up: with the contract set to `checkpointed`, the route reports
  `already-recorded` and both stored cells keep the values the checkpoint wrote. It exists because the
  full-record path writes `completed` + `cleanup="pending"`, the exact state `worktree_cleanup`
  requires, so taking it would have made an open series reclaimable.

### Conventions

The suite is a unittest class, matching the surrounding `mcp/tests` convention, and the cases run in
the ordinary unit population: the route avoids `status_payload`, so no bound worktree services are
needed and no `@pytest.mark.integration` marker is required.

`_git` cit:([`_git`], mcp/tests/test_record_landing.py:33-41) passes the identity via `-c` flags
rather than relying on repository or global Git configuration, so the fixture works on a machine with
no configured user.

### Invariants And Boundaries

- **Keep the fixture self-contained.** Importing `test_source_lineage` drags in its transitive support
  closure, which then has to be declared as a consumer for four artifacts in
  `mcp/tests/evidence-lifecycle.toml`; this suite avoids that coupling on purpose. If a future case
  genuinely needs the shared lineage fixture, that declaration is the price and it must be added in
  the same change.
- **The refusals are the point, not incidental coverage.** Each failure case protects a distinct way
  the terminal cell could be set wrongly or prematurely — including the newest one, which protects the
  cell from being *over*written on a checkpointed series.
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
| The route under test: approval gate, landing targets, ancestry refusal, dry run. | `record_landing_result` | mcp/src/agents_remember/worktrees/modules/record_landing.py:58-142 |
| The widened `already-recorded` guard the new case pins: a checkpointed series is not upgraded into a reclaimable integration. | "contract.integration_status in {\"completed\", \"checkpointed\"}" | mcp/src/agents_remember/worktrees/modules/record_landing.py:70-70 |
| The shared writer whose cell the happy path asserts, now taking the bundled `LandedIntegration` record (260831-LOCR-L30). | `record_landed_integration` | mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66 |
| The contract fields the recorded commits land in. | `integration_strategy`; `integrated_code_commit` | mcp/src/agents_remember/worktrees/worktree_contract.py:264-265 |
| The consumer-side guard that reads the cell this route sets. | "integration_status != \"completed\"" | mcp/src/agents_remember/worktrees/modules/cleanup.py:677-677 |
| The artifact catalog entry (one of the four whose consumer list already names the shared lineage fixture) that would have to gain this file as a consumer if the fixture were shared. | "mcp/tests/fixtures/repository_profiles/node/package.json" | mcp/tests/evidence-lifecycle.toml:621-621 |

## Cross-Repo References

These are in-process contract assertions against a fixture repository created in a temporary
directory; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: "mcp/tests/fixtures/repository_profiles/node/package.json" repointed to mcp/tests/evidence-lifecycle.toml:621-621. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T15:12:32+00:00: Generated citation repair: "mcp/tests/fixtures/repository_profiles/node/package.json" repointed to mcp/tests/evidence-lifecycle.toml:620-620. No content impact: mechanical anchor-range projection bound to citation source snapshot 418f5ce580b3710b5d8fe417585d48fd22eccd55346c84b05f01fef243a17917; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T06:05+02:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/evidence-lifecycle.toml:561-561` -> `mcp/tests/evidence-lifecycle.toml:562-562`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `record_landing_result` repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:58-142. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `record_landed_integration` repointed to mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `integration_strategy`; `integrated_code_commit` repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:264-264; mcp/src/agents_remember/worktrees/worktree_contract.py:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "integration_status != \"completed\"" repointed to mcp/src/agents_remember/worktrees/modules/cleanup.py:677-677. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/fixtures/repository_profiles/node/package.json" repointed to mcp/tests/evidence-lifecycle.toml:565-565. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T08:11:27+00:00 — 260915-KS-L9 curator (memory-quality closure): re-read every reopened claim in this card against code commit `c22beb0121946c0637e113ec4cf29da29fd4aec7` and advanced the verification stamp to that commit, which closeout re-stamps. A generated citation repair had already rewritten these ranges mechanically, so each was re-read rather than trusted: the range was checked against the current definition of the construct the claim is about, and the wording still holds. Extents chosen: `record_landing_result` at mcp/src/agents_remember/worktrees/modules/record_landing.py:58-142, `record_landed_integration` at mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `record_landing_result` repointed to mcp/src/agents_remember/worktrees/modules/record_landing.py:58-142. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `record_landed_integration` repointed to mcp/src/agents_remember/worktrees/modules/landing_record.py:36-66. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: `integration_strategy`; `integrated_code_commit` repointed to mcp/src/agents_remember/worktrees/worktree_contract.py:259-259; mcp/src/agents_remember/worktrees/worktree_contract.py:260-260. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "integration_status != \"completed\"" repointed to mcp/src/agents_remember/worktrees/modules/cleanup.py:677-677. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T06:49:47+00:00: Generated citation repair: "mcp/tests/fixtures/repository_profiles/node/package.json" repointed to mcp/tests/evidence-lifecycle.toml:561-561. No content impact: mechanical anchor-range projection bound to citation source snapshot 3fa9290dfd218ae31f16951129eb57f6acdf1a92ecb95026b64d55227e9f1ad6; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T03:31:11+02:00 — 260915-KS-L9 curator (re-scoped repair): re-read the reopened claim in the row 104 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances; re-read the reopened claim in the row 102 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances
- 2026-09-14T19:00+02:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 1
  claim(s) whose anchor no longer sat in its cited range and normalised 5 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.
- 2026-09-14T15:05+02:00 — No content impact: mechanical citation re-derivation after the
  260913-LCA-L8 change set added one import line to `worktrees/modules/cleanup.py`, shifting the
  `integration_status != "completed"` guard from line 664 to 665. The anchor was re-read at
  `cleanup.py:665-665`, where that expression still sits; the cited construct and its meaning are
  unchanged.
- 2026-09-12T04:10+02:00 — 260831-LOCR-L30 follow-up: added
  `test_a_checkpointed_series_is_not_upgraded_into_a_reclaimable_integration` (the suite now holds
  seven cases), recorded what it pins and why, added the guard's reference row, and re-derived every
  range shifted by the new `from dataclasses import replace` import and the appended case. Verification
  metadata remains closeout-owned; no acceptance claim.
- 2026-09-12T02:50+02:00 — 260831-LOCR-L30 checkpoint landing: re-derived the two source ranges this card cites
  (the route moved to 58-131 and the shared writer to 37-68 after the writer gained `LandedIntegration`
  and the `checkpoint` flag). No behavior this card documents changed. Verification metadata remains
  closeout-owned.
- 2026-09-11T23:05:00+00:00: The consumer-side guard cited the bare backticked expression `integration_status != "completed"`, which is not an anchor, and the catalog row cited `[[artifact]]` with a rangeless Source; both now use double-quoted literal anchors -- the exact guard expression at cleanup.py:664 and one of the four lineage-consumer artifact entries in mcp/tests/evidence-lifecycle.toml -- because `[[artifact]]` resolves many times in that file and no single target could be chosen.

- 2026-09-12T00:33+02:00 — Created by the LOCR-L29 curator pass. Documents the six cases, the
  deliberate self-contained fixture and the evidence-catalog cost that sharing `test_source_lineage`
  would incur, and why these cases run in the unit population. Verification metadata is pinned to the
  leaf base commit and remains closeout-owned.
