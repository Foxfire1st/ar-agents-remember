# mcp/src/agents_remember/application/knowledge_currentness/state.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_currentness/state.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-29T19:59:41+02:00 |
| lastVerifiedCommitHash | `719acba61e491d0b7f1ee82dbeea5314ecec5083`|
| lastVerifiedCommitDate | 2026-09-29T20:27:14+02:00|
| governingOverview | `../overview.md` |

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The one state function of (code tree, memory tree) (MIK-R03 rules 2 to 4).** `invariant_currentness`
takes the code tree the caller resolved (or `None`) and the memory tree as its derived MIK-R23 index, which
every read is served from. `knowledge_read` and the published-intent block call it today; the reviewer
(MIK-R25) will call it once per side, and the path-based reader (MIK-R29) at its selected commit.

## Code Commentary

### Logic

- **Rule 2, the invariant state.** `invariant_state` applies the first rule that holds:
  1. `stale` if any entry, realization or proof, is stale;
  2. otherwise `unverifiable` if any entry is unverifiable;
  3. otherwise `unrealized` if no entry is a realization (proofs do not count here);
  4. otherwise `current`.
- **Stale proofs (carried L28 ruling 1a).** Proofs are observed exactly like realizations
  (`knowledge.proofs` beside `knowledge.realizations`), so a proof whose test changed or disappeared makes
  its invariant `stale`, even when the realization is current, and a proof-only invariant with a stale
  proof is `stale`, not `unrealized`.
- `invariant_currentness(code_tree, index, invariants, families)` opens the code tree once, expands each
  named family to its members (a family header counts its stale members, so every member is evaluated
  whether or not the read named it), and observes every entry of every wanted invariant. An ID the index
  does not hold as a record of the right kind is left out rather than guessed at (`_is_record`).
- **Rule 3, the wire shape.** `Currentness.to_document` gives `codeTree`, `counts` by state
  (`INVARIANT_STATES` order), `invariants[]` each `{id, state, entries[]}` listing every entry that is not
  current (`InvariantCurrentness.differing`), `families[]` each `{id, members, staleMembers, stale[]}`, and
  `unverifiableReason` when the whole read cannot be observed.
- **Compact entries (review N4, 19:13:41).** When a read-wide `unverifiableReason` is set (for example no
  tree), each differing entry is rendered as `{id, kind, path, state}` only, because the one reason already
  explains all of them.

### Conventions

- "Differing" entries include `unverifiable` ones: the block lists every entry that is not current, each
  with its state and reason.

### Invariants And Boundaries

- **Stale takes precedence over every other state**, and a stale invariant is never presented as current.
- **Nothing is withheld (D9).** The statement and relationships stay in the read's own payload, which this
  module never edits.
- **Reads only.** Nothing is written or re-anchored.

### Todos

- None recorded.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is the requirement packet `MIK-R03@v2` of task
`260928_maintained-invariant-knowledge` (with the architect rulings in the task's leaf document
`03_stale-invariants-flagged-at-read-time.json`) and the coordination-root note Doc14
(`notes/ar-intent-reviewer-and-beyond/Doc14-text-canonical-knowledge-layout.md`); they live outside the
code and memory repositories, so they are named here and not cited as rows.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The one function, its consumers, the rule-2 order and the visibility rule. | "The first rule that applies wins" | mcp/src/agents_remember/application/knowledge_currentness/state.py:1-20 |
| The state vocabulary in count order. | `InvariantState`; `INVARIANT_STATES` | mcp/src/agents_remember/application/knowledge_currentness/state.py:49-55 |
| Rule 2: stale, then unverifiable, then unrealized (proofs do not count), then current. | `invariant_state` | mcp/src/agents_remember/application/knowledge_currentness/state.py:58-68 |
| One invariant's differing entries, compact when a read-wide reason explains them. | `InvariantCurrentness`; `differing` | mcp/src/agents_remember/application/knowledge_currentness/state.py:71-96 |
| The family header with its stale members. | `FamilyCurrentness` | mcp/src/agents_remember/application/knowledge_currentness/state.py:99-113 |
| The block, its counts and the read-wide reason. | `Currentness`; `unverifiableReason` | mcp/src/agents_remember/application/knowledge_currentness/state.py:116-145 |
| The function: family members expanded, realizations and proofs observed alike. | `invariant_currentness`; `knowledge.proofs` | mcp/src/agents_remember/application/knowledge_currentness/state.py:148-198 |
| Unknown IDs are left out. | `_is_record` | mcp/src/agents_remember/application/knowledge_currentness/state.py:201-203 |
| Precedence cases. | `test_precedence_stale_before_unverifiable_before_unrealized` | mcp/tests/test_knowledge_currentness.py:405-418 |
| The stale-proof cases. | `test_a_proof_whose_test_changed_or_disappeared_is_flagged_stale` | mcp/tests/test_knowledge_currentness.py:421-439 |
| The per-side computation. | `test_one_function_computes_each_side_of_a_comparison` | mcp/tests/test_knowledge_currentness.py:442-461 |

## Cross-Repo References

No meaningful cross-repo references found: the function reads one memory tree's index and one code tree,
both named by its caller.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-29T19:59:41+02:00 — 260928-MIK-L03 curator (uncommitted change set on `ar/260928-mik-l03`, code base `e40c314ca55305f7e4334b4e8e16a10297f6f175` plus the working-tree delta and untracked files): created this card for the new file MIK-R03 adds. It records the carried L28 stale-proof ruling (proofs are observed like realizations) and the 19:13:41 review ruling N4 (compact entries under a read-wide reason). The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
