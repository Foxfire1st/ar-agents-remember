# mcp/tests/test_code_certification_execution.py

## Governing Overview

[Tests overview](overview.md)

## Purpose

Builds selected R21 code-certification execution requests from real published generations and the exact certificate-reuse plan. The helper retains only the complete original prefix before the selected suffix.

## Code Commentary

### Logic

`selected_execution` arranges the production-shaped fixture, publishes and records original certificates, derives `plan_certificate_reuse`, and constructs `CodeCertificationExecution` plus the clean-executor request.

### Invariants And Boundaries

- Original certificate and result-manifest identities remain immutable inputs.
- The selected suffix starts at the requested first changed gate; earlier complete generations are retained.
- Constructing this request is preparation evidence and does not itself execute a certifying gate.

### Todos

None recorded.

## Evidence

### Docs References

No configured Domain Documentation source applies.

- Selected execution preparation is local test evidence. [1]

### Repo-Internal References

- Selected execution derives exact suffix reuse from original certificates. [2]

### Cross-Repo References

None; this helper consumes local certification fixtures.
