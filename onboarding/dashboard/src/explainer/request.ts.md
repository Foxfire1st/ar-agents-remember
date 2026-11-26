# dashboard/src/explainer/request.ts

## Governing Overview

[Route overview](../overview.md)

The module holds one pending ask. A new ask replaces that slot and notifies ask listeners. Clearing removes the slot only for the matching address, but always broadcasts the address supplied by the caller. A view closes its form when the event matches its address.

## Purpose

The one signal that asks the column to open its first-request form, carried from a ✦ Explain or a ⊕ pressed outside the column until the column is shown.

## Code Commentary

- The ask carries an address, any stale parts, stale grades and an optional message; it holds nothing to send and starts nothing.
- A pending ask is returned only for its own address.
- Ask, clear and their listener arrays carry the address across independently mounted views.
- The module remembers which targets belong to an archived explainer, keyed by address and bounded in number, so the tray can route a Send aimed at one back into the form.
- Registration refuses an address with any part missing, and a target whose seat is active is never reported as archived.

## Evidence

- A registered target keeps its agent ids and whether a seat is active, within a bounded map [1]
- A prefixed or registered target resolves to an archived explainer, and an active seat resolves to none [2]
- An ask is recorded and every listener is told at once [3]
- A pending ask is offered only to the address that made it [4]

- Clearing removes a matching pending slot and broadcasts the supplied address to all clear listeners. [5]

- A listener hears every new ask and unsubscribes by its returned function [6]
