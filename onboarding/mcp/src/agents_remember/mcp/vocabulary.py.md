# mcp/src/agents_remember/mcp/vocabulary.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

The words registration needs before any implementation exists: the sentinel a removed tool argument is defaulted to.

## Code Commentary

The removed-refresh sentinel lives outside the eager payload package; its public and old private names are the same string, preserving omission versus supplied-value refusal.

- A parameter default is evaluated when a tool is declared rather than when it is called, so the sentinel has to be importable without dragging an implementation package in behind it.
- It lives outside `agents_remember.mcp.tools` so a registration family declares its surface without loading every payload builder, which is what lets the import guard hold that package unloaded at discovery.
- Omitting the removed argument supplies the sentinel and keeps the admitted read path. Any explicitly supplied refresh value is distinguishable from omission and is refused by name; the sentinel does not restore that argument.
- The earlier private spelling is kept as an alias of the same object, so the two names cannot drift while call sites move over.

## Evidence

- A removed argument's default is one sentinel value [1]
- The earlier private spelling is the same object, so the two cannot drift [2]
- Only that sentinel is exported from this light module [3]

- The removed-refresh sentinel lives outside the eager payload package; its public and old private names are the same string, preserving omission versus supplied-value refusal. [4]
