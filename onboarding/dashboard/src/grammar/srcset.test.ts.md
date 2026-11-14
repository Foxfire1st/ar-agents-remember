# dashboard/src/grammar/srcset.test.ts

## Governing Overview

[overview](overview.md)

## Purpose

Checks source-set token boundaries and descriptor validity.

## Code Commentary

The cases cover comma-bearing URLs, trailing separators, parentheses, ASCII whitespace, end-of-input states and accepted or rejected descriptor combinations. Rejected descriptors preserve following candidates after a parsed delimiter; unclosed parentheses consume the remaining input.

## Relationships

These parser assertions complement DocumentMarkdown's production media-admission tests. They do not independently prove browser requests or referrer policy.

## Evidence

- Checks source-set token boundaries and descriptor validity. [1]
