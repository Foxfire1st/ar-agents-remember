# mcp/tests/test_lifecycle_turn_truth_doctrine.py

## Governing Overview

[overview](overview.md)

## Purpose

The cross-surface guard over the canonical lifecycle corpus: the doctrine states **one** handoff
authority boundary, and this module is the executable statement that every canonical surface agrees
with it. Its subject is not a typo but *disagreement between role descriptions* — the boundary stated
correctly in one file and contradicted in another, or asserted in the shared root while a role file
still promises a report checker that does not exist. Each file is individually plausible, so no
per-file check can see it.

## Code Commentary

### Logic

Four mechanisms defend four different readings, and they are deliberately **not** interchangeable:

- **No canonical surface contradicts the boundary.** `contradictions` / `RETIRED_CLAIMS` sweep every
  `.md` under `skills/l-01-agent-lifecycles`, not just the declared roster, so a contradiction in an
  undeclared file still fails. This is the cross-role agreement property.
- **Every surface that speaks the vocabulary states the mechanical reading.** `COMPLETION_TRUTH_ROSTER`
  is a census, not a list of favoured files: the declared roster must **equal** the files that use
  `COMPLETION_TRUTH_VOCABULARY`, in both directions. A surface that newly speaks the vocabulary and is
  not declared fails just as a declared surface that went silent does. The curation operation
  states the terminal-only half directly; the Curator consumes that operation instead of carrying
  an independent raw-role speaker claim. The Reviewer and Orchestrator roles retain local turn-only truth. The
  owner-validation half lives at the common home core/acceptance.md, which also states terminal
  truth. Composition and the common home do not turn a finished turn into semantic acceptance.
- **Each declared surface states its own owed clauses and does not deny them.** `OWED_STATEMENTS` is
  per-surface and contradiction-aware: a surface that states *and* denies fails `_assert_owed` and
  reads `CONTRADICTED`. The master-handover-packet and turn-report templates owe referral
  clauses to `core/acceptance.md`; for a template, `_assert_owed` also checks that the referral target
  resolves to `core/acceptance.md` and asserts that surface's own owed clauses.
- **The sweep can still fail.** `DetectorTeethTests` runs every retired-claim detector against the
  historical contradicting text it was written for *and* against the shipped wording it must pass;
  `DeclaredLimitsTests` pins the detectors' own documented limits.

`classify_reading` returns three states — `STATED` / `ABSENT` / `CONTRADICTED` — and **silence is not
contradiction**: a surface that owes no clause may legitimately be `ABSENT`, and only a surface that owes
a clause must state it. Conversely every canonical surface, owed or not, must
avoid `CONTRADICTED`.

`AgreementAcrossTheRoleSetTests` holds the census the roster carries; `SilenceIsNotContradictionTests`
pins all three reading states on synthetic samples; `ConvergenceTeethTests` pairs each reconciled site with a mutant that must still trip the same claim, reads the shipped
side from the file rather than pasting it, and proves that removing any owed clause of
any declared surface is caught.

**The boundary's one home is `core/acceptance.md`.** The whole-boundary case reads `core/acceptance.md`, and `SKILL.md`
is swept by the contradiction case like every other canonical surface.

### Conventions

- Detectors read **normalized, rejoined** sentence views, so punctuation and clause adjacency are part
  of what is measured — a sentence split or a connective can change a reading without changing meaning.
  The clause splitter also breaks at table-cell bars, so a table label and its adjacent cell are
  read as separate clauses.
- The roster's captured text is the guard's **declared data**, kept separate from the detectors: the
  census and owed sets track the corpus. The compact equivalent ‘proves only turn end’ and the form ‘a turn ending proves only that it ended’ are recognized by the mechanical-reading expression, and the turn-end restriction expression also recognizes past-tense attestations. Both compact and expanded statements followed by an acceptance claim must still classify CONTRADICTED; no path exception or disabled sweep is introduced.
- Detector teeth and declared-limit cases remain separate from changing corpus data.
  The Worker direct-handover and coordinator-capsule cases add explicit instruction-boundary
  coverage, with a deletion control per required clause or marker; they do not execute an AR acceptance transaction.

### Invariants And Boundaries

- **Equivalent wording is not acceptance.** Recognition of the compact turn-end-only form is paired
  with positive controls and state-plus-acceptance negative controls. It is not permission to weaken
  a contradiction detector or suppress a failing speaker. The coarse negated-fragment limit remains
  explicitly pinned by `DeclaredLimitsTests`.
- **Declaration is a census, not a preference.** Adding a vocabulary speaker without adding its roster
  row fails; removing a roster row while the surface still speaks fails.
- **The declared limits are pinned, not aspirational.** If a limit's sample no longer exists in the
  tree, that is a finding to report, never a reason to edit the limit.
- The shared table in `mcp/tests/test_sync_scripts.py` quotes this module's shipped wording rather than
  paraphrasing it, so the two guards cannot drift into two vocabularies.

## Evidence
### Docs References

No Domain Documentation source is configured for this repository; the boundary is repository-owned
canonical prose and the guard reads the corpus itself.

No configured `Domain Documentation` source applies; the doctrine under test is the repository's own canonical corpus.

### Repo-Internal References

- The shared acceptance home distinguishes mechanical turn-end truth from artifact validity, requires the structurally current owner to validate before advancing state, and keeps recipient checks for direct peer handovers separate from Manager gate acceptance. [1]

- The declared roster and vocabulary must equal the actual canonical speakers in both directions. [2]

- OWED_STATEMENTS declares each named surface's required boundary clauses; the master-handover-packet and turn-report templates owe referral clauses to `core/acceptance.md`. RELAY_REFERENCE_SURFACES names the turn-report template, checked as a referral to the acceptance owner; it is separate from the completion-truth roster and the mechanical-only reading vocabulary. [3]

- The detector scans promise views for the declared RETIRED_CLAIMS and classifies each text as stated, absent or contradicted. Contradictions take priority over a matching mechanical-only phrase, and an in-place denial does not count as a positive statement. [4]

- The silence controls distinguish stated, absent and contradicted readings, including compact and expanded turn-end wording, split acceptance claims and in-place denial. Detector controls retain per-claim samples and whole-tree census; the declared-limit case pins the detector's proximity-based misreading of another agent's acceptance inside its window. [5]

- The projection-side sibling that re-asserts the boundary clauses against the canonical doctrine tree and its one declared packaged copy. [6]

- The relay detector requires an attributed relay action rather than mere co-occurrence of sweep, open and packet words; active and passive artifact-inspection examples still fail. Worker handoff checks bind the Manager stage-start notice and the direct frozen-object Reviewer handover to their real sections in the Worker role, the implementation operation and the every-role core, with per-clause deletion controls. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [7]

### Cross-Repo References

No external repository boundary is exercised by this guard; it reads this repository's canonical corpus
and its packaged copies.

No meaningful cross-repo references found.
