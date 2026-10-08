# mcp/src/agents_remember/application/runtime/ — Runtime Application Operations

| Field | Value |
| --- | --- |
| sourceRoute | `mcp/src/agents_remember/application/runtime/` |

## Governing Overview

[application overview](../overview.md)

## Hot Path Summary

Use `startup.py` for trusted MCP process preparation, application collaborators, and the typed
serving-build gateway used by MCP registration; use `install.py` for runtime-install delegation
and `skills.py` for packaged skill deployment.

## What Belongs Here

Focused application entry points that bind runtime configuration to startup, runtime installation,
or skill installation. Provider, benchmark, worktree, memory, and task operations remain in their
own application modules.

## Operating Model

Startup declares process trust before configuration-backed authority is used, migrates the
MCP-owned durable logs, installs ambient lifecycle state, exposes the cached serving-build as a
strict wire payload to the higher-ranked MCP adapter, and optionally starts dashboard supervision.
Installation modules remain thin translations into their service owners.

## Local Invariants And Traps

- Do not introduce a package-level mega-facade or import-time process mutation.
- Keep live coordination ownership separate from the dashboard-owned notifier log.
- MCP adapters do not import serving-domain owners directly; startup owns that application seam.
- Runtime and skill install entry points accept typed config/options; they do not accept arbitrary
  host roots that bypass resolved settings.

## File-Level Onboarding Map

- [`__init__.py.md`](__init__.py.md) — side-effect-free package marker.
- [`install.py.md`](install.py.md) — runtime installation application entry point.
- [`skills.py.md`](skills.py.md) — skill installation application entry point.
- [`startup.py.md`](startup.py.md) — MCP process trust, migration, ambient state, and supervision.

## Child Overviews

None.

## Evidence

### Repo-Internal References

- Startup owns MCP process declaration, collaborator installation, and the serving-build payload gateway. [1]
- Runtime installation composes the lower service result with the public host step at the application entry. [2]
- Skill installation resolves the configured harness skill root and delegates the copy. [3]

### Docs References

No Domain Documentation source is configured.

### Cross-Repo References

No cross-repository implementation dependency governs this route.

## How To Use This Area

Start from the operation-specific sidecar, then follow its service-layer references for mechanics.
Keep MCP payload/registration concerns at their own routes.

## 260915-KS-L23 The Route Now Says Which Build Measured

`startup.py` gained the one function that makes every measurement in this master's tool surface
attributable: **`measuring_build_stamp()`** (`startup.py:36`). It reports the build a caller is
actually executing — `version`, `bootedAt`, `sourceDigest`, `pythonExecutable`, `packageRoot`,
`commit` and `dirty` — and it exists because of **D-33**: the MCP tool surface executes a *fixed
serving build*, not the candidate's own code, so a `memory_quality_check` or `citation_fix` count
produced during a leaf could not be told apart from a count produced by the leaf's own tree. The
stamp is now carried by the memory-quality and citation responses, which is what lets a reader name
the ruler for any count instead of assuming it.

The two rulers this route's own stamp distinguishes, measured 2026-09-18 by the leaf's curator:

| Ruler | `packageRoot` | `commit` | `dirty` |
| --- | --- | --- | --- |
| serving build (the MCP tool surface) | the main checkout's `mcp/src/agents_remember` | `f0313143` | `False` |
| worktree-bound (the candidate's own code) | `…/260915-ks-l23-ar/260915-ks-l23/mcp/src/agents_remember` | `c5a74a85` | `True`, `sourceDigest sha256:229170c6…` |

**One trap the same route carries, measured while taking that worktree-bound run.** An *undeclared*
interpreter running from a linked worktree is classified by
`kernel/primitives/checkout_coordination.py:checkout_cli_location` as checkout-CLI mode, so
`load_config` swaps in the leaf's synthetic dev coordination root
(`<worktree group>/provider-runtime/dev-ar-coordination`) and every configured-contract authority
check then refuses with `ConfiguredContractAuthorityError(side="task", name="coordination-root")` —
the contract lives in the real coordination root. A worktree-bound run must therefore declare
itself first (`declare_test_process()`, the same call pytest's bootstrap makes); with that
declaration the run resolves the real authority and writes nothing outside the enclosure's
`reports/`.

## 260928-MIK-L96 The install host step

The install entry now composes the host step after its existing steps: a configured host is provisioned or previewed, its report is the result's `host` part, and a failing host step keeps the earlier steps while setting `ok` false.

- The composition with the host part. [4]
