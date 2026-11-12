# mcp/src/agents_remember/serving/review_publication_watch.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

One connection's exact page and settled-environment invalidations across processes.

## Code Commentary

A connection is told about changes to the exact page and environment it is showing, across processes, and about nothing else: the watch is over those directories, so an unrelated change does not invalidate the page.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- PublicationInputs names the exact directories a connection is watching. [1]
