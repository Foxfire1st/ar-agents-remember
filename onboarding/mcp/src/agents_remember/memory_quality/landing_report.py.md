# mcp/src/agents_remember/memory_quality/landing_report.py

## Governing Overview

[Memory-quality overview](overview.md)

## Purpose

Measures what a memory candidate removes from existing onboarding cards and what it adds outside the knowledge folders. These facts inform independent memory review; they never become automated judgments of whether the removed prose is true or a new refusal.

## Code Commentary

The shared measure reports a Markdown card or overview when it removes at least eight base lines and more than twice the lines it adds. The line-multiset comparison is order-insensitive and linear in card size: rearranging identical lines is not a cut, and repeated lines do not trigger a quadratic sequence matcher. Complete card removals use the same predicate. New cards have no base prose to cut.

An admitted leaf compares with its contract's memory base, not the validator's operation base or the worktree HEAD. Thus committing leaf progress does not erase its cuts or additions from later checks. Application-supplied code-base paths prove the deleted-source exemption: the source must exist at the base and be absent at the candidate. A source absent on both known sides is not a deletion by the leaf. Overviews have no source-deletion exemption. In the diagnostic case with no code tree on either side, a vanished source card is unplaced and silent; that fallback does not describe ordinary contract-bound leaf checks.

Code-named `git -M` renames compare the moved card with its former path, including edited renames. Unnamed additions/deletions follow the deletion and new-card rules instead of guessing a move from a shared blob. The separate blob heuristic permits only an unambiguous departing/arriving pair; production Git entry points are preferred. Unstaged delete/add pairs that Git has not named as a rename remain unnamed.

The added-path census compares the full candidate listing with the admitted base, excludes paths under `onboarding/`, `knowledge/` and `system/`, and reports per-path byte size plus the total. Working-tree enumeration does not follow symlink targets: dangling links still count by their own `lstat` size, consistent with Git's stored link bytes. Any `.git` path component is administrative metadata, not repository content.

The pure report always has `ok=true`, zero refusing findings, and landing rows only in `reportOnlyFindings`. Pure inputs with `base_cards=None` and quality-run leaf-base failures name an unreadable memory base rather than interpreting it as an empty/no-cut result. The direct Git-ref adapter first reads both memory refs and can raise when a ref cannot be read; it is not the quality-run failure-envelope owner. Git-ref and working-tree adapters provide observations; neither decides which content should land. The answer projector bounds first rows, while the complete rows remain with the full quality result/checklist.

## Evidence

No Domain Documentation sources are configured. These are source/test contracts, not new test-execution claims.

- One shared predicate owns the eight-line and strict removed-to-added measure. [1]
- Line deltas compare multisets with linear hashing work and ignore line order. [2]
- Shortened and wholly removed cards apply the shared measure and proven-deletion boundaries. [3]
- Candidate additions exclude the three knowledge roots and retain sizes and the sum. [4]
- Working-tree inventory counts file/link entries without following targets or including Git administration. [5]
- Leaf-bound reports retain committed changes and keep the diagnostic fallback distinct. [6]
- The pure report keeps landing facts report-only and names an unreadable base. [7]
- The operation-level gate and closeout-quality cases compare landed and clean populations without claiming a live transaction. [8]
