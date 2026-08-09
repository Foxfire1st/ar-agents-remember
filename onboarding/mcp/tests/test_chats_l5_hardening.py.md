# mcp/tests/test_chats_l5_hardening.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/tests/test_chats_l5_hardening.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-07-21T12:00+02:00 |
| lastVerifiedCommitHash | `7af76249ff1aa728d34a6e81c5f09c8bcb797484` |
| lastVerifiedCommitDate | 2026-08-09T02:17:45+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The 260718-CHATS-L5 evidence-backed hardening regressions (R7): each test reproduces the EXACT
failure class named in a master hardening obligation BEFORE proving the bounded fix, so the
regression fails loudly if the guard is ever removed. Two families — **H1** (the hosted-interaction
synchronizer 500 breaking the whole terminal-catalog sweep, plus the F2 log-on-state-change bound)
and **H2** (the L1 unknown-input provenance-validator 500, plus the F4 no-op refinement). Every case
is proven non-vacuous (fails on stashed source). The report's before/after proof is the companion
evidence.

## Code Commentary

### Logic

Seven regressions (H1×3 + F2 + H2×2 + F4). Fixtures: `_harness_entry` mints a running `codex`
harness row with a control endpoint (one the sweep will project + observe); `_snapshot` the matching
`AdapterSnapshot`; `_AliveHost` reports every session alive without touching tmux; `_POISON_TRANSCRIPT`
is the exact H1 input — a terminal result with `requestId=None` and a `vendorCorrelationId`
(`"orphan-correlation"`) matching no accepted inbox row.

- **H1 — `test_h1_poisoned_completion_raises_from_synchronizer_standalone`**: pins the UNCHANGED
  pre-fix contract — the real `HostedInteractionSynchronizer.observe` still raises
  `HarnessControlError("…does not match an accepted inbox row")` on the poisoned completion. H1 does
  not soften this contract; it only stops the error from taking down the sweep.
- **H1 — `test_h1_poisoned_row_is_quarantined_and_never_breaks_the_catalog_sweep`** (the core
  regression): wires the REAL synchronizer as the sweeper's `on_control_snapshot` exactly as `app.py`
  does — now a field of the `probe=LivenessProbe(hysteresis=…, pane_capturer=…, snapshot_reader=…,
  on_control_snapshot=…)` parameter object rather than a loose keyword — with one poisoned + one
  healthy alive row. `refresh()` MUST NOT raise; both rows project;
  `poison-1.control_raw.interactionSyncError` is set with the exact message (fail-loud on its OWN
  row), and `healthy-1` is untouched. Before the guard the `HarnessControlError` propagated out of
  the per-entry comprehension inside `catalog.batch()`, aborting the sweep for every row.
- **F2 — `test_f2_quarantine_logs_on_state_change_and_heals`**: because an orphan completion is the
  steady state of every cockpit-driven hosted chat, the warning must fire ONCE (first occurrence),
  stay silent while the same failure persists, and emit one `recovered` log on heal — while the
  per-sweep marker keeps the wire honestly degraded throughout. Uses a fresh sweeper per sweep (fixed
  clock, `LivenessProbe(hysteresis=TerminalCatalogLivenessConfig(sweep_interval_seconds=0.0), …)`)
  to sidestep the intra-process rate limiter, and asserts the
  warning/recovery counts on the `agents_remember.serving.terminal_liveness` logger plus the marker
  set/cleared on the catalog row.
- **H1 — `test_h1_healthy_completion_still_synchronizes_through_the_sweep`**: the guard must not
  suppress the NORMAL effect — seeds an accepted/delivered `OperatorInboxStore` row (built through
  `create_operator_inbox_entry(InboxMessage(…), routing=InboxRouting(address=InboxAddress(…)),
  poster=InboxPoster(…))`), feeds a matching
  `requestId`, and asserts the inbox completion synchronizes (`adapterDeliveryState=="completed"`)
  with no `interactionSyncError` marker.
- **H2 — `test_h2_native_remap_after_resolution_never_splits_input_authority`**: reproduces E2 at the
  store — `apply_item` an honest `unknown-input`/`native-history` user item, `apply_provenance(...,
  "cockpit")` resolves it to `operator`/`cockpit-composer`/`exact`, then re-`apply_item` the SAME
  native user item (re-emitting the `unknown-input` default). The re-map must not revert OR split the
  resolved triple; `_revalidate` (which mirrors the route's `model_validate` re-check that
  `model_copy(update=…)` skips) must not raise. Pre-fix the split item 500-ed exactly there.
- **H2 — `test_h2_unresolved_user_item_stays_honest_unknown_input`**: the honest path is undisturbed —
  with `apply_provenance(..., None)` (not found) the item stays `unknown-input`/`native-history`/
  `native-only` with no producer across a re-map (R6.4), never guessed into an authority.
- **F4 — `test_f4_identical_remap_after_resolution_is_a_true_no_op`**: an identical native re-map of a
  resolved user item — differing only in the authority fields a re-map must never own — must emit NO
  mutation (`apply_item(...) == []`) and NOT bump the revision, honoring the store's idempotence
  docstring instead of a redundant revision-bumping `upsert-item`.

### Conventions

Pure-function/in-memory regressions: the H1 tests drive the real `TerminalCatalogLivenessSweeper` +
real `HostedInteractionSynchronizer` with a doubled alive host and a mocked `read_control_transcript`
(no tmux, no socket); the H2/F4 tests drive the real `ProjectionStore` directly. `_revalidate` is the
in-test proxy for the active-page route's response re-validation boundary — the surface where the
silently-stored split item actually 500s. The in-test doubles are strict-pyright / protocol-conformant:
`_AliveHost.has_session(self, tmux_name)` names its parameter to match the real host protocol (then
`del tmux_name` marks it unused) rather than the underscore-prefixed form, poison-error assertions are
narrowed through an `isinstance(..., str)` extraction before the substring check, and the F2 transcript
`state` carries an explicit `dict[str, tuple[Mapping[str, object], ...]]` annotation — all satisfy the
whole-project pyright gate with NO `type: ignore` and zero behavior change (commit `352d5cd`, "260718-CHATS-L5
fixup").

### Invariants And Boundaries

- Each test pins the EXACT failure class and is non-vacuous on stashed source; H1 leaves the
  completion-correlation contract intact (the standalone test guards it) and only contains its blast
  radius; H2 keeps the resolved user-item authority triple coupled and leaves the unresolved honest
  path untouched.
- The H1 tests wire the synchronizer as the sweeper probe's `on_control_snapshot` exactly as `app.py`
  does — the regression is against the real sweep seam, not a stand-in.
- `model_copy(update=…)` skips validation in pydantic v2, so the store can hold an
  authority-inconsistent item silently; `_revalidate` is the assertion that the served product stays
  valid.

### Todos

None.

## Docs References

The resolved `Domain Documentation` registry has no entries; the hardening contract is
repository-owned and cited below.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured domain documentation was available for this suite. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The H1 quarantine under test: `_observe_control_snapshot` contains the per-entry synchronizer failure; `LivenessProbe` (L71) is the sweeper's probe parameter object. | `LivenessProbe` | mcp/src/agents_remember/serving/terminal_liveness.py:85-106 |
| The synchronizer whose `observe` raises on the orphan completion (contract left intact). | `observe` | mcp/src/agents_remember/serving/hosted_interactions.py:59-61 |
| The H2/F4 store pin under test: `_preserved_input_authority` keeps the user-item authority triple intact. | `_preserved_input_authority` | mcp/src/agents_remember/serving/conversation/active/store.py:54-74 |
| The validator (`preserve_input_authority`) whose violation the split item raises at re-validation. | `preserve_input_authority` | mcp/src/agents_remember/serving/conversation/_models_blocks.py:197-248 |
| The projector-tier and installed companions to these store-level regressions. | "Projector engine: hydration, ordering, idempotence, provenance, rehydration, gaps."; "Installed-runtime production proof for the L3 control API (260718-CHATS-L3, R7)." | mcp/tests/test_conversation_active_service.py:1-1; mcp/tests/test_conversation_control_installed.py:1-7 |

## Cross-Repo References

No cross-repository implementation participates in this suite.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History

- 2026-08-04T18:40+02:00 — 260731-EFA-L6 S18-B18 curator: normalized the 2 citation rows
  (terminal_liveness probe + quarantine ranges, and the two companion-suite docstring literals).
  Zero findings remain.

- 2026-07-31T16:50+02:00 — 260731-EFA-L2 code-quality gate: `TerminalCatalogLivenessSweeper` now
  takes `config` / `pane_capturer` / `snapshot_reader` / `on_control_snapshot` as one
  `LivenessProbe` parameter object (`hysteresis=` holds the `TerminalCatalogLivenessConfig`), and
  `create_operator_inbox_entry` now takes `InboxMessage` / `InboxRouting(address=InboxAddress(…))`
  / `InboxPoster` objects. Rewrote the H1 core-regression bullet, the F2 fresh-sweeper note, the
  H1 healthy-completion bullet, and the Invariants line that named `on_control_snapshot` as a
  loose sweeper argument, so the card describes the real wiring the tests use. Also re-anchored
  the cited line ranges the same commit moved: `_observe_control_snapshot` is L371-L421 in
  `terminal_liveness.py` (was L259-L331), `_preserved_input_authority` plus the no-op comparison
  are L54-L75 / L221-L245 in `store.py` (was L52-L74 / L150-L172), and `preserve_input_authority`
  is L377 in `models.py` (was L400). All seven regressions (H1x3 + F2 + H2x2 + F4) keep their
  names and assertions.
- 2026-07-21T12:00+02:00 — 260718-CHATS-L5P curator: body-reviewed against the post-L5 pyright fixup
  (commit `352d5cd`, "260718-CHATS-L5 fixup") that changed this file after the L5 verification (`68b3205`).
  The diff is strict-pyright conformance ONLY — a `Mapping` import, the fake `_AliveHost.has_session`
  parameter renamed `_tmux_name`→`tmux_name` + `del` (protocol-conformant), the H1 poison-error assertion
  narrowed via an `isinstance(..., str)` extraction, and an explicit F2 `state` annotation — with zero
  behavior change and no `type: ignore`; all seven regressions (H1×3 + F2 + H2×2 + F4) are identical in
  intent, so every claim above still holds. Added the strict-typing/protocol-conformant note to
  Conventions; verification metadata advanced to `352d5cd` (the body was reviewed this cycle).
- 2026-07-21T11:00+02:00 — 260718-CHATS-L5 curator: created the sidecar for the evidence-backed
  hardening suite — the H1 catalog-sweep quarantine regressions (poisoned-completion contract still
  raises standalone; one poisoned row never breaks the sweep and is fail-loud on its own row; the
  healthy synchronizer effect survives; F2 logs on state change and heals) and the H2 store
  regressions (a native re-map after resolution never splits the input-authority triple; the
  unresolved honest path stays `unknown-input`; F4's identical re-map is a true no-op). Verification
  is pinned to the leaf base (`9e6c15d`) because the new source file is uncommitted; closeout owns
  its first source stamp.
