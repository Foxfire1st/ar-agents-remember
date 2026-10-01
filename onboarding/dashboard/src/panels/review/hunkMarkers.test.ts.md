# dashboard/src/panels/review/hunkMarkers.test.ts

## Governing Overview

[dashboard/src/panels route overview](../overview.md)

## Purpose

**The marker model over real served classifications (12 cases).** Every body is a real per-file classification of
MIK-L32's lane fixture world (real code and memory Git trees, reopened as the reviewer reopens a comparison) in six
scenarios: `precuration`, `curated`, `before_unread`, `after_unread`, `both_unread` and `partial`
(`hunkMarkers.classifier.captured.json`, receipt `hunkMarkers.capture-provenance.json`); one case also reads the real
`notes.py` body of the scratch leaf (`markerReturn.file.captured.json`).

## Code Commentary

### Logic

- **What each hunk names (8).** The curated `lines.txt` replace hunk lists INV-AAAAAA with its three family
  occurrences (member of FAM-F00001, removed or reassigned in after for FAM-F00002, before-only for FAM-F00003) and
  INV-BBBBBB with `No recorded family`, as `2 intents`; targets select the member row of a named family, or the
  invariant alone; one revision recorded on both sides merges into one occurrence, and an insertion-only hunk is named;
  a proof is `INV-AAAAAA · test` with its facet, never counted with realizations; unknown membership with and without a
  family (`after_unread`, `partial`), and the reason carried to the target (ruling Q3); `before_unread` keeps the
  readable side's links and names the unread side's changed lines unknown (`1 intent · unknown`, ruling Q2); a
  confirmed-unregistered file (`new.py`) and a file no side of which is readable get one file mark.
- **Where each mark sits (4).** Split: the deletion on the before side; inline: on the after line below its removed
  lines, or the last drawn after line at the end of the file, and a mid-file deletion (the real `notes.py` L210) below
  its removed line (review R1 N1); a window drawing two neighbours marks all three hunks (the L32 F5 carry); a
  one-sided pane on the side it draws.

### Conventions

- The bodies are read with `readFileSync` next to the test; `classified(scenario, file)` picks one.

### Invariants And Boundaries

- Proves the candidate invariant recorded on `hunkMarkers.ts.md` (marks only from the owner's response). The worker's
  mutations M1–M7 and N1 each fail at least one of these cases.

### Todos

No additional work is asserted by this card.

## Evidence

### Docs References

No domain documentation source is configured; the requirement packet `MIK-R34@v1` (adopting `ICR-R34@v1`), the adopted `ICR-R24@v3` item 2 and the architect's rulings live outside the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The six scenarios of real bodies. [1]
- What each hunk names: occurrences, targets, proofs, unknown membership and its reason, the unread side, file marks. [2]
- Where each mark sits, including a window's neighbours and an inline mid-file deletion. [3]
- The model under test. [4]

### Cross-Repo References

No cross-repo boundary is crossed by this file.
