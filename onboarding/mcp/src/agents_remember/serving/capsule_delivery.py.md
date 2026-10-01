# mcp/src/agents_remember/serving/capsule_delivery.py

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

## Evidence

### Docs References

No Domain Documentation entries are configured in the resolved source registry.

No configured live documentation source was available for this pass.

### Repo-Internal References

- The instruction parameter and the refresh-report key are named constants, chosen against the vendor's own base prompt. [1]
- The delivery value refuses an empty instruction stream and a non-`sha256:` digest at construction. [2]
- None [3]
- The binding identity refuses blank or untrimmed fields and can be read back from a published report. [4]
- The compilation converter reads L2's frozen shapes structurally and copies the rendered stream verbatim. [5]
- The refresh decision returns a supported boundary or an explicit refusal; a refusal yields no parameters. [6]
- The legacy-chain switch is scoped to a capsule launch and names what the host actually loaded. [7]
- The seam consumes this value from the session settings, which the production factory fills. [8]
- The wire form travels the encoded launch configuration, emitted only when a capsule is present. [9]
- The frozen shapes this conversion depends on are asserted against the real landed types by this leaf's tests. [10]

### Cross-Repo References

The instruction-channel choice is pinned against the installed vendor app-server schema, captured as a
fixture rather than trusted from a recorded snapshot.

- The instruction fields per thread-open request and the absence of a turn-level field are fixture evidence generated from the installed app-server. [11]
