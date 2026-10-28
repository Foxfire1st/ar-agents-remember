# mcp/src/agents_remember/application/review_memo_store.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

The review's blob-keyed memos, kept on disk between processes.

## Code Commentary

Memos are keyed by blob and stored on disk, so a second process answers from the same observation the first one measured instead of re-deriving it. A memo is only usable while the blob it was keyed on is the blob being asked about.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- _Stored is the on-disk shape a memo is kept in, keyed by blob. [1]
