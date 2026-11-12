# mcp/src/agents_remember/application/review_comparison_records.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A comparison's native record inputs, read with exact consumed-byte observations.

## Code Commentary

Records are read as consumed bytes, so what a comparison was built from is measurable rather than inferred: the directory, each record's bytes and the latest record are all observed, and a record that cannot be read is named rather than skipped.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- comparison_records reads the record inputs with their observed bytes. [1]

- latest_record answers the newest record or names why there is none. [2]
