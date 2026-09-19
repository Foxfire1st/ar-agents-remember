# mcp/src/agents_remember/models/knowledge/read.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/models/knowledge/read.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T23:50+02:00 |
| lastVerifiedCommitHash | `1ff1893f44d875073d58af863238501a6be35288`|
| lastVerifiedCommitDate | 2026-09-16T23:58:57+02:00|
| reviewedWorkingCandidate | `ar/260915-ks-l07` uncommitted source; base `4eb2b1992f6183fba06e9f31aa664d9a93094c26` |
| governingOverview | `mcp/src/agents_remember/models/overview.md` |

## Governing Overview

[models route overview](../overview.md)

## Purpose

**The whole vocabulary of one selective recorded-scope read: its seeds, its declared snapshot, its page
and its cursor.** This module holds no SQL, no Git resolution and no authority decision; it declares what a
caller may ask for and what a caller is told, and the deciders import it rather than redefining a branch
of it.

## Code Commentary

### Logic

**Four splits are load-bearing, and each one is a place a future edit could silently undo a guarantee:**

1. **Seed versus selection.** `KnowledgeReadSeed` is a closed discriminated union —
   `PathSeed | InvariantIdentitySeed | InvariantRevisionSeed | FamilyIdentitySeed | FamilyRevisionSeed`,
   one member per row of the requirement's table. A seed carries **no filter, no sort, no revision
   preference and no display version**, because none of those may select a record: the only thing that
   narrows a selection is an exact identity the caller named. `EXACT_REVISION_SEED_KINDS` and
   `IDENTITY_SEED_KINDS` name the two kinds whose identity is a revision choice.
2. **Selection versus page.** `KnowledgeReadCounts`'s `primary_items_*` fields describe **one walk**: the
   declared total, the cumulative returned, what remains. All three travel, so a one-item page cannot be
   read as a one-item scope **at any position of the walk** — not only at its first page.
3. **Provenance versus verdict.** Every statement, role, rationale and lifecycle crosses as the authored
   text it is stored as. **Nothing here can carry a current-truth marker, a severity, a ranking or a
   semantic assessment, because the response has no field that could hold one** — which is how the
   requirement's *Forbidden Overreach* is enforced structurally rather than by discipline.
4. **Continuing versus re-binding.** `KnowledgeReadCursor` names the exact snapshot, context, selector,
   policy, manifest and position it continues. A cursor is not a permission to read whatever the path
   holds now: presenting one against another dataset is refused rather than served a page assembled from
   two revisions.

**The declared vocabulary:**

| Declaration | Value / members |
| --- | --- |
| `KNOWLEDGE_READ_POLICY_VERSION` | `"recorded-family-frontier/v1"` — part of a cursor's binding, because a policy change can move the selected set |
| `MAX_PAGE_ITEMS` / `MAX_PAGE_UTF8_BYTES` | 32 / 49152 — declared presentation budgets, never a completeness mechanism |
| `SELECTION_ITEM_LIMIT` | 5000 — the declared execution bound; reaching it refuses rather than emitting invented totals |
| `ItemKind` | `invariant_revision`, `family_revision`, `family_membership`, `realization_claim`, `advertised_family` |
| `AnchorResolutionState` | the owner's seven members: `exact_recorded_blob`, `recorded_blob_mismatch`, `path_absent`, `entry_not_blob`, `recorded_object_unavailable`, `unsupported_locator`, `not_requested` — **unchanged by this leaf** |
| `ReadStage` | `seed_selected`, `invariant_identity`, `invariant_revision`, `family_identity`, `family_revision`, `member_of_selected_family`, `realization_of_selected_revision`, `sibling_membership_in_another_family` |

`KnowledgeReadContext(repository_id, knowledge, repository_root=None, code_tree_id=None, task_ref=None)`
is the whole admission one read has, and it enforces two rules at construction: the selected snapshot must
belong to the named repository namespace, and source resolution needs **both** `repository_root` and
`code_tree_id`. A half-specified resolution is refused rather than answered with `not_requested`, because
that would report a caller's mistake as a fact about a recorded anchor. **`task_ref=None` is a supported
state and not a degraded one**: a baseline read during planning does not need a leaf, an enclosure or a
fabricated task.

`ReadItem` is deliberately **one homogeneous model** with optional kind-specific fields, so a page is one
sequence a caller pages over without discriminating a second union. Every item carries `item_id` and
`selection_reasons`; a `realization_claim` item carries `anchor: AnchorResolution | None`.

### Three model-level invariants a consumer may rely on

These are refused **at construction**, which is why they are guarantees rather than conventions:

- **`KnowledgeReadPage`** refuses to exist with `has_more == enumeration_complete`, or with `has_more`
  disagreeing with the presence of a continuation. **A truncated page cannot be presentable as complete.**
- **`KnowledgeReadCounts`** refuses its own arithmetic contradiction
  (`returned + remaining != total`, or `returned > total`).
- **`KnowledgeReadResult`** refuses to be both a page and a refusal, or neither.

### The cursor format

`KnowledgeReadCursor` (`cursor_format = "knowledge-read-cursor/v1"`) carries `policy_version`,
`context_digest`, `seed_digest`, `manifest_digest`, `logical_digest`, `schema_version` and `position`,
encoded urlsafe-base64 over the model's JSON. **`cursor_for` and `continue_from_cursor` are the only
encoder and decoder**, and a continuation that is not this format's cursor decodes to `None` — the
application turns that into a typed `continuation_binding_mismatch` rather than a raw exception. The field
is named `cursor_format` rather than `schema` because `schema` is a deprecated `BaseModel` attribute and a
field shadowing it makes Pydantic warn on every construction.

`seed_digest(seed)` is the digest binding one seed into a selection identity;
`read_context_digest(context)` seals a context's whole resolved identity;
`snapshot_of_context(context)` returns the one snapshot a page declares, sealed with that digest. The
snapshot's `context_digest` is **derived** and is not canonical database content.

### Conventions

- `PathSeed` applies the same shape rule the stored anchor path applies, through the **one shared**
  `require_plain_git_path`, so a spelling the write path refuses cannot be presented as a seed that is
  answered with an absence.
- The union discriminator is `kind`, and every seed member declares a literal for it, so an unrecognised
  seed is a validation error rather than a silent fallthrough.
- Length ceilings are the ones `base.py` declares, imported rather than restated.

### Invariants And Boundaries

- **A display version never selects a revision, and nothing here can order revisions.** `ReadRevisionGroup`
  reports `record_id` and `selected_revision_count` and nothing else, so seeing one revision on a page
  cannot be read as that identity having one revision.
- **The absence of a verdict field is the guarantee.** No model in this module has a field that could carry
  "current", "accepted", "severity" or "ranked"; adding one is an owner decision and not a leaf edit.
- **A cursor is a binding.** Every field it carries is checked against the read it is presented to; the
  model itself makes the cursor unforgeable only in the sense that it cannot omit a binding.
- **Boundary.** This module declares. It holds no policy execution, no SQL, no Git call and no authority.

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
| **The closed seed union: five members, one per row of the requirement's table, carrying no filter, sort or display version.** | `KnowledgeReadSeed`; `PathSeed`; `InvariantIdentitySeed`; `InvariantRevisionSeed`; `FamilyIdentitySeed`; `FamilyRevisionSeed` | mcp/src/agents_remember/models/knowledge/read.py:204-213; mcp/src/agents_remember/models/knowledge/read.py:144-201 |
| **The read context and its two construction rules** (one namespace, and an all-or-nothing source resolution), with `task_ref=None` a supported state. | `KnowledgeReadContext` | mcp/src/agents_remember/models/knowledge/read.py:216-263 |
| The declared policy version, budgets and execution bound. | `KNOWLEDGE_READ_POLICY_VERSION`; `MAX_PAGE_ITEMS`; `MAX_PAGE_UTF8_BYTES`; `SELECTION_ITEM_LIMIT`; `KnowledgeReadBudget` | mcp/src/agents_remember/models/knowledge/read.py:84-96; mcp/src/agents_remember/models/knowledge/read.py:266-275 |
| **The correction this leaf's review sealed: the counts describe one walk, and the model refuses its own arithmetic contradiction.** | `KnowledgeReadCounts` | mcp/src/agents_remember/models/knowledge/read.py:404-448 |
| **The page that cannot present a truncation as complete, and the result that is a page or a refusal and never both.** | `KnowledgeReadPage`; `KnowledgeReadResult` | mcp/src/agents_remember/models/knowledge/read.py:451-482; mcp/src/agents_remember/models/knowledge/read.py:485-511 |
| **The cursor's binding fields, and the only encoder/decoder pair.** | `KnowledgeReadCursor`; `cursor_for`; `continue_from_cursor` | mcp/src/agents_remember/models/knowledge/read.py:514-531; mcp/src/agents_remember/models/knowledge/read.py:561-579; mcp/src/agents_remember/models/knowledge/read.py:582-588 |
| The one homogeneous item model, the anchor observation and the advertised frontier entry. | `ReadItem`; `AnchorResolution`; `AdvertisedExpansion`; `SelectionReason`; `ReadRevisionGroup`; `DirectlyContainingFamily` | mcp/src/agents_remember/models/knowledge/read.py:363-401; mcp/src/agents_remember/models/knowledge/read.py:345-360; mcp/src/agents_remember/models/knowledge/read.py:331-342; mcp/src/agents_remember/models/knowledge/read.py:312-316; mcp/src/agents_remember/models/knowledge/read.py:319-328; mcp/src/agents_remember/models/knowledge/read.py:300-309 |
| The seven-member anchor vocabulary this leaf did **not** extend. | `AnchorResolutionState`; `ANCHOR_RESOLUTIONS` | mcp/src/agents_remember/models/knowledge/read.py:112-130 |
| The digest binding one seed into a selection identity. | `seed_digest` | mcp/src/agents_remember/models/knowledge/read.py:534-537 |
| The digest sealing one read context's whole resolved identity. | `read_context_digest` | mcp/src/agents_remember/models/knowledge/read.py:555-558 |
| The one snapshot a page declares, sealed with that digest. | `snapshot_of_context` | mcp/src/agents_remember/models/knowledge/read.py:540-552 |
| **The nodes that measure the model invariants themselves: the corrected page arithmetic and the truncated page's honesty.** | "test_a_truncated_page_states_that_items_remain_rather_than_claiming_completeness"; "test_a_page_budget_of_one_item_still_advertises_the_second_location" | mcp/tests/test_knowledge_read_scope.py:838-871; mcp/tests/test_knowledge_read_scope.py:547-657 |
| The shared path-shape rule this module's seed applies. | `require_plain_git_path` | mcp/src/agents_remember/models/knowledge/base.py:59-92 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-16T23:50+02:00 — 260915-KS-L7 curator (uncommitted change set on `ar/260915-ks-l07`, base `4eb2b199`): created this one-to-one card for the read's typed vocabulary. It records the **four load-bearing splits** (seed versus selection — a seed carries no filter, sort, revision preference or display version; selection versus page — the three `primary_items_*` fields describe one walk so a one-item page cannot be read as a one-item scope at any position; provenance versus verdict — **the response has no field that could hold a current-truth marker, a severity or a ranking**, which is how the requirement's *Forbidden Overreach* is enforced structurally; and continuing versus re-binding), the **three model-level invariants a consumer may rely on** (a page cannot present a truncation as complete, the counts cannot contradict their own arithmetic, and a result is a page or a refusal and never both), the declared policy version, budgets, execution bound and the seven-member anchor vocabulary this leaf did **not** extend, and the cursor's binding fields with the one encoder/decoder pair. It also records that `task_ref=None` is a supported baseline state rather than a degraded one, and that the seed path applies the one shared path-shape rule. Verification metadata remains empty until closeout stamps the code commit.
