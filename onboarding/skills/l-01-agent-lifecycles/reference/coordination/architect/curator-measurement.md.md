# skills/l-01-agent-lifecycles/reference/coordination/architect/curator-measurement.md

## Governing Overview

[overview](../../../overview.md)

## Purpose

The Architect's rules for running or discussing a Curator measurement: an agreed observation and improvement loop, not a product or automatic acceptance gate.

## Code Commentary

Every measurement belongs to the Architect; the Worker implements tooling and agreed edits. The candidate and case-set identity arrive through the coordinating Manager, and the go returns on that route as a simple handover that starts no seat. Evaluations run when the Curator's text, model or role set changes and on the developer's request; no role text gains a per-leaf grader step, and the grader code stays in `scripts/agent_evals/` with ordinary tests. New-text trials use the candidate's own tool build, and every run binds head, change hash, build, text signature, case hashes, model, mode, judge and capture versions.

Results are reported as "all 3 right" and "at least 2 of 3" per case and fixed pair, separately per model. A case below 2 of 3 fails the loop; 2 of 3 is reported and discussed. The loop runs the full set, discusses failures with the developer, changes the text, repeats failing cases until none remain and ends with one full run, in which only a theme that is worse than in the old-text run reopens the loop. Unchanged text is re-run only to replace a trial spoiled by infrastructure, and no ruling record is kept per loop change. Infrastructure failures, missing captures and unanswered prompts make a trial unknown, which the Architect fixes and reruns; only a case that cannot run at all goes to the developer. Tokens are recorded per trial, attempt and run, with judge usage and unknown usage kept distinct; about 2.5 million tokens is a comparison guide, not a cap.

## Evidence

- Measurement ownership, triggers, tooling location and run binding. [1]
- Per-case and per-pair reporting, the failure threshold, the loop and the worse-theme reopening rule. [2]
- Unknown trials are fixed and rerun by the Architect, and token usage is recorded without a spending wait. [3]
- The loop is an observation process, not a product or automatic acceptance gate. [4]
