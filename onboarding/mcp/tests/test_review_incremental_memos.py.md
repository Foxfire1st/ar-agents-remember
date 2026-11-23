# mcp/tests/test_review_incremental_memos.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for review incremental memos.py.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

The oversized grep case returns the full answer, then recomputes it for the next read. The persistence case compares restored grep entries with the live byte and entry policy.

A symbol answer is kept by blob, path and name across reads

## Evidence

- A symbol answer is kept by blob, path and name across reads, and the second read parses nothing [1]
