# mcp/src/agents_remember/application/knowledge_baseline_generation.py

## Governing Overview

[application route overview](overview.md)

## Purpose

**Which comparison generation the review's before half holds, and how one admitted run fills it.**
The comparison is *between* two datasets, so the before side is not a scratch copy of whatever the
latest run was handed: it is the baseline that comparison was **opened on**. This module owns the one
decision neither of its two collaborators makes — whether this run may fill the half at all, and as
which generation (`fill_admitted_before_half` `:464-500`) — plus everything that decision is written
with: the durable generation record (`BaselineGeneration` `:108-160`), the four-state read of what the
half currently holds (`StandingGeneration` `:211-251`, `read_standing_generation` `:354-373`), the one
first placement (`place_original_baseline` `:579-612`), and the deliberate rebase with lineage
(`rebase_comparison_baseline` `:615-657`).

Two facts have to stay apart for a stable baseline to survive a repeated ingest, and the module's own
docstring names them as the reason it exists:

- **The first admitted baseline is the comparison's original one.** `--baseline` and `--publish-to`
  may name one path, so a second successful run's captured bytes are the *first* run's publication — a
  dataset that already contains the addition. Placing those bytes is how the review comes to compare a
  dataset against itself, with the addition present on both sides and an empty delta. The half is
  therefore filled **once** and a later run keeps the before side it was first handed.
- **A deliberate new baseline is a new generation, with lineage.** The way out is explicit and
  recorded, never silent: the replacement dataset is published with a record beside it naming the
  generation it began from *and* that generation's exact dataset identity.

The record is a *local operation fact* about the run that filled the half — the same kind of object the
first generation's origin record and the candidate receipt are — which is why it lives beside its
dataset in the leaf's disposable knowledge root. It is not knowledge, it decides no authority, and it
is never a second source of authored truth.

Reading the half and its datasets belongs to
[`application/knowledge_before_half.py`](knowledge_before_half.py.md) (layout, four states, first
generation's origin record), and establishing a repository's *first* generation belongs to
[`application/knowledge_first_generation.py`](knowledge_first_generation.py.md). Both are **called,
never reimplemented** (`_establish_first_generation` `:503-516` delegates the whole establishment;
`read_before_half` is the module's own four-state gate for the named-baseline case).

## Code Commentary

### Logic

**The record is one file beside the dataset, and its state is the one value that distinguishes it from
a first generation.** `BASELINE_GENERATION_NAME` (`:91-91`) is `baseline-generation.json`, resolved by
`baseline_generation_path` (`:266-269`). `GENERATION_VERSION` (`:92-94`) is the
`ar-knowledge-baseline-generation/v1` vocabulary, and `SELECTED_BASELINE` (`:97-97`) is the single
literal its `state` carries — the one state that separates "the dataset here is a baseline the run was
*handed*" from the first generation's `first-generation`, so a reader never has to infer which of the
two records it is looking at from a file name. `write_baseline_generation` (`:272-282`) writes it as
canonical JSON through the kernel's `atomic_write_bytes`, for the reason the origin record gives: the
same record always has the same file content, so a digest over the file is a digest over the facts.

**`BaselineGeneration` records identity that was read back, plus the lineage, and its own validator
refuses a record whose fields contradict each other.** `repository_id`, `schema_version` and
`logical_digest` come from the dataset that was actually published (built in `_generation_record`
`:763-792` from `admitted.identity`), so the record cannot claim an identity the bytes do not hold —
the same discipline the origin record follows. `selected_baseline` (`:125-125`) names the path the
bytes were captured from **before** the run could publish over it, which is the provenance a reader
needs to see that the dataset this comparison opens on is no longer the one at that path.
`generation_index` (`:124-124`) is *recorded* rather than counted, because "how many times has this
comparison been re-pointed" must be visible without trusting a directory to still hold its history.
The lineage pair `parent_generation_id` + `parent_identity` (`:132-133`) is what lets a reader say
*which dataset* was replaced rather than only which generation number preceded this one. The
`model_validator` `_lineage_agrees_with_the_index` (`:140-160`) is the load-bearing part: a record is
read by a verifier that was not present at the write, so index 1 must carry no parent, and a parent id
and its identity are both present or both absent.

**The generation id is derived, not minted.** `generation_identity` (`:319-348`) is a `uuid5` over the
version, the index, the three identity fields and the parent (or the spelled `_NO_PARENT` placeholder
`:105-105`), under the literal `_GENERATION_NAMESPACE` (`:102-102`) — a namespace that names one
*generation*, a local fact about one leaf's before half, rather than anything the knowledge plane
stores. Deterministic rather than freshly minted so a reader can **recompute** it: an id that does not
belong to the generation beside it is then a fact a verifier falsifies instead of a value it takes on
trust. Nothing enters the derivation that a reader of the record cannot see.

**The three values a placement is handed, and why each is a separate shape.** `CapturedBaseline`
(`:179-189`) is the admitted bytes read *before* the run could publish over the path they came from —
the bytes are carried rather than the path, because a read of the same path afterwards is a read of the
*after* state. `AdmittedBaseline` (`:193-203`) pairs those bytes with the `SnapshotIdentity` they were
read as, because by the time anything is written they are one fact: the bytes are what would be
published and the identity is what those bytes *are*, read through the same reader every other side
uses (`read_admitted_baseline` `:519-531`, over the bytes rather than over the path, since the path may
already hold this run's publication). `BaselineRun` (`:164-175`) is the run's own admitted facts — the
leaf, the enclosure contract, the authorization and the observed code base — the same four the
first-generation record carries.

**`read_standing_generation` is the four-state machine, and it reads the record before the bytes.** The
record is the half's own statement of what it holds, so it is consulted first (`:354-373`): a record
that cannot be read at all is `damaged` even when a perfectly good dataset sits beside it, because
answering `adopted` there would adopt whatever is on disk as the original baseline. The four answers
are `absent` (no dataset), `recorded` (a readable dataset whose record agrees with it), `adopted` (a
readable dataset with **no** record — the baseline this comparison already opened on, placed by a run
from before the record existed), and `damaged` (`_standing_with_a_dataset` `:376-415`,
`_standing_without_a_dataset` `:418-435`). The mismatch check `_record_mismatch` (`:438-458`) compares
the whole identity — repository, schema **and** logical digest — and names both paths, because those
are the two files a reader has to look at to see the disagreement for themselves. The identity travels
*with* the damage: `StandingGeneration.identity` (`:227-227`) is populated whenever the bytes could be
read at all, including when they disagree with the record, so a refusal can name the bytes actually on
disk rather than only the state they are in.

**`StandingGeneration` derives the id of an unrecorded half instead of leaving it unknown.**
`generation_id` (`:230-245`) answers with the recorded id when there is a record, and otherwise with
the id the half's own dataset facts derive — index 1, no parent. That is what lets a rebase *from* an
adopted half record an exact parent rather than a placeholder. `generation_index` (`:247-251`) answers
`1` for any half with no record.

**`read_baseline_generation` refuses an occupied record path rather than reading it as absent.**
(`:285-316`.) An absent file is `None`; a present file that will not decode or validate is a
`KnowledgeStorageError`; and a record *path* occupied by something which is not a record file at all
— a directory left where the record belongs — is that same error and not an absent record. Reading an
obstruction as absent is how it becomes invisible and the half goes on calling itself an adopted
baseline. This is a strictness branch the leaf's own verification round added.

**The one placement that is not a rebase lands the dataset first, and that order is deliberate.**
`place_original_baseline` (`:579-612`) fills an empty half with generation 1 of the comparison: there
is no earlier baseline to name as a parent, and a half holding these bytes without the record that
names them reads as an *adopted* baseline — which is exactly what it is when there was nothing there
before. The opposite order would leave a record naming bytes that are not on disk: the louder but
unnecessary damage of claiming a generation the half does not hold. It publishes with
`record_first=False` (`:603-607`).

**The rebase is the deliberate answer, and the record is durable before the bytes it names.**
`rebase_comparison_baseline` (`:615-657`) builds generation `standing.generation_index + 1` with the
standing half's id *and* identity as its parent pair, and publishes with `record_first=True`
(`:646-650`). The reason is the failure contract rather than style: this act *replaces* a baseline that
is already on disk, so landing the replacement first would mean a record that then failed to write
left a half holding a dataset no record describes — and for a half whose original was never recorded
that state reads `adopted`, which would relabel the replacement as the comparison's original baseline
and lose the one the comparison was actually opened on. With the record first, the one window that
remains is the previous bytes beside a record that disagrees with them: the named `damaged` state a
reader can act on.

**`_publish_generation` runs two *named* legs, and a failure states which leg refused and what the half
holds now.** (`:660-696`.) The order is an explicit parameter; the legs are `_publish_dataset_leg`
(`:699-712`) and `_publish_record_leg` (`:715-738`); and on any refusal `_failed_placement`
(`:741-760`) re-reads the half and appends the state plus the dataset identity it actually holds. Both
leg clauses say only **"did not report success"** rather than "was not written" / "was not replaced",
because the kernel owner publishes the bytes and *then* flushes the directory that names them, so a
failure it raises can arrive after the rename already put them on disk. The read-back is where that
fact is measured, and it is the whole of the claim. This wording is the leaf's second verification
round (F3), and the record leg additionally reads its own write back and refuses if the record did not
return unchanged (`:733-737`).

**The four routes out are the contract, and their order is the contract too.** `_place_or_keep`
(`:551-576`) answers in this order: a `damaged` half is named before anything else; the half's own
dataset being the one this run was handed is a **no-op** rather than a placement, so a retry restates
nothing (`_present` `:809-815`); an `absent` half gets the comparison's first generation; and a
standing baseline that differs is kept unless the caller's deliberate `--rebase-baseline` word says
otherwise (`_conflicting_baseline` `:818-840`). `fill_admitted_before_half` (`:464-500`) is the one
entry point and adds the two rules that sit *above* the generation reader: **no baseline named at all**
hands the whole decision to `knowledge_first_generation` (`_establish_first_generation` `:503-516`),
and an `identified` half — the first generation this leaf began from — is kept whatever the run named,
with the rebase flag explicitly unable to override it (`_identified_first_generation` `:843-856`). The
rebase flag never repairs damage either: both are named states with their own owners, and a flag that
silently overrode them would be a second, quieter way to rewrite what a comparison is *of*.

**The report lines are the result, and each carries the facts its caller needs to act.**
`_conflicting_baseline` (`:818-840`) carries four: which generation the half holds and its dataset
identity, that the standing baseline is *this comparison's original* rather than a stale artifact, the
state clause that says whether a record is even present, and the exact action that begins a new
generation deliberately. `_not_placed` (`:798-806`) takes the state's own sentence rather than the
object carrying it, because both readers of a half produce one — the generation reader here and the
before-half layout reader — and the report must say the same thing about either.

### Conventions

The module is a leaf of the `application/` route and imports only downward: the two sibling
application owners (`knowledge_before_half`, `knowledge_first_generation`), the kernel primitives
(`kernel.atomic_write`, `kernel.canonical_json`), one storage refusal
(`memory.knowledge.refusals.KnowledgeStorageError`) and the model vocabulary
(`models.knowledge.base`, `models.knowledge.candidate`). It defines no store, journal or approval
authority of its own and opens no database except through the shipped readers. `__all__` (`:69-86`)
publishes fifteen names — the two literals and the file-name constant, five dataclasses/state aliases,
the path/write/read helpers, the id derivation and the three placement entry points — and everything
else is private by the leading underscore, the same split its sibling modules use.

### Invariants And Boundaries

- **The half's generation record is not knowledge.** It lives in one leaf's disposable knowledge root
  beside the candidate; nothing here writes a record kind, a table or a row, and no read the knowledge
  plane answers can reach it.
- **The half is filled once, and a standing baseline is replaced only by an explicit rebase.** No
  silent fallback to current HEAD or current knowledge, no second store, no parallel writer: this
  module composes the shipped readers and writers rather than adding one.
- **Identity is read back, never asserted.** Every identity field on a record comes from the dataset
  that was actually published, and `_record_mismatch` re-checks all three on every read.
- **A read never raises for an input fact and never repairs.** A damaged half is named and left
  exactly as it is; the only raise in the module is the record's own unreadability, where a silent
  `None` would be the damaging answer.
- **The two legs land separately, so the outcome is only ever stated by a read-back.** No refusal this
  module produces claims a byte outcome it did not measure.
- **Boundary.** This module decides *what the half is afterwards*; the caller owns *whether* the run
  may fill it at all (the CLI's `_placement_refusal`), publication of the candidate belongs to
  `knowledge_curator_ingest`, and establishing a first generation belongs to
  `knowledge_first_generation`. What a closeout records about the generation it reviewed, and any
  retention contract for a *superseded* generation's bytes, are other leaves' work — the rebase
  replaces the bytes in place and preserves only their identity in the record.

### Todos

None recorded. The module is new in this leaf, so nothing here is a carried limitation. Two
deliberately unfixed conditions are recorded where they belong rather than here: the CLI owns no lock
between two concurrent ingests (a bounded failure mode, since a record-first rebase cannot leave
replacement bytes with no record), and `--rebase-baseline` cannot replace an identified first
generation, because R05's preservation boundary is stronger than R18's rebase action.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` in the memory
layer reads "No entries configured yet", so it carries no `Domain Documentation` category). The
statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the shipped candidate: the module's own docstring and its two
named facts, the record's fields and its lineage validator, the derived id, the four-state read, the
two publication legs and the report lines. Ranges are the exact construct extents in this candidate.

- The module's own statement of the two facts that must stay apart — the first admitted baseline is the comparison's original, and a deliberate new baseline is a new generation with lineage — and of the record being a local operation fact rather than knowledge. [1]
- The published surface: the file-name/version/state literals, the five values, the readers, the id derivation and the three placement entry points. [2]
- The record's file name beside the dataset, the one state that distinguishes it from a first generation, the id namespace and the spelled no-parent placeholder. [3]
- **The recorded generation: read-back identity fields, the recorded index, the captured-from path, and the lineage pair of parent id plus parent dataset identity.** [4]
- **The record's own consistency rule: index 1 carries no parent, and a parent id and its identity are both present or both absent.** [5]
- The run's admitted facts, carried to the record writer. [6]
- **The admitted bytes read before the run could publish over the path they came from — carried as bytes, not as a path.** [7]
- **The bytes paired with the identity they were read as, so no write is handed bytes whose identity nobody read.** [8]
- The four states of the half and the three placement answers, as closed literals. [9]
- **The half's generation as one of four states, carrying the identity whenever the bytes could be read — including when they disagree with the record.** [10]
- **An adopted half's id, derived from the dataset facts that are actually there rather than left unknown, so a rebase from it can record an exact parent** — the value's two derived-property accessors, distinct from the like-named fields the record itself carries. [11]
- What one run left in the half: its state, the report's line, and the record. [12]
- The record's path inside one before half, and its canonical, atomic, durable write. [13]
- **The record reader's three answers: absent, a storage error for a record that will not read, and that same error for a record *path* occupied by something that is not a record file.** [14]
- **The deterministic generation id a reader can recompute from the record's own facts.** [15]
- **The four-state read, taken record-first so an unreadable record is damage even beside a good dataset.** [16]
- The three ways a readable dataset answers: recorded, adopted, or damaged with the observed identity travelling with it. [17]
- The two ways a half with no dataset answers: absent, or a record that lost the side it names. [18]
- The whole-identity disagreement check, naming both paths a reader has to open. [19]
- **The one entry point: whether this run may fill the half at all, and which of the two owners answers.** [20]
- The no-baseline-named branch, which hands the whole establishment to the sibling owner rather than reimplementing it. [21]
- **The bytes read as a dataset before anything is written, so a corrupt expected dataset is never reported as placed.** [22]
- The named-baseline branch: keep what stands, or write a generation. [23]
- **The one placement that is not a rebase, and why its dataset leg lands first.** [24]
- **The deliberate rebase: a new generation whose record names the generation it replaced by id and by exact dataset identity, published record-first so the one remaining window is the named damage rather than replacement bytes with no record.** [25]
- **The two-leg publication whose order is the failure contract, and the read-back that states the outcome the leg clause deliberately does not.** [26]
- The record built from the dataset that was actually published and the run's facts. [27]
- The two answer lines whose failure to distinguish a refusal from a no-op would leave a caller unable to act: the kept-standing-baseline line with its generation, identity, state clause and rebase action, and the kept-first-generation line the rebase flag cannot override. [28]
- One dataset identity as a report line names it, or the absence the half records. [29]
- **The sibling owner this module composes for the half's layout and its four-state read, and the readers it calls rather than reimplements.** [30]
- **The sibling owner that performs the establishment when no baseline is named, the run it is handed, and the value it answers with.** [31]
- The kernel write and canonical-JSON primitives the record is written and read through. [32]
- The one storage refusal this module raises for a record that is present but will not read. [33]
- The model vocabulary the record is built from — the frozen base and the four pattern/length bounds its fields are validated against. [34]
- The identity value every field of the record is read back from. [35]
- **The CLI surface that calls this module: the argument that carries the deliberate word, the capture that reads the bytes before publication, and the run's one placement seam.** [36]
- **The successful journey these rules exist to protect: two successful writes over one path, the two retries, and the deliberate rebase.** [37]
- **Every way a placement refuses or loses a leg without losing the baseline, including the two flush windows that forced the "did not report success" wording.** [38]

### Cross-Repo References

No cross-repository behavior is implemented in this file. The half, its dataset and the generation
record beside it all live inside one leaf's disposable knowledge root, and the record carries no
identity beyond the repository namespace the dataset itself holds.

No meaningful cross-repo references found.
