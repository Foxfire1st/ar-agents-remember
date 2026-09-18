# mcp/tests/test_lifecycle_turn_truth_doctrine.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_turn_truth_doctrine.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T22:19+02:00 |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

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
  not declared fails just as a declared surface that went silent does.
- **Each declared surface states its own owed clauses and does not deny them.** `OWED_STATEMENTS` is
  per-surface and contradiction-aware: a surface that states *and* denies fails `_assert_owed` and
  reads `CONTRADICTED`.
- **The sweep can still fail.** `DetectorTeethTests` runs every retired-claim detector against the
  historical contradicting text it was written for *and* against the shipped wording it must pass;
  `DeclaredLimitsTests` pins the detectors' own documented limits.

`classify_reading` returns three states — `STATE` / `ABSENT` / `CONTRADICTED` — and **silence is not
contradiction**: architect, designer and orchestrator readings are declared `ABSENT` legitimately, and
only a surface that owes a clause must state it. Conversely every canonical surface, owed or not, must
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
- Protected classes (`DetectorTeethTests`, `DeclaredLimitsTests`) and every detector constant are
  byte-unchanged by this leaf; only data segments and one case target moved.

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

## Docs References

No Domain Documentation source is configured for this repository; the boundary is repository-owned
canonical prose and the guard reads the corpus itself.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source applies; the doctrine under test is the repository's own canonical corpus. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The doctrine's one home, which the census and the shared-root case follow. | `# Core — Completion Truth And Handoff Acceptance (one home — this file owns the truth boundary)` | skills/l-01-agent-lifecycles/core/acceptance.md:1-1 |
| The declared roster and the vocabulary whose speakers it must equal, in both directions. | `COMPLETION_TRUTH_ROSTER`; `COMPLETION_TRUTH_VOCABULARY` | mcp/tests/test_lifecycle_turn_truth_doctrine.py:112-128; mcp/tests/test_lifecycle_turn_truth_doctrine.py:132-132 |
| The per-surface owed clauses, and the relay-mechanics surfaces the corpus still names. | `OWED_STATEMENTS`; `RELAY_MECHANICS_SURFACES` | mcp/tests/test_lifecycle_turn_truth_doctrine.py:478-529; mcp/tests/test_lifecycle_turn_truth_doctrine.py:138-144 |
| The contradiction sweep and its three-state reading classification. | "Every retired-claim shape this text promises; first evidence per claim, in document order."; "Three-state reading of one surface: stated, silent, or contradicted." | mcp/tests/test_lifecycle_turn_truth_doctrine.py:397-577; mcp/tests/test_lifecycle_turn_truth_doctrine.py:598-610 |
| The protected teeth classes, byte-unchanged by this leaf and the reason a limit cannot be edited to pass. | `DetectorTeethTests`; `DeclaredLimitsTests` | mcp/tests/test_lifecycle_turn_truth_doctrine.py:949-1016; mcp/tests/test_lifecycle_turn_truth_doctrine.py:1017-1052 |
| The projection-side sibling that re-asserts the same clauses against canonical plus the nine generated copies. | `PROJECTED_BOUNDARY_CLAUSES`; `BoundaryClause` | mcp/tests/test_sync_scripts.py:101-129 |

## Cross-Repo References

No external repository boundary is exercised by this guard; it reads this repository's canonical corpus
and its packaged copies.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-18T05:26:45+00:00: Generated citation repair: `COMPLETION_TRUTH_ROSTER`; `COMPLETION_TRUTH_VOCABULARY` repointed to mcp/tests/test_lifecycle_turn_truth_doctrine.py:112-128; mcp/tests/test_lifecycle_turn_truth_doctrine.py:132-132. No content impact: mechanical anchor-range projection bound to citation source snapshot 70078cc4ca208e40e9a66742bdc38893ecfb1757ca7d77a526e6ba2159339959; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T22:19+02:00 — 260915-CAPS-L16 curator: created this card. The module is **260831-LOCR's
  landed guard**, re-pointed by this leaf at the master's consolidated corpus as a declared cross-task
  change: `COMPLETION_TRUTH_ROSTER` moved 8 → 14 rows so the census holds in both directions at the
  corpus as shipped, the whole-boundary owed set moved from the retired `SKILL.md` section to
  `core/acceptance.md`, five per-role owed markers were re-quoted at the files' current words, the
  shared-root case was re-pointed and renamed, and one **additive** `ConvergenceTeethTests` class was
  added. **No detector was touched**: `DetectorTeethTests` and `DeclaredLimitsTests` are byte-identical
  and the contradiction detector still fails synthetic contradicting samples, so the guard kept its
  teeth while its data moved. This card records what defends what (including that silence is not
  contradiction, and that declaration is a census rather than a preference), because the four
  mechanisms are not interchangeable and a later reader who conflates them will repair the wrong one.
  Verification metadata is pinned to this leaf's synced base `8997e184` because the candidate is
  deliberately uncommitted — the governed closeout stamps the real code commit, and no hash or
  fingerprint was invented here.
