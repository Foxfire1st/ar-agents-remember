# mcp/src/agents_remember/cli/review_comparison_record.py

| Field                  | Value                                         |
| ---------------------- | --------------------------------------------- |
| repository             | agents-remember                               |
| path                   | `mcp/src/agents_remember/cli/review_comparison_record.py` |
| doc_type               | `file-level-onboarding`                       |
| lastUpdated | 2026-09-27T05:41:59+00:00 |
| lastVerifiedCommitHash | `ee5f14e5405505d126125830e5323f8915c8d047`    |
| lastVerifiedCommitDate | 2026-09-29T07:25:39+02:00|
| governingOverview      | `../../../overview.md`                         |

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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` reads "No
entries configured yet", so it carries no `Domain Documentation` category). The statements below are
grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the two owners
it calls (the freeze and the generation reader), and in the registration that makes it reachable.
Three details a reader should carry: the module adds **no** mechanism — it composes the review
through the surface's own resolution and composition and publishes only what that composition bound;
the predecessor is decided here because it is a *caller-known* fact the freeze cannot infer; and the
no-preview decision rests on an idempotence property the current wiring does not have, recorded above
as a carried limitation rather than as a claim.

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of why the command exists, why `--contract` is the write guard, why `--config` is required, what it deliberately does not do, and why planning is not offered.** | `freeze_review_comparison`; `history:recorded-source-range` | mcp/src/agents_remember/cli/review_comparison_record.py:1-44 |
| The published surface: the two exits, the argument declaration, the report builder and the run. | `__all__` | mcp/src/agents_remember/cli/review_comparison_record.py:82-88 |
| **The two exits, and the one that is an outcome rather than an error code.** | `EXIT_PUBLISHED`; `EXIT_REFUSED` | mcp/src/agents_remember/cli/review_comparison_record.py:94-94; mcp/src/agents_remember/cli/review_comparison_record.py:95-95 |
| The one evidence separator, chosen so an owner cannot be read out of a path, and the two sides an absence may be declared for. | `_EVIDENCE_SEPARATOR`; `_ABSENCE_SIDES` | mcp/src/agents_remember/cli/review_comparison_record.py:99-99; mcp/src/agents_remember/cli/review_comparison_record.py:102-102 |
| **The declared inputs: required authority and contract, repeatable evidence and historical absence, unchanged-knowledge mode, paired explicit recovery identifiers, and report format.** | `add_arguments`; `--config`; `--contract`; `--evidence`; `--historical-absence`; `--json` | mcp/src/agents_remember/cli/review_comparison_record.py:105-159 |
| **The whole run: the argument-list answer, the predecessor, the request composed from the contract, the one freeze call and the outcome as the exit code.** | `run` | mcp/src/agents_remember/cli/review_comparison_record.py:162-202 |
| **The predecessor decision: the highest recorded index, the tie broken by the record's own instant, and `None` for a leaf that has published nothing.** | `_standing_generation` | mcp/src/agents_remember/cli/review_comparison_record.py:205-229 |
| One generation's own recorded instant, and the empty string that keeps an unreadable record from raising mid-report. | `_recorded_at` | mcp/src/agents_remember/cli/review_comparison_record.py:232-242 |
| **The argument-list facts answered before anything is read: the two blank checks, the contract load carrying its owner's typed failure, and the two option fields this command supplies.** | `_invocation` | mcp/src/agents_remember/cli/review_comparison_record.py:245-275 |
| **A citation that is not a citation: the separator split, the two empty halves, and the absolute-or-`..` path a task-relative citation may not be.** | `_evidence_inputs` | mcp/src/agents_remember/cli/review_comparison_record.py:294-318 |
| **The report built from the record's own fields, with a refusal in the comparison vocabulary's own four and the published half read off the manifest block by block.** | `report_payload` | mcp/src/agents_remember/cli/review_comparison_record.py:321-399 |
| The same facts as lines, with the predecessor line stating `nothing (first generation)` when none was named. | `_print_report` | mcp/src/agents_remember/cli/review_comparison_record.py:402-447 |
| **The freeze owner this adapter gives its production caller: resolve and compose exactly as the surface does, then freeze only what that composition bound.** | `freeze_review_comparison`; `freeze_comparison_generation` | mcp/src/agents_remember/application/review_comparison_freeze.py:239-258; mcp/src/agents_remember/application/review_comparison_freeze.py:319-354 |
| **The caller-known facts that travel together, one of which is the predecessor — the field this adapter is the first shipped caller to supply.** | `ComparisonFreezeOptions`; `EMPTY_FREEZE_OPTIONS` | mcp/src/agents_remember/application/review_comparison_freeze.py:152-165; mcp/src/agents_remember/application/review_comparison_freeze.py:169-169 |
| The outcome value the report and the exit code both read. | `ComparisonGenerationFreeze`; `published` | mcp/src/agents_remember/application/review_comparison_freeze.py:194-214 |
| **The lineage a named predecessor produces: the generation id *and* that generation's manifest digest, and the successor's recorded index.** | `_lineage`; `ComparisonPublicationLineage` | mcp/src/agents_remember/application/review_comparison_freeze.py:728-737; mcp/src/agents_remember/application/review_comparison_generation.py:380-402 |
| **The seal's own omission set, which is why naming a predecessor changes the binding digest and therefore the derived id — the fact behind this card's carried limitation.** | `_UNSEALED_FIELDS` | mcp/src/agents_remember/application/review_comparison_generation.py:162-162 |
| **The discovery the predecessor decision reads, and the address it answers with.** | `read_generation_refs`; `ComparisonGenerationRef` | mcp/src/agents_remember/application/review_comparison_generation.py:714-722; mcp/src/agents_remember/application/review_comparison_generation.py:725-753 |
| The one manifest file name the recorded instant is read through. | `COMPARISON_MANIFEST_NAME` | mcp/src/agents_remember/application/review_comparison_generation.py:133-133 |
| **The request value composed from the contract's own recorded identities rather than from anything the caller spelled.** | `ReviewSurfaceRequest` | mcp/src/agents_remember/models/knowledge/review.py:262-324 |
| The contract loader whose typed failure the invocation answer carries, and the contract whose recorded task root the generation is published under. | `load_contract`; `WorktreeContract` | mcp/src/agents_remember/worktrees/worktree_contract.py:233-286; mcp/src/agents_remember/worktrees/worktree_contract.py:437-467 |
| The authority loader and its typed failure, so an unreadable settings document is a named refusal rather than a traceback. | `load_config`; `ConfigError` | mcp/src/agents_remember/kernel/primitives/runtime_config.py:159-167; mcp/src/agents_remember/kernel/primitives/runtime_config.py:76-77 |
| **The registration that makes the command reachable: one of the umbrella's subparsers, and the declarative pair that wires it.** | `review_comparison_record`; "review-record-comparison" | mcp/src/agents_remember/cli/__main__.py:76-84 |
| The read the recorded refusal and the recorded source range are named by, so this command's record is what the surface reopens. | `HISTORY_RECORDED_COMPARISON`; `HISTORY_RECORDED_SOURCE_RANGE` | mcp/src/agents_remember/application/review_committed_leaf.py:77-78 |
| **The case that protects the journey this command completes: a baseline placed by a `--baseline` run is opened under the namespace its own record names.** | `test_the_placed_baseline_is_opened_under_its_own_recorded_namespace` | mcp/tests/test_knowledge_ingest_comparison_generation.py:329-370 |

| `add_arguments` owns the behavior described above. | `add_arguments` | mcp/src/agents_remember/cli/review_comparison_record.py:97-99 |
| `run` owns the behavior described above. | `run` | mcp/src/agents_remember/cli/review_comparison_record.py:146-148 |

The following declarations carry the changed boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| Recovery controls are paired and incompatible live selections refuse. | `_recovery_arguments` | mcp/src/agents_remember/cli/review_comparison_record.py:278-291 |

## Cross-Repo References

No cross-repository behavior is implemented in this file. It reads one leaf's enclosure contract, one
coordination authority's settings document and one leaf's own published generations, and it publishes
under the task root that contract records — none of which is a boundary this adapter crosses on its
own authority.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-29T07:08:34+02:00 — 260928-MIK-L22 curator (uncommitted change set on `ar/260928-mik-l22`, code base `4aa9a98cebb65d7bfb492d80a420e794a3fb9f8c` plus the working-tree delta): No content impact: citation-only re-measure. This card cites `cli/__main__.py`, where the `knowledge-validate` subparser insertion moved the `review-record-comparison` registration down six lines. Ranges were re-pointed by the installed `memory-citations --fix` or, for multi-anchor rows it declined, by the exact line shift, and a per-document check then reported 0 findings. The claims were re-read and are unchanged. No verification stamp was advanced.
- 2026-09-29T04:55:39+02:00 — 260928-MIK-L21 curator (uncommitted change set on `ar/260928-mik-l21`, code base `b7ef73f8efadc46b3a9bf5706b2cf61757aa63b4` plus the working-tree delta): No content impact: the registration row re-pointed to `cli/__main__.py:69-77` after MIK-R21 registered `knowledge-format`, and its finding no longer calls this the sixth subparser (the umbrella now has seven). Claim meaning unchanged; no stamp advanced.

- 2026-09-27T05:41:59+00:00 — Retained the CLI argument claim with its current unchanged-knowledge and explicit recovery inputs. Verification remains closeout-owned.

- 2026-09-27T05:31:41+00:00 — Selected the actual value/model declarations for 1 ambiguous source-linked citation(s), including container members and delegated type owners where applicable. The bounded claim is retained; generated history and real stamps remain unchanged.

- 2026-09-27T05:23:46+00:00 — Re-resolved 10 source-linked citation claim(s) against the extracted or shifted L41 owners. Each selected symbol uses its current declaration extent; other source references and prior generated history remain unchanged. Verification stamps remain closeout-owned.

- 2026-09-27T04:56:35+00:00 — Documented the explicit paired recovery controls, their refusal boundary and reuse of the existing producer/retention owners. Verification hashes/dates remain closeout-owned.
- 2026-09-26T21:15:59+00:00: Generated citation repair: `__all__` repointed to mcp/src/agents_remember/cli/review_comparison_record.py:74-80. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:15:59+00:00: Generated citation repair: `EXIT_PUBLISHED`; `EXIT_REFUSED` repointed to mcp/src/agents_remember/cli/review_comparison_record.py:86-86; mcp/src/agents_remember/cli/review_comparison_record.py:87-87. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:15:59+00:00: Generated citation repair: `_EVIDENCE_SEPARATOR`; `_ABSENCE_SIDES` repointed to mcp/src/agents_remember/cli/review_comparison_record.py:91-91; mcp/src/agents_remember/cli/review_comparison_record.py:94-94. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:15:59+00:00: Generated citation repair: `add_arguments` repointed to mcp/src/agents_remember/cli/review_comparison_record.py:97-143. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T21:15:59+00:00: Generated citation repair: `HISTORY_RECORDED_COMPARISON`; `HISTORY_RECORDED_SOURCE_RANGE` repointed to mcp/src/agents_remember/application/review_committed_leaf.py:77-77; mcp/src/agents_remember/application/review_committed_leaf.py:78-78. No content impact: mechanical anchor-range projection bound to citation source snapshot 4327ec15f102de46c16cef13f4d57a4013cc8f0e3ca10b9ae02b4b2b706c162e; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-26T20:57:44Z — Reconciled current source-owner citations and exact declarations; superseded wording is corrected in the affected reference rows.
- 2026-09-26T19:49:05Z — Reconciled the changed ownership and current behavior with the source.

- 2026-09-25T22:00:00+02:00 — 260921-ICR-L34 curator (leaf `260921-ICR-L34`, uncommitted change set on `ar/260921-icr-l34-ar`, code base `a9a1a41bba535803421470bd17d858657177cb5f` plus the working-tree delta): **created this one-to-one card for the module this leaf introduces as the Intent Reviewer's comparison producer.** It records what the command is *for* (the freeze owner was complete and measured but had no caller outside the test suite, so no leaf could ever publish a generation and the reviewer's knowledge column stayed empty), the write-guard role of `--contract`, why `--config` is required, the four facts the run is wide, the predecessor decision and the tie-break rule behind it, the citation checks, the report built from the record's own fields, and the two limits it deliberately does not cross (it authors no knowledge, places no dataset and establishes no before half; and it offers no preview). **One carried limitation is recorded as measured rather than as a claim:** the docstring's idempotence sentence is false as wired, because `lineage` sits inside the seal, so naming a predecessor changes the derived id and an ordinary retry appends a successor instead of reusing the record — the leaf's adversarial verifier proved it read-only by re-deriving the seal with the pure `assemble_manifest`, self-checked against the published id and seal. **Stamp accounting:** `lastVerifiedCommitHash`/`lastVerifiedCommitDate` name the **production line this reading was against** — `a9a1a41bba535803421470bd17d858657177cb5f`, this leaf's recorded base and the current tip of `ar/260921_complete-code-and-intent-review` — because every construct cited here exists only in this leaf's uncommitted working tree: no commit contains the module, so no commit contains the bytes a stamp would claim to have verified, and the governed closeout owns the real stamp once its code commit exists.
