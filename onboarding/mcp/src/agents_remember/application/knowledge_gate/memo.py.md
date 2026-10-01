# mcp/src/agents_remember/application/knowledge_gate/memo.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**A bounded in-process memo of the gate's verdicts over exact inputs (MIK-R09; ruling 2026-09-30T14:38:47 gap 4,
refined at 15:09:25).** One contract-scoped memory-quality run evaluates the gate up to three times over the same
candidate (the count, then twice through the closeout validator), and closeout admission evaluates it again; each
evaluation recomputes the worklist from its four sides (7–17 s on the real converted scratch). A repeated evaluation
over identical inputs reproduces the identical verdict, so the memo keeps it, keyed by everything the evaluation
reads. It does not weaken the always-recompute rule: a changed input is a different key, and a new candidate is
always recomputed.

## Code Commentary

### Logic

- **`GateMemoKey`**: the exact code tree C and memory tree K_C; the contract's path plus the SHA-256 of its bytes
  (which carry B, the branches and `memory_base_commit`); the parent line's memory tip (the validator base and the line
  K_B pairs on; review R1 F6); the SHA-256 of the leaf task document read through `strict_leaf_doc` (maintenance scope
  and declared effects); and the build (`measuring_build_stamp`). `memo_key` returns `None` (no memo) when any of
  these cannot be identified.
- **`_Kept`** holds when the verdict was computed, the verdict, and **the read set**: every file outside the trees
  that the evaluation read, as `(path, identity)` (the requirement manifests and packets MIK-R14's reconsideration
  links read through `requirement_endpoint`, and the settings files `trace_context` reads, including the coordination
  fallback; review R1 notes). `still_read_the_same` hashes each again with `file_identity`.
- **`remembered(key)`** returns the kept verdict only when it is younger than `MAX_AGE_SECONDS` (900) and every
  recorded file still has the recorded identity: a newly approved requirement version, a manifest that appeared or
  vanished, or edited settings is a miss, and the gate recomputes.
- **`remember(key, result, reads)`** keeps the verdict only when `result.memoisable` (no `incomplete` finding, no
  unreadable validator input, a `complete` worklist) and no recorded path is `CONFLICTING` (a file read twice with
  different identities in one evaluation). `GATE_MEMO` is the kernel's LRU `BoundedMemo` of `CAPACITY` (16).

### Conventions

- A refused verdict over complete inputs is deterministic and is kept like a pass (ruling 15:09:25: "only failed runs
  and incomplete results are never kept"). A run that involved a failed or timed-out Git call is incomplete and
  never kept (review R1 F9; R3-2 for `has_blob`).
- The approval state never depends on the age limit (15:09:25); the capacity and age bounds are belt and braces.

### Invariants And Boundaries

- **A kept verdict is reused only for identical trees, contract, parent tip, task document, build and recorded
  requirement-file reads; incomplete runs and Git failures are never kept.** Candidate invariant (not ingested).
  Realized by `GateMemoKey`, `_Kept.still_read_the_same`, `remembered` and `remember`; proved by
  `test_the_gate_memo_reuses_a_verdict_only_for_the_identical_inputs` (one `_evaluate` for three reads; a changed
  memory tree and a changed contract miss; incomplete and failed runs are never kept; the age limit),
  `test_a_kept_pass_is_recomputed_once_an_endpoint_s_approval_state_changes` (both "v1 approved" and "manifest
  missing" recompute and raise `reconsideration_candidate` once v2 is approved; with the re-hash mutated to `True`
  both fail), `test_the_memo_key_holds_the_parent_tip`, and
  `test_every_file_read_is_in_the_read_set_and_a_conflicting_read_is_never_kept`.
- **Timing (evidence `memo-timing.txt`):** on the real converted scratch, one run of four evaluations went from about
  67.5 s to 17.1 s for the maintenance-scope leaf and 30.7 s to 8.0 s for the answered leaf.

### Todos

- None.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The module docstring: the key, inputs outside the trees, the bounds, what is never kept. [1]
- The bounds and the key. [2]
- A kept verdict with its read set, hashed again before reuse. [3]
- The key of one evaluation, or no memo. [4]
- Reuse and keep. [5]
- Only identical inputs reuse a verdict. [6]
- A changed approval state recomputes a kept pass. [7]

### Cross-Repo References

The read set may name files of another task's folder under the coordination root (a `reconsider_on` link's
requirement manifest and packet), outside both repositories.

No cross-repo code boundary is crossed by this file.
