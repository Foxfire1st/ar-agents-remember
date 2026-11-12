# mcp/src/agents_remember/memory/knowledge/dataset_identity_memo.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

Bounded identity reads over retained read-only SQLite handles.

## Code Commentary

Dataset identity is read through retained read-only handles, and the memo is bounded, so identity answers are neither re-opened per question nor kept until the process ends. A handle that cannot answer is not silently treated as an unchanged dataset.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- DatasetIdentityMemo serves identity from retained handles within its bound. [1]
