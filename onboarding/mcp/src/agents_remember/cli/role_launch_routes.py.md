# mcp/src/agents_remember/cli/role_launch_routes.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Registers role launcher options/dispatch/result/frame APIs and serializes preparation/retry/revive.

## Code Commentary

_start_execution reconciles matching receipt before recompiling and rejects reused request identity or another starter. _launch_prepared_role_session writes artifact and complete starting receipt before saved runtime call. Leaf Revive checks recorded/current task scope before any bridge operation. Register these APIs through the serving injection before static mount; no removed-host route alias is installed. The module also registers the one read-only report route beside them (`role_report.register_role_report_route`, MIK-R75 rule 4a).

## Evidence


- Frozen implementation of _start_execution supporting the stated file behavior. [2]
- Frozen implementation of _launch_prepared_role_session supporting the stated file behavior. [3]
- Frozen implementation of _revive_execution supporting the stated file behavior. [4]

- Interrupts between receipt and call and checks retry retains one agent identity. [6]

- Races publication and checks one persisted winner; competing request cannot issue another launch. [8]
- Checks path, bytes, digest, read-only mode, exact reuse and conflicting-content refusal. [9]
- Checks size limit and refuses links without changing their target. [10]
- Changed/missing saved scope refuses with both pairs, no bridge/write/enclosure creation. [11]

## MIK-R95 Progress And Document Reads

The route registration adds the one-request progress read (`/api/role-launch/progress/{request_id}`) and the document-chat record read (`register_document_chat_route`), and the dispatch endpoint claims the progress notice at the beginning and reclaims it in its finally path. The dispatch answer carries the enclosure preparation (`created`/`found`/`not-applicable`).

## Investigator scope and request identity

Investigator dispatch uses the existing selection admission lock; options expose per-request executions and omitted display rows for selected tasks. Result, retry and revive carry the exact saved UUID and canonical references through existing route owners. The one earlier spelling emits the shared notice; original receipt and report addresses remain readable without migration.


- The current source implements this file’s stated Investigator boundary. [12]


## Refreshed current evidence

- Frozen implementation of register_role_launch_routes supporting the stated file behavior. [1]
- The launch observer checks complete receipt, stable UUID and stored call before runtime launch. [5]
- Changes task/capsule/prompt inputs and verifies repeat returns or replays saved receipt without new preparation. [7]
