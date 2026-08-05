# mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T00:56+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
| governingOverview      | `../../../../../overview.md`               |

## Purpose

`models.py` holds the shared data records, the drift-summary wire vocabulary, and
the constants for onboarding drift detection. It is the foundational module of the
`onboarding_drift_check` package and carries no behavior, so every classifier and
reporter — and, since 260731-EFA-L4, both wire models — can depend on it without
import cycles.

## Code Commentary

### Logic

Defines the `DriftRow` result record returned by every classifier, cit:([`DriftRow`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:64-75), the
`EntityFingerprint` row model, cit:([`EntityFingerprint`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:78-83), and the `InlineBlock` parse result,
cit:([`InlineBlock`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:86-89). Also defines the module constants: `CLASSIFICATIONS`,
`ACTIONABLE_CLASSIFICATIONS`, the inline markers, `GIT_BLOB_SET_ALGORITHM`,
`SIDECAR_DOC_TYPES`, cit:([`COMMON_BLOCK_DELIMITERS`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:53-61), and the
`repo_root_placeholder()` helper: cit:([`repo_root_placeholder`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:92-93).

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
`checked` status carries `count`/`actionableCount`/`reportPath`/`actionableSample`,
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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The drift facade re-exports these models/constants for backward-compatible imports. | `DriftRow` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/drift.py:63-75 |
| The producer of every `DriftStatus` member; its three summary builders are typed `-> DriftSummaryPacket`. | `not_checked`; `run_drift_summary`; `summarize_rows` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:21-22; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:25-73; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:76-91 |
| The context-packet wire model that reads `DriftStatus` and gained the matching `error` field. | `DriftSummary` | mcp/src/agents_remember/models/drift.py:13-23 |
| The tool response model that dropped its third copy of the enum for the same alias. | `DriftCheckResponse` | mcp/src/agents_remember/models/memory.py:13-27 |
| The quality runner that consumes the packet and reads its status-conditional keys with `.get`. | `run_drift_quality_check` | mcp/src/agents_remember/memory_quality/check.py:137-170 |

## Update History

- 2026-08-03T03:59:59+02:00 — Curated 7 citation findings (1 table row, 5 prose citations, 1 source-form repair): added exact anchors and source paths; removed one duplicate source extent; scoped fixer generated the final ranges.

- 2026-08-01T00:56+02:00 — 260731-EFA-L4 curator: the card said this module defines "the `DriftRow`
  result record, the `EntityFingerprint` row model, and the `InlineBlock` parse result" plus a
  named list of constants, and asserted "dataclasses and constants only". All three claims were
  incomplete after this leaf. Verified against the diff and the current source and documented the
  new declarations: cit:([`DriftStatus`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:14-14) and the `DriftSummaryPacket` TypedDict: cit:([`DriftSummaryPacket`], mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:17-25). Recorded
  why they are here rather than beside either wire model — `models/drift.py::DriftSummary` and
  `models/memory.py::DriftCheckResponse` now both import `DriftStatus` from this declaration, and
  the copy that used to sit on `DriftSummary` was missing `error`, so the packet crashed on the
  exact call (`run_drift_summary` with a non-existent onboarding root) that exists to report the
  problem. Widened the behavior-free invariant to name the TypedDict and type aliases, noted that
  the `models/` imports run in the allowed direction, and added two invariants (one declaration;
  status-conditional keys stay `NotRequired`). Added line ranges for the three dataclasses and the
  constants block, and four reference rows with verified citations.
- 2026-05-29T12:10+02:00: Created when `drift.py` was split into focused modules; metadata pending closeout refresh to the split commit.
