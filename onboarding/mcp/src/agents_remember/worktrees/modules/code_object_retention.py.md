# mcp/src/agents_remember/worktrees/modules/code_object_retention.py

## Governing Overview

[worktrees/modules route overview](overview.md)

## Purpose

Custody measurement and explicit release of pins earlier comparison freezes created.

## Code Commentary

### Logic

RetainedCodeObject names historical ref/commit/tree/base. No operation creates one. code_object_custody checks only named durable tips and recorded landed commits, not disposable branch sweeps or ancestry. [5] [10]

Observation distinguishes absent from retained/committed history. Release measures custody, checks the current ref still names its recorded commit, deletes with expected-value update-ref and returns the release record. Absent refs converge; moved refs refuse. [11] [13]

Real scratch-repository cases drive release and snapshot deletion owners with exact ref/byte guards. Old deterministic pin-creation and canonical-generation reopen cases do not establish current behavior. [22] [23]


**Custody examines the names and never walks history.** `_named_commits` (`:425-442`) resolves each named
durable ref through `^{commit}` — so a missing branch or a tag on a blob contributes **nothing** rather
than being compared as if it were history — then adds the recorded commits that resolve, dropping
duplicates so a commit named twice is examined once. `code_object_custody` compares each resolved commit's
tree (`_commit_tree`, `:454-458`) against the tree in question: a match is `committed-history`, otherwise
`retained`. The measurement is bounded by the number of names and never walks ancestry, so a tree
surviving only deeper in a named branch's past is still reported `retained` — and the docstring states the
asymmetry: *"Keeping a redundant pin is the safe direction to be wrong in; releasing one that was the
only reference is not."* It also never releases anything by itself.

**There are three observations, not two, and the third exists because a record must not lie.**
`code_object_observation` (`:243-256`) answers `absent` when the object does not resolve at all, and only
otherwise asks the custody question. The `CUSTODY_UNREADABLE` literal is `"absent"` and is deliberately a
**separate type** from `CodeObjectCustody` (`:75-84`): an object that does not resolve is not held by
anything, so reporting it as `retained` would claim a pin is holding bytes that are gone — which is
exactly the state a released-and-reclaimed history is in. "A record never stores this value; only a
reader that is looking at the world right now reports it."

**Release refuses to delete what it did not bind, and converges when there is nothing to delete.**
`release_retained_code_object` measures custody first — the value a caller stores as the
unavailable-history record, because "a reader of the record cannot recover that distinction afterwards"
and it includes the `absent` case honestly — then deletes the ref with `update-ref -d <ref> <commit>`
**only** while `_ref_commit` (`:418-422`) still equals the recorded commit. A moved ref raises
`code-object-ref-moved`; an already-absent ref is **not** a failure, so a retry of an interrupted release
converges on the same record instead of reporting a second, contradictory outcome.
`retained_object_readable` (`:259-267`) is the reader's question — both halves are asked, "because they
are two different failures: the ref may be gone (the pin was released) or it may point somewhere else
(something re-pointed it)".

**Every Git question is a question, not a check.** `object_readable` (`:165-175`) returns a boolean
because "the object this comparison bound is still here" is a fact the caller reports in its own voice —
a refusal while freezing, an unavailable channel while reopening. `_diagnostic` (`:468-474`) renders one
Git failure's own words, transport-safe, for a refusal that has to be actionable.

### Invariants And Boundaries

- Custody never releases automatically.
- The caller owns policy, record publication and lifetime.
- Release cannot delete a moved ref.

- **A ref is never re-pointed.** An occupied ref is returned only when it names the same pin, otherwise
  it is refused.
- **Only named durable history counts as custody**, and an empty name set means the pin stays.
- **The custody measurement never walks history and never releases anything.** A stale-but-redundant pin
  is the safe direction.
- **`absent` is not a custody value.** It is the reader's third observation, never a stored record.
- **Release requires the ref to still name the recorded commit**, and an already-absent ref converges.
- **Nothing outside `refs/ar/retained-code/` is ever written, and no branch, index or working tree is
  touched.**
- **No policy lives here.** What to retain, when a comparison is finished with a tree, and what the
  retention means all belong to the caller.
- **Boundary: whether any landed lifecycle operation objects to an unexpected ref namespace during
  integration or closeout is unmeasured.** The pin was measured to survive `worktree remove`/`prune`,
  `branch -D`, gc-packing and `git fsck`, but integration and closeout transactions were not run by this
  leaf and remain an open question for the verifying seat.

### Todos

- The `refs/ar/retained-code/` namespace's interaction with landed integration/closeout operations is
  unmeasured (see the boundary above). It is recorded as an open question rather than a todo with an
  owner in this leaf.


## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.


### Repo-Internal References

Every claim on this card is checkable in the module's own docstring and functions, in the cases that
measure the pin against a real repository, and in the two consumers (`review_comparison_retention` for
creating one, `review_comparison_reclamation` for releasing one). Three details a reader should carry:
the retention commit's **identity is supplied explicitly** so the commit id is a function of the retained
objects; custody counts only the refs and commits the caller **names**, so the leaf's own work branch is
never custody; and `absent` is a reader's observation with its own type, never a stored custody value.



- Complete retained pin identity. [5]


- Named-tip custody only. [10]


- Absence is a distinct observation. [11]


- Exact-ref release and absence convergence. [13]


- Real release guards and named custody. [22]


- Exact-byte snapshot deletion, with mismatch refusal. [23]



- The module's own statement of the three properties — one commit and one ref, measured custody over named history only, explicit release with a record — and of what it does not decide. [36]
- The published surface, the namespace, the two custody literals and the third observation's literal. [37]
- **The durable history a custody measurement is allowed to find the tree in, and the empty set as a statement.** [38]
- **The pin record — ref, commit, tree, base — whose four fields release requires together.** [39]
- **The release record a caller stores as unavailable history, including the custody measured at release and the honest `absent` case.** [40]
- The one Git question that answers a boolean rather than raising. [41]
- **Custody over named history only, bounded by the number of names and never walking ancestry.** [42]
- **The three-way observation, and the reason `absent` is a separate type from the two custody values.** [43]
- The reader's question about a recorded pin: gone, or re-pointed. [44]
- **Release: refuse a moved ref, converge on an absent one, and return the record with custody measured before deletion.** [45]
- The named-commit resolution that drops what does not resolve to a commit. [46]
- The Git failure's own words, rendered transport-safe for an actionable refusal. [47]


### Cross-Repo References

No cross-repository contract is established by this file.
