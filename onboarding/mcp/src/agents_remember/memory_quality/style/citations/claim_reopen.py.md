# mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Reopen citation claims whose anchored evidence changed since verification.

## Code Commentary

### Logic

Module-level surface:

- `LocalSource` (class, lines 71-77)
- `Candidate` (class, lines 80-84)
- `CurrentFiles` (class, lines 87-94)
- `SourceViews` (class, lines 97-136) — Parsed source revisions shared by every claim in one gate run.
- `Evaluation` (class, lines 139-190)
- `claims_in` (function, lines 193-207)
- `finding` (function, lines 210-223)
- `provenance_finding` (function, lines 226-240)
- `changed_finding` (function, lines 243-254)
- `selected_current` (function, lines 257-268)
- `selected_historical` (function, lines 271-282)
- `local_changes` (function, lines 285-312)
- `anchor_change` (function, lines 315-340)
- `dependency_changes` (function, lines 343-372)
- `evaluate_claim` (function, lines 375-418)
- `check_onboarding_root` (function, lines 421-500) — Compare every complete claim against its own historical provenance.

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
| Defines the class `LocalSource` (lines 71-77). | `LocalSource` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:71-77 |
| Defines the class `Candidate` (lines 80-84). | `Candidate` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:80-84 |
| Defines the class `CurrentFiles` (lines 87-94). | `CurrentFiles` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:87-94 |
| Defines the class `SourceViews` (lines 97-136) — Parsed source revisions shared by every claim in one gate run.. | `SourceViews` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:97-136 |
| Defines the class `Evaluation` (lines 139-190). | `Evaluation` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:139-190 |
| Defines the function `claims_in` (lines 193-207). | `claims_in` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:193-207 |
| Defines the function `finding` (lines 210-223). | `finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:210-223 |
| Defines the function `provenance_finding` (lines 226-240). | `provenance_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:226-240 |
| Defines the function `changed_finding` (lines 243-254). | `changed_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:243-254 |
| Defines the function `selected_current` (lines 257-268). | `selected_current` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:257-268 |
| Defines the function `selected_historical` (lines 271-282). | `selected_historical` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:271-282 |
| Defines the function `local_changes` (lines 285-312). | `local_changes` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:285-312 |
| Defines the function `anchor_change` (lines 315-340). | `anchor_change` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:315-340 |
| Defines the function `dependency_changes` (lines 343-372). | `dependency_changes` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:343-372 |
| Defines the function `evaluate_claim` (lines 375-418). | `evaluate_claim` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:375-418 |
| Defines the function `check_onboarding_root` (lines 421-500) — Compare every complete claim against its own historical provenance.. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:421-500 |

## Update History

- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
