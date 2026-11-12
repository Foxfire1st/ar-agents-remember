# scripts/check-public-docs.py

## Governing Overview

[overview](../overview.md)

## Purpose

`scripts/check-public-docs.py` is the offline check that keeps the public documents true after the documentation leaf lands. It reads the documents a user reads — `README.md`, `ROADMAP.md`, `CONTRIBUTING.md`, `SECURITY.md`, `CODE_OF_CONDUCT.md`, `mcp/README.md` and every `.md` and `.txt` file under `docs/` — compares them with the files Git tracks, fetches nothing, and prints one finding per line as `file:line: kind: target`. A file Git does not track is neither read nor judged. It exits non-zero when it finds anything.

## Code Commentary

`load_tree` lists the tree through `git ls-files --cached`, so only tracked files are read and an ignored build product or an untracked draft is not judged; `document_of` parses headings, links and markers from each document, and `steps_of` reads the install steps. `anchors_of` computes the anchors a page's headings offer in the renderer's form.

The checks are separate generators over one `Index`: `link_findings` reports a relative link, or an absolute link to this repository, whose path is not in the tree (`broken-link`) and an anchor that is no heading of its target (`missing-anchor`); `path_findings` reports a named repository path that does not exist (`missing-path`), skipping paths Git ignores and paths under `mcp/src/agents_remember/` or `skills/`, which the instruction consistency test owns; `reach_findings` reports a file under `docs/` that no link from `docs/README.md` reaches directly or through one index page (`unreached`); `entry_link_findings` reports an entry point that lacks a link it owes, a front page without the roadmap link, or a package description that links by a relative path (`entry-link`); `step_findings` compares the install steps of every entry point with `docs/getting-started.md` in number, order, titles and commands (`install-steps`); and `identifier_findings` reports an identifier of a task, a leaf, a packet or a direction, and also a name of that shape that the product itself shows — a rule code such as `R22.3-unresolved-target`, or the sandbox names `ar-pnt` and `pnt-sandbox` (`identifier`).

A line that names a missing path or an identifier on purpose carries `<!-- docs-check: path: <reason> -->` or `<!-- docs-check: identifier: <reason> -->`. `markers_of` reads a marker, `_next_block` covers the next line or the fenced block it opens, and `apply_markers` removes the findings a marker allows and adds a `marker` finding when the marker has no reason, an unknown kind, or nothing to allow. A marker alone on its line covers the next line.

The check runs with no argument on the current checkout; `main` also accepts `--root`. `check(tree)` returns every finding in document order.

## Boundaries

The check judges the documents' links, paths, reach, entry links, install steps and identifiers, not the truth of their prose. It is the enforcement half of MIK-R97 rule 7; the route overview explains the documentation surface it reads. The check is executed by `mcp/tests/test_public_docs_check.py`, which also proves each finding kind by a mutation of the checkout's own documents.

## Evidence

- The module docstring names the public documents, the nine finding kinds, the product-shown names and the marker form. [1]
- The tree comes from Git and holds only the files Git tracks; an untracked file is not read. [2]
- Link findings name a broken path or a missing anchor. [3]
- Path findings skip ignored paths and the instruction consistency test's paths. [4]
- Reach findings require a link from the docs index through one index page. [5]
- Install-step findings compare the install steps of each entry point with the getting-started page. [6]
- Identifiers of tasks, leaves, packets and directions, and product-shown rule and sandbox names, are findings on every page. [7]
- Markers allow their next line or fenced block and are themselves findings when malformed. [8]
- The check returns the findings and the command prints them and fails. [9]
