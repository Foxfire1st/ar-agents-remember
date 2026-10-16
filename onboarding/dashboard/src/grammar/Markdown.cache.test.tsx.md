# dashboard/src/grammar/Markdown.cache.test.tsx

## Governing Overview

[Route overview](overview.md)

## Purpose

Pin retained Markdown parsing without stale transforms or callbacks.

## Tested Boundary

Real Markdown mounts share parsed preparation across navigation. Marker/heading transforms stay isolated, and requirement clicks call only the returned page callback. Stubbed fetch and DOM assertions do not prove browser layout or native execution.

## Evidence

- Parse identity and transform isolation [1]
- Current callback [2]
