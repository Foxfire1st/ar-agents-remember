# mcp/tests/test_f08_registered_handler_river.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Proves the first-call river through the actual registered handler and startup path: a bound first call carries its
caller and facts, an unbound chat harness calls the same way, a caller fixed after the startup binding rewrite is
still seen, and a fresh process writes its first call through startup into a row on disk.

## Code Commentary

### Logic

`_build_world()` authors a disposable coordination root and builds a server on it; `_binding_environment()`,
`_empty_binding_environment()` and `_isolated_environment()` give each case the binding it needs;
`_call_server_info()` is the first-call vehicle, and `_river_rows()`/`_assert_bound_row()` read the retained rows.
The evidence a case produces can be retained through `_retain_evidence()`.

- **Bound call.** `test_f08_bound_first_call_through_registered_handler` carries the caller and its facts.
- **Unbound chat.** `test_f08_unbound_chat_harness_through_registered_handler` calls without a binding.
- **Rewritten binding.** `test_f08_caller_fixed_after_startup_binding_rewrite` fixes the caller after startup and
  still sees it.
- **Fresh process.** `test_f08_fresh_process_first_call_through_registered_handler` spawns a child
  (`_f08_spawn_child_main()`) that builds its own world and server and calls the registered `server_info` once.

### Conventions

The river is exercised through the registered handler and, for the fresh-process case, through a real child
process, so a shortcut in the test cannot substitute for the startup path.

### Invariants And Boundaries

- The first call of a process reaches the river through the registered handler.
- A child process writes its own row; the parent does not write it for the child.

## Evidence

- A bound first call through the registered handler carries the caller and its facts. [1]
- A fresh process writes its first call through startup. [2]
- The first-call protocol vehicle is the registered `server_info`. [3]
