# mcp/tests/knowledge_index_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_index_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T08:01:17+02:00 |
| lastVerifiedCommitHash | `ffd043f1354e94a7dcf435e10b4b7224495cbcba`|
| lastVerifiedCommitDate | 2026-09-29T08:30:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**Fixture memory trees for the derived knowledge index (MIK-R23).** `write_review_tree` writes a converted memory tree directly in the MIK-R21/R07 file formats — the packet's conforming example: a family whose members are realized across four files, one of them `dashboard/src/data/review.ts`, with a test proof, a decision and an incident linking to an invariant, a route sidecar citing it, and a closed history file with rows about it. `convert_dataset` is a *fixture converter*: it reads a legacy knowledge database and writes the head revision of every invariant and family, and every realization claim on a head revision, as record files and file sidecars.

## Code Commentary

### Logic

- Constants name the fixture's paths and IDs (`REVIEW_PATH`, `SIBLING_PATHS`, `TEST_PATH`, `REVIEW_INVARIANT`, `FAMILY`, `DECISION`, `INCIDENT`, `LEAF`, …); `anchor`, `write_document`, `git`, `init_repository` and `commit_all` are the shared helpers.
- `convert_dataset(database_path, destination)` writes the layout marker and converts heads (`_heads`, which refuses a lineage with several heads), mapping legacy locators with `_new_locator` and returning the legacy-ID → text-ID map.
- `build_parity_dataset` authors a store database through the shipped writers (`P→I`, `F{I,J}`, `G{J,K}`, `H{I,L}`, six claims over five paths); `add_parity_claim` adds one claim for the candidate-changed parity case.

### Conventions

- Test support only; it is imported by the three index test modules.

### Invariants And Boundaries

- **It is not the MIK-R24 conversion**, which owns the real export, anchors' content identities, onboarding and the layout version. Its anchors carry the recorded blob and a content identity derived from the recorded locator, not from code; it exists so parity tests and the timing measurement could run before L24, as the packet allows.

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The fixture writers and the converter.

| Finding | Anchor | Source |
| --- | --- | --- |
| The two fixture kinds and the converter's limits. | "It is not the MIK-R24 conversion" | mcp/tests/knowledge_index_test_support.py:1-15 |
| The conforming-example tree. | `write_review_tree`; `REVIEW_PATH`; `FAMILY` | mcp/tests/knowledge_index_test_support.py:144-339; mcp/tests/knowledge_index_test_support.py:37-37; mcp/tests/knowledge_index_test_support.py:48-48 |
| The fixture converter and its head selection. | `convert_dataset`; `_convert`; `_heads`; `_convert_realizations` | mcp/tests/knowledge_index_test_support.py:377-384; mcp/tests/knowledge_index_test_support.py:387-449; mcp/tests/knowledge_index_test_support.py:347-361; mcp/tests/knowledge_index_test_support.py:452-488 |
| The store-authored parity database and the extra candidate claim. | `build_parity_dataset`; `add_parity_claim` | mcp/tests/knowledge_index_test_support.py:504-683; mcp/tests/knowledge_index_test_support.py:686-745 |

## Cross-Repo References

No meaningful cross-repo references found: the fixtures are written under the caller's `tmp_path`.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): created this card for the new file MIK-R23 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
