# mcp/src/agents_remember/worktrees/modules/code_object_retention.py

## Governing Overview

[worktrees/modules route overview](overview.md)

## Purpose

**Explicit Git-object retention for the code a comparison binds, and its explicit release.** A captured
candidate tree is written by the capture owner through a private index, so **nothing points at it**:
`git gc` may delete it at any moment, and the only thing between "the comparison can be reopened" and
"the tree is gone" is an object reference that survives reclamation. This module is that reference, and
the whole of it. It sits beside `modules/git.py` because it is Git mechanics, and it routes every command
through the kernel's `run_git`.

Three properties, each of which is a decision rather than an implementation detail:

1. **Retention is one commit and one ref.** `retain_code_object` (`:178-212`) writes a commit whose tree
   is the captured tree and whose parent is the recorded base commit, then points
   `refs/ar/retained-code/...` at it. One ref therefore keeps **both** bound objects alive — the
   candidate tree as the commit's own tree and the base commit as its ancestor — so reclamation cannot
   keep the candidate and drop the baseline it is compared against. No other object is touched, moved or
   rewritten, and the user's branches, index and working tree are not involved.
2. **Custody is measured, never assumed — and only *named* history counts.** `code_object_custody`
   (`:215-240`) asks whether the tree is held by the durable history the caller **names**:
   `CustodyNames` (`:94-106`) carries refs whose history outlives the work that produced the tree (a
   leaf's protected source branch) plus the exact commits a task record landed. It deliberately does
   **not** sweep every local branch tip: a leaf's own work branch is disposable — `worktree_abandon`
   force-deletes it and `worktree remove` plus `branch -D` is an ordinary end to a leaf — so a commit
   that exists only on it is not custody at all. Naming nothing therefore means *nothing durable holds
   the tree*, and the pin stays.
3. **Release is explicit and leaves a record.** `release_retained_code_object` (`:270-316`) refuses to
   delete a ref that no longer points at the commit it recorded, and returns a `ReleasedCodeObject`
   naming the ref, the tree, the measured custody **at release** and the reason.

**Nothing here decides *what* should be retained, *when* a comparison is finished with a tree, or what
the retention means.** The module moves one object reference and reports what it found; the caller owns
the policy, the record and the lifetime.

## Code Commentary

### Logic

**The ref namespace is outside `refs/heads` and `refs/remotes` on purpose.**
`RETAINED_CODE_REF_NAMESPACE = "refs/ar/retained-code"` (`:70`): nothing fetches, pushes, merges, rebases
or deletes it, so `worktree remove`, `branch -D`, `worktree prune` and `gc --prune=now` all leave it
exactly where it is; and a reader can find every pin this feature holds with one `git for-each-ref` over
exactly that prefix. `retention_ref` (`:146-162`) refuses a leaf or generation segment that would escape
the namespace (empty, `/`, `\`, `.`, `..`), because "a ref is a name, and a name that can leave its
namespace is not one". `_require_namespaced` (`:322-334`) re-checks the whole ref before any write.

**The retention commit's identity is a function of the retained objects, and that is load-bearing.**
`_retention_commit` (`:366-394`) supplies author, committer and **both** timestamps explicitly through the
runner's `identity` option (`GIT_AUTHOR_*` / `GIT_COMMITTER_*` being the only spelling Git offers for
`commit-tree`), so the same tree on the same base always produces the **same commit id**. `_retention_identity`
(`:397-415`) dates it by the **base commit's own committer date** (falling back to the epoch only when
Git cannot report it). The module's own docstring states why this is not cosmetic: a retention commit
that embedded "now" would make a pin re-created after an explicit release a **different** object, the
generation describing it a different generation, and an exact retry of one freeze would stop converging
the moment it crossed a second — two generations claiming one index for a comparison nobody changed.

**The operation is idempotent in exactly one direction.** `_existing_or_refuse` (`:347-363`): a ref that
already holds a commit with **this tree and this parent** is returned as it stands (the same pin —
re-creating it would add nothing), while a ref that holds anything else raises
`CodeObjectRetentionError("code-object-ref-occupied")` rather than being overwritten, because "the objects
behind it may be another generation's only copy, and a retention owner that silently re-pointed it would
be the thing that loses history". `_require_present` (`:337-344`) refuses to pin an object this
repository cannot read, and a failed `update-ref` is `code-object-ref-unwritable`.

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

### Conventions

`__all__` publishes sixteen names: the three custody literals and the ref namespace, the five value
types (`CodeObjectCustody`, `CodeObjectObservation`, `CustodyNames`, `ReleasedCodeObject`,
`RetainedCodeObject`) and the seven operations. `RetainedCodeObject` and `ReleasedCodeObject` (`:109-143`) are pydantic models
with `extra="forbid"` and `frozen=True` — repository facts that travel together, and releasing requires
the *exact* commit a ref was created for, so a record carrying only a ref name could not tell "the object
I pinned" from "whatever that ref points at now". `CustodyNames` (`:94-106`) is a frozen dataclass whose
two fields default to empty tuples, and the empty set is a **statement** rather than a default: "nothing
durable was named, so nothing durable holds the tree and the pin stays". `_RETENTION_EMAIL`
(`retention@agents-remember.invalid`) and `_EPOCH` (`:90-91`) are constants for the same reason the
identity is: the commit id has to be a function of the retained objects and nothing else.

### Invariants And Boundaries

- **One ref keeps both bound objects**, because the retention commit's parent is the **recorded base
  commit**, never `HEAD`.
- **The retention commit id is a function of the two objects it keeps** — author, committer and both
  timestamps are supplied, so re-creating a released pin reproduces the identical commit.
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

- The module's own statement of the three properties — one commit and one ref, measured custody over named history only, explicit release with a record — and of what it does not decide. [1]
- The published surface, the namespace, the two custody literals and the third observation's literal. [2]
- The constants that make a retention commit's id independent of the ambient identity and the clock. [3]
- **The durable history a custody measurement is allowed to find the tree in, and the empty set as a statement.** [4]
- **The pin record — ref, commit, tree, base — whose four fields release requires together.** [5]
- **The release record a caller stores as unavailable history, including the custody measured at release and the honest `absent` case.** [6]
- The ref builder and its namespace-escape refusal. [7]
- The one Git question that answers a boolean rather than raising. [8]
- **Retention: the recorded base as parent, the one-directional idempotence, and the refusal to re-point a ref another generation owns.** [9]
- **Custody over named history only, bounded by the number of names and never walking ancestry.** [10]
- **The three-way observation, and the reason `absent` is a separate type from the two custody values.** [11]
- The reader's question about a recorded pin: gone, or re-pointed. [12]
- **Release: refuse a moved ref, converge on an absent one, and return the record with custody measured before deletion.** [13]
- **The identity-supplied commit, and the base commit's own date that keeps the pin meaningful in `git log` while staying derived.** [14]
- The named-commit resolution that drops what does not resolve to a commit. [15]
- The Git failure's own words, rendered transport-safe for an actionable refusal. [16]
- The Git runner and the identity option that makes an explicit commit identity possible. [17]
- The typed failure this module raises for every one of its ref outcomes. [18]
- The sibling Git-mechanics owner this module sits beside, and the branch-ref spelling its callers use for the protected source branch. [19]
- The create-side consumer: custody measured against the contract's names, and a pin created only when named history does not hold the tree. [20]
- The release-side consumer: the fast-fail re-check, the record written first, and the record withdrawn when this module refuses. [21]
- **The cases that measure the pin against a real repository: the leaf's own work branch is not custody and the pin survives losing it, genuine protected history stops the pin, and a moved ref is never deleted.** [22]
- **The case whose control object proves `git gc --prune=now` really reclaimed while the pinned objects survived.** [23]

### Cross-Repo References

No cross-repository behavior is implemented in this file. It runs Git against one local repository whose
path the caller supplies and creates a ref inside that repository's own namespace.

No meaningful cross-repo references found.
