# dashboard/src/grammar/markdownParseCache.ts

## Purpose

Reuse pure GFM parse data in bounded store resources.

## Code Commentary

remarkCachedParse wraps the configured native parser, keys preparation by text/parser version and structuredClones each cached tree before later plugins can mutate it. Missing parser refuses. No React nodes/handlers are cached.

## Governing Overview

[Area overview](overview.md)

## Evidence

- Implementation [1]
