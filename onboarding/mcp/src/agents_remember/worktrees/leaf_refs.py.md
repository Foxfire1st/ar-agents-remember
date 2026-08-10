# mcp/src/agents_remember/worktrees/leaf_refs.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/worktrees/leaf_refs.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T09:20+02:00 |
| lastVerifiedCommitHash | `a84add4c9422b18a26f1748dedaed16194994ded` |
| lastVerifiedCommitDate | 2026-08-10T05:11:18+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[mcp/overview.md](../../../overview.md)

## Purpose

`leaf_refs.py` is the dedicated task-tree leaf identity resolver. It validates user-provided leaf refs,
accepts canonical qualified ids, task document ids, and unambiguous legacy stems/slugs, and returns the
canonical identities each write surface persists.

## Code Commentary

### 260707-HFX2-L17 Resolution Guidance Channel

`LeafRefResolutionError` accepts optional guidance and appends it to the stable expected-form and
candidate diagnostics. The pair-binding validator uses this only for a proven legacy role suffix;
ordinary missing/ambiguous leaf behavior and status classification are unchanged.

### Logic

`resolve_leaf_ref(coordination_root, repo_name, ref, task_name, parent_task)` parses refs in the expected
`<repo>/<master-folder>/<doc-id>` form or as an unqualified legacy/doc-id value. It resolves the repository
scope, indexes active task roots from `task_resolver.py`, builds aliases from master subtask rows,
standalone/light `task.json` docs, sibling leaf task docs, file stems, slugs, and enclosure ids, then
returns `ResolvedLeafRef` with both the qualified catalog identity and the doc id used by worktree
contracts.

Candidate enumeration and candidate *building* are now separate (260731-EFA-L2). Two generators
yield `(doc id, alias seeds)` and know nothing about qualification or dedup:
`_root_document_leaves(root_doc, task_root)` — a master root names its sub-task leaves (number +
file stem + file), a leaf root names only itself (id + slug + folder name + enclosure leaf ids);
and `_declared_leaves(task_root)` — the root `task.json` through that helper, then every
marker-bearing sibling leaf document beside it. `_leaf_candidates_for_root` consumes the stream:
it strips each id, skips empties, qualifies as `<repo>/<task-root>/<doc-id>`, unions the alias set
per qualified id, and returns `_LeafCandidate`s sorted by lowercase qualified id. The alias sets
and the sort order are unchanged; the local `add_candidate` closure is gone.

Candidate indexing identifies task-document JSON by the raw `schema: ar-task-document/v1` marker before
model validation. Sibling JSON artifacts without that marker are ignored; malformed or unreadable
non-task JSON siblings are skipped as inert artifacts, while marker-bearing malformed task documents
still run through `read_task_doc` and fail loudly.

`LeafRefResolutionError` is the loud failure surface for no-match and ambiguous refs. Its message names the
expected form and candidate qualified ids, and its `status` is either `leaf-ref-not-found` or
`leaf-ref-ambiguous` for API/tool adapters.

### 260731-EFA-L4: `status` is a declared wire vocabulary, not a bare string

The two members are now the module-level alias `LeafRefStatus = Literal["leaf-ref-not-found",
"leaf-ref-ambiguous"]`, with `VALID_LEAF_REF_STATUSES: frozenset[LeafRefStatus] =
frozenset(get_args(LeafRefStatus))` derived from it rather than retyped beside it, and
`LeafRefResolutionError.__init__` annotates the assignment `self.status: LeafRefStatus = ...`.

**This module is the alias's only producer, and that is why it is declared here.**
`mcp.tools.leaf_ref.leaf_ref_refusal_payload` (the terminal-side adapter, used by
`attach_terminal_session_to_leaf` and `spawn_agent_session`) and
`modules.leaf_ref_start.invalid_leaf_ref_result` (the worktree-start adapter) both copy
`error.status` verbatim into whichever tool refused, so `models.terminal` folds `LeafRefStatus`
into both `LeafAssignmentStatus` and `SpawnAgentSessionStatus` — `Literal` flattens nested aliases,
so the published enums are unchanged — instead of keeping hand-written copies of the same two
members. A
hand-written second copy is exactly what drifts: the response model rejects a value the producer
emits, and the resulting pydantic `ValidationError` escapes an MCP tool handler that has no
`except` for it. Adding a resolution failure mode means adding a member here, and the wire models
inherit it.

`resolve_leaf_enclosure_contract_for_ref()` is the compatibility bridge for worktree contract loading. It
first resolves aliases through the same task tree, then tries existing enclosure directories in canonical
doc-id and legacy forms. If the task tree cannot prove a unique alias, it falls back to the raw legacy
enclosure path so old contracts remain loadable.

`canonical_leaf_doc_ids(repo_name, task_root)` (260712-PTS-L1) returns the frozen set of doc ids provable
for one task root through one bounded `*.json` scan of that root — never the whole tasks tree. It is the
heal's cheap-skip index: `worktree_contract.heal_contract_leaf_ids` consults it (cached per root) so a
leaf contract whose `leaf_id` already is one of these ids is classified canonical without any resolution
walk. `repo_name` only shapes the internal qualified ids, never the returned doc ids.

### Invariants And Boundaries

- Terminal catalog assignments and spawn provenance persist `ResolvedLeafRef.qualified_id`.
- Worktree contracts persist `ResolvedLeafRef.doc_id`.
- `LeafRefStatus` is declared here and imported by the wire models; it is never retyped at a
  response boundary. `VALID_LEAF_REF_STATUSES` is derived from it with `get_args`, so a member can
  only ever be added in one place.
- Missing optional master `task.json` files and sibling non-task JSON artifacts are skipped; malformed
  non-task JSON artifacts are tolerated for boot safety, but malformed
  marker-bearing task documents are not swallowed.
- `task_resolver.py` owns task roots and raw contract paths; this module owns leaf-ref matching and
  candidate policy.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Task-root and raw contract path helpers imported by this resolver. | "def series_contract_path" | mcp/src/agents_remember/worktrees/task_resolver.py:47-47 |
| Worktree start adapter returning doc ids or command refusals. | "def resolve_start_leaf_doc_id" | mcp/src/agents_remember/worktrees/modules/leaf_ref_start.py:15-15 |
| Worktree contract WRITES and the explicit `heal_contract_leaf_ids` sweep normalize legacy `leaf_id` values through this resolver; since 260712-PTS-L1 contract reads never call into this module. | "def heal_contract_leaf_ids" | mcp/src/agents_remember/worktrees/worktree_contract.py:480-480 |
| The heal consumes `canonical_leaf_doc_ids` as its per-task-root cheap-skip index. | "canonical_leaf_doc_ids(contract.repo_name, task_root)" | mcp/src/agents_remember/worktrees/worktree_contract.py:517-517 |
| Terminal serving adapter persists qualified catalog keys from this resolver. | "def resolve_catalog_leaf_key" | mcp/src/agents_remember/serving/leaf_ref_validation.py:18-18 |
| `LeafAssignmentStatus` and `SpawnAgentSessionStatus` fold in the `LeafRefStatus` alias declared here rather than restating its two members. | "LeafAssignmentStatus = Literal["; "SpawnAgentSessionStatus = Literal[" | mcp/src/agents_remember/models/terminal.py:21-21; mcp/src/agents_remember/models/terminal.py:47-47 |
| `leaf_ref_refusal_payload` copies `LeafRefResolutionError.status` onto the terminal-tool refusal verbatim. | `leaf_ref_refusal_payload` | mcp/src/agents_remember/mcp/tools/leaf_ref.py:18-35 |
| Focused resolver tests pin accepted forms, ambiguity, no-match candidates, missing optional master docs, schema-marked malformed doc failures, sibling artifact skips, read-path contract tolerance, and light-task indexing. | `LeafRefResolutionTests` | mcp/tests/test_leaf_ref_resolution.py:103-464 |

## Update History

- 2026-08-02T17:36:56+02:00 — 260731-EFA-L6 curator W1-B09: repaired 14 citation finding(s); scoped recheck clean.

- 2026-08-01T09:20+02:00 — 260731-EFA-L4 curator: the card said `LeafRefResolutionError.status` is
  "either `leaf-ref-not-found` or `leaf-ref-ambiguous`", which was true but no longer the whole
  fact: those two members are now the exported alias `LeafRefStatus = Literal[...]`, the assignment
  in `__init__` is annotated `self.status: LeafRefStatus = ...`, and `VALID_LEAF_REF_STATUSES` is
  derived from it with `get_args` (new `from typing import Literal, get_args`). Added the section
  recording that this module is the alias's only producer and that `models.terminal` folds it into
  `LeafAssignmentStatus` and `SpawnAgentSessionStatus` rather than restating the members — verified
  by reading both unions, which each embed `LeafRefStatus` directly. Named both copying adapters:
  `mcp.tools.leaf_ref.leaf_ref_refusal_payload` for the terminal tools and
  `modules.leaf_ref_start.invalid_leaf_ref_result` for worktree start. Added the one-declaration
  invariant and two reference rows. Resolution behaviour, candidate policy, the L2 generators and
  `canonical_leaf_doc_ids` are untouched by this leaf. Verification metadata pinned until closeout
  stamps the L4 commit.
- 2026-07-31T00:00+02:00 — 260731-EFA-L2 (gate honesty, `C901`/`PLR0912` armed with no
  exemptions): candidate enumeration was extracted from `_leaf_candidates_for_root` into the
  generators `_declared_leaves(task_root)` and `_root_document_leaves(root_doc, task_root)`, and the
  local `add_candidate` closure was replaced by the qualification/dedup loop in the caller. Alias
  sets, qualified ids and sort order are unchanged. Verification metadata pinned until closeout
  stamps the L2 commit.
- 2026-07-12T19:55+02:00 — 260712-PTS-L1: added `canonical_leaf_doc_ids(repo_name, task_root)`, the
  bounded one-scan per-task-root doc-id index the contract heal uses as its cheap-skip. Resolution
  behavior is unchanged; contract READS no longer reach this module at all (leaf-id normalization moved
  to write-time plus the explicit heal in `worktree_contract.py`). Verification metadata pinned until
  closeout stamps the 260712-PTS-L1 commit.
- 2026-07-10T15:07+02:00 — 260707-HFX2-L17: added an optional error-guidance channel so legacy
  role-suffixed refs can name the canonical leaf-plus-role replacement without changing resolution.

- 2026-07-08T23:59+02:00 — 260707-HFX2-L8 (minimal projection robustness): `_has_task_doc_schema_marker`
  now tolerates malformed/unreadable non-task JSON siblings while preserving loud failures for
  marker-bearing task documents, allowing the current active-task corpus to boot with artifact JSON
  beside task docs. Verification metadata pinned until closeout stamps the 260707-HFX2-L8 commit.
- 2026-07-07T23:45+02:00 — 260707-HFX-L4R2: candidate indexing now screens JSON siblings by the
  raw task-document schema marker before validation, ignores legitimate non-task JSON artifacts, keeps
  marker-bearing malformed task docs loud, and indexes standalone/light `task.json` docs as leaf
  candidates with slug, folder, and enclosure aliases. Verification metadata pinned until closeout stamps
  the 260707-HFX-L4 commit.
- 2026-07-07T20:50+02:00 — 260707-HFX-L4: created as the dedicated qualified leaf-ref validation and
  normalization module, split out from task-root/contract path resolution. Verification metadata pinned
  until closeout stamps the 260707-HFX-L4 commit.
