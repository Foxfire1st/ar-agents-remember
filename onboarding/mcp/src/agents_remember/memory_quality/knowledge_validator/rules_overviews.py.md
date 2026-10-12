# mcp/src/agents_remember/memory_quality/knowledge_validator/rules_overviews.py

## Governing Overview

[memory quality overview](../overview.md)

## Purpose

Registers the three refusing overview-order checks: purpose first, no leaf/date sections, and one trailing citation region. It governs the root onboarding overview and every nested onboarding `overview.md`, not ordinary file cards.

## Code Commentary

`overview_headings()` parses actual ATX headings at levels one through six, accepts up to three leading spaces and strips legal closing hashes. Fenced blocks contain no headings. The first level-one heading is treated as the document title for the no-leaf/date-section check; purpose ordering and citation placement use level-two sections.

`check_purpose_first()` skips a leading Governing Overview section and accepts exactly What This Repo Is, What This Area Is or Purpose as the next level-two section. An absent purpose or any other first section produces a finding naming the overview and its heading where present.

`check_no_leaf_sections()` checks all non-title ATX headings for the leaf-series and date patterns. Nested or legally indented headings are not loopholes.

`check_citations_at_end()` uses the shared live-marker grammar. A marker before the last level-two section is reported. After that section's first citation line, `_region_offenders()` permits only live citation lines, blanks and fenced lines; every other line is reported with its number. Introductory prose before that first citation remains legal. An escaped bracket or code span is not a live marker and does not exempt narration inside the region.

## Invariants And Boundaries

The whitelist is mechanical: it does not infer whether prose is an explanation from list syntax, bracket-shaped text or a keyword. Marker examples belong to the section they explain; only fenced examples remain legal inside the citation region.

All three checks return without findings for standalone conversion or when `context.leaf_publication` is false. They remain registered refusing rules, not report-only warnings, but enforce overview order only at leaf-publication routes: closeout, direct landing and a leaf’s recorded landing supply the publication context. Baseline adoption/status, census and ordinary writer validation do not activate these order checks; scaffold overview stubs can be adopted and subsequently conformed by curation. This route boundary does not waive the order at publication.

The heading vocabulary determines syntax, not semantic accuracy: the Curator must still establish that purpose, structure and boundary prose is true against code.

## Evidence

- At leaf publication, the first level-two section after governing navigation uses one of the fixed purpose headings or refuses. [1]
- Actual ATX headings outside fenced code are parsed at every level. [2]
- At leaf publication, every non-title heading is checked for leaf/date names. [3]
- The trailing region has a mechanical whitelist with no prose-aboutness exception. [4]
- At leaf publication, the shared live-marker grammar drives placement findings and exact line reporting. [5]
- Conversion and non-publication callers do not activate the three R80 order checks. [6]
