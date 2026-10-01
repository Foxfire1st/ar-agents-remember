# mcp/src/agents_remember/worktrees/direct_landing.py

## Governing Overview

[Nearest governing overview](overview.md)

Working-candidate verification: source inspected at 2026-09-15T00:51 UTC against the uncommitted L9
candidate. The commit fields identify the latest real commit touching this file; they do not
identify or claim a future commit for these working changes.

## Purpose

Coordinates branch-addressed delivery for a sanctioned leaf implemented without its own worktree
enclosure. It verifies already committed code, accepts an exact memory candidate, and creates or
observes one direct-landing journal generation. Ordinary series closeout and integration are
separate routes.

## Code Commentary

### Logic

`DirectLandingRequest` carries the exact code commit, memory message, approval intent, optional
candidate tree, and dry-run selection. The policy gate requires `directExecutionEnabled`.
`_direct_landing_after_policy` requires a series contract, normalizes the effective memory message,
requires intent, and rereads configured contract authority. The application boundary owns configured
admission and serialized execution; this module consumes the admitted contract.

`_verify_code_commit` first proves that the requested commit is the exact local series-branch HEAD,
then resolves its tree. Apply requires the supplied pre-commit candidate tree to match. This module
checks the candidate proof; it neither creates the code commit nor runs the caller's quality gate.
Preview reads repository/ref facts and does not parse or mutate a ledger.

For apply, `_direct_memory_admission_snapshot` verifies the checked-out memory branch. Real content
dirt triggers reversible cache preparation before the accepted snapshot is captured; cache-only
dirt does not. Memory snapshots exclude the consumer cache while retaining actual ref and object
identity. `_prepare_direct_landing_candidate` stores code/tree and memory repository/ref/snapshot
facts in the typed input. Ledger paths, bytes, digests, and commit messages are absent from that input.

`_create_direct_landing` admits the request itself: contract, code commit/tree, candidate, and
normalized inputs. It carries no closeout-door publication. The runtime executes or reconciles the
same generation. Success includes the lifecycle-operation projection; an existing generation that
requires action returns the closed public `refused` outcome with that evidence nested.

### 260928-MIK-L09 The Mandatory Gate At Direct Landing (MIK-R09 Rule 3)

Direct landing is one of MIK-R09's leaf-publication routes. On converted memory (the layout marker in the checkout's
working tree or `HEAD`) it gates before admission. Unconverted memory is refused by the cutover lock once the memory
repository holds converted memory (L37, MIK-R09 rule 6: `_direct_gate_owner` raises
`direct-landing-unconverted-memory-locked`, in preview and apply alike, before anything is captured). In a repository
that holds none it lands exactly as before (probed before anything
is captured or written: `count-objects` and `status` unchanged in the unconverted test; `unconverted.sh` finds the
preview payload and object count identical to base).

- **The gate.** `_direct_gate_owner(contract, code_commit)` probes `checkout_memory_converted`, captures the exact tree
  the memory-content commit would record (`_memory_content_tree`: a private index under the worktree group's
  `reports/`, `MEMORY_CONTENT_EXCLUDES`), and asks `direct_gate_verdict` through the port; any refusal raises
  `direct-landing-knowledge-gate-refused`. It returns the leaf that owns the one open history file (ruling
  2026-09-30T14:38:47 gap 2). The preview calls it too, so it refuses exactly as the apply.
- **The closing and the exact tree.** `_close_gated_leaf` gates, closes the owner's history file
  (`close_owner_history`, MIK-R07 rule 7), and validates the exact tree it will commit through
  `memory_commit_refusal(..., leaf_publication=True)` against `HEAD` (`direct-landing-knowledge-validation-refused`).
  Any refusal or exception restores the file.
- **The closing lives until the generation is decided (review R1 F3; R2-2, R2-5; R3-1).** `_start_or_observe_direct_landing`
  first settles the kept closings (`_settle_kept_closing`; an unreadable receipt refuses as
  `direct-landing-closing-receipt-unreadable`), then checks `_in_flight_retry`: an exact retry of the series'
  in-flight generation (same contract path, code commit, candidate tree, effective input and approval note,
  `_same_request`) prepares **without** the gate and reaches `_create_direct_landing`'s existing-generation check,
  which resumes it or reports the conflict; that generation was gated when it was admitted.
  `_prepare_direct_landing_candidate(identity, *, gated)` returns the input, the candidate and the closing (restored if
  building the input fails). `_admit_direct_landing` writes the generation's receipt (`keep_direct_closing`) before
  creating it and keeps the closing only when the journal **creates** a generation; an input conflict, a failing
  create, any exception, or a replayed generation restores it in process and drops only this call's receipt
  (`_undo_closing`). A receipt Git cannot write (`hash-object` failing) restores and refuses as
  `direct-landing-closing-receipt-unwritable`. The kept closings are settled again after a replayed completion and
  after execution (`_generation_state`: landed, cancelled or in flight); cancellation settles them too
  (`integration/lifecycle/control/cancellation.py`).
- **Tests:** `test_direct_landing_gates_names_its_leaf_closes_its_history_and_restores_on_refusal` and, through the
  public entry `direct_landing(config, request, series)`, the preview/apply, input-conflict, exact-retry, cancel,
  another-generation (N12), crash-before-create (N05), unreadable-receipt (R2-5), exact-tree (N09) and
  already-landed (R3-1, SHA-1 and SHA-256) cases in `test_knowledge_gate_routes.py`.

- The module docstring's gate and closing paragraphs. [1]
- The preview refuses as the apply. [2]
- Settle, exact retry, prepare, admit, and settle again. [3]
- Only a created generation keeps the closing. [4]
- The prepared input, the candidate and the closing. [5]
- The exact memory tree, the gate and the closing validated as a leaf publication. [6]

### Conventions

Execution is synchronous and journaled. Concurrency serialization is owned by configured
application authority, while crash recovery is owned by the durable operation. The code leg is
verified-existing, and the only mutation message is the memory-content message.

### Invariants And Boundaries

- Apply requires external memory and the exact pre-commit candidate tree.
- Series shape alone does not turn ordinary closeout or integration into direct execution.
- Real code, memory repository, branch, and content evidence retain their authority.
- Cached rows, bytes, or absence have no admission or recovery authority.
- There is no ledger third leg, ledger-only commit, closeout-door dependency, or repeat-from-scratch recovery route.

### Todos

No new file-local follow-up is established by this documentation pass.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository. No external domain documents
were available through the configured registry to consult; the current claims are grounded in the
working source and package-local evidence below. The registry is discovery input, not a citation.

No configured external domain-documentation evidence.

### Repo-Internal References

These repository-relative targets were checked in the L9 code checkout. The cited ranges support
the current working-candidate behavior; historical entries below retain their original scope.

- Policy, normalized request, exact code proof, and the preview, which writes no memory content and since MIK-R09 refuses exactly as the apply on converted memory. [7]
- Memory admission captures the prepared content snapshot and typed candidate (since MIK-R09 in `_operation_candidate`, after the gate's closing). [8]
- Generation creation and action-required public projection. [9]
- The application owns configured admission and execution serialization. [10]
- The focused integration scenario verifies cache-independent publication and recovery. [11]

- Unconverted memory: the lock refuses it once the repository holds converted memory, else the landing is ungated as before. [12]

### Cross-Repo References

Configured code and memory repositories or temporary fixture repositories are described through
the package-local implementation above. No additional external or sibling-repository evidence
source is configured for this file's claims.

No additional configured cross-repository evidence is claimed.
