# README.md

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `README.md`                                |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-03T12:30:00+02:00 |
| lastVerifiedCommitHash | `685f83c4405570ca8356e7481e0e2a9a16945757` |
| lastVerifiedCommitDate | 2026-09-02T11:38:00+02:00 |
| governingOverview      | `overview.md`                              |

## Governing Overview

[overview.md](overview.md)

## Purpose

`README.md` is the public front door for Agents Remember. It gives a concise product-level explanation, a high-signal Core Features section, a short quickstart, a Run The Dashboard section (260703 L3 — the first-class CLI install/run story), links to harness-specific install pages, optional benchmark guidance, and a compact repository/runtime map. The concentrated feature tour now lives in `docs/features.md`; detailed setup, concepts, workflows, benchmark methodology, guides, and reference material live under `docs/`.

## Code Commentary

### Logic

The README's `<h3>` headline now frames Agents Remember in two parts — git-verified records of what coding agents know, and a control plane for what they do — sharpening the earlier single-line "durable" framing toward the records-plus-control-plane positioning. Below it, the README uses `## Core Features` as the fast product pitch. It frames Agents Remember as project memory coding agents can verify and act on, shows the source-file to onboarding-unit mapping, and names the user-facing features a skimming reader needs in the first thirty seconds: path-addressed memory, Git-proven freshness, optional semantic/code-graph discovery that finds but does not decide, memory that lands with code through external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and harness-ready first-run packages. The previous `## Core Model` section carried the same conceptual spine but was less effective as a public feature pitch.

The previous MCP-installs-skills first-run model was replaced with package-first
harness setup. The root page now keeps one short, harness-agnostic three-step
quickstart that the agent drives: (1) copy the harness-native starter package
from the repo and render the copied package. The `render-starter` script is a
convenience that infers the workspace root from the copied harness folder, takes
one explicit `--repo` list such as `--repo my-app shared-lib`, and fills path,
repository, and hook-command placeholders; the docs also allow manual
placeholder replacement. The package provides skills, hooks, rules,
instructions, MCP settings templates, and rendered hook commands; (2) wire the
published
`agents-remember-mcp` package with `uvx agents-remember-mcp@latest --config
<abs>/agents-remember-settings.json`, then restart the harness once so it loads
the MCP server and native package files; (3) invoke `c-13-install-and-onboard`,
which runs or verifies `runtime_install()`, asks scaffold-new vs existing memory,
bootstraps onboarding when needed, and starts provider indexing when enabled.
`skills_install()` remains documented as maintenance/manual, not the normal
first-run path. Harness-specific setup links point to dedicated pages under
`docs/install/`, and detailed first-run setup lives in `docs/getting-started.md`.

The README distinguishes the source checkout from the installed runtime. The
source checkout exposes root `skills/` as the canonical skill source tree and
`scripts/sync-skills.py` as the helper that refreshes MCP package-data and
harness package skill copies. It also exposes root `agents-md-files/`,
`benchmarks/`, `providers/`, and `system/` as canonical runtime asset source
folders and `scripts/sync-runtime.py` as the helper that refreshes MCP
package-data copies only. The installed `ar-coordination/` runtime owns
installed instructions, skills, optional benchmark package content, local
coordination artifacts, external memory repos, worktrees, and temp files. The
Repository Layout section states the installed runtime defaults to
`<workspace>/ar-coordination/` — inside the workspace, never the user's home
directory — and points at the `c-13-install-and-onboard` skill, which presents
that and every other install path as a workspace-first accept-or-override
default.

A `## What It Looks Like In Practice` mini-transcript sits between Core Features and the Live Demo: it shows a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-onboarding-then-propose-then-refresh loop — a concrete picture of the by-path loop for skimming readers.

The post-quickstart workflow sentence now speaks the current `l-01-agent-lifecycles` vocabulary:
developer-facing free chat answers research inline and, for ordinary role-shaped work, compiles the
canonical architect brief and calls `dispatch_agent` once on the sprint document. An explicit
developer-declared task-seat takeover targets the named role on its canonical document instead. The identity-free launcher
hands over only after the exact brief is durable. Hosted seats use the same tool under structural
authority, and a plane refusal never falls back to ambient. Spawned backend orchestrators and
other role seats then follow their role briefs. The
named build modes remain the research-only exit, the `w-02-light-task-workflow` skill task, and the
master + light sub-task series (the chat build is retired — chat is never a build route). The
Status section's 3.0-arc paragraph likewise says "a system-managed agent lifecycle" instead of the
retired "session job lifecycle" phrase.

A ToC-linked `## Run The Dashboard` section (260703 L3) sits between Quickstart and
Documentation. It leads with the **unpinned** install as the first-class citizen —
`uv tool install agents-remember-mcp` then `agents-remember dashboard` (no `--config`:
L1's discovery walks up from the working directory) — then daemon mode
(`--daemon`/`--status`/`--stop`, state under `<coordinationRoot>/logs/dashboard/`) and the
`"dashboard": {"autoStart": true}` settings key (L2), presents version pinning
(`==X.Y.Z`, `uvx --from`) as the debugging/repro path, and closes with one pre-release
note: until 3.0.0 final the dashboard ships in `3.0.0rcN` pre-releases that default
resolution skips — `uv tool install --prerelease allow` or an explicit pin, including for
the MCP registration instead of `@latest`. The committed reproducibility examples and Status
line now name `3.0.0rc7`, while the surrounding guidance stays version-generic so later release
bumps remain mechanical. Every documented command was verified against
real PyPI resolution (unpinned resolves the latest stable; `--prerelease allow` resolves
the rc).

A short `## Live Demo` section sits between Core Features and Requirements. It states that Agents Remember runs on itself and links the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable example of the by-path onboarding layer. It surfaces the dogfooding message higher on the page than the existing Contributing-section mention, which still owns the operational instruction to clone that memory and use it while contributing.

The Requirements section now states the bounded Python 3.13 package line and points repository
developers to the exact source-built 3.13.15 contract in the MCP README. The root README remains a
public orientation layer; the executable bootstrap and provenance contract stay under `scripts/`.

### Conventions

- Keep the README short enough to scan.
- Use the README to orient and route, not to carry full setup matrices or reference material.
- Use `docs/` for user-facing docs, `benchmarks/` for optional benchmark fixtures, `AGENTS.md` and installed runtime templates for agent behavior, and onboarding for durable repository knowledge.
- Keep public language focused on the current intended install model: copy a harness starter package, wire the MCP server, run/verify `runtime_install()` through `c-13-install-and-onboard`, and store memory in either repo-local `ar-memory/` or selected external memory repos.
- Avoid presenting the public README as a source-package explanation or compatibility guide for old alpha layouts.

### Invariants And Boundaries

The README is explanatory, not the implementation source of truth. Runtime behavior belongs to MCP tools, package services, and skills. If README guidance disagrees with helper behavior, verify helper behavior before changing operational assumptions.

The public prerequisite must remain aligned with `mcp/pyproject.toml` (`>=3.13,<3.14`) and must not
imply that uv may silently select an arbitrary managed Python for repository development.

`docs/**` is currently excluded from file-level onboarding by this repository's path rules, so this README onboarding is the durable file-level companion for the public documentation front door. Repo-level overview onboarding should carry broad documentation-structure context when the docs tree changes.

### Todos

- If `docs/**` becomes eligible in path rules later, create focused file-level onboarding for high-value docs pages instead of overloading this README onboarding.

### Docs References

The README itself no longer depends on external harness docs for detailed setup claims; those claims live in the dedicated install pages.

| Finding | Anchor | Source |
| --- | --- | --- |
| No external documentation is needed to prove the root README's current structure; it is a same-repository public overview and link hub. | n/a | n/a |

## Repo-Internal References

The README routes readers into the split documentation tree and gives the current runtime/source layout.

| Finding | Anchor | Source |
| --- | --- | --- |
| The README now has a `## Core Features` section that replaces `## Core Model`; it shows the source-file to onboarding-unit mapping, pitches path-addressed memory, Git-proven freshness, optional semantic/code-graph discovery, external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and harness-ready first-run packages, then links to `docs/features.md`. | `## Core Features` | README.md:45-62 |
| The README shows a `## What It Looks Like In Practice` mini-transcript: a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-then-propose-then-refresh loop. | `## What It Looks Like In Practice` | README.md:63-80 |
| The README has a `## Live Demo` section stating Agents Remember runs on itself and linking the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable by-path onboarding example. | `## Live Demo` | README.md:81-87 |
| The Requirements section names Python 3.13, the bounded package range, and the canonical repository-development runtime documentation. | `## Requirements` | README.md:88-100 |
| The quickstart is a short, harness-agnostic three-step agent-driven flow: copy the harness starter package, render it either with the convenience `render-starter` script or manual placeholder replacement, wire the MCP server with `uvx`, restart once, then invoke `c-13-install-and-onboard`; `skills_install()` is maintenance/manual because the package already carries the initial skills and harness files. | `## Quickstart` | README.md:101-137 |
| The README routes readers first to the new Features tour, then to setup, concepts, workflows, benchmark methodology, guides, settings, and skills documentation under `docs/`. | `## Documentation` | README.md:178-191 |
| The `## Run The Dashboard` section: unpinned `uv tool install` first-class, discovery-backed flag-free `dashboard`, daemon mode + autoStart, pinning as the debugging path, and the rc-period pre-release note. | `## Run The Dashboard`; "autoStart" | README.md:138-177 |
| The README keeps the source checkout layout distinct from the installed runtime layout, exposes root `skills/` as canonical, identifies `scripts/sync-skills.py` as the helper that refreshes generated skill copies, exposes root `agents-md-files/`, `benchmarks/`, `providers/`, and `system/` as canonical runtime assets, identifies `scripts/sync-runtime.py` as the package-data-only runtime asset helper, and notes the workspace-first `<workspace>/ar-coordination/` default. | `## Repository Layout` | README.md:192-298 |
| The README's Status section is a two-paragraph current-state + direction statement: paragraph one states the current version (bumped every release), the core-path maturity, the Stability deferral, the GitHub Releases routing (the repository's canonical changelog — this repo keeps no `CHANGELOG.md`, and Status no longer narrates per-release summaries), and the harness-maturity note; paragraph two, since the L14 release, states the SHIPPED 3.0 arc (observable, steerable sessions — lifecycle entity, durable approval gates, projection layer — served as the mission-control browser cockpit from the MCP package via the `agents-remember dashboard` CLI, #2/#43) with the rc caveat that the cockpit surface is still settling toward the final 3.0.0 contract. | `## Status` | README.md:299-304 |
| The Stability section is the semver promise: skill IDs, MCP tool names and their inputs/outputs, the `ar-coordination/`/`ar-memory/` layout, and the settings schema do not change without a major version bump; internals/provider internals/prompt wording may change in minor releases. | `## Stability` | README.md:310-313 |
| The Contributing section points contributors at CONTRIBUTING.md, restates the core rules, and tells contributors to download/clone the project's own published memory (Foxfire1st/ar-agents-remember) and use it as the active Agents Remember memory for their checkout while contributing (dogfooding the by-path onboarding loop). | `## Contributing` | README.md:314-318 |
| The docs index now includes `docs/features.md` as the concentrated product tour alongside getting-started, concepts, workflows, install guides, guides, and reference pages. | `# Agents Remember Documentation` | docs/README.md:1-65 |
| `docs/features.md` carries the full feature tour, including the new table of contents plus harness-native setup and operational guardrails for MCP authority, baseline adoption, branch carryover, cross-repo gates, benchmarks, and source quality tooling. | `# Memory your coding agent can trust` | docs/features.md:1-479 |

## Cross-Repo References

The README describes external memory in general terms, but this file-level onboarding does not rely on sibling repository internals.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found for the README itself. | n/a | n/a |

## Current Gate Paragraph (260731-EFA-L1 tiering, 260731-EFA-L2 honesty, 260731-EFA-L17 ladder)

The README's generated-copy section previously said "both hooks also run
`python -m agents_remember_test_support.code_quality.check`". That was retired by L1's tiering, and L2
then corrected what each tier actually enforces. The public contract the README now
states:

- Both hooks are thin wrappers over `.githooks/_gate.sh`, which takes the tier as its argument.
- **pre-commit** runs the fast tier over the **staged** content: the generated-copy checks
  (`sync-skills.py --check`, `sync-runtime.py --check`, **`sync-harness.py --check`**), plus
  Ruff, **`ruff format --check`**, and Pyright.
- **pre-push** repeats the deterministic non-test checks over current-checkout bytes and records
  pushed refs; it does not run acceptance.
- **"No rail carries a baseline or exemption list"** — the README states this outright. The
  complexity baseline that existed for one day inside this leaf is deleted, and the README
  never shipped a description of it.
- **Radon is printed as a report and cannot fail either tier — it exits 0 whatever it
  finds.** The README says so explicitly rather than listing it beside the enforcing steps.

- **Agents Remember acceptance runs through the pinned Dagger graph only**, declared in the
  repository-owned `mcp/certification-profile-v1.json` and selected explicitly by
  `repositories.agents-remember.certificationProfile` in the MCP authority settings (CCR-R22@v1,
  L22, commit `685f83c44055`). Leaf and focused work use its targeted mode; the master
  integration gate runs its full mode exactly once. Both require the leaf/master's explicit Git
  diff base; the framework does not discover a wrapper or carry an Agents Remember command/report
  inventory.

Note that `sync-dashboard.py` is **not** among the generated-copy checks — it is a release
build step with no `--check` mode, because the bundle it places is no longer in version control.

### The Repository Map Gained The Harness Source

The layout section now lists `scripts/sync-harness.py` ("generate the nine harness
configuration trees") and `scripts/harness/` ("canonical source for those trees") beside
`sync-skills.py` and `sync-runtime.py`, and a paragraph tells readers to edit
`scripts/harness/` and run the generator to regenerate `.claude/`, `.codex/`, `.cursor/`,
`.github-vscode/`, `.vscode/`, `.hermes/`, `.openclaw/`, `.pi/` and `.agents/`. It names
`mcp/tests/test_sync_harness.py` as running the same check inside the suite, so drift is
caught even without hooks.

## 260718-CHATS-L5I Current Delta

The README presents the repository's mission-control welcome capture immediately below the canonical documentation links. The image is a product illustration, not an onboarding source: its PNG path remains excluded by the memory path rules.

Its developer section states the commit-gate contract as a public default rather than an optional
strict mode: Ruff, Pyright, the full pytest suite, and the configured CRAP threshold are one
wrapper, and closeout runs it before creating a code commit. (The *distribution* of that wrapper
across the two hooks was retiered by 260731-EFA-L1, and the *step list* was corrected by
260731-EFA-L2 — see the current gate paragraph above, which supersedes both this entry's
"pre-commit and pre-push both run the wrapper" wording and its four-step enumeration.)

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## R39 Acceptance And Workflow Model

The README now distinguishes deterministic hooks and pull-request checks from lifecycle
acceptance. Pre-commit/pre-push and GitHub PR validation are non-test checks; leaf closeout owns
targeted Dagger once, leaf integration reuses the certified commit, and master integration owns
full Dagger once. Direct pytest, Playwright, changed-lines CLI, and Python-wrapper execution
refuse. Direct targeted Vitest is supported diagnostic feedback only. Retry proof is an internal,
attested-Dagger optimization rather than a host acceptance path.

## 260824-PDLS — Contributor-Facing Python Route

The README now says that Python investigation and acceptance both execute in the pinned Dagger
environment. Candidate A's host command, cohort manifest, static closure classifier, and self-proof
were deleted after representative exact-candidate measurement failed to justify their cost. The
seven unique product assertions remain ordinary explicit-lane pytest regressions. Non-accepting
Dagger evidence routes stay labelled and cannot publish lifecycle acceptance; direct targeted
Vitest remains the only supported host test diagnostic.

## Update History
- 2026-09-03T12:30+02:00 -- 260831-CCR memory curation pass for 685f83c44055 (CCR-R22@v1/L22): recorded the repository-owned profile declaration -- mcp/certification-profile-v1.json selected by repositories.agents-remember.certificationProfile -- replacing the qualityGate.executor settings wording in the acceptance bullet.
- Host `pytest` is refused and Candidate A's direct wrapper no longer exists. Deterministic
  non-test host checks are feedback only, and a failed Dagger run never falls back to the host.
- Direct targeted Vitest unit/component runs are supported as fast diagnostic loops only. They do
  not provide acceptance, changed-lines coverage, or lifecycle evidence. Playwright, pytest, and
  changed-lines CLI execution remain Dagger-owned; there is no direct Python wrapper.
- **GitHub PR validation** runs deterministic non-test checks once per pull request; ordinary
  pushes do not duplicate it and GitHub does not run acceptance.
- **Leaf closeout** runs targeted Dagger exactly once before creating the commit. Leaf integration
  lands that exact commit without a rerun; master integration owns the one full run.
- The tier table and the staged-content stash contract live in `CONTRIBUTING.md`; the README links
  there rather than duplicating them.


- 2026-08-30T12:34+02:00 — 260821-ARSPAWN-L3 adopted the one-call ambient launcher and
  plane-hosted `dispatch_agent` vocabulary in the public quickstart narrative, distinguishing
  ordinary architect bootstrap from explicit named-role takeover. Verification remains
  closeout-owned.

- 2026-08-29T16:27+02:00 — Reconciled the public prerequisite with the project-wide Python 3.13
  support line and routed exact source-build details to the MCP README.

- 2026-08-28T10:03:40+02:00 — Corrected the current contributor gate summary: host pytest refuses,
  Candidate A's wrapper is absent, and no Python compatibility route remains.

- 2026-08-28T05:10+02:00 — Reconciled the measured Candidate A retirement and preservation of its
  unique assertions without a host compatibility route.
- 2026-08-26T10:44:52+02:00 — Reconciled the contributor-facing diagnostic contract with the sealed direct-cohort manifest and fail-closed content-drift rules that replaced structural admission.

- 2026-08-24T21:23+02:00 — 260824-PDLS added the contributor-facing Python diagnostic boundary.

- 2026-08-24T13:51:26+02:00 — 260821-DAGQC-L4: recorded direct targeted Vitest
  as supported diagnostic-only feedback while preserving Dagger-only pytest, Playwright,
  changed-lines, direct-wrapper, and acceptance evidence. Removed the now-resolved
  changed-lines documentation-gap claim. Dagger acceptance remains closeout-owned.
- 2026-08-14T11:25+02:00 — R39 curator: recorded the no-duplicate workflow topology, direct-host
  refusal, and Dagger-only retry boundary. Verification remains closeout-owned.
- 2026-08-14T09:37+02:00 — Reopened L23 cadence: public guidance now distinguishes the
  pull-request-only non-test check from the single targeted leaf-closeout and full master-integration
  Dagger owners. Push, leaf integration, tag, and publish do not rerun acceptance; host pytest and
  direct-wrapper execution refuse instead of providing a diagnostic path.
- 2026-08-13T14:32+02:00 — L23 final curator pass: replaced the obsolete host-wrapper acceptance
  wording with the public Dagger-only contract: targeted leaf/focused runs, one full master
  integration run, mandatory explicit diff base, generated help as the argument contract, and
  host pytest/wrapper execution as diagnostics only. Verification remains closeout-owned.
- 2026-08-12T22:04+02:00 — 260731-EFA-L23 post-code curator: reconciled the committed `3.0.0rc7` reproducibility pins and Status identity. This is a release-identity update only; dashboard installation, daemon, auto-start, and prerelease guidance remain unchanged. Final verification stamping remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T10:08+02:00 — No content impact: MCP 3.0.0rc7 refreshed the public dashboard pin and
  current-version statement from rc6 to rc7. The README structure and product contract are
  unchanged; verification metadata remains pinned until closeout stamps the release commit.

- 2026-08-12T07:10+02:00 — 260731-EFA-L24 curator: aligned the
  contributor-facing quality ladder with host-managed master RAM/swap and an
  optional explicit constrained-environment cap. Verification metadata remains
  pinned until closeout stamps L24.

- 2026-08-08T02:00+02:00 — 260731-EFA-L17 curator: rewrote the gate-paragraph
  section for the ladder — pre-push runs `--targeted`, the full wrapper runs
  once per master at the master integration gate (host-managed by default, invoked by
  `worktree_integrate`), leaf closeouts/integrations run the targeted tier —
  and adjusted the coverage-floor gap note to the targeted-tier sentence.
  Verification metadata stays pinned until closeout stamps the 260731-EFA-L17
  commit.

- 2026-08-02T20:43+02:00 — W2-B08: anchored 14 README citation claims and supplied exact source paths; ranges remain generated by the scoped fixer. Verification metadata stays pinned until closeout.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 final state. **Retired this card's mid-leaf claim
  that either hook tier runs a complexity baseline** — the baseline was deleted before the
  leaf ended, and the README's own sentence is "No rail carries a baseline or exemption
  list". Corrected both tier step lists, and recorded that the README, like `AGENTS.md`,
  does not name the changed-lines coverage floor. Verification metadata is pinned to the
  leaf's reformat commit until closeout stamps the code commit.

- 2026-07-31T06:30+02:00 — 260731-EFA-L2 gate honesty (mid-leaf): the README's tier description now names
  `ruff format --check`, the complexity baseline, and `sync-harness.py --check`, and states
  outright that Radon is a report that cannot fail either tier. The repository map gained
  `scripts/sync-harness.py` and `scripts/harness/` with the regenerate instruction and the
  suite-level drift check. Superseded this card's prior four-step enumeration of what the
  wrapper enforces. Verification metadata pinned to the leaf's reformat commit until closeout
  stamps the code commit.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1: rewrote the README's hook paragraph for the fast/full tier
  split over the shared `.githooks/_gate.sh`, recorded that CI now runs on every branch push and
  pull request rather than only `main`, and pointed readers at CONTRIBUTING.md for the tier table
  and staged-content stash contract. Verification metadata pinned to the pre-leaf source authority
  until closeout stamps the code commit.

- 2026-07-24T14:31Z — 260718-CHATS-L5I incremental curator: added the README's public
  pre-commit/pre-push/closeout strict-wrapper contract; verification remains pinned until the code
  commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-12T12:07+02:00 — No content impact: 260712-TRH-L1 bumps the public Status/install pin
  strings 3.0.0rc4 -> 3.0.0rc5 for the task-reader priority release; the body describes the release
  version generically, so README structure and guidance remain current.

- 2026-07-08T15:45+02:00 — No content impact: 260707-HFX2-L7 bumps the public Status/install pin
  strings 3.0.0rc3 -> 3.0.0rc4 for the hotfix release tail; the body describes the release version
  generically as "bumped every release" so README structure and guidance remain current.

- 2026-07-07T21:17+02:00 — 260707-HFX-L6 review remediation: the public workflow sentence
  after the quickstart now says the developer-facing session is the architect, while spawned
  backend orchestrators and other role seats follow their role briefs. The docs pages swept in
  the same review remain outside file-level onboarding per path rules. Verification metadata
  pinned until closeout stamps the HFX-L6 commit.

- 2026-07-07T21:10+02:00 — No content impact: release 4922146 bumped the Status/install version strings 3.0.0rc2 -> 3.0.0rc3; the body describes the version generically ('bumped every release'), so nothing goes stale. (Reconciliation: the bump landed as a direct owner commit between the L17 and L18 closeouts.)
- 2026-07-06T12:05+02:00 — 260703-L10 (one-vocabulary sweep): the workflow sentence after the quickstart and the Workflows docs-index line now name the `l-01-agent-lifecycles` skill (orchestrator + role briefs; research-only exit / `w-02-light-task-workflow` task / master series — the chat build removed), and the Status 3.0-arc paragraph says "system-managed agent lifecycle". The `docs/**` pages (workflows, getting-started, features, llms.txt, FAQ, concepts, reference/skills, reference/runtime-layout, install/claude-code, docs/README) were swept in the same pass but stay outside file-level onboarding per path rules. Verification metadata pinned until closeout stamps the L10 commit.
- 2026-07-03T12:05+02:00 — 260703 L4: Status version string bumped to 3.0.0rc2 (structure
  unchanged); the sidecar's Status reference row became version-generic so release bumps stop
  drifting it.
- 2026-07-03T11:55+02:00 — 260703 L3: added the ToC-linked `## Run The Dashboard` section between
  Quickstart and Documentation — unpinned `uv tool install agents-remember-mcp` as the first-class
  install, flag-free `agents-remember dashboard`, daemon mode + `dashboard.autoStart`, pinning as the
  debugging/repro path, and the single rc-period pre-release note
  (`--prerelease allow` / explicit pin, incl. the MCP registration). Concrete pin examples reference
  `3.0.0rc2`, the release this lands with. Verification metadata pinned until closeout stamps the
  code commit. cit:([`## Run The Dashboard`, "autoStart"], README.md:138-177)
- 2026-07-03T11:20+02:00 — L14 release: Status reads 3.0.0rc1 and the journey paragraph became 'The 3.0 arc' — the lifecycle/gates/projection substrate served as the mission-control cockpit from the MCP package (agents-remember dashboard), with the rc caveat on the settling cockpit surface.
- 2026-06-22T22:00+02:00 — No content impact: Status section version string bumped to 2.9.3 (worktree_name contract-resolution fix release, #90); the README structure and guidance this sidecar describes are unchanged.
- 2026-06-19T13:42 — No content impact: Status section version string bumped to 2.9.2 (benchmark provider isolation release, task 260619); the README structure and guidance this sidecar describes are unchanged.
- 2026-06-19T01:50+02:00 — Updated the Logic section for the README headline revision (PR #85 / `b9d7314`): the `<h3>` tagline changed from "Durable" to "Git-verified records for what your coding agents know. A control plane for what they do.", sharpening the public positioning toward records-plus-control-plane. Advanced verification metadata to merged `main` `cbea101`.
- 2026-06-12T19:06+02:00 — No content impact: Status section version string bumped to 2.9.1 (issue #83 closeout committed-range fix release); the README structure and guidance this sidecar describes are unchanged.
- 2026-06-12T12:05+02:00 — Rewrote the Status section from the per-release narrative chain (2.0.0→2.8.0, grown into a de-facto changelog) into a two-paragraph current-state + direction statement: version `2.9.0` with the core-path maturity, Stability deferral, GitHub Releases routing (the repository's canonical changelog), and harness-maturity notes, plus a "where the journey is going" paragraph (observable, steerable sessions: machine-readable lifecycle entity, durable gates, projection layer, browser cockpit #2/#43, the 3.0 posture) — making Status the one public place that states direction. The 2.9.0 release content (worktree-only closeout, GitHub #62) moves to the mcp-v2.9.0 GitHub Release notes instead of the README. Updated the stale Status body row (previously pinned at 2.5.2). Verification metadata stays pinned until closeout commits the source change.
- 2026-06-11T14:07+02:00: No content impact: re-verified against merged main `c2c2dcb` after the upstream doc-link/typo merges (PRs #69-#73) and the repository rename from `agents-remember-md` to `agents-remember`; card content already matched the source.
- 2026-06-10T10:26+02:00 — No content impact: Status section bumped to 2.8.0 with the GitHub #54 release sentence (lifecycle-long stale-base prevention: include_freshness, stale-base preflight, memory_main_advance, worktree_sync); the README structure this sidecar describes is unchanged.
- 2026-06-10T08:15+02:00 — Status section bumped to 2.7.0 with the release sentence: background worktree provider setup observability (#53) and container-form CGC seed argv on Windows (#58).
- 2026-06-10T06:05+02:00 — No content impact: Status section bumped to 2.6.0 with the memory-integrity release sentence (carryover overview candidates, closeout body/history gates, no-impact markers; GitHub #56); the sidecar's description of the README remains accurate.
- 2026-06-10T05:45+02:00 — Status section bumped to 2.5.2 with the carryover response compaction sentence (GitHub #52).
- 2026-06-10T05:30+02:00 — Status section bumped to 2.5.1 with the tool-reliability release sentence (protocol-pipe hygiene, stall-based wedge detection, GrepAI indexing parity, single runner-image derivation, tool-report compaction with keep-5/7-day retention).
- 2026-06-09T22:10+02:00 — Status section bumped to 2.5.0 with the CGC durability/readiness release sentence (FalkorDB host-path persistence, graph-content readiness states, degraded-packet propagation, `indexing` summary list, watcher self-heal, orphan cleanup).
- 2026-06-09T15:39+02:00: Bumped the Status section to `2.4.2` and documented it as the patch packaging the consolidated `l-01-session-job-lifecycle` skill, where the complete lifecycle spine now lives in `SKILL.md` instead of a separate `lifecycle.md` companion. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-08T12:22+02:00: Bumped the Status section to `2.4.1` and documented
  it as the patch for runtime asset packaging/source sync plus skipped-provider
  context-packet provider validation. Verification metadata stays pinned until
  closeout commits the source change.
- 2026-06-08T11:53+02:00: Updated repository-layout onboarding for canonical root runtime asset folders and `scripts/sync-runtime.py`, including the pre-commit/pre-push generated-copy checks. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-08T08:33+02:00: Bumped the Status section to `2.4.0` and documented it as the release for harness-local starter renderers, Python hook command rendering, and manual placeholder-replacement docs that remove the legacy Claude Code `jq` misconception. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T18:42+02:00: Refined setup memory so renderers are framed as optional convenience scripts for placeholder replacement; manual replacement is an explicit supported path. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T18:19+02:00: Refined the renderer setup memory after the CLI contract dropped the separate workspace-root flag; copied harness packages now infer the workspace root from their folder and accept one `--repo` list. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T16:45+02:00: Updated the quickstart memory after starter packages gained harness-local `render-starter` scripts; setup now says copy the package, render paths/repositories/hook commands before MCP wiring, then wire MCP and restart. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-06T12:28+02:00: Replaced README `## Core Model` memory with a faster `## Core Features` pitch and added the public `docs/features.md` link; updated references to the new features page and docs index entry. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-04T23:15+02:00: Updated the `2.3.3` Status note to include Docker-safe provider setup naming for dotted worktree names alongside the runtime reinstall watcher rebind patch. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-04T18:52+02:00: Bumped the Status section to `2.3.2` and documented it as the patch that packages the refreshed runtime skills with the C-09 worktree intent approval gate and integration checkout prerequisite reminder. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T19:25+02:00: Bumped the Status section to `2.3.1` and documented it as the patch that corrects the PyPI/MCP package README to the 2.3.0 package-first setup flow. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T18:58+02:00: Updated for the 2.3.0 starter-package release: package-first quickstart, one-restart first-run path, root `skills/` canonical source tree, `scripts/sync-skills.py`, and Status-section version bump. Verification metadata stays pinned until closeout commits the source change.
- 2026-06-03T04:25+02:00: Bumped the Status-section version reference to `2.2.0` (mcp 2.2.0 — lifecycle collaboration loop and C-09 source-branch contract refresh; a minor backward-compatible release on the 2.0.0 reshape). Verification metadata pinned until closeout. chore/release-mcp-2.2.0 branch.
- 2026-06-02T18:35+02:00: Bumped the Status-section version reference to `2.1.0` (mcp 2.1.0 — workspace-first install defaults, skill-name/MCP-tool reference convention, grepai-status + quality-gate fixes; a minor backward-compatible release on the 2.0.0 reshape). Verification metadata pinned until closeout. chore/release-mcp-2.1.0 branch.
- 2026-06-02T16:35+02:00: Second batch (install-location defaults) — the Repository Layout section gained a workspace-first note (installed runtime defaults to `<workspace>/ar-coordination/`, inside the workspace and never the home directory; the `c-13-install-and-onboard` skill shows each install path as an accept-or-override default). Realigned the post-Layout row ranges by +3 (layout end L105-L139, status L141-L143, stability L145-L147, contributing L149-L153). fix/skill-ref-naming-and-grepai-status branch; verification pinned until closeout.
- 2026-06-02T11:30+02:00: Added a `## What It Looks Like In Practice` mini-transcript between Core Model and Live Demo (by-path note + task-start `context_packet`/`memory_quality_check` + read/propose/refresh loop). Added its Repo-Internal References row cit:([`## What It Looks Like In Practice`], README.md:63-80) and realigned every post-insertion row range by +18 (live-demo L54-L59, quickstart L72-L90, documentation L92-L103, layout L105-L136, status L138-L140, stability L142-L144, contributing L146-L150). Part of the HN-launch doc pass that also touched `docs/getting-started.md`, `docs/workflows.md`, `docs/README.md`, and a new `docs/release-checklist.md` (all outside file-level onboarding). Verification metadata stays pinned until closeout. docs/hn-launch-hardening branch.
- 2026-06-02T10:10+02:00: Added a `## Live Demo: This Repo Uses Agents Remember` section between Core Model and Requirements — it states Agents Remember runs on itself and links the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable onboarding example, surfacing the dogfooding message higher on the page than the existing Contributing mention. Added a Live Demo Repo-Internal References row cit:([`## Live Demo`], README.md:81-87) and realigned every post-insertion row range by +7 (quickstart L54-L72, documentation L74-L85, layout L87-L118, status L120-L122, stability L124-L126, contributing L128-L132). Verification metadata stays pinned until closeout commits the source change. docs/readme-live-demo branch.
- 2026-06-02T05:10+02:00: Bumped the Status section to `2.0.0` and flagged it as a major, breaking release (the L-01 lifecycle reshape: retired W-03/W-01, flat skills, removed skill IDs + the `skills_install` `layout` input + heavy `workflow_kind` values). L-01 series, release, mcp 2.0.0.
- 2026-06-02T05:00+02:00: Updated the README's workflow language for the `l-01-session-job-lifecycle` skill reshape — "normal work starts in chat mode" became the `l-01-session-job-lifecycle` skill session job lifecycle, and the Workflows doc link now names the `l-01-session-job-lifecycle` skill build modes (read-only / chat build / `w-02-light-task-workflow` skill). The `docs/**` workflow/skills/layout/install pages were rewritten in the same pass but stay outside file-level onboarding. `l-01-session-job-lifecycle` skill series, docs pass, mcp 2.0.0.
- 2026-06-02T03:30+02:00: Bumped the Status-section version reference to `1.0.2` (mcp 1.0.2 — `system/git-workflow.md` + PR-gated landing doctrine). Verification metadata pinned until closeout.
- 2026-06-01T13:30+02:00: Bumped the Status-section version reference to `1.0.1` (mcp 1.0.1). Verification metadata pinned until closeout.
- 2026-05-31T12:40+02:00 — Added a new `## Stability` section (the 1.0.0 semver public-contract promise: skill IDs, MCP tool names/inputs/outputs, the `ar-coordination/`/`ar-memory/` layout, and the settings schema) and reconciled the Status section to defer to it instead of warning that those contracts may evolve. Added a Contributing line linking the project's own published memory layer (Foxfire1st/ar-agents-remember) as a downloadable example. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-31T12:30+02:00 — Bumped the Status-section reference from `0.9.6` (pre-1.0) to `1.0.0` and updated the stability caveat to "may still evolve across minor releases" (1.0.0 review remediation). Verification metadata stays pinned until closeout commits the source change.
- 2026-05-31T01:06+02:00: Bumped the Status-section version reference to `0.9.6` for the `w-02-light-task-workflow` skill design-section change (MCP 0.9.6). Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T22:29+02:00: Bumped the Status-section version reference to `0.9.5` for the S6 token-counter release. Verification metadata stays pinned until closeout commits the source change.
- 2026-05-30T21:22+02:00: Refreshed for the 0.9.0–0.9.4 run and verified against `57944df`. Rewrote the Logic quickstart description to the current short three-step, agent-driven flow that hands onboarding to `c-13-install-and-onboard` and frames the three harness restarts; corrected the stale Repo-Internal References (the quickstart row had described an older `c-00-initialize-memory-repo` skill / `c-03-repo-bootstrap` skill / `include_benchmarks` / `.codex` flow) and realigned all README line ranges to the 119-line source; cleared the resolved verification-refresh Todo.
- 2026-05-29T21:00+02:00: Updated after the Quickstart stopped telling users to clone this repo (Agents Remember runs from the published `agents-remember-mcp` package via `uvx`) and switched the `runtime_install`/`skills_install` examples to the act-by-default form.
- 2026-05-29T20:30+02:00: Verified the sidecar body against the committed re-spined `README.md` (TLDR, the three retrieval substrates, quickstart, install pages, source/runtime layout) and advanced verification metadata to the landed commit `01f503d`.
- 2026-05-29T17:30+02:00: Re-spined the README front door — added a TLDR framing repo knowledge as first-class infrastructure, replaced the sidecar-only "path-derived" positioning with the three retrieval substrates (by path / by meaning / by relationship), and removed the sidecar-era infographic embed. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-24T10:06+02:00: Refreshed verification metadata after source commit `f48a346` moved Codex setup to `.codex` and removed the source `.env` resolver path.
- 2026-05-24T09:38+02:00: Updated after the public quickstart switched Codex MCP registration and skill exposure examples from `.agents` to `.codex`.
- 2026-05-24T04:34+02:00: Updated after public docs renamed `c-02-memory-quality-control` skill to memory quality control.
- 2026-05-23T14:20+02:00: Updated after the public quickstart switched from deleted installer scripts to `runtime_install` MCP tool and copy-only `skills_install`.
- 2026-05-23T13:46+02:00: Updated repository layout after provider lifecycle, provider setup, and benchmark runner behavior moved into `mcp/` and the source `scripts/` route was removed.
- 2026-05-23T05:32+02:00: Updated after the quickstart stopped presenting source-installer provider dependency install and moved provider dependency operations behind MCP settings.
- 2026-05-21T02:14+02:00: Updated quickstart notes after reinstall began installing enabled provider dependencies by default and documented `--skip-provider-deps`.
- 2026-05-15T17:32+02:00: Clarified benchmark package wording after source-side empty workspace folders were removed in favor of generated workspaces. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T15:50+02:00: Updated after the README added optional benchmark install guidance, benchmark methodology routing, and benchmark package/runtime layout entries. Verification metadata remains pinned to the last committed source state until closeout.
- 2026-05-15T12:05+02:00: Refreshed after the README was rewritten as a concise public front door and detailed setup/reference material moved into `docs/`. Verification metadata remains pinned to the last committed source state until the docs rewrite is committed.
- 2026-05-14T21:38+02:00: Updated after README settings examples gained the standard path-rule exclusion baseline for generated/vendor/build/local artifacts. Verification metadata remains pinned to the last committed source until closeout.
- 2026-05-13T13:38: Updated after the README replaced top-level system examples with folder-shaped coordinator/global and memory-repo-specific scaffold examples.
- 2026-05-12T18:57+02:00: Updated after the README added Hermes.md, Pi.dev, and OpenClaw install instructions after the Claude Code section.
- 2026-05-12T18:51+02:00: Refreshed metadata and current README references after the install-skills guidance and harness-specific skill setup sections were added in the working tree.
- 2026-05-12T18:22+02:00: Updated after the README gained Cursor and Windsurf native skill instructions and split installer guidance into tree versus flat symlink layouts.
- 2026-05-12T18:08+02:00: Updated after the Claude Code README instructions were corrected to use `.claude/skills` / `~/.claude/skills` native discovery with the existing namespace symlink.
- 2026-05-12T17:53+02:00: Updated after the README gained harness-specific skill installation guidance, external-checkout examples, and explicit `AR_COORDINATION_ROOT` separation from skill installation.
- 2026-05-12T11:30: Updated after the external-memory example wording focused on the inspectable memory repo rather than repeating the code repository link.
- 2026-05-11T19:42: Refreshed verification metadata against commit `aa85d3862bf21fed791e3170e6957f9288c319e8` after coordination rename verification.
- 2026-05-11T18:34: Updated after the resolver overview adopted `code_repository_name`, `code_repository_root`, and `coordination_root` terminology.
- 2026-05-10T03:01: Updated after the README added `c-09-git-worktree-manager` skill direct-closeout as the lightweight current-checkout path for approved external-memory micro edits.
- 2026-05-10T02:20: Updated after the README added a working external-memory repo example and links to the code and memory repositories.
- 2026-05-09T22:46: Updated for the `c-10-adopt-memory-baseline` skill adoption skill entry.
- 2026-05-09T21:59: Updated for ar-memory/ar-coordination split, `c-09-git-worktree-manager` skill, and resolver contract changes.
- 2026-05-09T21:15: Created first file-level onboarding baseline for the public repository overview.
