# dashboard/src/panels/lifecycle-list/hierarchy.test.tsx

## Governing Overview

[panels/ overview](../overview.md)

## Purpose

The hierarchy/phase-grouping suite split from `LifecycleList.test.tsx` by the
260731-EFA-L8 test split. Pins row grouping, phase ordering, and collapsible
hierarchy behavior of the Operations list.

Since 260921-ICR-L33 it also owns a second `describe` — **"LifecycleList landed leaves under their
master (R33)"** — which is where the Operations list's landed-leaf admission and its default-collapse
rule are measured.

## Code Commentary

### Logic

Seeds the collapsible hierarchy projection and asserts group headers, phase
ordering, and re-show behavior.

### Invariants And Boundaries

Assertions preserved from the monolithic suite; shared cleanup from
`test-utils.tsx`.

### Todos

None recorded.

## Evidence

### Docs References

The curator checked `system/sources.md`; no Domain Documentation source is
configured for this file.

No relevant domain documentation was found.

### Repo-Internal References

- The hierarchy/grouping suite. [1]

### Cross-Repo References

No cross-repository implementation source governs this file.

No applicable cross-repository source was found.

## 260921-ICR-L33 The Landed-Leaf Cases

Five cases, in a `describe` of their own, measure `ICR-R33` — and one of them is the only delivered
protection the row-carries-rows exclusion has.

- **`holds a fully landed master closed by default and reaches its leaf when opened (R33.1/R33.4)`**
  (`:416-448`) — a dead-worktree enclosure with a `Completed` leaf renders one closed master row
  (`Tasks · 1`), and one click on its disclosure makes the leaf reachable at `data-depth="1"`,
  `data-parent-key=taskdoc:/tasks/master-a/task.json`, `data-landed="true"`, selectable as
  `taskdoc:/tasks/master-a/01_landed-leaf.json`, `Tasks · 2`.
- **`shows a master's landed leaves beside its live ones without a click (R33.1)`** (`:449-477`) — a
  master that still holds live work is open by DEFAULT, so its landed leaves are rendered with no
  interaction at all.
- **`never closes a row that carries OTHER rows, even when its own work has all landed (R33.4)`**
  (`:478-602`) — an orchestration row with landed leaves of its own that also commands another master,
  every worktree dead. It asserts the commander is NOT auto-collapsed (`data-auto-collapsed` is null,
  its disclosure reads "Collapse Commander tasks" with `aria-expanded=true`), that the commanded master
  is reachable without a click, **and** that the commanded master — whose only children are its own
  landed leaves — is itself still closed with its leaf not forced open, so the rule stays targeted
  rather than becoming "never collapse anything". Deleting
  `(structuralChildren.get(row.key) ?? 0) === 0` from `markAutoCollapsed` turns the full delivered suite
  from `1708 passed` into `1 failed | 1707 passed` — this case, at its line-584 assertion — and
  replacing the rule outright (never auto-collapse) fails its targeting assertions at 598-599; both
  mutations were run by the verifier in scratch copies outside the worktree, so the case is not passing
  for the wrong reason in either direction.
- **`counts the task entries it carries, not the projection's documents (R33.4)`** (`:603-691`) — the
  header counts ENTRIES, and the case pins the `h2`'s own tooltip sentence as well as the count, so the
  sentence cannot drift away from the number it explains (perturbing either the production string or
  the expected substring fails it).
- **`keeps a landed leaf that no series index resolves out of the list (R33.4)`** (`:692-`) — a
  boundary guard rather than fix evidence: it passes on the base too, and it exists because floating an
  unindexed landed leaf to the top of the list is the plausible regression this rule invites. It is the
  case the residual disclosure rests on: one real landed leaf
  (`260713_turn-aware-expectation-supervision/05a_bootstrap-approval-hotfix.json`) is deliberately not
  floating, so "a landed master's leaves are reachable" is not unconditional.

The suite's own row is re-derived for this leaf's growth (`19-321` → `19-355`); no pre-existing case was
re-worded or weakened.

## 260821-CLIVE Discarded Progress Proof

The suite now proves that a planning master with one live leaf and one discarded-before-start entry
renders `0/1 · 1 discarded`, explicitly not `1/1`. This preserves the distinction between audited
removal and completed execution while leaving hierarchy, phase grouping, collapse behavior, and
long-title coverage unchanged.
