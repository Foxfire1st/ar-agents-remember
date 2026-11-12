# mcp/src/agents_remember/mcp/registration/core.py

## Current operative account

Identity/orientation/install declarations use the light sentinel and lazily resolve payload builders and operation request constructors; task_context remains typed on both readers and explicitly supplied refresh remains refused.

- The registered tools are `server_info`, `context_packet`, `read_ar_files` and `runtime_install`.
- context_packet takes `repo_id`, `include_drift`, `include_freshness` and `task_context`; it has no `include_providers` parameter. It delivers slim roots, task ID/master, action lines and optional build/pair commits. The process serving-build commit is forwarded into this projection. Its drift description measures onboarding reference anchors and tree validity, reports a stale reference for repair while publication and the full quality run refuse it, distinguishes invariant currentness via knowledge_read/integrity, requires a changed-source card or no-impact record, and repairs nothing; omitting include_drift measures nothing.
- `read_ar_files` takes up to 20 path strings, names cards/states/overview locations and carries no file text, session served state or continuation. Per path it also names one count of the open weaknesses on the file and one count of the documents that stand on it (`openWeaknesses`, `dependentDocuments`), each absent at zero and never a record's text; a count that cannot be taken is said once in `statesProblem` and refuses nothing. `refresh` remains receivable only for a typed removal refusal and is scrubbed from the advertised schema; object entries are refused.
- `resolve_context` is not registered or forwarded; orientation is `context_packet`. Read-only marks are applied centrally after all registrars; `context_packet` is marked false because its opt-in freshness capability fetches remotes.
- runtime_install describes stop-only leftovers and unused provider keys, not provider builds or restarts.

## Current source contract evidence

- The orientation registrar supplies the current naming/slim-packet and drift-description account; identity annotations and installer registration remain separately attributed. No execution acceptance is inferred. [6] [7] [9]

## Governing Overview

[overview](overview.md)

## Code Commentary

The registered identity reader `server_info` retains explicit ToolAnnotations: `readOnlyHint=True`,
`destructiveHint=False`, `idempotentHint=True`, `openWorldHint=False`. These describe the identity
operation, not a promise that its admitted tool-call logging creates no bytes.

`register_core_tools` obtains one strict payload through the application-owned
`mcp_serving_build_payload()` gateway and passes that immutable value into the identity registrar;
every `server_info` call therefore reports the same boot and candidate identity without
request-time reprobes or an MCP-to-serving domain import.

### Invariants And Boundaries

- `runtime_install` registers `dry_run=False` — act-by-default; `dry_run=true` previews.
- No behaviour here. `read_ar_files`'s onboarding-lookup vocabulary lives in `application/read_files.py`.
- `server_info` must receive the shared process build; constructing or re-resolving a new build in
  the handler would break correlation with the dashboard and harness acceptance evidence.
- Serving-domain ownership stays behind `application.runtime.startup`; this MCP adapter consumes
  only the strict model payload.

### Role Runtime and Scope

server_info describes optional toolServer and agentBinding of a launched server. Registered context_packet/read_ar_files accept optional TaskScopedReaderContext with exact task and contract together; absent context keeps Projects scope. Core registration forwards typed requests without permitting caller-defined roots.

## Evidence

- The identity tool retains its explicit read-only/non-destructive/idempotent/closed-world annotations without restoring ping. [9]
- `read_ar_files_payload`, imported through the `mcp.tools` facade. [2]

- The registration takes the keyword-only `experiment` parameter and builds the run's request itself. [4]

- Frozen implementation of _register_identity_tools supporting the stated file behavior. [5]

- The installation tools and the runtime_install registration. [7]

- The packet description states what include_drift measures and that omitting it measures nothing. [8]

- `_register_orientation_tools` declares the read-only orientation tools `context_packet` and `read_ar_files` and scrubs the removed `refresh` argument from the advertised schema. [6]

## The install description and the skill corpus

The `runtime_install` description says the call refreshes the coordinator scaffold (instructions, docs, provider assets), keeps `memory-repos/` and `providers/data/`, prunes legacy binaries, installs no skill folder because skills are package-served, stops leftover provider watchers, reports unused provider keys and starts none, and provisions the pinned host/plugin from the active MCP authority's `paseoRuntime`. It also says daemon settings may be reconciled while user-settings protections and host-restart deferrals remain, that the result reports running-server currentness and every host action, and that a running dashboard is refreshed; `dry_run=true` previews the install actions.

- The install tool registration whose description states the scaffold install, running-server currentness report and running-dashboard refresh. [10]

- Identity/orientation/install declarations use the light sentinel and lazily resolve payload builders and operation request constructors; task_context remains typed on both readers and explicitly supplied refresh remains refused. [11]
