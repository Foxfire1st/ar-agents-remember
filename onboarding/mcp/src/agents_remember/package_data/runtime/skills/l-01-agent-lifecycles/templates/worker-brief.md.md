# l-01-agent-lifecycles/templates/worker-brief.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/package_data/runtime/skills/l-01-agent-lifecycles/templates/worker-brief.md` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-07-10T15:48+02:00 |
| lastVerifiedCommitHash | `79b2fd6c4da73c7845406f6c68b947b8bd0e1009`                                  |
| lastVerifiedCommitDate | 2026-07-10T22:22:16+02:00|

## Purpose

The institutionalized worker dispatch packet: the template a spawning seat (manager, or the
architect in a flat series) compiles a worker brief from. The brief is the worker's **entire
session start** — it replaces the front half the spawner already ran (trust checkpoint, reframe,
plan). This template turns the proven dispatch shape of the 260703 series (leaves L3–L8) into
doctrine and, as of L6R3, makes the worker the builder input for a separate curator memory pass.
It still absorbs the old dispatch frictions: route-index leaks into the official checkout (F-E),
provider-stack keying confusion (F-H), and the missing `python` shim in spawn environments (F-I).

## Code Commentary

### Logic

**260707-HFX2-L15 reviewer N7 current-source debt.** The source brief still instructs an
`echo-confirmed`/paste-chip dispatch check. L15 removes screen rendering as acceptance authority;
the future doctrine edit must say that the id-bearing input is accepted from the bound harness log,
with pane text restricted to duplicate-retry safety and failure diagnostics. This onboarding note
records the mismatch; it does not pretend the unchanged source has already been fixed.

Sync-propagated (`scripts/sync-skills.py`) bundle copy of the canonical
`skills/l-01-agent-lifecycles/templates/worker-brief.md`. The template body is a fenced markdown
brief with `<placeholder>` slots: leaf identity, the code worktree plus memory context path with
branch/base, the positive tool-surface statement (native edits, read-only AR retrieval with the
`read_ar_files`-serves-official-baseline caveat and the provider stack key or NONE, no mutating AR
tools, local `build_route_indexes` for generated indexes, explicit interpreter path — no `python`
shim), the task statement, the checks ladder (focused + full wrapper + `git diff --check`), a
curator handoff-input block (changed paths, code-diff summary, tests, route/onboarding observations,
and the pin idiom for the curator), and the mandatory turn-report path. Compiler notes bind the
spawning seat: fill every placeholder (an unresolved placeholder is not dispatchable), verify the
provider stack answers before naming it, spawn with `env={"AR_SPAWN_ROLE": "worker"}` and the
qualified leaf key as one pair claim for the worker's `(leaf, role)` seat, deliver as an
echo-confirmed paste and only count delivery on a post-boot echo.

As of cycle 5: the fenced brief opens with the canonical ROLE BRIEF — worker line (uniform with manager-brief).

## Cross-Repo Evidence

No sibling repository evidence is needed for this doctrine file.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-07-10T15:48+02:00 — 260707-HFX2-L17 generated-runtime doctrine delta: the worker dispatch
  contract now states that `AR_SPAWN_ROLE=worker` and the qualified leaf together claim the
  worker's `(leaf, role)` seat. Verification metadata remains pinned until closeout stamps the L17
  commit.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15 reviewer N7: recorded the stale echo/paste-chip
  instruction as current source debt awaiting a doctrine follow-up. No source behavior changed.

- 2026-07-07T21:40+02:00 — 260707-HFX-L6R3 curator seat: worker briefs now state
  the manager -> builder -> reviewer -> curator closeout chain, mark the memory worktree as
  context for changed-path notes, and require curator handoff input instead of same-pass onboarding
  writes by the worker. Sync-propagated bundle copy. Verification metadata pinned until closeout
  stamps the HFX-L6 commit.

- 2026-07-05T18:20+02:00 - L8 seam channel (cycle 5): the fenced brief opens with the canonical ROLE BRIEF — worker line (uniform with manager-brief).. Verification metadata pinned until closeout stamps the L8 commit.
- 2026-07-05T01:30+02:00 - Created file-level onboarding for the new worker-brief template (L9
  lifecycle convergence): the proven L3–L8 dispatch shape institutionalized, absorbing frictions
  F-E/F-F/F-H/F-I. Verification metadata pinned until closeout stamps the L9 commit.
