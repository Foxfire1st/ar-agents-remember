# mcp/src/agents_remember/serving/build_info.py

| Field                  | Value                                           |
| ---------------------- | ----------------------------------------------- |
| repository             | agents-remember                                 |
| path                   | `mcp/src/agents_remember/serving/build_info.py` |
| doc_type               | `file-level-onboarding`                         |
| lastUpdated            | 2026-08-01T08:30+02:00                          |
| lastVerifiedCommitHash | `1580f92715ff93c988f9a15439ad9bec60ef4c5d`      |
| lastVerifiedCommitDate | 2026-08-13T00:18:59+02:00|
| governingOverview      | `overview.md`                                   |

## Governing Overview

[serving overview](overview.md)

## Purpose

The serving **build stamp** (260703-L15): resolves ONCE at app creation which code is answering —
package version, best-effort commit short-hash, process boot time — so the cockpit can render it
and a stale serving process (the July-4 ghost-process lesson) is visible at a glance instead of
silently serving an old build.

## Code Commentary

### 260731-EFA-L4 Current Delta — `payload()` Returns A Declared Model

`ServingBuild.payload()` cit:(["def payload(self) -> ServingBuildPayload:"], mcp/src/agents_remember/serving/build_info.py:77-77) no longer hand-builds a `dict[str, Any]`. It returns
**`ServingBuildPayload`** cit:(["class ServingBuildPayload(BaseModel):"], mcp/src/agents_remember/serving/build_info.py:43-43), a `BaseModel` with `extra="forbid"` and the five camelCase
fields the dict carried: `version`, `bootedAt`, `commit`, `dashboardBuild`, `dirty`. A model
rather than an untyped dict because this object is now a *field* of the served state contract
(`served_state.ServedWorkspaceProjection.servingBuild`), and a contract whose members are
untyped dicts only pretends to be one.

**The honest-unknown rule moved from a chain of `if` statements into `None` + the caller's
`exclude_none=True`, and it is the same rule.** The old `payload()` appended `commit`,
`dashboardBuild` and `dirty` only when each was set; the new one always constructs them and
declares them optional, and every caller serializes with
`model_dump(mode="json", exclude_none=True)` (`served_state.served_state_tail`), so an
unresolvable commit, an unbuilt dashboard bundle and an unprovable tree are all OMITTED exactly
as before. The one conditional that survives in code is the dirty collapse — `dirty=True if
self.dirty else None` — because the tri-state must not leak: proven-clean (`False`) and
unprovable (`None`) both drop out, so the wire never fabricates a "clean" fact. Absence is not a
pristine claim.

**No bytes moved.** `test_serving.py`'s `_build_wire(build)` helper cit:(["return build.payload().model_dump("], mcp/tests/test_serving.py:94-94) is the one place
the tests express "the stamp exactly as the state body carries it"
(`build.payload().model_dump(mode="json", exclude_none=True)`), and every assertion that used to
call `build.payload()` directly now goes through it against the same expected dicts.

This entry supersedes any earlier description in this sidecar that conflicts with the current
source behavior above; verification metadata stays pinned to the pre-commit source history until
closeout.

### 260731-EFA-L1 Current Delta — `dashboardBuild` Is Now Routinely Absent

`_dashboard_build_fingerprint()` reads `package_data/dashboard.fingerprint`, and that sidecar is a
**generated artifact written next to the generated bundle** by `scripts/sync-dashboard.py` during
the release build. Neither is in version control (master decision OQ6, 2026-07-31). The two are
therefore absent together and present together:

- An **installation** (wheel or sdist) carries a cockpit and stamps which sources produced it. The
  release job asserts both files are in the distributions, so a published artifact always has it.
- A **source checkout** that never ran a frontend build carries neither, and `dashboardBuild` is
  simply omitted from the wire.

`None` therefore does **not** mean "legacy bundle" any more — it means no bundle was built here.
Omission follows the same honest-unknown rule as `commit` and `dirty`: never report a build
identity for a bundle that is not being served. Callers must treat `dashboardBuild` as optional;
`test_serving.py::BuildInfoTests` asserts present-or-omitted rather than indexing it.

The value itself is meaningful only because `sync-dashboard.py` reads it back out of the bundle's
own compiled `__AR_DASHBOARD_BUILD__` literal instead of stamping it over the tree, which is what
makes the cockpit's `CLIENT_DASHBOARD_BUILD` comparison a real staleness signal.

### FEUI-L9R Reviewed Candidate Delta

`ServingBuild` carries optional `dashboard_build`, serialized as `dashboardBuild`. Resolution
reads the packaged `dashboard.fingerprint` once at serving boot through `importlib.resources`.
Missing, unreadable, undecodable, or empty fingerprint data yields `None` and omission from the wire
rather than a fabricated identity; version, commit, and boot-time behavior is unchanged.

`ServingBuild(version, commit, booted_at)` is a frozen dataclass; `payload()` returns the
camelCase wire form — since **260731-EFA-L4** the declared `ServingBuildPayload` model rather
than a hand-built dict, with a `None` commit dropped by the caller's `exclude_none=True`. The
stamp never fakes a hash it could not resolve.

`resolve_serving_build(*, anchor=None)` composes the stamp: `version` from
`agents_remember.mcp.SERVER_VERSION` (the same identity the daemon's restart-on-version-mismatch
uses), `commit` via `_git_short_head` (`git rev-parse --short HEAD` anchored at the installed
package directory — git walks up to the enclosing checkout), `booted_at` from
`observer.events.now_iso()`. `_git_short_head` is best-effort by construction: fixed argv, a 2 s
bound, every exception suppressed to `None` — from an installed wheel (no git metadata) the
stamp serves version-only, never a crash.

### 260731-EFA-L3 — Both Probes Run On The One Git Runner

This module no longer spawns git itself. cit:([`_git_short_head`], mcp/src/agents_remember/serving/build_info.py:91-101) and `_git_worktree_dirty`
cit:(["def _git_worktree_dirty("], mcp/src/agents_remember/serving/build_info.py:104-104) each call `run_git` from `agents_remember.kernel.git_command` — the package's single
runner — with the module's own bound:

```python
_PROBE_TIMEOUT_SECONDS = 2
...
result = run_git(anchor, ["rev-parse", "--short", "HEAD"], timeout=_PROBE_TIMEOUT_SECONDS)
```

Two things change for the stamp, both in its favour:

- **The stamp now describes the checkout the server was started from.** The removed local
  `subprocess.run` passed no `env=`, so an exported `GIT_DIR` (worktree tooling, hooks, a wrapping
  git invocation) selected the repository and the probe would stamp *that* repository's HEAD and
  dirtiness onto this process. `run_git` strips the whole `GIT_DIR` family before every call.
- **`safe.directory` is no longer a failure mode.** `run_git` always passes
  `-c safe.directory=<repo_root>`, so a checkout owned by another user resolves instead of failing
  the probe into an honest-but-avoidable `None`.

`_PROBE_TIMEOUT_SECONDS` is kept deliberately tighter than the runner's general
`GIT_LOCAL_TIMEOUT_SECONDS` (300): this probe rides app creation, so a git that does not answer in
two seconds must read as "unstampable" like any other failure rather than delay boot. Everything
else is unchanged — fixed argv, stdin `DEVNULL` (the runner's default, so the probe can never touch
the MCP stdio protocol pipes), and every exception still suppressed to the honest `None`/`None`.

## Invariants And Boundaries

- **Boot-time only** — `create_app` calls `resolve_serving_build()` once; no per-request work
  and no per-tick work rides the stamp.
- **Never faked** — `commit` is `None` (and omitted from the payload) whenever the resolve
  fails; the payload's `version` alone then carries the identity.
- The stamp is **app-layer, not reducer truth**: it rides `/api/state` and the SSE `snapshot`
  (`serving/app.py`), never `WorkspaceProjection` or the persisted `latest-state.json`. Since
  **260731-EFA-L4** it is no longer *injected* into an undeclared dict either — the
  `servingBuild` key is declared on `served_state.ServedWorkspaceProjection`, the serving-layer
  subclass that exists precisely so this app-layer fact never becomes a projection field.

### Logic

Resolution combines package version, best-effort checkout commit, boot time, and the optional
packaged dashboard fingerprint into one immutable boot stamp.

### Conventions

Internal names are snake_case dataclass fields; `payload()` is the sole camelCase wire serializer.

### Invariants And Boundaries

Unavailable commit or fingerprint evidence is omitted, never guessed, and the fingerprint is read
from package resources rather than recomputed at request time.

### Todos

No task-independent technical debt was identified during FEUI-L9R review.

## Docs References

No relevant documentation was found after checking the configured sources; packaged-build behavior
is proven by repository source and tests.

| Finding | Anchor | Source |
| --- | --- | --- |
| No relevant external or domain documentation was found for this repository-local build stamp. | — | — |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The two merge points: the SSE snapshot and the `/api/state` body, both now via `served_state_tail` onto a copy of the memoized projection dump. |"payload.update(served_state_tail("; "served_state_tail(build=runtime.build"|mcp/src/agents_remember/code_quality/wire_contract.py:13-13; mcp/src/agents_remember/serving/_app_routes.py:97-97|
| The declaration of the `servingBuild` key, and the tail builder that applies this module's honest-unknown rule with `exclude_none=True`. | `ServedWorkspaceProjection`; `served_state_tail` | mcp/src/agents_remember/serving/served_state.py:47-55; mcp/src/agents_remember/serving/served_state.py:63-78 |
| `SERVER_VERSION` supplies the wheel version in the daemon restart identity through the kernel resolver, which uses installed package metadata with a source-checkout literal fallback (kernel-owned since L9). | `_resolve_server_version` | mcp/src/agents_remember/kernel/primitives/version.py:14-23 |
| The cockpit compares and renders the serving/client identity. | "function ServingBuildStamp()" | dashboard/src/cockpit/Cockpit.tsx:931-931 |
| The fingerprint sidecar this module reads is generated at release time beside the generated bundle, and is written only after a build that carries the same value. | "if not bundle_is_current(fingerprint):"; "FINGERPRINT_FILE.write_text(" | scripts/sync-dashboard.py:147-147; scripts/sync-dashboard.py:157-157 |
| The release job fails if either the bundle or this sidecar is missing from the wheel or sdist. | "agents_remember/package_data/dashboard/index.html"; "agents_remember/package_data/dashboard.fingerprint" | .github/workflows/publish-mcp-to-pypi.yml:93-94 |
| `test_resolves_commit_in_a_git_checkout` asserts `dashboardBuild` present-or-omitted rather than indexing it unconditionally, through the shared `_build_wire` helper that names the wire form. | `test_resolves_commit_in_a_git_checkout`; "return build.payload().model_dump(" | mcp/tests/test_serving.py:94-94; mcp/tests/test_serving_cli.py:40-55 |
| The one runner both probes call: `GIT_REPOSITORY_SELECTOR_ENV` (the `GIT_DIR` family stripped by `git_environment`) and `run_git` itself (`safe.directory`, stdin `DEVNULL`, caller-supplied `timeout`). | "GIT_REPOSITORY_SELECTOR_ENV = ("; "def git_environment() ->"; "def run_git(" | mcp/src/agents_remember/kernel/git_command.py:34-34; mcp/src/agents_remember/kernel/git_command.py:85-85; mcp/src/agents_remember/kernel/git_command.py:94-94 |
| `DecoyRepositoryTests` sets the selectors against a decoy repository and proves reads and writes still answer from the real one; `SingleRunnerTests.test_only_the_kernel_module_defines_a_git_runner` keeps this module from growing a private copy again. | `test_reads_answer_from_the_real_repository_not_the_decoy`; `test_only_the_kernel_module_defines_a_git_runner` | mcp/tests/test_git_command.py:191-209; mcp/tests/test_git_command.py:511-528 |

## Cross-Repo References

No meaningful cross-repository implementation source governs this repository-local build stamp.

| Finding | Anchor | Source |
| --- | --- | --- |
| The reviewed behavior is wholly repository-local. | — | — |

## 260718-CHATS-L5I Current Delta

Serving build identity now distinguishes a proven dirty checkout from an unprovable one. Only a successful `git status --porcelain` with output emits `dirty`; probe failure omits the claim instead of fabricating a clean build state.

This entry supersedes any earlier description in this sidecar that conflicts with the current source behavior above; verification metadata stays pinned to the pre-commit source history until closeout.

## Update History
- 2026-08-12T20:25+02:00 — L23 curator: re-read the serving identity claim after package-version resolution moved behind `_resolve_server_version`; behavior remains installed metadata with a source-checkout fallback. Verification remains closeout-owned.
- 2026-08-12T15:19+02:00 — L23 curator: re-read the current source-backed claims and retained their wording while the sanctioned MCP citation-fix wave regenerated exact ranges; verification provenance remains closeout-owned.

- 2026-08-12T10:20+02:00 — Citation maintenance only: re-anchored the kernel version identity
  after the release leaf named its existing metadata/fallback resolver; serving behavior is
  unchanged. Verification metadata remains pinned until closeout.

- 2026-08-08T17:18+02:00 — 260731-EFA-L9 curator: body verified against the current worktree after the model-extraction/caller-rewrite wave; stale moved-path references repaired and the L9 change recorded. Verification metadata pinned until closeout stamps the L9 code commit.

- 2026-08-02T22:10:00+02:00 — 260731-EFA-L6 W2-B05 curator: anchored 13 citation items (7 table rows and 6 prose citations); scoped citation check now passes.

- 2026-08-01T08:30+02:00 — 260731-EFA-L4 curator: recorded the new `ServingBuildPayload`
  cit:(["class ServingBuildPayload(BaseModel):"], mcp/src/agents_remember/serving/build_info.py:43-43) and `payload()`'s cit:(["def payload(self) -> ServingBuildPayload:"], mcp/src/agents_remember/serving/build_info.py:77-77) return-type change from `dict[str, Any]` to that model,
  including where the honest-unknown rule now lives — `None` on every best-effort field plus the
  caller's `exclude_none=True`, with the tri-state `dirty` still collapsed in code so
  proven-clean and unprovable both drop out. Corrected the FEUI-L9R sentence that still described
  `payload()` as returning a camelCase dict, and the boundary bullet that said the stamp is
  "injected" — the `servingBuild` key is now declared on
  `served_state.ServedWorkspaceProjection`. Repaired 4 citations: the two in-file probe ranges
  the 24 new lines above them invalidated (`_git_short_head` L67-L77 → L91-L101,
  `_git_worktree_dirty` L80-L94 → L104-L118); the `app.py` row, whose `L195-L202` is now the
  `served_state` import block and never held the injection points at all — replaced with the two
  real merge sites, L328-L329 (SSE snapshot) and L979-L982 (`/api/state`); and the
  `test_serving.py` row, whose `L945-L951` now spans the class header and the first asserts —
  the present-or-omitted branch is at L947-L962, cited with the new `_build_wire` helper at
  L128-L136. Wire bytes unchanged. Verification metadata pinned until closeout stamps the L4
  commit.

- 2026-07-31T20:55+02:00 — 260731-EFA-L3 curator: this module lost its two local `subprocess.run`
  copies. Corrected the FEUI-L9R sentence that described `_git_short_head` as a subprocess of its
  own and added the delta section: both probes now call `run_git`
  (`agents_remember.kernel.git_command`) with `timeout=_PROBE_TIMEOUT_SECONDS` (2), so they inherit
  the `GIT_DIR`-family scrub — the removed local runner passed no `env=`, and an exported `GIT_DIR`
  would have stamped another repository's HEAD and dirtiness onto this process — plus
  `-c safe.directory=<anchor>`. The 2 s bound, the fixed argv, the `DEVNULL` stdin and the
  fail-open `None`/`None` honesty are all unchanged. Re-verified the `test_serving.py` L945-L951
  citation against the current file (still the present-or-omitted `dashboardBuild` assertion) and
  added references for the runner and its decoy-repository proof. Verification metadata pinned
  until closeout stamps the L3 commit.

- 2026-07-31T17:20+02:00 — 260731-EFA-L2 curator: repaired 1 cross-file line citation that ran past
  the end of `mcp/src/agents_remember/mcp/__init__.py`, which is 11 lines, not 20. `SERVER_VERSION`
  is the `importlib.metadata.version("agents-remember-mcp")` lookup at L7-L11 with a
  `PackageNotFoundError` fallback literal for source checkouts; narrowed the range to L7-L11 and
  said so in the claim.

- 2026-07-31T04:28+02:00 — 260731-EFA-L1: the dashboard bundle and its `dashboard.fingerprint`
  sidecar left version control and are now generated by the release job, so `dashboardBuild` is
  routinely absent in a source checkout and routinely present in an installation. Corrected the
  docstring-derived reading that `None` means "legacy bundle". No behavioral change to this
  module beyond its docstring. Verification metadata pinned to the pre-leaf source authority until
  closeout stamps the code commit.

- 2026-07-24T13:18:47Z — 260718-CHATS-L5I curator: corrected the source-side behavior record for the current backend/shared delta and preserved the pre-commit verification stamp.

- 2026-07-18T12:43+02:00 — FEUI-L9R: recorded the packaged dashboard fingerprint and honest
  omission fallback; verification metadata remains pinned pending candidate closeout.

- 2026-07-07T05:00+02:00 — Created for 260703-L15 S3 (stale-server visibility): boot-time
  `ServingBuild` stamp + best-effort `_git_short_head` + `resolve_serving_build`.
  Verification metadata pinned until closeout stamps the L15 commit.
