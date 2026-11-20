# mcp/src/agents_remember/application/knowledge_writer/revision_stamps.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Owns revision-step and writer-stamp storage rules for knowledge writer placement.

## Evidence

- The comparison with the owner's base decides which revision the write owns. [1]
- An owned written revision gets the caller's stamp while a base-number placement preserves its base stamp. [2]
- The owner's writable history identifies the stored revision and its meaning. [3]
