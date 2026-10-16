# mcp/src/agents_remember/kernel/git_reference_files.py

## Governing Overview

[Area overview](../../../overview.md)

## Purpose

Read packed Git reference names and values without object interpretation.

## Code Commentary

An absent packed-refs file yields an empty mapping. Comment, peeled-object and empty lines are skipped; each remaining line must carry a value and nonempty reference name separated by a space or it raises OSError. Names and values are stripped and later duplicate names replace earlier ones. This is a small text reader, not object-ID validation, ref resolution or an atomic repository snapshot.

## Evidence

- Packed-reference parsing and explicit malformed-record failure. [1]
