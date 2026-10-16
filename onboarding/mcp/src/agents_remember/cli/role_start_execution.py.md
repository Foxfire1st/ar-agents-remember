# mcp/src/agents_remember/cli/role_start_execution.py

## Purpose

Prepare and reserve one exact role start before route receipt publication.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

start_execution enters the launch-only tolerate_unreadable_review scope, resolves canonical context/binding/digest, performs taskless migration and checks a same-request receipt before fresh preparation. Same-request replay is answered from frozen inputs, not recompilation against a changed task or capsule.

It refuses reused request IDs, carries an explicit reason to preparation, then asks step_up_request to infer an existing base holder only after host choice validation. It marks prepared stepUp, applies the route’s reservation/caller/occupancy guards and constructs _PreparedRoleStart for the existing native publication path.

The context-local fallback permits broken review evidence to be read diagnostically, preserves its raw bytes on incidental publication and does not relax other task facts or ordinary task/review readers. No extra review round, finding reset, settings write or second execution store is created.

## Evidence

- Exact replay precedes fresh preparation and validated successor reservation. [1]
- The diagnostic scope resets on exit. [2]
- Validated alternatives may infer a base holder without interrupt permission. [3]
- Canonical malformed review source test preserves task bytes and strict ordinary reads. [4]
