# mcp/src/agents_remember/memory_quality/check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/check.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `5920ea2b4bdd5d5ee969ae064ff9a8e1fc6b4060` |
| lastVerifiedCommitDate | 2026-08-05T12:41:24+02:00|
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

`run_drift_quality_check(drift_context)` branches on the packet's
status first: anything other than `checked` returns `ok: False` with one synthetic
`onboarding_drift_check_failed` finding built from `packet.get("error", ...)`: cit:([`run_drift_quality_check`], mcp/src/agents_remember/memory_quality/check.py:137-170).
Only past that guard does it read the checked-status keys. Since
260731-EFA-L4 `run_drift_summary` returns the typed `DriftSummaryPacket`, whose
`count`/`reportPath`/`actionableCount` are `NotRequired`, so those three reads are
`.get` rather than `[...]`: cit:(["count", "reportPath", "actionableCount"], mcp/src/agents_remember/memory_quality/check.py:137-170) — the guard has established the status, but
the TypedDict cannot carry that narrowing across the branch. No emitted value
changed: `summarize_rows` always sets all three on a `checked` packet.

### Invariants And Boundaries

- Unknown check names raise `ValueError`.
- Drift integrity requires `DriftCheckContext`; style checks can run with only
  an onboarding root.
- The top-level finding count uses each checker result's declared
  `findingCount`, so bounded drift samples can report fewer concrete findings
  than the total count. `run_memory_quality_check` coerces it with
  `int(result.get("findingCount", 0))`: cit:([`run_memory_quality_check`, "findingCount"], mcp/src/agents_remember/memory_quality/check.py:86-113), which assumes a checker never puts
  a literal `None` under that key — the drift checker's `.get` reads are safe only
  because the `checked` guard above guarantees the key is present.
- **The drift packet's shape is owned by `onboarding_drift_check/models.py`.**
  This runner narrows on `status` and reads the status-conditional keys
  defensively; it must not re-declare the status vocabulary or assume a key that
  `DriftSummaryPacket` marks `NotRequired`.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `memory_quality_check` MCP tool builds drift context and calls this runner. | `memory_quality_check` | mcp/src/agents_remember/mcp/registration/memory.py:57-75 |
| Update-history ordering is the first style checker. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/update_history/history_order.py:47-56 |
| Drift summary provides the integrity checker payload, now typed `-> DriftSummaryPacket`. | `run_drift_summary` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:25-73 |
| The declaration of the packet's status vocabulary and its `NotRequired` keys. | `DriftStatus`; `DriftSummaryPacket` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:14-14; mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:17-25 |

## Update History

- 2026-08-03T03:59:59+02:00 — Curated 8 citation findings (1 table row, 6 prose citations, 1 source-form repair): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T01:03+02:00 — 260731-EFA-L4 curator: the card documented `run_memory_quality_check`
  and the finding-normalization but never described `run_drift_quality_check`'s own result shape,
  which is what this leaf changed. Verified against the diff and the current source: the three
  checked-status reads `packet["count"]`/`packet["reportPath"]`/`packet["actionableCount"]` are
  now `.get`, because `run_drift_summary` returns the new `DriftSummaryPacket` TypedDict: cit:([`run_drift_quality_check`], mcp/src/agents_remember/memory_quality/check.py:137-170)
  whose keys are `NotRequired` — the `status != "checked"` guard above establishes them: cit:([`run_drift_quality_check`], mcp/src/agents_remember/memory_quality/check.py:137-170),
  but the type cannot carry that narrowing across the branch. Emitted values are unchanged.
  Documented the guard and the branch, sharpened the `findingCount` invariant to name the
  `int(result.get("findingCount", 0))` coercion: cit:([`run_memory_quality_check`], mcp/src/agents_remember/memory_quality/check.py:86-113), which depends on those keys actually being
  present, and added an invariant that the packet shape is owned by
  `onboarding_drift_check/models.py`. Added one reference row and citations for the two existing
  drift rows; the Repo-Internal References header was two columns and is now three.
- 2026-05-24T02:47+02:00: Created for the first combined memory quality runner.
