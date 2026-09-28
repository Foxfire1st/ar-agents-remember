# mcp/tests/test_review_intent_summary.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_review_intent_summary.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:55:21+02:00 |
| lastVerifiedCommitHash | `69883386d36d7cdb7faeed5bdf275ddd66d87aea` |
| lastVerifiedCommitDate | 2026-09-28T23:28:51+02:00|
| governingOverview | `mcp/tests/overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The executable pin for the changed-intent summary behind the compact `Intent review +N −N` entry
(`ICR-R24@v3`, leaf `260921-ICR-L47`). Six cases build real knowledge snapshots through the shipped
write operations and read them through the real
[`review_intent_summary`](../src/agents_remember/application/review_intent_summary.py.md) and its
route, so every count class and every answer state is measured rather than asserted from a mock.

## Code Commentary

### Logic

- `_shared_base` authors a common ancestor (`A` shared by two families, `B`, `D` realized once,
  families `F1 {A, B}` and `F2 {A, D}`); `_extend` copies it to an after side; `_resolution` builds the
  `ReviewCandidateResolution` the summary reads.
- **Counts:** added, revised and removed statements and guarantees are `+`/`−`; realization-only and
  membership-only changes are typed apart (+3 −4, realization_only 1, membership_only 1). A revised
  member shared by two families counts once on each side.
- **Record-only successors (L47-R1-F3):** a status-only invariant successor and a version-only family
  successor each count (1, 1); a same-guarantee successor with a new member stays `membership_only`.
- **States:** divergent successors make the answer `partial`; an absent candidate dataset is
  `unavailable` with its refusal and no counts; the route answers every typed state with 200 and an
  unwired process with 503.

### Conventions

Registered in the `unit-regression` lane of `test-evidence-lanes.toml` (an unregistered test file is
refused by the lane gate). It uses local constants rather than the exact-consumer
`read_scope_test_support` module, which would have made it a consumer of that support (worker event
E2). The module docstring states the route's status idiom (review F6).

### Invariants And Boundaries

The fixture drives the shipped writers only; it does not hand-edit SQLite. A revert of the F3 rule
(`review_intent_summary.py` at A1) fails the record-only case (`assert (0, 0) == (1, 1)`, review R2).

### Todos

None.

## Docs References

No Domain Documentation source is configured for this test module.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant domain documentation was found. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The shared ancestor the count cases extend. | `_shared_base` | mcp/tests/test_review_intent_summary.py:240-258 |
| Added/revised/removed as +/−, relationship-only as typed counts. | `test_counts_statement_and_guarantee_heads_and_keeps_other_changes_apart` | mcp/tests/test_review_intent_summary.py:261-316 |
| A shared revised member counts once per side. | `test_a_revised_statement_two_families_share_counts_once_on_each_side` | mcp/tests/test_review_intent_summary.py:319-338 |
| Record-only successors count; a same-guarantee member change stays typed. | `test_a_record_only_successor_counts_once_on_each_side` | mcp/tests/test_review_intent_summary.py:341-380 |
| Divergent heads are `partial`. | `test_an_identity_without_one_head_makes_the_summary_partial` | mcp/tests/test_review_intent_summary.py:383-403 |
| Absent knowledge is `unavailable`, never zero. | `test_missing_knowledge_is_unavailable_with_its_refusal_never_zero` | mcp/tests/test_review_intent_summary.py:406-418 |
| 200 for every typed state, 503 unwired. | `test_the_route_answers_every_typed_state_in_the_body` | mcp/tests/test_review_intent_summary.py:421-457 |
| The lane registration. | "mcp/tests/test_review_intent_summary.py" | mcp/tests/test-evidence-lanes.toml:185-185 |

## Cross-Repo References

No cross-repository behavior.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-28T23:11:42+02:00 — 260921-ICR-L56 curator (candidate tree `0dabc51f68b613546ec971657726b97828afb69a` over code base `ae2fd5c864aa2609ae45b5c7dbbaa693569aefc6`): No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_read_anchor_memo.py` row at `:173`; each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T20:07:41+02:00 — 260921-ICR-L55 curator: No content impact: re-pointed 1 citation into `test-evidence-lanes.toml` after this leaf inserted the `mcp/tests/test_notes_listing.py` row at `:162` (candidate tree `c77a4346480db6674dd760f974e8b24079d8f755` over code base `e66f1f3894116e0bb37b49f178d8bfcb130a7e28`). Each moved row cites the same line content it cited at the landed base. Wording is unchanged, and no stamp was advanced.
- 2026-09-28T18:18:00+02:00 — 260921-ICR-L47 curator (post-sync re-measure after the Architect's `worktree_sync` onto code `eda947325ccbe0791973953265278597e968a34a` / memory `6ccb9b615e383174c22f110a6492e6231a4e261f`; L47 candidate tree `5f22717e68041d6819e9671cee2ab30e4d3d3e13`): No content impact: citation ranges into files L44, L45 or L47 moved (`mcp/tests/test-evidence-lanes.toml`) were re-measured against the post-sync code; each re-pointed row held its anchors in its own measurement tree (`eda94732` or the pre-sync L47 candidate `72efa4bb`) and holds them after the line mapping, or names a literal that occurs exactly once in the post-sync file within five lines of its cited place. Claim wording unchanged. No stamp advanced.

- 2026-09-28T16:55:21+02:00 — 260921-ICR-L47 curator (uncommitted candidate tree `72efa4bbc169b16afe8ef249499edf79cad9940d` over code base `58e22246cc09ef0ee12095e284a111a475081c38`): created this card for the new summary test module (six cases after A2 added the record-only case). The verification pair names the code base; closeout owns the real stamp.
