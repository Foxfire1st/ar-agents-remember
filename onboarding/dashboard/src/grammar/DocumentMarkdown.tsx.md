# dashboard/src/grammar/DocumentMarkdown.tsx

## Governing Overview

[overview](overview.md)

## Purpose

Supplies document-aware links, anchors and media to the shared Markdown renderer.

## Code Commentary

A relative file link remains non-opening text until resolution identifies an existing file. Missing paths remain labelled text. An anchor alone searches the current document container. Outside HTTP(S) links open separately. Media admission allows repository media paths and outside HTTPS; every parsed source-set candidate is admitted separately. A forbidden candidate does not discard its permitted neighbors.

Document images set a per-element no-referrer policy. The dashboard declares a page-wide no-referrer policy before the app loads, which also covers video sources, posters and nested sources.

## Relationships

DocumentContext supplies file resolution, opening and media-address construction. Notes can supply their own resolver and disable HTML. srcset parses candidates; documentMarkdown owns HTML cleaning and heading identifiers.

## Evidence

- Supplies document-aware links, anchors and media to the shared Markdown renderer. [1]

- The dashboard sets the page-wide no-referrer policy before loading the app. [2]
- Rendered images set their own no-referrer policy alongside media admission. [3]
- Videos and nested sources admit their media addresses and use the page policy. [4]
