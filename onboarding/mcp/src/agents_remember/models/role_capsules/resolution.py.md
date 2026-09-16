# mcp/src/agents_remember/models/role_capsules/resolution.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                            |
| path                   | `mcp/src/agents_remember/models/role_capsules/resolution.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-09-16T08:56+02:00 |
| lastVerifiedCommitHash | `e9300687218205ec1c4b0b86f96d3ac7c2f344d3` |
| lastVerifiedCommitDate | 2026-09-16T09:41:55+02:00|
| governingOverview      | `../overview.md`                           |

## Governing Overview

[models overview](../overview.md)

## Purpose

Resolving each declared instruction identity to **exactly one** source block. Three outcomes
are permitted; the difference between them is the whole point of this module, and anything
else stops compilation.

## Code Commentary

### Logic

| Outcome | Meaning | Recorded as |
| --- | --- | --- |
| **One source** | the ordinary case; the block is composed once | a plain candidate |
| **Duplicate identity that collapses** | two admitted sources carry the same identity with byte-identical content | `duplicate-identity` collapse, exactly one block survives |
| **Explicit supersession** | the admitted binding names an override | the superseded identity is replaced wholesale, provenance preserved |
| **Contradiction at equal authority** | two different contents claim one identity with no declared winner | `equal-authority-contradiction` — **compilation stops** |

The stop is the module's reason to exist: *picking by filename, by path order, or by "last one
wins" would make the delivered instructions depend on an accident nobody wrote down.*

cit:([`gather_candidates`], mcp/src/agents_remember/models/role_capsules/resolution.py:93-134) collects every admitted source that claims a declared
identity, tiered by composition root through cit:([`_TIER`], mcp/src/agents_remember/models/role_capsules/resolution.py:49-52).
cit:([`resolve_instructions`], mcp/src/agents_remember/models/role_capsules/resolution.py:135-191) reduces each identity to its winner and returns them in
cit:([`_ordered`], mcp/src/agents_remember/models/role_capsules/resolution.py:192-204) contract order. cit:([`Candidate`], mcp/src/agents_remember/models/role_capsules/resolution.py:55-61) and
cit:([`ResolvedInstruction`], mcp/src/agents_remember/models/role_capsules/resolution.py:64-91) are the working shapes, the latter exposing
cit:([`tier`], mcp/src/agents_remember/models/role_capsules/resolution.py:76-78) and cit:([`block`], mcp/src/agents_remember/models/role_capsules/resolution.py:79-91).

Overrides are validated rather than trusted: cit:([`override_winners`], mcp/src/agents_remember/models/role_capsules/resolution.py:205-220) maps each superseded
identity to its winner, cit:([`_supersessions`], mcp/src/agents_remember/models/role_capsules/resolution.py:262-284) fans an override out to the identities it
supersedes, and cit:([`_require_override_target`], mcp/src/agents_remember/models/role_capsules/resolution.py:285-335) refuses an override that targets something
unselected or that pulls an earlier tier over a later one — an override may only replace a
block from the same or a later tier, so provenance cannot be used to smuggle authority
backwards. cit:([`_require_one_identity`], mcp/src/agents_remember/models/role_capsules/resolution.py:221-261) is the equality-conflict gate.

### Conventions

A collapse and a supersession are both **recorded**, not silent: the diagnostic manifest gets
the collapse or the override's provenance. A refusal is a typed `CapsuleCompilationError`, and
a stopped conflict carries structured conflict rows.

### Invariants And Boundaries

- Exactly one block per identity survives. Two surviving blocks for one identity is a bug.
- A byte-identical duplicate collapses; a different body at the same identity with no declared
  winner **stops compilation**. Never resolve it by filename, path order, or recency.
- Composition-root tier order is fixed. An override may replace a block from the same or a
  later tier; it may not pull an earlier tier over a role block.
- An override that supersedes an identity which is not selected, or that two overrides claim
  for one identity without an orderable winner, is refused as such.
- Override provenance is preserved into the manifest; the winner is named explicitly.

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
| The override and selection-reason value types this module consumes. | `CapsuleOverride`; `SELECTION_EXPLICIT_SUPERSESSION`; `SUPERSEDE_DUPLICATE_IDENTITY` | mcp/src/agents_remember/models/role_capsules/types.py:261-280; mcp/src/agents_remember/models/role_capsules/types.py:68-78 |
| The stopped-conflict code the equal-authority case resolves to. | `STATUS_EQUAL_AUTHORITY_CONTRADICTION`; `STATUS_UNKNOWN_SUPERSESSION`; `STATUS_SUPERSESSION_CONFLICT` | mcp/src/agents_remember/models/role_capsules/statuses.py:17-23 |
| The compiler step that calls gathering and resolution in this order. | `compile_role_capsule` | mcp/src/agents_remember/models/role_capsules/compiler.py:90-153 |
| The declared plan and admitted sources this module reduces over. | `CapsuleDeclaredInstruction`; `CapsuleSource` | mcp/src/agents_remember/models/role_capsules/sources.py:32-49; mcp/src/agents_remember/models/role_capsules/sources.py:50-95 |
| The collapse, stop, override-provenance and override-ordering cases. | `test_duplicate_identity_with_byte_identical_content_collapses_to_one_block`; `test_duplicate_identity_with_a_different_body_stops_compilation`; `test_an_explicit_override_records_its_provenance_and_selects_the_winner`; `test_an_override_that_pulls_an_earlier_tier_over_a_role_is_refused`; `test_two_overrides_for_one_identity_are_refused_as_unorderable`; `test_an_override_may_replace_a_block_from_a_later_tier` | mcp/tests/test_role_capsule_compiler.py:608-629; mcp/tests/test_role_capsule_compiler.py:630-650; mcp/tests/test_role_capsule_compiler.py:651-684; mcp/tests/test_role_capsule_compiler.py:704-724; mcp/tests/test_role_capsule_compiler.py:748-776; mcp/tests/test_role_capsule_compiler.py:725-747 |

## Cross-Repo References

No sibling-repository contract defines this resolution rule.

| Finding | Citations | Source Path |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History

- 2026-09-16T08:56+02:00 — 260915-CAPS-L2 curator: created this card for the identity-resolution
  module added by the deterministic capsule compiler leaf (`CAPS-R02@v1`). Records the three
  permitted outcomes plus the equal-authority stop, the fixed tier order with the
  same-or-later-tier override rule, the override validation refusals, and the invariant that a
  collapse or supersession is recorded rather than silent. Verification metadata is left at the
  leaf base commit because the source is uncommitted — the governed closeout stamps the real
  code commit.
