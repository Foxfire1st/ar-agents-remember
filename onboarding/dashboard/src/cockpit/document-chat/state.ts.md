# dashboard/src/cockpit/document-chat/state.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Bind the selected document to its admitted launcher roles, follow the host's agent answer and derive the retained chat panel's presentation.

## Code Commentary

The document scope keeps a launched request separate from a stale document completion. Bindings are memoized from the single native tasks array and served child tree. A successful dispatch retains its exact request until scope changes or its own fresh answer is empty. An explicit Investigator request refreshes the canonical Manager/Orchestrator primary chat rather than replacing it. [1] [2] [3] [5]

A review page whose task document is still pending or missing has an explicit unbound scope, distinct from the true documentless Projects Architect scope. It binds no roles, reads no chat and supplies no target. Pending task discovery retains the native screen out of reach under the supplied line; a known missing task hides the frame behind its named problem once the frame is available. Neither state offers a launcher.

Ordinary discovery uses preclick tree knowledge and prefers a fresh agent answer, otherwise a bounded previous answer. The exact just-started request is not replaced by the tree cache. Only an active pane with admitted roles reads its selected chat; the unbound review scope also disables known-chat discovery. Preload permits descriptor startup in a closed column but does not make those chat reads active.

For an ordinary document, known no-chat hides the retained frame; unknown agent knowledge keeps it visible and held, and unreadable answers do not become empty selections. Warmup observation is active-pane bound and uses the current hosted target. Per-agent state/reason takes precedence over the older pending/in-flight lists; unknown progress does not become a loaded agent. [4]

## Invariants And Boundaries

Canonical agent discovery and host-owned frame steering remain separate. The unbound worker-shaped placeholder supplies no admitted role and is never a substitute document or a Projects Architect binding. A frame descriptor being available is separate from a native shown-chat acknowledgement.

## Evidence

- The hook keeps document binding/request scope together and gates chat reads on active admitted roles. [1]
- A dispatch receipt is adopted only for the live scope with an exact agent and request ID. [2]
- The displayed agent follows the exact launched request or canonical document choice. [3]
- Ordinary unknown knowledge keeps the retained frame shown and held; known no-chat hides it. [4]
- An explicit Investigator launch refreshes rather than replacing the coordinator's primary chat. [5]
- An unbound review scope binds no role or chat target and is distinct from a documentless Projects Architect scope. [6]
- Pending unbound task discovery holds the retained screen; a known missing task hides it, with no launcher. [7]
- Preload starts the descriptor while hidden but does not activate chat reads. [8]

DocumentChatProps now accepts an optional ExplainerColumnTarget. This is a mode input for DocumentChat's composition owner, not another ordinary role binding: when it is supplied, that component disables this hook's active reads and delegates to the explainer column. Without it, the document's existing discovery, launcher and warmup behavior remains unchanged.

- DocumentChatProps now accepts an optional ExplainerColumnTarget. This is a mode input for DocumentChat's composition owner, not another ordinary role binding: when it is supplied, that component disables this hook's active reads and delegates to the explainer column. Without it, the document's existing discovery, launcher and warmup behavior remains unchanged. [9]
