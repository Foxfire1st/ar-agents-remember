# mcp/src/agents_remember/worktrees/modules/closeout_external.py

## Governing Overview

[Governing route overview](overview.md)

## Purpose

Owns the external-memory content leg of the admitted closeout transaction after the code output is accepted. A new memory-content commit carries the accepted code commit in its `Code-Commit:` trailer; the later disposable ledger refresh is informational and creates no commit.

## Code Commentary

A series delegates to its series owner. An ordinary leaf resumes an already recorded memory output only after the recovery gate; otherwise it refreshes the owned metadata/index inputs, closes the converted leaf's latest history file and calls `_commit_memory_content`. The cutover lock refuses an unconverted leaf once its repository holds converted memory.

For converted memory, the history closing and cache ignore rule are present before `_exact_memory_tree` captures the intended output. `_refuse_ungated_memory` validates that exact tree against the parent memory tip and runs the leaf invariant gate with the exact accepted code tree. Even a clean output reused as HEAD is judged. This is the closeout's mandatory invariant gate, not an additional full MQC or curator-coherence operation. Preview reads the same candidate verdict; recovered outputs are judged before resuming.

`_commit_memory_content` binds the contract work branch and the tip observed before judgment. It rechecks that admission, prepares the cache exclusion, and refuses a staged output different from the judged tree before mutation intent. It publishes the judged object through `publish_tree_commit`; content written after the final check cannot enter that commit and stays uncommitted. The exact accepted memory message supplies code attribution. An unconverted route, where admitted, stages actual content under its existing owner rather than claiming a converted-tree gate.

The restoring block runs from the first preparation until publication returns. `_restore_preparations` restores history/ignore bytes only while each still holds what this call wrote, preserving concurrent content. A provably unpublished refusal restores those preparations. A partial publication can raise after the branch moves: a switched HEAD and failed expected-old take-back may leave the memory commit reachable while preparations restore. Proof runs after successful publication return, outside that restoring block; a proof failure leaves preparations in place for recovery. Universal rollback is therefore not this contract. Code is committed before memory; a memory refusal can leave the accepted code output awaiting a successful memory leg.

The publication primitive's Git behavior is separate from prepared closeout policies; this owner does not call the removed `commit_verified_staged` helper. Root `memory.md` remains excluded from real content commits, including force-staged cache data. No cache repair can undo or become a prerequisite for a proven memory output.

## Evidence

### Repo-Internal References

- `external_closeout_commits` supplies the exact current transaction boundary above. [23]
- `_commit_memory_content` supplies the exact current transaction boundary above. [24]
- `_restore_preparations` supplies the exact current transaction boundary above. [25]
- `_require_judged_tree` supplies the exact current transaction boundary above. [26]
- `_refuse_ungated_memory` supplies the exact current transaction boundary above. [27]
- `require_gated_recovery` supplies the exact current transaction boundary above. [28]
- `candidate_gate_verdict` supplies the exact current transaction boundary above. [29]
