# mcp/src/agents_remember/mcp/registration/core.py

## Current operative account

Identity/orientation/install declarations use the light sentinel and lazily resolve payload builders and operation request constructors; task_context remains typed on both readers and explicitly supplied refresh remains refused.

- The registered tools are `server_info`, `context_packet`, `read_ar_files` and `runtime_install`.
- context_packet takes `repo_id`, `include_drift`, `include_freshness` and `task_context`; it has no `include_providers` parameter. It delivers slim roots, task ID/master, action lines and optional build/pair commits. The process serving-build commit is forwarded into this projection. Its drift description measures reference anchors of onboarding cards and tree validity (never blocking by itself), distinguishes invariant currentness via knowledge_read/knowledge_integrity_check, states MIK-R30 (update card or note why not; citation_fix repairs moved anchors and a curator re-authors stale ones), and repairs nothing; omitting include_drift measures nothing.
- `read_ar_files` takes up to 20 path strings, names cards, states and overview locations in its full form. A fuller eligible `brief` can carry recorded rule text and a file pointer. A compact row retains its path and can give applicable existence, card status and a brief pointer with saved freshness. A refusal row preserves its path and refusal code. The next write covering the file or its folder renews a missing or older saved brief when the writer can refresh it. If refresh cannot proceed, the writer reports `briefsProblem` and leaves the saved brief as it was. Source and card bodies stay in their files. The reply carries no session served state or continuation. The full row reports the counts `openWeaknesses` and `dependentDocuments` when nonzero; a count that cannot be taken is said once in `statesProblem` and refuses nothing. `refresh` remains receivable only for a typed removal refusal and is scrubbed from the advertised schema; object entries are refused.
- `resolve_context` is not registered or forwarded; orientation is `context_packet`. Read-only marks are applied centrally after all registrars; `context_packet` is marked false because its opt-in freshness capability fetches remotes.
- `runtime_install` describes reporting leftover removed stores without deleting them (not provider builds, watcher stops, or restarts); unused settings keys are described by `server_info`.

## Current source contract evidence

- The orientation registrar supplies the current naming/slim-packet and drift-description account; identity annotations and installer registration remain separately attributed. No execution acceptance is inferred.

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
- The registrar declares the mounted arguments and describes the brief reply. The lookup and answer fitting live in `application/read_files.py` and `application/read_files_briefs.py`.
- `server_info` must receive the shared process build; constructing or re-resolving a new build in
  the handler would break correlation with the dashboard and harness acceptance evidence.
- Serving-domain ownership stays behind `application.runtime.startup`; this MCP adapter consumes
  only the strict model payload.

### Role Runtime and Scope

server_info describes optional toolServer and agentBinding of a launched server. Registered context_packet/read_ar_files accept optional TaskScopedReaderContext with exact task and contract together; absent context keeps Projects scope. Core registration forwards typed requests without permitting caller-defined roots.

## Evidence


- The identity tool retains its explicit read-only/non-destructive/idempotent/closed-world annotations without restoring ping. [9]


- `read_ar_files_payload`, imported through the `mcp.tools` facade. [2]


- The registration takes the optional experiment parameter and builds the run's RuntimeInstallRequest itself. [4]



- Frozen implementation of `_register_identity_tools` supporting the stated file behavior. [5]



- The installation tools and the `runtime_install` registration. [7]


- The packet description states what `include_drift` measures and that omitting it measures nothing. [8]

- `_register_orientation_tools` declares `context_packet` and `read_ar_files` and removes the obsolete `refresh` argument from the advertised schema. [6]

## The install description and the skill corpus

The `runtime_install` description says the call installs/refreshes the coordinator scaffold (docs, user dirs), preserves `memory-repos/`, keeps skills package-served, reports leftover removed stores without deleting them, provisions the pinned `paseoRuntime` host/plugin while deferring host restart and keeping user-settings protections, refreshes a running dashboard, reports server currentness, previews with `dry_run=true`, and points to `docs/tool-details.md`.



- The install tool registration whose description states the scaffold install, running-server currentness report and running-dashboard refresh. [10]



- Identity/orientation/install declarations use the light sentinel and lazily resolve payload builders and operation request constructors; `task_context` remains typed on both readers and explicitly supplied `refresh` remains refused. [11]
