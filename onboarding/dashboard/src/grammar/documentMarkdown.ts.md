# dashboard/src/grammar/documentMarkdown.ts

## Governing Overview

[overview](overview.md)

## Purpose

Owns repository-document HTML cleaning, heading identifiers and local anchor lookup.

## Code Commentary

The repository-document pipeline parses raw HTML, applies the allowed-element sanitizer, removes document classes and adds heading identifiers. Raw identifiers retain sanitizer prefixing. With HTML disabled, no raw-HTML pipeline is installed. Anchor lookup compares identifier values inside the supplied container.

## Relationships

Markdown selects this pipeline for document mode. DocumentMarkdown supplies its links and media. Ordinary dashboard prose and notes with HTML disabled do not gain repository raw-HTML rendering.

## Evidence

- Owns repository-document HTML cleaning, heading identifiers and local anchor lookup. [1]
