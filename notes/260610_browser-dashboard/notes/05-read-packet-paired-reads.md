# 05 — Read Packet: Paired Source+Onboarding Reads As Observable Events

| Field | Value |
| --- | --- |
| Topic | Issue #46 (`read_source_packet`) and its role in dashboard observability |
| Status | Design-relevant now, implementable later (developer: "arguably this can be designed and implemented later") |
| Sources | Issue #46 body, developer notes 2026-06-10 |

## What #46 Already Specifies (recap)

A repository-scoped, read-only MCP tool (working name `read_source_packet`):
batch reads of repo-relative source paths; each file returns source (full or
range) **plus its deterministic file-level onboarding body automatically** when a
sidecar exists; per-file `onboarding` field only for deviations (sections,
suppress, include history); explicit per-lookup status
(`found | missing | disabled | unsupported | not_requested`); route-index
semantics preserved (inside `sourceScope` but absent from `coveredFiles` ⇒
report missing, don't probe); a separate front-door option for root/route
overviews; Pydantic-registered response with token metadata. Open in-issue
questions: final name, overview-tool-vs-option, batch/budget caps for v1.

## Why It Belongs In The Dashboard Discussion

Developer framing: this "wasn't a loose idea." It brings several interests under
one roof:

1. **Structured paired reads** — the Intent phase's source+onboarding workflow
   becomes one call instead of N ad-hoc reads. Better ergonomics, fewer tokens,
   and the onboarding actually gets read alongside the code (its design purpose).
2. **Observability** — today, file reads happen through harness-native tools and
   are invisible. Routed through the MCP, each read becomes an attributable
   event: *this lifecycle read these files with their onboardings at this time*.
3. **Lifecycle attribution** — reads are attributed via the ambient lifecycle
   (server-side auto-tagging, note 01); the request envelope needs no
   lifecycle param, so reads stop looking random by construction. The observer
   branch even had `read.session.*` / `read pairs` event families and a
   dashboard view for "onboarding usage" — same instinct, pre-MCP vintage.
4. **Token accounting** — packet responses are token-stamped like everything
   else, so "context spend per lifecycle" (the fuel gauge) gets its biggest
   missing contributor.

## Dashboard Projections This Unlocks

- Per-lifecycle read trail: which files (+ ranges) were read, with or without
  onboarding present — a live "what is the agent looking at" panel.
- Onboarding *usage* metrics (which sidecars actually get consumed vs merely
  maintained) — feedback into memory curation priorities.
- Missing-sidecar heatmap from real demand (`missing` statuses) instead of
  coverage-only counts (route indexes, note 03 surface 10).

## Sequencing Position

- The tool can ship after the lifecycle/event groundwork — but its **request and
  response envelope should be designed in the same pass as note 01/02 schemas**,
  so ambient lifecycle attribution and event emission are native, not
  retrofitted.
- Adoption risk to design around: the model must *prefer* this tool over
  harness-native reads during Intent work in managed repos, which is a skills/
  doctrine change (c-04 / l-01 teach it), not just a tool launch.

## Open Questions

- Does the dashboard need read *content* or only read *facts*? (Lean: facts +
  paths + statuses; never mirror file contents into the event log.)
- Range semantics for "what did the agent actually see" (full-file vs lines) —
  enough to be honest, small enough to store.
- Should harness-native reads in managed repos be discouraged by doctrine once
  this exists, or coexist quietly? (Affects how complete the read trail is.)
