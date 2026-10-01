# mcp/tests/knowledge_index_test_support.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The index's design authority is the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the requirement
packet `MIK-R23@v1` of task `260928_maintained-invariant-knowledge`; both live outside the code and
memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The fixture writers and the converter.

- The two fixture kinds and the converter's limits. [1]
- The conforming-example tree. [2]
- The fixture converter and its head selection. [3]
- The store-authored parity database and the extra candidate claim. [4]

### Cross-Repo References

No meaningful cross-repo references found: the fixtures are written under the caller's `tmp_path`.

No cross-repo boundary is crossed by this file.
