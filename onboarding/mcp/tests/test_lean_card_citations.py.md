# mcp/tests/test_lean_card_citations.py

## Governing Overview

[Overview](overview.md)

## Purpose

Exercise Lean citations in live cards and preserve the format 1 conversion contract.

## Code Commentary

The fixtures exercise mixed sources, extended names with bare Lean paths, and an extended name on a row without Lean. They check moved or changed citation state, uncertainty on an identical or changed blob, and a verified name beside an uncertain one.

## Relationships

Live card authoring calls `cells.parse_row` with its default `CitationReader.LIVE`. Legacy conversion selects `CitationReader.FORMAT_1` explicitly. The legacy fixture compares the digest of the converted output files for a card citing Lean with the historical format 1 digest.

## Evidence

- This test checks that candidate Lean scope uncertainty is reported even on an identical blob. [1]
