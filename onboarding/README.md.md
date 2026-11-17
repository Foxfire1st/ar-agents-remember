# README.md

## Governing Overview

[overview](overview.md)

## Purpose

`README.md` is the repository's front page: the first file a developer who has never heard of Agents Remember reads. It presents the product in the order a reader decides: the banner as the page's title, one line that names what the product does, badges for the package version, the Python version and the licence, named links to getting started, the documentation site, the features tour, the roadmap and the releases, a short hook, and the explainer video as a still picture that opens it. The body shows the product in three pictures, states six capabilities, gives the five install steps, and closes with the documentation, the status and the stability promise, the roadmap and the contributing guide.

## Code Commentary

The file uses only what GitHub keeps in a README: Markdown, `align` and `width` attributes, tables, folded blocks and pictures. Its one top heading holds the banner with the alternative text `Agents Remember`; the claim, the row of badges and the still picture are centered. Each badge links to what it shows, and so does each named link. Every picture has an alternative text.

The five install steps stand under the heading `Install steps` and keep the number, order, titles and command lines of `docs/getting-started.md`. The section `Status` states the version of the package in this repository, `3.0.1`, which the release checklist names as the place of the version; the full stability promise is one folded block. Terms link to `docs/concepts.md` at their first use. Pictures and the video live under `docs/assets/`; no path under the removed top-level `assets/` folder remains.

## Boundaries

`scripts/check-public-docs.py` reads this file with the other public documents and judges its links, paths, reach, entry links, install steps and identifiers, not the truth of its prose. It requires the front page to link `docs/README.md`, `docs/getting-started.md`, `docs/install/README.md` and `ROADMAP.md`. A file under `docs/` that is no page counts as reached when this file shows or links it by a relative path; a page must still be reached from `docs/README.md`. The version sentence is the release checklist's place for the version.

## Evidence

- The head is centered and holds the banner as the one top heading, the claim, three badge links, five named links and the still picture that opens the video. [1]
- The body states six capabilities and shows the product in three pictures, each followed by one sentence about what is seen. [2]
- The five install steps keep the number, order, titles and command lines of the getting-started page. [3]
- The section Status states the repository's package version as `3.0.1` and sends the reader to the release notes before an install. [4]
- A file under docs/ that is no page is reached when the front page shows or links it by a relative path; a page stays out of this set. [5]
- The front page owes links to docs/README.md, getting-started.md, install/README.md and ROADMAP.md. [6]
