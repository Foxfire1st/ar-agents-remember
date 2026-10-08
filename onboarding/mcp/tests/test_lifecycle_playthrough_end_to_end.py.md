# mcp/tests/test_lifecycle_playthrough_end_to_end.py

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

## Evidence

### Docs References

No external Domain Documentation source is configured for this memory root. These assertions concern
this repository's own ref movement, contract cells and activation state, so the retained source is the
direct evidence.

No external domain claim is required.

### Repo-Internal References

- The ref snapshot the "publishes nothing" beat is measured with. [1]
- The one-class, one-case fixture: one real temporary Git world per case, master-b's canonical series contract, external memory. [2]
- The six public drivers the run is expressed in, each a registered tool call. [3]
- The ordered run and the eight beats, including step 8 — a leaf commanded after the checkpoint landing still starts on a new base. [4]
- The deleted child-admission seal this module is the regression proof for: its module and call sites are gone, and masters are no longer locked by their own landing. The stop the module plays is `pause_result`, whose already-stopped branch answers an unselected master. [5]
- The public tools the master-level beats drive. [6]
- The one eligibility decision the checkpoint preview and apply both read, and the `checkpointed` cell this module asserts after the landing. [7]
- The shared world fixture and Git helper this module composes instead of re-implementing. [8]
- The leaf closeout recording it imports rather than duplicating. [9]
- The integration lane row the fail-closed manifest requires. [10]

- The lifecycle catalog lists this suite under checkpoint-landing and curator-coherence shared support. [11]

- The integration-case budget this module's membership is accounted against. [12]
- The integration lane row the fail-closed manifest requires. [13]
- The two shared-support consumer edges this module adds to the lifecycle catalog, one in each artifact block. [14]
- The integration-case budget this module's membership is accounted against. [15]

### Cross-Repo References

These are contract, ref and ledger assertions against repositories created in a temporary directory
by the module's own fixture; no sibling repository or external system participates.

No meaningful cross-repo references found.
