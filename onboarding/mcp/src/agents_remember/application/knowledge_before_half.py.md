# mcp/src/agents_remember/application/knowledge_before_half.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**Derived-index preflight for a review pair.** This module creates no canonical dataset layout and writes no knowledge. `read_dataset_identity` delegates to the storage owner's read-only `dataset_identity`, returning the selected index's `SnapshotIdentity` or a reason for a non-file or a named storage/SQLite/OS read failure. It neither repairs nor substitutes an index.  [10]

`unreadable_half_refusal` checks existing baseline and candidate indexes in that order. It skips absent files and returns `candidate_dataset_absent` for the first existing index it cannot read, with the half in `offending_input` and an instruction to rebuild the derived index from its recorded memory tree. Whole-pair preflight separately handles absent halves and candidate-namespace/receipt admission; those checks are not an origin-record reader in this module.  [18]

`SnapshotIdentity` carries the repository UUID, schema label and logical digest. It is the surviving identity model used here, rather than the retired `BaselineOrigin` described in the historical account below.  [18]

**Historical (retired by MIK-R26).** The layout and provenance machinery described below — the
one-dataset-plus-one-provenance-record layout, the module-owned origin record, the selected baseline's
generation record, and the four-state `read_before_half` readers — belonged to the canonical database.
The converted-memory writer creates no canonical dataset sides, and this module now carries only the
derived-index identity read and the unreadable-half refusal. The old account is retained as history.

## Historical source account

The following account is retained verbatim from the retired canonical-database implementation. Its present-tense descriptions, old line extents, module owners, caller census and export count describe that historical source; they do not claim those constructs exist in the current 40-line module. The retirement is established in code history at `b52adc8bc0564f6328d3543e48998e9235f1e417` (MIK-R26), before L191's admitted base.

> Three facts are told apart here because a writer that confuses them writes the wrong thing, and the
> module's own docstring names them as its load-bearing distinctions:
>
> - **Absent is not empty.** A half with no dataset is a pair that cannot be compared; it is not a
>   measured-empty history, and it must never be answered with a freshly created dataset unless the
>   caller's own act says the repository's knowledge begins there.
> - **Identified is not unidentified.** A dataset with **no** recorded origin is a fork point some
>   `--baseline` run placed; a dataset **with** a matching record is an explicitly identified first
>   generation. A later run keeps the first and never restates the second.
> - **Damaged is neither.** Bytes that cannot be read as a dataset of this code, a record that cannot be
>   read at all, or a record whose identity no longer matches the bytes beside it: each is a state that
>   has to be *named* with its reason and left exactly as it is.
>
> Every read answers with a reason instead of raising, and that is deliberate rather than defensive: a
> file that is not a dataset is an **input** fact in all three callers — the ingest admission reading a
> selected fork point, the ingest CLI inspecting the half it is about to fill, and the review refusing a
> comparison whose side cannot be opened — so each caller states the fact in its own voice instead of
> receiving one module's exception.
>
> ## Code Commentary
>
> ### Logic
>
> **The half's layout is one dataset plus one provenance record, and the origin record is deliberately
> not one of them being knowledge.** `baseline_database_path` (`:152-160`) composes the dataset under the
> name the review itself resolves (`CANDIDATE_DATABASE_NAME`, imported from the shipped snapshot models
> rather than re-spelled), so the dataset a run creates is the dataset the comparison opens *by name*
> rather than by two conventions agreeing. `baseline_origin_path` (`:163-166`) names the record this
> module owns — `baseline-origin.json`, the origin of an identified **first generation** — which sits
> **beside** the dataset: the comparison reads the dataset, and "there was no before-generation and here is why" is
> a fact about the run rather than a recorded invariant, so keeping it out of the database is what keeps
> it out of every read the knowledge plane answers. The other record a half may carry is the *selected
> baseline's* generation record, owned by
> `application/knowledge_baseline_generation.py`; a half carries
> one of the two and never both, because a half began from exactly one of them.
>
> **`BaselineOrigin` records one act, not a second copy of the dataset.** It is an
> `ar-knowledge-baseline-origin/v1` record whose `state` is the single literal `first-generation` and
> whose `pre_feature_history` is the single literal `not-recorded` — the two closed values that
> distinguish an empty first generation from a history that was measured and found empty, and from an
> unknown. `repository_id`, `schema_version` and `logical_digest` are read back from the dataset that
> was created, so the record cannot claim an identity the bytes do not hold. `selected_baseline` is
> `none` and is recorded because the two facts differ: "this run selected no prior dataset" is what the
> run observed, while "the repository never published one" is a claim about the repository that no
> caller input here can establish. `code_base_commit` is an **observation** of the code base the
> establishing run saw — it is not a source endpoint, and how a comparison binds its source side stays
> the review's own resolution. The remaining fields name the run: `leaf_id`, `contract_path`,
> `authorization_ref` and `recorded_at`. `write_baseline_origin` writes it as canonical JSON through
> `atomic_write_bytes`, for the reason the candidate receipt gives — the same record always has the same
> file content, so a digest over the file is a digest over the facts.
>
> **`read_baseline_origin` distinguishes "no record" from "a record that will not read".** An absent file
> is `None`. A present file that cannot be decoded or does not validate raises `KnowledgeStorageError`,
> and that is the point rather than an inconvenience: a half whose origin cannot be read is not an
> identified first generation, and answering "no record" would let a *damaged* record read as an older,
> unrecorded half — which is exactly the state the unidentified/identified split exists to keep apart.
>
> **The readers are one family with one signature shape, and the shape is what makes three callers
> possible.** `read_dataset_identity(database)` returns a `SnapshotIdentity` or a `str` reason;
> `read_captured_dataset_identity(payload, origin)` asks the same question of **bytes** rather than of a
> path, staging them in a private temporary directory through the same reader and reporting the reason
> against the path the caller handed over (a reason naming the staging directory would tell an operator
> about this module's internals instead of about their dataset); and `damaged_before_half_reason(path)`
> is the path-shaped sibling of `read_before_half` for a caller that names a *file* rather than the
> half's directory. All three funnel through `_dataset_identity_of`, which converts
> `KnowledgeStorageError`, `apsw.Error` and `OSError` into the reason string — the exception set is the
> union of what the shipped `dataset_identity` raises, so a file that is gone, not SQLite, written by
> another code generation or bound to no namespace is one input fact rather than four tracebacks.
>
> **`read_before_half` is the four-state machine a writer must consult before it writes anything.**
> `absent` (no dataset), `damaged` (a named reason), `unidentified` (a readable dataset with no recorded
> origin), or `identified` (a readable dataset whose record agrees with it). The dataset is *read*, not
> merely found: `_read_half` composes `read_dataset_identity` with `read_baseline_origin` and
> `_origin_mismatch`, and the mismatch check compares `repository_id`, `schema_version` and
> `logical_digest` between the record and the bytes and names **both** paths in its reason, because
> those are the two files a reader has to look at to see the disagreement for themselves.
>
> **`unreadable_half_refusal` is the one refusal the *review* answers an unreadable side with, and it is
> deliberately not a new code.** A comparison is between two dataset files, so a file that is not a
> dataset makes SQLite raise from inside the read; both sides are preflighted here instead — the
> baseline through its recorded origin as well as its bytes, the candidate through its bytes when it is
> present — so "the before side is unreadable" and "the before side is absent" stay two named states
> rather than one named state and one traceback. An absent side is deliberately not this function's
> business: absence has its own refusal already (`missing_dataset_half`) and is the more actionable
> answer when nothing was placed at all. The refusal reuses the shipped `candidate_dataset_absent` code
> rather than widening a shared refusal vocabulary the transport and the renderer both read; the *state*
> — present but unreadable — travels in the detail and in `offending_input`, which is where a caller
> distinguishing the two reads it, and `next_action` names the two repairs (re-author the candidate, or
> place the dataset the leaf forks from) because only one of the two sides can be repaired by authoring
> knowledge again.
>
> ### Conventions
>
> The module is a leaf of the `application/` route and imports only downward: the storage owners
> (`memory.knowledge.logical.dataset_identity`, `memory.knowledge.refusals`), the kernel primitives
> (`kernel.atomic_write`, `kernel.canonical_json`) and the model vocabulary
> (`models.knowledge.base`, `models.knowledge.candidate`, `models.knowledge.review`,
> `models.knowledge.snapshot`). It defines no storage operation of its own and opens no database except
> through the shipped `dataset_identity`. The public surface is the twelve names `__all__` publishes
> (`:60-73`) — the file-name literal, the origin record and the half's state, the two layout helpers, the
> five readers, the origin writer and the one refusal — and everything else in the file is private by the
> leading underscore, the same split its sibling modules use. (This card previously said "eleven names";
> re-counted against `__all__` in this candidate, the surface is twelve, the omitted one being
> `write_baseline_origin`.)
>
> ### Invariants And Boundaries
>
> - **The record is not knowledge and the half is not the repository's memory.** Both live in the leaf's
>   disposable knowledge root beside the candidate; nothing here writes a record kind, a table or a row,
>   and no read the knowledge plane answers can reach the origin record.
> - **Only one generation is ever recorded by *this* record, and it is never restated.** `state` and
>   `pre_feature_history` are single-literal fields, so an origin record cannot describe a second
>   generation or claim that pre-feature history was measured. A half whose before side is a *selected*
>   baseline is described by the other owner's generation record instead
>   (`application/knowledge_baseline_generation.py`), which is the
>   one record a half carries in that case — the two never coexist, because a half began from exactly one
>   of them.
> - **A read never raises for an input fact and never repairs.** The readers answer with reasons; a
>   damaged half is named and left exactly as it is, and `read_baseline_origin` raises only for the
>   record's own unreadability — where a silent `None` would be the damaging answer.
> - **Identity is read back, never asserted.** `repository_id`, `schema_version` and `logical_digest` in
>   the record come from the dataset, and `_origin_mismatch` re-checks all three on every read.
> - **Boundary.** This module establishes nothing, admits nothing and refuses nothing on the review's
>   behalf beyond the one named refusal above; `knowledge_first_generation` owns establishment,
>   `knowledge_baseline_generation` owns the selected baseline's generation, and `knowledge_review` owns
>   the composition that consumes the refusal.
>
> ### Todos
>
> None recorded. The module is new in `260921-ICR-L5`, so nothing here is a carried limitation. The one
> change `260921-ICR-L18` made to this module is the docstring reconciliation recorded above: its
> docstring said the half holds "exactly two files", which stopped being true once a half could carry the
> selected baseline's generation record instead of the origin record. **No behaviour, reader, writer or
> test changed with it**, and every range on this card was re-derived against the moved candidate rather
> than carried (the reconciliation added three lines, so every construct below it moved by three).

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` in the memory
layer reads "No entries configured yet", so it carries no `Domain Documentation` category). The
statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The references below describe the current derived-index readers and their actual model/storage/preflight owners. The historical account above is retained history, not a claim that the current module owns a two-file layout, origin record, four-state reader or twelve-name export surface.



- The module preflights the derived indexes selected for a review and creates no canonical dataset layout. [1]




- read_dataset_identity returns SnapshotIdentity or a reason for a non-file and for KnowledgeStorageError, apsw.Error or OSError; dataset_identity opens the selected index read-only and closes its connection. [10]




- Review preflight checks each existing baseline/candidate index in order and returns candidate_dataset_absent for the first unreadable one, putting the read failure in detail, that half in offending_input and a rebuild instruction. [15]



- SnapshotIdentity extends KnowledgeModel and validates repository_id with UUID_PATTERN, schema_version with the label-length bound and logical_digest with SHA256_PATTERN. [17]



- dataset_identity produces the SnapshotIdentity used by this module. The separate whole-pair preflight sequences absent-half, unreadable-index and candidate-namespace/receipt refusals; the receipt preflight delegates to review_namespace rather than reading the retired baseline-origin record. [18]


### Cross-Repo References

No cross-repository behavior is implemented in this file. Callers supply the two selected derived-index paths; this module does not create or require the retired leaf knowledge-root layout. The read identity carries the namespace, schema and logical digest the storage owner reads from that index.

No meaningful cross-repo references found.
