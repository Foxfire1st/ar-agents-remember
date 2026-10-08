# dashboard/src/cockpit/document-chat/DocumentChat.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Focused tests for the document panel: the exact roles each selection admits, the bound launcher row, the frame steering, the unavailable-host notice and the launcher's return after an empty confirmed agent answer.

## Code Commentary

The suite stubs only the network boundary and drives the real component, hook, model and shared launcher. It asserts the unreadable-host notice is distinct from the no-agent launcher, that a start from the row steers the retained frame to the exact started agent (including a System Specialist with no Architect), that an open bound row is marked running and cannot start twice, that leaf and Projects selections offer their exactly admitted rows while unsupported selections name the missing relationship, and that the trusted host snapshot moves the frame by message when the selection changes (the suite always fetches the architect/worker fixtures and exposes the launcher by clicking "Launch role"; no archived transition is exercised).

## Evidence

- An unreadable host shows the shared Retry notice and no start, then recovers to the launcher. [1]
- A started Projects role steers the retained frame to its exact agent. [2]
- An open bound row is running and offers no second start. [3]
- Bound rows and unsupported selections follow the admitted role set. [4]
- The role table is asserted for Projects, sprint, commanded master and leaf. [5]
- The trusted host snapshot moves the retained frame by message when the selection changes, and the launcher is exposed by the manual "Launch role" click; no empty-agent or archived transition is exercised. [6]
