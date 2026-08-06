# mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-05T00:00+02:00 |
| lastVerifiedCommitHash | `a3e43cb0877c18b9d2b0e6ada4eb5719a01f251f` |
| lastVerifiedCommitDate | 2026-08-06T05:49:07+02:00|
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
- `surfaced_finding` — the report-only review surface (never a blocker): a detected change whose
  citation is CURRENT (the anchor resolves exactly once and any cited range still contains the
  construct's declaration line, per `_anchor_in_cited_range`). Detected change splits three ways:
  absent or ambiguous anchors and unverifiable provenance are hard findings; a changed construct
  with a current citation is the curator's review surface, clearing with no commit; only a
  changed construct whose pointer is stale is an enforced reopened claim. Ambiguous provenance in
  documents the task did not touch demotes to report-only debt (`_demote_preexisting_provenance_debt`);
  in touched documents it stays enforced. This is what lets the citation gate run before the code
  commit at closeout (260731-EFA-L16).
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
| Defines the class `LocalSource` (lines 71-77). | `LocalSource` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:79-85 |
| Defines the class `Candidate` (lines 80-84). | `Candidate` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:88-92 |
| Defines the class `CurrentFiles` (lines 87-94). | `CurrentFiles` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:95-102 |
| Defines the class `SourceViews` (lines 97-136) — Parsed source revisions shared by every claim in one gate run.. | `SourceViews` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:97-136 |
| Defines the class `Evaluation` (lines 139-190). | `Evaluation` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:139-190 |
| Defines the function `claims_in` (lines 193-207). | `claims_in` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:193-207 |
| Defines the function `finding` (lines 210-223). | `finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:210-223 |
| Defines the function `provenance_finding` (lines 226-240). | `provenance_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:226-240 |
| Defines the function `changed_finding` (lines 243-254). | `changed_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:243-254 |
| Defines the function `selected_current` (lines 257-268). | `selected_current` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:292-303 |
| Defines the function `selected_historical` (lines 271-282). | `selected_historical` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:306-317 |
| Defines the function `local_changes` (lines 285-312). | `local_changes` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:320-349 |
| Defines the function `anchor_change` (lines 352-387). | `anchor_change` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:352-387 |
| Defines the function `dependency_changes` (lines 343-372). | `dependency_changes` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:457-486 |
| Defines the function `evaluate_claim` (lines 488-537). | `evaluate_claim` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:547-589 |
| Defines the function `check_onboarding_root` (lines 538-584) — Compare every complete claim against its own historical provenance.. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:592-666 |

## Update History

- 2026-08-05T23:20+02:00 — 260731-EFA-L16 curator: recorded the three-way split of detected change (hard absent/ambiguous/provenance, report-only current-citation surface via `surfaced_finding` + `_citation_covers_current`, enforced stale pointer) — the semantics that let the closeout citation gate run before the code commit. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
