# mcp/src/agents_remember/cli/role_step_up.py

## Purpose

Select one user-owned role alternative from typed review facts without mutating a seat.

## Governing Overview

[MCP package overview](../../../overview.md)

## Current Contract

Only completed failing code review rounds count for Worker; only completed failing memory review rounds count for Curator. Record-only checks of the unchanged candidate do not add a try; no legacy mixed-code row is reinterpreted as a Curator round. The optional user alternative defaults to afterTries=3 for these roles, not to extra review authority.

select_step_up uses an explicit one-sentence reason, a prior selected step-up or a reached configured threshold. A reason requires a configured alternative; absent settings keep the role’s own choices, warning when a prior selection no longer has configuration. Reasons are trimmed, single-line, nonblank and at most 1000 characters.

Selecting a step-up supplies the alternative row's launch defaults. The row's effective harness is its named harness or the role's harness when the row omits one. The row supplies its own mode on that harness, with no inheritance of the base mode even when the harness and model stay the same. Once a step-up is selected, final resolution gives an explicit launcher mode priority over the applicable alternative mode, whether selection came from a request, the review threshold or a retained prior step-up. The dashboard's Step up button sends document scope and the reason without an agent override. If neither applies, it uses the host-advertised default only when the selected harness's modes are known and the host advertises a default. Otherwise the start sends no mode field. Cross-provider or cross-model selection clears omitted model, effort, tier, features and notes. Same-scope selection can inherit those fields. Every selected alternative clears the base host role profile. An explicitly native service_tier feature suppresses the inherited tier alias. Origins remain tied to authored alternative keys.

stepUpSelection records source, tries, reason, role and sanitized predecessor note metadata. label_step_up_choices labels authored settings choices while preserving start-call/host-default provenance; step_up_note displays the model and step-up source from the supplied receipt. Host validation, actual predecessor rebinding and durable task publication belong to callers.

A prior selection is retained while an alternative remains configured, not an immutable lock on obsolete settings. Selection alone does not archive a busy seat, grant another round, replace the Reviewer or reset remaining findings.

## Evidence


- Threshold, manual and prior selection carry scoped choices and sanitized provenance. [1]

- The manual reason has an explicit bounded single-sentence shape. [2]
- Only settings-origin selections are relabeled. [3]
- Failed counts use role-specific typed lanes, not total record operations. [4]
- Incomplete typed history yields unknown, not an invented zero/count. [5]
- Test source keeps record-only checks and the memory sequence independent. [6]


- The alternative row supplies defaults on its effective harness without inheriting the original mode. Final resolution takes an explicit launcher mode first and omits mode when no applicable named mode or known advertised default exists. The Step up button sends scope and reason without agent override. [7]
