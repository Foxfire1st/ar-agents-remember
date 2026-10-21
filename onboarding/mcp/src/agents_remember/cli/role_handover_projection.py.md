# mcp/src/agents_remember/cli/role_handover_projection.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Defines the hand-over projection a first message carries — which fields, in what order, and what the rest of the object is left to — and measures it, so the field list and its budget have one home.

## Code Commentary

PROJECTION_FIELDS is the single definition of the projected fields; tests derive from it and never repeat it, so a field added to a projection is added here and every check sees it. project_handover drops a field the object does not carry or carries as null, projects the bound task document alone out of the documents list, and keeps only the workspace, reader, host and seat parts the role needs before its first tool call. FILE_ONLY_FIELDS and FILE_ONLY_NESTED name what the message leaves to the hand-over file, so a check can say which part a message must reach through the file rather than the projection. projection_text renders the compact JSON exactly as the message carries it, first_read_paragraph carries the sentences said nowhere else and names the file, and projection_tokens counts with the vendored vocabulary. The module writes nothing: it publishes no hand-over file and keeps no state, and its one reach outward is the token count's own vocabulary lookup, which reads the packaged vocabulary through its cache and is the resource check a count always needs — not a write and not part of the projection's transformation.

## Evidence

- The projected fields are defined once, in the order the message states them. [1]
- The projection keeps permitted fields, drops absent and null ones, and names the complete file. [2]
- The first-read paragraph carries the sentences said nowhere else and names the file. [3]
- The projection is counted with the vendored vocabulary as it stands in the message. [4]
