# mcp/src/agents_remember/kernel/eve_runtime_readiness.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/eve_runtime_readiness.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T13:26+02:00 |
| lastVerifiedCommitHash | `997305a9ced4caea67edb826224bf0351264fd56` |
| lastVerifiedCommitDate | 2026-09-17T19:54:27+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[MCP package overview](../../../overview.md)

## Purpose

Answers the one question the harness registry has to ask about eve: **would launching this harness
reach a real runtime, or would it fail** — and names the component that is missing when the answer is
no.

It exists because eve is not a PATH TUI. Its runtime is an AR-owned Node application that the session
adapter spawns itself, so `shutil.which("eve")` can only ever answer "no" and would report a present
runtime as a generic not-installed harness. The probe replaces that PATH question with the real
readiness predicate, and it does so in the `kernel` layer — which owns the harness vocabulary — while
the `serving` transport that actually execs node keeps owning the spawn.

Two readiness inputs, both required: the **application root** must exist and carry the two files that
make a directory an eve application, and a **Node interpreter** must be present, executable and at
least `MINIMUM_NODE_MAJOR`.

## Code Commentary

### Logic

`eve_runtime_readiness()` is the whole verdict, and it is ordered so the reason names the first thing
that is actually wrong:

1. `_resolve_application()` resolves the application root, **package data first, then the checkout** —
   the same order `serving.eve_runtime_launch` resolves it — with `AR_EVE_RUNTIME_ROOT` as the explicit
   override. A missing root returns immediately with the tried locations joined into the sentence;
   the node question is never asked, because a missing application is the more specific failure.
2. `_resolve_node()` then resolves an interpreter, and its search order mirrors the transport's:
   an explicit `AR_EVE_NODE`, then nvm runtimes under `~/.nvm/versions/node` (newest major first),
   then `PATH`.
3. Every candidate — declared, nvm or PATH — goes through the same `_usable_interpreter()` check, and
   every rejection is collected with its own reason rather than collapsed into one.

`_usable_interpreter()` is where the module's central decision lives. It asks the interpreter itself
for its version with one bounded `subprocess.run([path, "--version"], timeout=NODE_VERSION_TIMEOUT_SECONDS)`
and parses the major with `_NODE_MAJOR_PATTERN`. The docstring states the principle: *the version is
asked of the interpreter itself, which is the only authority on it; an interpreter that cannot be run
at all is unusable by definition, not a version question.* `_unusable_reason()` therefore runs first
and separates the three structural refusals — does not exist, is not a file, is not executable — from
the version question.

The three-part return travels through `eve_runtime_probe()`, which reshapes `RuntimeReadiness` into the
`(ready, reason, locations)` tuple the registry protocol expects and registers itself against
`EVE_RUNTIME_PROBE` at import time via `@register_runtime_probe`.

Readiness is **read-only in the sense that matters**: it creates nothing, mutates nothing and leaves no
state behind. It is not free of execution — one `node --version` per candidate is a real process — and
that cost is why the probe is bounded rather than open-ended.

### Conventions

- Every user-facing sentence is assembled from the values actually observed, so a diagnostic can be
  read back as the operator's next action (which path was tried, which interpreter was rejected and
  why).
- `_checkout_root()` walks **up** through `Path(__file__).resolve().parents` looking for a sibling
  `eve_runtime` directory. It never counts path levels, so moving this module cannot silently break
  resolution.
- `_packaged_application()` returns `None` rather than raising when `importlib.resources` cannot
  produce a real directory; the checkout path is then tried.
- The `which` lookup is injectable and threaded through from the registry, so a test can drive both
  halves of the verdict deterministically.
- `__all__` exports exactly `RuntimeReadiness`, `eve_runtime_probe` and `eve_runtime_readiness`.

### Invariants And Boundaries

- **`MINIMUM_NODE_MAJOR` is declared here and read from here.** The transport imports it
  (`serving/eve_runtime_launch.py` binds it as `KERNEL_MINIMUM_NODE_MAJOR` and re-exports the same
  object as its own `MINIMUM_NODE_MAJOR`), so the floor is one number with two readers and the two
  cannot drift. A second literal `24` anywhere on the launch path is a regression against this
  ownership.
- **A declaration is not a runtime.** An `AR_EVE_NODE` path that does not exist, is not executable, or
  is older than the floor is refused. Accepting a declared path on trust would advertise the harness on
  a box where every launch must fail — the false affordance this seam exists to remove.
- **A ready verdict without the application root is a lie the launcher would discover one process
  late.** Both halves are required; neither alone produces `ready=True`.
- **The probe decides detection, not launch.** The transport still applies its own launch-time
  resolution, and a declared override reaches the child verbatim — which is where a bad path fails
  loudly if some other caller reaches a launch without consulting this probe.
- This module owns no argv, no spawn and no launch policy; it answers a question and stops.

### Todos

None known. The packaged-runtime path (`PACKAGED_RUNTIME_PATH`) is written but unexercised until the
runtime is actually shipped as package data — that packaging is another leaf's scope, and the branch
here is covered by the missing-directory case.

## Docs References

No `Domain Documentation` category is configured for this repository, so no live domain-documentation
pass was available for this file. The Node version floor is a property of the pinned eve release and is
evidenced from the pinned runtime and its README rather than from a configured documentation registry.

| Finding | Anchor | Source |
| --- | --- | --- |
| No configured `Domain Documentation` source exists in `system/sources.md`; the Node floor is evidenced from the pinned runtime application, not from a documentation registry. | — | — |

## Repo-Internal References

The probe is the registry's detection answer for eve, the registry is its only caller shape, and the
launch transport is the second reader of the floor it declares.

| Finding | Anchor | Source |
| --- | --- | --- |
| The probe registers itself against the registry's eve probe name at import time and returns the registry-shaped `(ready, reason, locations)` tuple. | `eve_runtime_probe` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:77-86 |
| The verdict itself, in the order that makes the reason name the first real failure. | `eve_runtime_readiness` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:89-128 |
| The application root resolves package data first, then the checkout, with the env override ahead of both. | `_resolve_application`; `_packaged_application`; `_checkout_root`; `_is_application` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:131-150; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:153-162; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:165-171; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:174-175 |
| The interpreter search order and the per-candidate rejection collection. | `_resolve_node`; `_NodeVerdict` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:178-183; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:186-216 |
| The central decision: a candidate is a runtime only when it exists, is executable, and reports a major at or above the floor. | `_usable_interpreter`; `_unusable_reason`; `_reported_major_version`; `NODE_VERSION_TIMEOUT_SECONDS` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:62-62; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:219-235; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:238-247; mcp/src/agents_remember/kernel/eve_runtime_readiness.py:250-264 |
| The one floor with two readers — this declaration and the transport's import of the same object. | `MINIMUM_NODE_MAJOR` | mcp/src/agents_remember/kernel/eve_runtime_readiness.py:55-55; mcp/src/agents_remember/serving/eve_runtime_launch.py:48-48 |
| The registry seam the probe plugs into: the `eve` row carries `runtime_probe=EVE_RUNTIME_PROBE`, and detection consults the probe instead of PATH. | `EVE_RUNTIME_PROBE`; `register_runtime_probe`; `load_runtime_probes`; `is_harness_available`; `harness_availability_detail`; `harness_runtime_verdict` | mcp/src/agents_remember/kernel/harnesses.py:50-57; mcp/src/agents_remember/kernel/harnesses.py:60-68; mcp/src/agents_remember/kernel/harnesses.py:71-79; mcp/src/agents_remember/kernel/harnesses.py:82-103; mcp/src/agents_remember/kernel/harnesses.py:106-139; mcp/src/agents_remember/kernel/harnesses.py:144-144 |
| The cases drive both halves deterministically through the injectable `which`, including the below-floor, non-executable and missing-interpreter refusals. | `EveReadinessProbeTests` | mcp/tests/test_eve_product_integration.py:710-816 |
| The floor is asserted to be one number with two readers, so a second literal on the launch path fails a case rather than passing review. | `test_the_required_major_is_one_number_with_two_readers` | mcp/tests/test_eve_product_integration.py:810-816 |

## Cross-Repo References

The runtime this probe looks for is not a sibling Agents Remember repository: it is the AR-owned Node
application under `eve_runtime/`, built on the pinned third-party `eve` package.

| Finding | Anchor | Source |
| --- | --- | --- |
| The application markers this probe requires are the launcher's own predicate, and the pinned release is what fixes the Node floor. | `engines`; `dependencies` | eve_runtime/package.json:7-8; eve_runtime/package.json:15-20; eve_runtime/README.md:10-22 |

## Update History

- 2026-09-17T19:30+02:00 — 260915-CAPS-L20 curator: **both governing declarations repaired.** The field named `../../overview.md` and the body link named `../../overview.md`; each resolved card-relatively to nothing, and they did not agree with each other. Both now name `../../../overview.md`, the route-local overview of this card's own directory. Recorded under `260915-CAPS-L20` as this leaf's **S3** (D3, the packaged `l-01-agent-lifecycles` family) and **S4** (D16, govern-or-remove per card). The checker that previously reported this corpus clean now resolves both declarations, so this card reaches the curator's gated repair set instead of passing silently; that is the gap this leaf closed. Superseded history entries above stand unedited — including any entry that asserted an earlier repair this card did not in fact carry, which is the finding rather than an error to erase. No prose, anchor, range or verification stamp was otherwise changed.
- 2026-09-16T13:26+02:00 — 260915-CAPS-L8 curator: created this card for a file added by the eve
  product-integration change set. Records the readiness predicate (application root plus a usable Node
  at or above the floor), the order that makes a refusal name the first real failure, the bounded
  `<node> --version` execution that makes version viability a measurement rather than an assumption,
  the refusal of a declared-but-unusable `AR_EVE_NODE`, and the one-floor-two-readers ownership of
  `MINIMUM_NODE_MAJOR`. Verification metadata is pinned to the leaf's synced base commit `ff97072c`
  because the candidate is deliberately uncommitted — the governed closeout stamps the real code
  commit, and no hash or fingerprint was invented here.
