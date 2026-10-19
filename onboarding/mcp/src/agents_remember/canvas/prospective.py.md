# mcp/src/agents_remember/canvas/prospective.py

## Governing Overview

[governing route overview](overview.md)

## Purpose

The model-free load of a prospective revision before its ready pointer moves. It stages the exact bytes, loads them once in the selected browser through the package-owned runner, and reports what was observed.

## Code Commentary

- `BrowserProspectiveLoad.load` refuses a path that leaves the staging directory, runs the child once, and treats an unreadable answer as an unavailable load rather than a pass.
- A `loaded` answer that names its own faults is downgraded, so a pass cannot contradict its own observations.
- `StaticProspectiveLoad` stands in a load's place and says so, which keeps the difference between a static check and a real load visible.

## Evidence

- The prospective revision is loaded once in the selected browser through the package-owned runner. [1]
- A success that contradicts its own observations is downgraded. [2]
