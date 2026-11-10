# mcp/tests/test_l84_link_integrity.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that every link, anchor and `skill://` URI in the delivered `l-01-agent-lifecycles` skill resolves, in both the canonical `skills/` tree and its packaged copy, and that each kind of broken link is caught. Every `#` section link of every delivered skill, in both trees, must also name an existing section.

## Code Commentary

`_scan` walks every Markdown file of one tree through `_Tree`, which can overlay replaced, added or removed files, and `_check` resolves each target with `_resolve`: relative and same-file `(#anchor)` links, `<...>` angle-bracket targets, `{{detail:...}}` links and every `skill://` URI, in a link or in prose. A `skill://` URI must use the served origin (`SHIPPED_SKILL_ORIGIN`) and resolves inside the tree being scanned, so a package link resolves in the package. A target must exist inside the delivered skills tree, and an anchor must be a GitHub-style heading slug (`gfm_anchor`, with `-1`, `-2` suffixes for repeated headings) of a Markdown target; headings inside code fences are not anchors. Web links are not followed, and the fill-in placeholders of the repository-overview, route-overview and file-card templates are exempt only in their own template.

- Both trees scan with no problem.
- Each planted mutant adds a problem over the source baseline: a broken same-file, relative or detail anchor or path, broken angle-bracket targets, a template placeholder outside its template, a collapsed-hyphen anchor, a heading inside a code fence, an unserved `skill://` origin, a missing `skill://` target or anchor, and a link leaving the skills tree. A correct double-hyphen anchor passes, and removing a packaged file breaks the package's own `skill://` link to it.
- The acceptance core file does not link back to its own approval definition in `core/every-role.md`.
- `_fragment_problems` checks every link with a `#` fragment in one skill through the same `_check`. In both the source and the package tree, no skill that holds a `SKILL.md`, including `c-13-install-and-onboard`, `c-14-knowledge-bootstrap` and `l-01-agent-lifecycles`, has a broken section link.
- Pointing the `c-14-knowledge-bootstrap` `admission-of-new-records` link or the `c-13-install-and-onboard` `history-rows` link back from `templates/curator-handoff-ingestion.md` to `templates/curator-handoff-list.md` is reported as a missing anchor.

## Evidence

- Link targets resolve as detail, served skill URI or relative paths, and other schemes are refused. [1]
- A target must stay inside the delivered skills tree, exist, and hold the anchor. [2]
- Every delivered link and anchor resolves in the source and the package. [3]
- The GitHub anchor keeps one hyphen per space. [4]
- The planted link mutants are enumerated by kind. [5]
- Every mutant fails, the GitHub-form anchor passes, and package skill URIs resolve in the package. [6]
- The acceptance file does not point at its own approval definition. [7]
- Every fragment link in one skill is checked for its file and section. [8]
- Every skill's section links resolve in the source and the package. [9]
- Re-pointing the c-13 or c-14 handoff section link at `curator-handoff-list.md` fails as a missing anchor. [10]
