# mcp/src/agents_remember/memory_quality/check.py

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

**On a converted memory tree the runner dispatches by format (MIK-R24 rule 5).** `run_memory_quality_check`
asks `reference_state.is_converted_memory` whether the onboarding root's parent holds
`knowledge/layout.json`. If it does, every selected check goes through `_converted_check`:

- the checks that read the legacy card format (`LEGACY_FORMAT_CHECKS` in `converted_check.py`: Update
  History order, citation `range_resolution` and `claim_reopen`) return `not-applicable-converted` and pass;
- the drift slot runs `converted_knowledge_check` instead: the knowledge validator over the whole tree
  (refusing violations are findings), plus the stale-reference report, which is report-only;
- every other check runs as before.

The result key of the drift slot is `knowledge.converted`, not the drift check's name. An unconverted tree
runs exactly as before. Since the cutover (L37) the installed runtime carries this dispatch, and this master's
memory line is converted.

**The converted check's base (L37 review R3-1).** `DriftCheckContext.knowledge_base` is an optional
`KnowledgeBasePort`; `_converted_check` passes it to `converted_knowledge_check(..., base=...)`. The
application binds it to the shared converted-base cache, so a converted working tree on an unconverted `HEAD`
is validated against `HEAD`'s conversion (MIK-R24 rule 7). Without it the check uses a converted `HEAD`.

`run_drift_quality_check(drift_context)` branches on the packet's
status first: anything other than `checked` returns `ok: False` with one synthetic
`onboarding_drift_check_failed` finding built from `packet.get("error", ...)`
(`mcp/src/agents_remember/memory_quality/check.py:250-291`).
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
  `int(result.get("findingCount", 0))` (`mcp/src/agents_remember/memory_quality/check.py:124-160`),
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

## Evidence

### Repo-Internal References

- `memory_quality_check` MCP tool builds drift context and calls this runner. [1]
- Update-history ordering is the first style checker. [2]
- Drift summary provides the integrity checker payload, now typed `-> DriftSummaryPacket`. [3]
- The packet's `status` field typed by the imported status vocabulary, plus its `NotRequired` keys. [4]
- The first pre-code check enforces entity inventory/fingerprint alignment without requiring code metadata. [5]
- Style checks receive retained prepared-history anchors and forward them through the citation gate while current bytes remain the comparison surface. [6]
- A converted tree is dispatched by format: legacy-format checks do not apply, and the drift slot runs the validator plus the stale-reference report. [7]
- The guarded entry point that reports an unusable source index instead of raising. [8]
- The status a reported unusable source index carries. [9]
- An unusable source index becomes a reported result with the cause and the operator levers. [10]
- The inner runner the guard wraps. [11]
- The typed error the guard converts. [12]
- The checked-status reads and their `NotRequired` guard. [13]
- The case pinning the reported state when an index cannot be built at all. [14]
- The case pinning the closeout gate's own declared check group degrading the same way. [15]

- The drift context carries the converted tree's comparison base. [16]
- The converted check receives the base port. [17]
