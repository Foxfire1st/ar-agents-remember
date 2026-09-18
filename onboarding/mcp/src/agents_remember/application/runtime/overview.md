# mcp/src/agents_remember/application/runtime/ — Runtime Application Operations

| Field | Value |
| --- | --- |
| repository | agents-remember |
| sourceRoute | `mcp/src/agents_remember/application/runtime/` |
| doc_type | `route-local-overview` |
| lastUpdated | 2026-08-30T17:08:05+02:00 |
| lastVerifiedCommitHash | `5e4eb651be0691e2d2a90ea59bc662f92050db25` |
| lastVerifiedCommitDate | 2026-09-18T20:35:53+02:00|
| governingOverview | `../overview.md` |

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

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| Startup owns MCP process declaration, collaborator installation, and the serving-build payload gateway. | `declare_mcp_process`; `initialize_mcp_application`; `mcp_serving_build_payload`; `prepare_mcp_process` | mcp/src/agents_remember/application/runtime/startup.py:22-27; mcp/src/agents_remember/application/runtime/startup.py:30-33; mcp/src/agents_remember/application/runtime/startup.py:54-56; mcp/src/agents_remember/application/runtime/startup.py:59-62 |
| Runtime installation is a thin typed delegation. | `run_runtime_install` | mcp/src/agents_remember/application/runtime/install.py:15-19 |
| Skill installation resolves the configured harness skill root and delegates the copy. | `skills_install_tool` | mcp/src/agents_remember/application/runtime/skills.py:13-30 |

## Docs References

No Domain Documentation source is configured.

## Cross-Repo References

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

## Update History
- 2026-09-18T17:30:57+00:00: Generated citation repair: `declare_mcp_process`; `initialize_mcp_application`; `mcp_serving_build_payload`; `prepare_mcp_process` repointed to mcp/src/agents_remember/application/runtime/startup.py:54-56; mcp/src/agents_remember/application/runtime/startup.py:22-27; mcp/src/agents_remember/application/runtime/startup.py:30-33; mcp/src/agents_remember/application/runtime/startup.py:59-62. No content impact: mechanical anchor-range projection bound to citation source snapshot 90ac134ffc3f8e781bc1feb4daa6ea3e6fd982366fb532c5a9c6ca2e3d9aa040; claim bytes unchanged; generated by ccr-r10@v1.

- 2026-09-18T19:14+02:00 — 260915-KS-L23 curator (uncommitted change set on `ar/260915-ks-l23`, base `c5a74a85`): **added the L23 section for `startup.py`'s `measuring_build_stamp()`** — the function item 26 adds so a count names the build that produced it (D-33), the two rulers it distinguishes side by side as measured, and the linked-worktree authority trap a worktree-bound run has to declare itself out of. The route's `## File-Level Onboarding Map` and every other claim are unchanged; the reference row for `startup.py`'s older surface is left to the citation engine. No verification stamp moves: `startup.py` is modified in the delivered working tree and closeout owns the stamp. **No route impact on any child's own contract** — the change is inside `startup.py`, whose sidecar carries it.

- 2026-08-30T17:08:05+02:00 — ARSPAWN-L4 Dagger repair: recorded the typed application boundary
  between MCP registration and serving-build ownership. Verification remains closeout-owned.

- 2026-08-13T08:40+02:00 — Created for the L23 package move that groups runtime startup, runtime install, and skill install application operations without adding a new facade. Verification metadata remains closeout-owned.
