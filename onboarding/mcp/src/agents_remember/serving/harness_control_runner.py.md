# mcp/src/agents_remember/serving/harness_control_runner.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/serving/harness_control_runner.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T14:15+02:00 |
| lastVerifiedCommitHash | `621db8981aba09a6f17880d2138cf76a37332c6c` |
| lastVerifiedCommitDate | 2026-09-17T15:54:01+02:00|
| reviewedWorkingCandidate | `ar/260915-caps-l11-ar` uncommitted source; base `a29a20c6eefea424a7e0321a54fcda2ed1b35098` |
| governingOverview | `overview.md` |

## Governing Overview

[serving/ overview](overview.md)

## Purpose

Process entrypoint for one hosted native harness session. It carries the typed settings-resolved
launch across the tmux process boundary, performs token-free discovery and fail-loud validation,
starts the configured adapter, and keeps exact startup failure evidence available over local IPC.
260718-CHATS-L0E adds the additive codex `resume_thread_id` channel through the same runner
payload, and 260915-CAPS-L5 adds the optional **capsule carrier** that travels the same encoded
payload — emitted only when a capsule is present, so a capsule-free launch is byte-identical to the
payload it always sent.

## Code Commentary

### Logic

`RunnerConfig` serializes exact control identity, harness, cwd, base argv, endpoint root, explicit
session commands, and optional `ResolvedLaunch`. Decode verifies that the typed launch names the
same harness and workspace. `_prepare_controlled_launch` builds the unconfigured native
`LaunchSpec`, asks a transient adapter for its native knobs, applies conflict preflight before any
discovery process, enumerates the dynamic catalog without a prompt, validates model and model-local
launch effort, then builds a fresh runtime adapter carrying expected-launch evidence. Selectionless
sessions still allow the native catalog default; L4 roleless daemon opens can now carry the same
complete typed selection as role-based spawn.

L0E adds `RunnerConfig.resume_thread_id`, serialized as the additive `"resumeThreadId"` payload
key. Parse validation requires non-empty trimmed text or null; a legacy payload without the key
parses unchanged to `None`. The value rides into both real adapter-construction sites (the
selectionless path and the configured path) as the factory's codex-only kwarg — never into the
transient discoverer — and the factory refuses a non-codex harness or a malformed value before any
spawn. The runner does not validate or authorize the resume target; it is a native-identity
selector in the same authority class as verbatim `launch_args`.

**CAPS-L5 adds `RunnerConfig.capsule_delivery`,** the launch configuration's half of the one optional
carrier (`TerminalLaunchRequest.control.capsule_delivery` → here → the payload key → parse → both
factory calls → the adapter's settings). `control_runner_command` merges
`{"capsuleDelivery": config.capsule_delivery.to_json()}` **only when the carrier is not `None`**;
`_optional_capsule_delivery` reads it back and raises `HarnessControlError` on a present-but-unreadable
value. Both factory calls inside `_prepare_controlled_launch` — the no-selection path and the resolved
path — pass it through, so neither branch can silently drop it. The resolved path now passes its
selection as one `LaunchSelection` pair instead of two parameters (see the factories card).

`run_controlled_session` starts IPC before adapter startup. Any discovery, validation, conflict, or
vendor-start exception becomes the bridge's persistent failed snapshot. Session commands are sent
only after ready. A failed runner stays addressable and reads terminal input instead of exiting, so
readiness/daemon consumers can retrieve `control=failed`, `acceptance=rejected`, and the exact
`raw.bridgeError`. Codex argv conversion is exposed as `adapter_argv(harness_id, argv)` so hosted
launch and L4 pre-session discovery share the exact native process boundary. It adds `app-server`
while retaining every supplied argument so duplicate authority is refused, never silently deleted.

### Conventions

The typed payload is URL-safe base64 JSON because tmux launches this module as a fixed argv command.
Native selection ordering is preflight → discover → validate → runtime construction/start. The broad
exception catches at the subprocess/IPC boundary preserve exact external failures; they do not
retry, default, or continue the vendor launch.

### Invariants And Boundaries

- No configured real vendor session starts before token-free catalog validation succeeds.
- Adapter-owned selector conflicts fail before even transient discovery starts.
- Session commands and terminal input cannot run until the bridge is ready.
- Launch failure remains observable over the exact private endpoint; it is not collapsed into a
  generic process disconnect.
- Model/effort is never delivered through composer paste or synthesized session commands.
- The terminal catalog/tmux row may precede asynchronous discovery by design; the vendor session
  does not.
- `resumeThreadId` is additive: absent preserves legacy parse/dispatch behavior exactly, malformed
  shapes fail before construction, and the transient discovery adapter never receives it.
- **`capsuleDelivery` is emitted only when a capsule is present.** The key is added conditionally, so
  the capsule-free payload keeps exactly its eight legacy keys and is **byte-identical to base** —
  measured, not asserted: the base and candidate modules produce the same encoded token (344 chars,
  same sha256). An earlier draft emitted `"capsuleDelivery": null` and was merely equal-shaped; the
  omission is the invariant, and a future editor must not make the key unconditional.
- **A malformed capsule payload refuses.** `_optional_capsule_delivery` raises rather than returning a
  capsule-free configuration: a caller that supplied a capsule must never receive a capsule-free
  process.
- **Neither factory call may drop the carrier.** Both call sites in `_prepare_controlled_launch` pass
  `capsule_delivery=config.capsule_delivery`; removing either one is a seed the leaf's suite catches.

### Todos

None known for the runner boundary. **D12's bound is now stated and enforced here** — see the
`260915-CAPS-L11` section below: the payload no longer rides argv unbounded.

## Repo-Internal References

Launch validation and adapter construction remain separate pure/data and vendor-specific seams.

| Finding | Anchor | Source |
| --- | --- | --- |
| Launch selection, validation, effective echo checks, knob application, and duplicate-selector preflight are centralized in the launch module. | `ResolvedLaunch`; `validate_launch_selection`; `verify_effective_launch`; `apply_launch_knobs`; `_owned_argv_overrides` | mcp/src/agents_remember/serving/harness_launch.py:17-54; mcp/src/agents_remember/serving/harness_launch.py:78-119; mcp/src/agents_remember/serving/harness_launch.py:122-148; mcp/src/agents_remember/serving/harness_launch.py:173-206; mcp/src/agents_remember/serving/harness_launch.py:233-250 |
| The factory pairs a typed selection with adapter-produced knobs and ignores ambient role env as authority. | `create_harness_protocol_adapter` | mcp/src/agents_remember/serving/harness_control_factories.py:120-162 |
| The opener embeds the typed launch in this runner command and persists model/effort provenance on the terminal row. | `_session_command`; `_opened_catalog_entry` | mcp/src/agents_remember/serving/terminal_opener.py:534-568; mcp/src/agents_remember/serving/terminal_opener.py:571-636 |
| The bridge translates `mark_failed` into failed/rejected state with exact raw error evidence (`raw["bridgeError"]`), refusing to overwrite an already-started bridge. | `mark_failed` | mcp/src/agents_remember/serving/harness_control_bridge.py:164-178 |
| The pre-session catalog reuses `adapter_argv` before calling the transient adapter's token-free discovery path. | "argv=adapter_argv(installed.harness.id" | mcp/src/agents_remember/serving/harness_capability_catalog.py:205-212 |

## 260731-EFA-L2 Current Delta

The runner payload decoder was split into named checks, each stating the contract it enforces:

- `_decode_runner_payload(encoded)` — decode the base64url argv token the opener hands the runner
  into its JSON object.
- `_is_text_list(value)` — a `TypeGuard` for the only argv shape accepted: a list whose every entry
  is non-empty text.
- `_optional_resume_thread_id(raw)` — `resumeThreadId` is additive, so an absent or null field stays
  a legal payload.
- `_require_launch_agrees_with_config(config)` — refuse a payload whose settings-owned selection
  contradicts the session it launches.

The refusals and the launch sequence are unchanged.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## 260915-CAPS-L5 The Capsule Carrier On The Runner Payload

The capsule travels the **existing** runner payload; no protocol, process or ordering was added. The
whole chain is:

```
TerminalLaunchRequest.control.capsule_delivery      (the launch boundary)
  -> RunnerConfig.capsule_delivery                  (the launch configuration)
  -> payload key "capsuleDelivery"                  (ONLY when a capsule is present)
  -> parse_runner_config -> _optional_capsule_delivery
  -> _prepare_controlled_launch -> both factory calls
  -> CodexAppServerSettings.capsule_delivery
```

Two properties are load-bearing and must not be broken by a later edit:

1. **The capsule-free wire is byte-identical to base.** The added key is *omitted*, not null, so a
   legacy launch sends exactly the payload it always sent. This was re-measured by running the base
   module and the candidate module in separate interpreters and comparing the encoded token: same
   eight keys, 344 chars, same sha256, empty `diff`.
2. **A present-but-unreadable value refuses.** `_optional_capsule_delivery` raises
   `HarnessControlError("hosted control runner received a malformed capsule delivery")`; a silent drop
   would hand a capsule-requesting caller a capsule-free process, which is the worst outcome this
   boundary can produce.

The carrier is serialized by the value's own `to_json`/`from_json` (`serving/capsule_delivery.py`), so
the runner never re-derives or re-renders the instruction stream. The resolved-selection factory call
now passes `LaunchSelection(resolved_launch=…, launch_knobs=…)` — a mechanical pairing, not a
behaviour change (see the factories card for why it exists).

## 260915-CAPS-L11 D12's Bound, Stated And Enforced Before Encoding

**The mechanism.** The whole launch configuration travels as **one base64 token** (`argv[3]`), so
the kernel limit that binds this path is `MAX_ARG_STRLEN` — the limit on **one** `execve` argument
— not `ARG_MAX`, which bounds argv and environment together. Past it `execve` fails with `E2BIG`
**at spawn**, before this process can report anything, which is why the check lives here where the
encoded bytes first exist.

Three module constants state it, and one function enforces it:

| Symbol | Value | What it is |
| --- | --- | --- |
| `MAX_ARGV_TOKEN_BYTES` | `131072` | Linux `MAX_ARG_STRLEN`, the kernel limit on one argument |
| `ARGV_TOKEN_SAFETY_MARGIN_BYTES` | `2048` | the declared margin held under the kernel limit |
| `ARGV_TOKEN_BOUND_BYTES` | `129024` | the enforced bound = limit − margin |
| `_refuse_over_bound_token` | — | refuses an over-bound token by name, before any spawn |

**The margin is small on purpose.** The check measures the same byte string the kernel counts, so
the margin does not absorb an approximation; it exists so a token at the boundary is refused *here*
rather than by the kernel at spawn. A larger margin would refuse capsules the kernel accepts.

**The refusal names the measured size, the bound, the kernel limit it is derived from, and the seat
the capsule was compiled for.** That is deliberate: "the session did not start" is not an operator
message, and `E2BIG` at spawn is otherwise AR-invisible and indistinguishable from a runtime that
crashed on start. The bound is **enforced, not advisory** — the builder refuses by name at a
`PATH_MAX` cwd.

**Current measured width of the largest shipped pair** (`orchestrator/authorized-closeout`, measured
by L11 at production shape with the shipped builder): **126,096 B** with the settings-resolved launch
selection a real launch always carries (2,928 B under the bound; 126,164 B fully production-shaped;
**126,352 B** at the widest realistic shape, where an eve carrier binds the admitted worktree to a
102-character cwd — 2,672 B under the bound). **The measurement is a report figure, not a
guarantee**: at `~96 %` of the limit the margin is thin, and the route to the bound is a **path
length** as much as a capsule — the token grows ~**1.3320 encoded bytes per `cwd` character**
(that ratio is the base64 4/3 expansion, so it is the encoding's property rather than this capsule's)
and the bound is first crossed at a cwd ~2,297 characters longer than the server workspace root.
**Any pair measured over `129024` is a bound re-derivation that stops the loop, never a silent
re-bound.**

## Update History

- 2026-09-17T15:54+02:00 — 260915-CAPS-L11 curator (**final-verification leaf**): replaced the
  **stale forward-routing note** in `Todos` — which still said the bound "is routed to the
  final-verification leaf (`D12`), not to this seam" and quoted L15's superseded **120,536 chars /
  92.0 %** — with the delivered contract: `MAX_ARGV_TOKEN_BYTES` 131072, `ARGV_TOKEN_SAFETY_MARGIN_BYTES`
  2048, `ARGV_TOKEN_BOUND_BYTES` **129024**, and `_refuse_over_bound_token` refusing **before any
  spawn**. Recorded why the margin is small (the check measures the bytes the kernel counts) and what
  the refusal names (measured size, bound, kernel limit, seat) — the operator-visibility reason D12
  exists. Carried L11's own measured width for the largest pair and the two limit facts the leaf
  established: the bound is **enforced** (refused by name at a `PATH_MAX` cwd), and the route to it is
  a **path length** as much as a capsule (~1.3320 encoded bytes per `cwd` character — the base64 4/3
  expansion — first crossing at ~2,297 characters beyond the server workspace, so a headroom figure
  is only meaningful with its inputs named). Range repairs: `create_harness_protocol_adapter`
  48-90 → **120-162** (moved by an earlier leaf, not by this one), the catalog row 180-195 →
  **205-212**, and the catalog claim re-worded so its anchor lives inside its own range.
  Verification metadata stays pinned at the last committed source; the closeout stamps the real
  code commit.

- 2026-09-16T14:15+02:00 — 260915-CAPS-L5 curator: recorded the optional capsule carrier on the runner
  payload — `RunnerConfig.capsule_delivery`, the **conditional** `capsuleDelivery` key that keeps the
  capsule-free payload byte-identical to base (measured: 344 chars, same token sha256), the refusing
  decoder, and both factory call sites that must keep passing it. Added the payload-bound limit
  (`D12`: largest shipped capsule 120,536 chars = 92.0 % of `MAX_ARG_STRLEN`, ~10 KB headroom,
  invisible `E2BIG` at spawn) as a declared limit routed to the final-verification leaf. Repaired two
  stale cross-file ranges (`_opened_catalog_entry`, `mark_failed`) and joined a table split by a blank
  line. Verification metadata stays pinned to the last committed source (`c1dbebf8`).

- 2026-08-08T17:18+02:00 — No content impact: 260731-EFA-L9 rewrote this source's imports/callers only (model-extraction caller wave); the behavior this card documents is unchanged and the body was re-verified current. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-04T11:39+02:00 — 260731-EFA-L6 S18-B13 curator: split launch, factory, opener, and contract-test ownership and normalized scoped citation evidence.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation. `HarnessControlBridge.mark_failed` is a single contiguous method at L170-L184 in the 623-line `harness_control_bridge.py`, so the two-range citation collapsed to one; extended the claim to name `raw["bridgeError"]` and the already-started refusal, both read back at L174 and L181.
- 2026-07-31T16:10+02:00 — 260731-EFA-L2 curator: recorded the named payload-decode and launch-agreement checks; refusals unchanged.
- 2026-07-19T09:15+02:00 — 260718-CHATS-L0E curator: documented the additive `resumeThreadId`
  payload field — trimmed-non-empty parse validation, legacy field-less compatibility, and delivery
  into both real adapter-construction sites as the codex-only factory kwarg while the transient
  discoverer never receives it. Verification metadata stays pinned until closeout stamps the
  candidate commit.
- 2026-07-16T06:15+02:00 — 260714-ACPUI-L4 curator: documented the shared native argv helper
  used by hosted launch and token-free pre-session discovery, plus roleless complete-pair launch
  flowing through the existing runner boundary.
- 2026-07-15T23:00+02:00 — 260714-ACPUI-L2 curator: documented typed launch serialization,
  pre-discovery selector conflict refusal, token-free dynamic validation, fresh configured runtime
  construction, ready-only session commands, and persistent exact launch-failure IPC evidence.
- 2026-07-14T13:59+02:00 — 260713-PHA-L5: documented bridge-owned hosted launch, exact identity,
  correlated commands, transcript rendering, and shutdown.
