# mcp/src/agents_remember/models/knowledge_files/history.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**Per-leaf history files: the curator's judgment rows, one file per owner (MIK-R07).**
`knowledge/history/<owner-id>.json` (`ar-history/v1`) belongs to exactly one owner — a `leaf`, a
migration `wave`, or a master-line `crossing` sync — and the owner ID names the file, so two leaves
never write the same file and their history merges without conflict. An invariant's *meaning*
history is the `git log` of its record file; its *judgment* history is the set of rows about it
across all history files. Nothing here is written into a record file, and no judgment row is
produced automatically. The one mechanical writer, MIK-R24's crossing sync (rule 8 step 1), only moves
`No content impact:`/`No route impact:` markers that a curator already wrote into `onboarding_trace`
rows. The module also carries the freeze predicate for closed files and the writer-support
checks that compare a row with facts the caller reads from the base (K_B) and candidate (K_C) trees.

## Code Commentary

### Logic

- `HistoryRow` is the shared row shape: `id` (`ROW-…`, minted), `subject`, `disposition`, a
  nonblank `reason` and unique `items[]` (worklist item IDs, informational only). It cannot be
  validated directly; a concrete kind fixes `subject_pattern` and `dispositions`.
- `InvariantRow` (subject `INV-…`): `changed` | `moved` | `deleted` | `extended` | `no_impact`
  (D28), with `covers[]`, the invariant's K_C `revision` (≥1), `effect` (from the shipped nine
  `EffectLabel`s) and optional, non-empty `because[]` (decision IDs or requirement references).
  `_require_disposition_evidence` refuses a disposition its own covers or effect contradict:
  `changed` needs an effect; only `changed` and `deleted` may carry one, and `deleted` only
  `retire`; `deleted` without `retire` needs a removed entry. The `_COVER_REQUIREMENTS` table holds
  the rest: `moved` needs a re-anchored entry and no added or removed entry; `extended` needs an
  added entry; `no_impact` refuses added or removed entries.
- `CoveredEntry` is `{id: RLZ/PRF, before, after}`; each side is an anchor naming its `path`, or
  `"absent"`, never both absent. `added`, `removed` and `reanchored` derive from the two sides; any
  difference, including a blob-only one, counts as re-anchored.
- `FamilyRow` (subject `FAM-…`): `changed` | `rerouted` | `assigned` | `retired` | `no_impact`,
  with `examined[]` of `{id: INV, revision}` members, unique by ID.
- `OnboardingTraceRow` (kind `onboarding_trace`, MIK-R30/MIK-R53; same file/overview/root subjects):
  `updated` or `no_impact`, with optional `sources[]` of `SourceBlob {path, blob}`. Paths are unique
  repository paths; blobs are hexadecimal IDs or `absent`. `updated` requires sources; the writer
  fills them from C. Sourceless legacy rows keep the field omitted and only answer from their own
  closed winning file, never an open row or a later aggregate closed flag. **MIK-R24
  rule 8 step 1 was the kind's first writer:** when an open leaf's line crosses into the text format, the
  Update History `No content impact:`/`No route impact:` marker lines that leaf added move into its
  history file as these rows. Per the architect's ruling on review round 2 (N1), the moved lines go in
  the structured list field `markers` (`Text` values, at least one entry when present), one entry per
  marker line. A line longer than one text value is split deterministically into consecutive pieces,
  and `reason` becomes a short fixed summary. A real card gained 81 marker lines, 29,351 characters in
  all, which no single `reason` could hold. Registering the kind minimally was accepted at L24; L30
  gave it its initial semantics, and R53 now adds source binding and the `updated` disposition.
- `PlannedEffectRow` (kind `planned`, owner MIK-R11; subject `planned:<declared subject>#<effect>`): the
  authored disposition of a declared effect no row delivered, with dispositions `realized_elsewhere`,
  `deferred` and `dropped` and a `ref` (`PlannedRef`) naming exactly one of `row`, `invariant`,
  `requirement` (a `RequirementReference`), `leaf` or `decision` (the `at` of a task-document decision). The
  ref key must be one the disposition takes (`REFS_BY_DISPOSITION`); the forms come from `planned.py`. See
  the L11 section below.
- `UnexplainedChangeRow` (kind `unexplained`, owner MIK-R10; subject `hunk:<item id>` or
  `file:<path>@<blob>`, the `ROW_SUBJECT_PATTERN` of `unexplained.py`): the `no_invariant` disposition of an
  unexplained change in a covered file, with its `reason`. It is the only disposition and the row adds nothing
  to the common fields. Attach and author need no row of this kind. See the L10 section below.
- `ReconsiderationRow` (kind `reconsideration`, owner MIK-R14; subject `reconsider:<DEC-ID>#<alternative index>`,
  the `RECONSIDER_SUBJECT_PATTERN` of `reconsideration.py`): the curator's answer to a reconsideration candidate,
  `still_rejected` or `raise`, with its `reason` and nothing beyond the common fields. See the L14 section below.
- `MembershipRow` (MIK-R53, `membership:<INV>`): `no_family`, invariant candidate revision and
  unique `considered` family IDs (possibly empty); separate from invariant/family judgment rows.
- `RecordRow` (MIK-R53): decision, incident, assumption, limitation, failure-mode, scenario, diagnostic
  or term ID; candidate revision, `changed`/`retired`/`no_impact`, optional `because`. `changed` needs
  an effect, `retired` needs `retire`, and `no_impact` carries no effect.
- `HISTORY_ROW_KINDS` now has eight kinds: `invariant`, `family`, `onboarding_trace`, `planned`,
  `unexplained`, `reconsideration`, `membership`, `record`. `row_kind_for_subject`/`parse_row` dispatch
  by disjoint subject form and refuse unclaimed subjects; tests compare a set, not landing order.
- `HistoryFile` has `schema`, exactly one of `leaf`/`wave`/`crossing` (a crossing must match
  `<task>-crossing-<n>`), `closed` (strict bool) and `rows[]`, with row IDs and subjects each
  unique, so a file holds at most one row per subject (`row_about`). `closed_copy` and
  `empty_history(..., closed=True)` produce what the closeout writes.
- `is_closed_history` reads only `schema` and `closed` from raw bytes, so a closed file holding a
  row kind registered later is still recognized. `frozen_history_violation(bases, candidate)` is
  true when the file is closed on any base side (K_B or any merge parent) and the candidate bytes
  differ, including deletion and reformatting.
- Writer support: `reanchor_mismatches` (each `after` equals the entry's K_C anchor, `absent`
  means absent), `sidecar_entry_anchors` (fills the sidecar path into entry anchors for that
  comparison), `unknown_subjects` (invariant/family/record IDs and membership's prefixed invariant),
  `invariant_revision_violation` (the K_C revision; `changed` exactly K_B + 1; `moved`, `extended`,
  `no_impact` keep K_B; `deleted` checked only against K_C; new invariants need no invariant row), and
  `stale_examined_members` (a different K_C revision is stale; an absent member is not).
  `winning_row_closed` uses attempt order to retain each winning row's own file closure provenance,
  unlike the latest-file flag carried by `merged_leaf_history`.

### Conventions

- Reuses L21's building blocks (`FileModel`, `Anchor`, `RequirementReference`, `require_unique`,
  `parse_json`, `id_pattern`) and the shipped `EffectLabel`, so the effect vocabulary is unchanged.
- Arrays `rows`, `covers` and `examined` are identified-entry arrays: the canonical formatter sorts
  them by `id`, so file order carries no recency.
- Several spellings were chosen by the L07 worker where the packet was silent: the `ROW-` prefix,
  the `crossing` owner pattern. Stored `items[]` labels remain readable; newly authored tokens are checked at Writer/publication boundaries rather than by replacing the persisted row shape. Closed stored history is not rewritten for that strict-input check.

### Invariants And Boundaries

- **A history file closed in K_B, or in any merge parent, is byte-identical in K_C.** Only the
  predicate lives here; the validator (MIK-R22 rule 7) enforces it and the closeout (MIK-R09, live
  from MIK-R37) sets `closed: true`.
- **A judgment is never stored in a record file.** Records forbid extra fields, so a `no_impact`
  judgment can only live in a history row.
- The models check shape and the helpers check facts the caller supplies; whether a row is current
  for a worklist item is the gate's rule (MIK-R09 rule 2), and the writer is MIK-R12's.
- Historically the installed runtime read/wrote no history files before MIK-R37; this is not a
  current unconverted-write branch. The current writer refuses unconverted memory.
- **A leaf that writes again after its closeout (L37, decision record DEC-0AEQ28).** `HistoryFile.attempt` is optional
  (>= 2, a leaf only; a wave or crossing file with `attempt` is refused), so every existing file keeps its
  bytes; `attempt_number` is 1 without it. A leaf whose latest file a closeout closed (reopened after its integration, or continuing after a closeout that
  was not integrated) keeps that file frozen and writes `<leaf-id>-attempt-<n>.json`. `writable_attempt(closed_by_attempt)` names the attempt a write or a closeout
  goes to: the latest while it is open, the next once it is closed, 1 when there is no file.
  `merged_leaf_history(files)` reads all of an owner's files as one history, in attempt order: a later row about
  a subject supersedes the earlier one, and every other row, a closed file's included, still counts. The merge
  is a reading and is never written back. `empty_history(..., attempt=n)` creates an attempt file.
- **The governing row of a record the leaf changed (L37, INV-XN0FG8).**
  - `invariant_revision_violation(..., restated_revision=None)` accepts a `changed` row at an unchanged revision
    only when the candidate revision, the base revision and `restated_revision` are equal: the row restates the
    leaf's own `changed` row of that revision step in an earlier, frozen attempt. It corrects that step's effect,
    because and reason, and may carry entry work; it is no second change.
  - `keeps_change_visible(row)` is true for `changed`, `deleted` (an invariant) and `retired` (a family).
  - `changed_record_row_violation(row, base_revision, candidate_revision)` returns why a row cannot govern an
    invariant whose revision differs between the parent line and K_C; `changed_family_row_violation(row,
    guarantee_changed)` does the same for a family whose guarantee K_C restates. Both refusal sentences name the
    disposition ("a no_impact row", "an assigned row").

### Todos

D28 names seven dispositions; the family `retired` token follows MIK-R07 rule 5 and the architect's
ruling. Doc14 §4.7 still shows the older illustrative history shape; the architect owns that update.

## 260928-MIK-L30 What An Onboarding Row Means (MIK-R30)

L30 originally gave the no-impact row its semantics; R53 now binds current judgments to covered
source blobs. The writer authors `updated` with a real counted Markdown/reference change, or
`no_impact` when the reviewed contract still holds, and fills `sources` from C. A counted card edit
alone never answers an ordinary candidate item; realization/proof-only edits are not counted.
A source edit after the row reopens the item. Historical rows without sources remain omitted and
frozen: only a row in its own closed winning file retains legacy eligibility; open sourceless rows
answer nothing. Marker transport and root subject `onboarding:overview` retain their earlier forms.

- The row-kind docstring: `updated`/`no_impact`, writer-filled sources and legacy closed/open distinction. [1]
- The gate reads source currency, counted-change requirements and each winning row's own closure provenance. [2]

## 260928-MIK-L11 The Planned Row (MIK-R11 Rule 5)

`PlannedRef` and `PlannedEffectRow` add the fourth registered row kind, `planned`, owned by MIK-R11. A
planned row answers a `planned_untouched` worklist item: its subject is the item's planned key
`planned:<declared subject>#<effect>` (built from the declaration, never from its position), its disposition
is `realized_elsewhere`, `deferred` or `dropped`, and its `ref` names exactly one thing, of the kind its
disposition takes (`_require_exactly_one`, `_require_ref_of_disposition`):

- `realized_elsewhere`: `row` (a `ROW-…`) or `invariant` (an `INV-…`) that delivered the effect;
- `deferred`: `requirement` (the structured `{task, packet, id, version}` reference) or `leaf`;
- `dropped`: `decision`, the `at` of one decision entry in the leaf's task document.

The model checks shape only; whether the ref resolves is the writer's (`authoring._unresolved_ref`), and a
`dropped` decision is resolved by the task owner at write time. The declaration's `requirementRef` is the
string `<ID>@v<n>` while a `deferred` row's `requirement` is structured; both spellings are accepted (review
R1 F5, accepted by ruling 2026-09-29T22:35:34+02:00). The module docstring now names MIK-R30 and MIK-R11 as
the kinds that have landed.

- Historical module-docstring landing outline; the current registry also includes MIK-R53 membership and record kinds. [3]
- The ref: exactly one key. [4]
- The planned row and its disposition-bound ref. [5]
- The current registry test compares all eight kinds as a set, including MIK-R53 membership and record. [6]

## 260928-MIK-L10 The No-Invariant Row (MIK-R10 Rule 3)

`UnexplainedChangeRow` adds the fifth registered row kind, `unexplained`, owned by MIK-R10. A `no_invariant`
row answers an `unexplained_hunk` or `unexplained_file` worklist item **in a covered file**: its subject is the
item's `facts.row`, `hunk:<item id>` for a hunk (the ID names exactly one subject) or the item's own
`file:<path>@<blob>` for a non-text change; its disposition is `no_invariant`, the only one allowed; and its
`reason` (a non-blank `Text`) says why the change carries no invariant. Extra members are refused by the
model. Subjects and the pattern come from `models/knowledge_files/unexplained.py`, so the row, the item and the
gate's predicate share one spelling. The model checks shape only; whether a `file:` subject names the path's
object at C is the writer's (`CodeSnapshot.file_subject_mismatch`), and whether a row answers a raised item is
the worklist's (a stray row is reported as unnecessary, never refused). A `no_invariant` row about an item in
an **uncovered** file satisfies nothing (rule 5; ruling 2026-09-30T03:24:28 N2). The module docstring now names
MIK-R10 among the landed kinds.

- The row's subject pattern and disposition come from the one spelling. [7]
- The no_invariant row: its pattern, its one disposition, its owner. [8]
- Registered fifth. [9]
- The model's refusals: another disposition, a blank reason, `covers`, a malformed subject. [10]

## 260928-MIK-L14 The Reconsideration Row (MIK-R14 Rule 4)

`ReconsiderationRow` adds the sixth registered row kind, `reconsideration`, owned by MIK-R14. It answers a
`reconsideration_candidate` worklist item: its subject is the item's, `reconsider:<DEC-ID>#<alternative index>`
(the pattern comes from `models/knowledge_files/reconsideration.py`, so the row, the item and the gate's predicate
share one spelling); its disposition is `still_rejected` (the rejection holds, and `reason` says why) or `raise`
(the alternative goes to the developer); it carries the common fields only, and extra members are refused by the
model. The model checks shape only: what the subject names, the decision's `under_reconsideration` status, the
task-document question and the link refresh are the writer's (`knowledge_writer/reconsideration.py`,
`authoring._reconsideration_row`). The curator never reverses a decision. The historical module
outline names MIK-R14's `reconsider:…`; the current registry also contains the two R53 kinds.
`test_knowledge_history_files.py` compares the registry as a set because leaves register in landing
order (review F9); subject disjointness remains asserted (review N4, accepted as a note).

- The row's subject pattern and dispositions come from the one spelling. [11]
- The reconsideration row: its kind, pattern and two dispositions. [12]
- Registered sixth, owned by MIK-R14. [13]
- The row kind registered with its owner, and the subject parsed. [14]

## FamilyRow Keeps Effect And Own Revision Optional (MIK-R48)

`FamilyRow` admits a missing effect and a missing own revision on rows that are
already recorded, and keeps them missing when the row is written out again; the
sixteen frozen rows of this master read back with neither key. A new or edited
changed row must carry both facts, and a half-recorded changed row or an effect on
any other disposition is refused naming the family and the row.

- Recorded rows keep missing effect and revision missing on rewrite. [38]

## Evidence

- The docstring names the current registered row kinds; stored items retain Label shape with strict new-token checks assigned to writing/publication. [40]


### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R07@v2` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

No configured live documentation source was available for this pass.

### Repo-Internal References

The file model is registered in `documents.py`; the tests in `test_knowledge_history_files.py` pin
each rule.

- The invariant and family disposition vocabularies. [15]
- The shared row shape and kind dispatch check. [16]
- Covered entries: anchors with a path, or absent on one side. [17]
- What each disposition's covers must show. [18]
- The invariant row. [19]
- The family row and its examined members. [20]
- Many long marker lines move into one valid row. [23]
- The file: one owner, one row per subject. [24]
- The freeze predicate. [25]
- Re-anchoring checked against K_C. [26]

- The revision binding for invariant and family rows. [27]

- The history schema is dispatched by `documents.py`. [28]
- Closed files stay byte-identical, even when reformatted. [29]

- The optional attempt of a reopened leaf's file. [30]
- The attempt a write or closeout goes to. [31]
- All of an owner's history files read as one history. [32]

- A changed row at an unchanged revision is accepted only as a restatement. [33]
- The dispositions that may govern a record its leaf changed. [34]
- Why a row cannot govern an invariant whose revision the leaf changed. [35]
- Why a row cannot govern a family whose guarantee the leaf changed. [36]
- The three rules on their own, for every disposition. [37]

### Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

No cross-repo boundary is crossed by this file.

- The onboarding row: `updated`/`no_impact`, unique source paths, required updated binding and moved markers. [21]
- Eight registered kinds and subject dispatch, including MIK-R53 membership and decision/facet record rows. [22]
- Current source delta inspected statically: Replace stale single-disposition/six-kind model and captions, add source-blob shape, membership/record models and per-winning-file closure provenance, while preserving frozen history, covers and FamilyRow compatibility. [39]
