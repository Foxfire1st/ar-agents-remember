# mcp/src/agents_remember/cli/paseo_warmup_run.py

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Run one memory-gated, two-lane loading pass in tree order, promoting clicked pending agents without displacing already-running work. Unknown or below6GiB available memory waits and may give up with a truthful click-load reason. Individual failures do not stop the remaining list, and cancelled resumes drain.

## Code Commentary

Run one memory-gated, two-lane loading pass in tree order, promoting clicked pending agents without displacing already-running work. Unknown or below6GiB available memory waits and may give up with a truthful click-load reason. Individual failures do not stop the remaining list, and cancelled resumes drain.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence

- Run one memory-gated, two-lane loading pass in tree order, promoting clicked pending agents without displacing already-running work. Unknown or below6GiB available memory waits and may give up with a truthful click-load reason. Individual failures do not stop the remaining list, and cancelled resumes drain. [1]
