# mcp/src/agents_remember/serving/capsule_delivery.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/capsule_delivery.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:15+02:00 |
| lastVerifiedCommitHash | `34f818a190c35238dca33552d586ea2ace5d9e06` |
| lastVerifiedCommitDate | 2026-09-16T14:33:47+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l5-ar` uncommitted source; base `c1dbebf883f22710b71d40a66ec92c1ac134918f` |
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

**How one admitted role capsule reaches the Codex app-server instruction channel — as a value, not as a
second control system.** The module owns three things and nothing else:

1. the delivery **value type** (`CodexCapsuleDelivery`) and its binding identity, wire form and report;
2. the **lifetime decision** (`plan_refresh`) for a delivery that meets a thread which already exists;
3. the **legacy-chain switch** (`legacy_instruction_switch`) that keeps the host's own instruction
   document load off a capsule launch — and only a capsule launch.

`260915-CAPS-L5` added it. It exists because the capsule must arrive at the `serving` rank as an
**admitted value**: the compiler (L2) and the admission surface (L4) rank **above** `serving` in
`layers.toml`, so this module may not import them. It therefore defines what the seam consumes over
`models`-rank imports only, and the owner that compiles the capsule fills it.

## Code Commentary

### Logic

**The value.** `CodexCapsuleDelivery` is a frozen, slotted dataclass of exactly four fields — the
binding, the trusted instruction stream, the compiler's semantic digest, and the skill pointers.
`__post_init__` refuses an empty instruction stream and a digest that is not the compiler's own
`sha256:` form. `capsule_delivery_from(compilation)` is the **only** constructor from a compilation: it
reads L2's landed shapes structurally (`capsule.binding.admitted`, `render_instructions()` on the
result) rather than importing them, copies `render_instructions()` **verbatim**, maps the admitted seat
through `_seat_role` (a role seat's own `role`; the launcher seat's `LAUNCHER_ROLE_SENTINEL`), and
refuses an unrecognised seat kind instead of guessing a role.

**The refresh decision.** `plan_refresh(delivery, state, *, fork_available=False)` returns a
`RefreshPlan` — never a silent third answer:

| State | Mode |
| --- | --- |
| no thread open | `INITIAL` |
| open thread carries a different binding | `UNSUPPORTED` (refusal, `applies_instructions=False`) |
| same binding, same semantic digest | `IN_PLACE` (identical bytes, nothing stacks) |
| same binding, changed digest, `fork_available` | `FORK_THREAD` |
| same binding, changed digest, no fork | `FRESH_THREAD` (bounded fresh thread at a safe boundary) |

`thread_instruction_params(delivery, plan)` returns `{INSTRUCTION_PARAM: trusted_instructions}` and
nothing else; a refusal plan **raises** rather than yielding parameters. `INSTRUCTION_PARAM` is
`developerInstructions` — deliberately not `baseInstructions`, which replaces the vendor's own base
prompt and is the vendor's authority, not ours.

**The legacy switch.** `legacy_instruction_switch(*, capsule_delivered, observed_sources)` is
detect-then-switch: with no capsule it returns `suppress=False` (the legacy chain is preserved), and
with a capsule it returns `suppress=True` plus `request_config == {"project_doc_max_bytes": 0}` using
the **existing** per-thread `config` owner the adapter already sends. `observed_sources` is what the
host actually loaded on the previous open; the observation changes the **reason and its report**, not
whether the switch fires — that limit is stated rather than dressed up.

**The wire form.** `to_json`/`from_json` exist so the carrier survives the base64 runner payload.
`from_json` returns `None` for anything unusable and never raises: the value type stays free of
transport policy, and the runner decides (it refuses). `as_report` is the provenance projection
published on the thread-open evidence and carries no instruction prose.

### Conventions

Rank discipline is the module's reason to exist: `serving` must not import `application`. Field names
are wire-visible (`repositoryId`, `taskPath`, `role`, `operation`, `trustedInstructions`,
`semanticDigest`, `skillPointers`), so a rename is a transport change. Enum values are lower-case
hyphenated strings because they are published verbatim in `capsuleRefresh.mode`.

### Invariants And Boundaries

- **Three channels, three owners, no mixing.** `developerInstructions` carries the capsule's trusted
  instruction stream; the ordinary turn input carries the task projection; skill pointers are carried
  but never composed. Task text, MCP text, tool output and model-authored text have **no parameter**
  here — `thread_instruction_params` raises rather than accepting them, and `CapsuleSkillPointer` has
  no route into the instruction stream by construction.
- **One capsule per admitted binding, applied at a supported native boundary.** The installed
  app-server (measured `codex-cli 0.151.0`) exposes instruction fields on `thread/start`,
  `thread/resume` and `thread/fork` and **none** on `turn/start`, so an ordinary user message cannot
  re-apply the corpus. Stacking two instruction revisions on one thread is not a fourth option.
- **The delivered bytes are the compiler's bytes.** Nothing here re-derives, re-renders, re-orders or
  re-selects: `capsule_delivery_from` copies `render_instructions()` unchanged, and the digest it
  compares is the compiler's semantic digest.
- **Absent, not null.** A capsule-free launch must transmit the payload it always sent, so the
  carrier's wire form is emitted only when a delivery exists (the conditional key lives in
  `harness_control_runner.py`); nothing in this module may make the key appear unconditionally.
- **The suppression key is not a global configuration change.** `project_doc_max_bytes` rides the
  per-thread `config` object for one launch, and `request_config` is empty unless a capsule is being
  delivered.
- **Declared limits, not gaps.** The vendor-side effect of re-sending `developerInstructions` on
  `thread/resume` is unmeasured on `0.151.0` (no rollout persists until a real turn runs), so
  `IN_PLACE` is schema- and unit-proven only; `FORK_THREAD` is exercised by tests but has **no
  production consumer**; and the delivered payload's size is bounded by nothing in this module — see
  the `harness_control_runner.py` card and defect `D12` for the measured argv headroom and the
  `E2BIG` failure mode at spawn.

### Todos

None known for this module. A stated compiled-capsule size bound with a pre-encoding refusal is
routed to the final-verification leaf (`D12`), not to this seam.

## Docs References

No Domain Documentation entries are configured in the resolved source registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured live documentation source was available for this pass. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The instruction parameter and the refresh-report key are named constants, chosen against the vendor's own base prompt. | `INSTRUCTION_PARAM`; `REFRESH_REPORT_KEY` | mcp/src/agents_remember/serving/capsule_delivery.py:44-52 |
| The delivery value refuses an empty instruction stream and a non-`sha256:` digest at construction. | `CodexCapsuleDelivery.__post_init__` | mcp/src/agents_remember/serving/capsule_delivery.py:182-190 |
| The wire form returns `None` for an unusable value instead of raising, leaving refusal policy to the transport boundary. | `CodexCapsuleDelivery.from_json` | mcp/src/agents_remember/serving/capsule_delivery.py:199-236 |
| The binding identity refuses blank or untrimmed fields and can be read back from a published report. | `CapsuleBindingIdentity`; `from_report` | mcp/src/agents_remember/serving/capsule_delivery.py:91-165; mcp/src/agents_remember/serving/capsule_delivery.py:117-136 |
| The compilation converter reads L2's frozen shapes structurally and copies the rendered stream verbatim. | `capsule_delivery_from`; `_seat_role` | mcp/src/agents_remember/serving/capsule_delivery.py:304-368; mcp/src/agents_remember/serving/capsule_delivery.py:287-301 |
| The refresh decision returns a supported boundary or an explicit refusal; a refusal yields no parameters. | `plan_refresh`; `thread_instruction_params` | mcp/src/agents_remember/serving/capsule_delivery.py:399-440; mcp/src/agents_remember/serving/capsule_delivery.py:443-457 |
| The legacy-chain switch is scoped to a capsule launch and names what the host actually loaded. | `legacy_instruction_switch`; `LegacyInstructionSwitch`; `LEGACY_PROJECT_DOC_KEY` | mcp/src/agents_remember/serving/capsule_delivery.py:500-531; mcp/src/agents_remember/serving/capsule_delivery.py:472-497; mcp/src/agents_remember/serving/capsule_delivery.py:460-470 |
| The seam consumes this value from the session settings, which the production factory fills. | `CodexAppServerSettings`; `create_harness_protocol_adapter` | mcp/src/agents_remember/serving/codex_app_server_session.py:73-119; mcp/src/agents_remember/serving/harness_control_factories.py:120-167 |
| The wire form travels the encoded launch configuration, emitted only when a capsule is present. | `control_runner_command`; `_optional_capsule_delivery` | mcp/src/agents_remember/serving/harness_control_runner.py:64-87; mcp/src/agents_remember/serving/harness_control_runner.py:120-133 |
| The frozen shapes this conversion depends on are asserted against the real landed types by this leaf's tests. | `test_the_frozen_shapes_this_conversion_depends_on`; `test_delivery_consumes_a_genuine_compilation_result` | mcp/tests/test_codex_capsule_delivery.py:448-482 |

## Cross-Repo References

The instruction-channel choice is pinned against the installed vendor app-server schema, captured as a
fixture rather than trusted from a recorded snapshot.

| Finding | Anchor | Source |
| --- | --- | --- |
| The instruction fields per thread-open request and the absence of a turn-level field are fixture evidence generated from the installed app-server. | `"instructionFields"` | mcp/tests/fixtures/codex_app_server_instruction_channels.json:4-22 |

## Update History

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: created onboarding for the capsule-delivery value
  type, the refresh decision and the legacy-chain switch, recording the three-channel authority
  boundary, the one-capsule-per-binding lifetime, the verbatim compiler bytes, absent-not-null on the
  wire, and the declared limits (unmeasured vendor resume effect, production-unexercised
  `FORK_THREAD`, unbounded payload). Verification metadata stays pinned to the last committed source
  (`c1dbebf8`) because this leaf's candidate is deliberately uncommitted; closeout stamps the real
  commit.
