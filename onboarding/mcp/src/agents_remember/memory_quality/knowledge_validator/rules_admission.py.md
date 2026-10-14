# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_admission.py

## Governing Overview

[memory_quality route overview](../overview.md)

## Purpose

**MIK-R27's admission rule in the validator's one registry (MIK-R22 rule 9).** Every invariant, family
and decision record states which admission criterion it meets, with a one-sentence justification
(the shape is MIK-R21 rule 4, in `models/knowledge_files/shapes.py`). New-record admission refuses unsupported criteria or non-prose justification. Unsupported criteria on
existing/exported live records also refuse commit/landing publication: only sync/standalone conversion
reports under `merge_reports`, with writer-only reporting for repair. This is not a permanent
admission-maintenance exemption.
Importing the module registers the three admission rules and the refusing record-kept comparison rule; `validator.py` imports it next to the other rule modules,
so every place the validator runs (the writer, `validate_tree`, `require_valid_commit`, the managed
sync, `knowledge-validate`) runs them.

| Rule | Status | What it does |
| --- | --- | --- |
| `R27.2-new-record` | refusing | refuses a new record that fails admission, naming the record and the criterion |
| `R27.2-existing-record` | `merge_reports`, writer-reported | unsupported existing criteria refuse commit/landing; report at sync/standalone conversion and in the writer for repair |
| `R27.4-legacy-unassessed` | `migration_debt` | aggregate carried live debt while migration is incomplete; new debt and migration-complete carried debt refuse per record outside standalone conversion |
| `R27.4-record-kept` | refusing | every ID held by a comparison base remains in the candidate; leave use with `status: retired`, never deletion |

## Code Commentary

### Logic

- **Which records are new.** `_admitted_records` walks the parsed invariant, family and decision
  records. A record is new when its ID is absent from every comparison base (`_base_record_ids`: K_B
  at a commit route, each parent at a merge, read from the bases' record filenames) **and** it is not
  an export. With no base (a curator's standalone run without `--base`), every record that is not an
  export is new.
- **What an export is** (review R1 finding F2, ruling 23:04:57). `_exported(record)` is true only when
  `derived_record_id(kind, origin.legacyId)` equals the record's ID: the conversion's own derivation
  from `models/knowledge_files/ids.py`, not a copy of it. A hand-written `legacyId` that does not derive
  the ID does not make a record exported, so such a record is judged for admission like any new one.
- **A decision is never an export** (L13 review F6, ruling 02:05:07). `_exported` returns `False` for any
  `DecisionRecord` before it looks at `legacyId`: the conversion exports no decisions (MIK-R24), so a
  `legacyId` on a decision exempts it from nothing, even one chosen so that
  `derived_record_id("decision", legacyId)` equals the decision's ID. A new decision marked `legacy-unassessed`
  is therefore refused by `R27.2-new-record` like any other new record.
- **Retired records are exempt** from both admission rules (`_retired`; decisions cannot be retired).
- **Refused on a new record** (`check_new_record_admission`):
  - `legacy-unassessed`, which only the export writes (field `admission`);
  - a justification that `_only_references` finds to be only references (field
    `admission.justification`);
  - a claimed `spans_locations` or `guarded_by_test` that the tree's sidecar entries do not support
    (field `admission.criteria`, from `_unsupported`).
  - A record with no criterion never parses (MIK-R21: `criteria` has at least one item), so the shape
    rule `R22.1-shape` refuses it, naming `admission.criteria`; this module never sees it.
- **The two checkable criteria** (ruling 22:11:24 Q1). "Supported by the index" is checked against the
  sidecar `realizes` and `proves` entries the derived index (MIK-R23) is built from, read from the tree
  the validator already parsed, because `memory_quality` ranks below `memory/knowledge_index` in
  `layers.toml`. `_entry_facts` collects, per invariant, the files its realization entries sit in and
  whether any proof entry names it:
  - `spans_locations` holds when the realizations sit in two or more distinct files (proofs do not
    count);
  - `guarded_by_test` holds when at least one `proves` entry names the invariant (MIK-R28).
- **The reference-only detector** (`_only_references`) is a word list, not a judgment. Tokens are
  split on whitespace, most punctuation, `/`, apostrophes and curly quotes; surrounding dots, dashes,
  `*` and `_` are stripped; a master code directly before a leaf or requirement ID ("ICR L45") is
  joined into one reference first (`_MASTER_PREFIXED`). Each token must be filler (`_FILLER`), a bare
  number, or a reference (`_REFERENCE`), and at least one reference must be present:
  - **references:** task and leaf IDs, requirement IDs with dotted sub-rules (`R27.2`), bare leaf IDs,
    step IDs (`S2`), section signs, task directories, developer-ruling IDs (`D14`), commit hashes (7 to
    40 hex characters, at least one a digit, so a hex-only word such as "defaced" stays a word) and ISO
    dates or instants;
  - **filler:** connectives and the provenance words a note is made of ("added", "introduced",
    "implements", "per", "ruling", "developer", "commit", "decision", "acceptance", "criteria",
    "section", "fixes" and similar).
  - D-IDs and commit hashes are references by ruling 22:11:24 Q2; the provenance words, the
    tokenizing, dotted sub-rules, master-prefixed IDs, step IDs and dates came in by ruling 23:04:57
    F1. Any other word in the justification admits it, so "Per D14 at 4e1c9a7f2b: a landing that pairs
    the wrong commits corrupts the ledger." is admitted.
- **Existing-record criteria (`check_existing_record_admission`).** The same `_unsupported` failure
  refuses at commit/landing, reports at sync/standalone conversion via `merge_reports`, and is
  writer-reported for repair. The message names the criterion to reassess or demote; the source
  docstring's old unrelated-commit exemption is not the executable route contract.
- **Live unassessed debt (`check_legacy_unassessed`).** `_base_live_unassessed_ids` compares actual
  live `legacy-unassessed` findings in parsed bases, not just record-ID presence. Assessed-to-unassessed
  and retired-to-live-unassessed changes are new debt. Base-carried debt aggregates by kind while
  migration is incomplete (no census routes is not completion); new debt refuses immediately, and
  once every onboarding route is migrated or excluded carried debt also refuses per record.
  Standalone conversion reports the debt it authors rather than accepting later publication.

### Conventions

- Only `R27.2-existing-record` sets `writer_reports=True`; the writer reports that criterion failure
  for repair instead of refusing there. New admission, record retention and refusing migration debt
  are not waived by that writer setting. Later commit/landing still refuse unsupported existing criteria.
- Messages name the record ("new invariant INV-…") and the criterion; the refusal text asks for the
  reason "in words".
- Curly quotes and dashes are written as escapes in the source, because ruff's RUF001 flags the
  literal characters.

### Invariants And Boundaries

- **A new record is refused unless it carries a supported admission criterion with a justification
  stated in words.** Realized by `check_new_record_admission`, `_only_references` and `_unsupported`;
  proved by `test_a_new_record_whose_justification_is_only_a_reference_is_refused`,
  `test_a_new_record_without_a_criterion_or_marked_legacy_unassessed_is_refused` and
  `test_an_unsupported_checkable_criterion_on_a_new_record_is_refused_naming_it`.
- **Unsupported criteria on existing/exported live records refuse off merge.**
  `R27.2-existing-record` carries `merge_reports` and `writer_reports`; the static cases
  `test_an_existing_record_whose_test_was_deleted_refuses_off_merge` and
  `test_exported_retired_and_merged_records_refuse_off_merge` distinguish single-base refusal,
  sync reporting and retired exemption. Record-kept independently refuses deletion.
- **A record counts as exported only when its ID is the one the converter derives from its
  `legacyId`.** Realized by `_exported`; proved by `test_a_forged_legacy_id_does_not_make_a_record_exported`.
- **A decision is never treated as an export for admission.** Realized by the `DecisionRecord` guard in
  `_exported`; proved by `test_a_decision_is_never_an_export_so_a_legacy_id_exempts_it_from_nothing`
  (`test_knowledge_decisions.py`), which fails with the guard removed, and by the L13 reviewer's hand-forged
  decision on a converted clone (refused by the L13 build, not by the base build).
- **Retired records are exempt.** Realized by `_retired`; statically asserted by the retired block of
  `test_exported_retired_and_merged_records_refuse_off_merge`.
- **Converted applicability is not an export exemption.** The validator runs over converted
  candidate/comparison trees. Standalone conversion reports authored migration debt; ordinary
  commit/landing refuses new debt and unsupported existing criteria, including exported records.
  Historical worker/reviewer runs over 108 exported records with zero R27 refusals and byte-identical
  unconverted quality output describe the earlier L27 state, not a current pre-conversion permission
  or fresh execution. MIK-R46 ordinary operations now refuse unconverted memory.
- The module judges no meaning (Exclusions, Doc13): whether a justification is plausible, and whether
  `family_guarantee`, `prevents_costly_mistake`, `joint_guarantee`, `real_alternatives` or
  `constrains_future_work` hold, is the reviewer's judgment (OM-4, entered by requirement, ruling
  22:11:24 Q3).
- A statement that meets no criterion is not a record: it stays prose under "Boundaries" in the
  onboarding Markdown (packet rule 3). Demotion retires the record with a `deleted` row (effect
  `retire`) and never deletes its file (rule 4).

### Todos

- **L09 (ruling 22:11:24 Q6, carried).** Inside the writer the base is the memory worktree's `HEAD`,
  so a record committed earlier in the same leaf is "existing" there. Closeout and landing must
  validate admission against the parent line, so that a record first committed inside the leaf
  counts as new.
- **The R19 follow-up master (ruling 22:11:24 Q5; ruling 23:04:57 F2's remainder).** Whether demotion
  also removes a retired record's realization entries, recording the outcomes in the census (MIK-R20),
  and re-validation of exported records' assessments remain R19 concerns. The old report-only
  admission premise is superseded: unsupported criteria now refuse the next publication/landing.
- **Historical L06 sync (ruling 22:11:24 Q4, review F6): resolved at that time.** L06 landed second. Its new cases pin no exact
  findings list over the Doc14 fixture tree: the carried-route case asserts `validate_tree(...).ok` and
  filters the reports by rule (`R04.1-carried-route-absent`), so the `R27.4-legacy-unassessed` count needed
  no pin change, and L06's worker reran the validator, family-route and route-condition suites green on the
  synced tree.

## Evidence

- Records present in a comparison base are retained; retirement never deletes the file. [21]


### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The admission rule's design authority is the requirement packet
`MIK-R27@v1` of task `260928_maintained-invariant-knowledge`, developer ruling D14 and the
coordination-root note Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`,
section 6 for the derived IDs); they live outside the code and memory repositories, so they are named
here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The detector, novelty, the entry facts, the three rules and their proofs.

- The reference forms the detector recognises, D-IDs, commit hashes and ISO dates included. [1]
- A master code before a leaf or requirement ID is joined into one reference; the provenance filler words. [2]
- A justification is reference-only when every token is filler, a number or a reference, and one is a reference. [3]
- The base record IDs come from the bases' record filenames. [4]
- A record is new when no base holds its ID and it is not an export. [5]
- An export is a record whose legacy ID derives its ID; retired records are exempt. [6]
- The checkable facts come from the tree's sidecar realization and proof entries. [7]
- An unsupported spans_locations or guarded_by_test claim. [8]
- A new record is refused for legacy-unassessed, a reference-only justification or an unsupported claim. [9]


- The derivation the conversion writes and the export test reuses. [13]
- Reference-only justifications are refused, and real prose is admitted. [14]
- An unsupported checkable criterion on a new record is refused, naming it. [15]
- A forged legacy ID does not make a record exported. [17]
- The writer refuses a new invariant whose claim the tree does not support, and writes nothing. [18]

- A decision is never an export, so a legacy ID exempts it from nothing (L13 review F6). [19]

- A decision whose legacy ID derives its own ID, marked legacy-unassessed, is refused as new. [20]

### Cross-Repo References

No meaningful cross-repo references found: the rules read the validation context's memory trees only.

No cross-repo boundary is crossed by this file.

- Existing unsupported criteria refuse commit/landing and report at sync/standalone conversion or writer repair. [10]
- Actual base-carried live legacy debt aggregates while migration is incomplete; new or completion-time debt refuses per record. [11]
- Admission rules register named merge_reports/migration_debt reasons and the independent record-kept refusal; no permanent maintenance waiver. [12]
- The existing-record test-deletion case asserts single-base refusal and sync-merge reporting. [16]
- Current source delta inspected statically: Repair admission status table, logic, writer flags, boundaries/TODO and captions; preserve retirement and dated historical evidence. [22]
