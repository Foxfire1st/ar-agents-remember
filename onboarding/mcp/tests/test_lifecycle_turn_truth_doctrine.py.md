# mcp/tests/test_lifecycle_turn_truth_doctrine.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The cross-surface guard over the canonical lifecycle corpus: the doctrine states **one** handoff
authority boundary, and this module is the executable statement that every canonical surface agrees
with it. Its subject is not a typo but *disagreement between role descriptions* — the boundary stated
correctly in one file and contradicted in another, or asserted in the shared root while a role file
still promises a report checker that does not exist. Each file is individually plausible, so no
per-file check can see it.

## Current source account

The native worker owes one parent-addressed report-written message only when a parent agent started it, and states that a finished turn is not AR acceptance. Manifest-selected architect/manager/orchestrator operation capsules must inspect candidate/evidence before acceptance; a removed manager inspection sentence must fail the guard. The retained contradiction machinery checks authored instruction wording, not runtime acceptance transactions. The roster holds every canonical surface that speaks the completion vocabulary, including the composed curation operation and the curator and reviewer role documents, whose retained sentence states the mechanical reading.

## Code Commentary

### Logic

Four mechanisms defend four different readings, and they are deliberately **not** interchangeable:

- **No canonical surface contradicts the boundary.** `contradictions` / `RETIRED_CLAIMS` sweep every
  `.md` under `skills/l-01-agent-lifecycles`, not just the declared roster, so a contradiction in an
  undeclared file still fails. This is the cross-role agreement property.
- **Every surface that speaks the vocabulary states the mechanical reading.** `COMPLETION_TRUTH_ROSTER`
  is a census, not a list of favoured files: the declared roster must **equal** the files that use
  `COMPLETION_TRUTH_VOCABULARY`, in both directions. A surface that newly speaks the vocabulary and is
  not declared fails just as a declared surface that went silent does. The composed curation operation
  and the curator and reviewer role documents stand on the roster because each retains the sentence that
  terminal/finalizer truth attests only that the turn ended and wakes the owner who validates.
- **Each declared surface states its own owed clauses and does not deny them.** `OWED_STATEMENTS` is
  per-surface and contradiction-aware: a surface that states *and* denies fails `_assert_owed` and
  reads `CONTRADICTED`.
- **The sweep can still fail.** `DetectorTeethTests` runs every retired-claim detector against the
  historical contradicting text it was written for *and* against the shipped wording it must pass;
  `DeclaredLimitsTests` pins the detectors' own documented limits.

`classify_reading` returns three states — `STATE` / `ABSENT` / `CONTRADICTED` — and **silence is not
contradiction**: a surface that owes no clause may legitimately be `ABSENT`, and only a surface that owes
a clause must state it. Conversely every canonical surface, owed or not, must
avoid `CONTRADICTED`.

`AgreementAcrossTheRoleSetTests` holds the census the roster carries; `SilenceIsNotContradictionTests`
pins all three reading states on synthetic samples; `ConvergenceTeethTests` (additive, this leaf's
change) pairs each reconciled site with a mutant that must still trip the same claim, reads the shipped
side from the file rather than pasting it, and proves that removing any owed clause of
`core/acceptance.md` is caught.

**The boundary's one home is `core/acceptance.md`.** The whole-boundary assertion follows the boundary,
not the path it used to live at: the shared-root case now reads `core/acceptance.md`, and `SKILL.md`
remains swept by the contradiction case like every other canonical surface.

### Conventions

- Detectors read **normalized, rejoined** sentence views, so punctuation and clause adjacency are part
  of what is measured — a sentence split or a connective can change a reading without changing meaning.
  That is why several reconciled sites were repaired at punctuation level.
- The roster's captured text is the guard's **declared data**, kept separate from the detectors: the
  census and owed sets move with the corpus, the detectors and their teeth cases do not.
- Detector teeth and declared-limit cases remain separate from changing corpus data.
  The native Worker-parent and coordinator-capsule cases add explicit instruction-boundary
  coverage; they do not execute an AR acceptance transaction.

### Invariants And Boundaries

- **A detector is never loosened to make a corpus sentence pass.** A clause that cannot be satisfied
  without weakening a detector is an overconstraint to report, not a licence to edit the limit — and the
  guard's own coarse negated-fragment filter is a *documented* limit, pinned by `DeclaredLimitsTests`.
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

- The doctrine's one home, which the census and the shared-root case follow. [1]
- The declared roster and the vocabulary whose speakers it must equal, in both directions. [2]
- The per-surface owed clauses, and the relay-mechanics surfaces the corpus still names. [3]
- The contradiction sweep and its three-state reading classification. [4]
- The protected teeth classes, byte-unchanged by this leaf and the reason a limit cannot be edited to pass. [5]
- The projection-side sibling that re-asserts the same clauses against canonical plus the nine generated copies. [6]

### Cross-Repo References

No external repository boundary is exercised by this guard; it reads this repository's canonical corpus
and its packaged copies.

No meaningful cross-repo references found.
