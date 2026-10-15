# dashboard/src/cockpit/document-chat/state.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

The document chat's state hook: it binds the selected document to the launcher's admitted selection, follows the host's agent answer and derives what the panel shows.

## Code Commentary

Warmup observation is active-pane bound and uses the current hosted target. Per-agent state/reason wins over older pending/inflight fallback lists; unknown progress does not become a loaded agent. Canonical chat discovery and host-owned frame steering retain their prior authority.


The serialized task reference scopes the exact launched request and guards against stale-document completion. `documentBindings` derives the canonical tree once and `bindingInTree` selects its role set. Successful dispatch retains the exact request until scope changes or its own fresh answer is empty; Investigator launch still refreshes rather than replacing a Manager/Orchestrator primary chat.

`useKnownChats` supplies preclick tree knowledge and `useSelectionAgents` prefers a fresh answer, otherwise the bounded prior answer. Exact just-started requests are not substituted by the tree cache. The presentation hides the retained frame only after the selection is known to have no effective chat (or admits no role), never merely because the server is still answering. Unknown selection keeps the native screen visible and held under the dashboard's waiting line; an unreadable answer is not promoted to no-chat.
## Evidence



## Investigator scope and request identity

An explicit Investigator launch/result targets the returned exact request while refreshing the primary coordinator’s canonical record. This callback never replaces default document agent discovery, and native frame steering retains its existing ready-channel behavior.




## Refreshed current evidence

- The hook keeps the canonical document scope, the bound selection and the launched request together and re-reads on revision.  Anchor: `useDocumentChat` [1]
- A dispatch receipt is adopted only for the live scope with an exact agent and request id. [2]
- The displayed agent is the launched request's agent or the newest live record, never a stale document's. [3]
- Only a known agentless selection hides the retained frame; unknown agent knowledge keeps it shown and held. [4]
- The current source implements this file’s stated Investigator boundary. [5]
