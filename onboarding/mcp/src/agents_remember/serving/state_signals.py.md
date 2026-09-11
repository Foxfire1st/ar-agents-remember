# mcp/src/agents_remember/serving/state_signals.py

| Field                  | Value                                                     |
| ---------------------- | --------------------------------------------------------- |
| repository             | agents-remember                                           |
| path                   | `mcp/src/agents_remember/serving/state_signals.py`        |
| doc_type               | `file-level-onboarding`                                   |
| lastUpdated | 2026-09-10T11:42+02:00 |
| lastVerifiedCommitHash | `8a46bc8d186d9444bf9a83b21ad4683ec4937e3d`|
| lastVerifiedCommitDate | 2026-09-11T11:04:29+02:00|
| governingOverview      | `overview.md`                                             |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Derives terminal-outcome, compound-idle, non-reaction, and boundary-drain findings from catalog
truth using real task-document containment for manager ownership. The boundary-drain gate decides
whether a pending inbox row has a new delivery opportunity at its target's current turn boundary.

## Code Commentary

### Logic

`compound_idle_sets` groups a manager with running leaf-role occupants whose documents are direct
children of that manager's master. State-signal and non-reaction evaluation resolve the current
manager structurally through the shared incumbent/staged-heir selector. Compound-idle groups include only the current manager generation. Their candidate documents are
projected from the same running-manager snapshot consumed by the canonical selector, so each
non-ambiguous document necessarily has a primary or staged-replacement claimant; no synthetic
missing-occupant fallback is part of that path. Observer sweeps suppress a finding for an ambiguous
occupant rather than choosing a generation; a finding for an ambiguous or
malformed task-document route is suppressed the same way, without aborting unrelated seats.
`TaskDocumentRefError` is therefore a per-subject fence at state-signal finding evaluation;
action-time owner derivation remains a separate revalidation boundary. Inbox delivery/landing
remains owned by the shared durable message path.

`evaluate_boundary_drain_findings` is the boundary-delivery gate for a pending inbox row. It asks
`_boundary_follows_last_attempt(entry, boundary_at)` whether the target's current turn boundary is a
new delivery opportunity. A row carrying no attempt clock is a drain candidate only when
`messageKind == "state-signal"`: rebinding a held signal to a replacement occupant resets that clock
(`attemptCount=0`, `lastAttemptAt=None`), the generic redelivery path then suppresses the row through
`state_signal_held_on_boundary`, and this boundary gate is its only remaining delivery path. Every
other no-attempt row keeps the ordinary redelivery path and is still refused here. A parseable
attempt clock still requires `boundary_at > attempted_at`; an unparseable clock is refused.

Reviewer subjects are polymorphic: leaf and master reviewers route to their manager, while sprint
reviewers route to the architect or orchestrator stamped on that generation. The non-reaction
notifier expands only this reviewer family; it preserves its historical worker/curator subordinate
scope and does not silently treat every sprint role as a notifier subject. Unstamped historical
reviewers retain only the deterministic old leaf-manager meaning while those rows drain; master and
sprint reviewer notifications require the generation's explicit parent stamp.

### Conventions

Task hierarchy determines ownership; runtime ids only correlate observed episodes.

### Invariants And Boundaries

- Spawn ancestry does not establish manager/subordinate membership.
- A subordinate lookup with no current manager fails closed; an ambiguous canonical manager seat is
  locally suppressed.
- A missing or ambiguous task-document parent raises a typed refusal that suppresses only that
  subject; later sweeps can retry after topology recovers.
- Compound-idle manager documents come from the same immutable running snapshot used for selection,
  which guarantees a claimant after ambiguity is excluded.
- Findings arise from terminal/turn evidence, not model artifact judgment.
- State-signal delivery still obeys the target turn boundary.
- Boundary-drain eligibility for a pending row with no attempt clock is state-signal-scoped; every
  other row kind keeps the ordinary redelivery path, and an unparseable attempt clock never drains.
- A pending row whose target has no classified turn boundary is not drained by this gate; the row
  stays durable and pending, so that is a delay and not row loss.
- Ambiguity is local to the affected canonical seat; observers neither guess nor fail the whole
  sweep.
- Reviewer notification follows the generation's structural parent, while non-reviewer expansion
  remains bounded to the notifier's historical subordinate classes.

### Todos

None.

## Docs References

No Domain Documentation source is configured.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Compound-idle membership follows direct task containment and one current manager generation. | `compound_idle_sets` | mcp/src/agents_remember/serving/state_signals.py:160-174 |
| Terminal outcome findings resolve manager ownership structurally and suppress only ambiguous or malformed subjects. | `evaluate_state_signal_findings`; `_safe_state_signal_finding` | mcp/src/agents_remember/serving/state_signals.py:199-218 |
| A held state-signal row is suppressed from the generic redelivery path while its resolved target is running. | `state_signal_held_on_boundary` | mcp/src/agents_remember/serving/state_signals.py:188-196 |
| Non-reaction evaluation uses topology, current-generation identity, and durable landed rows. | `evaluate_non_reaction_findings` | mcp/src/agents_remember/serving/state_signals.py:286-305 |
| Non-reaction subject expansion adds all reviewer altitudes without widening unrelated role scope. | `_notifier_subject_owner_id` | mcp/src/agents_remember/serving/state_signals.py:397-414 |
| Boundary drain admits a pending row whose target turn boundary follows its last recorded attempt. | `_boundary_follows_last_attempt` | mcp/src/agents_remember/serving/state_signals.py:440-456 |
| Boundary-drain eligibility for a no-attempt row is state-signal-scoped; the sweep reuses the same durable pending row. | `evaluate_boundary_drain_findings` | mcp/src/agents_remember/serving/state_signals.py:459-498 |

## Cross-Repo References

No cross-repository implementation dependency governs this file.

## Update History

- 2026-09-10T11:42+02:00 — 260831-LOCR-L09 curator: recorded the boundary-drain predicate `_boundary_follows_last_attempt` and its call from `evaluate_boundary_drain_findings` — a pending row with no attempt clock is drainable only for `messageKind == "state-signal"` (the set whose clock an occupant rebind resets and whose push the boundary gate owns), while every other kind and every unparseable clock keep the previous refusal. Also repaired a duplicated garbled sentence in the Logic section and re-derived the construct ranges. Verification metadata remains closeout-owned.

- 2026-09-08T14:22:32+02:00 — 260831-LOCR-L08 curator: recorded the typed task-document refusal fence in state-signal evaluation, preserving local suppression and later retry while leaving canonical seat selection and delivery ownership unchanged.

- 2026-08-31T04:59+02:00 — Tightened notifier ownership to the same bounded migration rule as
  structural routing: unstamped leaf reviewers retain their historical manager; higher reviewers
  require explicit parent provenance. Verification remains closeout-owned.

- 2026-08-31T04:50+02:00 — 260821-ARSPAWN-L5 independent-review repair: documented
  plane-stamped reviewer routing across leaf/master/sprint altitudes and the deliberately narrow
  notifier expansion. Verification remains closeout-owned.

- 2026-08-26T17:57+02:00 — Removed the unreachable compound-idle missing-occupant fallback. Manager
  documents and occupants are selected from one running snapshot, so the only non-current case is
  ambiguity, which remains locally suppressed. This records the invariant instead of forcing an
  impossible mocked state solely for branch coverage.

- 2026-08-25T23:19+02:00 — Contract-wide citation curation: re-read the current anchored claim(s), retained the supported wording, and cleared verification metadata for closeout-owned restamping.

- 2026-08-25T22:27+02:00 — No content impact: final ARSPAWN-L2 review confirmed ambiguous seats
  are contained locally across state-signal, non-reaction, compound-idle, and boundary-drain
  evaluation. Verification remains closeout-owned.

- 2026-08-25T19:51+02:00 — 260821-ARSPAWN-L2: state-signal and non-reaction evaluation consume the
  shared canonical seat selector, exclude stale manager generations, and skip only the ambiguous
  seat during observer sweeps. Verification remains closeout-owned.

- 2026-08-11T19:58+02:00 — Aligned the current serving card for `state_signals.py` with seat ownership, delivery, lifecycle, and terminal boundaries represented by this source.
- 2026-08-10T10:35+02:00 — 260731-EFA-L9 curator repair: refreshed this staged card from the current onboarding body and re-resolved moved/deleted citations; verification metadata remains pinned until L9 closeout.\n
- 2026-08-10T04:39+02:00 — 260713-TES-L6: documented structural all-subordinate membership,
  shared relay evaluation, action-time revalidation, and timezone-aware non-reaction evidence.
  Verification metadata remains pinned until closeout stamps the code commit.

- 2026-08-09T12:08+02:00 — 260713-TES-L5 curator: recorded the ladder-vocabulary removal in
  `state_signal_held_on_boundary` (boundary-held rows wait for the next boundary; no ladder
  climb exists). Verification metadata pinned until closeout stamps the 260713-TES-L5 commit.
- 2026-08-09T06:48+02:00 — 260713-TES-L4 curator: updated the landing vocabulary to the formal
  `state="landed"` (non-reaction scan now filters on the terminal state; the by-rule pending
  predicate is gone), and recorded the dead-seat skip in `evaluate_boundary_drain_findings`
  (N2/N14 — rebind machinery owns dead-target rows). Verification metadata pinned until
  closeout stamps the 260713-TES-L4 commit.
- 2026-08-09T03:51+02:00 — 260713-TES-L3 curator: added the compound-idle predicate family
  (`_compound_worker_index`, `compound_idle_sets`, `compound_idle_signature`,
  `evaluate_compound_idle_findings`, `compound_idle_response`,
  `COMPOUND_IDLE_SWEEP_LATENCY_SECONDS=10.0`), master-scoped membership on every arm,
  zero-worker no-signal, action-time-signature semantics, and widened the non-reaction
  predicate from worker-only to worker+manager scope. Verification metadata pinned until
  closeout stamps the 260713-TES-L3 commit.
- 2026-08-09T01:21+02:00 — 260713-TES-L2 curator: created this sidecar for the new
  state-signal predicate module (NON_REACTION_WINDOW_SECONDS=300, three finding families,
  held-on-boundary exclusion, self-contained payloads, R1/F7 accepted notes). Verification
  metadata pinned to the leaf base `1c1629fc` until closeout stamps the 260713-TES-L2 commit.
