# mcp/tests/test_token_names.py

## Governing Overview

[Route overview](overview.md)

## Purpose

The tokenizer's name is declared twice — lightly beside the models and authoritatively in the counter — and the two declarations must remain one fact.

## Code Commentary

- The light declaration exists so a declaration owner can reach the name without loading the counter; this keeps the lighter copy from drifting into a second name.

## Evidence

- The case `test_the_light_name_is_the_counters_own_name` protects the light declaration staying the counter's own name. [1]
