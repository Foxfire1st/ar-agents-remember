# Native retirement proofs

[Tests route overview](overview.md)

## Contract

Fake-host operation and MCP-entry tests exercise scope-authorized retirement across every canonical role (Architect, Orchestrator, Manager, Worker, Reviewer, Curator, Investigator, Bootstrap, plus legacy `system-specialist` normalization), Manager and Orchestrator topology scope (including retiring a seat started by another Manager or Architect, and after a master is attached to a sprint), scope refusals naming caller scope and recorded selection, open-child refusal naming every open child and succeeding after they retire, `interrupt_turn` for active turns and running provider subagents on both leaf and non-leaf seats, unresolved-launch refusals (`starting`/`unknown`), unknown IDs, duplicate current and current-plus-history ambiguity, and unauthorized repeats. A successful retirement records caller/reason/time, archives without a child turn, settles waiting held messages, and makes both ID- and role-addressed messages refuse archived delivery.

Confirmed host archive refusal clears `retireIntent` so future host-archive attribution remains intact; uncertain archive transport preserves `retireIntent` for identical retry; and the record-write fault test (`role_receipt_files._replace_receipt_bytes`) distinguishes a host already archived from a receipt not yet naming retirement and proves an identical authorized retry converges. The tests do not establish restoration of the removed hosted-seat path or a live-host journey.

The message-attachment case places another-schema JSON beside launch receipts and asserts that authorized retirement still retires and archives its Worker. This is a fake-host source assertion, not a real-host run.

## Evidence

- Scope-authorized callers retire seats across all roles without a child turn and record retirement provenance. [1]

- Current plus historical receipt duplication refuses through the entry point without effects. [2]

- A failed final receipt write reports the split with `retireIntent` and an identical retry converges. [3]
