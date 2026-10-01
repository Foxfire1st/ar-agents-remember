# mcp/src/agents_remember/memory_quality/style/citations/claim_reopen.py

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

## Evidence

### Docs References

No Domain Documentation source is configured in the resolved memory repository. The current
contract is supported by the implementation and the authorized cache-retirement requirement.

No configured external domain source applies.

### Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

- Pending HEAD attribution requires a genuinely attributed ancestor and never reads the cache file. [1]
- Defines the class `LocalSource`. [2]
- Defines the class `Candidate`. [3]
- Defines the class `CurrentFiles`. [4]
- Defines the class `SourceViews` — Parsed source revisions shared by every claim in one gate run.. [5]
- Defines the class `Evaluation`. [6]
- Defines the function `claims_in`. [7]
- Defines the function `finding`. [8]
- Defines the function `provenance_finding`. [9]
- Defines the function `changed_finding`. [10]
- Defines the function `selected_current`. [11]
- Defines the function `selected_historical`. [12]
- Defines the function `local_changes`. [13]
- Defines the function `anchor_change`. [14]
- Defines the function `dependency_changes`. [15]
- Defines the function `evaluate_claim` — now threads the document's lines to `surfaced_finding`. [16]
- Defines the function `check_onboarding_root` — Compare every complete claim against its own historical provenance, group each document's lines with its claims, and pass retained predecessor-chain anchors into `Histories`. [17]
- The generated `Update History` bullet header and range clause the projection writes and this check reads back. [18]
- The bounded scan for the bullets that record a mechanical repair of THIS claim's range. [19]
- The review item that stops asserting currency and asks the support question when a projected range is detected. [20]
- The review item that reads the generated bullets first and returns `error` for the projected variant and `warning` otherwise. [21]
- The generated bullet shape this check parses, and the section bound it scans within. [22]
- The executor that pins the enforced projected item, the fail-closed no-git-view path, and the unchanged warning for a non-projected change. [23]
- The canonical Update History section line whose presence bounds the generated-bullet scan. [24]


### Cross-Repo References

No separate cross-repository implementation claim is made.

No external implementation source applies.
