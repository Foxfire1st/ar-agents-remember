# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py

## Governing Overview

[overview.md](../../../../../overview.md)

## Purpose

`models.py` holds the shared data records, the drift-summary wire vocabulary, and
the constants for onboarding drift detection. It is the foundational module of the
`onboarding_drift_check` package and carries no behavior, so every classifier and
reporter — and, since 260731-EFA-L4, both wire models — can depend on it without
import cycles.

## Code Commentary

### Logic

Defines the `DriftRow` result record returned by every classifier, cit:([`DriftRow`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:58-69), the
`EntityFingerprint` row model, cit:([`EntityFingerprint`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:72-77), and the `InlineBlock` parse result,
cit:([`InlineBlock`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:80-83). Also defines the module constants: `CLASSIFICATIONS`,
`ACTIONABLE_CLASSIFICATIONS`, the inline markers, `GIT_BLOB_SET_ALGORITHM`,
`SIDECAR_DOC_TYPES`, cit:([`COMMON_BLOCK_DELIMITERS`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:47-55), and the
`repo_root_placeholder()` helper: cit:([`repo_root_placeholder`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:86-87).

### The drift summary vocabulary (260731-EFA-L4)

The module now also declares, once, what a drift summary *is*:

```python
DriftStatus = Literal["notChecked", "checked", "error"]   # L14

class DriftSummaryPacket(TypedDict):                      # L17-L25
    status: DriftStatus
    count: NotRequired[int]
    actionableCount: NotRequired[int]
    reportPath: NotRequired[str]
    actionableSample: NotRequired[list[dict[str, Any]]]
    rows: NotRequired[list[dict[str, Any]]]
    error: NotRequired[str]
```

`summary.py` produces every member of `DriftStatus`, and **both** wire models now
read the alias from here rather than each keeping a copy:
`models/drift.py::DriftSummary.status` (the context-packet model) and
`models/memory.py::DriftCheckResponse.status` (the tool response). `error` is the
member the packet model was missing — `run_drift_summary` returns
`{"status": "error", "error": ...}` whenever the onboarding root does not exist,
which is precisely when the diagnostic is wanted, so `DriftSummary` used to crash
on the very call meant to explain the problem. `DriftSummary` gained both the
status member and a matching `error: str | None = None` field;
`DriftCheckResponse` had carried both all along and simply stopped keeping a third
identical copy of the enum.

The `NotRequired` keys are the status-conditional half of the shape: only a
`checked` status carries `count`/`actionableCount`/`reportPath`/`actionableSample` and may carry
the internal opt-in complete `rows`,
and only an `error` status carries `error`. That is why `memory_quality/check.py`
reads them with `.get` — the guard there establishes the status, but the TypedDict
cannot carry that narrowing across the branch.

### Invariants And Boundaries

- Behavior-free: dataclasses, a TypedDict, type aliases and constants only; no
  I/O, git, or policy.
- Imported by `git_ops`, `discovery`, `report`, `entities`, `inline`, and
  `sidecar`; it must not import from them (keeps the package acyclic). The two
  wire models under `models/` import `DriftStatus` from here, which is the same
  direction — nothing here imports `models/`.
- **`DriftStatus` is the one declaration.** A new summary status is added here and
  both wire models pick it up; never re-type the members beside a `status` field.
  A member that exists on the producer but not on a consuming model is a
  `ValidationError` on the diagnostic path, which is how `error` was lost.
- **Status-conditional keys stay `NotRequired`.** The packet's optional keys are
  what let one type describe all three statuses; consumers narrow on `status` and
  read with `.get`.
- Complete `rows` are internal opt-in report material. Ordinary context/tool callers keep the
  bounded actionable sample and do not widen their transport payload.

## Evidence

### Repo-Internal References

- The producer of every `DriftStatus` member; its three summary builders are typed `-> DriftSummaryPacket`. [1]
- The context-packet wire model that reads `DriftStatus` and gained the matching `error` field. [2]
- The tool response model that dropped its third copy of the enum for the same alias. [3]
- The quality runner that consumes the packet and reads its status-conditional keys with `.get`. [4]
