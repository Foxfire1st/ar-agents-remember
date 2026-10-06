# README.md

## Governing Overview

[overview.md](overview.md)

## Purpose

`README.md` is the public front door for Agents Remember. It gives a concise product-level explanation, a high-signal Core Features section, a short quickstart, a Run The Dashboard section (260703 L3 — the CLI install/run story, now through a locally built wheel), links to harness-specific install pages, optional benchmark guidance, and a compact repository/runtime map. The concentrated feature tour now lives in `docs/features.md`; detailed setup, concepts, workflows, benchmark methodology, guides, and reference material live under `docs/`.

## Code Commentary

### Logic

The landed IAS README now documents ordinary isolated pytest development, explicit integration selection and genuine Dagger-only certification. Its lines269–271 still contain superseded 90%/CRAP30 wording at d3610903; the current policy is diagnostic coverage and production CRAP20 review as declared by AGENTS.md and docs/design/python-pytest-bootstrap.md. This mismatch is a documentation defect, not authority to restore a floor. The primary implementation checkout carries the correction for subsequent delivery.

The README's `<h3>` headline now frames Agents Remember in two parts — git-verified records of what coding agents know, and a control plane for what they do — sharpening the earlier single-line "durable" framing toward the records-plus-control-plane positioning. Below it, the README uses `## Core Features` as the fast product pitch. It frames Agents Remember as project memory coding agents can verify and act on, shows the source-file to onboarding-unit mapping, and names the user-facing features a skimming reader needs in the first thirty seconds: path-addressed memory, Git-proven freshness, optional semantic/code-graph discovery that finds but does not decide, memory that lands with code through external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and harness-ready first-run packages. The previous `## Core Model` section carried the same conceptual spine but was less effective as a public feature pitch.

The previous MCP-installs-skills first-run model was replaced with package-first
harness setup. The root page now keeps one short, harness-agnostic three-step
quickstart that the agent drives: (1) copy the harness-native starter package
from the repo and render the copied package. The `render-starter` script is a
convenience that infers the workspace root from the copied harness folder, takes
one explicit `--repo` list such as `--repo my-app shared-lib`, and fills path,
repository, and hook-command placeholders; the docs also allow manual
placeholder replacement. The package provides skills, hooks, rules,
instructions, MCP settings templates, and rendered hook commands; (2) build the
checkout's wheel (`uv build --wheel mcp`) and wire that local artifact with
`uvx --python 3.14 --from <abs>/built-wheel.whl agents-remember-mcp --config
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
Documentation. For this checkout it leads with the local artifact: build the dashboard bundle
and sync it (`npm --prefix dashboard run build`, then `python3 scripts/sync-dashboard.py`),
build the wheel, install it as a uv tool (`uv tool install --python 3.14 <wheel>`) and start
`agents-remember dashboard` (no `--config`: L1's discovery walks up from the working
directory). It keeps daemon mode (`--daemon`/`--status`/`--stop`, state under
`<coordinationRoot>/logs/dashboard/`) and the `"dashboard": {"autoStart": true}` settings key
(L2). The historical published `3.0.0rc8` pin is documented as the Python 3.13 artifact rather
than as an installation example for this Python 3.14 build, and an official release of the
3.14 build is stated as pending.

A short `## Live Demo` section sits between Core Features and Requirements. It states that Agents Remember runs on itself and links the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable example of the by-path onboarding layer. It surfaces the dogfooding message higher on the page than the existing Contributing-section mention, which still owns the operational instruction to clone that memory and use it while contributing.

The Requirements section states the current checkout's Python 3.14 package line
(`>=3.14,<3.15`) with 3.14.8 pinned only for managed development and CI, separates that from the
historical published `3.0.0rc8` artifact and its Python 3.13 range, and points repository
developers to the exact source-built 3.14.8 contract in the MCP README. The root README remains a
public orientation layer; the executable bootstrap and provenance contract stay under `scripts/`.

### Conventions

- Keep the README short enough to scan.
- Use the README to orient and route, not to carry full setup matrices or reference material.
- Use `docs/` for user-facing docs, `benchmarks/` for optional benchmark fixtures, `AGENTS.md` and installed runtime templates for agent behavior, and onboarding for durable repository knowledge.
- Keep public language focused on the current intended install model: copy a harness starter package, wire the MCP server, run/verify `runtime_install()` through `c-13-install-and-onboard`, and store memory in a memory repository of its own under `ar-coordination/memory-repos/ar-<repo>/` — the only supported topology. The former repo-local `ar-memory/` internal mode was removed from the product and is refused by name; do not describe it as an available or default option.
- Avoid presenting the public README as a source-package explanation or compatibility guide for old alpha layouts.

### Invariants And Boundaries

The README is explanatory, not the implementation source of truth. Runtime behavior belongs to MCP tools, package services, and skills. If README guidance disagrees with helper behavior, verify helper behavior before changing operational assumptions.

The public prerequisite must remain aligned with `mcp/pyproject.toml` (`>=3.14,<3.15`) and must not
imply that uv may silently select an arbitrary managed Python for repository development; the
exact 3.14.8 pin belongs to managed development and CI, not to the package's admitted range.

`docs/**` is currently excluded from file-level onboarding by this repository's path rules, so this README onboarding is the durable file-level companion for the public documentation front door. Repo-level overview onboarding should carry broad documentation-structure context when the docs tree changes.

### Todos

- If `docs/**` becomes eligible in path rules later, create focused file-level onboarding for high-value docs pages instead of overloading this README onboarding.

### Docs References

The README itself no longer depends on external harness docs for detailed setup claims; those claims live in the dedicated install pages.

No external documentation is needed to prove the root README's current structure; it is a same-repository public overview and link hub.

## Evidence

### Repo-Internal References

The README routes readers into the split documentation tree and gives the current runtime/source layout.

- The README now has a `## Core Features` section that replaces `## Core Model`; it shows the source-file to onboarding-unit mapping, pitches path-addressed memory, Git-proven freshness, optional semantic/code-graph discovery, external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and harness-ready first-run packages, then links to `docs/features.md`. [1]
- The README shows a `## What It Looks Like In Practice` mini-transcript: a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-then-propose-then-refresh loop. [2]
- The README has a `## Live Demo` section stating Agents Remember runs on itself and linking the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable by-path onboarding example. [3]
- The Requirements section names Python 3.14, the bounded package range, the historical published 3.13 artifact, and the canonical repository-development runtime documentation. [4]
- The quickstart is a short, harness-agnostic three-step agent-driven flow: copy the harness starter package, render it either with the convenience `render-starter` script or manual placeholder replacement, wire the MCP server from a locally built wheel with `uvx`, restart once, then invoke `c-13-install-and-onboard`; `skills_install()` is maintenance/manual because the package already carries the initial skills and harness files. [5]
- The README routes readers first to the new Features tour, then to setup, concepts, workflows, benchmark methodology, guides, settings, and skills documentation under `docs/`. [6]
- The `## Run The Dashboard` section: local-wheel build/sync and install first-class, discovery-backed flag-free `dashboard`, daemon mode + autoStart, and the historical published pin named as the 3.13 artifact. [7]
- The README keeps the source checkout layout distinct from the installed runtime layout, exposes root `skills/` as canonical, identifies `scripts/sync-skills.py` as the helper that refreshes generated skill copies, exposes root `agents-md-files/`, `benchmarks/`, `providers/`, and `system/` as canonical runtime assets, identifies `scripts/sync-runtime.py` as the package-data-only runtime asset helper, and notes the workspace-first `<workspace>/ar-coordination/` default. [8]
- The README's Status section is a two-paragraph current-state + direction statement: paragraph one states the source version, that the Python 3.14 candidate awaits an official release, the core-path maturity, the Stability deferral, the GitHub Releases routing (the repository's canonical changelog — this repo keeps no `CHANGELOG.md`, and Status no longer narrates per-release summaries), and the harness-maturity note; paragraph two, since the L14 release, states the SHIPPED 3.0 arc (observable, steerable sessions — lifecycle entity, durable approval gates, projection layer — served as the mission-control browser cockpit from the MCP package via the `agents-remember dashboard` CLI, #2/#43) with the rc caveat that the cockpit surface is still settling toward the final 3.0.0 contract. [9]
- The Stability section is the semver promise: skill IDs, MCP tool names and their inputs/outputs, the `ar-coordination/` and `memory-repos/ar-<repo>/` layout, and the settings schema do not change without a major version bump; internals/provider internals/prompt wording may change in minor releases. The range was re-anchored by `CAPS-R12@v1`: the section still opens at `## Stability` and its body is now the single line that follows, and the promised layout no longer names `ar-memory/` because the internal mode was removed. [10]
- The Contributing section points contributors at CONTRIBUTING.md, restates the core rules, and tells contributors to download/clone the project's own published memory (Foxfire1st/ar-agents-remember) and use it as the active Agents Remember memory for their checkout while contributing (dogfooding the by-path onboarding loop). [11]
- The docs index now includes `docs/features.md` as the concentrated product tour alongside getting-started, concepts, workflows, install guides, guides, and reference pages. [12]
- `docs/features.md` carries the full feature tour, including the new table of contents plus harness-native setup and operational guardrails for MCP authority, baseline adoption, branch carryover, cross-repo gates, benchmarks, and source quality tooling. [13]

### Cross-Repo References

The README describes external memory in general terms, but this file-level onboarding does not rely on sibling repository internals.

No meaningful cross-repo references found for the README itself.

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
