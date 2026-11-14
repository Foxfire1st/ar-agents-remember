# dashboard/src/grammar/Media.tsx

## Governing Overview

[overview](overview.md)

## Purpose

Draws supported pictures and videos consistently in file, change-set, notes and knowledge-code viewers.

## Code Commentary

An oversize result returns a size notice before creating a media element. Pictures are lazy and request no referrer. Videos expose playback controls and metadata preload. The caption shows the media type and measured byte count when supplied.

## Relationships

The caller supplies the bytes URL and measured metadata. This component selects no Git revision and adds no bytes cache. Videos use the page's referrer policy rather than an unsupported element attribute.

## Evidence

- Draws supported pictures and videos consistently in file, change-set, notes and knowledge-code viewers. [1]
