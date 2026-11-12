# mcp/src/agents_remember/models/direct_execution_grant.py

## Governing Overview

[Nearest governing overview](overview.md)

## Purpose

Defines the closed public response vocabulary for the direct_execution_grant operation.

## Contract

DirectExecutionGrantResponse carries granted, revoked, reclaimed, unchanged or refused state, changed flag, optional grant, refusal status/detail and per-leaf reclaimed/preserved outcomes. The model validates answer shape; it neither grants authority nor reads or writes the store.

## Evidence

- Defines the closed public response vocabulary for the direct_execution_grant operation [1]
