# mcp/src/agents_remember/serving/projections/task_input_plan.py

## Governing Overview

[Route overview](../overview.md)

## Purpose

One task-reader input plan, shared by native registration and closeout invalidation.

## Code Commentary

Registration and closeout invalidation read through one plan, so both invalidate on the same task inputs instead of two lists that can drift.

## Boundaries

The detail this module owns stops at its own boundary; the route account above says what the surrounding surface promises.

## Evidence

- task_input_plan is the single input plan both paths use. [1]
