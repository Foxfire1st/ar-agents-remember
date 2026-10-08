# mcp/tests/eve_adapter_event_test_support.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Standing subscriber and adapter harness for the Eve conformance suite. The event stream is the real adapter's translation of the injected durable transport record.

## Code Commentary

`_Pump` owns one long-lived subscription task and collected-event positions. Its initial zero sleep is only a scheduler yield. Event, terminal-kind and settled-state waits use the shared hang guard. `_Harness` prepares actual control-operation references and submits through the adapter.

`read_completed_pass` records the runtime's stream-pass position and the adapter's current session/cursor, then waits for that exact durable-record pass to finish before returning newly collected events. An empty result therefore follows a positive read opportunity; it is not inferred from a short quiet window. Cleanup stops the subscriber before the adapter. `_clock` supplies request timestamps; the helper does not start a native Eve process or certify native execution.

## Evidence

No Domain Documentation source is configured; the references below establish repository-owned fixture and assertion behavior.

- One standing adapter subscriber collects translated events. [1]
- The harness uses a completed exact session/cursor record pass for absence evidence. [2]
- Adapter operations retain actual preflight references and close in subscriber-first order. [3]
