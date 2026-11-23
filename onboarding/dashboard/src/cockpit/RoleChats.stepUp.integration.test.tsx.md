# dashboard/src/cockpit/RoleChats.stepUp.integration.test.tsx

## Governing Overview

[Governing route overview](../overview.md)

## Purpose

Mounted RoleChatsPane step-up retry/storage recovery and honest post-step-up row disclosure.

## Code Commentary

Uses the real pane, sessionStorage initializer/decoder, dispatch/result folding and visible controls against mocked fetch. Architect and Investigator remount/404 retries preserve the exact request ID and trimmed reason; Investigator retains the legacy system-specialist storage key. Ordinary/legacy stored payloads do not acquire step-up. Nonempty strings alone decode as reasons. The cross-harness receipt case marks base mode, notes and speed as non-applied previews and hides editable feature controls. A separate case supplies an observed top-level mode that differs from the request and checks its display. A receipt without an observation shows “Mode/features unreported”.

## Evidence Boundaries

- The declared UI cases assert the exact persisted/replayed payload through actual mounted controls, not injected retry state.
- The cross-harness source case asserts one launcher container, observed model text, base/non-applied titles and no mode or permission-feature override in dispatch.
- Fetch replies and the receipt are local fixtures, not a live backend, native actor or paid model turn.
- DOM presence/one container does not establish pixel layout, all viewport widths, actual applied mode/features or permission behavior.

This card describes assertion/support/document source, not a test invocation, independent verdict or publication.

## Evidence

- Source assertion: replays %s step-up after storage reload and a real 404 result fold. The declaration is not an execution receipt. [1]
- Source assertion: retains ordinary and legacy %s storage without inventing step-up. The declaration is not an execution receipt. [2]
- Source assertion: retries an ordinary saved %s request through the pane without step-up. The declaration is not an execution receipt. [3]
- Source assertion: decodes only a nonempty string step-up reason (%j). The declaration is not an execution receipt. [4]

- The mounted test presents base options beside the reported step-up state without showing the base values as applied. [5]

- A top-level observed mode wins over the requested value in the displayed receipt, with a separate unreported case. [6]
