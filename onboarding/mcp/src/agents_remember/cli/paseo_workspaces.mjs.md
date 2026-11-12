# mcp/src/agents_remember/cli/paseo_workspaces.mjs

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Open a workspace for explicit canonical master/task placement while preserving archived generations and retry identity; retain the separate folder-only opening path.

## Code Commentary

The initial key remains `ar-task-workspace:v2:` plus SHA-256 of JSON `[masterKey, taskKey]`. Only an archived, archiving or completed replay absent from the live listing advances to a successor: hash JSON `[previousKey, predecessorWorkspaceId]` with the same prefix. Retries derive the same chain, relying on the host's idempotent creation ledger rather than a local history store. Eight successor steps permit nine create/refresh attempts; a ninth archived descriptor refuses with the task key and count, without another create.

Capture the completed replay with `current()` before refresh can clear it. A null refresh may use that replay only when preparation was `found`, solely as successor identity. Missing fresh creation is unavailable, never a live handle. Every descriptor must have an ID, the master's project ID and the task's resolved directory before continuation or workspace-title mutation. Only a refreshed, nonarchiving, nonarchived workspace is titled and returned. `preparation` describes that final create call's initial snapshot, not an earlier archived generation.

## Boundaries

Master project add/rename happens before workspace validation and is not rolled back by a placement refusal. No archived workspace is unarchived, renamed or deleted, and no actor is moved. Host retention and the reason an earlier workspace was archived remain outside this owner. A payload with neither masterProject nor task uses the existing folder open and reports `opened`; partial task placement refuses instead of falling back. A successful open is neither an agent's completed first turn nor task/landing acceptance.

## Evidence

- The original and successor keys share a deterministic SHA-256 construction. [1]
- The traversal bounds retries, validates placement and titles only the refreshed live workspace; a hidden completed replay supplies successor identity only. [2]
- Folder-only opening and explicit validated task placement retain the public reply envelope. [3]
