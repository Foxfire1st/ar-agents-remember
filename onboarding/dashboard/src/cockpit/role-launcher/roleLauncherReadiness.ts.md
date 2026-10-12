# dashboard/src/cockpit/role-launcher/roleLauncherReadiness.ts

## Governing Overview

[Route overview](../../overview.md)

## Purpose

Derive normalized selection and Start, Retry and Result readiness facts.

## Code Commentary

Live occupant, ready/complete/busy state, request policy and exact retry scope determine the offered action facts. Per-request starts exclude starting/unknown receipts; singleton and Projects bound Starts still pass the caller’s final bound guard.

## Boundaries

Pure predicates do not mutate selection or admit backend work. Retry scope matching is distinct from the UI busy/loading guards.

## Evidence

- resolveLaunchReadiness is a current owner of the behavior described above. [1]
- startAllowed is a current owner of the behavior described above. [2]
