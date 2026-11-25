# mcp/src/agents_remember/application/file_briefs/ordering.py

## Governing Overview

[Area overview](../overview.md)

## Purpose

Orders local rules and assigns weaknesses to their blocks.

## Code Commentary

More local realizations sort first, with the rule ID breaking ties. Bounded answers put moved rules first within this ordering. Explicit rule links govern weakness placement. With no such link, the first rule at the weakness’s symbol carries it and the others point to its ID.

## Evidence

- Weakness placement uses rule links and symbol matches, with a loose section for the remaining weaknesses. [1]
