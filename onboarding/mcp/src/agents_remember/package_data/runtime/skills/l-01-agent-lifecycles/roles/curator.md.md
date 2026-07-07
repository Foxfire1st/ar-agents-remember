# l-01-agent-lifecycles/roles/curator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-07T21:40+02:00 |
| lastVerifiedCommitHash |                                            `2c464cf4c29b60165fecae722bf76c307aaac6f1`|
| lastVerifiedCommitDate |                                            2026-07-07T22:59:19+02:00|

## Purpose

The portable **curator** lifecycle: a fresh per-leaf onboarding writer spawned after builder code
and reviewer verdict are available. It writes onboarding only — file sidecars, route overviews when
affected, generated route indexes, and the repo entity catalog when a real entity changed — then
returns a memory-pass report for the manager's leaf closeout packet.

## Code Commentary

### Logic

This is a sync-propagated (`scripts/sync-skills.py`) package-data copy of the canonical
`skills/l-01-agent-lifecycles/roles/curator.md`. The role ratifies the L6R3 curator seat in the
manager -> builder -> reviewer -> curator chain. Intake reads the curator brief, leaf task doc,
builder turn report, reviewer verdict, changed paths/code-diff evidence, and named notes. If the
change evidence is missing or ambiguous enough that onboarding would become guesswork, the curator
asks the owning seat for one clarification row instead of reconstructing a diff from transcript
memory.

The loop is: brief -> intake -> inspect diff + evidence -> write onboarding -> indexes/checks ->
memory-pass report -> end. Code worktree access is read-only for changed source confirmation. Memory
worktree writes are limited to onboarding surfaces: sidecars, route overviews when route meaning
changed, generated route indexes through local `build_route_indexes(...)`, and entity catalog
entries only for real load-bearing entity changes. The curator uses the c-05 file-level onboarding
workflow for sidecars and catalogs.

The curator never writes code, never decides gates, never mutates task-doc state, and never performs
closeout, integration, or finalization. This L6R3 source deliberately does not implement change-set
feeding, c-12 rewiring, or c-05 process rewiring; those remain outside this leaf. The manager closes
a leaf from builder code + reviewer verdict + curator memory pass.

### Invariants And Boundaries

- One fresh curator seat per leaf memory pass.
- Onboarding writes only; code and AR state are out of scope.
- Role-seat immutability applies in dashboard-owned sessions; a curator never absorbs another role
  brief.
- The memory-pass report is the durable output consumed by the owning seat.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [curator.md](agents-remember/skills/l-01-agent-lifecycles/roles/curator.md) |
| The l-01 spine that registers curator and documents the role-seat immutability rule. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| Manager lifecycle that spawns a fresh curator per leaf and consumes the memory-pass report. | n/a | [manager.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md) |
| Worker lifecycle that produces changed paths and code-diff evidence for the curator. | n/a | [worker.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: created onboarding for
  the new dedicated onboarding-writer lifecycle, including fresh per-leaf spawn, builder/reviewer
  inputs, onboarding-only write scope, local route-index regeneration, memory-pass reporting, and
  the explicit boundary excluding code edits, AR state, closeout, change-set feeding, and c-12/c-05
  rewiring. Verification metadata is blank until closeout stamps the first commit containing this
  new package-data source file.
