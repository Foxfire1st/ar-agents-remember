# mcp/src/agents_remember/application/knowledge_ingest.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_ingest.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-20T00:31+02:00 |
| reviewedWorkingCandidate | `ar/260915-ks-l30-ar`, uncommitted; base `7dcec036094768c5f50e571fb45e59a27ae78efc` |
| lastVerifiedCommitHash | `7ca3ac48914a562bb90b5fe04d6c17b5a3f51d80` |
| lastVerifiedCommitDate | 2026-09-20T02:00:33+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The reachable write entry point of the knowledge plane: it turns one **curator entry** — the
requirement-shaped item an orchestrator hands over — into the ordered command list one
`ChangeBatch` carries, and commits that batch through the closed write path. Its own docstring
states the historical fact that makes it load-bearing: before this module existed, "every importer
of `agents_remember.application.knowledge` was a test and the mounted change tool refused every
record kind, so the closed write path had no reachable entry point at all." It is therefore the
module in which "the curator's reachable ingest" lives, and the layer above it
(`application/knowledge_curator_ingest.py`) is the operation that admits a destination, resolves and
verifies each target, and then calls this module to author the result.

Two design statements in the docstring set the file's boundaries. First, the citation is a **second
record** rather than a field of the revision: each target is written as a `SourceAnchorDraft` by its
own `AddSourceAnchor` command and cited by a `RealizationClaimDraft` on the revision, so "an
existing revision's digest bytes do not move." Second, **provenance is not a parameter**: the
revision draft is built here with the admitted destination's own envelope, and "the batch operation
re-stamps it, so nothing a caller authors can become the stored provenance."

## Code Commentary

### Logic

**Two frozen dataclasses are the input shape, and neither holds a decision of its own.**
`CuratorCitation` is one resolved target plus the claim that cites it: a shipped `SourceAnchorDraft`
("a path, the source identity it was resolved at and the locator") together with the authored
`claim_id`, `role` and `rationale`, because "a stored anchor with nothing citing it attributes
nothing to the statement." `CuratorEntry` is one requirement-shaped entry: the `invariant_id`,
display label, revision identity and version, statement, applicability, the optional
`conditions`, `exclusions` and `predecessors` tuples that become the revision's own fields, and
`declares_invariant` (default `True`), which says whether this entry is declaring the invariant or
authoring a successor of one the repository already holds. The invariant identity "is declared once
and used for both the identity row and the revision, so a batch cannot file a revision under an
invariant its own command did not record." `citations` defaults to
the empty tuple, which is deliberate: "an entry whose targets are not yet resolved is still an
authored obligation, and the write path records it with no realization rather than inventing one."

**`curator_entry_commands` is the command order, and the order is the batch's own contract.** It
emits `AddInvariant` for the identity row **only when the entry is declaring that invariant**
(`entry.declares_invariant`), and then always `AddInvariantRevision` for the revision draft; an
entry that names predecessor revisions is authoring a successor, and re-declaring an invariant the
repository already holds is refused outright with `batch_stale_precondition`, because "the batch's
precondition for creating an invariant is that the invariant is ABSENT". Then, per citation, it
appends `AddSourceAnchor` **before** the `AddRealizationClaim` that
cites it, because "an anchor is written before the claim that cites it, so the claim's anchor
endpoint resolves against a row this same batch declared." The claim's `anchor` is an
`AnchorReference(anchor_id=str(citation.anchor.anchor_id))`, so the claim names the row the previous
command in the same batch declared rather than a row read from the store. Four entry points
publish this module's work: `curator_entry_commands` (commands only), `curator_batch` (one batch for
a whole list), `commit_curator_entry` (one entry, one batch) and `commit_curator_entries` (the whole
list, one batch); `__all__` names exactly those four plus the two dataclasses.

**`curator_batch` resolves the context itself instead of accepting one.** It calls
`resolve_candidate_context(destination, resolution)` and passes the result as the batch's `expected`,
so "the batch is compared against the identity the candidate actually holds" — a caller cannot
hand-write the dataset identity its own batch is compared against. The whole hand-off list travels
in that one batch for a stated reason: "the operation is all-or-nothing under one lock: a batch per
entry pays the commit boundary once per entry, and a list that fails halfway leaves a partially
recorded ingest that nothing can reconcile." The commands are flattened with a nested comprehension
over `entries` and then over `curator_entry_commands(destination, entry)`, which is why the entry
order and the per-entry command order both survive into the batch unchanged.

**`commit_curator_entry` is a one-element delegation, and `commit_curator_entries` is the whole
call.** The single-entry form exists so a caller that has exactly one entry does not have to build a
sequence: it delegates with `(entry,)`. The plural form builds the batch and hands it to
`change_knowledge_candidate(destination, curator_batch(...))`, and its docstring fixes what comes
back: "the receipt is the operation's own: it reports the rows written and the logical identity
before and after, and a refusal carries the typed refusal with the dataset left exactly as it was."
That is the shipped `MutationResult` contract, not a shape declared here — the module imports
`MutationResult`, `ChangeBatch`, `CandidateResolution`, `ProposedCommand` and the four command
classes from `models/knowledge/candidate.py` and declares no model of its own beyond the two
`@dataclass(frozen=True)` inputs.

**`_revision_draft` is the single private step, and it is where the provenance envelope is
attached.** It builds the shipped `RevisionDraft` from the entry's own fields — revision id,
invariant id, display version, statement, applicability, conditions, exclusions, predecessors — and
sets `provenance=destination.authorship`, the admitted envelope the write path re-stamps. No digest
is passed: `RevisionDraft`'s own docstring states the store recomputes and stores it, so a caller
cannot present a payload whose seal belongs to different content. The module never reads
`entry.invariant_id` for anything other than the invariant command and the revision draft, and never
touches a target's bytes: as the docstring puts it, "whether a recorded target actually holds its
recorded bytes is a fact `memory.knowledge.read_anchors` observes, not a condition this module can
establish."

**Its relationship to `application/knowledge_curator_ingest.py` is write-half to whole-operation.**
That module's own docstring names the split: `knowledge_ingest` "is the write half -- one resolved
entry, one command list, one batch. This module is the layer above it, and it is the operation the
leaf's objective names: the curator receives the orchestrator's hand-off list and commits it." The
curator-ingest module imports `CuratorCitation`, `CuratorEntry`, `commit_curator_entries` and
`curator_entry_commands` from here, converts each of its plans into one `CuratorEntry` through its
own `_curator_entry`, and commits the list through `_commit` → `commit_curator_entries`. It is the
only production importer; the other importers are the two test modules that exercise this file's
entry points directly.

### Conventions

The module is function-first and model-free: zero classes beyond the two frozen dataclasses, and
every value it returns is a shipped type imported from the models layer (`ProposedCommand`,
`ChangeBatch`, `MutationResult`, `RevisionDraft`, `SourceAnchorDraft`, `RealizationClaimDraft`,
`RealizationRole`, `AnchorReference`, `AdmittedKnowledgeDestination`, `CandidateResolution`). Names
are spelled the way the write path spells them (`destination`, `resolution`, `entry`, `citation`,
`commands`, `batch`, `receipt`) so a call site reads as the operation it is. Private helpers take a
leading underscore and exist only to keep a public function a single statement; there is exactly one
(`_revision_draft`). The two entry dataclasses are `@dataclass(frozen=True)`, so an entry is a value
that can be passed across the operation boundary without any party mutating the other's input.
Import order follows the repository convention: standard library, application seams, then models
grouped by module.

### Invariants And Boundaries

- **An anchor is written before the claim that cites it.** `curator_entry_commands` appends
  `AddSourceAnchor` and then `AddRealizationClaim` for each citation, so the claim's anchor endpoint
  resolves against a row declared in the same batch.
- **Provenance comes from the admitted destination, never from an entry.** `_revision_draft` sets
  `provenance=destination.authorship`, and the batch operation re-stamps it; the entry carries no
  author, authorization or instant.
- **One invariant identity per entry, used for both records.** The identity row and the revision are
  built from the same `entry.invariant_id`, so a revision cannot be filed under an invariant the
  batch did not record.
- **An invariant row is created only by an entry that declares it.** `curator_entry_commands`
  appends `AddInvariant` only when `entry.declares_invariant` is true — the default — and always
  appends `AddInvariantRevision`. An entry naming predecessor revisions is a successor: it carries
  its revision and its predecessor edges, and the invariant row it revises is left as it stands,
  because the batch refuses to create an invariant that already exists
  (`batch_stale_precondition`).
- **Empty citations are legal and mean "authored obligation with no realization".** The module
  records the invariant and revision and invents no anchor or claim for an entry whose targets are
  not yet resolved.
- **The whole list is one batch.** There is no per-entry commit loop in the public surface; a
  partially recorded ingest is the failure mode the single batch exists to prevent.
- **No sealing, digest, schema generation or payload-version work happens here.** The citation is a
  second record the revision cites rather than a field of its revision preimage, which is what keeps
  an existing revision's digest bytes still.
- **Resolution and validation are upstream.** This module neither resolves a path nor verifies that
  a target holds its recorded bytes; a refusal it produces is the write path's own typed refusal,
  and the dataset is left exactly as it was.
- **The module owns no authority and no durable state.** It opens nothing, closes nothing and stores
  nothing; the connection lifetime belongs to `change_knowledge_candidate`.

### Todos

No task-independent follow-up is recorded in the source. The docstring notes two facts a future
editor should not read as defects: the write path would accept a target that names nothing (it
stores what was authored), and the locator's extent is "a rendering of the recorded construct rather
than the record's identity." Both are deliberate boundaries of this seam rather than open work
items.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim above is checkable in the shipped candidate: this module's own docstring and functions,
the two seams it delegates to in `application/knowledge.py`, the batch and receipt shapes it builds
and returns, the only production importer above it, and the two test modules that drive its entry
points directly. The one detail worth carrying: the citation is a separate anchor row plus a claim
row rather than a field of the revision, which is exactly why the revision's digest bytes do not
move when a citation is added.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it is: the first production caller of the knowledge write plane, the curator entry turned into one batch, the second-record citation that keeps an existing revision's digest still, and provenance not being a parameter. | "This is the first production caller of the knowledge write plane." | mcp/src/agents_remember/application/knowledge_ingest.py:1-30 |
| The published surface: the two entry dataclasses and the four command/batch/commit functions, and nothing else. | `__all__` | mcp/src/agents_remember/application/knowledge_ingest.py:57-64 |
| One resolved target plus the claim that cites it — the shipped anchor draft with the authored claim identity, role and rationale. | `CuratorCitation` | mcp/src/agents_remember/application/knowledge_ingest.py:68-79 |
| One requirement-shaped entry: the invariant identity shared by the identity row and the revision, the authored revision fields, the empty-citations case that records an obligation with no realization, and `declares_invariant`, which keeps a successor from re-declaring the invariant it revises. | `CuratorEntry` | mcp/src/agents_remember/application/knowledge_ingest.py:83-102 |
| The load-bearing command order: the invariant row only when the entry declares it, then its revision, then each anchor before the claim that cites it, with the claim referencing the row the same batch declared. | `curator_entry_commands` | mcp/src/agents_remember/application/knowledge_ingest.py:105-142 |
| The single all-or-nothing batch for a whole hand-off list, with the context resolved against the candidate as it stands rather than accepted from the caller. | `curator_batch` | mcp/src/agents_remember/application/knowledge_ingest.py:145-163 |
| The two commit entry points: one entry committed as one batch, and the whole hand-off list committed as one batch through the closed write path. | `commit_curator_entry`; `commit_curator_entries` | mcp/src/agents_remember/application/knowledge_ingest.py:166-173; mcp/src/agents_remember/application/knowledge_ingest.py:176-187 |
| The one authoring step: the revision draft built from the entry's fields and sealed under the admitted destination's own provenance envelope. | `_revision_draft` | mcp/src/agents_remember/application/knowledge_ingest.py:190-205 |
| The two seams it delegates to: the resolver that reads the identity the candidate actually holds, and the operation that applies the batch under the destination's provenance. | `resolve_candidate_context`; `change_knowledge_candidate` | mcp/src/agents_remember/application/knowledge.py:267-285; mcp/src/agents_remember/application/knowledge.py:318-331 |
| The shapes it builds and returns: the ordered all-or-nothing batch, and the factual receipt whose refusal leaves the logical identity unchanged and reports no touched record. | `ChangeBatch`; `MutationResult` | mcp/src/agents_remember/models/knowledge/candidate.py:676-701; mcp/src/agents_remember/models/knowledge/candidate.py:704-741 |
| The only production importer, the curator's whole-operation layer, which reuses this module's entry and citation dataclasses and its batch commit, and builds one entry per plan. | "from agents_remember.application.knowledge_ingest import ("; `_curator_entry` | mcp/src/agents_remember/application/knowledge_curator_ingest.py:91-96; mcp/src/agents_remember/application/knowledge_curator_ingest.py:2261-2275 |
| The cases that drive this module directly: one curator entry committed through the public commit entry point, and the documented empty-citations path the whole-operation layer deliberately does not reach. | "from agents_remember.application.knowledge_ingest import ("; "``CuratorEntry.citations`` permits an empty list" | mcp/tests/test_knowledge_curator_ingest.py:34-34; mcp/tests/test_knowledge_curator_ingest_list.py:471-471 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Every identity it writes belongs to one
admitted knowledge destination for one repository namespace, and the provenance envelope it stamps
comes from that admission; the module opens no second repository and names no external system.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-20T01:41+02:00 — 260915-KS-L30 curator, hand re-read (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): the row naming this module's only production importer was re-read against the construct it is about, and both of its ranges were verified at their declarations — `knowledge_curator_ingest.py:91-96` is the import statement the row quotes, and `:2261-2275` is `_curator_entry`'s own span, which is the function that builds one entry per plan. The earlier automatic range projection that had rewritten one of this row's citations is superseded by this reading and no longer stands as its evidence. No claim wording, anchor or other range changed, and no verification stamp was advanced.
- 2026-09-20T01:26+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): **cleared the last three citation rows of this card — the reopened claim and the two stale ranges it rides on (one row).** The "only production importer" row cited `knowledge_curator_ingest.py:84-89` and `:2175-2189`; the construct it names is now lower in that file, so each range was repointed to the extent that carries its own anchor: the import statement is at 91-96 (`from agents_remember.application.knowledge_ingest import (` through its closing paren, which is what the row's quoted anchor is the head of), and `_curator_entry` is declared at 2261-2275, its own span through the returned `CuratorEntry(...)` construction. The Finding text, both anchors and every other row are unchanged; no citation was dropped and no range was deleted. The reopened claim is this same row — `_curator_entry` changed structurally after its recorded verification — so it was re-read against the candidate and **retained as written**: the curator's whole-operation layer is still the only production importer, and it still builds one entry per plan through that helper. **Stamp accounting:** the stale `lastVerifiedCommitHash`/`lastVerifiedCommitDate` rows were replaced by ONE `reviewedWorkingCandidate` row naming this candidate, because no commit contains the body as it now stands and no stamp was measured on it.
- 2026-09-20T00:31+02:00 — 260915-KS-L30 curator (uncommitted change set on `ar/260915-ks-l30-ar`, base `7dcec036094768c5f50e571fb45e59a27ae78efc`): re-read this card against the CYCLE-01 repair and corrected the two claims that change invalidates. `CuratorEntry` gained `declares_invariant` (default `True`), and `curator_entry_commands` no longer "always" emits `AddInvariant`: the identity row is created **only** when the entry declares that invariant, while `AddInvariantRevision` is always appended, because the batch's precondition for creating an invariant is that the invariant is ABSENT — which is why a changed statement used to be refused with `batch_stale_precondition` and the repository could accumulate obligations but never evolve one. Both statements were re-worded to the conditional form, and an invariant bullet records it. The reopened `_curator_entry` claim was re-read against the current construct: its wording ("reuses this module's entry and citation dataclasses and its batch commit, and builds one entry per plan") still holds — `_curator_entry` still builds one entry per plan and now also passes `predecessors` and `declares_invariant` through — so the wording was **retained** and only the range re-cited, from `knowledge_curator_ingest.py:2034-2047` to `:2175-2189`, with the importer's import block re-cited from `:80-85` to `:84-89`. Every other row in this card was re-read against the working candidate and re-cited to its construct's current extent (`CuratorCitation`, `CuratorEntry`, `curator_entry_commands`, `curator_batch`, the two commit entry points, `_revision_draft`), because this leaf's insertions moved each of them by seven to twelve lines. No verification stamp was advanced: the candidate is uncommitted and closeout owns the real code and memory commits.

- 2026-09-19T17:09+02:00 — 260915-KS-L28 curator: created this one-to-one card for the curator-facing
  write entry point of the knowledge plane. It records the module's role as the first production
  caller of the write path, the two frozen input dataclasses and the four published entry points,
  the load-bearing command order (anchor before the claim that cites it), the single all-or-nothing
  batch with a context resolved against the candidate as it stands, the revision draft sealed under
  the admitted destination's provenance, the `ChangeBatch` and `MutationResult` shapes it builds and
  returns, and its split from `application/knowledge_curator_ingest.py` as write half to
  whole-operation. Verified against the committed source at
  `d0c1d1cfa9b576fd117ac2a0c05c5defe0089678`.
