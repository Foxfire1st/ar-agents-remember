# mcp/src/agents_remember/kernel/harnesses.py

| Field | Value |
| --- | --- |
| repository | agents-remember |
| path | `mcp/src/agents_remember/kernel/harnesses.py` |
| doc_type | `file-level-onboarding` |
| lastUpdated | 2026-09-16T10:15+02:00 |
| lastVerifiedCommitHash | `609756111eb3c239d0563d8631bfd564645bc9d1` |
| lastVerifiedCommitDate | 2026-09-16T10:25:13+02:00|
| governingOverview | `../../../overview.md` |

## Governing Overview

[overview](../../../overview.md)

## Purpose

The harness vocabulary: what a harness IS, and the curated set of them. `HARNESSES` is the
developer-curated **max set** of native harnesses AR supports, and its docstring is the authoritative
statement of who may extend it.

## Code Commentary

### Logic

Module-level surface:

- `Harness` (class, lines 32-60) — One supported TUI harness: a stable ``id``, a display ``name``, the ``command`` to detect on
- `HARNESSES` (tuple, lines 63-84) — the curated rows: `claude`, `codex`, `pi`, followed by the docstring that owns the "who may add a row" rule.

The `HARNESSES` docstring states, as of 260915-CAPS-L6, that a **native `eve` protocol adapter exists
(`serving/eve_adapter.py`) and is registered in `harness_control_factories`, but deliberately has no
row here**: its runtime is an AR-owned application rather than a `PATH` command, so exposing it as a
launchable terminal harness is the capability-catalog/packaging leaf's decision, not the adapter's.

### Conventions

Module-level definitions follow the package conventions; names prefixed with `_` are private to this module.

### Invariants And Boundaries

- The card mirrors the source file one-to-one at `mcp/src/...` path.
- **A protocol adapter's existence does not earn a row here.** The two registries answer different
  questions — `HARNESSES` is "which `PATH`-detectable terminal harnesses does the developer support",
  while `serving/harness_control_factories.BUILTIN_PROTOCOL_HARNESSES` is "which ids can construct a
  hosted protocol adapter". Until a deliberate row is added, an `eve` harness id resolves through the
  protocol factory only and never through terminal launch, and no code path may imply otherwise.
- The set is developer-curated: extending it is a product decision with a named owner, not an
  implementation detail a leaf may settle incidentally.

### Todos

The capability-catalog/packaging leaf decides whether an `eve` row is ever added here; the packaging
of the runtime into `package_data/runtime/eve-agent` is the same leaf's scope.

## Repo-Internal References

This module defines the top-level symbols cited below; each row points at the exact source range holding the anchor.

| Finding | Anchor | Source |
| --- | --- | --- |
| Defines the class `Harness` (lines 32-60) — One supported TUI harness: a stable ``id``, a display ``name``, the ``command`` to detect on. | `Harness` | mcp/src/agents_remember/kernel/harnesses.py:31-60 |
| The curated set and its ownership docstring, which names the eve exclusion explicitly. | `HARNESSES`; "deliberately has no row here yet" | mcp/src/agents_remember/kernel/harnesses.py:63-85 |
| The separate protocol-adapter registry that an `eve` id actually resolves through. | `BUILTIN_PROTOCOL_HARNESSES`; `create_harness_protocol_adapter` | mcp/src/agents_remember/serving/harness_control_factories.py:33-103 |

## Update History

- 2026-09-16T10:15+02:00 — 260915-CAPS-L6 curator (A2 delta pass): **No content impact from the A2
  revision.** This file is byte-identical between the A1 and A2 candidates of the same change set, so
  the body — the `HARNESSES` docstring's record of why the native eve protocol adapter deliberately
  has no row here — is retained unchanged. The pass advanced the verification metadata to the leaf's
  current base `e9300687` under the leaf's one consistent convention (the candidate is uncommitted, so
  the governed closeout re-stamps the real code commit) and re-read the existing citations, which
  remain in the required `Finding | Anchor | Source` shape. No hash or fingerprint was invented.

- 2026-09-16T09:00+02:00 — 260915-CAPS-L6 curator: the curated set is unchanged (still `claude`,
  `codex`, `pi`) and this file's **only** delta is the `HARNESSES` docstring, which now records why
  the new native eve protocol adapter deliberately has no row here: eve's runtime is an AR-owned
  application, not a `PATH` command, so terminal-harness exposure is the packaging/capability leaf's
  decision. Body updated to state that boundary as an invariant rather than leaving the card silent
  about a registry that now contains an adapter with no row. Verification metadata pinned until
  closeout stamps the candidate commit.

- 2026-08-05T00:00+02:00 — 260731-EFA-L6 closeout pass: created this file-level onboarding card for the new source file; anchors and ranges derived from the current worktree source. Verification metadata pinned until closeout stamps the code commit.
