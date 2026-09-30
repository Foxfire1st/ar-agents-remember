# mcp/src/agents_remember/application/review_intent_summary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_intent_summary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T12:15:39+02:00 |
| lastVerifiedCommitHash | `ce4594231eac0b18950d22d6aee0d3b9f3eba3db` |
| lastVerifiedCommitDate | 2026-09-30T12:51:55+02:00|
| governingOverview | `mcp/src/agents_remember/application/overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The one owner of the changed-intent summary**: the two numbers the task entry's compact
`⇄ Intent review +N −N` control shows before the reviewer is opened (`ICR-R24@v3`, leaf
`260921-ICR-L47`). The numbers describe the **authored intent** of the comparison the entry opens — not
the change set's line totals (which the entry used to show by reusing the change-set button) and not
the subject catalogue's identity totals (which enumerate subjects without comparing them).

It answers over the reviewer's own resolution, so the entry cannot count a different pair from the one
it opens: `read_review_intent_summary` resolves the canonical task context through
`resolve_review_candidate` (a closed leaf resolves to its recorded comparison, `ICR-R12`), and
`intent_summary_of` refuses the pair through the shared
[`review_pair_preflight`](review_pair_preflight.py.md) before reading anything, so the catalogue and
the summary cannot disagree about whether a pair is readable.

## Code Commentary

### Logic

**Count semantics (master decision on count semantics, `task.json`, entry labelled 12:00 and
clock-corrected by the 12:10:21 entry; refined by the leaf's 16:15:11 ruling on L47-R1-F3).**

- Each side's current statement of an identity is its **head revision** under
  `review_revision_comparison.revision_heads` — the rule the reviewer uses to choose which before/after
  revisions it renders (`ICR-R07`). This module reuses it; it does not define a second head rule.
- `+` (`added`) counts invariant and family (joint-guarantee) heads **only the after side holds**; `−`
  (`removed`) counts heads **only the before side holds**. A revised statement is one of each, so it
  counts once on each side. An identity is counted once however many families hold it (memberships
  are compared by canonical invariant identity).
- **Every successor revision counts**, including a record-only successor whose text is unchanged and
  only its origin state, acceptance reference or version moved (`_STATEMENT_FIELDS` includes
  `state_at_origin` and `acceptance_ref`; `_GUARANTEE_FIELDS` is `joint_guarantee`, `state_at_origin`,
  `acceptance_ref`). The one exclusion is a successor whose compared fields are **equal** to the
  superseded head's while its attached relationships differ — an invariant's realization claims
  (`_claim_key`: path, locator, source identity, role, rationale) or a family's members. That, and an
  unchanged head whose realizations moved, is carried as the typed `realization_only` /
  `membership_only` count and never folded into `+`/`−`.
- An identity with several heads on a side, or a retained population with no head, is **unresolved**
  (`_no_single_head`); the answer is then `partial`, never a guessed winner.
- A pair the preflight refuses, or a half that fails to read between preflight and read
  (`KnowledgeStorageError`/`apsw.Error`), is **`unavailable`** with the owner's refusal and no counts.

**Read shape.** `_read_side` opens one snapshot read-only and reads, through the shipped
`read_queries` owners, the predecessor edges, each identity's retained revision ids, the head rows'
compared fields, the heads' realization claims and the family heads' memberships; then closes it.
`_tally` walks the union of identities and `_classify` places each one. It runs no subject comparison
and loads no subject content beyond each head's own fields.

### Conventions

Pure composition over existing read owners, returning the typed
[`ReviewIntentSummaryResult`](../models/knowledge/review_intent_summary.py.md). It is a sibling module
rather than a growth of `review_revision_comparison.py` (worker observation O1: that file is 552
lines); it imports `revision_heads` from there instead of copying it.

### Invariants And Boundaries

- **Unavailable is never zero.** No count is produced for an unread comparison; the model's validator
  makes `counts` and `refusal` mutually exclusive.
- **One head rule.** The summary's head is the revision comparison's head; changing one without the
  other would let the entry count a revision the reviewer renders as superseded.
- **Same resolution, same preflight as the catalogue.** No other dataset is substituted and no
  candidate is chosen here.
- **Read-only.** It writes, retains and freezes nothing.
- **Presentation is not owned here.** Whether an acceptance-only successor is worded differently from a
  text revision is `ICR-R35`/leaf L49's concern (leaf ruling 16:15:11 on F3; master decision 13:40 on
  "wording unchanged").

### Todos

- Query cost is linear in identities: one `fetch_revision_ids` call per identity per side (review R2
  observation O-R2-3: L41's summary makes 115 store calls, about 21 ms in-process). One grouped
  revision-id query per side would make it constant. The observation was routed as a candidate for a
  later performance leaf (L50/L51); it is not delivered here.

## Docs References

No Domain Documentation source is configured for this module; the count semantics are the repository's
own ruling, cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

The summary composes the reviewer's resolution, the shared pair preflight and the revision comparison's
head rule; the fixture tests pin every count class.

| Finding | Anchor | Source |
| --- | --- | --- |
| The public read: the reviewer's own resolution, a refused resolution returned as `unavailable`. | `read_review_intent_summary`; `resolve_review_candidate` | mcp/src/agents_remember/application/review_intent_summary.py:122-134 |
| One resolved pair: the shared preflight first, then both sides read, a mid-read storage failure refused as unreadable, `partial` exactly when something is unresolved. | `intent_summary_of`; `pair_preflight_refusal`; `unreadable_candidate_refusal` | mcp/src/agents_remember/application/review_intent_summary.py:137-167 |
| The compared fields, including the record status that makes a record-only successor count. | `_STATEMENT_FIELDS`; `_GUARANTEE_FIELDS` | mcp/src/agents_remember/application/review_intent_summary.py:76-83; mcp/src/agents_remember/application/review_intent_summary.py:85-85 |
| The classification: unresolved, after-only, before-only, relationship-only, or a counted successor. | `_classify`; "tally.attached_only"; "tally.after_only" | mcp/src/agents_remember/application/review_intent_summary.py:339-369 |
| Several heads, or a population with none, is not one head. | `_no_single_head` | mcp/src/agents_remember/application/review_intent_summary.py:372-375 |
| Family members compared by canonical invariant identity, so a member whose invariant moved is the same membership. | `_family_side`; "invariant_of.get(invariant_revision, invariant_revision)" | mcp/src/agents_remember/application/review_intent_summary.py:274-304 |
| What one realization claim asserts, independent of the claim record's own identity. | `_claim_key` | mcp/src/agents_remember/application/review_intent_summary.py:317-326 |
| The head rule reused from the revision comparison owner. | `revision_heads` | mcp/src/agents_remember/application/review_revision_comparison.py:81-94 |
| The fixture that pins added/revised/removed as +/− and realization-only/membership-only as typed counts. | `test_counts_statement_and_guarantee_heads_and_keeps_other_changes_apart` | mcp/tests/test_review_intent_summary.py:261-316 |
| A revised member shared by two families counts once on each side. | `test_a_revised_statement_two_families_share_counts_once_on_each_side` | mcp/tests/test_review_intent_summary.py:319-338 |
| A status-only or version-only successor counts once on each side (L47-R1-F3). | `test_a_record_only_successor_counts_once_on_each_side` | mcp/tests/test_review_intent_summary.py:341-380 |
| Divergent heads make the answer `partial`; absent knowledge is `unavailable` with no counts. | `test_an_identity_without_one_head_makes_the_summary_partial`; `test_missing_knowledge_is_unavailable_with_its_refusal_never_zero` | mcp/tests/test_review_intent_summary.py:383-403; mcp/tests/test_review_intent_summary.py:406-418 |
| The composition root wires this read as the fourth review port. | `review_intent_summary_port`; `read_review_intent_summary` | mcp/src/agents_remember/cli/dashboard.py:135-142 |

## Cross-Repo References

No cross-repository behavior is implemented here; the read stays inside one repository namespace's two
snapshots.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-30T12:15:39+02:00 — 260928-MIK-L29 curator (staged change set on `ar/260928-mik-l29`, code base `b54d1b0331f67454bcf245a7a338b04900181c3c`): No content impact: this card's own source is unchanged. MIK-R29 grew `mcp/src/agents_remember/cli/dashboard.py` (the reader import and the `knowledge_reader_port` binding), so the citation rows into it that moved were re-pointed by the installed fixer's normalisation or by the exact base-to-staged line shift; every re-pointed row was checked to hold its anchors in the new range, and no claim was reworded. No verification stamp was advanced.
- 2026-09-30T04:01:40+02:00 — 260928-MIK-L25 curator (uncommitted change set on `ar/260928-mik-l25`, code base `3eb034a6ab0493a51da5dcd6d013aa6f27f39496` plus the staged delta): No content impact: this card's source is unchanged. Rows citing lines that MIK-R25 moved in `dashboard.py` were re-pointed, by the installed fixer (its generated bullets are kept, since no claim was reworded) or by the exact base-to-staged line shift for the rows it declined; each such row was byte-identical to memory HEAD. No verification stamp was advanced.
- 2026-09-28T17:30:17+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): two rows re-anchored after the full memory-quality run reopened them: the attribute and parameter references (`attached_only`, `after_only`, `invariant_of`) are now named as the literal text the cited ranges hold ("tally.attached_only", "tally.after_only", "invariant_of.get(...)") instead of as symbols, because they are uses inside `_classify`/`_family_side`, not declarations. Claim wording unchanged.

- 2026-09-28T16:55:21+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`; delivery attempt L47-A3, review R2 pass-with-notes): created this card for the new changed-intent summary owner (`ICR-R24@v3`). It records the master's count semantics as the code implements them after the F3 ruling: record-only successors count; only same-content relationship changes are typed apart. The verification pair names the code base, because the file exists only in the uncommitted candidate; closeout owns the real stamp.
