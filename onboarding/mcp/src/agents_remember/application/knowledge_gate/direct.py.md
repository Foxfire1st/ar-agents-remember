# mcp/src/agents_remember/application/knowledge_gate/direct.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/knowledge_gate/direct.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-30T20:09:38+02:00 |
| lastVerifiedCommitHash | `c052b2593b85d9baf425cc1d5c46f384b13fc9ea`|
| lastVerifiedCommitDate | 2026-09-30T21:09:40+02:00|
| governingOverview | `../overview.md` |

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

- **The leaf (ruling 2026-09-30T14:38:47, gap 2).** The route names no leaf, so the leaf is the owner of the one
  open leaf history file in K_C (`open_leaf_owners`: `knowledge/history/*.json` with the history schema,
  `closed: false` and a string `leaf`; a file that does not parse is skipped, because the validator names it). None,
  or more than one, refuses: "it names no leaf, and the memory candidate holds N open leaf history file(s) …". A
  direct-mode leaf of a converted repository therefore records its rows, or an empty `rows`, in its own file, which
  the landing then closes. No public schema change; unconverted direct landing is unchanged.
- **`direct_verdict`** returns `DirectGateVerdict(applies, owner, refusal)`; a missing memory repository or a series
  line with no head refuses; a `SubprocessError` anywhere is a named refusal through `git_failure`.
- **`_verdict`:** a replay of an already published landing (HEAD's trailer names this code commit and HEAD's tree is
  the candidate) commits nothing and is not gated (`applies` false). Otherwise it finds the owner, recomputes the
  worklist over `_DirectSides`, and judges it with `validation_bases=(head,)` (the series memory head, the line it
  lands on) and `base_code_commit` = the published code commit.
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

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The design authority is `MIK-R09@v2` and `09_mandatory-invariant-closeout-gate.json`,
outside the repositories.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The module docstring: the four sides and the leaf a direct landing names. | "The route names no leaf, so the leaf is the owner" | mcp/src/agents_remember/application/knowledge_gate/direct.py:1-18 |
| The open leaf history files of a candidate. | `open_leaf_owners` | mcp/src/agents_remember/application/knowledge_gate/direct.py:62-81 |
| The verdict; a replay is not gated; exactly one owner. | `direct_verdict`; `_verdict` | mcp/src/agents_remember/application/knowledge_gate/direct.py:84-130 |
| The worklist over the series sides, failing closed. | `_worklist` | mcp/src/agents_remember/application/knowledge_gate/direct.py:142-191 |
| The route test. | `test_direct_landing_gates_names_its_leaf_closes_its_history_and_restores_on_refusal` | mcp/tests/test_knowledge_closeout_gate.py:865-896 |

## Cross-Repo References

No meaningful cross-repo references found.

| Finding | Anchor | Source |
| --- | --- | --- |
| No cross-repo boundary is crossed by this file. | — | — |

## Update History

<!-- newest entry by date and time is prepended at the top of the list; prepend-only -->
- 2026-09-30T20:09:38+02:00 — 260928-MIK-L09 curator (staged change set on `ar/260928-mik-l09`, code base `904e804b07a598d5d6c66f06b7e67ddab64d9b8e`; review R1 changes-required, fix round, R2 pass-with-notes, round, R3 pass with R3-1 and R3-2 fixed): created this card for the new file MIK-R09 adds, recording ruling 14:38:47 gap 2 (direct landing infers its leaf on converted memory only), the L11 fail-closed task-document read and the L03 Git-failure carry. The verification stamp is left empty: the file is new and uncommitted, so no commit yet holds the content it would claim to have verified; closeout owns the real stamp.
