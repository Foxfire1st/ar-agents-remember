# mcp/src/agents_remember/mcp/registration/role_agents.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Registers `role_start`, the Manager-owned `role_start_set`, `user_settings_init`, and `role_message` with their explicit caller-visible contracts.

## Code Commentary

Role calls build their existing strict call models, then resolve the existing payload before offloading it. Registration imports no role payload implementation.

### Current Contract

The existing typed start/message/set/settings registrars remain the public surface. Current compact descriptions advertise start agent-id/rejected outcomes (with 60-second serialization wait) and message wait/held/cancellation outcomes plus the longer reference. Mode/feature policy, attachments/hashes, capacity, successor and receipt authority stay with the input/application/reference owners, not a claim that every detail is still inline in the short docstrings. Held answer overrides remain distinct from ordinary compact delivery.

## Current Contract

The existing role_start registrar accepts optional step_up and passes it unchanged into RoleStartCall before delegating blocking work through the shared request-thread runner. The registrar adds no mode parameter, permission override, counted-try policy, retirement or launch authority; its compact description remains only the short public summary. role_start_set and role_message keep their existing registration/ownership and do not gain this new argument. The shared request-thread runner drains blocking work for both registered role-start handlers before propagating cancellation. `role_message` and `user_settings_init` run through the detached request-thread runner instead: a cancellation ends the request at once, and an error the worker raises later is still written to the tool log.

## Current source contract

The role_message description distinguishes host acceptance from AR acceptance: a waited consuming turn ending is not AR acceptance. Held means queued for delivery when the recipient can take it, and the caller must never resend held; hold-store capacity stays with the delivery/reference owners rather than inline in the shortened docstring. Input shape, host delivery ownership and permission boundaries remain unchanged.

- Message docstring clarifies host-only acceptance, queued held delivery and no resend. [10]

## Evidence


- Workers read failed tries from typed code rounds and Curators from typed memory rounds. A record-only correction revises the existing round without counting as another try. Incomplete typed history leaves the count unknown. [4]



- Reason admission, threshold and differing-harness/model inheritance boundary. [5]


- The caller harness name comes from MCP initialization. Role start forwards `step_up` into `RoleStartCall` and delegates launch through the shared request thread. [6]

- The registrar declares typed start/set/message inputs and delegates to their payload owners. The current `role_message` description distinguishes host acceptance from AR acceptance and says held is queued and must never be resent. [1]


- The typed role start, role start set and role message declarations expose the public inputs and compact descriptions. The payload owners retain launch, message and receipt policy. [3]


- The registration that mounts the role tools and the settings initializer. [8]


- The role registrars build typed calls and delegate to their payload owners. Both start handlers use the shared request-thread helper, which drains blocking work before propagating cancellation. [9]


- The settings initializer and role messages run through the detached request-thread helper. [11]

## The caller's harness name and the settings tool

`caller_harness_name` reads the client name the calling harness sent in its `initialize` request from the served request context, and answers `None` for a client that named nothing or for a call made outside a served request, so the launch reports an unknown caller harness rather than inventing one. `user_settings_init` is registered beside the three role tools, takes a target, an optional harness or per-role harnesses and a dry run, and runs its payload builder through the detached request-thread helper.

- The transport's own client name, or no name at all. [7]
