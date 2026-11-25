# mcp/src/agents_remember/models/knowledge_files/writer_stamp.py

## Governing Overview

[Governing overview](../overview.md)

## Purpose

Defines the persisted writer stamp of a knowledge record revision.

## Code Commentary

The stamp identifies its source, writer, timestamp and optional leaf, wave or crossing. It requires a reason for each unknown attribution value. A product or conversion source supplies an operation, while an agent stamp carries its launch attribution.

## Relationships

Current records and written history entries use this shape. The writer-key projection groups revision counts by role, harness and model.

## Evidence

- The model admits one optional history owner and validates operation and unknown-reason consistency. [1]
- The writer key groups the attribution by role, harness and model. [2]
