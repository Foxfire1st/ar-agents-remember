# mcp/src/agents_remember/kernel/eve_runtime_readiness.py

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

## Evidence

### Docs References

No `Domain Documentation` category is configured for this repository, so no live domain-documentation
pass was available for this file. The Node version floor is a property of the pinned eve release and is
evidenced from the pinned runtime and its README rather than from a configured documentation registry.

No configured `Domain Documentation` source exists in `system/sources.md`; the Node floor is evidenced from the pinned runtime application, not from a documentation registry.

### Repo-Internal References

The probe is the registry's detection answer for eve, the registry is its only caller shape, and the
launch transport is the second reader of the floor it declares.

- The probe registers itself against the registry's eve probe name at import time and returns the registry-shaped `(ready, reason, locations)` tuple. [1]
- The verdict itself, in the order that makes the reason name the first real failure. [2]
- The application root resolves package data first, then the checkout, with the env override ahead of both. [3]
- The interpreter search order and the per-candidate rejection collection. [4]
- The central decision: a candidate is a runtime only when it exists, is executable, and reports a major at or above the floor. [5]
- The one floor with two readers — this declaration and the transport's import of the same object. [6]
- The registry seam the probe plugs into: the `eve` row carries `runtime_probe=EVE_RUNTIME_PROBE`, and detection consults the probe instead of PATH. [7]
- The cases drive both halves deterministically through the injectable `which`, including the below-floor, non-executable and missing-interpreter refusals. [8]
- The floor is asserted to be one number with two readers, so a second literal on the launch path fails a case rather than passing review. [9]

### Cross-Repo References

The runtime this probe looks for is not a sibling Agents Remember repository: it is the AR-owned Node
application under `eve_runtime/`, built on the pinned third-party `eve` package.

- The application markers this probe requires are the launcher's own predicate, and the pinned release is what fixes the Node floor. [10]
