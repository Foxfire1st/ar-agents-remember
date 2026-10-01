# mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py

## Governing Overview

[memory_quality overview](../../../../overview.md)

## Purpose

Resolves every card's declared governing overview and reports the ones that do not
resolve — the check that closes D3/D16's product gap. Until this module, the product
validated that a source **has** a card and never that the card's declared route
**resolves**, so a card whose `governingOverview` field or whose
`## Governing Overview` body link pointed at a file that does not exist passed every
check the product runs and reported clean.

## Code Commentary

### Logic

Two declarations are graded per card, and only for a card that declares the field at
all. `_field_resolves` tries the field target relative to the card's own directory, then
relative to the onboarding root, then relative to the onboarding root's parent — three
bases, because two authoring conventions ship and the alternative is failing a form the
corpus actually uses. The body link is graded card-relative only (`_target_exists` on
`card_path.parent`), and that asymmetry is deliberate rather than an oversight: the field
is metadata a reader never clicks, while the body link is what a reader clicking it gets,
so the link is held to exactly what that reader experiences.

The two declarations fail **independently** and are both reported. A card can carry a
field no base resolves and a body link that lands nowhere, and reporting only the first
one found would understate D3's dead body links as 36 instead of 39. Measured on the live
corpus at the leaf's memory base: 5 field-dead declarations, 39 link-dead declarations,
44 findings, and **41 distinct cards** because 3 cards are broken in both
representations.

A card that declares the field but carries no `## Governing Overview` section — or a
section with no markdown link in it — is **observed, not failed**, and is returned in a
separate `observations` tuple carrying `CODE_SECTION_ABSENT`. It declares no body link,
so no link of its can fail to resolve. `ok` is `not findings`, so a pure-observation tree
is green; the leaf's independent control confirmed exactly that, and its negative arm
confirmed a single seeded dead link reds the check. Whether those cards *should* carry a
link is a doctrine question this module deliberately does not decide.

### Conventions

`SECTION_HEADING` is stored lowercased (`"## governing overview"`) and matched against
`line.strip().lower()`, so the heading is recognised in either case. `LINK_PATTERN` takes
the first markdown link in the section body and stops at the first `)` or whitespace, so a
title is optional and a link containing a fragment is parsed to its target alone:
`_target_exists` splits on `#` before probing.

The module is a **read-only** check. It resolves paths through
`kernel.filesystem.exists`, so the Windows long-path behaviour is the shared helper's
rather than a second implementation's, and it writes nothing.

`main` is a real entry point rather than a wrapper: it prints the five counters and one
row per finding, and exits **non-zero** while any declaration does not resolve. Before
this leaf no command in the product could fail on a dead governing overview, so the
guard is reachable outside pytest.

### Invariants And Boundaries

- Only a card that declares the field is graded; a card without it produces no finding
  and no observation.
- The two declarations are reported independently, never first-match-wins.
- The field is probed under three bases; the body link under one, card-relative.
- A section that is absent, and a section that carries no link, are observations with
  the same code; only a link that is present and dead is a finding.
- `ok` is derived from the findings tuple alone, so observations can never red the check.
- `_target_exists` strips a `#fragment` and refuses an empty target before probing.
- The walk covers every `*.md` under the root and skips non-files; `cardsWalked` is the
  population, `cardsFlagged` the cards with at least one finding **or** observation, so
  the two are not each other's complement.
- No writes, no network, no git subprocess.

## Evidence

### Repo-Internal References

- The section body is extracted between the card's own heading and the next `## ` heading, and its heading line is returned for the reader. [1]
- The field is probed under three bases — card directory, onboarding root, and the root's parent — because two conventions ship. [2]
- The per-card decision that reports both declarations independently and classifies no-section / no-link as observations. [3]
- The corpus walk and the five counters, with `ok` derived from findings alone. [4]
- The failable standalone runner: five counters, one row per finding, non-zero exit while any declaration is dead. [5]
- The metadata reader strips the value's backticks and skips the header and separator rows, which is why a declared target arrives unquoted. [6]
- Existence probes, including the Windows long-path prefix, are the shared helper's rather than a second implementation's. [7]
- The consumer: inside `_attach_curator_checklist` the findings are extended into the gated curator repair set, and the counts are published on the response as `governingOverviewResolution` for the curator's loop. [8]
- The falsifiable guard for this module's discrimination, with its green control in the same tree. [9]
