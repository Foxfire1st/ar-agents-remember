# mcp/tests/test_server_startup_imports.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The import boundary of a fresh server process: reaching tool discovery loads none of the implementation modules beneath the surface, and the guard is a fixed named list with its own positive control.

## Code Commentary

- A fresh interpreter answering `initialize` and a completed `tools/list` loads none of the tools behind the surface, compared by prefix against a written-out list.
- A positive control imports one implementation module eagerly, so a guard that never fires cannot pass for a clean one.
- The command the host actually launches answers `initialize` and `tools/list`, and a binding for another capability is refused at launch.
- A first call preserves the immutable boot identity, and an unexposed explainer dispatch is refused.

## Evidence

- The case `test_discovery_loads_no_implementation_module` protects tool discovery loading no implementation module behind the surface. [1]
- The case `test_the_guard_catches_an_eager_import` protects the guard reporting an eager import, so a silent guard cannot look like a pass. [2]
- The case `test_a_binding_for_another_capability_is_refused_at_launch` protects a binding for another capability being refused rather than served. [3]
- The case `test_the_real_command_answers_initialize_and_tools_list` protects the launched command answering the protocol's own initialize and tools list. [4]
- The case `test_first_call_preserves_immutable_boot_identity_and_refuses_unexposed_explainer_dispatch` protects the first call keeping the boot identity and refusing an unexposed explainer dispatch. [5]
