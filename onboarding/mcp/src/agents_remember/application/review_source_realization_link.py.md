# mcp/src/agents_remember/application/review_source_realization_link.py

## Governing Overview

[application route overview](overview.md)

## Purpose

Answers one question for the source-content admission owner: **does a realization recorded in the
knowledge this comparison binds link this exact path?** Since MIK-L31 a tree comparison's proof entry
anchored at the path links it too (ruling 2026-09-30T05:36:19 Q1), so a proof's focused card opens its
full file like a realization's. It reads no source bytes and decides nothing
else; `application/review_source_admission.py` turns the answer into an admission or a refusal.

It exists because a statement can be realized by code the task did not change. The inventory stays
exactly the measured change set, and a reviewer still has to be able to read that unchanged code — but
only when **this** comparison's own recorded knowledge points at it (ICR-R03@v1 under the 2026-09-28
admission ruling, with R26 subject/comparison isolation preserved).

## Code Commentary

### Logic

**Which comparison's knowledge (`_bound_knowledge`).** The baseline is already required to be the
leaf's recorded base, so only the after tree can differ. When the requested after tree is the
candidate the leaf's review binds now, the knowledge is that same resolution's two halves (a live
leaf's halves, or a closed leaf's reopened generation). Otherwise the pair is superseded: the leaf's
published comparison generations are walked newest-first (`read_generation_refs`), the first whose
manifest records exactly the requested pair is reopened through `resolve_committed_leaf_review`, and
its retained halves answer. With no such generation the answer is a **determined** "no knowledge is
bound to the requested comparison" — the knowledge the leaf holds now is never substituted. A
generation that records the pair but cannot be reopened is **undetermined**.

**Which halves (`_halves`).** Before and after, except that a half a closed leaf's generation manifest
did not retain is left out rather than looked for elsewhere.

**Which spelling (`_anchor_spelling`).** The requested path must validate as a `PathSeed` **and** the
validated value must equal the request string. The seed rule strips surrounding whitespace, so without
the equality a padded spelling (`" src/x.py"`, a trailing tab or newline) would be answered with the
link of the path it normalizes to (L43-R1-F1). A non-anchor spelling is a determined negative.

**One half's answer (`_side_reading`).** The snapshot's identity is resolved from the file with
`open_read_context`, then the read owner's exact claim-at-path query `fetch_realizations_at_path` is
run on a read-only connection. That query expands no family, so the selection bound that caps scope
reads cannot turn a linked path into a refusal (L43-R1-F2). A missing file or a storage, SQLite, OS
or value error while resolving or querying makes the half `unread` with its cause; a row is `linked`;
no row is `not_linked`. **Proofs of a tree comparison (MIK-L31):** when no realization row matches,
`_proof_at_path` asks the derived index's own `ix_entry` table for a `kind = 'proof'` entry at exactly the path
(proof entries, MIK-R28, have no table in the store's logical schema); a dataset has no `ix_entry` table and
answers `False`, so a dataset comparison is asked nothing more. A proof link reads "the <side> snapshot records a
proof here". A missing snapshot file is also marked `absent` on its reading.

**The answer (`RealizationLink`).** `linking_sides` names the halves that link the path; `detail` is
one sentence naming the comparison and what each half answered (`_sentence`), which the admission
owner carries verbatim into its admission detail or refusal. `determined` is false exactly when no
half links the path and some bound knowledge was not read — one established link is enough to admit.
`never_initialized` (MIK-R31 rule 6, ICR-L43 review R2 O1) is true when some half was unread and every unread
half does not exist at all: the leaf's knowledge was never created, so the admission owner's remedy is to
initialize it rather than restore or repair a damaged snapshot. The answer is composed by `_link_of`, split out of
`recorded_realization_link` when the `never_initialized` computation raised its radon rank to C (now B or
below).

### Conventions

`__all__` publishes `RealizationLink` and `recorded_realization_link`. Intermediate values
(`_SideReading`, `_BoundKnowledge`) are frozen dataclasses, not wire models. The module re-uses
existing owners (knowledge read, committed-leaf reopen, generation refs/manifest, namespace record)
and adds no store, schema or second reader; the direct `fetch_realizations_at_path` use follows the
same two-step pattern as `application/review_attribution.py`.

### Invariants And Boundaries

- **Only the requested comparison's knowledge answers.** Current pair → the resolution's halves;
  superseded pair → only a generation that recorded exactly that pair; otherwise nothing. No other
  leaf, master or published dataset is consulted.
- **Exact spelling only.** A path is linked only for the exact string a recorded anchor carries.
- **Anchor staleness is not a criterion.** A recorded anchor whose blob no longer matches still links
  its path for reading (Architect ruling closing L43-R1-F4 (1)); the content read beside it shows the
  bytes the requested endpoints actually hold.
- **Unreadable knowledge supports no admission and no negative.** It yields an undetermined answer
  with its cause.
- **A proof links only in an index-backed comparison, and only for the paths its recorded proof entries
  name** (review R1 focus check 3: an exact `ix_entry` query, reached only when no realization matches).
- **Two connections, no mislabel.** Identity is checked in one read-only connection and the claim
  query runs in a second; R2 judged every file-swap interleaving to be at worst a false refusal, never
  an admission of an unlinked path.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of which comparison, which fact, what is not a criterion, and why unreadable knowledge is undetermined.** [1]
- The published surface and the half order. [2]
- **The answer value: linking halves, the stated sentence, whether the negative was established, and whether the unread knowledge was never created.** [3]
- **The entry point: bind the comparison, check the spelling, read the namespace, ask each half; the halves' answer composed apart.** [4]
- **Exact-spelling check: the validated seed must equal the request string.** [5]
- **Comparison binding: current pair, recorded superseded pair, or nothing — never the leaf's current knowledge.** [6]
- Halves a closed leaf's generation did not retain are not read. [7]
- **One half asked by the exact claim-at-path query, with unreadable kept apart from not linked, and an absent snapshot marked.** [8]
- A tree index's proof entry at the path links it; a dataset (no `ix_entry`) answers nothing. [9]
- The read owner's identity resolution and exact claim-at-path query this module re-uses. [10]
- The generation owners that bind a superseded pair to its retained knowledge. [11]
- The namespace record (the record beside the bytes, or, since MIK-R25, a derived knowledge index's own namespace) and the path-seed shape rule. [12]
- **Cases: cross-comparison refusal, recorded historical bytes after the tree moves, closed leaf, padded spellings, and the lowered selection bound.** [13]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads only the knowledge snapshots bound
to one leaf's comparison in one repository namespace.

No meaningful cross-repo references found.
