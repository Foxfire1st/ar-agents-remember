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

**Historical source account, superseded by the current clause below:** The native worker freezes its candidate and hands it directly to the leaf's Reviewer, and states that a finished turn is not AR acceptance; the Manager receives no routine report notice. Manifest-selected architect/manager/orchestrator operation capsules must inspect candidate/evidence before acceptance; a removed manager inspection sentence must fail the guard. The retained contradiction machinery checks authored instruction wording, not runtime acceptance transactions. The declared roster must match the dynamically scanned vocabulary speakers in both directions. The curation operation and Reviewer role carry local terminal truth; the raw Curator role does not speak that vocabulary and is not itself a roster speaker. Its old raw-role subcase is retired, not an executed passing case. The operation remains owed, and the whole-corpus contradiction sweep still includes unrostered files. [Historical source custody: `mcp/tests/test_lifecycle_turn_truth_doctrine.py` blob `74a051a27a76bfa2d21ab404b581911d5e391701` at code base `59b01fb8f72a38d2d27f9c37b8b9ca2513fd3fa0`; this is no current implementation claim.]

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
  an independent raw-role speaker claim. The Reviewer role retains local turn-only truth. The
  owner-validation half lives at the common home core/acceptance.md, which also states terminal
  truth. Composition and the common home do not turn a finished turn into semantic acceptance.
- **Each declared surface states its own owed clauses and does not deny them.** `OWED_STATEMENTS` is
  per-surface and contradiction-aware: a surface that states *and* denies fails `_assert_owed` and
  reads `CONTRADICTED`.
- **The sweep can still fail.** `DetectorTeethTests` runs every retired-claim detector against the
  historical contradicting text it was written for *and* against the shipped wording it must pass;
  `DeclaredLimitsTests` pins the detectors' own documented limits.

`classify_reading` returns three states — `STATED` / `ABSENT` / `CONTRADICTED` — and **silence is not
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
  census and owed sets track the corpus. The compact equivalent ‘proves only turn end’ is now recognized by the mechanical-reading and turn-end restriction expressions. Both compact and expanded statements followed by an acceptance claim must still classify CONTRADICTED; no path exception or disabled sweep is introduced.
- Detector teeth and declared-limit cases remain separate from changing corpus data.
  The native Worker-parent and coordinator-capsule cases add explicit instruction-boundary
  coverage; they do not execute an AR acceptance transaction.

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

## 260928-MIK-L99 — a leaf's agents hand over to each other

The turn-truth doctrine suite now pins the worker's direct freeze hand-over to the Reviewer in place of the old parent-report notice test; the roster and mechanical-reading checks are unchanged.

The relay detector requires an attributed relay action rather than mere co-occurrence of sweep, open and packet words; active and passive artifact-inspection examples still fail. Worker handoff checks bind Manager-first Reviewer creation and subsequent direct frozen-object delivery to their real sections, with per-clause deletion controls. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
### Docs References

No Domain Documentation source is configured for this repository; the boundary is repository-owned
canonical prose and the guard reads the corpus itself.

No configured `Domain Documentation` source applies; the doctrine under test is the repository's own canonical corpus.

### Repo-Internal References


- The common home owns terminal-only truth, recipient validation and the separate acceptance authority. [Past-epoch source caption, detached from live reference 1. Recorded citation custody: skills/l-01-agent-lifecycles/core/acceptance.md blob 2a112bdb1148478a8a719636588cb908fab01cac (available); historical event commit not identified. No historical event or intent inferred.]

Current source: The shared acceptance home distinguishes mechanical turn-end truth from artifact validity, requires the structurally current owner to validate before advancing state, and keeps recipient checks for direct peer handovers separate from Manager gate acceptance.

- The declared roster and vocabulary must equal the actual canonical speakers in both directions. [2]
- The whole-corpus contradiction sweep and three-state classifier retain the declared retired-claim vocabulary and explicit-denial handling. [Past-epoch source caption, detached from live reference 4. Recorded citation custody: mcp/tests/test_lifecycle_turn_truth_doctrine.py blob 74a051a27a76bfa2d21ab404b581911d5e391701 (available); historical event commit not identified. No historical event or intent inferred.]

[Past-epoch source caption, detached from live reference 4. Recorded citation custody: mcp/tests/test_lifecycle_turn_truth_doctrine.py blob 74a051a27a76bfa2d21ab404b581911d5e391701 (available); historical event commit not identified. No historical event or intent inferred.]

Anchor: `RETIRED_CLAIMS`, `contradictions`, `_reading_is_denied_in_place`, `classify_reading`

Current source: The detector scans promise views for the declared RETIRED_CLAIMS and classifies each text as stated, absent or contradicted. Contradictions take priority over a matching mechanical-only phrase, and an in-place denial does not count as a positive statement.
- Silence/contradiction controls, detector teeth and declared limits distinguish equivalent turn-end-only wording from acceptance; the compact and expanded state-plus-acceptance controls remain. [Past-epoch source caption, detached from live reference 5. Recorded citation custody: mcp/tests/test_lifecycle_turn_truth_doctrine.py blob 74a051a27a76bfa2d21ab404b581911d5e391701 (available); historical event commit not identified. No historical event or intent inferred.]

[Past-epoch source caption, detached from live reference 5. Recorded citation custody: mcp/tests/test_lifecycle_turn_truth_doctrine.py blob 74a051a27a76bfa2d21ab404b581911d5e391701 (available); historical event commit not identified. No historical event or intent inferred.]

Anchor: `SilenceIsNotContradictionTests`, `DetectorTeethTests`, `DeclaredLimitsTests`

Current source: The silence controls distinguish stated, absent and contradicted readings, including compact and expanded turn-end wording, split acceptance claims and in-place denial. Detector controls retain per-claim samples and whole-tree census; the declared-limit case pins the detector’s proximity-based misreading of another agent’s acceptance inside its window.



- The per-surface owed clauses, and the relay-mechanics surfaces the corpus still names. [Past-epoch source caption, detached from live reference 3. Recorded citation custody: mcp/tests/test_lifecycle_turn_truth_doctrine.py blob 74a051a27a76bfa2d21ab404b581911d5e391701 (available); historical event commit not identified. No historical event or intent inferred.]

[Past-epoch source caption, detached from live reference 3. Recorded citation custody: mcp/tests/test_lifecycle_turn_truth_doctrine.py blob 74a051a27a76bfa2d21ab404b581911d5e391701 (available); historical event commit not identified. No historical event or intent inferred.]

Anchor: `OWED_STATEMENTS` `RELAY_MECHANICS_SURFACES`

Current source: OWED_STATEMENTS declares each named surface’s required boundary clauses. RELAY_MECHANICS_SURFACES names the retained turn-report template; it is separate from the completion-truth roster and the mechanical-only reading vocabulary.




- The projection-side sibling that re-asserts the boundary clauses against the canonical doctrine tree and its one declared packaged copy. [6]


### Cross-Repo References

No external repository boundary is exercised by this guard; it reads this repository's canonical corpus
and its packaged copies.

No meaningful cross-repo references found.

## 260928-MIK-L172 — the acceptance surface states the sending obligation

The acceptance-surface marker list now expects the shipped clause instead of the retired completion-post sentence: a file hands itself over to nobody, the artifact is sent with `role_message` to the agent that waits, and a file on record wakes no one. The contradiction sweep and the roster are otherwise unchanged, and this remains an instruction-wording reading, not an executed acceptance.

- The shared acceptance home distinguishes mechanical turn-end truth from artifact validity, requires the structurally current owner to validate before advancing state, and keeps recipient checks for direct peer handovers separate from Manager gate acceptance. [1]
- OWED_STATEMENTS declares each named surface’s required boundary clauses. RELAY_MECHANICS_SURFACES names the retained turn-report template; it is separate from the completion-truth roster and the mechanical-only reading vocabulary. [3]
- The detector scans promise views for the declared RETIRED_CLAIMS and classifies each text as stated, absent or contradicted. Contradictions take priority over a matching mechanical-only phrase, and an in-place denial does not count as a positive statement. [4]
- The silence controls distinguish stated, absent and contradicted readings, including compact and expanded turn-end wording, split acceptance claims and in-place denial. Detector controls retain per-claim samples and whole-tree census; the declared-limit case pins the detector’s proximity-based misreading of another agent’s acceptance inside its window. [5]

- The relay detector requires an attributed relay action rather than mere co-occurrence of sweep, open and packet words; active and passive artifact-inspection examples still fail. Worker handoff checks bind Manager-first Reviewer creation and subsequent direct frozen-object delivery to their real sections, with per-clause deletion controls. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [7]
