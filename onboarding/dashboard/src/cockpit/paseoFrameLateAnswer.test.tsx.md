# dashboard/src/cockpit/paseoFrameLateAnswer.test.tsx

## Governing Overview

[Route overview](../overview.md)

## Purpose

Protects late-answer versus application-silence recovery and the negotiated native-screen/waiting boundary.

## Code Commentary

The real frame/controller tests distinguish a slow open that answers pings from an unanswered application ping. Missing ready first asks a ping; late ready/pong releases a held selection by message, while silence permits recovery once for that load. A selection made after recovery waits for that new load's own ready/ping cycle rather than immediately reloading again. Current-plugin on-chat releases selected-screen input before shown removes the waiting line; load-failed removes the line and leaves native Retry in reach. Capability cases keep legacy message switches and their early-answer notice distinct from an explicitly non-open plugin's URL navigation.

## Invariants And Boundaries

Timer/channel fixtures establish executable component contracts, not a developer-dashboard walk, host-log reading, or native send attribution. The plugin-side native-display fixture remains a separate evidence owner.

## Evidence

- The suite contrasts responsive late answers with true ping silence and checks each loaded document's own readiness wait, input release, native failure and legacy capability notices. [1]
