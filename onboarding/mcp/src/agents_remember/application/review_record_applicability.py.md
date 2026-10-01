# mcp/src/agents_remember/application/review_record_applicability.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**The attribution half of one review: which supplied record may be displayed beside the subject the
request selected, and why.** `ICR-R14@v1` guarantees that every owner-produced collection reaches the
surface; this module is the separately falsifiable half that stops the panes from implying an
association the records never establish. The defect it removes is F09's: the adapter used to hand the
candidate-wide review matrix and every supplied assessment to whichever subject was selected, so a
valid assessment of a *sibling* invariant appeared in both panes of a different invariant.

The classification reads **two** things and nothing else: the recorded population one selection reaches
([`application/review_recorded_selection.py`](review_recorded_selection.py.md) — the selected subject,
the revisions the selection records for it, the identities its recorded relationship rows reach and the
spelling of the relationship that reached each) and **each record's own recorded bindings**. No label,
path spelling, display version or revision *nearest* to the selection participates, because none of
them is a statement an author made about which subject a record is about. That is the packet's own
Forbidden Overreach ("do not infer subject membership, compatibility or revision lineage from
labels/text") made structural: the module holds no similarity, no score and no nearest-match helper.

**One projection, six outcomes, produced once per review read.** `review_applicability(...)` is called
once by the composition, before either pane renders anything, and returns `AppliedRecords` — the
panes' port. A record whose own recorded subject/revision
binding names the selected subject is `direct` in the displayed generation and `historical` when its
recorded generation input is another one; a record whose recorded subject is a different identity the
selection reaches through an explicit recorded relationship becomes a labelled context row; a record
whose recorded subject is a subject this comparison records and the relationships do not reach is
`unrelated` and is **not** handed to a pane at all; a binding that cannot be resolved is displayed
`unresolved` with its actual references and the reason; and a record bound to the compared candidate —
or any record of a review that selected no subject — is `candidate`. Filtering is therefore stated as
arithmetic rather than performed silently: the panes' own collections carry only the records the
selected subject may be judged by, and the six-way count of every supplied collection travels beside
them.

## Code Commentary

### Logic

**`AppliedRecords` is the port the panes consume, and it is deliberately a projection rather than a
second reader.** `labels` is keyed by the record's own identity and carries a treatment only for the
records that stay in a judgment collection; `context` carries the labelled context rows; `summaries`
carries the six-way count of every supplied collection, including the records this review does not
display as the selected subject's judgments. `revision_selection` carries **the selection the
classification was made against**, so pane 1 renders the selected statements from the same value the
classification used instead of being handed a second spelling of "which revisions were selected" —
two spellings is how a pane comes to render one selection beside another selection's records.
`label_of` answers `None` for a record that is not displayed here, which is what keeps an unrelated
record out of a pane; `displayed_rows` keeps a row whose references resolved to nothing (dropping it
would report an unresolvable binding as an absence of records) and drops a row that resolved to
another subject's identity, whether or not it was displayed as context.

**`review_applicability` assembles the one entry the composition calls.** The composition passes what
it already holds — the resolution the request was answered from, the request's own selector, the record
inputs, the matrix rows and one `ComparisonFacts` value carrying the comparison's union items, R07's
revision selection, R11's comparison identity and R08's recorded relationship union — and this function
builds `ApplicabilitySources`, including the **lazily** read known-subject catalogue
(`known_subjects=lambda: read_subject_catalogue(resolved)`), which is opened only when some record names
a subject the selection does not reach. `apply_review_applicability` is the policy: the recorded
population is read once, and the four supplied collections are classified against it by
`_classify_assessments`, `_classify_signals`, `_classify_observations` and `_classify_rows`.

**The direct-versus-historical decision is a resolution of the record's own revision references, not a
set intersection.** `_revision_binding` resolves each recorded revision reference against the
selection's own revision→identity index and returns two disjoint tuples: `of_subject` (references that
name a revision this comparison records *for the subject*) and `foreign` (references that name a
revision it records for a **different** identity). A reference in neither is not a recorded revision at
all — a record carrying an identity where a revision belongs is exactly the malformed binding the
packet's Failure And Recovery Behavior refuses to resolve — so `_subject_bound_label` reports
`unresolved` for it, with the sentence that says a reference that is not a recorded revision of the
subject is never matched against the selection's revisions. A `foreign` reference is reported
`unresolved` too, because a revision binding that contradicts the subject binding is a binding that
could not be resolved. Only references that resolve **to the subject** may make the record `direct`
(recorded and inside the selection's recorded population) or `historical` (recorded but outside it).

**The generation match is decided from the record's declared candidate tree and the comparison's bound
after-tree only.** `_declared_candidate_tree` reads the one generated-input edge of an assessment's
examined-input declaration that names the candidate generation (`code-tree:candidate`) and
`_subject_bound_label` compares it with `selection.generation.after_code_tree_id`; a difference makes
the record `historical`, naming the old tree in its detail and naming `ICR-R15@v1` as the owner of
dependency *currentness*. The pair identity (`candidate-state:knowledge-candidate-pair`) is
deliberately **not** compared: it is a hash of the pair-authority contract cells, so no
knowledge-generation digest is comparable on a record at all, and comparing it with a snapshot digest
would be a similarity dressed as a match. The measured consequence is recorded as a boundary rather
than a fix: a knowledge-only move (same captured code tree, different dataset) leaves the record
`direct`, and the remedy belongs to R11 (publish a knowledge-generation identity) or R15 (measure the
knowledge side).

**A `direct` label states the basis it actually used.** `_retention_basis` is the one place a sentence
may cite R07's published retained list, and it cites it **only** when that page-bound list really
carries every matched revision; otherwise the label says the revisions are the ones the two snapshots
record for the subject, "which this classification reads from the selection itself rather than from the
retained list this page published". The distinction is not cosmetic: ICR-R07 publishes a selection for
the page it answered, so at a bounded page its retained list is narrower than the recorded population
the classification reads, and a label that cited it at `page_size=1` would name evidence it never
consulted. `RecordedSelection.published_retained` exists for exactly this and is kept separate from
`subject_revisions`.

**The classification is page-independent because the population is the selection's, not the page's.**
This was the F-V2 finding of this leaf's first verification round: classifying against `page.items`
made the selected subject's own record read `historical` at a bounded page and dropped the recorded
family context as `unrelated`. The fix is structural — the recorded population is read from the two
snapshots' own owners in [`review_recorded_selection.py`](review_recorded_selection.py.md) and merged
**under** the comparison's page facts — and it is measured: at page sizes default/32/8/4/3/2/1 the
treatments, the context signature and the summaries are identical, with exactly one comparison call at
the caller's bound and two read-only snapshot opens.

**A comparison subject is matched by exact authored reference, never by similarity.**
`_comparison_subject_label` handles the one subject kind whose recorded identity is an *authored
reference* rather than a stored identity: the record's `comparisonRef` (or the record's own
`comparisonRef`) must equal the displayed comparison's published `reference` or `binding_digest`, and
anything else is `unresolved` — never a match by label or nearest generation.

**Signals and matrix rows are classified from their own recorded paths.** `_classify_signals` matches
the relationship rows a detection signal walked and the item each walk reached against the selection's
own revisions and relationship ids (`_match_references`); a path that reaches a related identity is
displayed as context whose relationship spelling is the selection's own `relationship_of` answer (or
the recorded relationship row it matched), and a path that reaches nothing this selection holds is
`unresolved` — shown with the paths it recorded, never dropped and never read as support.
`_classify_rows` does the same for the review matrix's authored effects and evidence claims, reading a
claim's own recorded subject revision through the evidence owner's renderer input
(`ReviewClaimRecord.subject_revision_id`) instead of re-reading the claim. `_classify_observations`
labels a verification observation from its own recorded candidate binding: a binding to the compared
candidate is `candidate`, and nothing here promotes an execution observation to a judgment on a
subject.

**`task_context_applicability` is the second entry, for a review that selected no subject.** There is
no selected subject and no comparison generation, so every supplied record is `candidate` — the one
label that neither claims the record applies to a subject nor reports a binding as unresolved when
nothing was asked of it — each with its recorded subject beside it. The two matrix-owned collections
are read by no pane of a task-context review, so their `not_selected` channel says so while the claims
the owner did supply are still counted.

**A summary refuses a partition that loses a record.** `_summary` builds
`ReviewApplicabilitySummary` for one collection from its counted states, with the `detail` that states
what `supplied` counts; the model's own validator refuses a sum that does not account for every
supplied record exactly once, which is what stops a filtering bug from becoming silent erasure. The
`supplied` fact is stated per class rather than uniformly: for the three owner-read collections it is
the population the pane's own collection was classified from (the same population the R14 channel
counts), and for the two matrix-owned collections (`authored_effects`, `evidence_claims`) it is the
rows the review matrix **page** returned, with the owner's complete count travelling on the channel —
which the summary's `detail` says.

### Conventions

`__all__` publishes the four names the compositions consume: `AppliedRecords`,
`apply_review_applicability`, `review_applicability` and `task_context_applicability`. Every value
returned is a shipped type from
[`models/knowledge/review_applicability.py`](../../models/knowledge/review_applicability.py.md); this
module declares one dataclass of its own (`AppliedRecords`) and three private ones (`_RevisionBinding`,
`_Matched`, `_Context`) plus one private lazy reader (`_KnownSubjects`). `_MATRIX_OWNED` names the two
page-owned collections once, so the "page population versus owner population" fact is declared rather
than repeated. Names are public where two callers use them and private where one does. The module
declares no model, holds no state and writes nothing.

### Invariants And Boundaries

- **The classification reads recorded facts only.** The population is the selection's, the binding is
  the record's own, and the generation is the record's declared candidate tree against the
  comparison's bound after-tree. No label, path spelling or nearest revision participates.
- **A malformed binding is never matched.** A reference that is not a recorded revision of the subject,
  a revision that belongs to another identity, an unresolvable subject and a comparison reference that
  is not the displayed comparison's own are all `unresolved` states carrying their references and the
  reason.
- **A record of another subject is never a judgment on the selected subject.** It is either labelled
  context (with its true subject, the recorded relationship that reached it and the record's **kind** —
  never its finding, disposition or rationale, which belongs to that subject's own review) or it is
  `unrelated`: not handed to a pane, counted, and named as reachable through its own subject's review.
- **The page decides what is displayed, never what a record means.** The recorded population is read
  from the snapshots and merged under the page facts; no page is fetched here and R10's bound still
  decides the displayed rows.
- **Filtering is stated, never silent.** Every collection's six-way count travels on the pane, and the
  summary's own validator refuses a partition that loses a record.
- **The complete source inventory is untouched.** It is measured from the two bound code trees
  elsewhere and never from a record; record provenance (author, role, exact input identities, evidence
  references) is carried verbatim on every displayed value.
- **The projection is a port, and the dependency is one-way.** `ReviewApplicabilityProjection` in
  [`review_record_rendering.py`](review_record_rendering.py.md) is what a pane needs; the renderer
  renders the values it is handed and never reaches the comparison or the store through this module.
- **No judgment is produced here.** The vocabulary has no field for a relevance, a similarity, a
  confidence or a score, and this module adds no disposition, finding or sufficiency claim.

### Todos

None recorded. The one measured limitation this leaf leaves open is a fact about another owner rather
than a task here: a knowledge-only generation move leaves a record `direct` because only the code tree
is comparable, and the remedy is R11's published knowledge-generation identity or R15's
dependency-currentness measurement.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The module's own statement of the defect it removes, the two things its classification reads, the six outcomes and the rule that filtering is stated rather than silent.** [1]
- **The port the panes consume: per-record labels, the labelled context rows, the six-way summaries and the selection the classification was made against.** [2]
- **The one entry the composition calls, before either pane renders anything.** [3]
- **The sources that one entry is assembled from, with the known-subject catalogue a reader rather than a value.** [4]
- **The policy: the selection's recorded population is read once and the four supplied collections are classified against it.** [5]
- **The task-context entry: no subject selected, so every record is the candidate's own input with its recorded subject beside it.** [6]
- **The per-collection projection, and the context row one related identity earns: true subject, the recorded relationship that reached it, the record's kind as its label, author and role, and no judgment content.** [7]
- **The direct/historical decision and the two unresolved shapes a revision binding can earn, with the sentences that state each basis.** [8]
- **The one place a label may cite ICR-R07's published retained list, and only when that list really carries the matched revisions.** [9]
- **ICR-R07's own page-bound retained list, carried beside the recorded revisions rather than in place of them.** [10]
- **A comparison subject is matched by exact authored reference or binding digest, and nothing else resolves.** [11]
- **The signal and matrix-row classifications: a recorded path that reaches the selection, a related identity displayed as context, and an unmatched path shown unresolved with its references.** [12]
- **The lazy known-subject catalogue, opened only when a record names a subject the selection does not reach.** [13]
- **The catalogue owner the lazy reader calls, kept the one implementation of a subject enumeration.** [14]
- **The six-way summary a collection's counts are published as, with the page-versus-owner population stated per class.** [15]
- **The vocabulary the projection builds, and the validator that refuses a summary losing a record.** [16]
- **The recorded population this classification turns on, read from the two snapshots' own owners and merged under the comparison's page facts.** [17]
- **The one call the composition makes, before either pane renders anything.** [18]
- **The projection's own "what stays in a pane" rule, which is what keeps an unrelated record out of one.** [19]
- **The port the renderer consumes, so a pane renders what it is handed and never decides which records those are.** [20]
- **The cases that measure the projection: a sibling's assessment as context and never the selected subject's, the selected subject's own record direct, an unrelated subject counted and not displayed, an unresolvable binding displayed with its references, a previous generation historical, and a malformed revision binding unresolved.** [21]
- **The cases that measure the page-independence and the retention basis: identical treatments and summaries at every page size, and a `direct` label that may cite R07's list only when that list carries the record.** [22]
- **The cases that measure the stated populations and the vocabulary's own refusals.** [23]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It classifies records and identities that
belong to one repository's own snapshots and comparison.

No meaningful cross-repo references found.
