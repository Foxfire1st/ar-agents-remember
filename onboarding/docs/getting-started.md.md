# docs/getting-started.md

## Governing Overview

[Repository overview](../overview.md)

## Purpose

The first-run setup guide for a workspace that holds one or more code repositories. Setup is
agent-driven and starts with one call after the MCP server is installed and registered with the
harness: `role_start(role="bootstrap", request_id="<fresh UUID>")` prepares a missing coordinator
scaffold and host, verifies the plug-in and starts one instructed Bootstrap seat whose dashboard
chat continues setup. The page names no starter package, renderer or skill folder, says the MCP
server serves canonical skills from its package as resources, keeps optional harness-native
instruction and hook files under the per-harness install guides, gives the source-built wheel
registration command with an absolute MCP settings path, and states that the authored settings
authority is separate from the user settings file that records the harness choice for each role. It
closes by saying setup authors no onboarding or knowledge and starts no other role: at exit it tells
the developer how to start an Architect, which organises optional onboarding and the knowledge
foundation as a regular task, master or sprint.

## Current source account

The short path the page now states is: register the Agents Remember MCP server with `uvx` and an
absolute settings path, restart the harness if it needs that to discover the connection, then make one
call from your own chat — `role_start(role="bootstrap", request_id="<fresh UUID>")` — whose answer
names the Bootstrap seat and the dashboard chat where setup continues. The page says no skill folder,
starter package or renderer is required, because the MCP server serves canonical skills from its
package as resources, and the optional harness-native instruction or hook file carries only the
first-action directive. In that dashboard conversation Bootstrap previews settings, chooses new or
existing memory, initializes or reads the external memory scaffold, reports an existing user settings
file instead of overwriting it, and at exit tells the developer to start an Architect, which organizes
optional onboarding and the knowledge foundation as a regular task, master or sprint. Nothing provider-side starts: the two former search providers are retired, and setup begins no provider indexing or watcher.

The guide keeps external memory at `ar-coordination/memory-repos/ar-<repo>/` as the supported layout. It refuses the removed repo-local `ar-memory/` path rather than migrating or recreating it. Existing memory is inspected and its baseline/state reported, with dirty or unusable input distinguished from an absent root. Setup authors no onboarding or knowledge and starts no other role; the developer starts an Architect to organize that work as a regular task, master or sprint.

Maintenance previews `runtime_install(dry_run=true)` and reconciles managed runtime files while preserving memory, tasks and user-owned state. It creates no skill copy. Benchmarks are optional and local outputs remain. Retired providers are reported as unused, and setup starts no provider indexing or watcher. Normal work follows the user-started Architect's task and approval workflow; role agents follow their exact handovers and read verified onboarding alongside source.

## Boundaries

Guidance for a person and an agent, not proof that a command ran, that a harness copied the package,
or that a memory repo was initialized on any host.



- Current source account and its stated boundaries. [1]


The document states the retirement once, in its provider sentence: retired providers are reported as unused and setup starts no provider indexing or watcher. No setup step it describes installs, starts or indexes a provider, so a new user is never sent to one.
