# mcp/test_support/agents_remember_test_support/code_quality/citations.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/test_support/agents_remember_test_support/code_quality/citations.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-28T07:20+02:00 |
| lastVerifiedCommitHash | a06d2ffcfae2c277f2ae19330c17d09c616b77e8 |
| lastVerifiedCommitDate | 2026-08-28T13:58:55+02:00 |
| governingOverview | `overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

Resolve repository path citations in package comments and docstrings.

## Code Commentary

### Logic

Module-level surface:

- `Citation` (class, lines 80-95) — One prose reference to a path, with the line anchor it carried.
- `anchors` (function, lines 98-108) — Directory names a citation may start with, derived from the tree.
- `prose_spans` (function, lines 111-125) — ``(line, text)`` for every comment and docstring -- prose, never a string operand.
- `_docstrings` (function, lines 128-139)
- `citations_in_source` (function, lines 142-162) — Every in-grammar citation in one module's prose.
- `resolve` (function, lines 165-171) — The file a citation names, or ``None`` when no declared root holds it.
- `_anchor_offender` (function, lines 174-187) — A citation whose line anchor points past the end of the file it resolved to.
- `module_citation_offenders` (function, lines 190-210) — Every citation in one module that does not resolve, or overruns its target.
- `unresolved_citations` (function, lines 213-223) — Every prose citation in the package that names a path this repository lacks.
- `all_citations` (function, lines 226-234) — Every in-grammar citation in the package -- what the check is actually watching.

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
| Defines the class `Citation` (lines 80-95) — One prose reference to a path, with the line anchor it carried.. | `Citation` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:79-95 |
| Defines the function `anchors` (lines 98-108) — Directory names a citation may start with, derived from the tree.. | `anchors` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:98-108 |
| Defines the function `prose_spans` (lines 111-125) — ``(line, text)`` for every comment and docstring -- prose, never a string operand.. | `prose_spans` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:111-125 |
| Defines the function `_docstrings` (lines 128-139). | `_docstrings` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:128-139 |
| Defines the function `citations_in_source` (lines 142-162) — Every in-grammar citation in one module's prose.. | `citations_in_source` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:142-162 |
| Defines the function `resolve` (lines 165-171) — The file a citation names, or ``None`` when no declared root holds it.. | `resolve` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:165-171 |
| Defines the function `_anchor_offender` (lines 174-187) — A citation whose line anchor points past the end of the file it resolved to.. | `_anchor_offender` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:174-187 |
| Defines the function `module_citation_offenders` (lines 190-210) — Every citation in one module that does not resolve, or overruns its target.. | `module_citation_offenders` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:190-210 |
| Defines the function `unresolved_citations` (lines 213-223) — Every prose citation in the package that names a path this repository lacks.. | `unresolved_citations` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:213-223 |
| Defines the function `all_citations` (lines 226-234) — Every in-grammar citation in the package -- what the check is actually watching.. | `all_citations` | mcp/test_support/agents_remember_test_support/code_quality/citations.py:226-234 |

## Update History

- 2026-08-05T03:52+02:00 — 260731-EFA-L6 batch B curator: normalized decorator-inclusive citation ranges via scoped --fix against the frozen snapshot.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
