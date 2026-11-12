# mcp/src/agents_remember/application/knowledge_gate/direct.py

## Governing Overview

[application route overview](../overview.md)

## Purpose

**The gate at direct landing, the branch-addressed leaf closeout (MIK-R09 rule 3).** A direct landing publishes a
leaf implemented on the series branch itself, without its own worktree enclosure, so its four sides are read from
the series lines: K_B is the series memory line's head (the commit the landing's memory commit follows), B is the code
commit K_B's `Code-Commit` trailer names (which must be an ancestor of the landed code commit), C is the verified code
commit's tree and K_C the memory checkout's exact candidate tree. The worktree layer probes the marker first and calls
`direct_verdict` through the port only on converted memory.

## Code Commentary

### Logic

- **The named leaf.** Optional `leaf_id` selects the direct publication's owner explicitly. A valid name with no file creates a closed rowless history; another leaf's open file or an invalid name refuses. Without a supplied name, the owner is inferred from exactly one open leaf history file, and none/several refuses while naming `leaf_id` as the remedy. Owner selection is separate from closing and exact-tree admission.
- **`direct_verdict`** returns `DirectGateVerdict(applies, owner, refusal)`; a missing memory repository or a series
  line with no head refuses; a `SubprocessError` anywhere is a named refusal through `git_failure`.
- **`_source`** recognizes a no-publication replay only when the memory head's code trailer and tree equal the requested inputs, returning `applies=false`. Otherwise it selects the explicit or inferred owner. `direct_verdict` validates any retained pre-closing source identity against the closed candidate before asking `_verdict` to recompute and judge the exact series sides.
- **`_verdict`** recomputes the selected owner's worklist and judges it against the series memory head and published code base. Supplying `leaf_id` changes owner selection, not the obligation to answer every item.
- **`_worklist`:** an unpublished or non-ancestor B is `incomplete` (`pairing`); the owner's task document is read
  strictly (`strict_leaf_doc`, fail closed: `LeafDocumentUnresolved` is `incomplete`, the L11 carry); the run goes
  through `leaf.worklist_over` (L08's run, MIK-R30's onboarding items, MIK-R10's settling) over `ExplicitSides`; a
  `SubprocessError` is `incomplete [git]`; any other exception names the run; both sides unconverted (the caller's
  probe said otherwise) is `incomplete [K_C]`.

### Conventions

- The direct landing's closing of the history file and the exact-tree validation live in
  `worktrees/direct_landing.py`; this module decides only the verdict.

### Invariants And Boundaries

- **A direct landing of a converted leaf lands only with every item answered and the validator passing.** Realized by
  `_verdict` and `judge`; proved by `test_direct_landing_gates_names_its_leaf_closes_its_history_and_restores_on_refusal`
  and, through the public route entry, `test_direct_landing_preview_and_apply_refuse_through_their_route_entry`
  (including two open files, the review's M20). This is the packet's second non-conforming example: "A direct landing
  commits memory without evaluation."

### Todos

- None.

## Evidence

- A supplied valid owner selects rowless closed history while other open owners refuse. [14]


### Repo-Internal References

- `_open_histories` implements the retained boundary described above. [6]

- `_source` implements the retained boundary described above. [7]


- `direct_verdict` implements the retained boundary described above. [8]


### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

No configured live documentation source was available for this pass.

### Repo-Internal References


- The module docstring: the four sides and the leaf a direct landing names. [9]

- The open leaf history files of a candidate. [10]

- The direct verdict binds the explicit or inferred owner; only an exact no-publication replay skips a fresh gate. [11]

- The worklist over the series sides, failing closed. [12]

- The route test. [13]


### Cross-Repo References

No meaningful cross-repo references found.

No cross-repo boundary is crossed by this file.
