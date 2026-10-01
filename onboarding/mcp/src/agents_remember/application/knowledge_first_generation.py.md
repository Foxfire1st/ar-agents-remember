# mcp/src/agents_remember/application/knowledge_first_generation.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**Establishing a repository's first knowledge generation as an identified, empty before side.** A
comparison is *between* two datasets, so the first knowledge a repository ever records has to be
reviewed against a before side. The ingest CLI places that side from the dataset a task forks from
(`--baseline`); this module owns the other, equally explicit case: a repository's **first
generation**, where there is no earlier dataset to fork from and the truthful before side is an empty
one that says so.

Three properties are load-bearing, and the module's own docstring names each as a way an empty before
side could become a lie:

- **Empty is created, never copied.** The dataset is built by the shipped initialization owner
  (`create_knowledge_candidate`) under the namespace and the exact input pair the committed
  candidate's own record names, so it is schema-valid and belongs to the same namespace. It is never a
  copy of the candidate: a populated candidate used as its own before side would display the first
  addition as present on both sides.
- **The generation is identified.** The dataset alone cannot say whether it is an empty *first*
  generation or a history that was measured and found empty, and those are different facts. The origin
  record written beside it
  ([`application/knowledge_before_half.py`](knowledge_before_half.py.md)) names which one this is, the
  namespace it belongs to, the code base the run observed, and that pre-feature history is **not
  recorded**.
- **Initialization is all-or-nothing.** The dataset and its record are built in a private stage and
  exposed as one directory, exactly as candidate creation does, so a failure leaves either a complete,
  identified before half or nothing at all — never a dataset a later reader could accept as a valid
  baseline without knowing what it is.

Nothing here decides authority, and nothing here is knowledge: the record is a *local operation fact*
about the run that wrote the half, which is why it lives beside its dataset in the leaf's disposable
knowledge root rather than as a row anything can query.

## Code Commentary

### Logic

The receipt-to-resolution conversion is imported from memory.knowledge.candidate_receipt.resolution_from_receipt. First-generation establishment continues to derive its empty before side from the exact admitted candidate receipt; the conversion has one shared owner.

**`establish_first_generation` is the whole operation, and its first act is a read rather than a
write.** It calls `read_before_half` and returns `_standing_before_half` for anything that is not
`absent`, so an existing dataset is **never** rewritten, relabelled or replaced: an identified half
reports `present` with its own recorded origin, and an unidentified half reports `present` with the
fact that this half was not established here. A half whose own bytes cannot be read as the generation
its record names reports `not-established` carrying the damage, and is left exactly as it is. Only an
`absent` half proceeds, which is what keeps "this run established nothing" and "this run restated
something" two different answers.

**The admission is read from the candidate's own record rather than re-derived.** `_candidate_admission`
reads the committed candidate's receipt (`read_candidate_receipt`) and its own recorded namespace
(`_recorded_namespace`, through the shipped read-only open and `bound_repository`), then refuses by
name when the dataset is not a file, when the receipt cannot be read, or when the dataset records no
namespace at all. It also compares the two: a receipt naming one namespace while the dataset is bound
to another is `not-established`, because a before half built under a namespace the candidate does not
hold would be a second derivation of the pair — exactly the drift a comparison would display as a
difference that never happened. `resolution_from_receipt` then reads the receipt back into a
`CandidateResolution`, which is the *input* shape the creation owner takes; the two hold the same facts
under two names because one is the record of an admission and the other is its input.

**The build is staged, verified by re-read, and promoted by one rename.** `_stage_directory` returns a
fresh **uncreated** sibling path beside the half
(`.<half-name>.<uuid4>.first-generation`) — beside it so the promote is a rename inside one filesystem,
and uncreated because the shipped creation owner's own first act is to refuse an occupied destination,
so a stage this function had already created would be refused as a resume attempt rather than built.
`_build_first_generation` creates the empty dataset at
`admitted_candidate_destination(stage, repository, resolution)`, reads the identity **back** from the
dataset that was created (rather than taking the admission's answer), builds the `BaselineOrigin`
through `_origin_record`, writes it, and re-reads it — a record that does not read back unchanged is
`not-established` rather than a claim. `_promote_first_generation` then installs the whole directory
with one `atomic_replace`. `_expose_first_generation` owns the stage's lifetime: the `finally` removes
the stage, which after a successful promote is a path that no longer exists, so the removal can only
ever discard a stage that never became a half.

**Every failure names what it could not do, and the failure set is closed.** The stage that cannot be
created, the dataset that cannot be built (`KnowledgeStorageError`, `apsw.Error`, `OSError`,
`ValueError`), the creation owner's own refusal (relabelled into the reason with its code and detail),
and the promote that cannot replace an occupied destination each produce a `not-established` value
carrying the path and the reason. Nothing is raised to the caller and nothing is claimed at the half.

### Conventions

The module imports downward only — its sibling `knowledge_before_half`, the shipped creation owner
`application/knowledge_snapshot`, the storage owners (`memory.knowledge.candidate_receipt`,
`memory.knowledge.connection`, `memory.knowledge.logical`, `memory.knowledge.refusals`), the kernel's
`atomic_write.atomic_replace` and the model vocabulary — and it defines no storage operation of its
own. `__all__` publishes exactly three names: the run descriptor, the result value and the operation.
The two dataclasses are frozen, and the result carries the `origin` record it wrote so a caller can
report it without re-reading the half.

### Invariants And Boundaries

- **Nothing is written to a half that already holds a dataset.** The `absent` check is the operation's
  first act, and no branch below it can replace, relabel or repair an existing side.
- **The half is built under the candidate's own admission, not under a second derivation.** Both the
  namespace and the resolution come from the candidate's receipt and its own repository row.
- **All-or-nothing exposure.** The dataset and its origin record are complete inside the private stage
  before the single `atomic_replace`; a failure leaves nothing at the half, and the stage is discarded.
- **The record's identity is read back from the bytes.** `_origin_record` takes the `SnapshotIdentity`
  read from the created dataset, so the record cannot state an identity the bytes do not hold.
- **Boundary.** This module never commits, publishes, moves a ref or writes a ledger row, and it does
  not decide *whether* establishment happens — the caller does, and the caller is the run that
  committed the candidate. It also never touches the candidate: the candidate directory is read
  (receipt, namespace) and never written.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` in the memory
layer reads "No entries configured yet", so it carries no `Domain Documentation` category). The
statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and its
three properties, the read-before-write guard, the candidate-derived admission, the private stage and
the single promote, and the four named failures. Ranges are the exact construct extents in this
candidate.

- The module's own statement of the two cases it owns, the three properties that keep an empty before side from becoming a lie, and the fact that its record is a local operation fact rather than knowledge. [1]
- The published surface: the run descriptor, the result and the one operation. [2]
- The admitted run as its record names it: the leaf, the contract, the authorization and the code base the run observed. [3]
- What one run left in the before half: its state, the report's line about it, and the record it wrote. [4]
- **The whole operation, with the read-before-write guard as its first act so an existing dataset is never rewritten, relabelled or replaced.** [5]
- **The three answers a half that already holds something produces: the damage named for a damaged half, `present` with its own origin for an identified one, and `present` with the fact that this half was not established here for an unidentified one.** [6]
- **The admission read from the candidate's own record: its receipt, its repository row, and the comparison between them, with four named refusals instead of a re-derivation.** [7]
- The receipt read back into the resolution the creation owner takes, because one is the record of an admission and the other is its input. [8]
- **The private stage and the one exposure: the stage removed in a `finally` that can only ever discard a stage which never became a half.** [9]
- **The closed failure set and the one promote: the build's four failure types, the creation owner's own refusal relabelled with its code and detail, and the rename that installs a complete half.** [10]
- **The build: the empty dataset created by the shipped owner under the candidate's own namespace and input pair, the identity read back from the bytes, the record written, and the re-read that refuses a record which did not read back unchanged.** [11]
- The one origin record built from the dataset that was actually created and the run that made it, including the `recorded_at` stamp this module is the only writer of. [12]
- **The reader every guard above is stated in terms of, and the four-state value it answers with.** [13]
- The failure type the build catches, and the identity value the record is built from. [14]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The half it establishes lives inside one
leaf's disposable knowledge root, under the namespace the committed candidate's own record names.

No meaningful cross-repo references found.
