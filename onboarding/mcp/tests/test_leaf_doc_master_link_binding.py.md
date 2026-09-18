# mcp/tests/test_leaf_doc_master_link_binding.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_leaf_doc_master_link_binding.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec`|
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

Proves, on real repositories, that a leaf task document authored **before** its master's series contract
exists acquires its derived master link when the leaf is started — and that the authoring plane refuses
the one case nothing would ever repair.

Planning a master necessarily authors its leaf documents before the master's first `worktree_start`
bootstraps the series contract. At authoring time `task_doc` cannot stamp the two derived fields
(`seriesContractPath`, `enclosures[]`), so start is the only place they can ever be bound. This module
pins both halves of that fix together: the bind-at-start half and the fail-closed half, because either
alone is wrong — binding without the refusal leaves an unrepairable silent drop, and refusing without the
binding makes the normal planning flow impossible.

The restamp's own decision table is covered on the unit population in
`test_task_document_application_1.py` (`LeafDocMasterLinkBindingTests`); this module is the end-to-end
proof over a real coordination root, code repository and Git-backed memory repository.

## Code Commentary

### Logic

One scratch coordination root, one code repository and one external memory repository per case, built in
`setUp` (`:45-66`) from `init_repo`, `initialized_memory_repo` and a real `McpRuntimeConfig`. The task root
is `tasks/repo-a/260624_master/`.

`_author_master` (`:78-93`) and `_author_leaf` (`:95-108`) author both documents through the real
`task_doc_tool`; `_write_leaf_document` (`:110-141`) instead authors the pre-contract document state
directly, giving the master its live row for the leaf first (that row is what start proves leaf identity
against) while deliberately withholding the series contract and the two derived fields. `_start_leaf`
(`:143-159`) drives the real public `worktree_manager.start_result` with `skip_provider_setup=True` and
`memory_mode="disabled"`.

The four cases:

- `test_leaf_authored_before_its_series_contract_gets_its_link_at_start` (`:163-195`) is the exact sequence
  that produced this master's own first leaf with `seriesContractPath: None`. It asserts the precondition
  rather than assuming it — `series_contract_path(task_root).exists()` is false and the authored document
  carries `seriesContractPath is None` and `enclosures == []` — then starts the leaf and asserts the
  document now carries the series contract path, the one `enclosures[]` ref naming the real enclosure
  contract, and the stamped `lifecycleId`.
- `test_an_existing_damaged_document_is_repaired_by_its_next_start` (`:197-233`) is the already-damaged
  case: the document exists with `lifecycleId="LC-OLD"` and no link, and its authored content (title,
  objective, requirements, steps) must survive the repair. Start binds the link, follows the fresh
  lifecycle `LC-REPAIR`, and changes nothing else — asserted field by field.
- `test_authoring_a_leaf_with_no_master_document_is_refused_with_its_remedy` (`:235-250`) is the fail-closed
  half: with no series contract and no master document in the task root, authoring the leaf raises
  `TaskDocError` whose message names `seriesContractPath`, the exact missing master `task.json` path and the
  remedy, and no leaf document is written.
- `test_authoring_a_master_and_its_leaves_before_any_start_still_succeeds` (`:252-268`) is the counter-case
  that keeps the planning flow usable: master first, then two leaves, no start anywhere. Both leaves are
  still unstamped (`seriesContractPath` `None`, `enclosures` empty, `lifecycleId` `None`) — the documented,
  repairable state the first case proves start binds — and both master rows exist.

### Conventions

The module authors documents through the real `task_doc` plane wherever the plane is the subject, and only
falls back to `write_task_doc` for the pre-contract state the plane is forbidden to produce. `LEAF_ID`
(`15_leaf`) is the enclosure leaf id and `LEAF_DOC_ID` (`15`) the authored document id, which keeps the
case-insensitive lookup path in play rather than accidentally matching on identical strings.

The module is a registered consumer of `mcp/tests/closeout_input_test_support.py` and
`mcp/tests/curator_coherence_test_support.py` in `mcp/tests/evidence-lifecycle.toml` (consumer rows `:315`
and `:373`), both reached transitively through `test_worktree_support`'s `initialized_memory_repo`, which
imports both. Consumer declarations are ownership accounting only; they are not execution or acceptance
evidence. The module is registered in the **integration** lane of `mcp/tests/test-evidence-lanes.toml`
(entry row `:152`) by the same change set that created it: it drives a real worktree start over real
temporary Git repositories, so that is its behaviour-preserving lane.

### Invariants And Boundaries

- The precondition assertions are load-bearing, not decoration: without them the case would still pass if
  authoring quietly started stamping the fields, and the module would stop proving anything about start.
- The repair is asserted to be **additive**: fresh lifecycle yes, but objective, requirements, steps and
  title must be unchanged, so a repair that rewrote the authored document would fail here.
- The refusal case asserts the message's substance (the missing link's field names, the exact master path,
  the remedy) and that nothing was written, rather than matching one phrasing verbatim.
- These are focused development cases over disposable repositories. They are behavior evidence for one
  route, not full-suite certification or independent review, and this card records source inspection, not a
  test run.

### Todos

None recorded. The module deliberately does **not** cover the false premise that survived in
`restamp_leaf_doc_lifecycle`'s docstring — that function has no caller in `mcp/src` at all (see the
`tasks/leaf_doc.py` card), so there is no route to exercise; the live publisher is covered through start.

## Docs References

No Domain Documentation source is configured for this repository; the proving evidence is this
repository's own source, the real `task_doc` plane and real Git objects.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external source is required for this repository-owned binding proof. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The pre-contract authoring path and the exact sequence that lost the master link: master and leaf authored through `task_doc` with no series contract, then started. | `test_leaf_authored_before_its_series_contract_gets_its_link_at_start`; `_author_master`; `_author_leaf`; `_start_leaf` | mcp/tests/test_leaf_doc_master_link_binding.py:78-93; mcp/tests/test_leaf_doc_master_link_binding.py:95-108; mcp/tests/test_leaf_doc_master_link_binding.py:143-159; mcp/tests/test_leaf_doc_master_link_binding.py:163-195 |
| The repair path for an already-damaged document, asserted additive (authored content unchanged). | `test_an_existing_damaged_document_is_repaired_by_its_next_start`; `_write_leaf_document` | mcp/tests/test_leaf_doc_master_link_binding.py:110-141; mcp/tests/test_leaf_doc_master_link_binding.py:197-233 |
| The fail-closed half: a leaf under a task root with no master document is refused with its remedy and writes nothing. | `test_authoring_a_leaf_with_no_master_document_is_refused_with_its_remedy` | mcp/tests/test_leaf_doc_master_link_binding.py:235-250 |
| The counter-case that keeps planning usable: master plus two leaves before any start, still unstamped. | `test_authoring_a_master_and_its_leaves_before_any_start_still_succeeds` | mcp/tests/test_leaf_doc_master_link_binding.py:252-268 |
| The refusal this module asserts, with its remedy text. | `_require_bindable_leaf_authoring` | mcp/src/agents_remember/application/task_docs/task_doc_tools.py:619-649 |
| The start publisher that binds the missing link, entered from the real start path. | "def _publish_leaf_task_enclosure_binding(" | mcp/src/agents_remember/worktrees/modules/start.py:858-933 |
| The worktree-side wrapper that resolves the canonical parent row and delegates to the task-domain planner. | "def plan_current_leaf_enclosure_registration(" | mcp/src/agents_remember/worktrees/task_leaf_binding.py:178-202 |
| The task-domain planner that decides whether the derived master link is bound. | "def plan_leaf_doc_enclosure_registration(" | mcp/src/agents_remember/tasks/leaf_doc.py:332-391 |
| The focused restamp decision-table class in the sibling module, which this module's docstring points at. | `LeafDocMasterLinkBindingTests` | mcp/tests/test_task_document_application_1.py:577-663 |
| The two artifact rows that declare this module as an exact consumer, both through `test_worktree_support`. | "path = \"mcp/tests/closeout_input_test_support.py\""; "path = \"mcp/tests/curator_coherence_test_support.py\"" | mcp/tests/evidence-lifecycle.toml:283-283; mcp/tests/evidence-lifecycle.toml:363-363; mcp/tests/evidence-lifecycle.toml:326-333; mcp/tests/evidence-lifecycle.toml:373-380 |
| The transitive importer that makes the module a consumer of both supports. | `initialized_memory_repo` | mcp/tests/test_worktree_support.py:364-392 |
| The integration lane row the fail-closed manifest requires. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:230-230 |
| The transitive importer that makes the module a consumer of both supports. | `initialized_memory_repo` | mcp/tests/test_worktree_support.py:364-366 |
| The integration lane row the fail-closed manifest requires. | "mcp/tests/test_leaf_doc_master_link_binding.py" | mcp/tests/test-evidence-lanes.toml:230-230 |

## Cross-Repo References

Each case builds both repositories it spans — a code repository and an external memory repository — as real
temporary Git repositories, which is what lets `worktree_start` run at all. No production
cross-repository authority is claimed by this focused module.

| Finding | Anchor | Source |
| --- | --- | --- |
| The external-memory side of each case is a real second repository created by the fixture, not a mock. | `init_repo`; `initialized_memory_repo` | mcp/tests/test_worktree_support.py:364-392 |

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:230-230. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:230-230. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:228-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:228-228. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:226-226. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:204-204. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:202-202. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 8 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_leaf_doc_master_link_binding.py`, `init_repo`, `initialized_memory_repo`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 5 generated projection bullet(s) by hand** — `mcp/tests/test_leaf_doc_master_link_binding.py`, `init_repo`, `initialized_memory_repo`. Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_leaf_doc_master_link_binding.py"` → `mcp/tests/test-evidence-lanes.toml:195-195`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:193-193` -> `mcp/tests/test-evidence-lanes.toml:194-194`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T20:42:17+00:00: Generated citation repair: `initialized_memory_repo` repointed to mcp/tests/test_worktree_support.py:364-392. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_leaf_doc_master_link_binding.py" repointed to mcp/tests/test-evidence-lanes.toml:190-190. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/tests/test_worktree_support.py:364 to the row 126 of this card as the citation for `initialized_memory_repo`: no cited file carried the construct, and the checker named line(s) [364, 757] in this file as its live location; added mcp/tests/test_worktree_support.py:364 to the row 137 of this card as the citation for `initialized_memory_repo`: no cited file carried the construct, and the checker named line(s) [364, 757] in this file as its live location

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): added mcp/tests/test_worktree_support.py:364-366 to the row 126 of this card as the citation for `initialized_memory_repo`: no cited file carried the construct, and the checker named line(s) [364, 757] in this file as its live location; re-pointed `initialized_memory_repo` in the row 137 of this card from mcp/tests/test_worktree_support.py:93-94 to mcp/tests/test_worktree_support.py:364-366, the extent of the construct the claim is about (the checker named line(s) [364, 757] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `init_repo` in the row 137 of this card from mcp/tests/test_worktree_support.py:364-366 to mcp/tests/test_worktree_support.py:93-94, the extent of the construct the claim is about (the checker named line(s) [93, 160, 367] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `initialized_memory_repo` in the row 137 of this card from mcp/tests/test_worktree_support.py:93-94 to mcp/tests/test_worktree_support.py:364-366, the extent of the construct the claim is about (the checker named line(s) [364, 757] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): kept one copy of the repeated citation mcp/tests/test_worktree_support.py:93-94 in the row 137 of this card; the repetition added no pooled evidence

- 2026-09-14T18:00:00+00:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because two of its three anchors appeared in both a
  definition and an import in their own files, so no historical location was unique. Repaired the
  citation, not the claim: the row is now three rows, each naming one exact declaration, so the
  publisher, the worktree-side wrapper and the task-domain planner each resolve once. Verification
  metadata remains closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (flag resolved): the code worktree is frozen, so
  the earlier flag is now measured rather than conditional. `mcp/tests/evidence-lifecycle.toml`
  carries the inserted `checkpoint_landing_test_support.py` artifact block at `:342-361`, which
  leaves `path = "mcp/tests/curator_coherence_test_support.py"` at `:363` — the position this row
  already cites — and `path = "mcp/tests/closeout_input_test_support.py"` at `:283`. The pair
  `283-283` / `363-363` is confirmed against the frozen tree, and the flag above stands as the
  record of the interim state it described. Verification metadata remains closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (drift re-verification): this row cites the
  curator-coherence artifact path at `mcp/tests/evidence-lifecycle.toml:363`, which is its position
  in the current working tree, where the in-flight `checkpoint_landing_test_support.py` artifact
  block sits above it. The committed HEAD still carries that path at `:343`; the two forms differ
  only by that uncommitted insertion, so the citation is correct for the tree this leaf is being
  curated against and must be re-measured if the insertion does not land. Flagged rather than
  silently chosen; verification metadata remains closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 2
  claim(s) whose anchor no longer sat in its cited range and normalised 5 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). No claim wording changed; every rewritten range was read
  back at its current position. Verification metadata remains closeout-owned.

- 2026-09-14T05:05:00+00:00 — 260913-LCA-L5 curator (uncommitted change set on `ar/260913-lca-l5-ar`, base
  `52875e7a`): created this one-to-one sidecar for the leaf's new integration module. Recorded the exact
  sequence the leaf exists for (author master and leaf through `task_doc` with no series contract, then
  start the leaf), the case-by-case proof shape — precondition asserted rather than assumed, repair asserted
  additive, refusal asserted by message substance plus no write, planning counter-case — and the two
  ownership facts the registration carries: registered in the integration lane at
  `mcp/tests/test-evidence-lanes.toml:152`, and declared an exact consumer of
  `closeout_input_test_support.py` (`:315`) and `curator_coherence_test_support.py` (`:373`) through
  `test_worktree_support`'s `initialized_memory_repo`, which imports both. Verification metadata is
  intentionally blank: the candidate is uncommitted and no commit contains this file yet, so closeout owns
  the stamp; no execution or acceptance claim.
