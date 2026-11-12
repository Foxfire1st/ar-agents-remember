# mcp/tests/test_curator_card_layouts.py

## Governing Overview

[overview](overview.md)

## Purpose

Proves that the Curator's shipped layout templates (file card, repository overview, route overview and entity catalog), once filled, pass the real citation writer, the leaf publication gate and the catalog readers. These are commit-gate tests on disposable Git repositories, not a running role, closeout or landing.

## Code Commentary

`_filled` strips a template's leading comment, replaces every placeholder and refuses any placeholder left over. `_world` commits a code repository holding the real `memory_quality/legacy_cards.py` scanner as `src/pkg/legacy_cards.py`, plus a memory repository with the validator fixture family and the three filled documents and entity catalog left uncommitted. `_fix` runs the converted `citation_fix` over those documents, and `_publish` writes the memory tree and requires `GitKnowledgeValidation().leaf_refusal` to admit it before committing.

- **Authoring and publication.** A dry run authors one reference per document without changing a byte; the real run creates each sidecar with reference `1` and the `- <finding> [1]` line, leaves a markerless overview alone, leaves no old-format card, and the pair publishes.
- **Overview gate.** An overview whose citation stands before a later section, whose prose follows the final citation, or whose first section is not its purpose section (`What This Repo Is` / `What This Area Is`) is refused with only `R80.7-citations-at-end` or `R80.1-purpose-first` findings on that document, and the restored text publishes.
- **Named batch.** When one overview's sidecar does not parse and another holds two tables with no blank line between them, the fixer refuses those two by name, leaves their bytes untouched, authors the valid file card, and that card pair publishes alone.
- **Entity catalog.** The filled catalog has one supported inventory/fingerprint pair whose evidence is the scanner path. Orphaned, missing or duplicated fingerprints and missing section headings are refused by the alignment check and the census reader; a duplicated inventory heading is refused only by the exact census reader; an unsupported algorithm or evidence path absent from the code candidate is a fingerprint-plan problem.
- **Old format.** The filled card carries no old-format mark until a metadata-table row or an `## Update History` heading is appended.

## Evidence

- Templates are filled with every placeholder replaced and none left. [1]
- The world commits the real scanner as code evidence and writes the filled documents into memory. [2]
- Publication requires the leaf knowledge gate to admit the written memory tree. [3]
- Filled layouts author real references, create sidecars and publish. [4]
- Bad citation order in an overview is refused as citations-at-end. [5]
- A named batch refuses two bad cards, keeps their bytes, and the valid pair publishes. [6]
- The filled catalog has one supported inventory and fingerprint pair. [7]
- Misaligned inventory and fingerprint sections are refused. [8]
- An overview whose first section is not its purpose is refused. [9]
- Old-format marks appear only after the negative mutation. [10]
- A duplicated inventory heading is refused by the exact census reader. [11]
- An unsupported algorithm or absent evidence path is a fingerprint-plan problem. [12]
