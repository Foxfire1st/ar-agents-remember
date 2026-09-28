# mcp/src/agents_remember/application/review_family_sources.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/application/review_family_sources.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-28T16:42:25+02:00 |
| lastVerifiedCommitHash | `9b2f775f1ab0fca5f82b4f661785dd8216d4a8b3` |
| lastVerifiedCommitDate | 2026-09-28T17:43:09+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[application route overview](overview.md)

## Purpose

**The projection of one recorded realization claim of a family member into its inspectable,
side-bound source reference (ICR-R31@v1).** The roster owner, `application/review_family_rosters.py`,
reads a family revision's members and hands each member's realization claims here through `member_source`.
This module owns only that projection: the claim's identity, its stored role and rationale, and what
*this side's* anchor observation established about the address — the path and blob identities, the
structured recorded locator, the line ranges the read's anchor resolver placed that locator on, and the
locator state that names which of those facts the side established.

**Nothing here resolves, searches or re-anchors anything.** The ranges are the resolver's own structured
values (`AnchorResolution.resolved_ranges`, filled by `memory/knowledge/read_anchors.py`); a locator the
resolver could not place on the recorded bytes is stated as `unresolved` beside the resolver's own
resolution, and the diagnostic `detail` sentence is composed *from* the observation and never read back.
Because each side is read with its own anchor resolver, the before and after sources of one claim carry
their own regions: a file whose blob changed while the attributed lines did not keeps that range on both
sides, and a side holding other bytes than the claim recorded carries the recorded locator and no range.

## Code Commentary

### Logic

`member_source(claim)` builds one `ReviewFamilyMemberSource` from one realization-claim `ReadItem`:

- **Role and rationale are carried exactly as stored, or the claim is refused.** The store's claim columns
  are NOT NULL, so a realization item without them is not a row this read produced; `member_source`
  raises a `RuntimeError` naming the claim rather than supplying text in their place (no `str(None)`).
- **The address fields come from the anchor observation or are all absent.** `path`,
  `recorded_source_identity`, `observed_source_identity`, `resolution` and `locator` are the observation's
  own, and `resolved_ranges` is the observation's own tuple — `()` when there is no anchor.
- **`locator_state` is stated by the model's one rule.** `_locator_state` calls
  `source_locator_state(anchor.locator, exact=…, ranged=…)` — the same function the model's validator
  checks against — with `exact` meaning `resolution == "exact_recorded_blob"` and `ranged` meaning a
  non-empty `resolved_ranges`; no anchor is `not_observed`.
- **`detail` is the sentence a source reference has always carried, unchanged.** `_detail` composes
  "the author recorded this realization at <path> (<resolution>): <observation detail>" or the
  no-address sentence, so every pre-existing field keeps its published value.

### Conventions

`__all__` publishes `member_source` only; the two helpers are private. The module imports only the read
vocabulary (`AnchorResolution`, `ReadItem`) and the member-source reference with its state rule.

### Invariants And Boundaries

- **No region from prose.** Ranges come only from `resolved_ranges`; `detail` is output, never input.
- **No range on bytes the side did not find**, and no guessed range for an unresolved locator — the model's
  validators refuse both, and this projection never constructs either.
- **Per side, per claim.** Two claims at one path keep two locators and two ranges; the projection never
  merges sources by path.
- **Boundary.** One claim in, one reference out. Which claims a page carries, the member they belong to and
  the page's completeness are the roster owner's; whether the address still realizes the obligation is the
  source inventory's and the relationship union's.

### Todos

None recorded. Rendering the region is the dashboard's work and is not done by this leaf.

## Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation could be checked. | — | — |

## Repo-Internal References

The rows below name the projection, its two helpers, the one caller and the production-path cases that
drive it over two real datasets and two real Git trees.

| Finding | Anchor | Source |
| --- | --- | --- |
| **One recorded realization claim projected as a side-bound reference, refusing a claim read without its stored role or rationale.** | `member_source` | mcp/src/agents_remember/application/review_family_sources.py:27-51 |
| **The locator state stated through the model's own rule, from the observation's locator, exactness and ranges.** | `_locator_state` | mcp/src/agents_remember/application/review_family_sources.py:54-63 |
| The diagnostic sentence one source reference has always carried, unchanged. | `_detail` | mcp/src/agents_remember/application/review_family_sources.py:66-77 |
| The one caller: the roster owner's member composition. | `member_source` | mcp/src/agents_remember/application/review_family_rosters.py:523-523 |
| **The value and the rule this projection fills.** | `ReviewFamilyMemberSource`; `source_locator_state` | mcp/src/agents_remember/models/knowledge/review_family_source.py:36-123 |
| **The structured ranges this projection carries, filled by the resolver on the exact recorded blob only.** | `resolved_ranges` | mcp/src/agents_remember/models/knowledge/read_anchor.py:64-69 |
| **Two members in one file keep two locators, two ranges and two stored rationales; a line range and a file locator resolve as their own states.** | "test_two_members_in_one_file_carry_their_own_locators_ranges_and_rationale" | mcp/tests/test_review_family_member_sources.py:262-290 |
| **A changed file keeps its unchanged attributed range on each side.** | "test_a_changed_file_keeps_its_unchanged_attributed_range_on_each_side" | mcp/tests/test_review_family_member_sources.py:293-311 |
| **Every pre-existing field keeps its published value; only the three new fields are added.** | "test_the_existing_source_fields_keep_their_published_values" | mcp/tests/test_review_family_member_sources.py:364-385 |

## Cross-Repo References

No cross-repository behavior is implemented in this file.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-09-28T16:42:25+02:00 — 260921-ICR-L44 curator (uncommitted change set on `ar/260921-icr-l44`, base `55c62237132eaa56b0df28ae5a8420a8dc05303d`): created this one-to-one card for the member-source projection moved out of the roster module (which previously held it as the private `_source`) and extended per ICR-R31@v1 to carry, per side and per claim, the structured recorded locator, the resolver's resolved ranges and the locator state, with role and rationale carried exactly as stored and required. The module is untracked at the base commit, so `lastVerifiedCommitHash` names the leaf base and the verified basis is the working-tree delta on top of it; the closeout records the real commit.
