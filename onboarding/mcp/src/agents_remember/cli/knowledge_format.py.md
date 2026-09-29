# mcp/src/agents_remember/cli/knowledge_format.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/cli/knowledge_format.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T09:30:11+02:00 |
| lastVerifiedCommitHash | `6ad4e076bbbc5d98b8c770fc374d56ddc4a2d695`|
| lastVerifiedCommitDate | 2026-09-29T09:57:49+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**`agents-remember knowledge-format [--check] PATH...`: the command that applies the canonical
knowledge formatting (MIK-R21 rule 8).** Each PATH is a file or a directory; a directory contributes
every `*.json` below it except the generated route-index cache (`*.index.json`) and anything under a
hidden directory (such as `.ar-index`). A dot-named *file* is still formatted. It is the command the
validator (MIK-R22) names, as `agents-remember knowledge-format <path>`, when it refuses a
non-canonical file.

## Code Commentary

### Logic

- `add_arguments` declares `paths` (one or more) and `--check`.
- `iter_json_files` yields a named file as-is, and for a directory the sorted `rglob("*.json")`
  minus every path that `memory_quality.knowledge_validator.trees.is_excluded_from_knowledge` excludes:
  a `*.index.json` cache, or a path with a dot-named *directory* component. Since MIK-R22 this is the
  validator's own predicate, so the formatter and the validator cannot disagree about which files are
  knowledge. The module's former `CACHE_SUFFIX` constant and its own copy of the rule are gone.
- `run` reads each file, formats it with `canonical.format_bytes`, and: on `OSError` or
  `CanonicalFormatError` prints `invalid <path>: …` and sets status 2 (file untouched); if already
  canonical, continues; with `--check` prints `not canonical <path>` and sets status ≥1; otherwise
  rewrites with `kernel.atomic_write.atomic_write_bytes` and prints `reformatted <path>`.

### Conventions

- Registered in `cli/__main__.py` with the umbrella's declarative `add_arguments` +
  `set_defaults(func=run)` pair; the adapter owns its flags and exit codes.

### Invariants And Boundaries

- Exit status: 0 all canonical (after rewriting), 1 `--check` found a non-canonical file, 2 a file
  could not be read or parsed. `--check` writes nothing.
- It formats only; it validates nothing and changes no content.
- **The formatter and the validator share one "is this a knowledge file" predicate.** The import runs
  from the CLI layer down to `memory_quality`, which is the permitted direction.
- **Nothing in the installed runtime reads or writes these files before MIK-R37.** The package is
  reached only from `agents-remember knowledge-format` and the tests; the live memory repository
  is still read and written through the SQLite knowledge store until the layout switch.

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

The formatting rules live in the model package; this adapter only walks paths and writes.

| Finding | Anchor | Source |
| --- | --- | --- |
| Arguments. | `add_arguments` | mcp/src/agents_remember/cli/knowledge_format.py:26-32 |
| Cache files and hidden directories are skipped through the validator's shared predicate. | `iter_json_files`; `is_excluded_from_knowledge` | mcp/src/agents_remember/cli/knowledge_format.py:35-45; mcp/src/agents_remember/memory_quality/knowledge_validator/trees.py:50-63 |
| Exit statuses and the atomic rewrite. | `run` | mcp/src/agents_remember/cli/knowledge_format.py:48-66 |
| Registration in the umbrella. | "knowledge-format" | mcp/src/agents_remember/cli/__main__.py:70-70 |
| The command's check, rewrite and skip behaviour is tested end to end. | `test_knowledge_format_command_checks_rewrites_and_skips_caches` | mcp/tests/test_knowledge_file_canonical.py:85-120 |

## Cross-Repo References

No meaningful cross-repo references found: the command rewrites only the files it is given.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **No content impact** — citation-only repair. MIK-R20 registers `knowledge-census` in `cli/__main__.py` (one import line and a longer docstring sentence), which moves the later registrations down by two lines; this card's registration row was re-pointed to the new extent, its claim unchanged. No verification stamp was advanced.
- 2026-09-29T08:49:57+02:00 — 260928-MIK-L04 curator (uncommitted change set on `ar/260928-mik-l04`, code base `ffd043f1354e94a7dcf435e10b4b7224495cbcba` plus the staged delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`__main__.py`, `trees.py`) were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact base-to-working line map; no claim wording changed. No verification stamp was advanced.
- 2026-09-29T08:01:17+02:00 — 260928-MIK-L23 curator (uncommitted change set on `ar/260928-mik-l23`, code base `ee5f14e5405505d126125830e5323f8915c8d047` plus the working-tree delta): No content impact: this card's source is unchanged. Citation ranges into files this change set edited (`application/published_intent.py`, `mcp/tools/knowledge.py`, `mcp/registration/knowledge.py`, `models/tools/knowledge_responses.py`, `cli/__main__.py`, `mcp/tests/test-evidence-lanes.toml`) were re-pointed by the installed fixer or, for the multi-anchor rows it declined, by exact base-to-working line mapping; a per-document `memory-citations` check then reported 0 findings. No claim wording changed.
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): `iter_json_files` now uses the validator's `trees.is_excluded_from_knowledge` in place of its own rule and `CACHE_SUFFIX` (review R1 finding 1). Documented the shared predicate and that a dot-named file is formatted, and updated the Purpose now that the validator names this command. I folded the same-pass generated repair bullet for `iter_json_files` into this entry, because that claim's text changed. The verification stamp is unchanged; closeout owns it.
- 2026-09-29T05:00:46+00:00: Generated citation repair: `add_arguments` repointed to mcp/src/agents_remember/cli/knowledge_format.py:26-32. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T05:00:46+00:00: Generated citation repair: `run` repointed to mcp/src/agents_remember/cli/knowledge_format.py:48-66. No content impact: mechanical anchor-range projection bound to citation source snapshot 4f49c430ac3ddcb93815034b5cf7de82be47b24afeddd7bfc8ef2ba769b871ac; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): created this card for the new file MIK-R21 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
