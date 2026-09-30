# mcp/src/agents_remember/models/knowledge_files/history.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge_files/history.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:13:48+02:00 |
| lastVerifiedCommitHash | `f9e1262283469df895c98dda5b9549a1bbad5b74`|
| lastVerifiedCommitDate | 2026-09-30T13:14:52+02:00|
| governingOverview | `../overview.md` |

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
- `OnboardingTraceRow` (kind `onboarding_trace`, owner MIK-R30; subject `onboarding:<source path>` for a
  file card, `onboarding:<route>/overview` for a route overview, `onboarding:overview` for the root):
  a reviewed-no-impact attestation about one card, with the single disposition `no_impact`. **MIK-R24
  rule 8 step 1 is its first writer:** when an open leaf's line crosses into the text format, the
  Update History `No content impact:`/`No route impact:` marker lines that leaf added move into its
  history file as these rows. Per the architect's ruling on review round 2 (N1), the moved lines go in
  the structured list field `markers` (`Text` values, at least one entry when present), one entry per
  marker line. A line longer than one text value is split deterministically into consecutive pieces,
  and `reason` becomes a short fixed summary. A real card gained 81 marker lines, 29,351 characters in
  all, which no single `reason` could hold. Registering the kind minimally was accepted at L24; MIK-R30
  (L30) then gave it its semantics without changing the model (see the L30 section below).
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
- `HISTORY_ROW_KINDS` is the row-kind registry, now holding `invariant`, `family`, `onboarding_trace`,
  `planned`, `unexplained` and `reconsideration`; `row_kind_for_subject` and `parse_row` dispatch a row to the one
  kind whose subject form it has, and refuse a subject no kind claims. MIK-R06 adds its kind later; MIK-R30 owns
  `onboarding_trace`'s semantics, MIK-R11 owns `planned`, MIK-R10 owns `unexplained` and MIK-R14 owns
  `reconsideration`. Leaves register in landing order, so the tests compare the registry as a set.
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
  comparison), `unknown_subjects`, `invariant_revision_violation` (the row's revision is the K_C
  revision; `changed` is exactly K_B + 1; `moved`, `extended` and `no_impact` keep the K_B revision;
  `deleted` is checked only against K_C; an invariant absent from K_B needs no row) and
  `stale_examined_members` (a member whose K_C revision differs is stale; one absent from K_C is
  not).

### Conventions

- Reuses L21's building blocks (`FileModel`, `Anchor`, `RequirementReference`, `require_unique`,
  `parse_json`, `id_pattern`) and the shipped `EffectLabel`, so the effect vocabulary is unchanged.
- Arrays `rows`, `covers` and `examined` are identified-entry arrays: the canonical formatter sorts
  them by `id`, so file order carries no recency.
- Several spellings were chosen by the L07 worker where the packet was silent: the `ROW-` prefix,
  the `crossing` owner pattern, and `items[]` accepting any exact token until MIK-R08 fixes item
  IDs.

### Invariants And Boundaries

- **A history file closed in K_B, or in any merge parent, is byte-identical in K_C.** Only the
  predicate lives here; the validator (MIK-R22 rule 7) enforces it and the closeout (MIK-R09, live
  from MIK-R37) sets `closed: true`.
- **A judgment is never stored in a record file.** Records forbid extra fields, so a `no_impact`
  judgment can only live in a history row.
- The models check shape and the helpers check facts the caller supplies; whether a row is current
  for a worklist item is the gate's rule (MIK-R09 rule 2), and the writer is MIK-R12's.
- Nothing in the installed runtime reads or writes history files before MIK-R37.

### Todos

D28 names seven dispositions; the family `retired` token follows MIK-R07 rule 5 and the architect's
ruling. Doc14 §4.7 still shows the older illustrative history shape; the architect owns that update.

## 260928-MIK-L30 What An Onboarding Row Means (MIK-R30)

L30 changes only the `OnboardingTraceRow` docstring; the model is L24's, unchanged. The docstring now states
MIK-R30's semantics: on a converted tree, a row with disposition `no_impact` satisfies the onboarding gate's
item for a changed source file's card or governing route overview that has no counted change
(`worktrees/modules/onboarding_trace.py`); `no_impact` is the only disposition; the curator writes it through
the writer's `history` section (`authoring._onboarding_row`), and MIK-R24 rule 8 step 1 also writes it by
moving an open leaf's markers. The root route's subject is `onboarding:overview` (architect ruling
2026-09-29T18:49:50 (3)).

| Finding | Anchor | Source |
| --- | --- | --- |
| The row kind's docstring, with MIK-R30's semantics and the root subject. | `OnboardingTraceRow`; "satisfies the onboarding gate's item" | mcp/src/agents_remember/models/knowledge_files/history.py:261-283 |
| The gate that reads these rows. | `_history_rows` | mcp/src/agents_remember/worktrees/modules/onboarding_trace.py:339-361 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The docstring's list of landed row kinds (since MIK-R14 it names MIK-R10's and MIK-R14's, with MIK-R06 still to come). | "MIK-R06 later" | mcp/src/agents_remember/models/knowledge_files/history.py:26-28 |
| The ref: exactly one key. | `PlannedRef`; `_require_exactly_one` | mcp/src/agents_remember/models/knowledge_files/history.py:286-312 |
| The planned row and its disposition-bound ref. | `PlannedEffectRow`; `_require_ref_of_disposition` | mcp/src/agents_remember/models/knowledge_files/history.py:315-338 |
| The registry test, since MIK-R14 six kinds compared as a set. | `test_row_kind_registry_owns_disjoint_subject_forms` | mcp/tests/test_knowledge_history_files.py:168-193 |

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

| Finding | Anchor | Source |
| --- | --- | --- |
| The row's subject pattern and disposition come from the one spelling. | "from agents_remember.models.knowledge_files.unexplained import" | mcp/src/agents_remember/models/knowledge_files/history.py:80-80 |
| The no_invariant row: its pattern, its one disposition, its owner. | `UnexplainedChangeRow` | mcp/src/agents_remember/models/knowledge_files/history.py:341-353 |
| Registered fifth. | "HistoryRowKind(\"unexplained\", UnexplainedChangeRow, \"MIK-R10\")" | mcp/src/agents_remember/models/knowledge_files/history.py:387-387 |
| The model's refusals: another disposition, a blank reason, `covers`, a malformed subject. | `test_the_kinds_are_registered_and_no_invariant_is_the_only_row_disposition` | mcp/tests/test_unexplained_change_disposition.py:161-181 |

## 260928-MIK-L14 The Reconsideration Row (MIK-R14 Rule 4)

`ReconsiderationRow` adds the sixth registered row kind, `reconsideration`, owned by MIK-R14. It answers a
`reconsideration_candidate` worklist item: its subject is the item's, `reconsider:<DEC-ID>#<alternative index>`
(the pattern comes from `models/knowledge_files/reconsideration.py`, so the row, the item and the gate's predicate
share one spelling); its disposition is `still_rejected` (the rejection holds, and `reason` says why) or `raise`
(the alternative goes to the developer); it carries the common fields only, and extra members are refused by the
model. The model checks shape only: what the subject names, the decision's `under_reconsideration` status, the
task-document question and the link refresh are the writer's (`knowledge_writer/reconsideration.py`,
`authoring._reconsideration_row`). The curator never reverses a decision. The module docstring now names
MIK-R14's `reconsider:…` among the landed kinds, with MIK-R06 still to come. The registry is compared as a set in
`test_knowledge_history_files.py`, because leaves register in landing order (review F9); the duplicate-name check
that the ordered list gave is gone, while subject disjointness is still asserted (review N4, accepted as a note).

| Finding | Anchor | Source |
| --- | --- | --- |
| The row's subject pattern and dispositions come from the one spelling. | "from agents_remember.models.knowledge_files.reconsideration import" | mcp/src/agents_remember/models/knowledge_files/history.py:65-68 |
| The reconsideration row: its kind, pattern and two dispositions. | `ReconsiderationRow` | mcp/src/agents_remember/models/knowledge_files/history.py:356-368 |
| Registered sixth, owned by MIK-R14. | "HistoryRowKind(\"reconsideration\", ReconsiderationRow, \"MIK-R14\")" | mcp/src/agents_remember/models/knowledge_files/history.py:388-388 |
| The row kind registered with its owner, and the subject parsed. | `test_the_row_kind_and_the_item_kind_are_registered` | mcp/tests/test_reconsideration_surfacing.py:604-611 |

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The format's design authority is the coordination-root note
Doc14 (`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`) and the
requirement packet `MIK-R07@v2` of task `260928_maintained-invariant-knowledge`; both live outside
the code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

The file model is registered in `documents.py`; the tests in `test_knowledge_history_files.py` pin
each rule.

| Finding | Anchor | Source |
| --- | --- | --- |
| The invariant and family disposition vocabularies. | `INVARIANT_DISPOSITIONS`; `FAMILY_DISPOSITIONS` | mcp/src/agents_remember/models/knowledge_files/history.py:85-86 |
| The shared row shape and kind dispatch check. | `HistoryRow` | mcp/src/agents_remember/models/knowledge_files/history.py:105-130 |
| Covered entries: anchors with a path, or absent on one side. | `CoveredEntry` | mcp/src/agents_remember/models/knowledge_files/history.py:133-164 |
| What each disposition's covers must show. | `_COVER_REQUIREMENTS`; `_require_disposition_evidence` | mcp/src/agents_remember/models/knowledge_files/history.py:176-198; mcp/src/agents_remember/models/knowledge_files/history.py:201-217 |
| The invariant row. | `InvariantRow` | mcp/src/agents_remember/models/knowledge_files/history.py:220-236 |
| The family row and its examined members. | `ExaminedMember`; `FamilyRow` | mcp/src/agents_remember/models/knowledge_files/history.py:239-243; mcp/src/agents_remember/models/knowledge_files/history.py:246-258 |
| The onboarding-trace row: one disposition, and the moved marker lines as a structured list. | `OnboardingTraceRow` | mcp/src/agents_remember/models/knowledge_files/history.py:261-283 |
| The row-kind registry, now with six kinds (MIK-R11 adds `planned`, MIK-R10 `unexplained`, MIK-R14 `reconsideration`), and dispatch. | "HISTORY_ROW_KINDS: Final["; `row_kind_for_subject` | mcp/src/agents_remember/models/knowledge_files/history.py:382-389; mcp/src/agents_remember/models/knowledge_files/history.py:392-398 |
| Many long marker lines move into one valid row. | `test_many_long_markers_move_into_one_valid_history_row` | mcp/tests/test_knowledge_crossing.py:217-243 |
| The file: one owner, one row per subject. | `HistoryFile` | mcp/src/agents_remember/models/knowledge_files/history.py:418-462 |
| The freeze predicate. | `is_closed_history`; `frozen_history_violation` | mcp/src/agents_remember/models/knowledge_files/history.py:476-495; mcp/src/agents_remember/models/knowledge_files/history.py:498-506 |
| Re-anchoring checked against K_C. | `reanchor_mismatches`; `sidecar_entry_anchors` | mcp/src/agents_remember/models/knowledge_files/history.py:514-526; mcp/src/agents_remember/models/knowledge_files/history.py:529-534 |
| The revision binding for invariant and family rows. | `invariant_revision_violation`; `stale_examined_members` | mcp/src/agents_remember/models/knowledge_files/history.py:547-567; mcp/src/agents_remember/models/knowledge_files/history.py:570-581 |
| The history schema is dispatched by `documents.py`. | `HISTORY_SCHEMA` | mcp/src/agents_remember/models/knowledge_files/documents.py:64-71 |
| Closed files stay byte-identical, even when reformatted. | `test_closed_in_base_implies_byte_identical_in_candidate` | mcp/tests/test_knowledge_history_files.py:332-360 |

## Cross-Repo References

No meaningful cross-repo references found: the module reads and writes only files of the memory
repository layout it declares, and calls no sibling repository or external service.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History
- 2026-09-30T12:13:48+02:00 — 260928-MIK-L14 curator (uncommitted change set on `ar/260928-mik-l14`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c` plus the staged delta): **body updated for MIK-R14.** A Logic bullet for `ReconsiderationRow`; the registry bullet names six kinds and the set comparison; a new section "260928-MIK-L14 The Reconsideration Row (MIK-R14 Rule 4)" with four rows (review F9, N4). **Reopened claim re-read and reworded:** the docstring row's anchor "MIK-R06 and R14" is gone from the code (the list now names MIK-R14 and leaves MIK-R06 for later). The committed L10 entry names that anchor, so the row is re-anchored on "MIK-R06 later" (`26-28`) instead of editing committed history. The registry row and the L11 registry-test row are reworded for six kinds; their anchors are unchanged. The four rows the fixer declined (`row_kind_for_subject`, `frozen_history_violation`, `sidecar_entry_anchors`, `stale_examined_members`) were re-pointed by the exact line shift of this leaf's diff (the new row class and imports sit above them). The fixer's generated bullets are kept: none of their claims was reworded. No verification stamp was advanced.
- 2026-09-30T10:07:07+00:00: Generated citation repair: "from agents_remember.models.knowledge_files.unexplained import" repointed to mcp/src/agents_remember/models/knowledge_files/history.py:80-80. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:07:07+00:00: Generated citation repair: "HistoryRowKind(\"unexplained\", UnexplainedChangeRow, \"MIK-R10\")" repointed to mcp/src/agents_remember/models/knowledge_files/history.py:387-387. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T10:07:07+00:00: Generated citation repair: `INVARIANT_DISPOSITIONS`; `FAMILY_DISPOSITIONS` repointed to mcp/src/agents_remember/models/knowledge_files/history.py:85-85; mcp/src/agents_remember/models/knowledge_files/history.py:86-86. No content impact: mechanical anchor-range projection bound to citation source snapshot fa7748792a962532da9358f73baa3b69634d367f6d9f44b01836b65362dd93a4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-30T04:44:12+02:00 — 260928-MIK-L10 curator (uncommitted change set on `ar/260928-mik-l10`, code base `8a2d4b478971bf40cca0f24d5e5d24a0844bd563` plus the staged delta): **body updated for MIK-R10.** Added a Logic bullet for `UnexplainedChangeRow` and the section "260928-MIK-L10 The No-Invariant Row (MIK-R10 Rule 3)" with four rows (ruling 03:24:28 N2). **Two reopened claims reworded and re-anchored:** the docstring row (its anchor "MIK-R06, R10 and R14 later" is gone from the code; now "MIK-R06 and R14") and the registry row (five kinds; re-anchored on the line-exact quote "HISTORY_ROW_KINDS: Final["). The registry Logic bullet names five kinds. Other rows were projected or normalised by the installed fixer, or re-pointed by exact line shift. No verification stamp was advanced.
- 2026-09-30T02:33:27+00:00: Generated citation repair: `INVARIANT_DISPOSITIONS`; `FAMILY_DISPOSITIONS` repointed to mcp/src/agents_remember/models/knowledge_files/history.py:82-82; mcp/src/agents_remember/models/knowledge_files/history.py:83-83. No content impact: mechanical anchor-range projection bound to citation source snapshot 2501d8517027eb87355c9ee9e103bd2540df3597da078061ee6e1a15b93cb8de; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:49:00+00:00: Generated citation repair: `INVARIANT_DISPOSITIONS`; `FAMILY_DISPOSITIONS` repointed to mcp/src/agents_remember/models/knowledge_files/history.py:80-80; mcp/src/agents_remember/models/knowledge_files/history.py:81-81. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-29T21:49:00+00:00: Generated citation repair: `HistoryFile` repointed to mcp/src/agents_remember/models/knowledge_files/history.py:381-425. No content impact: mechanical anchor-range projection bound to citation source snapshot 638702294543ccef6675e0edeea49c5b9a4c8b527268ae6b389f7cfbcbb941b1; claim bytes unchanged; generated by ccr-r10@v1.

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T23:27:43+02:00 — 260928-MIK-L11 curator (uncommitted change set on `ar/260928-mik-l11`, code base `2c6f170ef07bf6767d582f76c9f9dd06bbdd06a4` plus the staged delta): **body updated for MIK-R11.** Added a Logic bullet for `PlannedEffectRow` and the section "260928-MIK-L11 The Planned Row" (`PlannedRef`, the disposition-bound ref, the two requirement spellings of review R1 F5). **The reopened `HISTORY_ROW_KINDS` claim was re-read and reworded** (four kinds, `planned` owned by MIK-R11) and re-measured; the Logic bullet on the registry was reworded to match. Other rows were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T20:47:37+02:00 — 260928-MIK-L30 curator (uncommitted change set on `ar/260928-mik-l30`, code base `719acba61e491d0b7f1ee82dbeea5314ecec5083` plus the staged delta, including the untracked-then-staged new files): **body updated for MIK-R30.** Added the section "260928-MIK-L30 What An Onboarding Row Means" (the docstring-only change, recording architect ruling 2026-09-29T18:49:50 (3)) and reworded the Logic sentence that left the kind's semantics to L30. Rows below the docstring were re-pointed by the installed fixer. No verification stamp was advanced.
- 2026-09-29T14:21:42+02:00 — 260928-MIK-L24 curator (uncommitted change set on `ar/260928-mik-l24`, code base `cd3e943d740b490d391722389af0a6bca0ccf93e` plus the working-tree delta and untracked files): **Body update: the `onboarding_trace` row kind (registered by MIK-R24, owned by MIK-R30).** Added a Logic bullet for `OnboardingTraceRow`, including the architect ruling N1: the moved marker lines go in the structured `markers` list, and `reason` is a short fixed summary. **Corrected claims this change made untrue:** the registry holds three kinds, not two; MIK-R30 is no longer a future adder; and "no row is produced automatically" now names the crossing sync's marker move as its one mechanical writer. The reopened `HISTORY_ROW_KINDS` row was re-measured (`282-286`) and reworded. A row for the new class and one for its long-marker test were added.
- 2026-09-29T09:30:11+02:00 — 260928-MIK-L20 curator (uncommitted change set on `ar/260928-mik-l20`, code base `aa07b1c937d1dc01ea6c51d0582eaf3871afcc8d` plus the staged delta): **No content impact** — citation-only repair. MIK-R20 adds the census import and the `CensusDocument` member to `models/knowledge_files/documents.py`, so its `SCHEMA_MODELS` table moved to `:64-71`; this card's history-schema row was re-pointed, its claim unchanged (the history schema is still registered there). No verification stamp was advanced.
- 2026-09-29T06:00:00+02:00 — 260928-MIK-L07 curator (uncommitted change set on `ar/260928-mik-l07`, code base `45fe37749b388de348d16ced50c28c03490dce64` plus the working-tree delta, after worker fix round 1): created this card for the new file MIK-R07 adds. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
