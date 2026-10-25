# dashboard/src/data/reviewJudgment.ts

## Governing Overview

[data overview](overview.md)

## Purpose

Carry the selected record's leaf-history judgments and proof entries as the browser half of Judgment and proofs. This is a wire mirror, not a judgment author or a test runner; the main review entry re-exports its pane/row/proof types.

## Code Commentary

ReviewJudgmentRow preserves attempt, row identity, subject, disposition, optional effect/revision, reason, because, optional covered-entry/examined-member counts, history path and closed flag. Because can be a record string or a structured requirement address (task repository/path, packet, id, version); it is not flattened into a guessed in-memory record.

ReviewProofDisplay preserves proof identity, invariant, test path, optional symbol, facet, supplied current/stale/unverifiable state and detail. That state describes the proof entry at the after code tree, not whether its test just passed. ReviewJudgmentPane carries rows/none/unavailable plus detail and proofs; unreadable history need not remove proofs. The Python producer validates that nonempty rows occur exactly in rows state. The TypeScript interface mirrors those fields but does not enforce that correlation at runtime.

SubjectJudgment rejects a missing pane or mismatched selected subject instead of presenting none. It renders row reasons/because/counts and proof path/state/facet openly; only identifiers are disclosed. These renderer guarantees belong to that consumer, not to the interface itself. No new request route, effect inference, browser storage or write path is introduced here.

## Evidence

- Row and structured requirement preserve history identity and because without conclusions. [1]
- Proof entry state and pane history state remain independent. [2]
- Producer says proof currentness is not a run result and validates rows-state correlation. [3]

- Consumer rejects missing/misaddressed judgment and renders rows and proofs. [4]
