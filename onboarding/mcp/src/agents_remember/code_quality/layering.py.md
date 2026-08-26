# mcp/src/agents_remember/code_quality/layering.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/code_quality/layering.py`           |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-08T14:38+02:00                                      |
| lastVerifiedCommitHash | `ae8c47ce897b04380ebcb80f750d77ed4dc9f37d`                  |
| lastVerifiedCommitDate | 2026-08-26T08:10:26+02:00|
| governingOverview      | `../../../../overview.md`                                    |

## Governing Overview

[root overview](../../../../overview.md)

## Purpose

`code_quality/layering.py` is the package layering fitness function built and ARMED by
260731-EFA-L9 (R12). It reads `layers.toml [contract].order`, walks every module's imports,
builds the package graph, and fails on any import where `rank(imported) >= rank(importer)` and on
any package-pair cycle. There is no baseline and no allowlist.

## Code Commentary

### Logic

`LayersContract` (cit:(["class LayersContract"], mcp/src/agents_remember/code_quality/layering.py:27-27)) models the declared order; `load_contract`
(cit:([`load_contract`], mcp/src/agents_remember/code_quality/layering.py:62-62)) parses `layers.toml`; `package_for`/`resolve_import_target`
(cit:([`resolve_import_target`], mcp/src/agents_remember/code_quality/layering.py:86-86)) map paths/imports to packages; `imports_of`
(cit:([`imports_of`], mcp/src/agents_remember/code_quality/layering.py:104-104)) extracts import statements; `undeclared_dirs`
(cit:(["def undeclared_dirs(source_root: Path"], mcp/src/agents_remember/code_quality/layering.py:118-118)) fails closed on undeclared top-level directories (F-3 fix);
`_collect_violations`/`_collect_cycles`/`_collect_stale_flags` produce the report; and
`_package_import_statements` (cit:([`_package_import_statements`], mcp/src/agents_remember/code_quality/layering.py:157-157)) turns `from agents_remember import X`
into either a rank-checked edge (declared X) or an undeclared-import failure (unknown X).

### Conventions

- Packages carrying `present = false` are skipped; a stale `present = false` entry surviving past
  its `arrives_in` leaf fails the build (L6-R12).
- A `_ScanContext` dataclass and `_record_edge` helper keep the scan single-pass and
  ruff-clean.

### Invariants And Boundaries

- Enforcement-universe completeness: a scanner enforcing a declared universe must fail closed on
  real Python entities outside it (candidate CS-7 — undeclared dirs and
  `from agents_remember import X` forms fail). A directory containing only ignored cache debris,
  such as `__pycache__` left behind after a package deletion, is not a source package; recursive
  `.py` discovery still catches undeclared namespace packages without `__init__.py`.
- The step is wired unconditionally into the quality wrapper (`check.py` quality steps) and has
  no validate-then-mutate surface.

### Todos

Recorded residual: top-level files directly under `agents_remember/` outside the declared
packages are not scanned (delta residual, non-blocking).

## Docs References

No external/domain documentation is configured.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The wrapper registers the layering step unconditionally. | `quality_steps` | mcp/src/agents_remember/code_quality/check.py:378-428 |
| The unit suite pins rank violations, cycles, undeclared dirs/imports, and present-false rules. | `test_rank_violation_fails` | mcp/tests/test_layering.py:48-67 |
| The structural-coverage suite pins CLI/edges/render/stale behavior. | `test_layering_cli_and_edges` | mcp/tests/test_leaf_structural_coverage.py:83-83 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T01:38+02:00 — 260731-EFA-L22 curator: distinguished undeclared Python source from
  cache-only deleted-package debris while preserving fail-closed recursive `.py` detection.

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the armed layering rail; includes
  the F-3 fail-closed hardening and the delta residual. Verification metadata pinned until
  closeout stamps the L9 code commit.
