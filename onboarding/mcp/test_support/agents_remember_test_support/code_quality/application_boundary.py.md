# mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py

## Governing Overview

[overview](../../../overview.md)

## Purpose

Enforce the MCP/application transport boundary (L6-R7).

## Code Commentary

### Logic

Module-level surface:

- `BoundaryContractError` (class, lines 27-28) — The declared package order cannot define the application boundary.
- `BoundaryViolation` (class, lines 39-52) — One import that crosses the MCP/application boundary.
- `_LayerContract` (class, lines 56-58)
- `_read_contract` (function, lines 61-85)
- `_resolved_imports` (function, lines 88-100)
- `_top_package` (function, lines 103-107)
- `_permitted` (function, lines 110-114)
- `_required_modules` (function, lines 117-131)
- `_serving_modules` (function, lines 134-141)
- `_module_imports` (function, lines 144-147)
- `_transport_violations` (function, lines 150-175)
- `_reverse_serving_violations` (function, lines 178-214)
- `application_boundary_violations` (function, lines 217-228) — Return every MCP transport bypass and reverse serving edge in stable source order.

MCP transport modules must enter the application layer instead of importing higher domain owners
directly. The layer declaration also supplies the permitted lower packages. The reverse check
prevents serving modules from importing application or MCP transport. Static absolute and relative
imports are inspected throughout the AST, including TYPE_CHECKING blocks; dynamic imports are
outside this static check. Missing or empty required source trees refuse instead of making the
check vacuously pass.

cit:([`_permitted`], mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:110-114)
cit:([`_transport_violations`], mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:150-175)
cit:([`_reverse_serving_violations`], mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:178-214)

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.

### Todos

None.

## Evidence

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Defines the class `BoundaryContractError` (lines 27-28) — The declared package order cannot define the application boundary.. [1]
- Defines the class `BoundaryViolation` (lines 39-52) — One import that crosses the MCP/application boundary.. [2]
- Defines the class `_LayerContract` (lines 56-58). [3]
- Defines the function `_read_contract` (lines 61-85). [4]
- Defines the function `_resolved_imports` (lines 88-100). [5]
- Defines the function `_top_package` (lines 103-107). [6]
- Defines the function `_permitted` (lines 110-114). [7]
- Defines the function `_required_modules` (lines 117-131). [8]
- Defines the function `_serving_modules` (lines 134-141). [9]
- Defines the function `_module_imports` (lines 144-147). [10]
- Defines the function `_transport_violations` (lines 150-175). [11]
- Defines the function `_reverse_serving_violations` (lines 178-214). [12]
- Defines the function `application_boundary_violations` (lines 217-228) — Return every MCP transport bypass and reverse serving edge in stable source order.. [13]
