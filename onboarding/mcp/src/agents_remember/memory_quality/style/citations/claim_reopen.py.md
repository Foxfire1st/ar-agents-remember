# mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-07T14:30+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Reopen citation claims whose anchored evidence changed since verification.

## Code Commentary

### Logic

Module-level surface:

- `LocalSource` (class, lines 84-92)
- `Candidate` (class, lines 93-99)
- `CurrentFiles` (class, lines 100-109)
- `SourceViews` (class, lines 110-151) — Parsed source revisions shared by every claim in one gate run.
- `Evaluation` (class, lines 152-204)
- `claims_in` (function, lines 205-221)
- `finding` (function, lines 222-237)
- `provenance_finding` (function, lines 238-254)
- `changed_finding` (function, lines 255-268)
- `surfaced_finding` — the report-only review surface (never a blocker): a detected change whose
  citation is CURRENT (the anchor resolves exactly once and any cited range still contains the
  construct's declaration line, per `_anchor_in_cited_range`). Detected change splits three ways:
  absent or ambiguous anchors and unverifiable provenance are hard findings; a changed construct
  with a current citation is the curator's review surface, clearing with no commit; only a
  changed construct whose pointer is stale is an enforced reopened claim. Ambiguous provenance in
  documents the task did not touch demotes to report-only debt (`_demote_preexisting_provenance_debt`);
  in touched documents it stays enforced. This is what lets the citation gate run before the code
  commit at closeout (260731-EFA-L16). The absent-at-stamp rule extends to whole source files added
  after the stamp (260731-EFA-L8): a unique working-tree anchor inside a cited range surfaces
  report-only; absent, ambiguous, or stale constructs stay hard.
- `selected_current` (function, lines 297-310)
- `selected_historical` (function, lines 311-324)
- `local_changes` (function, lines 325-360) — missing-source handling now reports the
  absent-at-stamp-plus-absent-now case explicitly and lets each anchor judge the whole-new-file
  currency rule (`_anchor_in_cited_range`) instead of failing on any absent-at-stamp source.
- `anchor_change` (function, lines 361-419)
- `dependency_changes` (function, lines 482-513)
- `evaluate_claim` (function, lines 560-604)
- `check_onboarding_root` (function, lines 605-681) — Compare every complete claim against its own historical provenance.
- Closeout may pass `unstamped_code_commit` for dirty cards only. The checker uses that base as
  comparison provenance without writing a verification stamp; committed unstamped debt remains
  hard, and closeout's post-refresh run supplies no fallback.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- A whole source file added after the stamp follows the absent-at-stamp rule (260731-EFA-L8):
  an exactly-once working-tree anchor inside a cited range is the report-only surface; absent,
  ambiguous, or stale evidence is enforced.

### Todos

None.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `LocalSource` (lines 84-92). | `LocalSource` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:84-92 |
| Defines the class `Candidate` (lines 93-99). | `Candidate` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:93-99 |
| Defines the class `CurrentFiles` (lines 100-109). | `CurrentFiles` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:100-109 |
| Defines the class `SourceViews` (lines 110-151) — Parsed source revisions shared by every claim in one gate run.. | `SourceViews` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:110-151 |
| Defines the class `Evaluation` (lines 152-204). | `Evaluation` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:152-204 |
| Defines the function `claims_in` (lines 205-221). | `claims_in` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:205-221 |
| Defines the function `finding` (lines 222-237). | `finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:222-237 |
| Defines the function `provenance_finding` (lines 238-254). | `provenance_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:238-254 |
| Defines the function `changed_finding` (lines 255-268). | `changed_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:255-268 |
| Defines the function `selected_current` (lines 297-310). | `selected_current` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:297-310 |
| Defines the function `selected_historical` (lines 311-324). | `selected_historical` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:311-324 |
| Defines the function `local_changes` (lines 325-360). | `local_changes` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:325-360 |
| Defines the function `anchor_change` (lines 361-419). | `anchor_change` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:361-419 |
| Defines the function `dependency_changes` (lines 482-513). | `dependency_changes` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:482-513 |
| Defines the function `evaluate_claim` (lines 560-604). | `evaluate_claim` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:560-604 |
| Defines the function `check_onboarding_root` (lines 605-681) — Compare every complete claim against its own historical provenance.. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:605-681 |

## Update History

- 2026-08-10T08:20+02:00 — 260805-ARG-L1: added closeout-only temporary base provenance for
  dirty unstamped cards, reusing the Git dirty-path truth that also controls provenance-debt
  demotion. Standalone checks and committed unstamped cards remain hard failures; post-refresh
  closeout reruns without the fallback. Verification stays pinned until closeout stamps ARG-L1.
- 2026-08-07T14:30+02:00 — 260731-EFA-L8 curator (bounded delta): recorded the round-9 mechanism
  change — the absent-at-stamp rule now extends to whole source files added after the stamp: an
  anchor that resolves exactly once in the working tree inside a cited range surfaces report-only;
  absent, ambiguous, or stale constructs stay hard. Corrected the Logic bullets and reference
  ranges to the current mechanism build. Verification metadata stays pinned until closeout stamps
  the code commit.
- 2026-08-05T23:20+02:00 — 260731-EFA-L16 curator: recorded the three-way split of detected change (hard absent/ambiguous/provenance, report-only current-citation surface via `surfaced_finding` + `_citation_covers_current`, enforced stale pointer) — the semantics that let the closeout citation gate run before the code commit. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-05T03:49+02:00 — 260731-EFA-L6 C1 closeout pass: aligned the Logic bullets and Finding line numbers with the scoped fixer's generated decorator-inclusive class ranges; verification metadata unchanged.
- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
