# mcp/src/agents_remember/code_quality/layering.py

| Field                  | Value                                                       |
| ---------------------- | ----------------------------------------------------------- |
| repository             | agents-remember                                             |
| path                   | `mcp/src/agents_remember/code_quality/layering.py`           |
| doc_type               | `file-level-onboarding`                                     |
| lastUpdated            | 2026-08-08T14:38+02:00                                      |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`                  |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
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
`_package_import_statements` (cit:([`_package_import_statements`], mcp/src/agents_remember/code_quality/layering.py:147-147)) turns `from agents_remember import X`
into either a rank-checked edge (declared X) or an undeclared-import failure (unknown X).

### Conventions

- Packages carrying `present = false` are skipped; a stale `present = false` entry surviving past
  its `arrives_in` leaf fails the build (L6-R12).
- A `_ScanContext` dataclass and `_record_edge` helper keep the scan single-pass and
  ruff-clean.

### Invariants And Boundaries

- Enforcement-universe completeness: a scanner enforcing a declared universe must fail closed on
  entities outside it (candidate CS-7 — undeclared dirs and `from agents_remember import X`
  forms fail; a stray root-level file is the recorded non-blocking residual).
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
| The wrapper registers the layering step unconditionally. | `quality_steps` | mcp/src/agents_remember/code_quality/check.py:262-308 |
| The unit suite pins rank violations, cycles, undeclared dirs/imports, and present-false rules. | `test_rank_violation_fails` | mcp/tests/test_layering.py:47-47 |
| The structural-coverage suite pins CLI/edges/render/stale behavior. | `test_layering_cli_and_edges` | mcp/tests/test_leaf_structural_coverage.py:84-84 |

## Cross-Repo References

No cross-repository implementation participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-08T14:38+02:00 — 260731-EFA-L9 curator: created for the armed layering rail; includes
  the F-3 fail-closed hardening and the delta residual. Verification metadata pinned until
  closeout stamps the L9 code commit.
