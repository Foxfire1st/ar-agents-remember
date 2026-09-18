# mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-15T00:51+00:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l23` uncommitted source; base `c5a74a85af20a8fb48cc44f59de7e926d589d3fc` |
| governingOverview | `../../overview.md` |

## Governing Overview

[overview](../../overview.md)

## Purpose

Reopen citation claims whose anchored evidence changed since verification.

Since 260831-LOCR-L33 the review surface also distinguishes **where the range came from**. A range
written by the mechanical anchor-range projection is indistinguishable in the document from a
curator's edit; only the generated `Update History` bullet records it. So `generated_repair_bullets`
reads that bullet, and where it names this claim's anchors the surfacing item stops asserting the
citation is current and asks the support question instead: the projection resolves an exact NAME,
never the claim's subject, so a range that arrived that way can point at a declaration the claim was
never about.

That item is **ENFORCED (`severity="error"`), not report-only**, and the severity is conditional on
the bullet: `"error" if bullets else "warning"`. The rationale is that a mechanically projected range
is *unverified evidence* — nothing in the tree records whether anyone reviewed the projection, and
this check cannot prove that a review happened, so evidence it cannot verify must force an explicit
disposition rather than offer a note a curator can read past. `_gate_result` moves only
`severity == "warning"` findings into `surfacedFindings`, so while this item was always `warning` it
was reported and then dropped from the enforced set — readable and ignorable. **The cost is
deliberate and total: every mechanically projected range now blocks until somebody disposes of it.**
The ordinary (non-projected) evidence-change item keeps its `warning`, because there the currency
test *is* evidence.

## Code Commentary

### Logic

The pending-current-code exception is proved from real history: the failing attribution
must name the current code HEAD, that HEAD must have no attributed memory output yet, and
`Histories.memory_mappings` must contain an attribution for an ancestor code commit. The same
observation supplies those mappings without reading the ledger cache. A cache miss is neither
provenance evidence nor a refusal; a head with no attributed ancestor is not treated as pending.

The projection-aware surface:

- `PROJECTION_BULLET` / `REPOINTED_TO` (constants) — The generated `Update History`
  bullet header a mechanical anchor-range projection writes (`deterministic_projection.history_bullet`)
  and the clause it uses to introduce the ranges it chose.
- `generated_repair_bullets` (function) — The Update History bullets recording that a
  mechanical repair moved THIS claim's range. `deterministic_projection.history_section_line` bounds the
  scan to the canonical section, and the anchor list is read **between** the bullet header and its
  `repointed to` clause: the ranges after that clause carry file paths, which would otherwise match an
  anchor that merely shares its name with a file the repair wrote. Every named anchor is matched by
  exact text, so another claim's bullet in the same document is not evidence about this one.
- `_names_an_anchor` (function) — Requires both the bullet header and the
  `repointed to` clause, then matches this claim's anchors against the clause before that phrase.
- `_repointed_ranges` (function) — The ranges the bullet recorded, read from the
  `repointed to` clause and stopped at `deterministic_projection.NO_IMPACT_MARKER`, so the item can
  quote what the citation now reads.
- `_projected_review_message` (function) — The review item for a range that arrived by
  mechanical projection. It says the citation is **NOT shown to be current** and asks two things:
  whether the construct the new range covers supports the claim's own words, and whether the range was
  projected or rebound from a mention the claim was verified against to the anchor's declaration
  elsewhere.
- `surfaced_finding` (function) — Reads the document's generated repair bullets first;
  where they name this claim's anchors it publishes the support question, otherwise it keeps the
  original currency assertion. **Severity is `"error" if bullets else "warning"`**: the projected
  branch is enforced, the ordinary currency branch stays report-only.
- `evaluate_claim` (function) and `check_onboarding_root` (function) —
  Thread the document's `lines` through to `surfaced_finding`; `check_onboarding_root` groups each
  document's `(relative, lines, claims)` so the bullet scan reads the bytes already in hand.

The three-way split of a detected change is otherwise unchanged: absent or ambiguous anchors and
unverifiable provenance are hard findings; a changed construct with a current citation is the curator's
review surface, clearing with no commit; only a changed construct whose pointer is stale is an enforced
reopened claim. What changed is that "current citation" is no longer sufficient for the report-only
bucket when a generated repair wrote the range — that case leaves the report-only bucket entirely.

The rest of the module surface (the entries marked with a description are the ones this change
touched; ranges shown are the pre-change values and are re-measured only where a row below cites
them):

- `LocalSource` (class)
- `Candidate` (class)
- `CurrentFiles` (class)
- `SourceViews` (class) — Parsed source revisions shared by every claim in one gate run.
- `Evaluation` (class)
- `InvalidReason` (class) — One reason a claim cannot be compared, plus whether any edit could ever
  clear it; `uneditable=True` marks the anchor-multiplicity class that closeout owns.
- `claims_in` (function)
- `finding` (function)
- `provenance_finding` (function) — Carries the finding's `closeout_owned` flag through to
  `QualityFinding`, so the routing is one structural fact rather than a message match.
- `changed_finding` (function)
- `selected_current` (function)
- `selected_historical` (function)
- `local_changes` (function) — missing-source handling reports the absent-at-stamp-plus-absent-now
  case explicitly and lets each anchor judge the whole-new-file currency rule (`_anchor_in_cited_range`)
  instead of failing on any absent-at-stamp source.
- `anchor_change` (function)
- `dependency_changes` (function)
- `_closeout_owned_provenance` (function) — Splits the `closeout_owned` rows out of the finding list
  before the debt demotion runs; `_gate_result` publishes them under `closeoutOwnedFindings`.
- `_pre_task_revision` (function), `_row_predates_the_task` (function),
  `_committed_document_lines` (function), `_working_tree_row` (function) — The demotion's
  pre-task-revision test: the memory worktree's `HEAD`, and the finding's own row looked up by exact
  text in that revision's copy of its document.
- `check_onboarding_root` (function) — Compare every complete claim against its own historical
  provenance; selected prepared runs may retain explicit predecessor-chain code anchors while this
  function reads current working-tree bytes.

The currency rule the surface test uses — an exactly-once anchor and some cited range still holding
the construct's declaration line — is what a mechanically projected range satisfies BY CONSTRUCTION,
because the projection chose the declaration it wrote. That is the whole reason the generated bullet
is read first. Detected change splits three ways: absent or ambiguous anchors and unverifiable
provenance are hard findings; a changed construct with a current citation is the curator's review
surface, clearing with no commit; only a changed construct whose pointer is stale is an enforced
reopened claim. What changed since 260915-KS-L23 is that "current citation" now means the range
covers the DECLARATION's own line, not the widened extent's start:

- `Extent.declaration` is what `_anchor_in_cited_range` reads for a `DEFINITION` extent
  (`extents.definitions` populates it from `grammars.bindings`), because a decorated Python
  definition's extent is widened to cover its decorator. A card citing such a declaration at exactly
  its own lines used to reopen its own claim while the identical citation one line earlier passed.
  The reopen rule itself is not relaxed: the range must still begin at or before the declaration and
  still end at or after it, so a range starting inside the body reopens exactly as before.

Two provenance facts changed with it:

- `_demote_preexisting_provenance_debt` keys on the **row's pre-task revision**, not on document
  dirtiness. `_pre_task_revision` reads the memory worktree's `HEAD` — the commit the run's working
  tree started from — and `_row_predates_the_task` reads the finding's row from the working tree at
  the finding's own line and looks it up **by exact text** in the same document at that revision. A
  line inserted above the row changes nothing; correcting the row itself makes the row the leaf's
  own. Every unusable input fails closed: an unreadable document, a path that escapes `onboarding/`,
  a card this task created, a line past the end of the file, or a blank row all leave the finding
  enforced. Keying on document dirtiness asked the wrong question, because a curator's correction
  pass is exactly what makes every document it touches dirty, so the demotion was structurally
  unreachable for the rows a curator meets (0 of 4 demoted, measured at L18).
- Anchor multiplicity is **closeout-owned**, not curator debt. The multiplicity reasons are marked at
  their two creation sites with a typed `InvalidReason(detail, uneditable=True)`, and a claim whose
  every invalid reason is uneditable is published with `closeout_owned=True`; `_gate_result` splits
  that bucket before the demotion and reports it as `closeoutOwnedFindings` + `closeoutOwnedCount`.
  An anchor resolving more than once in the cited FILE cannot be made unique by any edit a curator
  may write — narrowing changes no occurrence count and splitting adds a row — so the stamp decision
  is closeout's, and the row leaves `findingCount` and the curator-actionable arithmetic while
  staying in the report.

This is what lets the citation gate run before the code commit at closeout (260731-EFA-L16). The
absent-at-stamp rule extends to whole source files added after the stamp (260731-EFA-L8): a unique
working-tree anchor inside a cited range surfaces report-only; absent, ambiguous, or stale constructs
stay hard.
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
- **A mechanically projected range passes the currency test by construction.** The projection picked
  the declaration it wrote, so "the anchor resolves and a cited range holds its declaration line" is
  the one question whose answer cannot repair the damage. When the document's generated repair bullet
  names this claim's anchors, the item must ask the support question instead of asserting currency —
  the projection resolves an exact NAME, never the claim's subject.
- **A mechanically projected range is enforced, not surfaced.** The projected variant is
  `severity="error"`; the ordinary evidence-change item stays `warning`. A projected range is
  unverified evidence, so it must force a disposition rather than land in the report-only bucket a
  curator may read past; the accepted cost is that every projected range blocks until it is disposed
  of. Do not restore the warning severity without re-deciding that trade.
- **Nothing demotes this item.** `_demote_preexisting_provenance_debt` moves only findings whose
  `code == INVALID` into the debt bucket, and then only when the row itself is carried by the
  pre-task revision; a `citation_claim_reopened` finding is never demoted to pre-existing debt —
  touched or untouched document alike. A `closeout_owned` finding is split out before that call, so
  it never reaches the debt bucket either.
- **Provenance debt is decided per ROW, not per document.** A row the task created or corrected is
  the task's own and stays enforced; a row the document merely carries from the pre-task revision is
  inherited debt. An anchor-multiplicity row is neither: no curator edit can discharge it, so it is
  published as closeout-owned rather than billed as repairable debt.
- **With no git view, every finding stays enforced.** `_pre_task_revision` returns `None` when
  `git rev-parse HEAD` fails, and the demotion path then returns the enforced findings unchanged —
  the fail-closed direction. Nothing about the projected item can be swallowed there.
- The bullet scan is bounded and anchored on purpose: it reads only the canonical `Update History`
  section, only text **before** the bullet's `repointed to` clause (the ranges after it carry file
  paths that could match an anchor sharing a file's name), and only a bullet naming this claim's
  anchors by exact text. A bullet for another claim in the same document is not evidence about this
  one.

### Todos

None.

## Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured external domain source applies. | — | — |

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Pending HEAD attribution requires a genuinely attributed ancestor and never reads the cache file. | `_mapping_pending_for_code_head` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:737-762 |
| Defines the class `LocalSource`. | `LocalSource` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:117-123 |
| Defines the class `Candidate`. | `Candidate` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:126-130 |
| Defines the class `CurrentFiles`. | `CurrentFiles` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:133-140 |
| Defines the class `SourceViews` — Parsed source revisions shared by every claim in one gate run.. | `SourceViews` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:128-167 |
| Defines the class `Evaluation`. | `Evaluation` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:170-221 |
| Defines the function `claims_in`. | `claims_in` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:239-253 |
| Defines the function `finding`. | `finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:256-269 |
| Defines the function `provenance_finding`. | `provenance_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:272-294 |
| Defines the function `changed_finding`. | `changed_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:297-308 |
| Defines the function `selected_current`. | `selected_current` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:411-422 |
| Defines the function `selected_historical`. | `selected_historical` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:425-436 |
| Defines the function `local_changes`. | `local_changes` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:416-449 |
| Defines the function `anchor_change`. | `anchor_change` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:452-508 |
| Defines the function `dependency_changes`. | `dependency_changes` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:703-734 |
| Defines the function `evaluate_claim` — now threads the document's lines to `surfaced_finding`. | `evaluate_claim` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:781-832 |
| Defines the function `check_onboarding_root` — Compare every complete claim against its own historical provenance, group each document's lines with its claims, and pass retained predecessor-chain anchors into `Histories`. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:835-930 |
| The generated `Update History` bullet header and range clause the projection writes and this check reads back. | `PROJECTION_BULLET`; "Update History" | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:80-82; mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:84 |
| The bounded scan for the bullets that record a mechanical repair of THIS claim's range. | `generated_repair_bullets` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:311-323 |
| The review item that stops asserting currency and asks the support question when a projected range is detected. | `_projected_review_message` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:315-338 |
| The review item that reads the generated bullets first and returns `error` for the projected variant and `warning` otherwise. | `surfaced_finding` | mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:341-385 |
| The generated bullet shape this check parses, and the section bound it scans within. | `history_bullet` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:129-150 |
| The executor that pins the enforced projected item, the fail-closed no-git-view path, and the unchanged warning for a non-projected change. | `test_a_projected_range_is_enforced_with_the_support_question_not_currency` | mcp/tests/test_memory_citation_resolution.py:954-983 |
| The canonical Update History section line whose presence bounds the generated-bullet scan. | `history_section_line` | mcp/src/agents_remember/memory_quality/style/citations/deterministic_projection.py:116-126 |


## Cross-Repo References

No separate cross-repository implementation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external implementation source applies. | — | — |

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `_mapping_pending_for_code_head` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:737-762. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `LocalSource` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:117-123. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `Candidate` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:126-130. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `CurrentFiles` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:133-140. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `claims_in` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:239-253. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `finding` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:256-269. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `provenance_finding` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:272-294. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `changed_finding` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:297-308. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `selected_current` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:411-422. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `selected_historical` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:425-436. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `dependency_changes` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:703-734. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `evaluate_claim` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:781-832. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `check_onboarding_root` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:835-930. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `generated_repair_bullets` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:311-323. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T17:30:57+00:00: Generated citation repair: `test_a_projected_range_is_enforced_with_the_support_question_not_currency` repointed to mcp/tests/test_memory_citation_resolution.py:954-983. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T19:20+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): corrected three claims this change falsified. (1) `_anchor_in_cited_range` now reads the `declaration` line of a `DEFINITION` extent instead of the widened extent's start, so a card citing a decorated Python declaration at its OWN lines no longer reopens its own claim (item 14; the recorded 0-based/1-based diagnosis was wrong — every extent producer was already 1-based, and the mechanism is `grammars._widened` growing the extent through `decorated_definition`). The reopen rule itself is unrelaxed: the range must still begin at or before the declaration and end at or after it. (2) `_demote_preexisting_provenance_debt` keys on the ROW's pre-task revision (`_pre_task_revision` reads the memory worktree's `HEAD`; `_row_predates_the_task` looks the finding's own row up by exact text in that revision's copy of its document) instead of on document dirtiness, which made the demotion structurally unreachable for the rows a curator meets. (3) The anchor-multiplicity reasons are marked `InvalidReason(uneditable=True)`, and `_gate_result` splits that population before the demotion and publishes it as `closeoutOwnedFindings` + `closeoutOwnedCount` — reported, out of `findingCount` and out of the curator-actionable arithmetic. Documentation only: no source byte was touched by this pass. `lastVerifiedCommitHash`/`lastVerifiedCommitDate` are NOT advanced — these sources are uncommitted, so no commit carries their bytes; the candidate is named in the `reviewedWorkingCandidate` metadata row and the governed closeout owns the real commits.

2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-15T00:51+00:00 — LCA-L9 current candidate: Rebased pending-current-code citation handling on attributed ancestor commits without cache authority. Reviewed the uncommitted source and current references; existing verification commit/date and all prior history are retained. No landed or test-execution claim.

- 2026-09-13T02:05+02:00 — 260831-LOCR-L33 curator (delta after publish): the projected-range variant
  of `citation_claim_reopened` is now `severity="error" if bullets else "warning"`, so it is
  **enforced** rather than report-only. Recorded the rationale (a mechanically projected range is
  unverified evidence — nothing records whether anyone reviewed the projection and the check cannot
  prove a review happened, so it must force an explicit disposition) and the **cost** (every
  mechanically projected range now blocks until somebody disposes of it). Also recorded that the
  ordinary evidence-change item keeps its `warning`, that `_demote_preexisting_provenance_debt`
  demotes only `code == INVALID` so this item is never demoted, and that with no git view every
  finding stays enforced. **This supersedes the earlier L33 entry that described the warning severity
  as an open, undecided policy call**: the call is now made and it is enforced. Re-measured every
  module-surface and reference range for the grown docstring. Verification metadata remains
  closeout-owned; no acceptance claim.
- 2026-09-12T23:59:24+00:00: Generated citation repair: `Candidate` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:111-115. No content impact: mechanical anchor-range projection bound to citation source snapshot 4a22e48ac28c91e3e49addaa189c7b7faec69ca86011782c4a4f607ce34e37b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T23:59:24+00:00: Generated citation repair: `claims_in` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:224-238. No content impact: mechanical anchor-range projection bound to citation source snapshot 4a22e48ac28c91e3e49addaa189c7b7faec69ca86011782c4a4f607ce34e37b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T23:59:24+00:00: Generated citation repair: `finding` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:241-254. No content impact: mechanical anchor-range projection bound to citation source snapshot 4a22e48ac28c91e3e49addaa189c7b7faec69ca86011782c4a4f607ce34e37b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T23:59:24+00:00: Generated citation repair: `provenance_finding` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:257-271. No content impact: mechanical anchor-range projection bound to citation source snapshot 4a22e48ac28c91e3e49addaa189c7b7faec69ca86011782c4a4f607ce34e37b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T23:59:24+00:00: Generated citation repair: `selected_current` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:388-399. No content impact: mechanical anchor-range projection bound to citation source snapshot 4a22e48ac28c91e3e49addaa189c7b7faec69ca86011782c4a4f607ce34e37b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T23:59:24+00:00: Generated citation repair: `selected_historical` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:402-413. No content impact: mechanical anchor-range projection bound to citation source snapshot 4a22e48ac28c91e3e49addaa189c7b7faec69ca86011782c4a4f607ce34e37b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `LocalSource` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:98-104. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `Candidate` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:107-111. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `CurrentFiles` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:114-121. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `changed_finding` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:270-281. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `selected_current` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:376-387. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `selected_historical` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:390-401. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `local_changes` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:404-437. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `anchor_change` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:440-496. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-12T22:45:49+00:00: Generated citation repair: `dependency_changes` repointed to mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py:569-598. No content impact: mechanical anchor-range projection bound to citation source snapshot 7464238939d75c2065358d53c0f2e066dda635c5705830dfbe24fff068177c35; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-13T00:40+02:00 — 260831-LOCR-L33 curator: recorded the projection-aware review surface.
  The item now reads the document's generated `Update History` bullet for a mechanical repair naming
  this claim's anchors, and in that case stops asserting the citation is current and asks two things:
  whether the construct at the new location supports the claim's own words, and whether the range was
  projected or rebound to a different file. Recorded why: the currency test — the anchor resolves and
  a cited range holds the changed construct's declaration — is satisfied BY CONSTRUCTION by a
  projected range, because the projection chose the declaration it wrote, so a curator asked only
  that question could only answer it yes; production rebound a claim about two adjacent tool names to
  the registrar definitions that declared them while reporting `No content impact … claim bytes
  unchanged`. Recorded the bounded scan (canonical section, only text before the `repointed to`
  clause, exact anchor text) and that **severity is still `warning` because whether a projected range
  should block is a separate, undecided policy call** — not settled. Verification metadata remains
  closeout-owned; no acceptance claim.

- 2026-09-10T04:35+02:00 — CCR-L42 final predecessor-history curation: updated the current
  `check_onboarding_root` body and range to record explicit retained code-history anchors while
  preserving current working-tree reads and strict standalone provenance; verification metadata
  remains closeout-owned.

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
