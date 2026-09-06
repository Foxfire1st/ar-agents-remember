# mcp/tests/test_citation_deterministic_projection.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_citation_deterministic_projection.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-06T00:42:13+00:00 |
| lastVerifiedCommitHash | `709dd07671b07d85ac49eaf3b77f4609b1e5fc5f` |
| lastVerifiedCommitDate | 2026-09-04T00:53:17+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

CCR-R10 forcing fixtures for the deterministic anchor-to-range projection. Only exact unique
moves generate: the range is projected from the frozen source-index snapshot through the shared
oracle (`symbol_index.locate` / `Sightings.unique`), the claim is rewritten inside the
same byte-level edit transaction as an explicit generated no-content-impact Update History
bullet, and every projection binds snapshot id, prior claim digest, anchor, resolved extent, new
document digest, and repair-tool version. Multiple definitions, parsed mention-only anchors,
renames, deletions, stale snapshots, conflicting writes, and malformed claims refuse
deterministically and never accept the old range as a fallback. The module is standalone and
in-memory/on-tempdir: it never imports test-support or fixture modules.

## Code Commentary

### Logic

The module builds a two-root fixture (`Tree`, `test_citation_deterministic_projection.py:74-120)
holding a code repository and the memory onboarding tree it documents, with helpers to write
canonical cards carrying an optional Update History section (`document`,
`test_citation_deterministic_projection.py:59-67), to run the real fixer with an injected UTC
clock (`Tree.fix`, `test_citation_deterministic_projection.py:103-105), and to run the
range-resolution checker (`Tree.check`, `test_citation_deterministic_projection.py:107-108).
`TreeCase` (`test_citation_deterministic_projection.py:123-146) is the shared base.

The forcing groups then pin the seam:

- `UniqueMoveProjectionTests` (`test_citation_deterministic_projection.py:149-334):
  a unique move projects the range and binds every packet field
  (`test_a_unique_move_projects_the_range_and_binds_every_packet_field`,
  `test_citation_deterministic_projection.py:161-196); the history bullet is newest-first and
  parseable by the checker (`test_citation_deterministic_projection.py:198-216); dry runs stage
  but write nothing (`test_citation_deterministic_projection.py:218-228); a second run is a
  byte-for-byte no-op (`test_citation_deterministic_projection.py:230-241); identical inputs
  produce identical projection records (`test_citation_deterministic_projection.py:243-261); a
  document without an Update History section gets a bound projection but no invented bullet
  (`test_citation_deterministic_projection.py:263-277); multi-anchor claims bind every resolved
  extent (`test_citation_deterministic_projection.py:279-298); in-file tiebreaker moves and
  unparsed-language single-occurrence moves stay projectable
  (`test_citation_deterministic_projection.py:300-315; test_citation_deterministic_projection.py:317-334).
- `ProjectionRefusalTests` (`test_citation_deterministic_projection.py:337-433): renames,
  deletions, multiple definitions, parsed mention-only anchors, and malformed claims refuse
  without guessing; a stale snapshot refuses the whole run before any write
  (`test_citation_deterministic_projection.py:419-433).
- `TransactionSeamTests` (`test_citation_deterministic_projection.py:436-518): a
  conflicting write between plan and stage refuses the rewrite
  (`test_citation_deterministic_projection.py:439-478); the staged range edit and the history
  edit land in one document batch (`test_citation_deterministic_projection.py:480-518).
- `ProjectionBoundaryTests` (`test_citation_deterministic_projection.py:525-600): an
  anchor placed in two cited files and a repair with no matching extent decline the empty
  projection.
- `ProjectionDeclineThroughFixerTests` (`test_citation_deterministic_projection.py:603-637):
  a two-file anchor resolution stages the edit and refuses the projection through the real fixer.
- `StagingGuardTests` (`test_citation_deterministic_projection.py:640-704): a pre-existing
  run stamp is kept without reconsulting the clock; each document batch digest binds only its own
  projection.
- `ClockContractTests` (`test_citation_deterministic_projection.py:707-718): the
  injectable clock returns a UTC-aware instant.
- `ScopedNormalisationEditTests` (`test_citation_deterministic_projection.py:721-766): a
  normalised passing claim stages the edit and skips the projection.

### Conventions

Tests drive the real `fixer.fix_onboarding_root` with
`deterministic_projection.now_utc` patched to a fixed instant so replays are byte-for-byte;
refusal assertions read the exact decline codes.

### Invariants And Boundaries

- Only exact unique moves generate; every refusal is deterministic and never falls back to the old range.
- Range rewrites and their generated no-content-impact bullets share one document batch.
- No test-support or fixture-module imports, so the evidence-lifecycle catalog records no
  transitive test-support consumer here.

### Todos

None.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The canonical-card and two-root fixture builders shape every forcing scenario. | `document`; `Tree` | mcp/tests/test_citation_deterministic_projection.py:59-67; mcp/tests/test_citation_deterministic_projection.py:74-120 |
| Unique-move projection binds snapshot id, prior claim digest, resolved extents, digest, and version. | `test_a_unique_move_projects_the_range_and_binds_every_packet_field` | mcp/tests/test_citation_deterministic_projection.py:161-196 |
| Refusals are forced across rename, deletion, multiple-definition, mention-only, malformed, and stale-snapshot cases. | `ProjectionRefusalTests` | mcp/tests/test_citation_deterministic_projection.py:337-433 |
| The plan-then-stage seam refuses conflicting writes and batches the range and history edits. | `TransactionSeamTests` | mcp/tests/test_citation_deterministic_projection.py:436-518 |
| The real fixer stages the edit and refuses the projection for two-file anchor resolutions. | `ProjectionDeclineThroughFixerTests` | mcp/tests/test_citation_deterministic_projection.py:603-637 |
| The run stamp and per-document digest guards hold across a full fixer run. | `StagingGuardTests` | mcp/tests/test_citation_deterministic_projection.py:640-704 |
| The suite is registered in the integration lane of the evidence manifest. | "mcp/tests/test_citation_deterministic_projection.py" | mcp/tests/test-evidence-lanes.toml:251-251 |

## Update History

- 2026-09-06T00:42:13+00:00 — Gate-5 citation repair: re-read the cited evidence-lane member and its declared classification and corrected its incoming range. Existing source verification provenance is retained.

- 2026-09-05T06:39:59+00:00 — L31 scoped citation curation against frozen ea359649: repaired anchor grammar and exact source coordinates while preserving the current behavioral claims. No content impact; source verification metadata was not advanced.

- 2026-09-04T01:15+02:00 - 260831-CCR-L10 Gate-5 memory pass: created this file-level
  onboarding card for the new CCR-R10 deterministic anchor-range projection forcing suite
  delivered in code commit 709dd076; anchors and ranges derived from the current worktree source
  and pinned to that commit. The suite entered the `integration` lane of
  `test-evidence-lanes.toml` in the same change.
