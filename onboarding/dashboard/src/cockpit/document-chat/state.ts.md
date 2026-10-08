# dashboard/src/cockpit/document-chat/state.ts

## Governing Overview

[Route overview](../overview.md)

## Purpose

The document chat's state hook: it binds the selected document to the launcher's admitted selection, follows the host's agent answer and derives what the panel shows.

## Code Commentary

The scope is the serialized task document reference, so every piece of state is keyed to one document. `documentChatBinding` supplies the role set and default selection; a successful dispatch is retained as the exact returned request id and is dropped when the selection changes or the record read returns no agent. `displayedAgent` prefers the exact launched request's agent and otherwise takes the newest non-archived matching record; a late completion for another document cannot steer this panel (`launchedRequest` checks the live scope). `chatPresentation` decides when the panel shows the launcher (no target, or the user opened it), hides the unresolved frame, and offers the one control that opens the same bound launcher.

## Evidence


- A dispatch receipt is adopted only for the live scope with an exact agent and request id. [2]
- The displayed agent is the launched request's agent or the newest live record, never a stale document's. [3]
- The presentation flags hide an unresolved frame and keep one control for the bound launcher. [4]

## Investigator scope and request identity

An explicit Investigator launch/result targets the returned exact request while refreshing the primary coordinator’s canonical record. This callback never replaces default document agent discovery, and native frame steering retains its existing ready-channel behavior.


- The current source implements this file’s stated Investigator boundary. [5]


## Refreshed current evidence

- The hook keeps the canonical document scope, the bound selection and the launched request together and re-reads on revision. [1]
