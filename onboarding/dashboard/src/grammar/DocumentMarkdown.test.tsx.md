# dashboard/src/grammar/DocumentMarkdown.test.tsx

## Governing Overview

[overview](overview.md)

## Purpose

Checks document HTML isolation, navigation and media admission through the production Markdown component.

## Code Commentary

The cases assert allowed HTML, removal of executable or styling attributes, prefixed identifiers, ordinary Markdown's HTML exclusion, confined file links, local anchors and outside navigation. Media cases cover image, video, poster and nested-source addresses plus candidate-by-candidate source-set admission.

## Relationships

The test file supplies executable facets for document rendering. Browser-observed referrer behavior for elements without their own policy has separate request-header evidence.

## Evidence

- Checks document HTML isolation, navigation and media admission through the production Markdown component. [1]
