# mcp/src/agents_remember/mcp/tools/core.py

## Governing Overview

[overview.md](overview.md)

## Current source contract evidence

- Current candidate source supports the operative account; historical sections grant no current tool or execution acceptance. [7]

## Purpose

Build retained server information, scoped slim orientation and runtime-installation answers. `resolve_context_payload` is removed; there is no context-resolution adapter in this module.

## Code Commentary

`server_info_payload` receives the boot-resolved serving build, reports unusedProviderKeys and
optional launch agentBinding/toolServer, and does not publish tools/reservedTools or pretend to
remeasure build identity. `context_packet_payload` resolves the reader's exact task context
before calling the rich application builder, then applies `slim_context_packet` with the optional
serving-build commit. Mounted answers carry roots, task, action lines and short build/pair values;
the log preserves that delivered slim answer. Rich V2 is rebuilt through the internal/CLI/dashboard
builder, not automatically stored by this adapter. No TaskRef/resolve-context route remains.
Runtime installation forwards its per-call request unchanged; the request experiment takes
precedence over the documented environment fallback. With `request.dry_run=true`, the
adapter passes `report_path=None`: the preview files no per-call report and exposes no
`reportPath`. Only an executed install files the full result before response compaction
and supplies that report's path. Compaction projects only declared RUNTIME_INSTALL_ANSWER_FIELDS;
for a list of messages it retains string entries among the first five original entries,
truncates each to the short-string bound plus an ellipsis when needed, and reports overflow
from original list length. The rebind digest retains attempted/ok and phase/action/ok for
mapping-shaped runs. For an executed install, full detail can be reopened in its filed
report. Retained response logs are separate custody, not a per-call report for a preview;
the compactor's overflow wording does not establish that an unfiled preview has a report.
Removed ping and skills-install
adapters do not supply a generic restart or skill installation tool.

## Current evidence

- Current source excerpt `def server_info_payload(` identifies this section's adapter/control owner, not an executed success. [3]

- Current source excerpt `class ServerInfoResponse(ResponseModel):` identifies this section's adapter/control owner, not an executed success. [4]

- Current source excerpt `def runtime_install_payload(` identifies this section's adapter/control owner, not an executed success. [5]

- Current source excerpt `# Rule 2: a list with more entries is cut; the answer keeps the count, the` identifies this section's adapter/control owner, not an executed success. [6]

## Historical superseded account (non-operative)

Prior descriptions/evidence remain below for provenance. They are not current public
registration, provider/lifecycle/skill-install instructions or execution acceptance.



Server, context, install, and skills payload builders.

Builds server-info and orientation/install tool payloads through the shared token envelope.

## Code Commentary

### Logic

Holds `ping_payload`, `server_info_payload`, `context_packet_payload`,
`runtime_install_payload`, `resolve_context_payload`, and
`skills_install_payload`. `resolve_context_payload` takes one `TaskRef`
(`agents_remember.application.task_ref`) carrying `repo_id` plus whichever locator the caller holds
— `task_name`, `contract_path`, `leaf_id`, `parent_task` — and keeps `worktree_name`/`topology` as
separate keyword arguments, since neither is part of "which task".
`ping`/`server_info` are built locally from
`SERVER_NAME`/`SERVER_VERSION`/`TRANSPORT` and config; the rest forward typed
arguments to their application entry points (`build_context_packet`, `run_runtime_install`,
`resolve_context_tool`, `skills_install_tool`). `server_info_payload` reports
`PUBLIC_TOOLS`/`RESERVED_TOOLS` plus the caller-supplied, boot-resolved `ServingBuildPayload`. The
payload builder serializes that strict model directly and never reprobes or fabricates build
identity. **Since 260915-CAPS-L9 `runtime_install_payload(config, request)` takes the run's own
`RuntimeInstallRequest` unchanged** — the tool builds the request and hands it over, so the knobs
the tool exposes and the fields the application entry point reads cannot drift apart. That is
what makes `request.experiment` this run's own selection input: the tool's `experiment` parameter
supplies it, the `AR_EXPERIMENT` environment variable of the server process is the documented
fallback for a short-lived CLI/developer run, and the install payload names which one supplied
the mode in its record's `selectionSource`, so a long-lived server cannot leave an ambient switch
behind unnoticed. A dry run is a preview and files nothing (rule 6); only an executed install
files its report, and only then does the answer carry the path. The builder then
response-budgets the
result (S4, 2.5.1): the full install detail goes to a temp report via
`write_tool_report`, and `compact_runtime_install_payload` returns summary
counts, a rebind digest (`{attempted, ok, phases:[{phase, action, ok}]}`), the
first 5 messages plus an overflow marker, and `reportPath` (the rebind runs
were historically >50k chars inline). `skills_install_payload`
forwards `overwrite`/`archive_existing` alongside `dry_run` (the installer is a
flat copy, so there is no layout argument). `context_packet_payload` forwards
`include_providers`/`include_drift`/`include_freshness` (issue #54) into
`ContextPacketRequest`.

### Invariants And Boundaries

- Every builder returns through `base._tool_payload`.
- Imports `SERVER_NAME`/`SERVER_VERSION` via `..` and `McpRuntimeConfig` via
  `..config`.
- `runtime_install_payload`/`skills_install_payload` default `dry_run=False`
  (act-by-default), matching the server registration; `dry_run=true` previews.
- Keep the builder signatures in lockstep with the `RuntimeInstallRequest` /
  `skills_install_tool` contracts and the server registration (e.g. `no_cache`);
  the builder stays transport-thin and does not interpret these flags.
- `server_info_payload` requires an explicit `ServingBuildPayload`; package version alone cannot identify
  equal-version source or installed candidates.

### Role Runtime and Scope

server_info_payload adds toolServer and AgentBindingPayload only for readable bound identity; servingBuild remains the process/build owner fact. context_packet_payload derives optional call-local admitted config before invoking the existing context packet owner. No binding creates a second globally selected repository root.

## Series-Contract Notes

`resolve_context_payload` still resolves a nested task root and a specific leaf enclosure — the
`parent_task` and `leaf_id` locators now travel inside the `TaskRef` rather than as their own
keyword arguments, through the same response-model validation path as the rest of the core payload.

## L23 Runtime Package Review

Core tool adapters now import runtime installation from `application.runtime.install` and skill
installation from `application.runtime.skills`. Payload validation and transport-thin forwarding
remain unchanged; the move removes the former flat application-module ownership.

## Evidence



### Runtime Source References

- Frozen implementation of server_info_payload supporting the stated file behavior. [1]
- Frozen implementation of context_packet_payload supporting the stated file behavior. [2]

## Server info names no harness skill root

`server_info_payload` no longer reports `harnessSkillRoot`: no skill folder is resolved or installed, so there is no root to name, and `ServerInfoResponse` no longer declares the field. The remaining roots, allowed repo ids and unused provider/settings keys are reported as before.

- The server-info answer, which no longer carries a harness skill root. [8]
