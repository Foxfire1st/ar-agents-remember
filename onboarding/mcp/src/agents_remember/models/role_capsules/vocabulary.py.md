# mcp/src/agents_remember/models/role_capsules/vocabulary.py

## Governing Overview

[overview](../overview.md)

## Purpose

The frozen role and operation vocabularies a role capsule may be compiled for, declared in
code rather than read from the canonical composition manifest. This is the direction of
authority that makes a manifest edit fail instead of minting a new role.

## Code Commentary

### Logic

`CapsuleRole` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:31-40) is the eight-name
lifecycle-role literal and `CapsuleOperation` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:43-53) the nine-name operation literal; `CAPSULE_ROLES` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:75-84) and
`CAPSULE_OPERATIONS` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:89-99) are explicit runtime tuples; the literal/tuple agreement test keeps their names and order in step.
`get_args` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:27-27; mcp/src/agents_remember/models/role_capsules/vocabulary.py:69-69) derives `CAPSULE_SEAT_KINDS`, not those two tuples.
`CAPSULE_SEAT_KINDS` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:58-58; mcp/src/agents_remember/models/role_capsules/vocabulary.py:69-69) is the seat-kind
vocabulary (`role` / `launcher`). The retained `CAPSULE_COMPOSITION_ORDER` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:104-109) lists
**core → role → operation → specialization**; actual seat composition uses
`CAPSULE_ROLE_COMPOSITION_ORDER` (**role → operation**) or
`CAPSULE_LAUNCHER_COMPOSITION_ORDER` (**core → operation**), selected by
`role_composition_order`. A role capsule receives no shared core block.

The module's load-bearing decision is stated in its own docstring and enforced by the
manifest parser: *the declared vocabulary is authoritative over the manifest, not the other
way round.* Because these tuples are declared here and handed to the parser, a manifest edit
that renamed or added a role or operation **fails compilation** rather than quietly minting
one. A caller-controlled string must never acquire another role.

``launcher`` is **deliberately absent** from `CAPSULE_ROLES`. The ambient launcher is a
routing condition, not a ninth role; it is reached through `CAPSULE_LAUNCHER_MODE` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:66-66) and
composes its own core block.

``bootstrap`` is **present and last** in the registry order: it is the new user's first-hour seat and
the only role that carries the `bootstrap` operation. It is a
**FREE agent, not a structural seat**: its session has no task document, and its instructions are
its compiled capsule. It is deliberately absent from the task layer's altitude sets
(`SPRINT_ROLES`/`MASTER_ROLES`/`LEAF_ROLES`), and
the absent altitude must **not** be "fixed" by adding one — a task altitude is the wrong shape for
this seat.

The four narrowing helpers are the only sanctioned way to cross from an untrusted string into
the vocabulary: `is_capsule_role` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:136-136) and `is_capsule_operation` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:156-156) answer membership, and
`capsule_role_or_none` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:162-162) and `capsule_operation_or_none` (mcp/src/agents_remember/models/role_capsules/vocabulary.py:176-176) return the narrowed literal or `None` rather
than a coerced value.

### Conventions

Adding a role or an operation is a coordinated change: the literal, the runtime tuple, the
`__all__` list, the canonical `composition-manifest.json`, the role's or operation's source
file, **and** the generated copies must move together. The shipped check is what proves they did.

### Invariants And Boundaries

- The vocabulary is closed at **eight roles and nine operations**. An unknown role or operation is
  an explicit error, never a silent fallback.
- These tuples are the authority the manifest is validated *against*. Never invert that by
  reading the vocabulary out of the manifest.
- `launcher` is a `CapsuleSeatKind`, not a `CapsuleRole`. Do not add it to `CAPSULE_ROLES` to
  "simplify" seat handling — `CapsuleLauncherSeat` exists precisely so it needs no role.
- `bootstrap` is the eighth role **and a free agent**. Its presence here makes it compilable; it does
  not make it a task seat, and its absent task altitude is the ruling rather than a missing field.
- The literal types and explicit runtime tuples must keep the same names and order;
  the literal/tuple agreement test guards this deliberate duplication.
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


- The eight-role/nine-operation census, the literal/tuple agreement guard and the launcher-is-not-a-role guard. [1]


- The independent role census this module's runtime tuple is compared against.


- The parser that is handed this vocabulary and refuses a manifest that disagrees. [3]


- The narrowing helpers that turn an untrusted string into a role or refuse it. [4]

- The canonical authored metadata that must agree with these tuples. [5]

- The settings registry kept in step with this vocabulary, so a published role is configurable. [6]



- The capsule role registry ends with bootstrap; no task-binding set supplies admission. [7]

### Cross-Repo References

No sibling-repository contract defines this vocabulary.

No meaningful cross-repo references found.

- The independent role census this module's runtime tuple is compared against. [2]
