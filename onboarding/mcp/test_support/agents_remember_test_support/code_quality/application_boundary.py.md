# mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

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

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `BoundaryContractError` (lines 27-28) — The declared package order cannot define the application boundary.. | `BoundaryContractError` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:27-28 |
| Defines the class `BoundaryViolation` (lines 39-52) — One import that crosses the MCP/application boundary.. | `BoundaryViolation` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:38-52 |
| Defines the class `_LayerContract` (lines 56-58). | `_LayerContract` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:55-58 |
| Defines the function `_read_contract` (lines 61-85). | `_read_contract` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:61-85 |
| Defines the function `_resolved_imports` (lines 88-100). | `_resolved_imports` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:88-100 |
| Defines the function `_top_package` (lines 103-107). | `_top_package` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:103-107 |
| Defines the function `_permitted` (lines 110-114). | `_permitted` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:110-114 |
| Defines the function `_required_modules` (lines 117-131). | `_required_modules` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:117-131 |
| Defines the function `_serving_modules` (lines 134-141). | `_serving_modules` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:134-141 |
| Defines the function `_module_imports` (lines 144-147). | `_module_imports` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:144-147 |
| Defines the function `_transport_violations` (lines 150-175). | `_transport_violations` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:150-175 |
| Defines the function `_reverse_serving_violations` (lines 178-214). | `_reverse_serving_violations` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:178-214 |
| Defines the function `application_boundary_violations` (lines 217-228) — Return every MCP transport bypass and reverse serving edge in stable source order.. | `application_boundary_violations` | mcp/test_support/agents_remember_test_support/code_quality/application_boundary.py:217-228 |

## Update History

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
