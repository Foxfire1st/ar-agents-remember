# mcp/src/agents_remember/application/file_briefs/facts.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Assembles the memory facts for a source path.

## Code Commentary

BriefSource reads the knowledge index and measures anchors against the captured code tree. A local rule, open weakness, decision or standing document makes the path eligible. The assembled brief also carries the card purpose, families and retired-rule count.

## Evidence

- Assembly combines the four qualifying record classes and skips a path with none. [1]
