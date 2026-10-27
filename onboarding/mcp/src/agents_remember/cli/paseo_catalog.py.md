# mcp/src/agents_remember/cli/paseo_catalog.py

## Governing Overview

[Route overview](../../../overview.md)

## Purpose

Owns launcher catalog discovery, host role-profile reads, source-precedence selection resolution and launch choice provenance.

## Code Commentary

The settings role defaults carry origins/sources, host role and useHostDefaultMode through resolve_agent_selection; this is normal catalog-qualified launch resolution rather than a second explainer-specific model catalog.

Each operation asks Paseo afresh. A view asks for the full catalog; a start asks metadata and then the selected model’s features. A ContextVar shares these answers only within the current operation. The durable store is scoped by install prefix, home, listen and version and supplies only unanswered parts from their last successful answer. `resolve_agent_selection` resolves each choice by source precedence — explicit start call, host role profile, our settings, host default — while keeping lower choices bound to their authored provider/model: an incompatible lower value is omitted with its source and reason rather than reinterpreted. `read_host_role` reads the running host's profiles through a read-only bridge call; the first exact role-name match wins and an unreadable catalog falls back to role settings with the reason recorded. Mode is never a start-call argument. Ordinary resolution uses host profile, then applicable settings, then the explicit least offered working mode. A selected cross-provider/model step-up with no authored mode instead requests the host defaultModeId; concrete defaults must be offered when the mode list is known. If neither fresh nor saved mode data answers, the configured mode passes through unchecked; a known list still refuses an unoffered value. Features resolve per offered host metadata: `service_tier` and `fast_mode` are speed choices a start call may state, while permission-bearing and unknown-bearing values are refused and belong in user settings or the host profile. `serviceTier` stays independent of effort, is revalidated for model overrides, matches offered IDs before labels without case, and is never replaced with a different offered choice. There is no local fast-to-priority alias. `launcher_options` publishes resolved values with per-choice sources, and empty feature maps stay out of old request digests.


**L184 — NEW-R192-EXTRA-ARGS.** This is where the launch record is assembled from the plan, so a plan the start did not build leaves the field out of the record. The obligation this leaf records for this place is stated in the invariant named here; the card's earlier account of this file stands, and this paragraph adds what the change made true.

## Current Contract — Scoped Launch And Settings Changes

launcher_options exposes each role’s configured stepUp alternative. resolve_agent_selection validates the selected provider/model/effort, mode and offered features where a fresh or saved answer exists before creation; unanswered parts pass their configured values through unchecked, then labels selected user-authored alternative values with the step-up source while leaving host defaults and explicit start-call provenance distinct.

Ordinary no-mode launches keep the existing least offered working mode policy. When mode data is known, a cross-provider/model step-up without its own mode passes useHostDefaultMode and takes that host’s defaultModeId instead; any non-null result must match that known offering. If neither a fresh nor a saved mode answer exists, the configured mode passes through unchecked. This is not an unconditional least-mode guarantee and does not transfer another harness’s mode/features or authorize permission-bearing start arguments.

Runtime identity, explicit provider refresh, host-profile discovery, per-choice provider/model binding and omitted lower-choice disclosure remain with this owner. The host’s IDs and labels govern spelling normalization; disk persistence belongs to paseo_catalog_store.

## Evidence

- Options include the configured alternative. [6]


- Host catalog validation and step-up provenance share the existing resolver. [7]


- The host-default-mode path remains conditional; concrete modes are checked when mode data is known, while unknown mode data passes the configured value through. [8]

- Test source contrasts ordinary auto with step-up host default. [9]


- Frozen implementation of launcher_catalog supporting the stated file behavior. [1]


- Frozen implementation of resolve_agent_selection supporting the stated file behavior. [2]



- Frozen implementation of _selection_refusal supporting the stated file behavior. [3]



- Checks that every view and start asks fresh and explicit refresh rescans provider discovery. [4]



- Checks rejected choices create no receipt, workspace, agent or enclosure. [5]


- The settings role defaults carry origins/sources, host role and useHostDefaultMode through resolve_agent_selection; this is normal catalog-qualified launch resolution rather than a second explainer-specific model catalog. [10]
