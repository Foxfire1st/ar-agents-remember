# mcp/src/agents_remember/models/role_capsules/vocabulary.py

## Governing Overview

[models overview](../overview.md)

## Purpose

The frozen role and operation vocabularies a role capsule may be compiled for, declared in
code rather than read from the canonical composition manifest. This is the direction of
authority that makes a manifest edit fail instead of minting a new role.

## Code Commentary

### Logic

`CapsuleRole` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:36-48) is the ten-name
lifecycle-role literal and `CapsuleOperation` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:50-61) the nine-name operation literal; `CAPSULE_ROLES` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:82-96) and
`CAPSULE_OPERATIONS` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:98-111) are their runtime tuples, derived from the literals with
`get_args` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:31-31; mcp/src/agents_remember/models/role_capsules/vocabulary.py:76-76) so the two spellings cannot drift.
`CAPSULE_SEAT_KINDS` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:65-65; mcp/src/agents_remember/models/role_capsules/vocabulary.py:76-76) is the seat-kind
vocabulary (`role` / `launcher`) and `CAPSULE_COMPOSITION_ORDER` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:113-119) fixes
assembly as **core → role → operation → specialization**.

The module's load-bearing decision is stated in its own docstring and enforced by the
manifest parser: *the declared vocabulary is authoritative over the manifest, not the other
way round.* Because these tuples are declared here and handed to the parser, a manifest edit
that renamed or added a role or operation **fails compilation** rather than quietly minting
one. A caller-controlled string must never acquire another role.

``launcher`` is **deliberately absent** from `CAPSULE_ROLES`. The ambient launcher is a
routing condition, not an eleventh role; it is reached through `CAPSULE_LAUNCHER_MODE` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:73-73) and
composes its own core block.

``bootstrap`` is **present and deliberately last**: it is the new user's first-hour seat, the
only role that carries the `bootstrap` operation, and appending it to the registry order keeps the
nine roles that pre-date it at their existing positions — so a compilation, a settings key or a
dashboard projection addressed to an earlier role cannot shift because this one was added. It is a
**FREE agent, not a structural seat**: a session opens with `AR_SPAWN_ROLE=bootstrap` and no task
document, and its instructions are its compiled capsule rather than a dispatch brief. It is
deliberately absent from the task layer's altitude sets and from `serving/structural_seats.py`, and
the absent altitude must **not** be "fixed" by adding one — a task altitude is the wrong shape for
this seat.

The four narrowing helpers are the only sanctioned way to cross from an untrusted string into
the vocabulary: `is_capsule_role`, `is_capsule_operation` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:121-131) answer membership, and
`capsule_role_or_none`, `capsule_operation_or_none` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:133-155) return the narrowed literal or `None` rather
than a coerced value.

### Conventions

Adding a role or an operation is a coordinated change: the literal, the runtime tuple, the
`__all__` list, the canonical `composition-manifest.json`, the role's or operation's source
file, **and** the generated copies must move together. The shipped check is what proves they did.

### Invariants And Boundaries

- The vocabulary is closed at **ten roles and nine operations**. An unknown role or operation is
  an explicit error, never a silent fallback.
- These tuples are the authority the manifest is validated *against*. Never invert that by
  reading the vocabulary out of the manifest.
- `launcher` is a `CapsuleSeatKind`, not a `CapsuleRole`. Do not add it to `CAPSULE_ROLES` to
  "simplify" seat handling — `CapsuleLauncherSeat` exists precisely so it needs no role.
- `bootstrap` is the tenth role **and a free agent**. Its presence here makes it compilable; it does
  not make it a task seat, and its absent task altitude is the ruling rather than a missing field.
- The literal types and the runtime tuples must stay derived from one another; a hand-written
  parallel tuple is the drift this module exists to prevent.
- A role published here must be configurable: `kernel/_agentic_settings_core.py` `KNOWN_ROLES` is
  kept in step with `CAPSULE_ROLES` by a test, so an orchestration knob addressed to a published
  role cannot fail loud.

### Todos

None recorded.

## Evidence

### Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

No relevant documentation found after checking live sources.

### Repo-Internal References

- The literal/tuple agreement guard, the launcher-is-not-a-role guard, and the ten-role/nine-operation census the leaf extended. [1]
- The independent role census this module's runtime tuple is compared against. [2]
- The parser that is handed this vocabulary and refuses a manifest that disagrees. [3]
- The narrowing helpers that turn an untrusted string into a role or refuse it. [4]
- The canonical authored metadata that must agree with these tuples. [5]
- The settings registry kept in step with this vocabulary, so a published role is configurable. [6]
- The free-agent shape the tenth role carries, and the exclusion list it must not be added to. [7]

### Cross-Repo References

No sibling-repository contract defines this vocabulary.

No meaningful cross-repo references found.
