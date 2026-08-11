# test_harnesses.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harnesses.py`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-15T23:16+02:00                           |
| lastVerifiedCommitHash | `d9a1eb82849baea6c0b86735e772a932f4bbdc7c`       |
| lastVerifiedCommitDate | 2026-08-12T00:45:15+02:00|
| governingOverview      | `overview.md`                               |

## Governing Overview

[MCP tests overview](overview.md)

## Purpose

`test_harnesses.py` covers the harness launch registry (`serving/harnesses.py`, slice 6e-2b): the
curated supported set, `find_harness`, detection (`is_detected` / `detect_harnesses`) driven by
an injected `which` so the suite is deterministic regardless of what is installed on the test box,
and the native-versus-settings-defined registry mapping boundary (`KnobMappingTests`).

## Code Commentary

### 260714-ACPUI-L2 Native/Custom Registry Boundary

The changed registry expectations remove static model/effort mappings from the three built-in
native harness rows. Their model-gated vocabularies now come only from adapter discovery. Existing
helper coverage remains for settings-defined custom harnesses, where an explicit model flag,
effort flag/menu, or effort session template is still a legitimate declared mapping rather than a
fallback for Claude, Codex, or Pi.

### Logic

A `_which(*installed)` factory returns a `shutil.which` fake that resolves only the named commands.
`HarnessRegistryTests` assert the supported ids are exactly `["claude", "codex", "pi"]`, each harness
has a name + an `argv` equal to `(command,)`, and `find_harness` returns the known harness / `None`
for an unknown id. `DetectionTests` assert `is_detected` reflects the injected `which`, and
`detect_harnesses(which=_which("claude","codex"))` marks claude+codex detected and pi not, in
registry order (a full `DetectedHarness` list equality). `KnobMappingTests` assert every builtin
returns empty `knob_argv`, effort vocabulary, and effort session commands and has no static invalid
effort detail. A constructed settings-defined custom row proves its explicit model/effort flags,
enumerated vocabulary, and loud invalid-effort detail remain registry-owned.

### Conventions

Inserts `mcp/src` on `sys.path` (suite idiom). The `assert x is not None` narrowing keeps pyright
happy on the `find_harness` `Harness | None` returns. Detection is exercised purely through injected
fakes here; the *endpoint* detection path (`GET /api/harnesses`, monkeypatching `shutil.which`) lives
in `test_terminal_ws.py`.

### Invariants And Boundaries

- Built-in registry rows describe identity, command, and detection only; adapters own native spend.
- Dynamic per-install model and effort catalogs must not be hardcoded here.
- Static knob helpers apply only when settings explicitly define the mapping.

### Todos

No file-local todos.

## Docs References

The resolved source registry has no Domain Documentation entries, so no live source was available
for this repository-specific registry contract. Repository source and normalized adapter tests are
the direct evidence.

| Finding | Anchor | Source |
| --- | --- | --- |
| No Domain Documentation source is configured for this repository. | n/a | n/a |

## Repo-Internal References

| Finding | Anchor | Source |
| --- | --- | --- |
| The registry under test. | `find_harness` | mcp/src/agents_remember/serving/harnesses.py:61-70 |
| The endpoint-level harness tests (GET detection + the harness opener). | `test_get_harnesses_lists_supported_set_with_detection` | mcp/tests/test_terminal_ws_websocket_2.py:192-202 |

## Cross-Repo References

No sibling repository defines this registry boundary.

| Finding | Anchor | Source |
| --- | --- | --- |
| No meaningful cross-repo references found. | n/a | n/a |

## Update History
- 2026-08-03T03:06:00+02:00 — 260731-EFA-L6-W3-B01 curator: curated 2 Repo-Internal table citations with exact registry and endpoint test anchors. Verification metadata remains unchanged for closeout.

- 2026-07-15T23:16+02:00 — 260714-ACPUI-L2 curator: documented removal of static built-in launch
  mappings and retention of explicit settings-defined custom mappings; corrected the governing
  overview backlink and the no-configured-domain-source evidence. Verification metadata remains
  pinned until closeout stamps the L2 code commit.
- 2026-07-14T12:00+02:00 — 260713-PHA-L1 closeout remediation: corrected Codex validation prose
  and recorded dynamic-builtin versus declared-settings-menu coverage.

- 2026-07-10T13:03+02:00 — 260707-HFX2-L15: replaced mapping-less-Codex expectations with explicit
  argv/template/enum coverage while preserving Pi.dev's env-only behavior. Verification metadata
  remains pinned until closeout stamps the eventual L15 code commit.

- 2026-07-07T09:45+02:00 — 260703-L16 (spawn knob application): added `KnobMappingTests` — claude
  model/effort flag mapping, the two-vehicle effort vocabulary (flag set + session-only
  `ultracode`), session-command routing, the refusal detail naming both value sets, and the
  env-only/unvalidated posture of mapping-less builtins. Existing registry/detection tests
  unmodified. Verification metadata pinned until closeout stamps the L16 commit.

- 2026-06-18T21:27+02:00 — Created for task 6 slice 6e-2b: covers `serving/harnesses.py` (the curated
  set, `find_harness`, `is_detected`/`detect_harnesses` via an injected `which`). Verification
  metadata pinned to the task base until closeout stamps the 6e-2b code commit.
