# mcp/tests/knowledge_validator_test_support.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/knowledge_validator_test_support.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T00:17:15+02:00 |
| lastVerifiedCommitHash | `c493b55731545a090d6b81f504bf02e1e427ec74`|
| lastVerifiedCommitDate | 2026-09-30T00:38:11+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[tests route overview](overview.md)

## Purpose

**Builds the converted fixture memory tree the MIK-R22 validator tests start from.** `fixture_tree_files()` assembles the MIK-R21 Doc14 §4 fixtures (`fixtures/knowledge_files`) into one converted tree: the layout marker; the invariant, family, decision and incident records; and the file and route sidecars of `direct_landing.py`, its test, `integrate.py` and the `worktrees` route, each beside its Markdown card. Since MIK-R04 (leaf 260928-MIK-L04) it also carries the other four realizations of the Doc14 §4.2 family, so the family's three routes satisfy Coverage and Non-empty. It is a helper module, not a test module (no `test_` prefix).

## Code Commentary

### Logic

- It adds the two invariants the fixtures name but do not define (`INV-R8M2TD`, `INV-C0VR4G`), so the tree is whole. Since MIK-R27 (leaf 260928-MIK-L27) they carry `UNCHECKED_ADMISSION`, a `prevents_costly_mistake` claim with a prose justification: they have no realization or proof of their own, so the Doc14 invariant's copied `spans_locations`/`guarded_by_test` claim would be unsupported, and in a base-less validation they are new records. The review reverted this and saw 40 validator and family-route tests fail.
- `LEGACY_COUNT` (`"R27.4-legacy-unassessed"`) names MIK-R27's one report-only count: the Doc14 §4.2 family is an export (`legacy-unassessed`), so every validation of the fixture tree carries it, and the tests' report-only pins include it.
- `DIRECT_LANDING_MARKDOWN` carries markers `[1]`–`[7]` plus an escaped `\[9]`, an inline `signals[0]` code span and a fenced `journal[1]`, so the passing tree exercises the marker grammar.
- `FAMILY` names the Doc14 §4.2 family record (`FAM-SEQNTS6C`). `FAMILY_REALIZATIONS` lists that family's other realizations as `(source file, entry ID, symbol, blob)`: `ledger_projection.py` (`resolve_memory_source_commit`), `models/knowledge/source.py` (`SourceAnchor`), `authorship.py` (`Authorship`) and `application/curator_source_manifest.py` (`read_source_plane`). Each blob is the file's blob at the code base, and each symbol exists there (review R1 checked both).
- `realization_sidecar(path, entry, symbol, blob, invariant="INV-7K3F9Q")` builds a file sidecar with one `realizes` entry anchoring that symbol; `fixture_tree_files()` adds one such sidecar and a one-line Markdown card for each `FAMILY_REALIZATIONS` row, so all six realizations sit under Doc14's three routes.
- `CODE_PATHS` lists the real repository paths the anchors name, now including the four `FAMILY_REALIZATIONS` files; `code()` returns them as a `CodePathSet`, so its directories also answer the family's route existence check.
- Helpers: `encode` (canonical bytes), `invariant_document`/`invariant_path`, `tree`, `edit_json` (a changed copy of one JSON file) and `write_tree` (materialise a tree on disk for the Git and CLI route tests).

### Conventions

- Every file is written through `canonical_text`, so the base tree passes `R22.1-canonical`.

### Invariants And Boundaries

- The assembled tree passes every registered rule with no refusal and exactly one report-only finding, the `LEGACY_COUNT` of its exported family (`test_converted_fixture_tree_passes_every_rule`), MIK-R04's route rules and MIK-R27's admission rules included: every route of the Doc14 family holds a realization and every realization lies under a route.
- A later leaf that extends `fixture_tree_files()` must keep that property (the review flagged a possible collision with L12 or L20 at sync).

### Todos

None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The validator's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R22@v1` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The fixture assembly and its helpers.

| Finding | Anchor | Source |
| --- | --- | --- |
| The Doc14 family's other realizations, by file, entry, symbol and blob. | `FAMILY`; `FAMILY_REALIZATIONS` | mcp/tests/knowledge_validator_test_support.py:30-30; mcp/tests/knowledge_validator_test_support.py:32-57 |
| The real code paths the anchors name, the family's realization files included. | `CODE_PATHS` | mcp/tests/knowledge_validator_test_support.py:58-66 |
| MIK-R27's legacy count, and the unchecked admission the two added invariants claim. | `LEGACY_COUNT`; `UNCHECKED_ADMISSION` | mcp/tests/knowledge_validator_test_support.py:106-106; mcp/tests/knowledge_validator_test_support.py:110-113 |
| A file sidecar with one realization entry. | `realization_sidecar` | mcp/tests/knowledge_validator_test_support.py:127-149 |
| The card with markers, an escape, a code span and a fenced block. | `DIRECT_LANDING_MARKDOWN` | mcp/tests/knowledge_validator_test_support.py:76-93 |
| The converted fixture tree, with a sidecar and card for each family realization. | `fixture_tree_files` | mcp/tests/knowledge_validator_test_support.py:152-185 |
| Editing one JSON file and writing a tree to disk. | `edit_json`; `write_tree` | mcp/tests/knowledge_validator_test_support.py:196-203; mcp/tests/knowledge_validator_test_support.py:206-210 |

## Cross-Repo References

No meaningful cross-repo references found: the helper reads the repository's own fixtures.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T00:17:15+02:00 — 260928-MIK-L27 curator (uncommitted change set on `ar/260928-mik-l27`, code base `46ca74302e76cf40fb6370ea9ece16d8fa719f00` plus the staged delta): **body update — `LEGACY_COUNT`, and `UNCHECKED_ADMISSION` on the two added invariants (MIK-R27).** Logic states both; the Invariants bullet was reworded, because the tree now passes with one report-only finding rather than none; one row added; the other rows re-pointed by the exact line shifts (+12, and +16 after `fixture_tree_files`). No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): **body update — the fixture tree now carries the Doc14 §4.2 family's other four realizations.** Purpose, Logic and Invariants name `FAMILY`, `FAMILY_REALIZATIONS`, `realization_sidecar` and the extended `CODE_PATHS`; two rows added. The reopened `CODE_PATHS` and `fixture_tree_files` claims were re-read and reworded against the current constructs; the fixer's two same-pass "claim bytes unchanged" bullets for them were removed and folded into this entry. No verification stamp was advanced.
- 2026-09-29T06:45:50+00:00: Generated citation repair: `DIRECT_LANDING_MARKDOWN` repointed to mcp/tests/knowledge_validator_test_support.py:76-93. No content impact: mechanical anchor-range projection bound to citation source snapshot 1a5c7dd5cb87835c8b4e585975574124e545ed7ed5b56804bf2cecaf1ab8ce6b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): created this card for the new file MIK-R22 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
