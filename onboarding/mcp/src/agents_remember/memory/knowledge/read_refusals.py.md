# mcp/src/agents_remember/memory/knowledge/read_refusals.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/memory/knowledge/read_refusals.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b`|
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l07` uncommitted source; base `4eb2b1992f6183fba06e9f31aa664d9a93094c26` |
| governingOverview | `mcp/src/agents_remember/memory/overview.md` |

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
| `registration_absent_refusal` | `registration_absent` | the seed is a **path with no recorded realization claim** — a right question whose answer is that nothing is recorded there yet (zero recorded counts) |
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| **The two absence codes, separated by which question the caller got wrong.** | `selector_absent_refusal`; `registration_absent_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:35-57; mcp/src/agents_remember/memory/knowledge/read_refusals.py:60-79 |
| **The budget refusal that reports the exact minimum and leaves the position unchanged.** | `page_budget_too_small_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:82-108 |
| **The binding refusal: a page assembled from two snapshots is not a page of either.** | `continuation_binding_mismatch_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:111-135 |
| **The snapshot-unavailable refusal, which is also what an unreadable schema generation surfaces as.** | `snapshot_unavailable_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:138-156 |
| The execution-bound refusal, so a partial selection with an invented total is unrepresentable. | `selection_incomplete_refusal` | mcp/src/agents_remember/memory/knowledge/read_refusals.py:159-177 |
| The shared factory and facts model this module composes rather than re-declares. | `refusal`; `RefusalFacts` | mcp/src/agents_remember/memory/knowledge/refusals.py:48-55; mcp/src/agents_remember/memory/knowledge/refusals.py:57-77 |
| **The six codes and the one operation this leaf added to the shared vocabulary.** | `KnowledgeRefusalCode`; `KnowledgeOperation` | mcp/src/agents_remember/models/knowledge/result.py:36-143; mcp/src/agents_remember/models/knowledge/result.py:36-72; mcp/src/agents_remember/models/knowledge/result.py:143-143; mcp/src/agents_remember/models/knowledge/result.py:151-151 |
| **The node that measures the persisted-nothing property at a later page as well as at the first.** | "test_a_refused_read_leaves_every_table_and_the_logical_digest_unchanged" | mcp/tests/test_knowledge_read_scope.py:1001-1058 |
| **The node that measures a refused read of a real database leaving the file byte-identical.** | "test_a_refused_read_of_a_real_database_leaves_the_file_byte_identical" | mcp/tests/test_knowledge_read_boundaries.py:893-941 |
| The absence nodes, one per absence code. | "test_an_unregistered_path_reports_registration_absence_rather_than_an_empty_scope"; "test_a_selector_naming_no_recorded_identity_is_told_that_the_selector_is_absent" | mcp/tests/test_knowledge_read_scope.py:962-981; mcp/tests/test_knowledge_read_scope.py:982-1000 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-18T07:45:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `66f8b9f0`): **re-read every claim this card carries against the construct as the merged, post-landing line now stands, and advanced the verification stamp to `66f8b9f0` because the body was re-read against the current source.** The engine had reopened 1 claim(s) here (1 x citation_claim_reopened). Each was read at its cited extent: the wording is **retained as it stands**, because the constructs it names still exist and still mean what the card says — what moved was a *range* this leaf's own addition had shifted, together with the payload-model, registry and budget facts the merged line grew. No claim was deleted, softened or dropped from an anchor set, and no range was advanced without a reading.

- 2026-09-17T23:18:00+00:00 — 260915-KS-L11 curator (uncommitted change set on `ar/260915-ks-l11`, base `4904e08f`): recorded the one behavioural change this leaf made to the module — **three factories now carry the operation they refuse for**. `selector_absent_refusal`, `snapshot_unavailable_refusal` and `selection_incomplete_refusal` take an `operation: KnowledgeOperation = _OPERATION` keyword, so the facet selection seam raises the same three codes under `read_facet_scope` through the shared factories rather than a second copy of their wording, while the default leaves every existing caller byte-identical. The body states that the other three factories still name `_OPERATION` unconditionally and that the six-code vocabulary is unchanged. Verification metadata is **not** advanced: the code commit does not exist yet and closeout owns the stamp.

- 2026-09-16T21:50:00+00:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the read's refusal vocabulary. It records the six factories and the three groupings a consumer acts on — **absence** (`selector_absent`, `registration_absent`, a fact about the recorded graph and explicitly not a verdict of "no semantic impact"), **wrong snapshot** (`continuation_binding_mismatch`, `snapshot_unavailable` and the shared codes, none of which returns partial items), and **budget** (`page_budget_too_small`, which reports the exact minimum and leaves the position unchanged) — plus the property that makes "a refused read persisted nothing" structural rather than remembered: the operation only issues `SELECT` on a connection it opened read-only. It also records that a schema this build cannot read surfaces as `snapshot_unavailable` naming both generations rather than as `unsupported_schema`, and that no code in this vocabulary can name a semantic verdict. Verification metadata remains empty until closeout stamps the code commit.
