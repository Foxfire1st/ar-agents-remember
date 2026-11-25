# mcp/src/agents_remember/application/tool_call_outcome.py

## Governing Overview

[Area overview](overview.md)

## Purpose

Normalizes refusal outcomes for the tool-call log.

## Code Commentary

A refused state or status becomes ok=false in the log. It uses the first available refusalCode, refusal or code string and supplies refused when all are absent. Other results retain their normal success and code.

## Evidence

- The outcome helper adapts refusal fields for logging without rewriting the tool result. [1]
