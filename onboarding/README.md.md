# README.md

## Governing Overview

[overview](overview.md)

## Purpose

`README.md` is the public front door for Agents Remember. It gives a concise product-level explanation, a high-signal Core Features section, a short quickstart, a Run The Dashboard section (the CLI install/run story through a locally built wheel), links to harness-specific install pages, optional benchmark guidance, and a compact repository/runtime map. The concentrated feature tour lives in `docs/features.md`; detailed setup, concepts, workflows, benchmark methodology, guides, and reference material live under `docs/`.

## Code Commentary

### Logic

The README documents ordinary isolated pytest development, explicit integration selection and genuine Dagger-only certification. Combined branch coverage is diagnostic changed-code coverage and the CRAP review threshold is 20; neither score blocks delivery.

The README's `<h3>` headline frames Agents Remember in two parts — git-verified records of what coding agents know, and a control plane for what they do. Below it, the README uses `## Core Features` as the fast product pitch. It frames Agents Remember as project memory coding agents can verify and act on, shows the source-file to onboarding-unit mapping, and names the user-facing features a skimming reader needs in the first thirty seconds: path-addressed memory, Git-proven freshness, memory that lands with code through external-memory ledgers and dual worktrees, repo-owned `system/` behavior, and a harness-ready first run.

The retrieval bullet names by-path evidence and states that the former semantic and code-graph providers are retired. The memory bullet names converted cards, structured records and Curator judgment rows. The `Harness-ready first run` bullet says to register the MCP server with the harness and that the server serves skills from its installed package, so registration installs no second skill tree. The Requirements section states that setup neither enables the retired providers nor needs Docker, Ollama or an embedding-model download.

The first-run model the page states is neither an MCP install of skills nor a copied
starter package. Quickstart step 1 is the MCP authority settings file — copy
`examples/mcp/settings.example.json` to `~/.config/agents-remember/agents-remember-settings.json`
(under `XDG_CONFIG_HOME` when set) and replace its paths with absolute ones: the coordination folder (it may not exist yet), the workspace root, the
transcript folder and one entry per code repository. Step 2 registers the wheel with `uvx
--python 3.14 --from <abs>/built-wheel.whl agents-remember-mcp --config
<user-config>/agents-remember/agents-remember-settings.json`, adapting the common registration
example `examples/mcp/server.example.json` within the configuration envelope of the harness
guide, then restarts the harness once so it starts the server. Step 3 is one call in a chat
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
installed build and no separate skill-install route exists. In the source checkout section, root `skills/` is the canonical authoring tree and
`scripts/sync-skills.py` refreshes only the packaged copy that is served, while the runtime-asset
paragraph names root `agents-md-files/`, `benchmarks/`, `providers/` and `system/` as sources
refreshed by `scripts/sync-runtime.py`; this checkout has no `agents-md-files/` folder and the
synchronizer targets only the other three. Harness registration uses the common MCP registration
example adapted per harness guide; product installation leaves existing harness folders alone, and
server settings use the user-config directory. The installed `ar-coordination/` layout lists no
`skills/`, and the page says why: the server serves the packaged copy, so the coordination root
carries no second skill tree to keep current. The generated-copy checks are
`sync-skills.py --check` and `sync-runtime.py --check`.

A `## What It Looks Like In Practice` mini-transcript sits between Core Features and the Live Demo: it shows a source file's by-path onboarding note, the task-start `context_packet`/`memory_quality_check` calls, and the read-onboarding-then-propose-then-refresh loop — a concrete picture of the by-path loop for skimming readers.

The post-quickstart workflow sentence uses the host role-start route. Free chat answers questions inline. For managed-repository work it creates or resolves the sprint document, writes the developer’s request into it, calls `role_start` once for an Architect without any document reference or brief, and tells the developer where the agent and request are. The developer speaks with the started Architect in the dashboard. A different role is started this way only when the developer explicitly names the role and task. A launched role follows its handover; unbound `role_message` remains refused, and a refusal admits no alternative launch route. The agent resolves context with `context_packet`, checks memory quality through the l-01 knowledge-commands reference, reads onboarding beside code and updates onboarding after approved changes.

A ToC-linked `## Run The Dashboard` section sits between Quickstart and
Documentation. For this checkout it leads with the local artifact: build the dashboard bundle
and sync it (`npm --prefix dashboard run build`, then `python3 scripts/sync-dashboard.py`),
build the wheel, install it as a uv tool (`uv tool install --python 3.14 <wheel>`) and start
`agents-remember dashboard` (`--config` is optional: the CLI reads
`~/.config/agents-remember/agents-remember-settings.json`, under `XDG_CONFIG_HOME` when set,
independently of the working directory, and an explicit path overrides it). It keeps daemon mode (`--daemon`/`--status`/`--stop`, state under
`<coordinationRoot>/logs/dashboard/`) and the `"dashboard": {"autoStart": true}` settings key. The historical published `3.0.0rc8` pin is documented as the Python 3.13 artifact rather
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
- Use `docs/` for user-facing docs, `benchmarks/` for optional benchmark fixtures, `AGENTS.md` and the served skills for agent behavior, and onboarding for durable repository knowledge.
- Keep public language focused on the current intended install model: write the MCP authority settings, register the server by adapting the common registration example to the harness's configuration, restart once, and make one `role_start(role="bootstrap", …)` call whose dashboard chat carries setup onward into a user-started Architect. No starter package, rendered settings or skill folder is copied, and memory stays in a memory repository of its own under `ar-coordination/memory-repos/ar-<repo>/` — the only supported topology. The former repo-local `ar-memory/` internal mode was removed from the product and is refused by name; do not describe it as an available or default option.
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

The README does not depend on external harness docs for detailed setup claims; those claims live in the dedicated install pages.

No external documentation is needed to prove the root README's current structure; it is a same-repository public overview and link hub.

## Evidence

### Repo-Internal References

The README routes readers into the split documentation tree and gives the current runtime/source layout.

- The README has a `## Live Demo` section stating Agents Remember runs on itself and linking the project's own published memory repo (`Foxfire1st/ar-agents-remember`) as a live, inspectable by-path onboarding example. [3]

- The Requirements section names Python 3.14, the bounded package range, the historical published 3.13 artifact, and the canonical repository-development runtime documentation. [4]

- The quickstart is a short, harness-agnostic three-step agent-driven flow: copy `examples/mcp/settings.example.json` to the user-config settings path, register the locally built wheel with `uvx --config` by adapting the common registration example and restart the harness once, then make one `role_start(role="bootstrap", request_id="<UUID>")` call whose dashboard chat continues setup; no starter package, rendered settings or skill folder is copied. [5]

- The `## Run The Dashboard` section: local-wheel build/sync and install first-class, `dashboard` with an optional `--config` that reads the user-config settings file independently of the working directory, daemon mode + autoStart, and the historical published pin named as the 3.13 artifact. [7]

- The README keeps the source checkout layout distinct from the installed runtime layout, exposes root `skills/` as canonical, identifies `scripts/sync-skills.py` as the helper that refreshes the one served package copy and `scripts/sync-runtime.py` as the runtime-asset helper, points harness registration at the common MCP registration example, states that the installed runtime carries no `skills/` folder, and notes the workspace-first `<workspace>/ar-coordination/` default. [8]


- The README's Status first paragraph distinguishes the Python 3.14 source candidate from the historical Python 3.13 artifact at the same `3.0.0rc8` version, states core-path and harness maturity, and sends stability guarantees to Stability and release notes to GitHub Releases, the canonical changelog rather than a local CHANGELOG.md. Its second paragraph describes the 3.0 arc with the rc settling caveat; it is not authority to restore product-owned session or gate surfaces. [9]

- The Stability section is the semver promise: skill IDs (its examples are `l-01-agent-lifecycles` and `c-10-adopt-memory-baseline`), MCP tool names and their inputs/outputs, the `ar-coordination/` and `memory-repos/ar-<repo>/` layout, and the settings schema do not change without a major version bump; internals, provider internals and prompt wording may change in minor releases. [10]

- The Contributing section points contributors at CONTRIBUTING.md, restates the core rules, and tells contributors to download/clone the project's own published memory (Foxfire1st/ar-agents-remember) and use it as the active Agents Remember memory for their checkout while contributing (dogfooding the by-path onboarding loop). [11]








### Cross-Repo References

The README describes external memory in general terms, but this file-level onboarding does not rely on sibling repository internals.

No meaningful cross-repo references found for the README itself.

## Commit Gate Tiers

The README states this commit-gate contract:

- Both hooks are thin wrappers over `.githooks/_gate.sh`, which takes the tier as its argument.
- **pre-commit** runs the fast tier over the **staged** content: the generated-copy checks
  (`sync-skills.py --check`, `sync-runtime.py --check`), plus
  Ruff, **`ruff format --check`**, Pyright and deterministic dashboard checks.
- **pre-push** repeats the deterministic non-test checks over current-checkout bytes and records
  pushed refs; it does not run acceptance.
- Inside the Dagger graph the wrapper runs Ruff, formatting, file size, Pyright and Radon
  reports before pytest; CRAP and changed-lines coverage score that run's branch-coverage
  artifact last.

- **Agents Remember acceptance runs through the pinned Dagger graph only**, declared in the
  repository-owned `mcp/certification-profile-v1.json` and selected explicitly by
  `repositories.agents-remember.certificationProfile` in the MCP authority settings. Leaf and focused work use its targeted mode; the master
  integration gate runs its full mode exactly once. Both require the leaf/master's explicit Git
  diff base; the framework does not discover a wrapper or carry an Agents Remember command/report
  inventory.

Note that `sync-dashboard.py` is **not** among the generated-copy checks — it is a release
build step with no `--check` mode, because the bundle it places is not in version control.

## Welcome Image

The README presents the repository's mission-control welcome capture immediately below the canonical documentation links. The image is a product illustration, not an onboarding source: its PNG path remains excluded by the memory path rules.

## Acceptance And Workflow Model

The README distinguishes deterministic hooks and pull-request checks from lifecycle acceptance. Pre-commit/pre-push and GitHub PR validation are non-test checks; leaf closeout owns targeted Dagger once, leaf integration reuses its certified commit, and master integration owns full Dagger once. Ordinary Python development can use pytest directly as diagnostic feedback without Dagger admission, coverage, mutation or catalog preflight. Direct targeted Vitest remains diagnostic feedback. Neither development loop replaces the targeted/full acceptance graph; retry proof remains an internal attested-Dagger optimization.

## Host Install And Start

The product's install brings the Paseo host: the `runtime_install` step fetches the build's own Node, installs the host release the packaged contract names and starts it, so a user who follows the install types no host command. `agents-remember dashboard --daemon` makes sure the host runs; stopping or restarting the dashboard never stops it, and `agents-remember paseo stop --config <file>` remains the one host-stop command. `agents-remember dashboard --status` prints one line for the dashboard and one for the host.


- The install procedure the readme mirrors. [14]


- The dashboard daemon start ensures the dashboard daemon and then the host. [15]

- The docs index includes `docs/features.md` as the concentrated product tour alongside getting-started, concepts, workflows, install guides, guides, and reference pages. [12]


- Core Features names external Markdown/JSON memory, path-derived evidence, retired search providers, paired worktrees, structured records and Curator judgments with exact-tree publication checks; memory.md is an ignored attribution cache, and the harness-ready bullet registers the MCP server, which serves skills from its installed package. [1]

- The by-path mini-transcript reads source and card together; its current continuation puts Curator card/sidecar/record reconciliation and the recomputed worklist, validator and exact-tree gate before publication. [2]

- The documentation list starts with Features and links the Knowledge system reference alongside getting started, concepts, architecture, workflows, benchmarks, guides, settings and served skills. [6]

- The feature tour describes external Markdown/JSON memory, converted cards and sidecars, shared records and Curator judgment history; it keeps the setup and operational-guardrail tour, and its task-isolation section says worktree setup provisions no provider stack and describes the disposable SQLite knowledge index. [13]
