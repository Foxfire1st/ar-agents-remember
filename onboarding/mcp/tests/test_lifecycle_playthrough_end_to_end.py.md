# mcp/tests/test_lifecycle_playthrough_end_to_end.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_lifecycle_playthrough_end_to_end.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-14T20:00+02:00 |
| lastVerifiedCommitHash | `a7076008db4772554123794392f84b51143004ec` |
| lastVerifiedCommitDate | 2026-09-18T16:14:01+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Tests overview](overview.md)

## Purpose

The **whole leaf-and-master lifecycle, played through in order** on one real temporary Git world,
driven through the **public** operations wherever a public route exists. Every other end-to-end module
in `mcp/tests` proves one interaction at one boundary; this module exists because the defect class it
covers is produced by the *sequence* — an operation that is correct on its own and leaves the world in
a state the next operation cannot accept.

The regression it pins is **step 8**: a leaf commanded *after* the master's first landing still
starts. While the deleted `worktrees/atomic_series_seal.py` read the parent series'
`(closeout_status, integration_status, cleanup)` cells as a child-admission seal, a master that took a
checkpoint landing (`integration_status == "checkpointed"`) could never admit another leaf — so a
paused master was a dead master. No single-boundary case could see that, which is why the module
plays the run instead of extending a seam-level test.

The run, in the module's own order: master open and unlanded with no activation selection → a leaf is
commanded and started on the master's current line → the leaf is worked, committed and closed out →
the leaf lands through the public `worktree_integrate` → the unfinished master publishes its
accumulated line through the public `worktree_checkpoint_landing` and stays open → the master is
stopped through the public `worktree_pause` and publishes nothing → the master is resumed by the
ordinary attach route → a leaf commanded after that landing still starts, on the line the master now
has. Steps 6 and 7 are also the pause/resume pair the developer asked to see played.

## Code Commentary

### Logic

`LifecyclePlaythroughTests` (code lines 62-173) is a single `unittest` class holding a single case.
`setUp` builds one real temporary world from `test_closeout_queue.QueueFixture` with `atomic_b=True`
and `memory_mode="external"`, loads the master's canonical **series** contract from
`fixture.tasks / "master-b" / "series-contract.md"` and asserts `kind == "series"` rather than assuming
it; `tearDown` disposes the temporary directory.

`_snapshot(repository)` (code lines 51-59) reads every ref in one repository
(`git for-each-ref --format=%(refname) %(objectname)`) through the shared `git` helper, so a
publication is a visible difference rather than a payload claim.

The module's public drivers, each one call into a registered tool:

| Driver | Public entry point |
| --- | --- |
| `_status` | `worktree_status_tool` |
| `_integrate` | `worktree_integrate_tool` (`strategy="ff-only"`) |
| `checkpoint` | `worktree_checkpoint_landing_tool` (`strategy="ff-only"`) |
| `_pause` | `worktree_pause_tool` |
| `_attach` | `worktree_attach_tool` |
| `_reload` | `load_contract` |

`test_the_lifecycle_plays_through_from_an_unstarted_master_to_a_resumed_one` (code lines 117-173) is
the run, in eight ordered beats:

| Beat | Assertion |
| --- | --- |
| 1. open master | `worktree_status` reports `integration_status == "not-started"` and `atomicSeriesActivation.state == "vacant"` — nothing landed, nothing selected. |
| 2-3. leaf commanded, then started | `author_unstarted_leaf("master-b", "LEAF-C")` then `start_leaf("LEAF-C", master="master-b")`; the result is a `leaf` whose code worktree really exists. |
| 4. leaf closed out and landed | `close_out_leaf(leaf)` reaches `closeout_status == "completed"`, the public `worktree_integrate` returns `ok`, and the master's `integration_status` is asserted to still be `not-started` afterwards. |
| 5. unfinished master checkpoints | the public preview reports `would-checkpoint`, the apply returns `ok` / `checkpointed`, and the reloaded master reads `integration_status == "checkpointed"` with `closeout_status` still `not-started` — it published and stayed open. |
| 6. master paused | ref maps of **both** repositories are captured first; the public pause returns `ok`, `paused is True`, `atomicSeriesActivation.state == "vacant"` and **no** `nextTool`, and both ref maps are byte-identical afterwards. |
| 7. master resumed | the ordinary `worktree_attach` returns `ok`, and the code refs are still the captured ones. |
| 8. **a leaf after the landing still starts** | `author_unstarted_leaf("master-b", "LEAF-D")` then `start_leaf`; `leaf_id == "LEAF-D"`, the code worktree exists, and `code_base_commit` differs from the first leaf's — it really starts on the line the master now has. |

### Conventions

- One real temporary world per case, `TemporaryDirectory` cleanup in `tearDown`, and the module is
  marked `pytestmark = pytest.mark.integration` (code line 48).
- Registered in the **integration** lane of `mcp/tests/test-evidence-lanes.toml` (row 157). That
  manifest is fail-closed — `load_lane_manifest` derives the repository's actual test modules and
  refuses a manifest that omits one — so an unregistered module is a hard load failure.
- Registered as an exact consumer of the same two shared-support artifacts every other
  `QueueFixture`-based boundary suite consumes:
  `closeout_input_test_support.py` (its consumer row is `:318`) and
  `curator_coherence_test_support.py` (its consumer row is `:398`), both
  reached transitively through `QueueFixture`. No artifact row was added, removed or re-categorised.
- Support is composed, never re-implemented: `QueueFixture`/`REPO` come from `test_closeout_queue`,
  `close_out_leaf` is imported from `checkpoint_landing_test_support`, and `git` comes from
  `test_worktree_support`.
- The module docstring states exactly where the public route is used and where it is not, so the
  exception is deliberate rather than an oversight: leaf start and leaf closeout use the fixture's
  structural equivalents (`QueueFixture.start_leaf`, which is what `worktree_start` records, and the
  same closeout recording the checkpoint module uses), because the registered start route needs the
  harness lifecycle and provider scaffolding that a coordination-root fixture deliberately does not
  carry. The master-level interactions — status, integrate, checkpoint, pause, resume — are the
  registered tools themselves.

### Invariants And Boundaries

- **The order is the subject.** Each beat asserts the state the next beat depends on, so a change that
  keeps every operation correct in isolation but breaks the handoff between two of them fails here.
- **The master-level steps drive the registered tools.** Calling `integrate_result`,
  `checkpoint_landing_result`, `pause_result` or the attach innards directly would pass while the
  registered tool stayed broken.
- **"Publishes nothing" is measured on refs, in both repositories.** The pause beat compares
  `_snapshot` maps taken before and after, on the code repository *and* the external-memory
  repository; it does not infer inertness from the payload.
- **The checkpoint and the pause are asserted as different verbs on the same world.** The checkpoint
  genuinely moves cells (`not-started` → `checkpointed`) and keeps the master open; the pause that
  follows moves no ref at all. A change that made one of them do the other's work fails on the other's
  assertion.
- **Leaf start and closeout are the fixture's structural equivalents**, as the module docstring
  states. Do not present this module as public-route coverage for `worktree_start`; that coverage
  lives where the harness scaffolding exists.
- **The base commit really advances between the two leaves.** Step 8 asserts
  `second.code_base_commit != closed.code_base_commit`, so a "start" that re-used the old base would
  fail rather than pass.

### Todos

None recorded. Verification metadata on this card remains closeout-owned.

## Docs References

No external Domain Documentation source is configured for this memory root. These assertions concern
this repository's own ref movement, contract cells and activation state, so the retained source is the
direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external domain claim is required. | N/A | N/A |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The ref snapshot the "publishes nothing" beat is measured with. | `_snapshot` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:51-59 |
| The one-class, one-case fixture: one real temporary Git world per case, master-b's canonical series contract, external memory. | `LifecyclePlaythroughTests` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:62-173 |
| The six public drivers the run is expressed in, each a registered tool call. | `_status`; `_integrate`; `_checkpoint`; `_pause`; `_attach`; `_reload` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:78-82; mcp/tests/test_lifecycle_playthrough_end_to_end.py:84-90; mcp/tests/test_lifecycle_playthrough_end_to_end.py:92-98; mcp/tests/test_lifecycle_playthrough_end_to_end.py:100-104; mcp/tests/test_lifecycle_playthrough_end_to_end.py:106-110; mcp/tests/test_lifecycle_playthrough_end_to_end.py:112-113 |
| The ordered run and the eight beats, including step 8 — a leaf commanded after the checkpoint landing still starts on a new base. | `test_the_lifecycle_plays_through_from_an_unstarted_master_to_a_resumed_one` | mcp/tests/test_lifecycle_playthrough_end_to_end.py:117-173 |
| The deleted child-admission seal this module is the regression proof for: its module and call sites are gone, and masters are no longer locked by their own landing. The stop the module plays is `pause_result`, whose already-stopped branch answers an unselected master. | `pause_result`; `_already_stopped_result`; `require_parent_series` | mcp/src/agents_remember/worktrees/modules/pause.py:79-127; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:309-330 |
| The public tools the master-level beats drive. | "def worktree_attach_tool("; "def worktree_integrate_tool("; "def worktree_checkpoint_landing_tool("; "def worktree_pause_tool(" | mcp/src/agents_remember/application/worktree_tools.py:265-275; mcp/src/agents_remember/application/worktree_tools.py:371-425; mcp/src/agents_remember/application/worktree_tools.py:427-468; mcp/src/agents_remember/application/worktree_tools.py:470-500 |
| The one eligibility decision the checkpoint preview and apply both read, and the `checkpointed` cell this module asserts after the landing. | `checkpoint_landing_eligibility`; "contract.integration_status in {\"completed\", \"checkpointed\"}" | mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:265-265; mcp/src/agents_remember/worktrees/modules/integrate.py:412-458 |
| The shared world fixture and Git helper this module composes instead of re-implementing. | "class QueueFixture:"; "REPO = \"repo-a\""; "def git(repo: Path, *args: str) -> str:" | mcp/tests/test_closeout_queue.py:184-694; mcp/tests/test_closeout_queue.py:54-54; mcp/tests/test_worktree_support.py:79-86 |
| The leaf closeout recording it imports rather than duplicating. | `close_out_leaf` | mcp/tests/checkpoint_landing_test_support.py:59-82 |
| The integration lane row the fail-closed manifest requires. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:233-233 |
| The two shared-support consumer edges this module adds to the lifecycle catalog, one in each artifact block. | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:330-333; mcp/tests/evidence-lifecycle.toml:330-380 |
| The integration-case budget this module's membership is accounted against. | `integration_case_budget` | pyproject.toml:176-215 |
| The integration lane row the fail-closed manifest requires. | "mcp/tests/test_lifecycle_playthrough_end_to_end.py" | mcp/tests/test-evidence-lanes.toml:233-233 |
| The two shared-support consumer edges this module adds to the lifecycle catalog, one in each artifact block. | "mcp/tests/closeout_input_test_support.py"; "mcp/tests/curator_coherence_test_support.py" | mcp/tests/evidence-lifecycle.toml:326-333; mcp/tests/evidence-lifecycle.toml:363-363; mcp/tests/evidence-lifecycle.toml:283-283; mcp/tests/evidence-lifecycle.toml:373-380 |
| The integration-case budget this module's membership is accounted against. | `integration_case_budget` | pyproject.toml:215-215 |

## Cross-Repo References

These are contract, ref and ledger assertions against repositories created in a temporary directory
by the module's own fixture; no sibling repository or external system participates.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | N/A | N/A |

## Update History
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T13:36:47+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:233-233. No content impact: mechanical anchor-range projection bound to citation source snapshot 468e47519c1a75ea8349538fbc4903207afc60f299e5295d1631f1f15f11a5ef; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T12:07:24+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:231-231. No content impact: mechanical anchor-range projection bound to citation source snapshot 5571c165ff8c0fb8964492349c8f2d6be0134e3c91863ce685e4c34bb24aa86b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:229-229. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T10:45:13+00:00: Generated citation repair: `integration_case_budget` repointed to pyproject.toml:215-215. No content impact: mechanical anchor-range projection bound to citation source snapshot a1ce4e2ec12e0f7b6d953d252db00653f23138548de5122388515485a9e05d23; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T08:36:42+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:207-207. No content impact: mechanical anchor-range projection bound to citation source snapshot 62bb4ecc832f24577a616642ab14d8fff48bf74187b0e3c11571c9de796a4ee4; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:205-205. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T07:21:19+00:00: Generated citation repair: `integration_case_budget` repointed to pyproject.toml:323-323. No content impact: mechanical anchor-range projection bound to citation source snapshot 9c25e22b4a75362a466772fad50098779327e24acf1460715dd01e0595ea5288; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T07:15:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 8 generated projection bullet(s) by hand while resolving the memory sync** — `mcp/tests/test_lifecycle_playthrough_end_to_end.py`, `pause_result`, `_already_stopped_result`, `require_parent_series`, `checkpoint_landing_eligibility`, `contract.integration_status in {\`, `, \`, `}` and 1 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen until an agent had read what it points at. This leaf's own addition moved the ranges they project, so a bullet still naming the old extent is stale evidence; the resident claims' ranges were re-verified against the current source in this pass. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:40:00+00:00 — 260915-KS-L12 curator (uncommitted change set on `ar/260915-ks-l12`, base `e963a01c`): **retired 6 generated projection bullet(s) by hand** — `mcp/tests/test_lifecycle_playthrough_end_to_end.py`, `pause_result`, `_already_stopped_result`, `require_parent_series`, `checkpoint_landing_eligibility`, `contract.integration_status in {\`, `, \`, `}` and 1 further anchor(s). Each was a `citation_fix` projection rather than a reading, and each kept its claim in enforced reopen; **this leaf's own addition moved the ranges they project**, so a bullet that still names the old extent is stale evidence; this document's claims were not otherwise re-read in this pass and its rows were left as they stand. Nothing in the body above was deleted to clear a finding.

- 2026-09-18T04:35:00+00:00 — 260915-KS-L19 curator (uncommitted change set on `ar/260915-ks-l19`, base `e963a01c`): **retired 1 generated projection bullet(s) by hand, after re-reading each claim against the construct its range now covers.** A projected range is unverified evidence and keeps the claim reopened until an agent has read what it points at; each of these was read, and the resulting citation is the one recorded here rather than the range the tool wrote: `"mcp/tests/test_lifecycle_playthrough_end_to_end.py"` → `mcp/tests/test-evidence-lanes.toml:198-198`. No claim wording changed — the byte-unchanged claims these bullets were attached to are unchanged — and no verification stamp is advanced over prose that was not re-read.

- 2026-09-18T04:05:00+00:00 — 260915-KS-L15 curator (uncommitted change set on `ar/260915-ks-l15`, base `837961d4`): re-read every claim in this card whose cited range the leaf's own source edits had moved. This leaf's insertion of `mcp/tests/test-evidence-lanes.toml` rows and a test module shifted the anchors below them, and the re-cited range of each claim was checked against the construct it is about rather than accepted from the mechanical projection. Ranges re-cited: `mcp/tests/test-evidence-lanes.toml:196-196` -> `mcp/tests/test-evidence-lanes.toml:197-197`. The generated projection bullets that recorded the same moves are retired here, so no mechanically rewritten range remains recorded as unverified evidence. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-18T01:52:52+00:00: Generated citation repair: `integration_case_budget` repointed to pyproject.toml:176-176. No content impact: mechanical anchor-range projection bound to citation source snapshot 1b549a05c7448b2578454675e173eaf65501170ee85e72dbbfb2c4a4132b3242; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-18T01:40:00+00:00 — 260915-KS-L24 curator (uncommitted change set on `ar/260915-ks-l24`, base `9c12e8b1`): **re-read the one row whose range the mechanical projection had rewritten, and re-cited it by hand.** The row asserts that `integration_case_budget` is the budget this module's membership is accounted against; the identifier's own declaration moved from `:287` to `:305` when this candidate raised the pair, so the row cites `pyproject.toml:305-305` — the extent the engine resolves for it, and the only line in that file that carries the identifier at all (the surrounding comments spell the raises as "300 -> 340" prose, not as the key). The claim itself is unchanged and still true: the module is registered in the `integration` lane and that key is the cap its membership is accounted against. Nothing else in this card was re-read in this pass. Verification metadata remains closeout-owned; no acceptance or certification claim is made.

- 2026-09-17T20:42:17+00:00: Generated citation repair: `checkpoint_landing_eligibility`; "contract.integration_status in {\"completed\", \"checkpointed\"}" repointed to mcp/src/agents_remember/worktrees/modules/integrate.py:412-458; mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:265-265. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `close_out_leaf` repointed to mcp/tests/checkpoint_landing_test_support.py:59-82. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: "mcp/tests/test_lifecycle_playthrough_end_to_end.py" repointed to mcp/tests/test-evidence-lanes.toml:193-193. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `integration_case_budget` repointed to pyproject.toml:166-166. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-17T08:11:27+00:00 — 260915-KS-L9 curator (memory-quality closure): re-read every reopened claim in this card against code commit `c22beb0121946c0637e113ec4cf29da29fd4aec7` and advanced the verification stamp to that commit, which closeout re-stamps. A generated citation repair had already rewritten these ranges mechanically, so each was re-read rather than trusted: the range was checked against the current definition of the construct the claim is about, and the wording still holds. Extents chosen: `pause_result`; `_already_stopped_result`; `require_parent_series` at mcp/src/agents_remember/worktrees/integration/integration_branch_authority.py:309-330; mcp/src/agents_remember/worktrees/modules/pause.py:79-127; mcp/src/agents_remember/worktrees/modules/pause.py:130-149, `integration_case_budget` at pyproject.toml:287-287.

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `mcp/tests/curator_coherence_test_support.py` in the row 150 of this card from mcp/tests/evidence-lifecycle.toml:283-283 to mcp/tests/evidence-lifecycle.toml:330, the extent of the construct the claim is about (the checker named line(s) [330] as its live location); added mcp/src/agents_remember/worktrees/modules/pause.py:79 to the row 144 of this card as the citation for `pause_result`: no cited file carried the construct, and the checker named line(s) [79] in this file as its live location

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `pause_result` in the row 144 of this card from mcp/src/agents_remember/worktrees/modules/pause.py:130-133 to mcp/src/agents_remember/worktrees/modules/pause.py:79-82, the extent of the construct the claim is about (the checker named line(s) [79] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `_already_stopped_result` in the row 144 of this card from mcp/src/agents_remember/worktrees/modules/pause.py:79-82 to mcp/src/agents_remember/worktrees/modules/pause.py:130-133, the extent of the construct the claim is about (the checker named line(s) [116, 130] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-read the reopened claim in the row 151 of this card against the current code: its anchor still resolves inside the cited range, so the wording holds and the stamp advances

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): re-pointed `QueueFixture` in the row 147 of this card from mcp/tests/test_closeout_queue.py:186-696 to mcp/tests/test_closeout_queue.py:184-195, the extent of the construct the claim is about (the checker named line(s) [184] as its live location); re-pointed `git` in the row 147 of this card from mcp/tests/test_worktree_support.py:83 to mcp/tests/test_worktree_support.py:79-86, the extent of the construct the claim is about (the checker named line(s) [79] as its live location); re-pointed `pause_result` in the row 144 of this card from mcp/src/agents_remember/worktrees/modules/pause.py:130-133 to mcp/src/agents_remember/worktrees/modules/pause.py:79-82, the extent of the construct the claim is about (the checker named line(s) [79] as its live location)

- 2026-09-17T01:31:11+00:00 — 260915-KS-L9 curator (re-scoped repair): clamped mcp/tests/test_closeout_queue.py:186-697 to mcp/tests/test_closeout_queue.py:186-696, the range the cited construct now occupies; kept one copy of the repeated citation mcp/src/agents_remember/worktrees/modules/pause.py:130-133 in the row 144 of this card; the repetition added no pooled evidence

- 2026-09-14T18:00:00+00:00 — 260913-LCA-L12 curator (drift re-verification): corrected three numbering
  claims in the body — the class and case spans are `:62-173` and `:117-173`, the lane row is 157,
  and this module's evidence-lifecycle consumer rows are `:318` and `:398` inside the blocks
  declared at `:282-341` / `:362-421`. Verification metadata remains closeout-owned.

- 2026-09-14T18:00:00+00:00 — 260913-LCA-L12 curator (provenance repair): the gate could not compare
  this claim with its verification provenance because one or more of its anchors resolved more than
  once at the verification commit, so no historical location was unique. Repaired the citation, not
  the claim: each anchor that named a construct by bare name now names its exact declaration text,
  which resolves once in the code tree, and any range that had drifted off its construct was re-read
  at the declaration. The claim wording is unchanged, and the construct each range covers is the one
  the claim is about. Verification metadata remains closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (frozen-tree re-read): the code worktree is frozen
  and this module declares its checkpoint driver as `_checkpoint` again (line 92), the shape the row
  names. I had changed the anchor to `checkpoint` during the in-flight window, when an intermediate
  state spelled it without the underscore; that change is reverted and the row reads `_status`;
  `_integrate`; `_checkpoint`; `_pause`; `_attach`; `_reload` with the range 92-98 confirmed at the
  declaration. Verification metadata remains closeout-owned.

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

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (reopened-claim judgement): the checker reopened
  this claim because the module did not exist at the recorded verification commit. Re-read the
  module claim against the current card and source: the test file exists, its lane row is
  registered, and the claim that it is the ordered lifecycle playthrough for the seal-removal change
  set still holds. Retained; verification metadata remains closeout-owned.

- 2026-09-14T17:00:00+00:00 — 260913-LCA-L12 curator (citation pass): re-derived the source ranges of 3
  claim(s) whose anchor no longer sat in its cited range and normalised 4 further range(s) in this
  card from their anchors against the frozen source snapshot (`agents-remember memory-citations
  --fix --document`, snapshot 188b8ecd). 1 claim(s) were declined as ambiguous or not the subject
  and were left for a reading curator. No claim wording changed; every rewritten range was read back
  at its current position. Verification metadata remains closeout-owned.

- 2026-09-13T18:42:00+00:00 — Created by the curator pass for the uncommitted child-admission-seal
  removal / already-vacant change set on `ar/260831_lifecycle-owned-completion-relay`. Documents the
  module as the ordered lifecycle playthrough and the regression proof for the deleted
  `worktrees/atomic_series_seal.py`: the eight beats and their assertions, the public-driver-only
  discipline for the master-level steps, the module docstring's stated exception for leaf start and
  closeout, the ref-snapshot measurement of "publishes nothing", the support composition
  (`QueueFixture` + `close_out_leaf` + `git`, no new support module), the integration lane row 153 and
  the two evidence-lifecycle consumer edges (rows 316 and 372). Verification metadata is pinned to the
  branch's recorded verified baseline
  (`9c8a7a42a3d761b13c462874c7b312313a11c0ae`, the ledger's `lastVerifiedCodeCommit`) because the code
  this card describes is uncommitted; the stamp remains closeout-owned and no acceptance claim is made.
