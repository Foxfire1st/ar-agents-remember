# mcp/tests/l114_e4_river_scale.py

## Governing Overview

[mcp/tests route overview](overview.md)

## Purpose

The retained E4 scale probe for the Event River (MIK-R114 evidence item 4): live-stream
continuity while the river takes size cuts at load. A probe script, not a test module —
it generates the two-load river and retains the capture the unit surface cannot show.

## Code Commentary

The script drives writers against the workspace river at both required loads while a live
stream reads, so continuity holds across the size cuts the per-append admission makes.
Its retained stdout/capture artifact is the E4 evidence the completion dossiers cite.

## Evidence

- The scale probe drives both loads with live-stream capture. [1]
