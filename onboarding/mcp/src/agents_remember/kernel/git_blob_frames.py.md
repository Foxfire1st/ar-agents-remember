# mcp/src/agents_remember/kernel/git_blob_frames.py

## Governing Overview

[MCP overview](../../../overview.md)

## Purpose

Decodes exact Git blob bodies from binary batch output.

## Code Commentary

For each requested object, the decoder checks the object ID, blob type and decimal size, reads the body once and requires a newline delimiter. It checks cancellation between frames and refuses trailing bytes. When the stream end is known, the body reader can report the available byte count before allocating an incomplete payload.

## Relationships

The Git batch command reads these frames from its private spool. The review evidence reader shares the body reader for complete history blobs.

## Evidence

- The decoder validates requested frames and rejects trailing bytes. [1]
- The body reader can report short input before allocating it. [2]
