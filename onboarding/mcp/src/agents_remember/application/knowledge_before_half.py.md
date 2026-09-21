# mcp/src/agents_remember/application/knowledge_before_half.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_before_half.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-21T13:40+02:00 |
| reviewedWorkingCandidate | candidate `ar/260921-icr-l5`, uncommitted; production line `702714fc05363cb28eacaf101ba8384475a6aa56` |
| lastVerifiedCommitHash | `c755cec64fa9dc12e797c9fcfb4c96822718330c` |
| lastVerifiedCommitDate | 2026-09-21T15:29:12+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The review's before half**: the layout one before side occupies, the origin record that says which
generation its dataset is, and the readers that decide what the half currently *is*. A comparison is
*between* two datasets, so whatever a review is opened on must have a before side; this module owns
that side's shape and every read of it, and nothing here establishes one. Establishing a first
generation is the separate act in
[`application/knowledge_first_generation.py`](knowledge_first_generation.py.md), which is the caller of
these readers.

Three facts are told apart here because a writer that confuses them writes the wrong thing, and the
module's own docstring names them as its load-bearing distinctions:

- **Absent is not empty.** A half with no dataset is a pair that cannot be compared; it is not a
  measured-empty history, and it must never be answered with a freshly created dataset unless the
  caller's own act says the repository's knowledge begins there.
- **Identified is not unidentified.** A dataset with **no** recorded origin is a fork point some
  `--baseline` run placed; a dataset **with** a matching record is an explicitly identified first
  generation. A later run keeps the first and never restates the second.
- **Damaged is neither.** Bytes that cannot be read as a dataset of this code, a record that cannot be
  read at all, or a record whose identity no longer matches the bytes beside it: each is a state that
  has to be *named* with its reason and left exactly as it is.

Every read answers with a reason instead of raising, and that is deliberate rather than defensive: a
file that is not a dataset is an **input** fact in all three callers — the ingest admission reading a
selected fork point, the ingest CLI inspecting the half it is about to fill, and the review refusing a
comparison whose side cannot be opened — so each caller states the fact in its own voice instead of
receiving one module's exception.

## Code Commentary

### Logic

**The half's layout is two files, and the origin record is deliberately not one of them being
knowledge.** `baseline_database_path` composes the dataset under the name the review itself resolves
(`CANDIDATE_DATABASE_NAME`, imported from the shipped snapshot models rather than re-spelled), so the
dataset a run creates is the dataset the comparison opens *by name* rather than by two conventions
agreeing. `baseline_origin_path` names the second file, `baseline-origin.json`, which sits **beside**
the dataset: the comparison reads the dataset, and "there was no before-generation and here is why" is
a fact about the run rather than a recorded invariant, so keeping it out of the database is what keeps
it out of every read the knowledge plane answers.

**`BaselineOrigin` records one act, not a second copy of the dataset.** It is an
`ar-knowledge-baseline-origin/v1` record whose `state` is the single literal `first-generation` and
whose `pre_feature_history` is the single literal `not-recorded` — the two closed values that
distinguish an empty first generation from a history that was measured and found empty, and from an
unknown. `repository_id`, `schema_version` and `logical_digest` are read back from the dataset that
was created, so the record cannot claim an identity the bytes do not hold. `selected_baseline` is
`none` and is recorded because the two facts differ: "this run selected no prior dataset" is what the
run observed, while "the repository never published one" is a claim about the repository that no
caller input here can establish. `code_base_commit` is an **observation** of the code base the
establishing run saw — it is not a source endpoint, and how a comparison binds its source side stays
the review's own resolution. The remaining fields name the run: `leaf_id`, `contract_path`,
`authorization_ref` and `recorded_at`. `write_baseline_origin` writes it as canonical JSON through
`atomic_write_bytes`, for the reason the candidate receipt gives — the same record always has the same
file content, so a digest over the file is a digest over the facts.

**`read_baseline_origin` distinguishes "no record" from "a record that will not read".** An absent file
is `None`. A present file that cannot be decoded or does not validate raises `KnowledgeStorageError`,
and that is the point rather than an inconvenience: a half whose origin cannot be read is not an
identified first generation, and answering "no record" would let a *damaged* record read as an older,
unrecorded half — which is exactly the state the unidentified/identified split exists to keep apart.

**The readers are one family with one signature shape, and the shape is what makes three callers
possible.** `read_dataset_identity(database)` returns a `SnapshotIdentity` or a `str` reason;
`read_captured_dataset_identity(payload, origin)` asks the same question of **bytes** rather than of a
path, staging them in a private temporary directory through the same reader and reporting the reason
against the path the caller handed over (a reason naming the staging directory would tell an operator
about this module's internals instead of about their dataset); and `damaged_before_half_reason(path)`
is the path-shaped sibling of `read_before_half` for a caller that names a *file* rather than the
half's directory. All three funnel through `_dataset_identity_of`, which converts
`KnowledgeStorageError`, `apsw.Error` and `OSError` into the reason string — the exception set is the
union of what the shipped `dataset_identity` raises, so a file that is gone, not SQLite, written by
another code generation or bound to no namespace is one input fact rather than four tracebacks.

**`read_before_half` is the four-state machine a writer must consult before it writes anything.**
`absent` (no dataset), `damaged` (a named reason), `unidentified` (a readable dataset with no recorded
origin), or `identified` (a readable dataset whose record agrees with it). The dataset is *read*, not
merely found: `_read_half` composes `read_dataset_identity` with `read_baseline_origin` and
`_origin_mismatch`, and the mismatch check compares `repository_id`, `schema_version` and
`logical_digest` between the record and the bytes and names **both** paths in its reason, because
those are the two files a reader has to look at to see the disagreement for themselves.

**`unreadable_half_refusal` is the one refusal the *review* answers an unreadable side with, and it is
deliberately not a new code.** A comparison is between two dataset files, so a file that is not a
dataset makes SQLite raise from inside the read; both sides are preflighted here instead — the
baseline through its recorded origin as well as its bytes, the candidate through its bytes when it is
present — so "the before side is unreadable" and "the before side is absent" stay two named states
rather than one named state and one traceback. An absent side is deliberately not this function's
business: absence has its own refusal already (`missing_dataset_half`) and is the more actionable
answer when nothing was placed at all. The refusal reuses the shipped `candidate_dataset_absent` code
rather than widening a shared refusal vocabulary the transport and the renderer both read; the *state*
— present but unreadable — travels in the detail and in `offending_input`, which is where a caller
distinguishing the two reads it, and `next_action` names the two repairs (re-author the candidate, or
place the dataset the leaf forks from) because only one of the two sides can be repaired by authoring
knowledge again.

### Conventions

The module is a leaf of the `application/` route and imports only downward: the storage owners
(`memory.knowledge.logical.dataset_identity`, `memory.knowledge.refusals`), the kernel primitives
(`kernel.atomic_write`, `kernel.canonical_json`) and the model vocabulary
(`models.knowledge.base`, `models.knowledge.candidate`, `models.knowledge.review`,
`models.knowledge.snapshot`). It defines no storage operation of its own and opens no database except
through the shipped `dataset_identity`. The public surface is the eleven names `__all__` publishes —
three dataclasses/literals, the layout helpers, the four readers and the refusal — and everything else
in the file is private by the leading underscore, the same split its sibling modules use.

### Invariants And Boundaries

- **The record is not knowledge and the half is not the repository's memory.** Both live in the leaf's
  disposable knowledge root beside the candidate; nothing here writes a record kind, a table or a row,
  and no read the knowledge plane answers can reach the origin record.
- **Only one generation is ever recorded, and it is never restated.** `state` and
  `pre_feature_history` are single-literal fields, so a half cannot record a second generation or claim
  that pre-feature history was measured.
- **A read never raises for an input fact and never repairs.** The readers answer with reasons; a
  damaged half is named and left exactly as it is, and `read_baseline_origin` raises only for the
  record's own unreadability — where a silent `None` would be the damaging answer.
- **Identity is read back, never asserted.** `repository_id`, `schema_version` and `logical_digest` in
  the record come from the dataset, and `_origin_mismatch` re-checks all three on every read.
- **Boundary.** This module establishes nothing, admits nothing and refuses nothing on the review's
  behalf beyond the one named refusal above; `knowledge_first_generation` owns establishment and
  `knowledge_review` owns the composition that consumes the refusal.

### Todos

None recorded. The module is new in this leaf, so nothing here is a carried limitation.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` in the memory
layer reads "No entries configured yet", so it carries no `Domain Documentation` category). The
statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and its
three named distinctions, the two-file layout, the origin record's fields, the four-state read and the
one refusal. Ranges are the exact construct extents in this candidate.

| Finding | Anchor | Source |
| --- | --- | --- |
| The module's own statement of what it owns, the three facts a writer must tell apart, and why every read answers with a reason instead of raising. | "Absent is not empty."; "Identified is not unidentified."; "Damaged is neither." | mcp/src/agents_remember/application/knowledge_before_half.py:11-27 |
| The published surface: the layout constants, the origin record and the half's state, the four readers and the one refusal. | `__all__` | mcp/src/agents_remember/application/knowledge_before_half.py:57-70 |
| The origin record's file name and the three closed vocabulary values it carries — the version, the one generation state, and the one value pre-feature history has. | `BASELINE_ORIGIN_NAME`; `ORIGIN_VERSION`; `FIRST_GENERATION`; `NOT_RECORDED`; `BeforeHalfState` | mcp/src/agents_remember/application/knowledge_before_half.py:76-76; mcp/src/agents_remember/application/knowledge_before_half.py:77-77; mcp/src/agents_remember/application/knowledge_before_half.py:78-78; mcp/src/agents_remember/application/knowledge_before_half.py:81-81; mcp/src/agents_remember/application/knowledge_before_half.py:83-83 |
| **The recorded origin: every field a fact about this act, `selected_baseline` recorded as what the run observed rather than as a claim about the repository, and the code base recorded as an observation rather than as a source endpoint.** | `BaselineOrigin` | mcp/src/agents_remember/application/knowledge_before_half.py:86-117 |
| **The four states the half can be in, read from the half rather than assumed.** | `BeforeHalf` | mcp/src/agents_remember/application/knowledge_before_half.py:120-134 |
| One before side read, carried as the identity it holds, the origin record beside it, or the damage. | `_HalfReading` | mcp/src/agents_remember/application/knowledge_before_half.py:137-143 |
| The half's two files: the dataset under the name the review resolves, and the origin record beside it. | `baseline_database_path`; `baseline_origin_path` | mcp/src/agents_remember/application/knowledge_before_half.py:149-157; mcp/src/agents_remember/application/knowledge_before_half.py:160-163 |
| **The origin record written as canonical bytes, atomically and durably.** | `write_baseline_origin`; `atomic_write_bytes`; `canonical_json_bytes` | mcp/src/agents_remember/application/knowledge_before_half.py:166-176; mcp/src/agents_remember/kernel/atomic_write.py:53-72; mcp/src/agents_remember/kernel/canonical_json.py:27-31 |
| **The one place this module raises: an origin record that is present but will not read is a storage error, because answering `None` would let a damaged record read as an older, unrecorded half.** | `read_baseline_origin`; `KnowledgeStorageError` | mcp/src/agents_remember/application/knowledge_before_half.py:179-201; mcp/src/agents_remember/memory/knowledge/refusals.py:27-32 |
| **The value-or-reason reader: a file is a dataset only once it is read as one, and every way that read fails is an input fact rather than a defect of the run.** | `read_dataset_identity`; `dataset_identity` | mcp/src/agents_remember/application/knowledge_before_half.py:207-220; mcp/src/agents_remember/memory/knowledge/logical.py:153-175 |
| **The same question asked of already-captured bytes, staged privately and reported against the path the caller handed over.** | `read_captured_dataset_identity` | mcp/src/agents_remember/application/knowledge_before_half.py:223-237 |
| The one conversion of the storage owner's three failure types into a reason string, with the reporting path kept separate from the read path. | `_dataset_identity_of` | mcp/src/agents_remember/application/knowledge_before_half.py:240-251 |
| **The four-state read: the dataset is read, the record beside it is read, and the three identity fields are compared before a half may be called identified.** | `read_before_half`; `_read_half`; `_origin_mismatch` | mcp/src/agents_remember/application/knowledge_before_half.py:254-283; mcp/src/agents_remember/application/knowledge_before_half.py:299-314; mcp/src/agents_remember/application/knowledge_before_half.py:317-338 |
| The path-shaped sibling for a caller that names a file rather than a directory, where absence is deliberately not this reader's answer. | `damaged_before_half_reason` | mcp/src/agents_remember/application/knowledge_before_half.py:286-296 |
| **The one refusal the review answers an unreadable side with: both sides preflighted, the shipped `candidate_dataset_absent` code reused rather than a shared vocabulary widened, and the state carried in the detail and the offending input.** | `unreadable_half_refusal`; `_unreadable_half_refusal`; `ReviewRefusal` | mcp/src/agents_remember/application/knowledge_before_half.py:344-374; mcp/src/agents_remember/application/knowledge_before_half.py:377-392; mcp/src/agents_remember/models/knowledge/review.py:559-571 |
| The dataset name both halves take, imported rather than re-spelled, so a half's dataset is the file the review opens. | `CANDIDATE_DATABASE_NAME` | mcp/src/agents_remember/models/knowledge/snapshot.py:52-52 |
| The model vocabulary the record is built from — the frozen base and the four pattern/length bounds its fields are validated against. | `KnowledgeModel`; `UUID_PATTERN`; `SHA256_PATTERN`; `GIT_OBJECT_PATTERN`; `LABEL_MAX_LENGTH`; `PATH_MAX_LENGTH`; `REFERENCE_MAX_LENGTH` | mcp/src/agents_remember/models/knowledge/base.py:34-37; mcp/src/agents_remember/models/knowledge/base.py:18-18; mcp/src/agents_remember/models/knowledge/base.py:19-19; mcp/src/agents_remember/models/knowledge/base.py:20-20; mcp/src/agents_remember/models/knowledge/base.py:25-25; mcp/src/agents_remember/models/knowledge/base.py:27-27; mcp/src/agents_remember/models/knowledge/base.py:26-26 |
| The identity value every reader answers with, the module that produces it, and the receipt the sibling module reads to bind a half to the candidate's own admission. | `SnapshotIdentity`; `read_candidate_receipt` | mcp/src/agents_remember/models/knowledge/candidate.py:195-204; mcp/src/agents_remember/memory/knowledge/candidate_receipt.py:61-86 |
| The candidate files the establishing sibling reads to bind a half to the candidate's own admission — recorded here because that is the contract this module's readers are handed, not because this module reads them. | `candidate_database_path`; `candidate_receipt_path`; `CandidateReceipt` | mcp/src/agents_remember/models/knowledge/snapshot.py:58-61; mcp/src/agents_remember/models/knowledge/snapshot.py:64-67; mcp/src/agents_remember/models/knowledge/snapshot.py:109-141 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. Both sides of the pair live inside one
leaf's disposable knowledge root, and the module carries no identity beyond the repository namespace
the dataset itself records.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-21T14:40+02:00 — orchestrating session, pre-closeout metadata repair on `ar/260921-icr-l5`: the governed closeout refused the memory leg because this card carried no verification stamp at all (`external-memory closeout requires onboarding verification metadata before memory commit`), and the card's own recorded reason for omitting it cannot be satisfied by a card that the transaction must read. The two fields were therefore added naming the **production line this card was read against** — `702714fc05363cb28eacaf101ba8384475a6aa56`, the master line after this leaf's `worktree_sync` brought in leaf `260921-ICR-L1`'s landed extraction, at that closeout's recorded time `2026-09-21T13:27:46+02:00` — and the candidate row was corrected from the pre-sync base `f745e166` to that same production line. This is a statement of *what the reading was against*, not a claim that the constructs exist in that commit; the governed closeout's own metadata refresh re-stamps the card against the code commit this transaction creates, and that remains the real stamp. No range, claim or anchor was changed by this repair.
- 2026-09-21T13:40+02:00 — 260921-ICR-L5 curator (uncommitted change set on `ar/260921-icr-l5`, code base `f745e16659c5602252bb185a2ffccc356c2bde26`): created this one-to-one card for the new module, which is this leaf's first half: ICR-R05@v1 requires a legitimate first generation to be *identified*, and this module is where the identification and every read of it live. The card records the three distinctions the module's own docstring makes load-bearing (absent is not empty, identified is not unidentified, damaged is neither), the two-file layout that keeps the origin record out of every knowledge-plane read, the record's single-literal `state`/`pre_feature_history` pair and its read-back identity fields, the four-state `read_before_half`, the one place the module raises, and the reused `candidate_dataset_absent` code on the review's unreadable-half refusal. It also records what the module deliberately does **not** own: establishment belongs to `application/knowledge_first_generation.py`, and absence has its own refusal in `knowledge_review` rather than being answered here. Ranges are the exact construct extents in this candidate. This card carries **no `lastVerifiedCommitHash` and no `lastVerifiedCommitDate`**: every construct it cites exists only in this leaf's uncommitted candidate, so no commit contains the content a stamp would claim to have verified. Verification metadata is closeout-owned.
