# mcp/src/agents_remember/application/review_family_sources.py

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

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The rows below name the projection, its two helpers, the one caller and the production-path cases that
drive it over two real datasets and two real Git trees.

- **One recorded realization claim projected as a side-bound reference, refusing a claim read without its stored role or rationale.** [1]
- **The locator state stated through the model's own rule, from the observation's locator, exactness and ranges.** [2]
- The diagnostic sentence one source reference has always carried, unchanged. [3]
- The one caller: the roster owner's member composition. [4]
- **The value and the rule this projection fills.** [5]
- **The structured ranges this projection carries, filled by the resolver on the exact recorded blob only.** [6]
- **Two members in one file keep two locators, two ranges and two stored rationales; a line range and a file locator resolve as their own states.** [7]
- **A changed file keeps its unchanged attributed range on each side.** [8]
- **Every pre-existing field keeps its published value; only the three new fields are added.** [9]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
