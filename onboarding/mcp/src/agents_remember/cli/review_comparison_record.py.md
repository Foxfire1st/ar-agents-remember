# mcp/src/agents_remember/cli/review_comparison_record.py

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

**The production caller of the review comparison freeze** — `agents-remember
review-record-comparison`, the command that makes a leaf's Intent Reviewer comparison recordable at
all. The owner that produces a durable per-leaf generation,
`application/review_comparison_freeze.freeze_review_comparison`, was a complete and measured
operation with **no caller outside the test suite**: a closed leaf's review therefore reopened from
`history:recorded-source-range` for every leaf, and the reviewer's whole knowledge column rendered
its empty state. This adapter is that caller and it adds no mechanism: it composes the review through
the same resolution and the same composition the surface uses, and publishes only what the
composition actually bound.

Two facts about the operands are the whole of its boundary. A comparison is *between* two datasets,
and both are the **write plane's** artifacts: `knowledge-ingest` authors the candidate half and
places the dataset the leaf forks from, and the shipped first-generation owner establishes an
identified empty before half for a repository whose knowledge begins at this leaf. The default invocation authors no knowledge and does not establish absent halves; the freeze names that refusal. The explicit unchanged-knowledge mode validates the exact recorded memory base against published and pending knowledge before the existing placement owners prepare the normal pair. Neither mode authors a semantic record or publishes a knowledge dataset.

The command is reached from a **non-editable install** of the package, exactly as `knowledge-ingest`
is: `kernel/primitives/checkout_coordination.checkout_cli_location` refuses an undeclared CLI loaded
from the primary checkout and isolates one loaded from a linked worktree to that worktree's
disposable coordination root, so `--config` names the live coordination authority explicitly rather
than letting it be inferred.

## Code Commentary

### Logic

The paired `--recover-generation` and `--curator-record-digest` controls explicitly select one retained task-context parent and its original validated curator generation. Unpaired or conflicting live/absence controls refuse. Recovery delegates to `recover_review_comparison`, preserving old generations and original judgments; it neither scans arbitrary receipts nor creates a live candidate from historical inputs. An exact recovery retry uses the same explicit parent, unlike the ordinary command's standing-predecessor succession.

The explicit --unchanged-knowledge option routes code-only work through freeze_unchanged_knowledge_review; ordinary invocation continues to freeze the existing curated pair. The command still requires the real settings and enclosure contract, carries predecessor generation identity, and reports publication or refusal. It authors no knowledge or assessment and never defaults to the unchanged mode.

**`run` (`:141-172`) is four facts wide, and the report is its result.** `_invocation` answers the
argument list (or the sentence saying why it cannot be one); the standing generation, when the leaf
has published one, is named as the successor's predecessor; the request is composed from the
contract's own recorded identities rather than from anything the caller spelled; and
`freeze_review_comparison` is called once. The exit code is the outcome and not an error channel:
`EXIT_PUBLISHED` (`0`) when the freeze published, `EXIT_REFUSED` (`2`) when it answered with a named
refusal, and the refusal's own `code` / `detail` / `next_action` / `offending_input` are printed
because a caller decides what to do next from those rather than from a message composed here.

**The request is composed from the contract, so no argument list can aim a record at another leaf's
line.** `repository_id` is `contract.repo_name`; `leaf_id` is `contract.leaf_id`; and `master` is
`contract.parent_task_name or contract.task_name`, because a leaf enclosure names its parent task
while a master enclosure names itself. A generation is published under the `task_root` the contract
records, which is why `--contract` is required and is the write guard — the same role it plays in
`knowledge-ingest`, `memory-citations` and `memory-backfill`.

**`_standing_generation` (`:175-199`) decides the predecessor once, because the freeze derives the
successor's index from it.** `ComparisonFreezeOptions.parent` is documented as a *caller-known* fact,
and a caller that names none publishes an **index 1** generation: right for a leaf's first record
and wrong for every later one, because a leaf whose comparison legitimately changed would hold two
generations both claiming index 1 with different bindings — and `review_comparison_reopen` refuses a
tied highest index by design, so the leaf's own review could no longer say which comparison it was
reading. The function reads the leaf's published refs (`read_generation_refs`), takes the highest
recorded index, and breaks a tie at that index by the record's own `recorded_at` and then by
generation id, because directory order is not an answer. `None` — a leaf that has published nothing —
leaves the option unset, and the freeze publishes the first generation. `_recorded_at` (`:202-212`)
reads one generation's own instant and answers the empty string for a record that will not read, so
naming a predecessor can never raise in the middle of a report.

**`_invocation` (`:215-240`) answers every argument-list fact before a contract, a dataset or a byte
is touched.** A blank `--contract` or `--config` is refused by name; the contract is loaded through
the shipped `load_contract`, whose own typed failure is carried rather than replaced; and the
caller's calls are assembled into the two `ComparisonFreezeOptions` fields this command can supply —
the evidence citations, and the declared historical absences, deduplicated in the order given.

**`_evidence_inputs` (`:243-265`) is where a citation that is not a citation is caught.** Each
`--evidence` value is split on one colon into an owner and a task-relative path; a missing separator,
an empty owner or an empty path is refused here rather than at the read, because the freeze's own
refusal would name the path it could not read instead of the argument that had no separator in it.
An absolute path or one containing `..` is refused too: the citation is recorded with the
task-relative path its bytes were read from, so a citation that escapes the task root is not one.
`_EVIDENCE_SEPARATOR` (`:92`) is a colon rather than a path separator so an owner can never be read
out of a path by accident, and `_ABSENCE_SIDES` (`:95`) is the two sides a caller may declare an
absence for.

**`report_payload` (`:268-346`) reads every value off the record rather than restating it.** The four
top-level facts are the state, `reused`, the manifest path and the generation directory; a refusal is
reported in the comparison vocabulary's own fields; and the published half of the payload is built
from the manifest's own `generation`, `source`, `scope`, `knowledge`, `records`, `evidence`,
`policies` and `lineage` blocks, each dumped through the model that owns it. That is what keeps the
report from describing a generation the manifest does not. `_print_report` (`:349-394`) prints the
same facts as lines; a refusal prints the freeze's own four fields, and a published record prints the
generation id and index, the seal, the recorded instant, the leaf, the manifest path, the task root,
the temporary storage scope, the scope line, the source line, one line per knowledge side with its
own retained identity, one line per citation, and the predecessor (or `nothing (first generation)`).

### Conventions

`__all__` (`:75-81`) publishes five names: the two exit codes, `add_arguments`, `report_payload` and
`run` — the registration surface `cli/__main__.py` reads plus the two values a caller or a case
addresses directly. The two exits are the ingest CLI's own two, and `EXIT_REFUSED` is deliberately
not an error code for a broken command: it is the code for "the freeze answered, and its answer was
no". Every argument is declared in the adapter (`add_arguments`, `:98-138`) — `--config` and
`--contract` required, `--evidence` and `--historical-absence` repeatable, `--json` switching the
report's shape — and the umbrella contributes only the one registration line, the same declarative
`add_arguments` + `set_defaults(func=...)` pair every other subcommand uses.

### Invariants And Boundaries

- **`--contract` is the write guard, and the task root comes from it.** There is no argument that
  names a task root, a leaf or a repository: all three are read from the enclosure document, so a
  record cannot be aimed at another leaf's line.
- **`--config` is required, and the authority is named rather than inferred.** The freeze resolves a
  canonical candidate and retains knowledge snapshots through the storage owner, and both read the
  coordination root the authority settings declare.
- **The command publishes nothing itself.** Every write is the freeze's, through the retention and
  snapshot owners; this adapter reads a contract, composes a request, names a predecessor and prints
  an outcome.
- **It authors no knowledge or semantic assessment.** Ordinary recording consumes an existing pair. Explicit unchanged-knowledge recording delegates validated pair placement to the existing candidate and original-baseline owners.
- **A refusal is an outcome, not a crash.** The exit code separates published from refused, and the
  refusal's own three fields plus its offending input are what a caller acts on.
- **The predecessor is the highest recorded generation, and a tie is broken by the record's own
  instant.** No directory order, no timestamp of the filesystem, and no reclamation is performed
  here: superseding is recorded as lineage, which is the owner's own resolution for a leaf whose
  comparison changed.
- **PLANNING IS NOT OFFERED.** The command has no `--dry-run`. The reason its own docstring carries is
  that a freeze "either publishes or refuses", so the honest way to ask what it would do is to run it
  and read whether the record was written or reused; a preview would have to describe a generation id
  it had not derived, which this surface must not invent.
- **Carried limitation, measured, not a claim of this card: `reused` is unreachable in the ordinary
  sequence, and the docstring's idempotence sentence is therefore false as wired.** `lineage` sits
  *inside* the seal (`review_comparison_generation._UNSEALED_FIELDS` names only `binding_digest`,
  `generation_id` and `recorded_at`), so naming the standing generation as `parent` changes the
  binding digest and therefore the derived generation id; `_publish` keys reuse on `if final.exists()`
  and that id does not exist, so the write branch runs. Measured by the leaf's adversarial verifier
  read-only, by re-deriving the seal with the pure `assemble_manifest`: the reconstruction reproduces
  the published id and seal byte for byte, and the retry derives the next index (`3`) under a new id
  that is not on disk. Consequence for a reader: every invocation appends a generation with two full
  retained knowledge snapshots, so the no-preview argument above is unsound as stated. The suggested
  remedy belongs to a later leaf and is recorded in *Todos*.

### Todos

- **Carried, for the next leaf on this route (the verifier's F1):** make the retry converge, or stop
  claiming it does. The two shapes named are to name a `parent` only when the derived binding actually
  differs, or to ask the reuse question before the parent-dependent index. Until then the command's
  own docstring states a property the wiring does not have, and every no-op retry costs two retained
  knowledge snapshots.
- **Carried, for the owner rather than the caller:** `freeze_comparison_generation` still permits the
  state it then refuses to read — a caller that names no `parent` for a leaf that already holds a
  readable generation publishes a second generation claiming the same index, which
  `review_comparison_reopen` reports as `ambiguous`. This command supplies the predecessor, so the
  ambiguity does not arise from it; the guard belongs beside `_reuse_or_refuse`, and adding it changes
  the freeze owner's contract rather than this adapter's.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` reads "No
entries configured yet", so it carries no `Domain Documentation` category). The statements below are
grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the two owners
it calls (the freeze and the generation reader), and in the registration that makes it reachable.
Three details a reader should carry: the module adds **no** mechanism — it composes the review
through the surface's own resolution and composition and publishes only what that composition bound;
the predecessor is decided here because it is a *caller-known* fact the freeze cannot infer; and the
no-preview decision rests on an idempotence property the current wiring does not have, recorded above
as a carried limitation rather than as a claim.

- **The module's own statement of why the command exists, why `--contract` is the write guard, why `--config` is required, what it deliberately does not do, and why planning is not offered.** [1]
- The published surface: the two exits, the argument declaration, the report builder and the run. [2]
- **The two exits, and the one that is an outcome rather than an error code.** [3]
- The one evidence separator, chosen so an owner cannot be read out of a path, and the two sides an absence may be declared for. [4]
- **The declared inputs: required authority and contract, repeatable evidence and historical absence, unchanged-knowledge mode, paired explicit recovery identifiers, and report format.** [5]
- **The whole run: the argument-list answer, the predecessor, the request composed from the contract, the one freeze call and the outcome as the exit code.** [6]
- **The predecessor decision: the highest recorded index, the tie broken by the record's own instant, and `None` for a leaf that has published nothing.** [7]
- One generation's own recorded instant, and the empty string that keeps an unreadable record from raising mid-report. [8]
- **The argument-list facts answered before anything is read: the two blank checks, the contract load carrying its owner's typed failure, and the two option fields this command supplies.** [9]
- **A citation that is not a citation: the separator split, the two empty halves, and the absolute-or-`..` path a task-relative citation may not be.** [10]
- **The report built from the record's own fields, with a refusal in the comparison vocabulary's own four and the published half read off the manifest block by block.** [11]
- The same facts as lines, with the predecessor line stating `nothing (first generation)` when none was named. [12]
- **The freeze owner this adapter gives its production caller: resolve and compose exactly as the surface does, then freeze only what that composition bound.** [13]
- **The caller-known facts that travel together, one of which is the predecessor — the field this adapter is the first shipped caller to supply.** [14]
- The outcome value the report and the exit code both read. [15]
- **The lineage a named predecessor produces: the generation id *and* that generation's manifest digest, and the successor's recorded index.** [16]
- **The seal's own omission set, which is why naming a predecessor changes the binding digest and therefore the derived id — the fact behind this card's carried limitation.** [17]
- **The discovery the predecessor decision reads, and the address it answers with.** [18]
- The one manifest file name the recorded instant is read through. [19]
- **The request value composed from the contract's own recorded identities rather than from anything the caller spelled.** [20]
- The contract loader whose typed failure the invocation answer carries, and the contract whose recorded task root the generation is published under. [21]
- The authority loader and its typed failure, so an unreadable settings document is a named refusal rather than a traceback. [22]
- **The registration that makes the command reachable: one of the umbrella's subparsers, and the declarative pair that wires it.** [23]
- The read the recorded refusal and the recorded source range are named by, so this command's record is what the surface reopens. [24]
- **The case that protects the journey this command completes: a baseline placed by a `--baseline` run is opened under the namespace its own record names.** [25]

| `add_arguments` owns the behavior described above. | `add_arguments` | mcp/src/agents_remember/cli/review_comparison_record.py:97-99 |
| `run` owns the behavior described above. | `run` | mcp/src/agents_remember/cli/review_comparison_record.py:146-148 |

The following declarations carry the changed boundary.

- Recovery controls are paired and incompatible live selections refuse. [26]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one leaf's enclosure contract, one
coordination authority's settings document and one leaf's own published generations, and it publishes
under the task root that contract records — none of which is a boundary this adapter crosses on its
own authority.

No meaningful cross-repo references found.
