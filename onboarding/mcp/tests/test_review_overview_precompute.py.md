# mcp/tests/test_review_overview_precompute.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

A test suite for review overview precompute.py.md: it drives the behaviour the commentary states and asserts it.

## Code Commentary

A turn end hands its capture to the leaf-wide build and a page open reuses that build. The supersession case changes either the code tree or only the recorded memory-base commit and checks that the latest capture wins.

## Boundaries

A same-tree capture can supersede an in-flight build when its recorded memory-base commit changes.

## Evidence

- A turn end hands its capture to the leaf-wide build and a page open does not build it again [1]
