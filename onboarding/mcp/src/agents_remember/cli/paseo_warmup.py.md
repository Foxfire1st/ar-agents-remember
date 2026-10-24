# mcp/src/agents_remember/cli/paseo_warmup.py

## Governing Overview

[governing overview](../../../overview.md)

## Purpose

Intake the configured host's real process start and eligible tree agents once through the shared OS claim; expose progress through the existing role-launch read route. Unknown process identity does not consume a start. Unreadable daemon-home or task-root intake retries while the give-up window is open; when that failure reaches the configured window, it consumes that exact start and records a `given-up` outcome with its reason. Claim-publication, candidate-read and initial-progress failures use separate retry/release paths and are not subject to this branch's give-up check. The transport performs only a timeline resume, not a message, refresh, interruption or unarchive.

## Code Commentary

Warmup removes all explainer_seat_ids derived from environments after collecting ordinary role ids; a host restart does not load those seats.

Warmup retains each selected agent’s receipt projection (including report path) in `WarmupRun.role_receipts`. Before its one `agent-resume` command, `resume_agent` republishes that receipt’s role identity through `role_activity`; the saved context is supplied by the serving loading driver. Shared OS start-claim, bounded request reads, no-message transport and the intake-specific retry/give-up distinctions remain as stated above. Role-facts publication is best effort and not a plugin acknowledgement.

## Boundaries

Local implementation and executable evidence do not replace requirement authority or the owning transaction. Retained source semantics and explicit unavailable/failure states remain binding.

## Evidence


- Intake the configured host's real process start and eligible tree agents once through the shared OS claim; expose progress through the existing role-launch read route. Unknown process identity does not consume a start. Unreadable daemon-home or task-root intake retries while the give-up window is open; when that failure reaches the configured window, it consumes that exact start and records a `given-up` outcome with its reason. Claim-publication, candidate-read and initial-progress failures use separate retry/release paths and are not subject to this branch's give-up check. The transport performs only a timeline resume, not a message, refresh, interruption or unarchive. [1]

- Warmup removes all explainer_seat_ids derived from environments after collecting ordinary role ids; a host restart does not load those seats. [2]
