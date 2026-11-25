# mcp/tests/test_review_external_git_movement_read.py

## Governing Overview

[mcp tests route overview](overview.md)

## Purpose

Raw Git movement is measured from retained commit evidence, with absent work-head proof kept unmeasured.

## Code Commentary

### Logic

The uncommitted candidate carries no observed work-branch commit. The live report stays `not-measured` with a reason and no transition, and a historical comparison receives no live movement. [5]

Commit-bound cases distinguish untouched, advanced and rewritten branches. Source-history replacement retains the recorded source and omits retired generation keys. Branch switches and unreadable channels remain distinct. Validator forgeries start from the published stale report. [6] [7] [8] [14]

The shared `TreeReceiptFixture` constructs the enclosure and its exact comparison. [2]

### Invariants And Boundaries

- A tree cannot stand in for observed commit proof.
- Unavailable is neither movement nor agreement.

### Invariants And Boundaries

- **The enclosure cases read measured production values.** Movement cases use the real Git enclosure
  and shipped boundary read. The validator case forges fields on a published movement value to check
  model contradictions. `test_documented_support_matrix_matches_the_measured_operations` is different:
  it takes no enclosure fixture and compares `render_git_transition_support()` with repository Markdown;
  it performs no Git movement or lifecycle operation.
- **The document contains the rendered support matrix verbatim.** `render_git_transition_support()`'s
  output must be a substring of `docs/reference/worktrees-c09.md`.

### Todos

None recorded.

## Evidence

### Docs References



### Repo-Internal References

- Current shared enclosure fixture. [2]


- Uncommitted tree supplies no observed work-head proof. [5]


- Source replacement without fabricated UUID. [6]


- Leaving the declared branch is a switch. [7]



- The commit-bound cases distinguish untouched, appended and rewritten work branches. The unread-channel case separates a measured memory rewrite from unavailable memory and declared-source channels. [8]



- Model rejects state contradictions. [14]


- The managed-sync sibling test records a memory-only move and checks its effect on the live review’s staleness. [25]

The enclosure cases use real Git and read the production boundary. Separate assertions distinguish unchanged, appended and rewritten work branches, branch switches and unavailable channels. The matrix test checks that repository Markdown contains the rendered support text.

### Docs References

No configured domain documentation could be checked for this module. The resolved memory layer's
`system/sources.md` carries no `Domain Documentation` category, so no documentation row is recorded
here. The one document these cases read is a repository file rather than an external source:
`docs/reference/worktrees-c09.md`. The matrix is under Raw Git Identity Boundary. The test searches the full document.

### Repo-Internal References (continued)

- **The sibling fixture this module shares rather than rebuilds.** [26]



- The documentation test requires the rendered support matrix as a substring of the complete Markdown file. [29]




### Cross-Repo References

No cross-repository contract is established by this file.

No cross-repository contract is established here. Git movement operations in the enclosure cases
use the fixture's temporary local repositories. The matrix case reads repository Markdown and the
validator case also constructs model forgeries; those operations are not Git subprocesses. No
cross-repo reference row is recorded for this module.

- **The lifecycle catalog names this module in the consumer lists for `_user_settings_guard.py` and the Node profile fixture lockfile.**

### Repo-Internal References (continued)

- The `integration` lane selects `mcp/tests/test_review_external_git_movement_read.py`. [27]
