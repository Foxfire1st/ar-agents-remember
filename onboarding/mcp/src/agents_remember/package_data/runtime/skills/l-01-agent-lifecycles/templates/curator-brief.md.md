# l-01-agent-lifecycles/templates/curator-brief.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/curator-brief.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T15:48+02:00 |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|

## Purpose

The curator dispatch packet — the first dedicated dispatch-pack template for the curator seat
(260707-HFX-L11, R1/R4). The manager (or the architect in a flat series) compiles a curator's
entire session start from this shape, fresh per leaf, after builder code exists and the reviewer
verdict is available. It is the change-set feeding contract: the curator never infers a change set
from transcript memory, it is FED the landed change set, the leaf task doc, and notes/ as inputs.

## Code Commentary

### Logic

**260707-HFX2-L15 reviewer N7 current-source debt.** The source brief's delivery footer still says
`echo-confirmed`/post-boot echo. The current runtime contract is unique-id evidence in the bound
harness log; pane text is not acceptance. This note preserves the mismatch for the doctrine owner
without changing the brief from the curator seat.

New file, sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/templates/curator-brief.md`. Opens with the canonical `ROLE BRIEF —
curator` header line (the router's condition-2 recognizer) followed by a `# CURATOR BRIEF —
<leaf-id> · <leaf title>` line. Placeholder blocks: **Worktrees** (code worktree read-only, memory
worktree the only write surface, with branch/base facts); **The landed change set (fed, not
inferred)** — code diff over `<base-commit>..<worker-head-commit-or-HEAD>` with a changed-path
list or dashboard change-set view reference (`/api/changeset/task` scope, or the leaf's
`committed`/`working` change-set), any pre-existing memory-diff carry-forward, and counters
(files/insertions/deletions) the manager attached — the curator must not re-derive these from its
own guess; **Task inputs** — the leaf task doc path and the notes/ path (builder turn report,
reviewer verdict when the leaf ran a loop, other factual current-state clarifications); the
**Routing rule (mgmt-L4 design)** stated in full and enforced before any writing: (1) a concrete
source file's own sidecar when the change is about that file's behavior, (2) the nearest governing
route-local overview when the change is about route/package shape or crosses several files in one
route, (3) the repo entity catalog only for a real load-bearing cross-layer entity change, (4) the
L3 Operational-Notes target as LAST RESORT ONLY — overview-dumping is rejected; the **Tool surface**
(native reads in the code worktree, native reads/edits in the memory worktree, the c-05 workflow,
local `build_route_indexes(...)`, inbox for one clarification row, explicit exclusion of
`worktree_*`/`lifecycle_*`/`task_doc`/`gate_*`/`memory_quality_check`-mutating tools and code
edits); **Checks** (`git diff --check` in the memory worktree, plus any onboarding/reference checks
the brief or role file names); and the **Memory-pass report** obligation (write
`<notes-reports-path>/<leaf-id>-curator-report.md` naming which change-set/notes item each changed
onboarding file routes to and why, route index results, reference checks, blockers, exact commands
run — this report plus the builder's code and the reviewer's verdict are exactly the manager's
three closeout inputs).

Compiler notes bind the manager: fill every placeholder (an unresolved placeholder makes the brief
non-dispatchable); pull change-set counters/paths from the leaf's actual landed range (contract's
recorded base commit through the builder's current HEAD/worktree state), never a stale or guessed
diff; attach the builder turn report and (when the leaf ran a loop) the reviewer verdict as the
notes/ inputs so the curator never re-requests evidence that already exists in `notes/reports/`;
deliver as an echo-confirmed paste; and this brief runs strictly AFTER builder code exists and the
reviewer verdict (when the leaf tier requires one) is available — never before, never in place of
either.

As of 260707-HFX2-L17, spawning with `AR_SPAWN_ROLE=curator` and the qualified leaf key is
documented as one pair claim for the curator's `(leaf, role)` seat. That pair identity lets the
curator use the same canonical leaf as the worker and reviewer without role-suffixed leaf keys.

### Conventions

Mirrors the `worker-brief.md`/`manager-brief.md` compiler-notes convention: a spawning seat compiles
the brief FROM the template, fills every placeholder, and the brief IS the fresh session's entire
start (it replaces the front half the spawner already ran). The template forces a real
base-to-head range and real notes/ paths before dispatch — closing the gap where "change-set
feeding" could otherwise be satisfied by a manager pasting a vague summary.

### Invariants And Boundaries

The curator-brief template must not be dispatched with unresolved placeholders, must not be used
before builder code exists, and (when the leaf tier runs a loop) must not be used before the
reviewer verdict is available. The curator it spawns is barred from inferring a change set from
transcript memory and must ask the owning seat for one clarification row instead when the fed
evidence is missing or ambiguous. Its task-seat claim is the qualified leaf plus `curator` role,
not a curator-suffixed leaf key.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Canonical source this bundle copy is sync-propagated from. | `# Template — Curator Brief` | skills/l-01-agent-lifecycles/templates/curator-brief.md:1-105 |
| The l-01 spine's Companion Files registry, which lists this template among the on-disk templates. | `## Companion Files` | skills/l-01-agent-lifecycles/SKILL.md:372-387 |
| The curator role lifecycle this brief is the session start for. | `# Lifecycle — Curator` | skills/l-01-agent-lifecycles/roles/curator.md:1-132 |
| The manager role lifecycle that compiles this brief and gates the closeout preview on the resulting memory pass. | `### 2 — Leaf dispatch loop (per leaf)` | skills/l-01-agent-lifecycles/roles/manager.md:95-174 |
| `manager-brief.md`'s Dispatch defaults section, updated in the same leaf to reference this template. | `AR_SPAWN_ROLE` | mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/manager-brief.md:38-43 |

## Cross-Repo References

No sibling repository evidence is needed for this doctrine file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-08-03T02:32:19+02:00 — Curator W3-B02 repaired 5 Repo-Internal citation rows, resolving 10 manifest findings with exact current headings and code-repository-relative sources; verification metadata was preserved.
- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: documented
  `AR_SPAWN_ROLE=curator` plus the qualified leaf as the curator's `(leaf, role)` pair claim, with
  no role-suffixed leaf key. Verification metadata remains pinned until closeout stamps the L17
  commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 reviewer N7: recorded the stale echo-confirmation footer
  as doctrine debt; no source behavior changed.

- 2026-07-08T00:00+02:00 — 260707-HFX-L11 curator activation (R1/R4): created file-level onboarding
  for the new `curator-brief.md` dispatch-pack template — the first dedicated curator session-start
  artifact, closing the gap where change-set feeding was doctrine text with no concrete brief shape.
  Doctrine-only change set (60 files: 6 canonical `skills/` edits + this new template, each synced
  to 9 mirrors, 0 Python); sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
  `skills/l-01-agent-lifecycles/templates/curator-brief.md`. Verification metadata blank — no commit
  yet on `ar/260707-hfx-l11-curator-activation` (working-tree change; new file, never previously
  onboarded).
