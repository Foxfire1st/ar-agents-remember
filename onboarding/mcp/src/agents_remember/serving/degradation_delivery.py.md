# mcp/src/agents_remember/serving/degradation_delivery.py

## Governing Overview

[serving overview](overview.md)

## Purpose

`serving/degradation_delivery.py` (260731-EFA-L9) is the serving-backed implementation of the
provider degradation alert port, added when the providers→serving layering violation was removed:
providers may not import serving, so serving provides this delivery implementation behind a port.

## Code Commentary

### Logic

`DegradationAlertDelivery` (cit:(["class DegradationAlertDelivery"], mcp/src/agents_remember/serving/degradation_delivery.py:20-20)) implements the alert delivery contract used
by the degradation detector to post role-addressed inbox alerts; `__all__` exports only the class.

### Invariants And Boundaries

- Providers depend on the port; serving owns the concrete delivery. Do not move delivery into
  providers (layering rail enforced).

### Todos

No known follow-up.

## Evidence

### Docs References

No external/domain documentation is configured.

No configured domain documentation was available.

### Repo-Internal References

- The degradation detector declares the alert port this module implements. [1]

### Cross-Repo References

No cross-repository implementation participates.

No meaningful cross-repo references found.
