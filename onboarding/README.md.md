# README.md

## Governing Overview

[overview.md](overview.md)

## Purpose

`README.md` is the public front door for Agents Remember. It gives a concise product-level explanation, a high-signal Core Features section, a short quickstart, a Run The Dashboard section (260703 L3 — the CLI install/run story, now through a locally built wheel), links to harness-specific install pages, optional benchmark guidance, and a compact repository/runtime map. The concentrated feature tour now lives in `docs/features.md`; detailed setup, concepts, workflows, benchmark methodology, guides, and reference material live under `docs/`.

## Code Commentary

### Logic

The landed IAS README now documents ordinary isolated pytest development, explicit integration selection and genuine Dagger-only certification. Its lines269–271 still contain superseded 90%/CRAP30 wording at d3610903; the current policy is diagnostic coverage and production CRAP20 review as declared by AGENTS.md and docs/design/python-pytest-bootstrap.md. This mismatch is a documentation defect, not authority to restore a floor. The primary implementation checkout carries the correction for subsequent delivery.

The README's `<h3>` headline now frames Agents Remember in two parts — git-verified records of what coding agents know, and a control plane for what they do — sharpening the earlier single-line "durable" framing toward the records-plus-control-plane positioning. Below it, the README uses `## Core Features` as the fast product pitch. It frames Agents Remember as project memory coding agents can verify and act on, shows the source-file to onboarding-unit mapping, and names the user-facing features a skimming reader needs in the first thirty seconds: path-addressed memory, Git-proven freshness, memory that lands with code through external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and harness-ready first-run packages. Its `Search that finds, not decides` bullet and its Docker note still offer the optional semantic-memory and code-graph providers; that is residual source wording, because the two search providers and their public retrieval and setup surfaces are retired and it describes no available capability. Its `Harness-ready first run` bullet still says starter packages carry the native MCP, skills, hooks, rules and instruction files, which the Quickstart's statement that no starter package, rendered settings or skill folder is copied contradicts; that table sentence is retained source text, not a corrected claim. The previous `## Core Model` section carried the same conceptual spine but was less effective as a public feature pitch.

The first-run model the page now states is neither an MCP install of skills nor a copied
starter package. Quickstart step 1 is the MCP authority settings file — copy
`examples/mcp/settings.example.json` to a path of your own and replace its paths with
absolute ones: the coordination folder (it may not exist yet), the workspace root, the
transcript folder and one entry per code repository. Step 2 registers the wheel with `uvx
--python 3.14 --from <abs>/built-wheel.whl agents-remember-mcp --config
<abs>/agents-remember-settings.json`, pointing at the registration file the harness guide
carries, then restarts the harness once so it starts the server. Step 3 is one call in a chat
that names no task, sprint or repository — `role_start(role="bootstrap",
request_id="<a UUID you generate>")` — which prepares the runtime scaffold, provisions and
starts the Paseo host, verifies the plug-in, starts one instructed Bootstrap seat and returns
that seat's dashboard address; setup continues there (repository and memory root, initialize
or read the baseline, adopt its content, harness per role with model and effort left unset),
Bootstrap writes the user settings file and reports an existing one instead of overwriting it,
and it finally tells the developer to start the Architect, which organises the knowledge
foundation as ordinary task work.

The page states plainly that this is the whole first-run path: no skill folder, starter
package or rendered settings is copied into a harness, because the tool server serves the
canonical skills as MCP resources, so the skills a session reads belong to exactly one
installed build and no separate skill-install route exists. The source checkout paragraph is
corrected to match: root `skills/` is the canonical authoring tree and
`scripts/sync-skills.py` refreshes only the packaged copy that is served, while root
`agents-md-files/`, `benchmarks/`, `providers/` and `system/` stay canonical runtime asset
sources refreshed by `scripts/sync-runtime.py`. The self-hosted harness trees under
`.claude/`, `.codex/`, `.cursor/`, `.github-vscode/`, `.vscode/`, `.hermes/`, `.openclaw/`,
`.pi/` and `.agents/` are maintained in place, one file per harness — MCP registration,
optional instructions and an optional session-start hook or rule — and carry no skill folder
and no placeholder renderer. The installed `ar-coordination/` layout therefore no longer
lists `skills/`, and the page says why: the server serves the packaged copy, so the
coordination root carries no second skill tree to keep current. The hooks paragraph drops
`sync-harness.py` from the generated-copy checks, keeping `sync-skills.py --check` and
`sync-runtime.py --check`.

A `## What It Looks Like In Practice` mini-transcript sits between Core Features and the Live Demo: it shows a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-onboarding-then-propose-then-refresh loop — a concrete picture of the by-path loop for skimming readers.

The post-quickstart workflow sentence uses the host role-start route. Free chat answers questions inline. For managed-repository work it creates or resolves the sprint document, writes the developer’s request into it, calls `role_start` once for an Architect without any document reference or brief, and tells the developer where the agent and request are. The developer speaks with the started Architect in the dashboard. A different role is started this way only when the developer explicitly names the role and task. A launched role follows its handover; unbound `role_message` remains refused, and a refusal admits no alternative launch route. Context resolution, full memory-quality curation, paired source/onboarding reads and approved memory maintenance keep their existing owners.

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
- Keep public language focused on the current intended install model: write the MCP authority settings, register the server with the harness's own registration file, restart once, and make one `role_start(role="bootstrap", …)` call whose dashboard chat carries setup onward into a user-started Architect. No starter package, rendered settings or skill folder is copied, and memory stays in a memory repository of its own under `ar-coordination/memory-repos/ar-<repo>/` — the only supported topology. The former repo-local `ar-memory/` internal mode was removed from the product and is refused by name; do not describe it as an available or default option.
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

- The README now has a `## Core Features` section that replaces `## Core Model`; it shows the source-file to onboarding-unit mapping, pitches path-addressed memory, Git-proven freshness, external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and harness-ready first-run packages, then links to `docs/features.md`. Its optional semantic/code-graph discovery and its Docker/provider wording are residual source text: the two search providers are retired, so neither describes an available capability. Its retained `Harness-ready first run` bullet still says starter packages carry skills, hooks, rules and instruction files, which the Quickstart's no-copied-package statement contradicts. Anchor: `## Core Features` [1]
- The README shows a `## What It Looks Like In Practice` mini-transcript: a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-then-propose-then-refresh loop. [2]
- The README has a `## Live Demo` section stating Agents Remember runs on itself and linking the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable by-path onboarding example. [3]

- The Requirements section names Python 3.14, the bounded package range, the historical published 3.13 artifact, and the canonical repository-development runtime documentation. [4]

- The quickstart is a short, harness-agnostic three-step agent-driven flow: write the MCP authority settings file from `examples/mcp/settings.example.json`, register the locally built wheel with `uvx --config` and restart the harness once, then make one `role_start(role="bootstrap", request_id="<UUID>")` call whose dashboard chat continues setup; no starter package, rendered settings or skill folder is copied. Anchor: `## Quickstart`; `uvx`; `role_start`; `bootstrap` [5]

- The README routes readers first to the new Features tour, then to setup, concepts, workflows, benchmark methodology, guides, settings, and skills documentation under `docs/`. [6]


- The `## Run The Dashboard` section: local-wheel build/sync and install first-class, discovery-backed flag-free `dashboard`, daemon mode + autoStart, and the historical published pin named as the 3.13 artifact. [7]

- The README keeps the source checkout layout distinct from the installed runtime layout, exposes root `skills/` as canonical, identifies `scripts/sync-skills.py` as the helper that refreshes the one served package copy, exposes root `agents-md-files/`, `benchmarks/`, `providers/` and `system/` as canonical runtime assets refreshed by `scripts/sync-runtime.py`, states that the self-hosted harness trees are maintained in place without a renderer and that the installed runtime carries no `skills/` folder, and notes the workspace-first `<workspace>/ar-coordination/` default. Anchor: `## Repository Layout`; `skills/`; `scripts/sync-skills.py`; `agents-md-files/`; `scripts/sync-runtime.py`; `<workspace>/ar-coordination/` [8]
- The README's Status first paragraph distinguishes the Python 3.14 source candidate from the historical Python 3.13 artifact at the same `3.0.0rc8` version, states core-path and harness maturity, and sends stability guarantees to Stability and release notes to GitHub Releases, the canonical changelog rather than a local CHANGELOG.md. Its second paragraph retains the historical observable/steerable-session and durable-gate 3.0 account with the rc settling caveat. MIK-R113 removed the product-owned session/gate surfaces: that retained source paragraph is not authority to restore them or a claim that the current product still hosts chats. Native host role agents and the dashboard remain. [9]
- The Stability section is the semver promise: skill IDs, MCP tool names and their inputs/outputs, the `ar-coordination/` and `memory-repos/ar-<repo>/` layout, and the settings schema do not change without a major version bump; internals/provider internals/prompt wording may change in minor releases. The range was re-anchored by `CAPS-R12@v1`: the section still opens at `## Stability` and its body is now the single line that follows, and the promised layout no longer names `ar-memory/` because the internal mode was removed. [10]
- The Contributing section points contributors at CONTRIBUTING.md, restates the core rules, and tells contributors to download/clone the project's own published memory (Foxfire1st/ar-agents-remember) and use it as the active Agents Remember memory for their checkout while contributing (dogfooding the by-path onboarding loop). [11]

> Retained earlier citation wording: - The docs index now includes `docs/features.md` as the concentrated product tour alongside getting-started, concepts, workflows, install guides, guides, and reference pages. [12]




> Retained earlier citation wording: - `docs/features.md` carries the full feature tour, including the new table of contents plus harness-native setup and operational guardrails for MCP authority, baseline adoption, branch carryover, cross-repo gates, benchmarks, and source quality tooling. [13]



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
  (`sync-skills.py --check`, `sync-runtime.py --check`), plus
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

### The Repository Map No Longer Carries A Harness Generator

The layout section lists `sync-skills.py` as the helper that refreshes the one served package
copy, beside `sync-runtime.py` for runtime assets; `scripts/sync-harness.py` and
`scripts/harness/` are gone from the map and from the repository. A paragraph now states that
the self-hosted harness configuration in `.claude/`, `.codex/`, `.cursor/`,
`.github-vscode/`, `.vscode/`, `.hermes/`, `.openclaw/`, `.pi/` and `.agents/` is maintained
in place, one file per harness — MCP registration, optional instructions, and the optional
session-start hook or rule — carrying no skill folder and no placeholder renderer, with the
`<PATH/TO/YOUR/PROJECTS_FOLDER>` markers replaced by hand. The earlier claim that
`mcp/tests/test_sync_harness.py` caught drift inside the suite describes a test that no
longer exists.

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

The README distinguishes deterministic hooks and pull-request checks from lifecycle acceptance. Pre-commit/pre-push and GitHub PR validation are non-test checks; leaf closeout owns targeted Dagger once, leaf integration reuses its certified commit, and master integration owns full Dagger once. Ordinary Python development can use pytest directly as diagnostic feedback without Dagger admission, coverage, mutation or catalog preflight. Direct targeted Vitest remains diagnostic feedback. Neither development loop replaces the targeted/full acceptance graph; retry proof remains an internal attested-Dagger optimization.

## 260824-PDLS — Contributor-Facing Python Route

The README now says that Python investigation and acceptance both execute in the pinned Dagger
environment. Candidate A's host command, cohort manifest, static closure classifier, and self-proof
were deleted after representative exact-candidate measurement failed to justify their cost. The
seven unique product assertions remain ordinary explicit-lane pytest regressions. Non-accepting
Dagger evidence routes stay labelled and cannot publish lifecycle acceptance; direct targeted
Vitest remains the only supported host test diagnostic.

## 260928-MIK-L96 Host install and start

The product's install brings the Paseo host: the `runtime_install` step fetches the build's own Node, installs the host release the packaged contract names and starts it, so a user who follows the install types no host command. `agents-remember dashboard --daemon` makes sure the host runs; stopping or restarting the dashboard never stops it, and `agents-remember paseo stop --config <file>` remains the one host-stop command. `agents-remember dashboard --status` prints one line for the dashboard and one for the host.


- The install procedure the readme mirrors. [14]


- The dashboard start that ensures the host. [15]

## Historical provider account

The following source-epoch wording is retained as history. It does not restore a removed provider consumer or operation.

<details>
<summary>Superseded provider passages</summary>

> path-addressed memory, Git-proven freshness, optional semantic/code-graph discovery that finds but does not decide, memory that lands with code

> The previous `## Core Model` section carried the same conceptual spine but was less effective as a public feature pitch.

> bootstraps onboarding when needed, and starts provider indexing when enabled.

> pitches path-addressed memory, Git-proven freshness, optional semantic/code-graph discovery, external-memory ledgers

</details>

- The docs index now includes `docs/features.md` as the concentrated product tour alongside getting-started, concepts, workflows, install guides, guides, and reference pages. [12]


- `docs/features.md` carries the full feature tour, including the new table of contents plus harness-native setup and operational guardrails for MCP authority, baseline adoption, branch carryover, cross-repo gates, benchmarks, and source quality tooling. [13]
