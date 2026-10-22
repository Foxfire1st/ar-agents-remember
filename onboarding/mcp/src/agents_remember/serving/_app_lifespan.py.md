# mcp/src/agents_remember/serving/_app_lifespan.py

## Governing Overview

[Serving overview](overview.md)

## Purpose

Own the serving lifetime, its retained background loops and drained shutdown. Terminal catalog observation, notifier sweeps and their health payload readers are absent; one leaf-archive recovery cadence remains.

## Code Commentary

Startup compacts the workspace river before projector prime, then starts projection, provider metrics, leaf-archive recovery, held-message delivery and river-compaction tasks. Heap tracing and malloc trimming are separately opt-in. The archive loop awaits one tick through the drained thread boundary, sleeps after each completed attempt and closes its archive owner in finally; it introduces no second recovery timer. Shutdown first invokes the review-tree child shutdown hook, then cancels and awaits every background task. A cancelled shielded worker is awaited before cancellation is re-raised, so serving cannot return while that worker still writes. Provider sampling/recording/degradation/compaction use the same drained boundary. Source inspection does not supply new teardown execution.

The serving lifetime retains the L81 shared background ledger and server-side host-start loading watch. Archive recovery, provider metrics, held-message work and each native resume are attributed to their executing worker units. The loading driver uses shared OS lease/progress, records completion or cancellation, and drains before its claim closes. Removed terminal observation and notifier sweeps are not reintroduced by that loading watch. The measured warmup resume receives `run.role_receipts[agent_id]`, so receipt identity is republished before native resume. This reuses the existing loading driver and offload/drain accounting; it is not the host-activity intake and adds no host polling timer.


**L184 — NEW-LIMIT-FROM-REPORT-ONLY, NEW-R192-RULE19-PORT.** The lifespan owns the refresher's lifetime, so no reaper of its own is needed. The lifespan consumes the collaborator it was given instead of reaching into cli, which is the edge the finding was about. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Held-message delivery tick

`_held_delivery_loop` runs with serving under the shared background ledger and calls `_held_delivery_tick` every `HELD_TURN_END_TICK_SECONDS` (three). Each tick reads the host's activity publication through `turn_ended_agents` and hands the agents whose turn ended to `deliver_ended_turns`, which drains only the receipts a holder named. Every `HELD_DELIVERY_SWEEP_SECONDS` (fifteen) the same tick also runs `sweep_held_messages` as the fallback for receipts no holder named. A failed tick is logged and retried on the next interval; the store keeps everything that still waits, and each tick is one accounted worker unit.

## Periodic Provider Safety Boundary

The provider loop remains periodic: sample labelled containers, record, evaluate degradation with the existing stop callback, compact, then sleep at the configured sample interval. Every stage uses the accounted cancellation-drained offload. A launch-authority map is not a fleet-retirement witness: empty, revoked or malformed authority and a dashboard restart do not prove leftover labelled stacks are gone. Neither page interest nor authority decoding gates this safety sequence. Launch refusal, sampler label discovery, degradation policy and Docker handling keep their own owners. This is the retained landed loop, not an accepted fleet-absence optimization; controlled real-loop regression tests are not a claim that a real fleet was launched.

## Evidence boundary

This is current-source interpretation of the A9 candidate, not a new test result, CODE grade or MEMORY acceptance. The retained supporting references below are reauthored through the ordinary fixer; unsupported removed constructs are withdrawn, not rebound to arbitrary neighboring code.

## Source-bound reference inputs

- [11]
- [16]
- [20]
- [22]
- [24]
- [25]
- [26]

- Periodic safety samples, records, evaluates with its existing stop callback and compacts through accounted drained offload, with no page/authority gate. [27]
- Controlled real-loop tests cover revoked, between-tick, restarted and malformed authority while keeping launch refusal separate. [28]
