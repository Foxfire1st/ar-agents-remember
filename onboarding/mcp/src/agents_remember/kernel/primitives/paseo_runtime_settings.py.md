# mcp/src/agents_remember/kernel/primitives/paseo_runtime_settings.py

## Governing Overview

[Route overview](overview.md)

## Purpose

Defines strict optional authority for one install prefix, home, listen endpoint and exact native version.

## Code Commentary

A present block must carry exactly six fields; providers/embed may be empty but cannot be malformed. Parser rejects nonabsolute paths, malformed listen/ports and version ranges/tags/partials. Embed origins/URLs are canonicalized and validated by their own rules; absent block remains None and require_paseo_runtime names no runtime configured.

## Evidence

- Frozen implementation of parse_paseo_runtime_settings supporting the stated file behavior. [1]
- Frozen implementation of _exact_version supporting the stated file behavior. [2]
- Frozen implementation of _embed_entry supporting the stated file behavior. [3]
- Exercises absent, valid empty providers/embed, missing and unknown runtime fields and rejects malformed block shapes. [4]
- Runs all three commands without the block and checks named refusal, exit two and no process operation. [5]
- Checks a mismatched install is replaced and a failed staged installation preserves the preceding install and daemon. [6]
