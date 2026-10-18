# docs/getting-started.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The first-run setup guide for a workspace that holds one or more code repositories. Setup is
agent-driven: the user asks the agent to do the work and answers one question along the way, and the
only mandatory restart in the package-based path is after copying the harness package and wiring the
MCP server.

## Current source account

The short path is: copy a harness starter package and render it (`render-starter` with one `--repo`
list, or replace the placeholders by hand); register the Agents Remember MCP server with `uvx` and an
absolute settings path outside `ar-coordination/`; restart the harness once; then invoke
`c-13-install-and-onboard`, which pre-checks setup, runs or verifies `runtime_install()`, sets up the
memory repo (it asks whether to scaffold a new one or use an existing one), bootstraps onboarding,
and starts provider indexing.

The guide states the resolver's memory topology: external memory is the only supported topology,
bound at `ar-coordination/memory-repos/ar-<repo>/`, initialized by the `c-13-install-and-onboard` and
`c-00-initialize-memory-repo` skills; a repository still carrying the removed repo-local `ar-memory/`
root is refused with that path and the route to re-point it. A new memory repo's onboarding runs
`c-03-repo-bootstrap`, for which a thin `overview.md` is enough to start.

Its Providers section records that MIK-R112 removed the provider tools: no product path installs,
starts or watches `codegraphcontext-code` / `grepai-memory`; the install skill stops leftover watcher
processes and reports old provider keys once as unused, and there is nothing to start. Providers are
optional for memory, onboarding, drift and task workflows.

The working section routes sessions by role through `l-01-agent-lifecycles` and states the normal
task loop: resolve the repository context, run the memory quality check, read the onboarding beside
the code, propose, wait for approval, implement, then update onboarding through the c-05 workflow.
Work that needs a durable plan escalates to `w-02-light-task-workflow` or a master series.

## Boundaries

Guidance for a person and an agent, not proof that a command ran, that a harness copied the package,
or that a memory repo was initialized on any host.

The document is not internally uniform on providers: its short path still says the install skill
starts provider indexing, while its Providers section says the provider tools were removed and there
is nothing to start. The card records both statements and resolves neither.
