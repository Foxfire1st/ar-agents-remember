# mcp/src/agents_remember/memory_quality/check.py

| Field                  | Value                                      |
| ---------------------- | ------------------------------------------ |
| repository             | agents-remember                         |
| path                   | `mcp/src/agents_remember/memory_quality/check.py` |
| doc_type               | `file-level-onboarding`                    |
| lastUpdated            | 2026-08-02T01:05+02:00                     |
| lastVerifiedCommitHash | `14582854955223f75588c23c9f29f9d51bde9675` |
| lastVerifiedCommitDate | 2026-09-18T09:05:03+02:00|
| governingOverview      | `../../../overview.md`                     |

## Governing Overview

[overview.md](../../../overview.md)

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

`StyleCheckInputs` carries the selected prepared code-history anchors alongside the code root and
temporary unstamped base. `run_check()` forwards those anchors to `claim_reopen`, so a prepared
closeout can verify current working-tree bytes against an explicit predecessor chain while
standalone checks remain strict. `DriftCheckContext` owns the same history tuple at the combined
runner boundary; it is comparison context, never a new verification stamp.

Drift rows from `run_drift_summary()` are normalized into quality findings so
the MCP response has one finding list even when checks come from different
subdomains. Internal callers may request all report-only rows and all drift rows for a file report;
the ordinary wire response keeps its bounded samples. `DriftCheckContext` also carries explicit
report output options so the full leaf checklist can defer Markdown publication to the unified
renderer while preserving the observer snapshot's final report path.

The closeout gate consumes this registry through two declared phase lists.
`BEFORE_METADATA_REFRESH_CHECKS` begins with the tree-only
`entity_catalog_alignment` check, then runs the citation gate (`range_resolution` +
`claim_reopen`). This phase runs before staging, hooks, the code commit, and the strict test
wrapper, so orphaned entity fingerprint rows and broken citations reject before Pyright or
pytest. `AFTER_METADATA_REFRESH_CHECKS` repeats citations without temporary provenance and adds
drift, document shape, and history order after metadata refresh. Closeout supplies the leaf base
only while evaluating dirty unstamped cards in the preflight; the post-refresh repetition has no
fallback, so every such card must receive the real code-commit stamp before memory commits.
`claim_reopen` splits detected change three ways: absent/ambiguous anchors and
unverifiable provenance are hard; a changed construct whose citation stays current (anchor
resolves uniquely, range covers it) is the report-only review surface; only a changed construct
with a stale pointer is enforced. The curator runs the same `memory_quality_check` during the
leaf, so gate findings are the exception, not the rule (260731-EFA-L16, repairing the L6
placement that deadlocked this leaf's own closeout with 115 unresolvable findings).

`run_drift_quality_check(drift_context)` branches on the packet's
status first: anything other than `checked` returns `ok: False` with one synthetic
`onboarding_drift_check_failed` finding built from `packet.get("error", ...)`
(`mcp/src/agents_remember/memory_quality/check.py:216-257`).
Only past that guard does it read the checked-status keys. Since
260731-EFA-L4 `run_drift_summary` returns the typed `DriftSummaryPacket`, whose
`count`/`reportPath`/`actionableCount` are `NotRequired`, so those three reads are
`.get` rather than `[...]` — the guard has established the status, but
the TypedDict cannot carry that narrowing across the branch. No emitted value
changed: `summarize_rows` always sets all three on a `checked` packet.

**A check that cannot acquire its source index reports rather than raising (260915-CAPS-L14).**
`run_check` wraps `_run_check` and converts a `SourceIndexError` into
`source_index_unavailable_result`: a `status: "citation-source-index-unavailable"` result carrying
one `error`-severity finding (`citation_source_index_unavailable`) whose message is the cause and
whose `nextStep` names the two operator levers (`onboarding.pathRules.exclude`,
`onboarding.citationIndex`). The raw exception must never escape to a client as a bare tool error,
because that turns the surface that *describes* memory into the surface that blocks it. Satisfiable
caps never reach this branch — they skip and report.

### Invariants And Boundaries

- Unknown check names raise `ValueError`.
- Drift integrity requires `DriftCheckContext`; style checks can run with only
  an onboarding root.
- The top-level finding count uses each checker result's declared
  `findingCount`, so bounded drift samples can report fewer concrete findings
  than the total count. `run_memory_quality_check` coerces it with
  `int(result.get("findingCount", 0))` (`mcp/src/agents_remember/memory_quality/check.py:112-143`),
  which assumes a checker never puts a literal `None` under that key — the drift checker's `.get`
  reads are safe only because the `checked` guard above guarantees the key is present.
- **An unusable source index is a reported check result, never a raised exception out of this
  runner.** The quality surface must remain able to describe a broken memory layer rather than
  becoming the thing that blocks work.
- **The drift packet's shape is owned by `onboarding_drift_check/models.py`.**
  This runner narrows on `status` and reads the status-conditional keys
  defensively; it must not re-declare the status vocabulary or assume a key that
  `DriftSummaryPacket` marks `NotRequired`.
- Full internal detail is opt-in and is removed before the public response. Bounded samples remain
  the default transport contract; report generation must not expand normal MCP payloads.

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| `memory_quality_check` MCP tool builds drift context and calls this runner. | `memory_quality_check` | mcp/src/agents_remember/mcp/registration/memory.py:57-75 |
| Update-history ordering is the first style checker. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/update_history/history_order.py:47-56 |
| Drift summary provides the integrity checker payload, now typed `-> DriftSummaryPacket`. | `run_drift_summary` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/summary.py:25-73 |
| The packet's `status` field typed by the imported status vocabulary, plus its `NotRequired` keys. | `DriftSummaryPacket` | mcp/src/agents_remember/memory_quality/integrity/onboarding_drift_check/models.py:11-20 |
| The first pre-code check enforces entity inventory/fingerprint alignment without requiring code metadata. | `check_onboarding_root` | mcp/src/agents_remember/memory_quality/style/document_shape/entity_catalog_alignment.py:70-130 |
| Style checks receive retained prepared-history anchors and forward them through the citation gate while current bytes remain the comparison surface. | `StyleCheckInputs` | mcp/src/agents_remember/memory_quality/check.py:40-55 |
| The guarded entry point that reports an unusable source index instead of raising. | `run_check` | mcp/src/agents_remember/memory_quality/check.py:146-163 |
| The status a reported unusable source index carries. | `SOURCE_INDEX_UNAVAILABLE_STATUS` | mcp/src/agents_remember/memory_quality/check.py:33-33 |
| An unusable source index becomes a reported result with the cause and the operator levers. | `source_index_unavailable_result` | mcp/src/agents_remember/memory_quality/check.py:193-213 |
| The inner runner the guard wraps. | `_run_check` | mcp/src/agents_remember/memory_quality/check.py:166-190 |
| The typed error the guard converts. | `SourceIndexError` | mcp/src/agents_remember/memory_quality/style/citations/source_index_state.py:64-65 |
| The checked-status reads and their `NotRequired` guard. | `run_drift_quality_check` | mcp/src/agents_remember/memory_quality/check.py:216-257 |
| The case pinning the reported state when an index cannot be built at all. | `test_an_index_that_cannot_be_built_is_a_reported_state_with_a_next_step` | mcp/tests/test_citation_index_resilience.py:613-629 |
| The case pinning the closeout gate's own declared check group degrading the same way. | `test_the_closeout_gates_own_check_group_degrades_the_same_way` | mcp/tests/test_citation_index_resilience.py:631-656 |

## Update History
2026-09-18T06:55+02:00 — 260915-CAPS-L24 curator: **stale citations repaired in this document.** This leaf's curator re-derived every failing citation row against the file it cites: each Anchor cell now names text that exists inside the cited range, each Source cell is a plain `path:start-end` in bounds of the file as it stands, and a claim whose construct the source no longer carries was re-worded to what the source now says rather than re-pointed at something adjacent. Mechanically regenerable ranges were rewritten by the shipped citation fixer; the rest were repaired by reading the source. No verification stamp advanced on content alone: the candidate is uncommitted and the governed closeout owns the real code and memory commits.

- 2026-09-17T12:45+02:00 — 260915-CAPS-L14 curator: recorded the **reported-state guard** this leaf adds — `run_check` wrapping `_run_check` so a `SourceIndexError` becomes a `citation-source-index-unavailable` result with the cause and the two operator levers, instead of a bare tool error out of the surface that is supposed to describe a broken memory layer. Added the `source_index_unavailable_result` / `_run_check` / `run_drift_quality_check` rows and the corresponding invariant. **Flattened the legacy citation form**: four body cells using an inline `cit:([…], path:a-b)` wrapper and every `cit:(…)` in this card's history are now the required `| Finding | Anchor | Source |` rows plus plain `path:start-end`; the historical entries keep their wording, identifiers and meaning, with only the wrapper and their stale ranges re-expressed. **Re-derived every range against the 296-line source** (the runner moved from `:103-130` to `:112-143` and `run_drift_quality_check` from `:171-212` to `:216-257`). Verification metadata is left at this leaf's synced base `0346da9c`; the candidate is deliberately uncommitted, so the governed closeout stamps the real code commit.

- 2026-09-10T04:35+02:00 — CCR-L42 final predecessor-history curation: documented the retained
  code-history tuple flowing through `StyleCheckInputs`, `DriftCheckContext`, and `run_check()`
  into current-byte citation validation; verification metadata remains closeout-owned.

- 2026-08-11T16:54+02:00 — Added opt-in complete drift/report-only materialization and report
  output control for the unified enclosure curator checklist; default quality payloads stay bounded.
- 2026-08-10T12:46+02:00 — L9 fail-fast repair: registered
  `style.document_shape.entity_catalog_alignment` and placed it first in
  `BEFORE_METADATA_REFRESH_CHECKS`, ahead of citations and every code rail. This moves pure
  catalog-structure failures out of the post-refresh drift phase without moving source/hash drift,
  which can only clear after real commit metadata exists. Verification metadata stays pinned until
  closeout stamps the repair commit.

- 2026-08-10T08:20+02:00 — 260805-ARG-L1 closeout-order hardening: recorded the explicit
  pre-code-quality citation preflight, temporary base provenance for dirty unstamped cards, and
  the no-fallback post-refresh citation repetition that proves real stamps exist before memory
  commits. Verification metadata remains pinned until closeout stamps ARG-L1.
- 2026-08-05T22:55+02:00 — 260731-EFA-L16 curator: recorded the citation-gate semantics and placement. The L6 closeout placement ran `style.citations.claim_reopen` before the code commit with a clearing condition that required the commit to exist — unreachable, and it deadlocked this leaf's closeout with 115 unresolvable findings. Now: detected change splits into hard (absent/ambiguous anchor, unverifiable provenance, stale pointer) versus report-only review surface (changed construct with a current citation — anchor resolves uniquely, range covers it, clearing needs no commit), and the citation gate (`range_resolution` + `claim_reopen`) runs before the strict wrapper and the code commit, so failures reject in seconds. The curator runs the same `memory_quality_check` during the leaf; gate findings are the exception. Verification metadata stays pinned until closeout stamps the L16 commit.
- 2026-08-03T03:59:59+02:00 — Curated 8 citation findings (1 table row, 6 prose citations, 1 source-form repair): added exact anchors and source paths; scoped fixer generated the final ranges.

- 2026-08-02T01:05+02:00 — No content impact: `mcp/src/agents_remember/tasks/reopen.py` moved to `mcp/src/agents_remember/worktrees/reopen.py` (reopen rewrites the leaf's enclosure contract, and ranking it as a task operation made `tasks` and `worktrees` mutually dependent per `layers.toml`). Re-pointed the reference here; the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-02T00:17+02:00 — No content impact: 260731-EFA-L6 renamed `mcp/src/agents_remember/controllers/` to `application/` and moved `worktrees/status.py` to `application/worktree_status.py`. Updated the references and the vocabulary here ("the application layer" for the package, "an application entry point" for one function); the behavior this document describes is unchanged. Verification metadata pinned until closeout stamps the L6 code commit.
- 2026-08-01T01:03+02:00 — 260731-EFA-L4 curator: the card documented `run_memory_quality_check`
  and the finding-normalization but never described `run_drift_quality_check`'s own result shape,
  which is what this leaf changed. Verified against the diff and the current source: the three
  checked-status reads `packet["count"]`/`packet["reportPath"]`/`packet["actionableCount"]` are
  now `.get`, because `run_drift_summary` returns the new `DriftSummaryPacket` TypedDict (mcp/src/agents_remember/memory_quality/check.py:216-257).
  whose keys are `NotRequired` — the `status != "checked"` guard above establishes them (mcp/src/agents_remember/memory_quality/check.py:216-257),
  but the type cannot carry that narrowing across the branch. Emitted values are unchanged.
  Documented the guard and the branch, sharpened the `findingCount` invariant to name the
  `int(result.get("findingCount", 0))` coercion (mcp/src/agents_remember/memory_quality/check.py:112-143), which depends on those keys actually being
  present, and added an invariant that the packet shape is owned by
  `onboarding_drift_check/models.py`. Added one reference row and citations for the two existing
  drift rows; the Repo-Internal References header was two columns and is now three.
- 2026-05-24T02:47+02:00: Created for the first combined memory quality runner.

