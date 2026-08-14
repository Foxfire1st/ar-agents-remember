# mcp/src/agents_remember/worktrees/source_lineage.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/worktrees/source_lineage.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-08-13T09:27+02:00 |
| lastVerifiedCommitHash | `5aff1e8f01dfa949efc8f68e46bc62a99ed31432` |
| lastVerifiedCommitDate | 2026-08-14T14:36:50+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[mcp overview](../../../overview.md)

## Purpose

`source_lineage.py` is the fail-closed, task-identity-derived admission policy for
structural work. It proves the applicable super-integration to master and master
to leaf branch ancestry for code and, when configured, external memory. Callers
provide a canonical task-document reference or an enclosure contract; they do
not provide runtime ids, remembered branch ids, or an alternate lineage root.

## Code Commentary

`source_lineage_for_task` resolves the canonical document through
`TaskDocumentTopology`. Sprint-scoped roles have no single master edge. A master
resolves its series contract and attributes an absent or unreadable contract to
`super-to-master`; a leaf resolves its enclosure and attributes the same failure
to `master-to-leaf`. Once a contract exists, `source_lineage_for_contract`
proves every transitive edge: a series checks its super-to-master code edge and
external-memory edge, while a leaf checks both parent edges plus its own
master-to-leaf edges.

The leaf edge is not merely a Git comparison. `_linked_edge` first proves that
the leaf contract names the parent master's repository and work branch. `_edge`
then classifies the descendant as `current`, `behind`, `diverged`, or
`unavailable` from branch existence and `ahead_behind`. `_projection` reduces
the edges to one strict public state and deduplicates ordered `worktree_sync`
recoveries by contract path. Recovery arguments are dry-run by default, so the
projection guides a deliberate parent-first repair rather than silently moving
branches.

Repository equality is Git identity, not checkout-path equality. The shared `repository_identity`
Git helper asks each
checkout for its absolute `--git-common-dir` through the guarded kernel Git runner and resolves that
path before comparison. A parent contract may therefore point at one linked worktree while a leaf
contract points at a sibling worktree of the same repository; a missing/non-directory checkout or
failed/empty Git result remains unavailable rather than being guessed equal.

`parent_source_lineage` is the narrower pre-mutation guard used by leaf reopen
and start: it proves the master already contains the super before leaf state is
rewritten. `lineage_refusal` maps blocked and unprovable projections to the
published refusal vocabulary, and `lineage_block_payload` gives worktree entry
points one consistent blocked payload with the projected evidence and first
sync operation.

`require_current_source_lineage` is the lifecycle-boundary guard for closeout and integration. It
recomputes the full task-derived chain and raises a status-bearing refusal for stale or unavailable
lineage. Its summary now says task-bound work cannot continue, because admission applies both when
a seat begins and again before an irreversible lifecycle edge.

## Invariants And Boundaries

- Task and contract identity own lineage discovery; agents never carry branch,
  runtime, or session identity to this policy.
- Missing or unreadable contracts and incomparable branches are unavailable,
  never implicitly current.
- `proceed-stale` cannot override source-lineage admission. It belongs to the
  separate stale-base decision after ancestry has been proved.
- External-memory edges are mandatory when the parent or current contract says
  memory is external; disabled/internal memory does not invent such an edge.
- Recovery points at the contract whose descendant branch must be synchronized,
  and never performs the synchronization during admission.
- Linked worktrees are the same repository only when Git reports the same resolved common
  directory; their distinct checkout paths are not repository identities.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical task altitude selects the correct contract and missing-edge relation. | `source_lineage_for_task` | mcp/src/agents_remember/worktrees/source_lineage.py:40-64 |
| Leaf pre-mutation admission proves the parent series edge. | `parent_source_lineage` | mcp/src/agents_remember/worktrees/source_lineage.py:67-79 |
| Contract admission composes the complete series or transitive leaf projection. | `source_lineage_for_contract` | mcp/src/agents_remember/worktrees/source_lineage.py:82-95 |
| The generic lifecycle guard refuses a stale or unavailable transitive chain. | `require_current_source_lineage` | mcp/src/agents_remember/worktrees/source_lineage.py:113-126 |
| Refusal and blocked-payload helpers publish one recovery shape. | `lineage_refusal`; `lineage_block_payload` | mcp/src/agents_remember/worktrees/source_lineage.py:98-140 |
| Linked-edge validation prevents a leaf from naming an unrelated parent source. | `_linked_edge` | mcp/src/agents_remember/worktrees/source_lineage.py:220-237 |
| Repository equality routes both paths through the shared Git-identity helper so sibling worktrees compare as one repository. | "def _same_repo(" | mcp/src/agents_remember/worktrees/source_lineage.py:254-257 |
| The shared helper resolves Git's common directory as repository identity. | "def repository_identity(" | mcp/src/agents_remember/worktrees/modules/git.py:70-79 |
| Git facts become strict edge states and ordered sync recoveries. | `_edge`; `_projection` | mcp/src/agents_remember/worktrees/source_lineage.py:244-312 |

## Update History

- 2026-08-14T05:26Z — L23 final curator: corrected repository-identity ownership after the helper
  moved into the shared worktree Git module; lineage still compares resolved common directories and
  fails closed. Verification remains closeout-owned.
- 2026-08-13T09:27+02:00 — L23 curator: replaced checkout-path identity in the documented lineage
  boundary with Git's resolved absolute common-directory identity, preserving fail-closed behavior
  for absent or unresolvable repositories. Verification metadata remains closeout-owned.

- 2026-08-13T08:40+02:00 — L23 integration-gate repair: generalized the lineage summary beyond seat admission and documented the reusable full-chain guard now enforced at closeout/integration preflight and their last reversible boundary. Verification metadata remains closeout-owned.

- 2026-08-12T20:10+02:00 — 260731-EFA-L23 curator: created for task-derived, transitive code/external-memory source-lineage admission. Verification remains pinned to the leaf base until closeout assigns the dirty source a real commit identity.
