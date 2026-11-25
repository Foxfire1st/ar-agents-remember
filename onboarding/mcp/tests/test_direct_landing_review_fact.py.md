# mcp/tests/test_direct_landing_review_fact.py

## Governing Overview

[Governing overview](overview.md)

## Purpose

The forward direct landing case checks the committed ignore rule, the derived tree stamp and the brief's paired code revision. The test removes the stamp, then checks that the refused replay leaves it absent and keeps memory HEAD at the original output.


Exercises history closure and exact-tree memory review facts through converted direct landing.

## Evidence

- The matching pass is present in the committed closed history. [1]
- A pass for another tree does not attach a review fact. [2]


- The gate refuses an added fact in an already closed history. [3]
