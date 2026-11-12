# mcp/tests/test_role_first_message.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Checks the first message of every allowed start, role by role: the same shared block arrives on both
start paths, a parentless and a parented start each carry the projection, and a successor, a step-up or a
restored launch says what it takes over. The matrix derives its combinations from the code, so a role
added to the may-start rule is exercised without a new case.

## Code Commentary

### Logic

**Historical source account, superseded by the current clause below:** `FirstMessageMatrixTests` builds one start per allowed combination and reads the message the launch
actually emits. `shared_block()` fills the block at the compiler, as a later source fills it, so the
shared-block case reads the compiler's outcome rather than a copy written into the message. The world and shared checks live in `role_first_message_support.py`; send-time whole-path negative controls and held-delivery guard cases live in `test_role_first_message_guards.py`. [Historical source custody: `mcp/tests/test_role_first_message.py` blob `cc2abd63701c52fbf53d57df04d23c5db4f4d05d` at code base `59b01fb8f72a38d2d27f9c37b8b9ca2513fd3fa0`; this is no current implementation claim.]

- **Both start paths.** `test_the_shared_block_comes_from_the_compilation_on_both_start_paths` covers a
  task-bound leaf role and a taskless architect.
- **The projection.** `test_parentless_starts_carry_the_projection`,
  `test_parented_starts_carry_the_projection` and
  `test_the_system_specialist_alias_carries_the_projection` — the last for a taskless seat whose alias
  role projects the investigator's material — keep the projection on every shape of start.
- **Seats and successions.** `test_a_held_seat_opens_with_a_sane_first_message`,
  `test_a_started_set_gives_each_seat_a_sane_first_message`, `test_a_successor_names_the_seat_it_takes_over`
  and `test_a_step_up_names_the_material_it_takes_over` keep a seat's opening message sane and its
  succession explicit.
- **Restored launches.** `test_a_restored_launch_sends_the_saved_message_and_files` replays the saved
  message and its files rather than rebuilding them.

### Conventions

Every case starts from the role matrix and asserts on the emitted message text, so a message built by a
second path is caught by the same expectation.

### Invariants And Boundaries

- The shared block has one producer: the compiler.
- A restored launch sends what was saved; it does not recompile the message.

`composition_corpus` supplies real copied corpus and manifest bytes while leaving production admission and compilation intact. Declared every-role bytes reach both task-bound Worker and taskless Architect exactly once; an undeclared shared source emits no shared block. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance.

## Evidence
- The main matrix derives its allowed start combinations from the code and checks the emitted messages. [Past-epoch source caption, detached from live reference 1. Recorded citation custody: mcp/tests/test_role_first_message.py blob cc2abd63701c52fbf53d57df04d23c5db4f4d05d (available); historical event commit not identified. No historical event or intent inferred.]

Current source: FirstMessageMatrixTests derives its start cases from imported role, harness, parent, leaf and taskless tables and checks emitted or held-opening messages for parentless, parented, held-seat, set-start, successor, step-up and restored launches. Separate controls require an admitted shared block exactly once and no heading when the source is undeclared.


- Which emitted paths must exist is decided by one predicate in the shared first-message support. [2]

- The guard case checks whole whitespace paths, send snapshots and absence of a required snapshot. [3]

- The shared helper reads emitted whole paths from delimited message text and structured projection values. [4]

- FirstMessageMatrixTests derives its start cases from imported role, harness, parent, leaf and taskless tables and checks emitted or held-opening messages for parentless, parented, held-seat, set-start, successor, step-up and restored launches. Separate controls require an admitted shared block exactly once and no heading when the source is undeclared. [1]

- `composition_corpus` supplies real copied corpus and manifest bytes while leaving production admission and compilation intact. Declared every-role bytes reach both task-bound Worker and taskless Architect exactly once; an undeclared shared source emits no shared block. These are source assertions/support behavior, not a fresh invocation, host result or AR acceptance. [5]
