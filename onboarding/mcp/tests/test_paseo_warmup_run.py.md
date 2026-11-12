# mcp/tests/test_paseo_warmup_run.py

## Governing Overview

[governing overview](overview.md)

## Purpose

Unit assertions for the background warmup scheduler (MIK-R145), with injected resume and memory callbacks; this module observes no actual host start or host request.

## Code Commentary

The suite checks archived agents are left out; tree order is kept duplicates run once; at most two agents load at once; a clicked agent goes first; an injected resume callback is invoked once per admitted agent, without contacting a host; a failed agent is noted with the hosts words and the next follows. Tests assert only their named facets; they do not confer MEMORY, installation, lifecycle or broad performance acceptance.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence



- Unit assertions for the background warmup scheduler (MIK-R145), with injected resume and memory callbacks; this module observes no actual host start or host request. [1]
