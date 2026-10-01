# mcp/src/agents_remember/serving/conversation/active/capabilities.py

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

## Evidence

### Docs References

No `Domain Documentation` source is configured for this repository, so no live domain-documentation
pass was available for this file. Its subject is fixture evidence recorded in this repository.

No configured `Domain Documentation` source exists in `system/sources.md`; the evidence classes this module builds are the repository's own recorded fixtures.

### Repo-Internal References

- The keyed dispatch that replaced the silent pi fall-through, and the selector that reads it. [1]
- eve's own evidence builder — supported rows on the pinned native scenario, `unavailable` for a contract eve's stream does not carry, `unverified` for a real but unexercised one. [2]
- eve's fixture id, runtime version and its own observation time, distinct from the other three harnesses'. [3]
- The evidence record now takes its observation time as a parameter, so a builder cannot inherit another harness's date. [4]
- The three state constructors every builder shares, and the no-attachment declaration. [5]
- The sibling builders this one must not resemble in evidence. [6]
- The control gate's single-source interrupt verdict and eve's telemetry declaration, both consumed rather than restated. [7]
- The cases: the advertised catalog derives from the launch selection, eve never borrows another harness's evidence, and an unknown harness fails loudly instead of inheriting a catalog. [8]
- The projector whose frames every eve `supported` reason names. [9]

### Cross-Repo References

No external repository boundary is implemented by this module: it builds evidence records from
fixtures recorded in this repository.

No meaningful cross-repo references found.
