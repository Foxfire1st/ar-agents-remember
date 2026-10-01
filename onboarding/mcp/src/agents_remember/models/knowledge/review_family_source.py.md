# mcp/src/agents_remember/models/knowledge/review_family_source.py

## Governing Overview

[models route overview](../overview.md)

## Purpose

**One recorded realization claim of a family member, as the review payload references it (ICR-R31@v1).**
This is the source-reference half of the family review vocabulary: `ReviewFamilyMemberSource`, the
`ReviewSourceLocatorState` it names, and the one rule — `source_locator_state` — that decides which
locator fact a side established. `models/knowledge/review_family_context.py` imports and re-exports all
three, so callers keep importing from there.

A reviewer needs the exact region each claim attributes: two members realized in one file are two regions
with two explanations, not one file. So every source reference carries, per side and per claim, the
claim's identity, its **stored role and rationale unchanged**, the address the side's read observed, the
anchor's **structured recorded locator**, the **line ranges** the read's anchor resolver placed that
locator on in *this side's* exact recorded blob, and a **locator state**. Nothing is parsed from the
diagnostic `detail` sentence.

## Code Commentary

### Logic

**The four locator states are four different facts:**

| `locator_state` | The fact | What the reference carries |
| --- | --- | --- |
| `resolved` | the resolver placed the locator on the exact recorded blob of this side | one or more `resolved_ranges` (every defining extent of a symbol, or the recorded line range) |
| `whole_file` | a `file` locator on the exact recorded blob | the locator, no range — the whole blob is the place |
| `unresolved` | a recorded locator this side could not place on the recorded bytes | the recorded locator and no range; `resolution` and `detail` say why (a different blob, an absent path, a symbol the bytes do not define, a recorded range past the blob's end, no tree requested) |
| `not_observed` | the read reported no anchor observation for the claim at all | no path, no resolution, no locator |

`source_locator_state(locator, *, exact, ranged)` is the one rule: no locator → `not_observed`; ranges →
`resolved`; an exact blob with a `file` locator → `whole_file`; otherwise `unresolved`. The projection in
`application/review_family_sources.py` states each source's state through this function and the model's
validator checks it through the same function, so the two cannot come to disagree about what a range
means.

**Two validators refuse every way a range could be invented.**
`_require_an_address_to_travel_with_its_observation` keeps `path` and `resolution` together and `path` and
`locator` together — an address without an observation reads as a resolved realization, and a locator
without its address places a region at no path. `_require_the_locator_state_to_match_what_it_carries`
refuses ranges beside any resolution other than `exact_recorded_blob` and any `locator_state` that is not
the one `source_locator_state` derives from the locator, ranges and resolution carried beside it — so
ranges presented as unresolved, a resolved state with no range, or a whole file claimed for a narrower
locator are all construction errors.

**`role` and `rationale` are required.** The store's claim columns are NOT NULL and admission requires a
rationale, so an optional field would model an unreachable state and invite a blank rendering; both are
`str` with a minimum length of one and carried exactly as stored.

### Conventions

- `resolved_ranges` defaults to `()` and `locator` to `None`; `locator_state` has no default, so a
  constructor always states which fact it is.
- Bounds come from `models/knowledge/base.py`; the locator types are the storage owner's own
  (`models/knowledge/source.py`), so the wire carries the same `{kind, …}` shapes the store records.
- `__all__` publishes the three names; `review_family_context.py` keeps all three in its own `__all__`.

### Invariants And Boundaries

- **A region is only ever stated on bytes this side's read found at the recorded path.**
- **No range is guessed.** An unresolved locator carries its recorded value and no range; the reason lives
  in `resolution`/`detail`, which are carried unchanged from the observation.
- **Additive only.** The nine fields the roster published before locators were carried keep their names and
  values; `locator`, `resolved_ranges` and `locator_state` are added beside them.
- **Boundary.** A reference, not a verdict: whether the address still realizes the obligation, whether the
  bytes moved and what that means stay with the source inventory and the relationship union.

### Todos

None recorded.

## Evidence

### Docs References

No domain documentation source is configured for this repository (`system/sources.md` carries no
`Domain Documentation` entries). The statements below are grounded in repository source only.

No configured domain documentation could be checked.

### Repo-Internal References

The rows name the declarations, the one producer that fills them and the cases that pin each state.

- The published surface of the member-source reference. [1]
- **The four locator states and what each one carries.** [2]
- **One recorded realization claim as a side-bound source reference, with required role and rationale and the structured locator, ranges and state.** [3]
- **The validator keeping the address, its observation and its locator together.** [4]
- **The validator refusing ranges off the exact blob and any state the carried facts do not support.** [5]
- **The one locator-state rule shared by the projection and the validator.** [6]
- The re-export that keeps every existing import from the family-context module working. [7]
- The projection that fills a reference from one claim and its side's anchor observation. [8]
- **The value case refusing a reference whose state, ranges or locator disagree, or that lacks role or rationale.** [9]
- **The production-path cases for `resolved`, `whole_file` and `unresolved` on two real sides.** [10]
- The dashboard's mirror of this reference. [11]

### Cross-Repo References

No cross-repository behavior is implemented in this file.

No meaningful cross-repo references found.
