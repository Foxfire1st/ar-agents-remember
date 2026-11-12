# mcp/test_support/agents_remember_test_support/code_quality/layering.py

## Governing Overview

[root overview](../../../../overview.md)

## Purpose

`code_quality/layering.py` is the package layering fitness function built and ARMED by
260731-EFA-L9 (R12). It reads `layers.toml [contract].order`, walks every module's imports,
builds the package graph, and fails on any import where `rank(imported) >= rank(importer)` and on
any package-pair cycle. There is no baseline and no allowlist.

## Code Commentary

### Logic

`LayersContract` (cit:(["class LayersContract"], mcp/test_support/agents_remember_test_support/code_quality/layering.py:27-27)) models the declared order; `load_contract`
(cit:([`load_contract`], mcp/test_support/agents_remember_test_support/code_quality/layering.py:62-62)) parses `layers.toml`; `package_for`/`resolve_import_target`
(cit:([`resolve_import_target`], mcp/test_support/agents_remember_test_support/code_quality/layering.py:86-86)) map paths/imports to packages; `imports_of`
(cit:([`imports_of`], mcp/test_support/agents_remember_test_support/code_quality/layering.py:104-104)) extracts import statements; `undeclared_dirs`
(cit:(["def undeclared_dirs(source_root: Path"], mcp/test_support/agents_remember_test_support/code_quality/layering.py:118-118)) fails closed on undeclared top-level directories (F-3 fix);
`_collect_violations`/`_collect_cycles`/`_collect_stale_flags` produce the report; and
`_package_import_statements` (cit:([`_package_import_statements`], mcp/test_support/agents_remember_test_support/code_quality/layering.py:157-157)) turns `from agents_remember import X`
into either a rank-checked edge (declared X) or an undeclared-import failure (unknown X).
The caller threads the exact project root through package traversal; scanners no longer infer it
from a source-root parent and therefore retain the configured repository boundary in nested layouts.

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

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The wrapper registers the layering step unconditionally. [1]
- The unit suite pins rank violations, cycles, undeclared dirs/imports, and present-false rules. [2]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
