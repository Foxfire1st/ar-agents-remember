# mcp/tests/test_knowledge_state_conversion.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Exercises state conversion on fixture copies, including planning, repeated application and recovery.

## Evidence

- The conversion preserves meaning and frozen history bytes. [1]
- Repeating the conversion leaves its output unchanged. [2]
- A report write failure leaves the fixture memory unchanged. [3]
