# mcp/tests/test_knowledge_review_comparison_generation.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The **production-composition evidence for `ICR-R11@v1`**: one frozen comparison survives restart,
worktree cleanup and Git object reclamation. The packet names the one non-conforming shape directly — a
manifest that stores only a digest of already-deleted SQLite bytes — and these fifteen cases measure that
through the real production composition, never through a preconstructed payload: a real enclosure
contract on disk, a real linked worktree with staged, unstaged and untracked content, the real resolution
and capture owners, the real comparison, the real storage snapshot owner and a **real Git object store**.

Three measurements together make the first case the packet's journey rather than a re-read of what the
implementation just wrote (`:336-387`): a written-and-pruned **control object** proves `git gc
--prune=now` really reclaimed something in this run, so the candidate tree's survival is attributable to
the recorded pin rather than to a reclamation that did nothing; the fixture's whole worktree group —
worktree, live datasets and stage — is removed; and the reopen happens in a **child process** that shares
no state with the one that froze the comparison (`_reopen_in_a_new_process`, `:279-315`, running the
inline `_CHILD_REOPEN` program at `:102-164`).

The module's docstring states the load-bearing properties one case each; the header lists all fifteen.

## Code Commentary

### Logic

The manifest-binding case expects the ordinary producer's actual R14/currentness inputs and explicit assessment availability. It still compares exact owner identities and preserves zero records when the authority is unavailable. The adjustment is grouped assertions inside the existing case, not a new case or a relaxation of source/knowledge custody.

**The fixture is shared with the sibling review suite, not rebuilt.** `comparison_fixture` (`:168-171`)
calls `build_endpoint_fixture` imported from `test_knowledge_review_source_endpoints` — the R01
production-composition fixture — so these cases measure the *same* real enclosure, worktree and capture
path the source-endpoint cases measure rather than a second, drifting one. The two Git-truth helpers are
taken from the shipped scope-test support (`_git`, `BATCH_PATH`, `BATCH_PATH_CANDIDATE_TEXT`), and the
file whose candidate bytes are read back (`CANDIDATE_CONTENT_PATH`) is the one the fixture edits
**without staging it**, so its content exists in no commit and only the pin keeps it.

**`_freeze` (`:174-185`) requires a published generation.** Every journey case starts from a freeze that
asserted `state == "published"` and carries the refusal as its message, so a case can never silently
measure a refusal path while claiming to measure retention.

**The child process is a real restart.** `_CHILD_REOPEN` imports the package from the worktree it is
pointed at, builds its own `McpRuntimeConfig` from the payload, calls
`reopen_comparison_generation(..., generation_id=…)` with **no enclosure, no worktree and no live
state**, and reads the candidate content back with `git show <tree>:<path>` under an isolated
environment. It prints one JSON summary, and `_reopen_in_a_new_process` raises with the child's exit code
and stderr if the child failed — so a broken child is a failure, never an empty result.

**`_live_composition` (`:318-330`) is the independent counter-value.** It composes the same review again
from the live surface and returns the owners' own values (the comparison's `binding_digest`, its
`policy_version`, the digest over R02's inventory payload and its `listed_total`), which is how the
"what the manifest binds" case compares the record against a second reading instead of against itself.

**Damage is injected, never simulated.** The helpers exist to inject exactly the four shapes the cases
need: `_reseal` (`:244-253`) recomputes the seal over an edited field set **the way a fabrication would
have to** — so whatever catches it can only be a *second* statement of the same identity, which is what
`read_manifest`'s directory-name check is; `_write_control_object` (`:236-241`) writes an unreferenced
object for the reclamation measurement; `_hidden_stages` (`:229-233`) lists the stage directories the
freeze is supposed to have removed; `_refs` (`:224-226`) lists `refs/ar/` so "no pin was created" is
measured; and `_side`/`_artifact` (`:265-276`) address a half by its own name rather than by position.

**The fifteen cases, and the property each one protects:**

| Case | Property |
| --- | --- |
| `test_a_frozen_comparison_reopens_the_exact_content_after_restart_and_reclamation` (`:336-387`) | the packet's journey: freeze → real reclamation (with control) → worktree group removed → child-process reopen of the exact tree, both exact datasets and the cited evidence |
| `test_the_manifest_binds_the_owners_identities_versions_and_its_own_fields` (`:393-477`) | what the record stores is the **owners'** values (contract base, capture tree, each dataset's logical identity, R02's inventory, the comparison's binding digest, all five policy stamps), and its seal covers its own fields |
| `test_an_explicit_release_records_unavailable_history_and_is_measured_not_assumed` (`:483-550`) | the release leaves a record, the reopen reports `custody_observed="absent"` beside `unavailable-history`, and the object ids are still named rather than resolving to today's data |
| `test_a_missing_or_damaged_retained_input_is_reported_per_channel` (`:556-598`) | an injected deleted snapshot is `missing`, a corrupted one is `corrupt`, a rewritten citation is `corrupt`, and the untouched channel stays `available` |
| `test_a_record_that_cannot_be_read_is_not_a_readable_generation` (`:601-669`) | four unreadable shapes in order: unparseable bytes, a sealed field edited in place, the verifier's full **reseal**, and a reseal plus a matching id — each `manifest-unreadable` with no payload |
| `test_a_refused_freeze_publishes_nothing_and_reclaims_its_stage_and_pin` (`:675-708`) | a refused freeze leaves no generation directory, no hidden stage and no pin it created, and the same leaf freezes successfully after the damaged half is repaired |
| `test_an_exact_retry_converges_and_a_superseding_generation_names_its_predecessor` (`:711-762`) | `reused=True` with a byte-identical manifest, then a successor naming its predecessor by id **and** manifest digest while the first generation's bytes are untouched |
| `test_a_half_with_no_recorded_generation_freezes_as_typed_absence_never_as_inference` (`:768-836`) | R05's typed absence and the comparison's own `not-selected` are recorded as statements and each half is reported in its own state without calling the generation unavailable |
| `test_a_declared_absence_beside_present_bytes_is_refused` (`:839-866`) | a declared historical absence standing beside a readable dataset is refused |
| `test_the_leaf_s_own_work_branch_is_not_custody_and_the_pin_survives_losing_it` (`:869-910`) | the F1 falsifier reproduced exactly: commit on the work branch → `custody="retained"` + one ref → `worktree remove --force` → `branch -D` → `gc --prune=now` → child-process reopen `available` |
| `test_protected_history_taking_custody_stops_the_pin_and_the_generation_still_reopens` (`:913-966`) | the genuine `committed-history` path: the protected source branch fast-forwarded the way integration does it → **no ref created** → still reopens after the same deletions |
| `test_a_retention_ref_that_moved_is_never_deleted` (`:969-1016`) | a moved ref is refused, records nothing, and is left in place |
| `test_a_stage_a_dead_freeze_left_behind_is_reclaimed_and_a_live_one_is_not` (`:1030-1057`) | a real child process creates a stage and exits; after one freeze the dead stage is gone, this process's stage is untouched, and `_hidden_stages` is exactly the live one |
| `test_discarding_snapshots_records_the_bytes_it_measured_and_refuses_a_mismatch` (`:1060-1124`) | a mismatched snapshot is refused with both files in place and no record; recorded digests then equal the frozen ones; both halves report `unavailable-history`; the retry records `None` |
| `test_a_frozen_again_comparison_reports_its_live_pin_before_the_release_history` (`:1127-1170`) | release → refs empty → re-freeze → `reused=True`, same digest, ref back → reopen reports `pin_present=True` **and** `release_recorded=True` with the live measurement leading the detail |

### Conventions

`pytestmark = pytest.mark.evidence_unit` (`:81`) is the module's lane marker, and the module's path is
registered in `mcp/tests/test-evidence-lanes.toml`'s `unit-regression` lane. It also appears as a
**source-derived consumer** in the two `consumer_scope = "exact"` rows of `mcp/tests/evidence-lifecycle.toml`
that its imports make it a consumer of (`diff_scope_test_support.py`, `read_scope_test_support.py`) — so
the catalog's consumer sets stay exact rather than approximate. Every case is deterministic: no case
depends on wall-clock ordering, and order-sensitive Git commands run through helpers that pin `PATH`,
`HOME` and `GIT_CONFIG_NOSYSTEM`.

### Invariants And Boundaries

- **Production composition only.** No case injects a preconstructed manifest, a fake repository or a
  hand-built payload; every value the record binds is produced by the shipped owner.
- **Restart is measured, not simulated.** The reopen runs in a child process that shares no state, and a
  child failure is an assertion failure with its stderr, never an empty result.
- **Reclamation is proven to have happened.** The control object makes "the tree survived `gc`" a
  measurement rather than an assumption.
- **A fabrication is caught by a second statement of the same identity**, which is why the reseal case
  exists: an internally consistent forgery is exactly what a seal-only check would accept.
- **Damage is injected into real artifacts**, so the channel states are measured on the real readers.
- **No case reaches the HTTP surface, a browser or a route.** The reopen is exercised through the
  application operation only; wiring a route or a pane is R12/R13/R17/R20/R21 territory.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

Every claim on this card is checkable in the module's own docstring, helpers and cases. Three details a
reader should carry: the fixture is **shared with the R01 source-endpoint suite** rather than rebuilt, so
these cases measure the same real enclosure and capture path; the reopen really is a child process, and
the module's first case also proves `git gc --prune=now` reclaimed something via an unreferenced control
object; and the unreadable-record case injects a **full reseal** specifically because a seal-only check
would accept it.

- The module's own statement of the packet's journey and of the load-bearing property behind each case. [1]
- The lane marker, the two content constants the fixture edits without staging, and the cited-evidence paths. [2]
- **The child program: a real restart that builds its own config, reopens from the task artifact plane alone, and reads the candidate bytes back through `git show`.** [3]
- The shared R01 production fixture these cases build on rather than duplicating. [4]
- The freeze helper that requires a published generation, and the evidence-citation options. [5]
- **The injection helpers: the reclamation control object, the fabrication's own reseal, the hidden-stage list and the `refs/ar/` list.** [6]
- The independent counter-value the "what the record binds" case compares against. [7]
- **The packet's journey, with the control object and the removed worktree group.** [8]
- **The owners' values versus the record's own fields.** [9]
- **The release record, and the custody measured before reclamation reported beside the deletion.** [10]
- **Per-channel damage: missing, corrupt, corrupt citation, and the untouched channel.** [11]
- **The four unreadable shapes, including the internally consistent reseal that only a second identity statement catches.** [12]
- **A refused freeze publishes nothing and reclaims its own stage and pin.** [13]
- **Convergence on a published record, and a successor's resolved lineage.** [14]
- **The typed absences, and the refusal of a declaration beside present bytes.** [15]
- **The two custody cases: the work branch is not custody, and protected history taking custody stops the pin.** [16]
- The moved-ref refusal, and the dead-versus-live stage sweep driven through a real child process. [17]
- **The measured-discard case, and the live-pin-before-release-history case.** [18]
- The lane row this module was registered under, inside the array whose own key declares the classification. [19]
- **The two exact-consumer rows this module was added to, because its imports make it a source-derived consumer — each cited down to the artifact's own `consumer_scope` and the list it opens.** [20]
- The lane row this module was registered under. [21]
- **The two exact-consumer rows this module was added to, because its imports make it a source-derived consumer.** [22]
- The Git-truth support helpers the module reads its evidence through. [23]

The following declarations carry the changed boundary.

- The manifest is checked against actual owner records, identities and availability. [24]

### Cross-Repo References

No cross-repository behavior is measured in this file. It creates a local repository, an enclosure and a
task-artifact root under `tmp_path` for each case.

No meaningful cross-repo references found.
