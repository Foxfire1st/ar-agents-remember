# mcp/tests/pnt_sandbox_test_support.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

What the PNT sandbox test modules share: a sandbox directory, a directory that looks like a PNT build, real
child processes and a fake for the operations that would build or start something. Ports are chosen and claimed
per run, so two modules running at once do not collide.

## Code Commentary

### Logic

`free_port()`/`release_port()` pick a port nothing listens on and no other run of these modules has claimed, and
`ended()` waits until a killed session leader and what it started have left the process table.

`SandboxCase` gives a case its sandbox: `mark_built()`, `child()` (a real process, leader of its own session),
`end()` (kill it with its session and wait), `dashboard()`, `supervisor()`, `paseo_record()` and `good_roots()`.
Its `Path.exists` view hides named harness configuration markers at ancestors outside its owned fixture while
existence inside the fixture and for every other path uses the real filesystem, so production location guards and
lexical harness-path refusals still see what they would in a real checkout.

`FakeOperations` records every call that would run or start something — `build_python()`, `prepare_python()`,
`prepare_bundle()`, `render_settings()`, `resolve_roots()`, `tool_calls()`, `runtime_install()`, `paseo()`,
`spawn_dashboard()`, `paseo_supervisor()`, `dashboard_answers()`, `stop_tmux_server()` — and the processes it
reports are real children.

### Conventions

A process a case needs is started as a real child in its own session and ended with that session; nothing is
simulated where the tooling inspects `/proc` or a process record.

### Invariants And Boundaries

- A test never picks a port another run of these modules holds.
- Hiding a marker at an ancestor leaves the fixture's own paths and every other path real.

## Evidence


- The sandbox fixture, its real child processes, port claims and recorded fake operations. [1]


- `SandboxCase` hides named harness configuration markers at ancestors outside its owned fixture through a scoped existence view, while the fixture's own paths and all others use the real filesystem. [2]
