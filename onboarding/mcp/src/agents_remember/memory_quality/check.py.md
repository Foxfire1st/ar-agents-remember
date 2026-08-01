# mcp/src/agents_remember/memory_quality/check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/check.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-01T01:03+02:00                     |
| lastVerifiedCommitHash | `e52edaf5b655f495580efd93306afdf922b19b51` |
| lastVerifiedCommitDate | 2026-08-01T11:01:51+02:00|
| governingOverview      | `../../../overview.md`                     |

## Purpose

`check.py` runs memory-layer quality checks and returns a single structured
payload for MCP closeout workflows.

## Code Commentary

### Logic

The module registers style checks by name, defines the drift integrity check
name, and exposes `run_memory_quality_check()`. Without drift context, the
default run is style-only. With `DriftCheckContext`, the default run combines
`integrity.onboarding_drift_check.summary` with
`style.update_history.history_order`.

Drift rows from `run_drift_summary()` are normalized into quality findings so
the MCP response has one finding list even when checks come from different
subdomains.

`run_drift_quality_check(drift_context)` (L71-L104) branches on the packet's
status first: anything other than `checked` returns `ok: False` with one synthetic
`onboarding_drift_check_failed` finding built from `packet.get("error", ...)`
(L77-L91). Only past that guard does it read the checked-status keys. Since
260731-EFA-L4 `run_drift_summary` returns the typed `DriftSummaryPacket`, whose
`count`/`reportPath`/`actionableCount` are `NotRequired`, so those three reads are
`.get` rather than `[...]` (L99-L101) — the guard has established the status, but
the TypedDict cannot carry that narrowing across the branch. No emitted value
changed: `summarize_rows` always sets all three on a `checked` packet.

### Invariants And Boundaries

- Unknown check names raise `ValueError`.
- Drift integrity requires `DriftCheckContext`; style checks can run with only
  an onboarding root.
- The top-level finding count uses each checker result's declared
  `findingCount`, so bounded drift samples can report fewer concrete findings
  than the total count. `run_memory_quality_check` coerces it with
  `int(result.get("findingCount", 0))` (L47), which assumes a checker never puts
  a literal `None` under that key — the drift checker's `.get` reads are safe only
  because the `checked` guard above guarantees the key is present.
- **The drift packet's shape is owned by `onboarding_drift_check/models.py`.**
  This runner narrows on `status` and reads the status-conditional keys
  defensively; it must not re-declare the status vocabulary or assume a key that
  `DriftSummaryPacket` marks `NotRequired`.

## Repo-Internal References

| Finding | Citations | Source Path |
| --- | --- | --- |
| `memory_quality_check` MCP tool builds drift context and calls this runner. | — | [skill_tools.py](agents-remember/mcp/src/agents_remember/controllers/skill_tools.py) |
| Update-history ordering is the first style checker. | — | [history_order.py](agents-remember/mcp/src/agents_remember/memory_quality/style/update_history/history_order.py) |
| Drift summary provides the integrity checker payload, now typed `-> DriftSummaryPacket`. | `run_drift_summary` L24-L72 | [summary.py](agents-remember/mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py) |
| The declaration of the packet's status vocabulary and its `NotRequired` keys. | `DriftStatus` L14; `DriftSummaryPacket` L17-L25 | [models.py](integrity/onboarding_drift_check/models.py) |

## Update History

- 2026-08-01T01:03+02:00 — 260731-EFA-L4 curator: the card documented `run_memory_quality_check`
  and the finding-normalization but never described `run_drift_quality_check`'s own result shape,
  which is what this leaf changed. Verified against the diff and the current source: the three
  checked-status reads `packet["count"]`/`packet["reportPath"]`/`packet["actionableCount"]` are
  now `.get` (L99-L101), because `run_drift_summary` returns the new `DriftSummaryPacket` TypedDict
  whose keys are `NotRequired` — the `status != "checked"` guard above (L77-L91) establishes them,
  but the type cannot carry that narrowing across the branch. Emitted values are unchanged.
  Documented the guard and the branch, sharpened the `findingCount` invariant to name the
  `int(result.get("findingCount", 0))` coercion at L47 that depends on those keys actually being
  present, and added an invariant that the packet shape is owned by
  `onboarding_drift_check/models.py`. Added one reference row and citations for the two existing
  drift rows; the Repo-Internal References header was two columns and is now three.
- 2026-05-24T02:47+02:00: Created for the first combined memory quality runner.
