# docs/install/README.md

## Governing Overview

[Repository overview](../../overview.md)

## Purpose

The install-guide index: how to register the Agents Remember MCP tool server with each agent harness
and what the normal first-run path is. Per-harness pages are linked from it. The current page carries
no starter package and no skill folder: the server serves the canonical skills as MCP resources, the
optional native instruction or hook file carries only the first-action directive, and its path markers
are replaced by hand.

## Current source account

The normal path is to write absolute MCP authority settings, register the server with `--config` pointing to that file, restart or reload the harness, and call `role_start(role="bootstrap", request_id="<fresh UUID>")` from a chat with no task, sprint or repository selection. The call prepares a missing coordinator scaffold and host, verifies the plug-in and starts one parentless, taskless Bootstrap seat with its compiled instructions. The same request UUID reconciles to the same seat.

In that seat's dashboard conversation, the developer chooses the repository/memory root and each role's harness. Bootstrap initializes or reads the memory baseline, adopts content after review, and creates an absent user settings file; an existing user file is reported rather than overwritten. Model and effort may remain unset. At exit Bootstrap tells the developer to start an Architect, which organizes optional onboarding and knowledge foundation work as an ordinary task, master or sprint. Bootstrap itself authors no onboarding or knowledge and starts no role.

The shipped host remains Linux x86_64 with `/proc`, one exact host/whole npm lock, and Node 26.11.1 with its official archive digest. A missing `paseoRuntime` block is prepared in the active MCP authority settings file with absolute data/state paths and listen `127.0.0.1:8766`; an existing block is never rewritten. Invalid settings or a host that holds live sessions produce the actual failed stage and retained daemon state. They are not reported as a successful launch. The user role-settings file is a separate authority.

The Windows long-path prerequisite and projected-path `worktree_start` refusal remain documented. Optional per-harness instruction/hook/rule files carry only a first-action directive; users replace their path markers by hand. There is no renderer, starter package, copied skill folder or skill-install step.

## Boundaries

Instructions for a person and an agent; not proof that setup or installation ran, that a harness
restarted, or that a host was provisioned on any machine.

- Current source account and its stated boundaries. [1]
