# mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated | 2026-09-18T14:05:00+02:00 |
| lastVerifiedCommitHash | `7b1db4e0d73a321ee49df8725f5fe75846cf6c2b` |
| lastVerifiedCommitDate | 2026-09-18T13:43:14+02:00|
| governingOverview      | `../../../../overview.md`                  |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The section body is extracted between the card's own heading and the next `## ` heading, and its heading line is returned for the reader. | `_section_body` | mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py:93-106 |
| The field is probed under three bases — card directory, onboarding root, and the root's parent — because two conventions ship. | `_field_resolves` | mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py:116-118 |
| The per-card decision that reports both declarations independently and classifies no-section / no-link as observations. | `resolve_card` | mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py:121-201 |
| The corpus walk and the five counters, with `ok` derived from findings alone. | `check_governing_overview_resolution` | mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py:211-251 |
| The failable standalone runner: five counters, one row per finding, non-zero exit while any declaration is dead. | `main` | mcp/src/agents_remember/memory_quality/integrity/governing_overview_resolution.py:254-274 |
| The metadata reader strips the value's backticks and skips the header and separator rows, which is why a declared target arrives unquoted. | `table_metadata` | mcp/src/agents_remember/kernel/onboarding_doc.py:37-52 |
| Existence probes, including the Windows long-path prefix, are the shared helper's rather than a second implementation's. | `exists` | mcp/src/agents_remember/kernel/filesystem.py:28-29 |
| The consumer: the findings are extended into the gated curator repair set, and the counts are published on the response for the curator's loop. | `_attach_curator_checklist` | mcp/src/agents_remember/application/memory_quality/controller.py:425-470 |
| The falsifiable guard for this module's discrimination, with its green control in the same tree. | `test_every_dead_declaration_form_is_reported_and_no_clean_card_is` | mcp/tests/test_governing_overview_resolution.py:92-155 |

## Update History
- 2026-09-18T14:05:00+02:00 — 260915-KS-L13 owning seat: re-cited the consumer claim from the mechanically projected range :416-580 to the declaration's own extent :425-470, where `_attach_curator_checklist` is declared; the claim's wording is unchanged because the declaration supports it.
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.
- 2026-09-17T20:42:17+00:00: Generated citation repair: `_attach_curator_checklist` repointed to mcp/src/agents_remember/application/memory_quality/controller.py:416-580. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: created this card for the new module the leaf added, so the new source file has its 1-to-1 onboarding pair before closeout. Verified metadata is left at the leaf's frozen code base `621db8981aba09a6f17880d2138cf76a37332c6c`; the governed closeout stamps the real code commit, and no hash or fingerprint was invented here. Ranges in Repo-Internal References were read back at that revision and none is a projection from memory.
