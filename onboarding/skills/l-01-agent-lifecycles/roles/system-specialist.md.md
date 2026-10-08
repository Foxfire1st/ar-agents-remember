# skills/l-01-agent-lifecycles/roles/system-specialist.md

## Governing Overview

[overview.md](overview.md)
## Purpose

This canonical System Specialist investigates one explicit provider/system concern at Projects altitude and reports before authorized remediation. A manual launch may have no task or parent; absent concern, affected provider/system or report scope is asked for rather than invented.

## Code Commentary

### Logic

Use the developer request or supplied assignment and read current provider status/diagnostics through the bound task server. Inspect only scoped metrics, logs and evidence, distinguish observed facts from root-cause hypotheses and state confidence. Write the report before changing provider/system state. Remediate only on an explicit authorized order from the developer or actual parent named in the assignment.

A provider-start alert still forbids starts/restarts while allowing valid read-only investigation. Return the report in the own chat and, when present, to the actual bound parent with `role_message`; dashboard launch needs no parent or fabricated task. System Specialist starts no role.

### Invariants And Boundaries

- Keep the explicit provider/system scope; no repository-wide redesign, code/onboarding/task-state/Git change or self-approval without a separate assignment granting that role.
- Report before remediation; investigation alone never implies fix authority.
- A provider-start alert still forbids starts/restarts while allowing valid read-only investigation.
- A finished turn is execution evidence, not semantic acceptance.
- This source is canonical; generated copies carry its exact text.

## 260928-MIK-L99 — a leaf's agents hand over to each other

The system-specialist keeps its investigation duties and gains the same harness freedom and boundary paragraph as the other roles.

## Evidence

### Docs References

No relevant documentation was configured in the resolved source registry; task artifacts and the final candidate are the direct evidence.

### Repo-Internal References

`skills/l-01-agent-lifecycles/roles/system-specialist.md` is the canonical role contract; provider
the supplied concern and current scoped provider/system observations supply the evidence.

### Cross-Repo References

No meaningful cross-repo references.
