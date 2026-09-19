# mcp/src/agents_remember/memory/knowledge/merge_validation.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/merge_validation.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:45+02:00 |
| lastVerifiedCommitHash | `4904e08f0668ed6d11a2c44d0118716bb82f735c` |
| lastVerifiedCommitDate | 2026-09-17T22:32:32+02:00|
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**What the merge proves about its own result, after SQLite applied the changeset.** Applying a changeset is not evidence that the intended changes landed. This module is the postcondition half of the merge: it reads the merged candidate and the three inputs and refuses when the result does not carry what the operation said it would. Every check reads through read-only connections and writes nothing; a refusal here means no candidate was published and the merged temporary is discarded by its owner.

## Code Commentary

### Logic

`MergeInputs` names the four datasets of one merge once — base, left, right, merged — so a validation pass cannot mix them up. Four checks, each answering a different question:

- `require_structural_validity(inputs)` — no foreign-key violation, every authored row still reading back as its typed aggregate, and every declared predecessor edge present. The typed-row read is the whole check: decoding every canonical table through the logical body constructor proves the JSON columns hold unambiguous JSON and the sealed aggregates still match their stored digests, because the decoders **recompute** the seal rather than trusting it (`_require_sealed_aggregates`).
- `require_immutable_revisions_preserved(base, candidate)` — every revision the common base sealed is still identical to the base's row (`_first_revision_difference`), and every edge the base sealed is still present (`_first_missing_edge`). Immutability is compared against the **base** rather than against whichever side happens to be present: a revision the common base sealed is the same revision in every dataset derived from it, so a difference is an in-place rewrite of a sealed aggregate rather than an authored successor.
- `require_side_inputs_preserved(base, side)` — each side's sealed revisions still match the common base. This is the refusal for a side that rewrote a revision in place behind its identity, which is the one input defect no schema comparison can see: the file is internally consistent and its content is simply not the aggregate the base sealed. It runs **before** the merge, so the defect is refused as an input defect instead of being carried into a candidate.
- `require_applied_changes(delta, candidate)` — every operation the changeset materialised is looked for in the result: an insert's row is there holding the side's values, an update's supplied columns hold the side's values, a delete's row is gone. The comparison is per supplied column and against the **side the operation came from** (`_first_unapplied_change`, `_first_differing_column`).

**The digest comparison is deliberately the *stored* payload digest recomputed from the stored row**: re-stating the same payload with a different JSON key order is not a change to a sealed revision, while changing the statement behind the digest is.

### Conventions

- Refusals are rendered with the not-supplied marker named explicitly (`_render`, `_render_key`), so a refusal never presents the marker as a stored value.
- `_row_of` reads one canonical row by its declared primary key, and `_revision_rows` pairs each revision row with its identity, so a difference can name both sides of the comparison.
- `_EdgeCheck` carries one sealed-edge comparison's aggregate, role and the two readers it needs, rather than threading four arguments through the walk.

### Invariants And Boundaries

- **Two reachability facts are stated, not implied.** `require_immutable_revisions_preserved` is called twice with two different reachability facts: on a **side input** the call is reachable and has failing cases, while on the **merged candidate** it is not reachable by a black-box case — the merged candidate is a copy of the left side with the right delta applied, the left side has already passed the same comparison, and the right delta cannot remove or rewrite a sealed aggregate without the right side failing first. `require_applied_changes` is likewise unreachable under this schema: the only producer of the merged candidate is SQLite's own application over a copy of the left side, every canonical table is a plain `STRICT` table and every declared trigger only `RAISE(ABORT)`, and an input whose trigger set is not the declared one is refused by the preflight. Neither is therefore a covered guard; both stay because publication is where the invariant has to hold, and each policy is exercised directly by a boundary node.
- **Only `require_structural_validity` has a reachable failing case** — a candidate carrying a foreign-key violation built from inputs that all carry it, so no delta mentions it and the candidate is the first place it can be seen.
- **Nothing here writes.** All four checks are read-only, and no check repairs what it finds.
- **Boundary.** This module validates a produced candidate and its inputs. It does not apply a changeset, decide a conflict policy, freeze or publish.

### Todos

None recorded for this slice.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no `Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The four datasets named once so a validation pass cannot mix them up. | `MergeInputs` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:64-70 |
| The reachable structural check, whose typed-row read recomputes every seal. | `require_structural_validity` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:73-101 |
| The immutability comparison, including the two calls with two different reachability facts. | `require_immutable_revisions_preserved` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:104-152 |
| The side-input pass that refuses an in-place rewrite before the merge starts. | `require_side_inputs_preserved` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:155-166 |
| The applied-change postcondition and its three-part unreachability statement. | `require_applied_changes` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:169-211 |
| The per-column comparison against the side the operation came from. | `_first_unapplied_change`; `_first_differing_column` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:214-247; mcp/src/agents_remember/memory/knowledge/merge_validation.py:250-276 |
| The sealed-aggregate read that catches a row edited behind its seal with the file still open. | `_require_sealed_aggregates` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:279-309 |
| The two halves of the base comparison: the sealed revision rows and the predecessor edges in their separate table. | `_first_revision_difference`; `_revision_rows`; `_first_missing_edge`; `_edge_set` | mcp/src/agents_remember/memory/knowledge/merge_validation.py:327-346; mcp/src/agents_remember/memory/knowledge/merge_validation.py:389-396; mcp/src/agents_remember/memory/knowledge/merge_validation.py:360-375; mcp/src/agents_remember/memory/knowledge/merge_validation.py:378-386 |
| The refusal for a sealed revision whose stored row no longer matches its payload. | `immutable_revision_changed_refusal` | mcp/src/agents_remember/memory/knowledge/merge_refusals.py:176-196 |
| The boundary node for the reachable structural guard, and the two direct-policy nodes for the unreachable call sites. | "test_a_candidate_carrying_a_foreign_key_violation_is_refused_by_the_structural_check" | mcp/tests/test_knowledge_guarded_merge_boundaries.py:187-226 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T13:45+02:00 — 260915-KS-L5 curator (uncommitted change set on `ar/260915-ks-l05`, base `3332a4ce`): created this one-to-one card for the new postcondition module. It records the four checks and what each answers, the sealed-digest rule (the *stored* payload digest is recomputed, so re-stating the same payload with different JSON key order is not a change while changing the statement behind the digest is), and — as the load-bearing statement a later reader needs — this leaf's two stated reachability facts: the merged-candidate immutability call and the applied-change check are non-experiments under this schema, their policies are exercised directly by boundary nodes, and only the structural check has a reachable failing case. It also corrects the record in this leaf's own review: the predecessor set lives in a **separate** edge table, so the revision-row comparison never sees it. Verification metadata remains empty until closeout stamps the code commit.
