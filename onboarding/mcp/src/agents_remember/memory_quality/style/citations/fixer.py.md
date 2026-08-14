# mcp/src/agents_remember/memory_quality/style/citations/fixer.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/fixer.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Regenerate citation ranges from anchors.

## Code Commentary

### Logic

Module-level surface:

- `Candidate` (class, lines 44-53) — One gating claim, or one passing claim selected for scoped normalisation.
- `Applied` (class, lines 56-64) — One claim's source list, before and after.
- `Refused` (class, lines 67-94) — One claim ``--fix`` left for the curator agent, with the facts it needs.
- `Result` (class, lines 97-107) — What one run of the fixer did, and everything it refused.
- `table_sites` (function, lines 110-120) — Every conforming table row, with the span of its Source cell.
- `prose_sites` (function, lines 123-144) — Every ``cit:`` that opens and closes on ONE line, and the count of those that do not.
- `cit_bounds` (function, lines 147-157) — Each ``cit:`` opening parenthesis on the line, and its closer when there is one.
- `prose_site` (function, lines 160-164)
- `sites` (function, lines 167-170) — Every claim in one document whose source list can be rewritten in place.
- `scope_of` (function, lines 173-179)
- `failing` (function, lines 182-189) — Whether this claim carries a defect a regenerated range could clear.
- `Walk` (class, lines 192-200) — Run-scoped trees, sources, documents, and result for one candidate walk.
- `candidates` (function, lines 203-238) — Every repairable or duplicate-bearing claim, plus scoped passing claims.
- `fix_onboarding_root` (function, lines 241-297) — Regenerate every repairable range in the memory tree, and report the rest.
- `_decide` (function, lines 300-332)
- `_scoped_source` (function, lines 335-364) — Normalise each citation, exact-deduplicate it, and preserve verified spans.
- `_scoped_citation` (function, lines 367-423) — One original Source segment, generated only from anchors that segment verifies.
- `payload` (function, lines 426-468) — The complete offender list and the complete repair list, never a sample (L6-R15).

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
| Defines the class `Candidate` (lines 44-53) — One gating claim, or one passing claim selected for scoped normalisation.. | `Candidate` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:44-53 |
| Defines the class `Applied` (lines 56-64) — One claim's source list, before and after.. | `Applied` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:56-64 |
| Defines the class `Refused` (lines 67-94) — One claim ``--fix`` left for the curator agent, with the facts it needs.. | `Refused` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:67-94 |
| Defines the class `Result` (lines 97-107) — What one run of the fixer did, and everything it refused.. | `Result` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:97-107 |
| Defines the function `table_sites` (lines 110-120) — Every conforming table row, with the span of its Source cell.. | `table_sites` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:110-120 |
| Defines the function `prose_sites` (lines 123-144) — Every ``cit:`` that opens and closes on ONE line, and the count of those that do not.. | `prose_sites` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:123-144 |
| Defines the function `cit_bounds` (lines 147-157) — Each ``cit:`` opening parenthesis on the line, and its closer when there is one.. | `cit_bounds` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:147-157 |
| Defines the function `prose_site` (lines 160-164). | `prose_site` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:160-164 |
| Defines the function `sites` (lines 167-170) — Every claim in one document whose source list can be rewritten in place.. | `sites` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:167-170 |
| Defines the function `scope_of` (lines 173-179). | `scope_of` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:173-179 |
| Defines the function `failing` (lines 182-189) — Whether this claim carries a defect a regenerated range could clear.. | `failing` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:182-189 |
| Defines the class `Walk` (lines 192-200) — Run-scoped trees, sources, documents, and result for one candidate walk.. | `Walk` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:192-200 |
| Defines the function `candidates` (lines 203-238) — Every repairable or duplicate-bearing claim, plus scoped passing claims.. | `candidates` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:203-238 |
| Defines the function `fix_onboarding_root` (lines 241-297) — Regenerate every repairable range in the memory tree, and report the rest.. | `fix_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:241-297 |
| Defines the function `_decide` (lines 300-332). | `_decide` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:300-332 |
| Defines the function `_scoped_source` (lines 335-364) — Normalise each citation, exact-deduplicate it, and preserve verified spans.. | `_scoped_source` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:335-364 |
| Defines the function `_scoped_citation` (lines 367-423) — One original Source segment, generated only from anchors that segment verifies.. | `_scoped_citation` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:367-423 |
| Defines the function `payload` (lines 426-468) — The complete offender list and the complete repair list, never a sample (L6-R15).. | `payload` | mcp/src/agents_remember/memory_quality/style/citations/fixer.py:426-468 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
