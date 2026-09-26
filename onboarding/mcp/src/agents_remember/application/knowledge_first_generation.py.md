# mcp/src/agents_remember/application/knowledge_first_generation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_first_generation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-26T20:13:29Z |
| lastVerifiedCommitHash | `43b247d5bf30d4191f8fd5eb4dea9cfd72e4258d` |
| lastVerifiedCommitDate | 2026-09-27T00:14:33+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` in the memory
layer reads "No entries configured yet", so it carries no `Domain Documentation` category). The
statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and its
three properties, the read-before-write guard, the candidate-derived admission, the private stage and
the single promote, and the four named failures. Ranges are the exact construct extents in this
candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of the two cases it owns, the three properties that keep an empty before side from becoming a lie, and the fact that its record is a local operation fact rather than knowledge. | "Empty is created, never copied."; "The generation is identified."; "Initialization is all-or-nothing." | mcp/src/agents_remember/application/knowledge_first_generation.py:9-32 |
| The published surface: the run descriptor, the result and the one operation. | `__all__`; `BeforeGenerationState` | mcp/src/agents_remember/application/knowledge_first_generation.py:74-78; mcp/src/agents_remember/application/knowledge_first_generation.py:80-80 |
| The admitted run as its record names it: the leaf, the contract, the authorization and the code base the run observed. | `FirstGenerationRun` | mcp/src/agents_remember/application/knowledge_first_generation.py:83-90 |
| What one run left in the before half: its state, the report's line about it, and the record it wrote. | `BeforeGeneration` | mcp/src/agents_remember/application/knowledge_first_generation.py:93-99 |
| **The whole operation, with the read-before-write guard as its first act so an existing dataset is never rewritten, relabelled or replaced.** | `establish_first_generation` | mcp/src/agents_remember/application/knowledge_first_generation.py:102-126 |
| **The three answers a half that already holds something produces: the damage named for a damaged half, `present` with its own origin for an identified one, and `present` with the fact that this half was not established here for an unidentified one.** | `_standing_before_half` | mcp/src/agents_remember/application/knowledge_first_generation.py:129-154 |
| **The admission read from the candidate's own record: its receipt, its repository row, and the comparison between them, with four named refusals instead of a re-derivation.** | `_candidate_admission`; `read_candidate_receipt`; `_recorded_namespace`; `bound_repository`; `open_read_only_database` | mcp/src/agents_remember/application/knowledge_first_generation.py:157-187; mcp/src/agents_remember/application/knowledge_first_generation.py:190-202; mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:62-87; mcp/src/agents_remember/memory/knowledge/logical.py:178-197; mcp/src/agents_remember/memory/knowledge/connection.py:52-63 |
| The receipt read back into the resolution the creation owner takes, because one is the record of an admission and the other is its input. | `resolution_from_receipt`; `CandidateResolution`; `CandidateReceipt` | mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:103-115; mcp/src/agents_remember/models/knowledge/candidate.py:659-676; mcp/src/agents_remember/models/knowledge/snapshot.py:109-141 |
| **The private stage and the one exposure: the stage removed in a `finally` that can only ever discard a stage which never became a half.** | `_expose_first_generation`; `_stage_directory` | mcp/src/agents_remember/application/knowledge_first_generation.py:205-228; mcp/src/agents_remember/application/knowledge_first_generation.py:320-332 |
| **The closed failure set and the one promote: the build's four failure types, the creation owner's own refusal relabelled with its code and detail, and the rename that installs a complete half.** | `_promote_first_generation`; `atomic_replace` | mcp/src/agents_remember/application/knowledge_first_generation.py:231-270; mcp/src/agents_remember/kernel/atomic_write.py:80-126 |
| **The build: the empty dataset created by the shipped owner under the candidate's own namespace and input pair, the identity read back from the bytes, the record written, and the re-read that refuses a record which did not read back unchanged.** | `_build_first_generation`; `create_knowledge_candidate`; `admitted_candidate_destination`; `dataset_identity` | mcp/src/agents_remember/application/knowledge_first_generation.py:273-297; mcp/src/agents_remember/application/knowledge_snapshot.py:102-107; mcp/src/agents_remember/application/knowledge_snapshot.py:67-82; mcp/src/agents_remember/memory/knowledge/logical.py:153-175 |
| The one origin record built from the dataset that was actually created and the run that made it, including the `recorded_at` stamp this module is the only writer of. | `_origin_record`; `BaselineOrigin`; `write_baseline_origin`; `read_baseline_origin` | mcp/src/agents_remember/application/knowledge_first_generation.py:300-317; mcp/src/agents_remember/application/knowledge_before_half.py:89-120; mcp/src/agents_remember/application/knowledge_before_half.py:169-179; mcp/src/agents_remember/application/knowledge_before_half.py:182-204 |
| **The reader every guard above is stated in terms of, and the four-state value it answers with.** | `read_before_half`; `BeforeHalf`; `baseline_database_path`; `baseline_origin_path` | mcp/src/agents_remember/application/knowledge_before_half.py:123-137; mcp/src/agents_remember/application/knowledge_before_half.py:152-160; mcp/src/agents_remember/application/knowledge_before_half.py:163-166; mcp/src/agents_remember/application/knowledge_before_half.py:257-286 |
| The failure type the build catches, and the identity value the record is built from. | `KnowledgeStorageError`; `SnapshotIdentity`; `RepositoryIdentity` | mcp/src/agents_remember/memory/knowledge/refusals.py:27-32; mcp/src/agents_remember/models/knowledge/candidate.py:195-204; mcp/src/agents_remember/models/knowledge/repository.py:19-31 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. The half it establishes lives inside one
leaf's disposable knowledge root, under the namespace the committed candidate's own record names.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T20:13:29Z — Reconciled exact-source capture and explicit predecessor-bound progression while retaining strict ordinary candidate open.
- 2026-09-22T19:40:00+02:00 — 260921-ICR-L8 curator (candidate `ar/260921-icr-l8`, uncommitted; production line at this leaf's base `02957762709c9b515b4ff57f7f13524a7c0dfb8d`): **metadata-row removal.** The candidate-reading metadata rows this card carried were removed under the developer's 2026-09-22 rule: the field is not a real metadata field, has no purpose, and must not be written or carried anywhere. The reading those rows recorded is preserved in this entry's own words — the claims on this card were taken against the leaf candidate named above where they describe uncommitted work, and against the last real commit the card's stamp names where they describe shipped code. No claim, anchor, wording or citation range changed, no table shape changed, and no verification stamp was advanced.

- 2026-09-21T14:40+02:00 — orchestrating session, pre-closeout metadata repair on `ar/260921-icr-l5`: the governed closeout refused the memory leg because this card carried no verification stamp at all (`external-memory closeout requires onboarding verification metadata before memory commit`), and the card's own recorded reason for omitting it cannot be satisfied by a card that the transaction must read. The two fields were therefore added naming the **production line this card was read against** — `702714fc05363cb28eacaf101ba8384475a6aa56`, the master line after this leaf's `worktree_sync` brought in leaf `260921-ICR-L1`'s landed extraction, at that closeout's recorded time `2026-09-21T13:27:46+02:00` — and the candidate row was corrected from the pre-sync base `f745e166` to that same production line. This is a statement of *what the reading was against*, not a claim that the constructs exist in that commit; the governed closeout's own metadata refresh re-stamps the card against the code commit this transaction creates, and that remains the real stamp. No range, claim or anchor was changed by this repair.
- 2026-09-21T13:45+02:00 — 260921-ICR-L5 curator (uncommitted change set on `ar/260921-icr-l5`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`): created this one-to-one card for the new module, which is this leaf's second half and the act ICR-R05@v1 names: the supported owner now *establishes* a schema-valid empty before-generation for a legitimate first generation. The card records the three properties the module's own docstring calls load-bearing (created never copied, identified by a record beside the dataset, all-or-nothing exposure), the read-before-write guard that makes an existing half unrewritable, the candidate-derived admission that avoids a second derivation of the namespace and the input pair, the uncreated stage beside the half and the single `atomic_replace` promote, the closed failure set with its four named refusals, and the explicit boundary that this module decides no authority, commits nothing and never writes the candidate. Ranges are the exact construct extents in this candidate. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no commit contains the content a stamp would claim to have verified. Verification metadata is closeout-owned.
