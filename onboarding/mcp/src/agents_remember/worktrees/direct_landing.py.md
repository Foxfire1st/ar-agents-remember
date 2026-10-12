# mcp/src/agents_remember/worktrees/direct_landing.py

## Governing Overview

[Nearest governing overview](overview.md)

Current operative account reconciles the admitted L94 create/verify route and L143 owner/recovery changes on the Manager-synced working candidate. The older L9 evidence retains only its explicitly historical scope; source reading is not a new executed test or CODE verdict.

## Purpose

Coordinates explicitly selected publication for a granted canonical leaf on its master series branch, without its own enclosure. Verify-existing mode binds an already committed code output; create mode judges and commits the previewed code/memory pair under the same direct journal. Ordinary closeout and integration remain separate routes.

## Code Commentary

### Logic

DirectLandingRequest selects the exact canonical leaf and requires its current external grant. With code_commit, it verifies the existing local series HEAD; without code_commit, create mode requires code_commit_message, memory_commit_message and the prior code candidate_tree proof on apply. Configured series admission and branch/root identity remain mandatory; a harness switch supplies no authority.

The optional `leaf_id` selects the history owner and participates in the immutable operation input and retry identity; it is distinct from the required canonical `leaf_task_document_ref` and grant. `_direct_landing_after_policy` retains series-contract shape, effective-message normalization, nonblank approval intent and configured contract rereading. The application still owns configured admission and serialized execution. Preview prefers the proven `bound_leaf_id` over the optional caller `leaf_id`. During a live generation, `_select_gated_history` leaves the leaf selector unset while owner enforcement is off, so `direct-landing-input-conflict` retains precedence; a new request cannot evade that conflict through a history-gate refusal.

_verify_code_commit is the verify-existing route: it proves exact local series HEAD/tree and creates no code commit. Create preview binds the exact pair without branch/content publication. Apply checks the previewed tree/checkout, claims only policy-required review, creates a provisional Git object, judges the exact invariant/knowledge pair, persists the accepted input/policy/generation, then journals code intent and publishes/proves the branch output before memory convergence. The thirteen-row census describes those reached checks and the explicitly ruled door/leaf-taskIntent substitutes; it does not run an automatic strict-quality, full-MQC or affected-closure campaign or journal full pre-code verdict results. Before branch publication is the boundary, not before every Git object creation. Canonical leafTaskDocumentRef replaces the direct task-intent binding; hooks are not an added gate.

For apply, `_direct_memory_admission_snapshot` verifies the checked-out memory branch. Real content
dirt triggers reversible cache preparation before the accepted snapshot is captured; cache-only
dirt does not. Memory snapshots exclude the consumer cache while retaining actual ref and object
identity. `_prepare_direct_landing_candidate` stores code/tree and memory repository/ref/snapshot
facts in the typed input. Ledger paths, bytes, digests and a ledger-commit message are absent from that input; the effective memory message and create-mode codeCommitMessage are retained.

The admitted generation pins its canonical leaf, effective messages, code mode/tree and memory state. Verify mode records the existing code identity; create mode binds and proves the one provisional output before pairing memory. Interrupted accepted create output reuses that same code commit and completes/reconciles memory; exact repeat and public recovery never create a second code commit. Real ambiguity stays on the advertised developer-decision path. No closeout-door or ledger-byte publication is invented.

A completed doorless generation retired by its authorized owner stays readable for audit. Only a changed request may replace that retired terminal record with a fresh generation; an exact same-request replay retains the existing generation. Converted successors still require their own admitted open leaf history, not reopening the prior closed leaf. Public direct recover continues the accepted generation and settles its kept closing receipt on successful completion; ordinary closeout intent and door guards remain separate.

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
  `direct-landing-knowledge-gate-refused`. Preview uses the proven canonical `bound_leaf_id` before optional caller `leaf_id`; only when both selectors are absent does legacy selection infer the sole open history owner. A supplied valid identity is not a sole-open inference. Named invalid/foreign owners refuse within the source-selection rules. Apply uses the distinct select → close → judge sequence below.
- **Apply selection, closing, then judgment.** `_close_gated_leaf` first selects the exact history source through `_select_gated_history`/`direct_gate_source`, then closes that owner's history and captures the retained closed memory snapshot. `direct_gate_verdict` judges that exact closed tree with the selected source; `memory_commit_refusal(..., leaf_publication=True)` validates the same tree against `HEAD`. Any refusal or exception after closing restores the history and cache-ignore bytes. A replay that commits nothing returns no closing and remains bound to its already-paired head tree. Preview judgment and apply's select → close → judge sequence are distinct.
- **The closing lives until the generation is decided (review R1 F3; R2-2, R2-5; R3-1).** `_start_or_observe_direct_landing`
  first settles the kept closings (`_settle_kept_closing`; an unreadable receipt refuses as
  `direct-landing-closing-receipt-unreadable`), then checks `_in_flight_retry`: an exact retry of the series'
  in-flight generation (same contract path, code commit, candidate tree, effective input and approval note,
  `_same_request`) reuses the retained record directly: `record, created = current, False`. It does not call preparation, claim another review or call `_admit_direct_landing`; its accepted input was judged at admission. New/nonmatching requests use `_prepare_direct_landing_candidate(identity, *, enforce_owner=True)` followed by `_admit_direct_landing`. Owner enforcement is disabled only while a live conflicting generation must retain its input-conflict refusal precedence. Preparation returns the input, candidate and closing, restoring the closing if input construction fails. `_admit_direct_landing` writes the generation's receipt (`keep_direct_closing`) before
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


- Exact in-flight retry reuses the retained record without preparation or admission; other requests prepare and admit, then execution settles receipts. [3]


- Only a created generation keeps the closing. [4]


- Preparation takes identity and enforce_owner, selects/closes/judges before retaining the exact admitted snapshot, and restores on failure. [5]


- Apply selects the history source, closes it, judges the exact retained closed tree and validates that same tree as leaf publication, restoring on refusal. [6]


### Conventions

Execution is synchronous and journaled. Concurrency serialization is owned by configured
application authority, while crash recovery is owned by the durable operation. Verify-existing mode creates no code commit and needs no code message; create mode carries an explicit code message and prospective codeBefore. Both retain memory intent and same-generation recovery.

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

References 3, 5 and 6 below are re-authored for the current retained-record retry and select → close → judge implementation. Reference 7 and the create-mode reference retain the landed L94 account. Other original L9 references and test descriptions retain their original historical evidence scope; they are not fresh execution or current gate-order certification.

- Current direct request, canonical-leaf grant admission, verify-existing code proof and pure pair preview; the retired settings gate is not current. [7]
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

- Direct landing separates verify-existing from pre-code judged create mode and same-generation paired recovery. [13]

- Exact direct replay retains its generation; only a changed request may replace retired completed evidence. [14]
