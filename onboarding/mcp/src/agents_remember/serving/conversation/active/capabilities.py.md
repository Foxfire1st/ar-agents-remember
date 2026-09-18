# mcp/src/agents_remember/serving/conversation/active/capabilities.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/conversation/active/capabilities.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `ea9cf0abeab4fe88961bda10b4f54d30266a9634` |
| lastVerifiedCommitDate | 2026-09-17T23:56:19+02:00|
| governingOverview | `overview.md` |

## Governing Overview

[Active conversation serving overview](overview.md)

## Purpose

Exact-session capability evidence for the active conversation surface: per-session
`ConversationCapabilities` built only from landed installed-runtime fixture evidence through the
production seam — a feature is `supported`/`partial` only with fixture evidence, a native shape whose
contract has never been probed through a captured fixture is `unverified`, and a contract the harness
cannot provide is `unavailable`.

**The dispatch is a keyed table, and that is a correctness property, not a style choice.**
`capabilities_for` looks the harness id up in `_CONTROL_PLANE`; a harness this view has no evidence
for raises instead of being served. The previous shape ended in `return _pi_capabilities(snapshot)`,
which would have published **pi's** fixture ids, runtime version and `supported` rows under any
unrecognized harness's name — the exact capability dishonesty this module exists to prevent. Adding
`eve` is what exposed it, and the fix is a keyed dispatch rather than a fourth `if`.

THE CONTRACT IS THE ONLY GATE (developer ruling 2026-07-21, executed in R4):
no capability is gated, locked, or demoted by a version-string comparison. The observed
runtime/helper version rides the evidence record as informational metadata only; a capability
demotes solely when its contract fails verification or has never been probed — never because an
installed version drifts from a fixture's captured version. The prior observed-version read-time
demotion is REMOVED: harnesses auto-update, and a version predicate is exactly what made the
natively-succeeding claude surface unusable (the image3 "unverified: observed runtime/helper
version differs from capability evidence" banner).

## Code Commentary

### Logic

Each harness has its own builder — `_codex_capabilities` (121), `_claude_capabilities` (212),
`_pi_capabilities` (260), `_eve_capabilities` (351) — and each returns a `ConversationCapabilities`
with four parts: `live`, `history`, `controls`, `telemetry`.

The builders share three constructors rather than restating policy: `_runtime(state, reason, evidence)`
for a claim backed by an observed runtime, `_adapter(state, reason, runtime_version)` for a claim
about the adapter whose contract is unprobed, and `_unavailable(reason)` for a contract the harness
cannot provide at all. `_fixture_evidence()` (64) assembles the `CapabilityEvidence` record, and it
now takes `observed_at` as a parameter so a builder can carry its own observation time instead of
inheriting one global constant — eve's evidence is observed on a different date from the other three.

`_eve_capabilities` (351) is the new builder, and its conservatism is the point: `text`, `thinking`,
`tools`, `interactions` and `policy_read` are `supported` on the pinned runtime's recorded native
scenario (a real session, tool round-trip, an input request, a cancel and a park) crossing the
production evidence seam; `diffs` is `unavailable` because eve's stream carries no structured diff
frame; `completeness` is `partial` because the durable stream is complete per session but this view
reads a bounded evidence window; the two history-completeness rows are `unverified`; and the three
library-shaped history rows are `unavailable` with the owning leaf named. `controls.interrupt` is
bridged from the control gate's single-source verdict, and `telemetry` from the control module —
neither is restated here.

`_CONTROL_PLANE` (432) is the dispatch table, and `capabilities_for` (440) is one lookup:
`return _CONTROL_PLANE[harness_id](snapshot)`.

### Conventions

- Capabilities are per-session evidence, never a global harness marketing table: no feature is enabled
  by documentation or changelog text, and fixture presence alone never enables anything — only
  fixture-observed shapes through the production seam count.
- Every reason string names the frame or contract it rests on, so a `supported` row is auditable
  without reading the builder.
- A cross-leaf feature is `unavailable` **with the owning leaf named**, never `supported` by
  anticipation.
- Each builder carries its own fixture id, runtime version and observation time; nothing is shared by
  default across harnesses.

### Invariants And Boundaries

- Every `supported`/`partial` claim names its fixture evidence (runtime version, fixture id,
  observed-at); `unverified` claims name the un-probed contract (never a version).
- NO version-string comparison gates or demotes any capability. A capability demotes solely when its
  contract fails verification or was never probed; the observed runtime version is informational
  evidence only. `capabilities_for` deliberately ignores the snapshot version.
- **An unrecognized harness must fail loudly.** `_CONTROL_PLANE[harness_id]` raises `KeyError` for an
  id with no evidence; a `default` arm or a final unconditional `return` reintroduces the silent
  inheritance defect.
- **No harness may borrow another's evidence.** Each builder names its own fixture id and runtime
  version, and a case asserts eve's rows never equal pi's.
- Cross-leaf features stay `unavailable` with the owning leaf named — no active-route feature claims
  library or control surface.

### Todos

None.

## Docs References

No `Domain Documentation` source is configured for this repository, so no live domain-documentation
pass was available for this file. Its subject is fixture evidence recorded in this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source exists in `system/sources.md`; the evidence classes this module builds are the repository's own recorded fixtures. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The keyed dispatch that replaced the silent pi fall-through, and the selector that reads it. | `_CONTROL_PLANE`; `capabilities_for` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:432-437; mcp/src/agents_remember/serving/conversation/active/capabilities.py:440-457 |
| eve's own evidence builder — supported rows on the pinned native scenario, `unavailable` for a contract eve's stream does not carry, `unverified` for a real but unexercised one. | `_eve_capabilities` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:351-429 |
| eve's fixture id, runtime version and its own observation time, distinct from the other three harnesses'. | `_EVE_FIXTURE`; `_EVE_RUNTIME`; `_EVE_OBSERVED_AT` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:51-51; mcp/src/agents_remember/serving/conversation/active/capabilities.py:58-58; mcp/src/agents_remember/serving/conversation/active/capabilities.py:61-61 |
| The evidence record now takes its observation time as a parameter, so a builder cannot inherit another harness's date. | `_fixture_evidence` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:64-76 |
| The three state constructors every builder shares, and the no-attachment declaration. | `_runtime`; `_adapter`; `_unavailable`; `_no_attachments` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:79-89; mcp/src/agents_remember/serving/conversation/active/capabilities.py:92-98; mcp/src/agents_remember/serving/conversation/active/capabilities.py:101-102; mcp/src/agents_remember/serving/conversation/active/capabilities.py:105-118 |
| The sibling builders this one must not resemble in evidence. | `_codex_capabilities`; `_claude_capabilities`; `_pi_capabilities` | mcp/src/agents_remember/serving/conversation/active/capabilities.py:121-209; mcp/src/agents_remember/serving/conversation/active/capabilities.py:212-257; mcp/src/agents_remember/serving/conversation/active/capabilities.py:260-348 |
| The control gate's single-source interrupt verdict and eve's telemetry declaration, both consumed rather than restated. | `interrupt_capability_for`; `telemetry_capabilities_for`; `_eve_controls`; `_eve_telemetry` | mcp/src/agents_remember/serving/conversation/control/capabilities.py:310-342; mcp/src/agents_remember/serving/conversation/control/capabilities.py:345-359; mcp/src/agents_remember/serving/conversation/control/capabilities.py:390-398; mcp/src/agents_remember/serving/conversation/control/capabilities.py:401-411 |
| The cases: the advertised catalog derives from the launch selection, eve never borrows another harness's evidence, and an unknown harness fails loudly instead of inheriting a catalog. | `EveCapabilityHonestyTests` | mcp/tests/test_eve_product_integration.py:1134-1287 |
| The projector whose frames every eve `supported` reason names. | `map_evidence_frame` | mcp/src/agents_remember/serving/conversation/projectors/eve.py:147-159 |

## Cross-Repo References

No external repository boundary is implemented by this module: it builds evidence records from
fixtures recorded in this repository.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | — | — |

## Update History
- 2026-09-17T20:42:17+00:00: Generated citation repair: `EveCapabilityHonestyTests` repointed to mcp/tests/test_eve_product_integration.py:1134-1287. No content impact: mechanical anchor-range projection bound to citation source snapshot a7178848e5b50ce4b2c04d35c06a10a15d6ed52d29d3880b7d032b23fc57f74b; claim bytes unchanged; generated by ccr-r10@v1.
- 2026-09-16T11:42:27+00:00: Generated citation repair: `_runtime`; `_adapter`; `_unavailable`; `_no_attachments` repointed to mcp/src/agents_remember/serving/conversation/active/capabilities.py:79-89; mcp/src/agents_remember/serving/conversation/active/capabilities.py:92-98; mcp/src/agents_remember/serving/conversation/active/capabilities.py:101-102; mcp/src/agents_remember/serving/conversation/active/capabilities.py:105-118. No content impact: mechanical anchor-range projection bound to citation source snapshot 0660715def1042680448936e65be361ff85885dc4b74c0f6d91afac6b5f24074; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: **the selector no longer has a default arm.**
  `capabilities_for`'s `if codex / if claude / return _pi_capabilities(...)` chain is now a keyed
  `_CONTROL_PLANE` lookup, so a harness this view has no evidence for raises instead of being served
  pi's fixture ids, runtime version and `supported` rows under its own name — the silent-inheritance
  defect that adding `eve` exposed. Added `_eve_capabilities` with its own fixture id, runtime version
  and observation time; `_fixture_evidence` gained an `observed_at` parameter so a builder carries its
  own date rather than inheriting the shared constant. Body rewritten on Purpose, Logic, Conventions,
  Invariants and the reference table, and the three inline `cit:(…)` prose citations were converted to
  audit rows in the required `Finding | Anchor | Source` shape. Verification metadata moves to the
  leaf's synced base `ff97072c`; the candidate is deliberately uncommitted, so the governed closeout
  stamps the real code commit and no hash or fingerprint was invented here.
- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T13:47:55+02:00 — 260731-EFA-L6 S18-B11 same-reviewer correction: bound the all-harness capability rule to every builder, the selector, and the interrupt bridge. Verification metadata unchanged.

- 2026-07-31T16:35+02:00 — No content impact: the whole-tree `ruff format` pass changed only
  formatting in this module; the prior capability references were revalidated against the linked
  source cards after the service and model edits.

- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator ATTESTATION: this file was touched by the whole-tree `ruff format` commit (`00e8379`) and by nothing else — `git diff 00e8379 -- <this file>` is empty, so no identifier, signature, branch or behaviour in it changed in this leaf and no claim in this sidecar can have been invalidated by it. Attested, deliberately not rewritten.
- 2026-07-24T13:18:47Z — Prior curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-21T11:30+02:00 — Prior curator: corrected the now-false read-time version-demotion doctrine,
  refreshed the per-harness evidence, and left the first verification stamp for closeout.
- 2026-07-19T17:35+02:00 — Prior curator: created the sidecar for exact-session capability evidence.
