# mcp/src/agents_remember/models/role_capsules/vocabulary.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/vocabulary.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `e9300687218205ec1c4b0b86f96d3ac7c2f344d3` |
| lastVerifiedCommitDate | 2026-09-16T09:41:55+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

The frozen role and operation vocabularies a role capsule may be compiled for, declared in
code rather than read from the canonical composition manifest. This is the direction of
authority that makes a manifest edit fail instead of minting a new role.

## Code Commentary

### Logic

cit:([`CapsuleRole`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:20-32) is the nine-name
lifecycle-role literal and cit:([`CapsuleOperation`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:33-46) the eight-name operation literal; cit:([`CAPSULE_ROLES`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:64-75) and
cit:([`CAPSULE_OPERATIONS`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:77-89) are their runtime tuples, derived from the literals with
cit:([`get_args`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:55-59) so the two spellings cannot drift.
cit:([`CAPSULE_SEAT_KINDS`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:55-59) is the seat-kind
vocabulary (`role` / `launcher`) and cit:([`CAPSULE_COMPOSITION_ORDER`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:88-94) fixes
assembly as **core → role → operation → specialization**.

The module's load-bearing decision is stated in its own docstring and enforced by the
manifest parser: *the declared vocabulary is authoritative over the manifest, not the other
way round.* Because these tuples are declared here and handed to the parser, a manifest edit
that renamed or added a role or operation **fails compilation** rather than quietly minting
one. A caller-controlled string must never acquire another role.

``launcher`` is **deliberately absent** from `CAPSULE_ROLES`. The ambient launcher is a
routing condition, not a tenth role; it is reached through cit:([`CAPSULE_LAUNCHER_MODE`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:52-55) and
composes its own core block.

The four narrowing helpers are the only sanctioned way to cross from an untrusted string into
the vocabulary: cit:([`is_capsule_role`, `is_capsule_operation`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:96-107) answer membership, and
cit:([`capsule_role_or_none`, `capsule_operation_or_none`], mcp/src/agents_remember/models/role_capsules/vocabulary.py:111-149) return the narrowed literal or `None` rather
than a coerced value.

### Conventions

Adding a role or an operation is a coordinated change: the literal, the runtime tuple, the
`__all__` list, the canonical `composition-manifest.json`, the role's or operation's source
file, **and** the generated copies must move together. The shipped check is what proves they did.

### Invariants And Boundaries

- The vocabulary is closed at **nine roles and eight operations**. A ninth operation or a
  tenth role is an explicit error, never a silent fallback.
- These tuples are the authority the manifest is validated *against*. Never invert that by
  reading the vocabulary out of the manifest.
- `launcher` is a `CapsuleSeatKind`, not a `CapsuleRole`. Do not add it to `CAPSULE_ROLES` to
  "simplify" seat handling — `CapsuleLauncherSeat` exists precisely so it needs no role.
- The literal types and the runtime tuples must stay derived from one another; a hand-written
  parallel tuple is the drift this module exists to prevent.

### Todos

None recorded.

## Docs References

No external or domain documentation is configured for this memory root
(`system/sources.md` has no entries), so no external documentation claim is made.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No relevant documentation found after checking live sources. | n/a | n/a |

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| The literal/tuple agreement guard and the launcher-is-not-a-role guard. | `test_the_frozen_vocabulary_is_exactly_the_nine_roles_and_eight_operations`; `test_the_role_and_operation_literals_agree_with_their_runtime_tuples`; `test_the_launcher_is_a_seat_kind_and_not_a_tenth_role` | mcp/tests/test_role_capsule_admission.py:146-152; mcp/tests/test_role_capsule_admission.py:153-159; mcp/tests/test_role_capsule_admission.py:160-165 |
| The parser that is handed this vocabulary and refuses a manifest that disagrees. | `parse_composition_manifest`; `MANIFEST_VOCABULARY_MISMATCH` | mcp/src/agents_remember/models/role_capsules/manifest.py:168-216; mcp/src/agents_remember/models/role_capsules/manifest.py:39-43 |
| The narrowing helpers that turn an untrusted string into a role or refuse it. | `narrow_role`; `narrow_operation` | mcp/src/agents_remember/models/role_capsules/selection.py:176-190; mcp/src/agents_remember/models/role_capsules/selection.py:191-213 |
| The canonical authored metadata that must agree with these tuples. | `"role_order"` | skills/l-01-agent-lifecycles/composition-manifest.json:1-4 |

## Cross-Repo References

No sibling-repository contract defines this vocabulary.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the frozen role-capsule
  vocabulary added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the
  declared-over-manifest direction of authority, the closed nine-role/eight-operation registry,
  the reasons `launcher` is a seat kind rather than a tenth role, and the two narrowing helpers
  that are the only sanctioned entry from an untrusted string. Verification metadata is left at
  the leaf base commit because the source is uncommitted — the governed closeout stamps the real
  code commit.
