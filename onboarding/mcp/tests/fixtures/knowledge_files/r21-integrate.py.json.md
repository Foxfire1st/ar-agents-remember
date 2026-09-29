# mcp/tests/fixtures/knowledge_files/r21-integrate.py.json

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/fixtures/knowledge_files/r21-integrate.py.json` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T04:55:39+02:00 |
| lastVerifiedCommitHash | `45fe37749b388de348d16ced50c28c03490dce64`|
| lastVerifiedCommitDate | 2026-09-29T05:18:17+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[mcp/tests overview](../../overview.md)

## Purpose

**MIK-R21's own file-sidecar example, encoded in MIK-R21's normative shape.** The file holds a file sidecar for `worktrees/modules/integrate.py` with one `primary-authority` realization (`RLZ-4E1C9A`). It is
read by `test_doc14_worked_examples_validate_and_round_trip_byte_for_byte`, which requires it to
parse as `FileSidecar` and to re-serialize to exactly these bytes.

## Code Commentary

### Logic

A canonical JSON document (`schema: ar-onboarding-file/v1`): sorted keys, two-space indentation, one trailing
newline — the output of `agents-remember knowledge-format` on itself.

### Conventions

Test data only; never imported by production code. Recorded `blob` values are the real blobs at base
`b7ef73f8`; `content` hashes are illustrative.

### Invariants And Boundaries

- The file must stay canonical: any hand edit must be followed by `agents-remember knowledge-format`
  or the round-trip case fails.
- The fixture set is closed: the test asserts the directory holds exactly the nine names it lists.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R21@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The fixture is consumed by one test case.

| Finding | Anchor | Source |
| --- | --- | --- |
| The fixture names its schema. | "ar-onboarding-file/v1" | mcp/tests/fixtures/knowledge_files/r21-integrate.py.json:20-20 |
| Its distinguishing identity. | "RLZ-4E1C9A" | mcp/tests/fixtures/knowledge_files/r21-integrate.py.json:13-13 |
| The test maps this file to its model. | "r21-integrate.py.json" | mcp/tests/test_knowledge_file_formats.py:126-126 |

## Cross-Repo References

No meaningful cross-repo references found: the fixture names paths of this repository only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is represented. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
