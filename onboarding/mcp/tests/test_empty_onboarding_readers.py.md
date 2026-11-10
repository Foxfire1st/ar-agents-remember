# mcp/tests/test_empty_onboarding_readers.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Distinguish an empty onboarding collection from an invalid onboarding path.

## Code Commentary

All three route-index builders refuse a file at the onboarding path with the same `NotADirectoryError` and truthful message. An absent collection yields zero routes, no build errors and checked zero-card drift without creating a directory. Baseline status accepts that state. The missing-onboarding CLI case selects no changed sources, so its source and missing-card counts are both zero; it does not imply that added sources never need cards.

## Evidence

- Each builder names a non-directory path as the refused case. [1]
- Absent onboarding is measured without creating it. [2]
- Baseline status reads an absent card collection as zero. [3]
- The CLI measures the empty changed-source selection instead of refusing the missing folder. [4]
