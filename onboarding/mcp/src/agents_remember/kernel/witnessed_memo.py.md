# mcp/src/agents_remember/kernel/witnessed_memo.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A bounded memo of answers read from files, each kept with the file identity it was read under.

## Code Commentary

A memoised answer is kept beside the identity of the file it was read from, so it is reused only while that file is the one being asked about. A changed file invalidates its answer rather than being served from the older read.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- WitnessedMemo keys an answer by the file identity it was read under. [1]
