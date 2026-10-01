# dashboard/src/panels/session-cockpit/QueuePreview.tsx

## Governing Overview

[session-cockpit overview](overview.md)

## Purpose

Renders the compact FEUI-L5 queue projection beside the shared composer using only server-
authoritative queued submission rows.

## Code Commentary

### Logic

The component derives its rows from the per-session reliable-submit store, shows bounded operator-
useful identity/state, and exposes no control of its own. Pop-back remains the composer's Alt+Up
action against the authority route; this view never mutates queue order or removes optimistic rows.

### Invariants And Boundaries

- Only authoritative queued rows render; locally sending, ambiguous, dispatching, withdrawn, and
  settled records are not represented as queued work.
- The preview does not reveal backend raw evidence or another source's private text.
- Empty queue is a normal absent projection, not proof that no adapter operation is active.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository.

No configured live domain-documentation source was available.

### Repo-Internal References

- The shared composer mounts the preview and owns the Alt+Up action. [1]
- The lifecycle client hydrates only raw-free authoritative status rows. [2]

### Cross-Repo References

No meaningful cross-repo references found.

This is a repository-local cockpit projection.

## Current L5I Maintenance

The queue head can offer `steer` only when the active projection proves an interrupt capability and
a real working turn. Steering requests that exact-turn interrupt; it never withdraws, duplicates,
or locally reorders queued messages, so the server dispatches the same head after settlement.
