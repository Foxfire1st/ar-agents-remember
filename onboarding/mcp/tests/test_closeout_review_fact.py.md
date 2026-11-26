# mcp/tests/test_closeout_review_fact.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

Checks the pairing, preparation order and restoration of the memory review fact at closeout.

## Evidence

- The fact carries the exact reviewed memory tree and its verdict. [1]
- The review fact already exists when derived-file renewal runs. [2]
- A renewal failure restores the preceding history bytes. [3]
