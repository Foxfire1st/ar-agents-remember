# mcp/src/agents_remember/serving/projections/landing_cadence.py

## Governing Overview

[Projection readers overview](overview.md)

## Purpose

Keep transient landing-probe due times for the serving refresher, without turning a schedule into durable landing truth or launch authority.

## Code Commentary

`LandingProbeSchedule` owns one entry per currently eligible contract identity; each interested discovery calls `retain` to discard departed identities. A missing entry, unequal contract, time before the remembered changed epoch or expired due time is due. Contract equality is checked in addition to the external exact identity key.

`observed` serializes the ordered rows using only `kind`, `label`, `state`, `factState`, `detail` and the fact's own `at`. Observation timestamps and computed age are not a semantic change. Equal answers on equal contracts keep their changed epoch; a changed answer or clock before that epoch resets it. The next interval is 30 seconds below 120 seconds of unchanged age, 120 below 600, 600 below 3600 and 3600 thereafter.

## Invariants And Boundaries

The refresher applies this policy only when bound to actual Projector subscriber interest, and advances it after publishing actual rows. It does not schedule explicit unbound callers or bypass terminal eligibility/final validation. Due times are checked by ordinary sweeps, not exact timer execution or a publication-latency guarantee. No page means no new discovery; retention is refreshed when an interested discovery next occurs, not by a second cleanup loop.

## Evidence

- Current-identity retention, contract equality, clock regression and unchanged-answer age bands are the schedule's complete policy. [1]
- The refresher gates discovery/admission on actual bound interest and advances due state only for published rows. [2]
- Controlled-clock assertions cover every age band and a changed answer reset. [3]
- Rewrites, reopening, new identities, finishing and removal are checked at two populations. [4]
