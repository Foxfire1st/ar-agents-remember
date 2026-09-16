# mcp/src/agents_remember/models/role_capsules/vocabulary.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/vocabulary.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `0dd1df9a950d59ac9622e5fb54250e528df08fa5` |
| lastVerifiedCommitDate | 2026-09-16T20:47:18+02:00|
| governingOverview      | `../overview.md`                           |

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

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The literal/tuple agreement guard, the launcher-is-not-a-role guard, and the ten-role/nine-operation census the leaf extended. | `test_the_frozen_vocabulary_is_exactly_the_ten_roles_and_nine_operations`; `test_the_role_and_operation_literals_agree_with_their_runtime_tuples`; `test_the_launcher_is_a_seat_kind_and_not_a_role` | mcp/tests/test_role_capsule_admission.py:148-153; mcp/tests/test_role_capsule_admission.py:155-160; mcp/tests/test_role_capsule_admission.py:162-166 |
| The independent role census this module's runtime tuple is compared against. | `SHIPPED_ROLES`; `SHIPPED_OPERATIONS` | mcp/tests/test_role_capsule_admission.py:76-87; mcp/tests/test_role_capsule_admission.py:89-98 |
| The parser that is handed this vocabulary and refuses a manifest that disagrees. | `parse_composition_manifest`; `MANIFEST_VOCABULARY_MISMATCH` | mcp/src/agents_remember/models/role_capsules/manifest.py:168-216; mcp/src/agents_remember/models/role_capsules/manifest.py:39-39 |
| The narrowing helpers that turn an untrusted string into a role or refuse it. | `narrow_operation`; `narrow_role` | mcp/src/agents_remember/models/role_capsules/selection.py:176-188; mcp/src/agents_remember/models/role_capsules/selection.py:191-213 |
| The canonical authored metadata that must agree with these tuples. | `"role_order"` | skills/l-01-agent-lifecycles/composition-manifest.json:6-17 |
| The settings registry kept in step with this vocabulary, so a published role is configurable. | `KNOWN_ROLES` | mcp/src/agents_remember/kernel/_agentic_settings_core.py:78-94 |
| The free-agent shape the tenth role carries, and the exclusion list it must not be added to. | `CAPSULE_ROLES`; `TASKLESS_SEAT_ROLES` | mcp/src/agents_remember/models/role_capsules/vocabulary.py:82-96; mcp/src/agents_remember/serving/task_binding.py:60-83 |

## Cross-Repo References

No sibling-repository contract defines this vocabulary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T17:59+02:00 — 260915-CAPS-L13 curator: **body rebased on the vocabulary extension this
  leaf made** (`CAPS-R13@v1`). The registry is now ten roles and nine operations: the card's Logic,
  its closed-registry invariant and every line range were re-derived against the source (the
  `cit:([...], path:a-b)` inline form was replaced with plain `path:start-end` citations, which is
  also what cleared this card's `citation_anchor_absent_from_range` family), the launcher is stated
  as *not an eleventh* role, and the new role's shape is recorded — present, deliberately last in
  registry order, and a **free agent** whose absent task altitude is the ruling rather than a missing
  field. Added the `KNOWN_ROLES` coupling invariant and its citation, and rewrote the three reference
  tables into the required `| Finding | Anchor | Source |` shape. Verification metadata is left at
  the leaf base commit because the source is uncommitted — the governed closeout stamps the real
  code commit.
- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the frozen role-capsule
  vocabulary added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  declared-over-manifest direction of authority, the closed nine-role/eight-operation registry,
  the reasons `launcher` is a seat kind rather than a tenth role, and the two narrowing helpers
  that are the only sanctioned entry from an untrusted string. Verification metadata is left at
  the leaf base commit because the source is uncommitted — the governed closeout stamps the real
  code commit.
