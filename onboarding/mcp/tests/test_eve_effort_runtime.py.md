# mcp/tests/test_eve_effort_runtime.py

## Governing Overview

[mcp/tests overview](overview.md)

## Purpose

The effort axis, **executed**: the shipped application's own consumer, read at the provider boundary.
`CAPS-R17@v1` behaviour 1 asserts that `eve_runtime/agent/agent.ts` reads `AR_EVE_EFFORT` and applies it
through eve's own `defineAgent({ reasoning })`, so that a settings-selected level arrives at the
provider the runtime actually calls.

No Python case can observe that: the consumer is TypeScript inside the pinned application, and the
field under test is the request body a direct provider receives. So these three cases start the **real
runtime** with a complete verified capsule binding and read the body verbatim. The claim being
falsified is narrow and load-bearing, and this module exists so that the catalogue's advertisement
rests on a measurement rather than on documentation.

**Integration-marked** (`pytestmark = pytest.mark.integration`, 65), so the default unit selection
deselects it; its lane row is `integration` (`mcp/tests/test-evidence-lanes.toml:148`, with this
module's path at `:173`).

## Code Commentary

### Logic

Three native consumer cases in `EveEffortConsumerTests`, each starting its own application root and process:

| Case | What it proves |
| --- | --- |
| `test_every_advertised_level_is_the_body_the_provider_receives` (178) | **the whole accepted vocabulary, not an example**: for every `REASONING_EFFORTS` member except the sentinel, the recorded body must carry exactly that level. A level the menu advertises but the runtime cannot apply fails here. |
| `test_the_sentinel_sends_no_reasoning_key_at_all` (194) | `provider-default` means **no explicit reasoning**, so the key must be **absent** from the body — not present with the token, and not present as `null`. Asks `"reasoning_effort" not in request.body` directly, because the support module's `reasoning_effort` property collapses absent and null to `None`. |
| `test_the_model_the_selection_names_is_the_one_the_provider_receives` (206) | the **control** for the case above: the *same* runtime and the same body, so a case that passed on an empty or defaulted request rather than on the effort key would fail here. |

`_one_level` (the helper the three cases share) starts **one** configured level and returns what the
provider saw. Two properties make the measurement trustworthy rather than self-confirming, and both are
stated in the module docstring:

- the application root each case starts is the **checkout's own** `eve_runtime/agent` tree, linked into
  a scratch root by `staged_runtime_root` because `node_modules` is machine-local — and the staged copy
  is compared **byte for byte** against that tree before the assertion is read, plus the authored
  `agent.ts` is asserted to contain `AR_EVE_EFFORT`, so the case cannot pass against a reduced
  application written for it;
- **one application root and one process per case.** The authored definition is read when the runtime
  boots, so a shared root would measure the previous case's source — a failure mode observed while
  building this measurement and invisible in a summary table.

`_admitted_workspace` (80) builds a real git worktree on an admitted branch with a carrier through the
capsule seam's own fixture support: the runtime refuses every session route without a complete verified
binding, so this is what makes the cases observe the **production** consumer rather than a stub. Only
the transport's peer is a recording server.

`_node_executable` (166) skips by name when this host has no Node at or above the floor;
`require_installed_eve_application` (called first in `_one_level`) skips by name when the machine-local
`eve_runtime/node_modules` install is absent. Both are named skips, never retries.

The module also tests the isolated startup owner without the Eve dependency. A controlled base
startup proves retry only after an observed bind collision and propagation of other failures.
Cancellation and RuntimeError are injected after an actual local child, HTTP client and stderr reader
exist, then assert reaping, client closure, reader completion and original failure propagation with
no port retry. These local resource checks do not claim the native effort consumer executed.

### Conventions

- The provider is the support module's **recording HTTP server**, deliberately **not** the product's
  deterministic fixture model: the fixture traces a normalized projection of the request, and a
  projection is exactly what must not be trusted when the request body is the value under test.
- The module asserts its own premises before reading a verdict — the staged copy equals the authored
  tree, and the authored source contains the consumer — so a green case cannot come from measuring the
  wrong bytes.
- `START_TIMEOUT_SECONDS` (240) and `CALL_TIMEOUT_SECONDS` (120) are generous because a real hermetic
  Node application boots and compiles per case; the poll loop has a deadline rather than a fixed sleep.

### Invariants And Boundaries

- **One level, one root, one process.** Sharing an application root across levels would measure the
  source the first boot compiled, so a case that reuses a root is measuring the wrong thing even when
  it is green.
- **The staged bytes must be the repository's own.** The byte comparison against the authored tree is
  what keeps the measurement about this repository's shipped application; a copy or a reduction would
  make the claim vacuous.
- **The absence of the key is asserted on the body, not on the convenience property.** For the sentinel
  the distinction between "not sent" and "sent as `null`" is the rule being pinned.
- **This module proves the launch *preparation* and the runtime's own request, not the whole dispatch
  chain.** It resolves a spec through `resolve_runtime_spec` with a real binding and starts
  the test-owned `IsolatedEveRuntimeProcess` directly; the runner **process** hop (tmux → runner → adapter) is exercised by the
  settings-chain evidence, not here. Read the two together before claiming an end-to-end seat launch.
- The cases need a machine-local install and a Node at or above the floor; without them they **skip by
  name**, so a green run on a bare checkout is not coverage of this consumer.

### Todos

None known.

## Evidence

### Docs References

No Domain Documentation source is configured for this repository, so no live domain-documentation pass
was available for this module.

No configured `Domain Documentation` source; the external authority the consumer is written against is eve's own published `defineAgent`/reasoning typing, reached through the pinned package rather than a specification in this repository.

### Repo-Internal References

- The vocabulary the cases iterate and the sentinel they single out — the adapter's one declaration, which the launch gate validates against and the catalogue publishes. [1]
- The real runtime process the cases start, and the launch environment the selected level is carried into. [2]
- The recording provider boundary and the staged application root, which are what make the body the evidence. [3]
- The complete verified capsule binding the runtime refuses to start without, built through the capsule seam's own fixture support. [4]
- The consumer under measurement: the authored application reads the effort input and applies it through eve's own definition, omitting the property for the sentinel. [5]
- The catalogue whose advertisement rests on this measurement, and the case that reads the axis off the serialized envelope. [6]
- The sentinel rule in its other form, which the provider boundary cannot observe and so is pinned as an authored source shape. [7]
- The module's own lane row, which the fail-closed loader requires. [8]

- Only observed bind collisions cause a retry; other startup failures propagate. [10]
- Actual child, client and stderr cleanup precede cancellation or runtime-error propagation. [11]

### Cross-Repo References

The controlled application is the pinned published `eve` package started as a real Node process; it is
a dependency rather than a sibling Agents Remember repository.

- The pinned runtime the cases start, the exact dependency pins, and the machine-local install command that the README documents and the guard enforces. [9]
