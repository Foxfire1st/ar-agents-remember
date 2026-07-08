# l-01-agent-lifecycles/roles/curator.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/curator.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-08T00:00+02:00 |
| lastVerifiedCommitHash |                                            `c72deebadb4a96740cf955999d51a00d93c181d2`|
| lastVerifiedCommitDate |                                            2026-07-08T02:19:03+02:00|

## Purpose

The portable **curator** lifecycle: a fresh per-leaf onboarding writer spawned after builder code
and reviewer verdict are available. As of 260707-HFX-L11 it is spawned from a dedicated
`../templates/curator-brief.md` dispatch pack that FEEDS it three inputs (never inferred from
transcript memory): the leaf's landed change set, the leaf task doc, and notes/. It writes
onboarding only — file sidecars, route overviews when affected, generated route indexes, and the
repo entity catalog when a real entity changed — then returns a memory-pass report for the
manager's leaf closeout packet.

## Code Commentary

### Logic

This is a sync-propagated (`scripts/sync-skills.py`) package-data copy of the canonical
`skills/l-01-agent-lifecycles/roles/curator.md`. The role ratifies the L6R3 curator seat in the
manager -> builder -> reviewer -> curator chain, and 260707-HFX-L11 activates it: change-set
feeding (R1), the c-12/c-05 process rewiring that moves onboarding-authoring duty off the builder
and onto this seat (R2/R3), and the manager wiring that makes the chain enforced rather than
descriptive (R4).

**What This Seat Is** now names the fed inputs explicitly: the brief FEEDS the curator the leaf's
landed change set (code diff over the leaf's base-to-head range, with counters/paths — the manager
pulls this from the leaf contract's recorded range, not a guess), the leaf task doc, and notes/ (the
builder turn report and, when the leaf ran a loop, the reviewer verdict). A new paragraph states the
seat-routing rule plainly: during leaf work, onboarding create/update duty belongs to this seat, not
the builder — the builder produces code + a turn report only (`../roles/worker.md`), and this seat
is where `c-05-create-or-update-onboarding-files` runs; the strict 1-to-1 source mapping,
governing-overview links, and metadata rules that skill enforces are unchanged, only the writing
seat moved. The closing-seat binding is now explicit too: the `c-12-closeout` skill's
missing-onboarding and changed-sidecar checks are satisfied by THIS pass, before the manager ever
runs the closeout preview — a check still failing after this pass is a closeout failure escalated
back to a respawned curator pass, never something the closing seat patches inline.

Intake (step 1) now names the FED change-set explicitly (paths + counters over the leaf's
base-to-head range) instead of a generic "changed-path list." Step 3 ("Write Onboarding Only") now
opens with the mgmt-L4 routing rule stated in full: route every change-set item and every notes/
item to the RIGHT onboarding home (a source file's own sidecar; the nearest governing route-local
overview for route/package-shape changes; the repo entity catalog only for a real load-bearing
cross-layer change; the L3 Operational-Notes target as LAST RESORT ONLY) — overview-dumping is
rejected as a default, not just discouraged.

The loop remains: brief -> intake -> inspect diff + evidence -> write onboarding -> indexes/checks ->
memory-pass report -> end. Code worktree access is read-only for changed source confirmation. Memory
worktree writes are limited to onboarding surfaces: sidecars, route overviews when route meaning
changed, generated route indexes through local `build_route_indexes(...)`, and entity catalog
entries only for real load-bearing entity changes. The curator uses the c-05 file-level onboarding
workflow for sidecars and catalogs.

The curator never writes code, never decides gates, never mutates task-doc state, and never performs
closeout, integration, or finalization. The manager closes a leaf from builder code + reviewer
verdict + curator memory pass — now an enforced sequencing rule (`roles/manager.md`: "do not run the
closeout preview before this pass exists"), not just a descriptive line.

### Invariants And Boundaries

- One fresh curator seat per leaf memory pass.
- Onboarding writes only; code and AR state are out of scope.
- The curator is FED its change-set/task-doc/notes inputs via `../templates/curator-brief.md`; it
  never infers a change set from transcript memory, and asks the owning seat for one clarification
  row when evidence is missing or ambiguous.
- Every routed item goes to the specific sidecar or governing overview whose subject it is; the L3
  Operational-Notes target is last-resort only, never a default.
- Role-seat immutability applies in dashboard-owned sessions; a curator never absorbs another role
  brief.
- The memory-pass report is the durable output consumed by the owning seat; the `c-12-closeout`
  gates are bound to it (doctrinally — the underlying checks remain role-agnostic on-disk checks,
  per this leaf's doctrine-review Note C).

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | n/a | [curator.md](agents-remember/skills/l-01-agent-lifecycles/roles/curator.md) |
| The l-01 spine that registers curator, lists `curator-brief` among the on-disk templates, and documents the role-seat immutability rule. | n/a | [SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/SKILL.md) |
| Manager lifecycle that compiles the curator-brief, spawns a fresh curator per leaf, and consumes the memory-pass report; gates the closeout preview on this pass existing. | n/a | [manager.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/manager.md) |
| Worker lifecycle that produces changed paths and code-diff evidence for the curator (builder = code + report only). | n/a | [worker.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/roles/worker.md) |
| The dispatch-pack template this leaf added; the curator's entire session start is compiled from it. | n/a | `agents-remember/skills/l-01-agent-lifecycles/templates/curator-brief.md` (new; onboarding sidecar to be created this pass) |
| `c-12-closeout` skill, now framed as verifying (not authoring) the curator's onboarding output. | n/a | [c-12-closeout SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-12-closeout/SKILL.md) |
| `c-05-create-or-update-onboarding-files` skill, whose "Seat routing" paragraph names the curator as the seat that runs it during leaf work. | n/a | [c-05-create-or-update-onboarding-files SKILL.md](agents-remember/mcp/src/agents_remember/package_data/runtime/skills/c-05-create-or-update-onboarding-files/SKILL.md) |

## Cross-Repo References

No sibling repository evidence is needed for this orchestration role file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-08T00:00+02:00 — 260707-HFX-L11 curator activation (R1/R2/R3/R4): rewrote "What This
  Seat Is" to describe the fed inputs (landed change set + task doc + notes/, delivered via the new
  `../templates/curator-brief.md`, never inferred from transcript memory), the seat-routing
  statement (builder = code + report only; curator = where c-05 runs), and the explicit binding of
  the c-12 missing-onboarding/changed-sidecar checks to this pass (a still-failing check escalates
  to a respawned curator pass, never patched inline by the closing seat). Intake (step 1) now names
  the FED change-set explicitly; step 3 opens with the mgmt-L4 routing rule in full (sidecar >
  governing overview > entity catalog > L3 Operational-Notes last-resort; overview-dumping rejected
  as a default). Removed the prior "this role deliberately does not implement change-set feeding,
  c-12 rewiring, or c-05 process rewiring" sentence — that scope is exactly what this leaf lands.
  Doctrine-only change set (60 files: 6 canonical `skills/` edits + 1 new template, each synced to 9
  mirrors, 0 Python); sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-01-agent-lifecycles/roles/curator.md`. Verification metadata pinned — no commit yet on
  `ar/260707-hfx-l11-curator-activation` (working-tree change); this memory pass is itself dogfooding
  the new curator-brief template (the first leaf dispatched with it).
- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: created onboarding for
  the new dedicated onboarding-writer lifecycle, including fresh per-leaf spawn, builder/reviewer
  inputs, onboarding-only write scope, local route-index regeneration, memory-pass reporting, and
  the explicit boundary excluding code edits, AR state, closeout, change-set feeding, and c-12/c-05
  rewiring. Verification metadata is blank until closeout stamps the first commit containing this
  new package-data source file.
