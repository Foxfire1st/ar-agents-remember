# mcp/src/agents_remember/memory/knowledge/read_refusals.py

## Governing Overview

[memory route overview](../overview.md)

## Purpose

**The refusal vocabulary of the selective recorded-scope read**: one factory per observable failure point,
in one module so the codes, the offending selector and the advertised next action stay together instead of
being spelled out at each call site. The shared `refusal` factory and the exception types stay in
`refusals.py`; this module only names the failures one bounded snapshot-bound read can produce.

## Code Commentary

### Logic

Six factories, and the distinction they carry is the one a caller actually acts on — not "did it work":

| Factory | Code | The fact |
| --- | --- | --- |
| `selector_absent_refusal` | `selector_absent` | the seed names an identity or revision the snapshot does not hold — the caller asked the **wrong question** |
| `registration_absent_refusal` | `registration_absent` | the seed is a **path with no recorded realization claim** (or, with `with_proofs`, no realization or proof claim) — a right question whose answer is that nothing is recorded there yet (zero recorded counts) |
| `page_budget_too_small_refusal` | `page_budget_too_small` | the selection is valid and one indivisible item does not fit; `observed` is the exact minimum and the **position is unchanged**, so raising the budget re-reads the same item rather than skipping it |
| `continuation_binding_mismatch_refusal` | `continuation_binding_mismatch` | the cursor binds another snapshot, context, selector, policy, schema, manifest or a position outside the selection; **no items returned** |
| `snapshot_unavailable_refusal` | `snapshot_unavailable` | the selected snapshot cannot be obtained at all: absent namespace row, another schema generation, another logical digest, unreadable file. The mirror of the two absence codes — nothing is known about the graph because the dataset itself is missing |
| `selection_incomplete_refusal` | `selection_incomplete` | the selection reached the declared execution bound; **no total and no partial manifest** are emitted |

Three groupings carry the semantics, and they are what a consumer should read the module for:

- **absence** (`selector_absent`, `registration_absent`) — the snapshot *was* read and holds no such
  record. That is a fact about the recorded graph and explicitly **not** a statement that the path,
  identity or family has no obligations, and never a finding of "no semantic impact". No Markdown, no
  working tree and no `HEAD` is consulted to fill the gap.
- **wrong snapshot** (`continuation_binding_mismatch`, `candidate_snapshot_unpublished`,
  `stale_precondition`, `snapshot_unavailable`) — the bytes are not the ones the request named. A page
  assembled from two revisions is not a page, so none of these returns partial items.
- **budget** (`page_budget_too_small`) — the selection is valid and the presentation does not fit. A
  budget is a presentation choice and must not be able to alter the selection.

**Every one of them leaves the database byte-identical.** This operation only ever issues `SELECT`
statements on a connection it opened read-only, so "a refused read persisted nothing" is a property of the
read path rather than a rollback it has to remember to perform. The evidence measures it at the first page
*and* at a later page of one walk, by comparing per-table row counts and the logical digest either side of
the refusal.

**`selector_absent` and `registration_absent` are separate codes on purpose:** a caller that named a
family identity which does not exist asked the wrong question, while a caller that named a path with no
recorded claims asked a right question whose answer is that nothing is recorded there yet. Folding them
together would tell one of the two callers something false about the repository.

**Three of the six factories now carry the operation they refuse for.**
`selector_absent_refusal`, `snapshot_unavailable_refusal` and `selection_incomplete_refusal` each take
an `operation: KnowledgeOperation = _OPERATION` keyword whose default is this module's own
`read_knowledge_scope`, so the facet selection seam raises those same three codes under
`read_facet_scope` through the shared factories instead of a parallel copy of their messages. The
default keeps every existing caller byte-identical; `registration_absent_refusal`,
`page_budget_too_small_refusal` and `continuation_binding_mismatch_refusal` still name `_OPERATION`
unconditionally, and the six-code vocabulary itself is unchanged.

**`registration_absent_refusal` names proof claims for the family-complete leaf read (260928-MIK-L01,
ruling N6 of 2026-09-30 00:08:39).** It takes `with_proofs: bool = False`. The leaf read of a converted tree
(`application/knowledge_leaf/pages.py`) seeds on realization *and* proof entries (ruling Q3 of 2026-09-29
23:21:57) and passes `True`, so its detail, `expected` and `next_action` say "realization or proof claim".
The default wording, which the recorded-scope read and the diff use, is byte-for-byte unchanged, so the
database read and every existing caller keep their exact message.

### Conventions

- Each factory carries a `RefusalFacts` triple (`record_id`, `expected`, `observed`) and a `next_action`
  sentence, so a caller can branch on the code and still be told what to do without parsing message text.
- **`snapshot_unavailable` is the code a schema this build cannot read surfaces as** — the read does
  **not** use `unsupported_schema` (which is shared with earlier leaves and unchanged). The detail names
  **both** generations, so a caller is never told "unsupported" without being told what was expected and
  what was observed.
- `selected_input_unavailable` remains the absent/unreadable-file case and is raised from
  `refusals.py` by the application seam, not re-declared here.
- A `record_id` defaults to `<continuation>` for the cursor refusals, because the offending object is the
  cursor rather than a stored record.

### Invariants And Boundaries

- **The vocabulary is defined where it decides.** The codes themselves live in
  `models/knowledge/result.py`; this module supplies the factories, and it imports the shared `refusal`
  helper rather than restating it.
- **No factory here can produce a page.** Each is a `KnowledgeRefusal`, and the result model refuses to
  carry both a page and a refusal.
- **No code names a semantic verdict.** `registration_absent` is absence and not "no semantic impact";
  the requirement's *Forbidden Overreach* forbids inventing one, and the vocabulary has no room for it.
- **Boundary.** This module names failures. It does not detect them (the application seam and the
  selection layer do), does not decide the operation's authority, and writes nothing.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

- **The two absence codes, separated by which question the caller got wrong.** [1]
- **MIK-R01: the leaf read's wording names proof claims too; the default wording is unchanged (ruling N6).** [2]
- **The budget refusal that reports the exact minimum and leaves the position unchanged.** [3]
- **The binding refusal: a page assembled from two snapshots is not a page of either.** [4]
- **The snapshot-unavailable refusal, which is also what an unreadable schema generation surfaces as.** [5]
- The execution-bound refusal, so a partial selection with an invented total is unrepresentable. [6]
- The shared factory and facts model this module composes rather than re-declares. [7]
- **The six codes and the one operation this leaf added to the shared vocabulary.** [8]
- **The node that measures the persisted-nothing property at a later page as well as at the first.** [9]
- **The node that measures a refused read of a real database leaving the file byte-identical.** [10]
- The absence nodes, one per absence code. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
