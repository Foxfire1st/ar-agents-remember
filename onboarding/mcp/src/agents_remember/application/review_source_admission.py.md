# mcp/src/agents_remember/application/review_source_admission.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_source_admission.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T10:05:09+02:00 |
| lastVerifiedCommitHash | `b54d1b0331f67454bcf245a7a338b04900181c3c`|
| lastVerifiedCommitDate | 2026-09-30T11:03:56+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

The one owner of the question **which paths the review's source-content read may open** (ICR-R03@v1,
under the 2026-09-28 admission ruling). `application/review_source_content.py` reads bytes and
assembles the answer; this module decides, before any byte is read, whether the requested path is
admitted and states why.

Exactly two populations are admitted, and every other path is refused by name:

1. **A changed path.** The requested generation's own measured change set lists it, or — only when
   that pair could not be measured — the change set this leaf's review publishes lists it. The
   inventory entry's own status travels with it.
2. **An attributed unchanged path.** The requested pair **was** measured and does not list the path,
   and a realization recorded in *that comparison's own* knowledge (before or after snapshot) is
   anchored at exactly this spelling — or, for a tree comparison since MIK-L31, a proof entry is
   (ruling 2026-09-30T05:36:19 Q1: a proof card's unchanged test file opens in full; datasets record no
   proofs and are unaffected). It is opened as context for that realization, stated as
   `admission="attributed_unchanged"` with `status="unchanged"`, and never becomes an inventory entry
   or a count: this module adds nothing to the inventory it reads.

The link question itself belongs to `application/review_source_realization_link.py`; this module only
consumes its answer. The policy was extracted from `review_source_content.py` before behavior was
added (that module went 733 → 596 lines), so the content read carries no admission logic of its own.

## Code Commentary

### Logic

**`admit_source_path` asks the measurements in a fixed order.** The requested generation's inventory
is asked first (`_entry_for`, an exact string match); a listed path returns a `SourceAdmission` with
that entry and `path_bound="requested_generation"`. When the inventory is `measured` and does not list
the path, the only remaining admission is the recorded realization link, delegated to
`recorded_realization_link` and judged by `_attributed_or_refused`. When the requested pair could not
be measured, the leaf's own published pair (recorded baseline against the candidate tree it binds now)
is re-measured through `review_inventory`; a path it lists is admitted as
`path_bound="leaf_change_set"`, and otherwise `_unconfined` refuses. **No unchanged path is admitted
while the requested pair is unmeasured**: "unchanged" is then not a fact this read holds.

**`_attributed_or_refused` keeps three outcomes apart.** A link on either half admits the path with
`path_bound="requested_generation"` (the measurement that proves the path unchanged) and an
`admission_detail` naming which halves linked it and in which comparison. Since ruling Q1 the sentence reads
"a realization or proof recorded for the path in the comparison's {sides} knowledge is anchored at this unchanged
path (…); it is opened as that entry's context …", matching the link owner's parenthetical ("records a
proof here"). No link with every bound
half read is the established negative, `_not_listed`. No link with some bound knowledge unread is
**undetermined**, `_link_undetermined`: the refusal says the link "could not be determined", names the
cause, directs the remedy at the unreadable snapshot, and never asserts that no realization links the
path. **The remedy names the cause (ICR-L43 review R2 O1, routed to MIK-R31 rule 6):** when every unread half
does not exist at all (`RealizationLink.never_initialized`), the next action is `_INITIALIZE` ("initialize this
leaf's knowledge -- the snapshot files the detail names do not exist, so it was never created -- …"); a half that
exists but could not be read keeps `_RESTORE` ("restore or repair the knowledge snapshot …").

**`SourceAdmission` carries what the expansion states.** `entry` is present only when the requested
generation listed the path. `status` is derived: `unchanged` for attributed context, the entry's own
status for a listed path, and `unknown` for a path the leaf change set bounded (the pair was not
classified). `mode_change` is false without an entry.

**The three refusals are all `source_content_unresolved`** with `offending_input` bounded by
`bounded_input` (512 characters), which `review_source_content.py` also uses for its own four
admission-fact refusals.

### Conventions

`__all__` publishes `SourceAdmission`, `admit_source_path` and `bounded_input`; the refusal builders
and `_entry_for` are private. `SourceAdmission` is a frozen dataclass rather than a wire model: only
`models/knowledge/review_source_content.py` defines wire shapes. `admission` defaults to `changed` so
both changed-path constructors stay identical to the pre-L43 values.

### Invariants And Boundaries

- **Attributed context never enters the inventory or its counts.** The module reads the inventory and
  returns an admission; it never appends an entry or changes `listed_total`.
- **Attributed context is bounded only by the requested generation's own measurement.** The model
  validator in `models/knowledge/review_source_content.py` makes any other `path_bound` for an
  `attributed_unchanged` expansion unconstructible.
- **An unmeasured pair admits no unchanged path** (Architect ruling closing L43-R1-F4 (3)); a
  superseded pair with no recorded generation admits none either (ruling (2)), which the link owner
  enforces.
- **Undetermined is not absent.** A refusal caused by unreadable knowledge must not carry the
  established-negative sentence.
- **Never initialized is not damaged.** Knowledge that was never created asks to be initialized, never
  restored or repaired; a damaged snapshot still asks to be restored or repaired.
- **A proof link admits only for an index-backed comparison, and only the paths its recorded proof
  entries name** (the link owner's `_proof_at_path`); a dataset comparison admits exactly as before.
- **Changed-path behavior is the pre-L43 behavior.** The R2 differential found all 19 bodies
  byte-identical to base after the two new fields were dropped.

### Todos

- **Resolved by MIK-L31:** the undetermined remedy says "initialize" when the leaf never initialized knowledge
  (reviewer observation O1, routed from ICR-L49 to MIK-R31 rule 6).

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The module's own statement of the two admitted populations and of why every other path is refused.** | "An attributed unchanged path." | mcp/src/agents_remember/application/review_source_admission.py:1-18 |
| The published surface and the fixed detail a changed path carries. | `__all__`; `_CHANGED_DETAIL` | mcp/src/agents_remember/application/review_source_admission.py:49-49; mcp/src/agents_remember/application/review_source_admission.py:51-51 |
| **The admission value: which measurement admitted the path, and the derived `unchanged` / entry / `unknown` status.** | `SourceAdmission` | mcp/src/agents_remember/application/review_source_admission.py:54-83 |
| **The fixed order: requested inventory, then the recorded link for a measured pair, then the leaf change set for an unmeasured one.** | `admit_source_path` | mcp/src/agents_remember/application/review_source_admission.py:86-128 |
| **Linked admits (a realization, or a proof of a tree comparison), established negative refuses, unread knowledge refuses as undetermined.** | `_attributed_or_refused` | mcp/src/agents_remember/application/review_source_admission.py:131-159 |
| The three refusals: unmeasured pair with no admitting change set, measured pair with no link, and a link that could not be determined. | `_unconfined`; `_not_listed`; `_link_undetermined` | mcp/src/agents_remember/application/review_source_admission.py:162-193; mcp/src/agents_remember/application/review_source_admission.py:196-215; mcp/src/agents_remember/application/review_source_admission.py:218-242 |
| The two remedies: initialize never-created knowledge, restore or repair a damaged snapshot. | `_RESTORE`; `_INITIALIZE` | mcp/src/agents_remember/application/review_source_admission.py:245-256 |
| Exact-string inventory match and the bounded offending input. | `_entry_for`; `bounded_input` | mcp/src/agents_remember/application/review_source_admission.py:259-265; mcp/src/agents_remember/application/review_source_admission.py:268-275 |
| **The link owner this module consumes.** | `RealizationLink`; `recorded_realization_link` | mcp/src/agents_remember/application/review_source_realization_link.py:77-97; mcp/src/agents_remember/application/review_source_realization_link.py:116-151 |
| The one caller: the content read hands its inventory here before reading any byte. | `_content` | mcp/src/agents_remember/application/review_source_content.py:241-285 |
| The inventory owner re-used for the leaf change set. | `review_inventory`; `source_tree_side` | mcp/src/agents_remember/application/review_source_inventory.py:429-469; mcp/src/agents_remember/application/review_source_inventory.py:168-176 |
| The wire literals this module fills and the validator that ties attributed context to `unchanged` and `requested_generation`. | `ReviewSourceAdmission`; `ReviewSourceExpansionStatus`; `_require_attributed_context_to_be_a_measured_unchanged_path` | mcp/src/agents_remember/models/knowledge/review_source_content.py:102-102; mcp/src/agents_remember/models/knowledge/review_source_content.py:107-107; mcp/src/agents_remember/models/knowledge/review_source_content.py:198-214 |
| **The cases: attributed admission without counting, unlinked refusal, and undetermined refusal.** | `test_an_unchanged_path_a_recorded_realization_links_opens_as_context_without_counting`; `test_an_unchanged_path_no_recorded_realization_links_is_still_refused`; `test_an_unreadable_snapshot_leaves_the_link_undetermined_rather_than_absent` | mcp/tests/test_knowledge_review_attributed_source_content.py:119-152; mcp/tests/test_knowledge_review_attributed_source_content.py:155-166; mcp/tests/test_knowledge_review_attributed_source_content.py:328-353 |
| The never-initialized remedy, and a proof entry linking its path in a tree index while a dataset links none. | `test_never_initialized_knowledge_asks_to_initialize_it`; `test_a_tree_index_links_a_path_its_proof_entry_is_anchored_at` | mcp/tests/test_knowledge_review_attributed_source_content.py:356-369; mcp/tests/test_knowledge_review_attributed_source_content.py:372-385 |
| Ruling Q1 at the route: an unchanged test file only a proof names is refused before the proof exists and admitted with the new sentence after. | `test_an_unchanged_path_only_a_proof_names_opens_in_a_tree_review` | mcp/tests/test_review_git_trees.py:950-1016 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T10:05:09+02:00 — 260928-MIK-L31 curator (staged change set on `ar/260928-mik-l31`, code base `48f680d5b95b8cb6eafff4f1ccd19c8f32e8c48c`; review R3 pass-with-notes): body update. Purpose and Logic record ruling 2026-09-30T05:36:19 Q1 (a tree comparison's proof entry admits its unchanged path; the admission sentence now says "a realization or proof recorded for the path", matching its parenthetical) and MIK-R31 rule 6 O1 (`_INITIALIZE` when the leaf's knowledge was never created, `_RESTORE` otherwise); two invariants added; the O1 Todo is marked resolved. The `_attributed_or_refused` row is reworded; three rows added (the remedies, the two new unit cases, the F12 route case of review R1 at 06:10:21).
- 2026-09-28T12:38:10+02:00 — 260921-ICR-L43 curator (uncommitted candidate tree `990a5c1a3afab15d04881475b2501ed98cddf908` over code base `a0b2c18d2b8d08ac1242a13f65bde900a190df7a`): created this card for the module that now owns source-content path admission. **Semantic transition:** the admission boundary set by L3 (a path is read only from a measured change set) is extended by the 2026-09-28 developer ruling to one further population — an unchanged path a realization recorded in the bound comparison's knowledge is anchored at — with the Architect's four scope rulings (stale anchors admit; unfrozen superseded and unmeasured pairs admit nothing; `unchanged` is the typed status). The undetermined-link refusal is from the L43-R1-F2 fix. Verification stamp names the code base; the module exists only in the uncommitted candidate and closeout owns the real stamp.
