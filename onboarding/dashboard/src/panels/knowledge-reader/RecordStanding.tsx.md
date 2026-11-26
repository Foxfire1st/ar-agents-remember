# dashboard/src/panels/knowledge-reader/RecordStanding.tsx

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Formats the selected record revision's state and writer for knowledge-reader links and the sidebar.

## Code Commentary

The text uses the state when the summary supplies one and names the writer by role and model when available. Empty details produce no note. The note supplies the optional record state as a data attribute.

## Relationships

KnowledgeTree uses the same text for a wrapping detail below the record title. RecordLink displays the note beside its link.

## Evidence

- One formatter combines the supplied state and writer. [1]
- The inline note is absent when no detail is available. [2]
