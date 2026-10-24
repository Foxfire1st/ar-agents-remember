# mcp/tests/test_role_step_up.py

## Governing Overview

[Tests route overview](overview.md)

## Purpose

Covers the single step-up a task seat gets: what the user's settings admit, when a launch chooses a
step-up rather than a fresh role, and what stays intact when the seat's predecessor, its review evidence
or its receipt is missing. Settings are checked for exact keys and provenance, and a step-up that the
host refuses leaves the holder and the user's permission authority as they were.

## Code Commentary

### Logic

`write_role()` writes a role file into a settings tree reached through `_user_settings_guard`, so the
settings cases read the same file a real launch would. `launch_world()` builds the launch fixture from
`paseo_launch_test_support` and wires the command surface (`role_step_up`, `paseo_catalog`,
`paseo_role_tools`, the task documents and the review history).

- **Settings.** A user step-up accepts its own choices and defaults to three selections; an invalid one
  names the file and the exact key.
- **Counting.** A failed try is a review-kind round rather than a record check; a step-up selection uses
  its own choices and never steps down; the count selects a step-up at and above its threshold.
- **Provenance.** A step-up's provenance uses the actual predecessor's choices, and a catalog that does
  not offer the chosen tier or model is reported as an unoffered choice rather than silently replaced.
- **Seat handling.** A manual start replaces an idle holder and keeps the step-up across a restart; a
  step-up refuses an active turn or a pending permission without archiving the seat; a failed creation
  leaves an empty seat and the same request retries; a host refusal keeps the holder and the user's
  permission authority.
- **Degraded review.** An unreadable review launches the base role with a warning, or preserves an
  explicit or prior step-up, and the fallback keeps the raw evidence and the other validation.
- **Recorded rounds.** A recorded round names the step-up without granting a round; a third failed round
  changes the harness with its own mode and keeps the reviewer.
- **Replay.** A step-up replay reconciles the decision before the host and survives receipt loss; a host
  default successor model is observed without losing the requested provenance; an incomplete historical
  count warns without inventing tries.
- **No repository supply.** A repository cannot supply a step-up at all.

### Conventions

Cases build a settings tree and a launch world per case, and assert on the recorded decision, the seat's
state and the settings file rather than on internal call order.

### Invariants And Boundaries

- A step-up only ever steps the seat up; it never steps a seat down or invents a try.
- A step-up refused before replacement leaves the holder in place and the settings file unedited; a creation
  failure after the old holder is retired leaves an empty seat that the same request retries.

## Evidence

- A user step-up accepts its own choices and defaults to three. [1]
- An invalid step-up names the file and the exact key. [2]
- A failed try is a review-kind round, not a record check. [3]
- A step-up selection uses its own choices and never steps down. [4]
- The count selects a step-up at and above its threshold. [5]
- A step-up's provenance follows the catalog and reports an unoffered choice. [6]
- A manual start replaces an idle holder and keeps the step-up across a restart. [7]
- Provenance uses the actual predecessor's choices. [8]
- A step-up refuses an active turn or permission without archiving. [9]
- A recorded round names the step-up without granting a round. [10]
- A failed creation leaves an empty seat and the same request retries. [11]
- A host refusal keeps the holder and the user's permission authority. [12]
- A third failed round changes the harness with its own mode and keeps the reviewer. [13]
- An unreadable review launches the base role with a warning. [14]
- An unreadable review preserves an explicit or prior step-up. [15]
- The launch-review fallback keeps the raw evidence and the other validation. [16]
- A step-up replay reconciles the decision before the host and survives receipt loss. [17]
- A host default successor model is observed without losing the requested provenance. [18]
- An incomplete historical count warns without inventing tries. [19]
- A repository cannot supply a step-up. [20]
