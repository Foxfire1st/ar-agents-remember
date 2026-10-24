# mcp/src/agents_remember/cli/role_launch_admission.py

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Settle a start's selection and request binding before any stage writes, and say whether an earlier attempt already owns the request.

## Code Commentary

`admit` reaches three decisions in one order. A document reference the role's parentless row does not admit is refused first: a Bootstrap seat takes no sprint, master or task document, so a reference it carries is an invalid call refused before a scaffold, an authority file or a host exists to undo. The task-document resolution itself stays where it was, before a seat is compiled, because a genuinely cold root has no documents to resolve yet. Then the request binding: a request id whose receipt carries it is an execution that already exists and is reconciled instead of prepared again, and a message-binding file of this same selection proves the request already prepared — the binding is written once, so a retry whose receipt never landed returns to the seat it prepared rather than preparing the root again. A binding file of another selection is refused by the same reason the later write-once check gives. Only a request with neither reaches the first-run stages, and the caller holds the dispatch lock around this so two starts cannot prepare one cold root side by side. `prepare_first_run_for` keeps the older requirement — a configured runtime — for every non-Bootstrap start, and a failed stage is raised as the start path's refusal carrying the stage and the effects before it. The route body stays a delegation call; the decisions live here.

## Evidence

- The three decisions and their order. [1]
- The parentless selection refused before any effect. [2]
- An invalid document reference and an archived request id are both refused before any effect. [3]
- A request with a binding but no receipt is not prepared again, and an existing receipt is reconciled without a second preparation. [4]
- Cold preparation runs under the dispatch lock. [5]
