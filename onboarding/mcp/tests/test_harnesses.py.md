# test_harnesses.py

| Field                  | Value                                            |
| ---------------------- | ------------------------------------------------ |
| repository             | agents-remember                                  |
| path                   | `mcp/tests/test_harnesses.py`                    |
| doc_type               | `file-level-onboarding`                          |
| lastUpdated            | 2026-07-10T13:03+02:00                           |
| lastVerifiedCommitHash | `409891a4bea54f3b6c3a125611afe54c41cca661`       |
| lastVerifiedCommitDate | 2026-07-14T10:43:35+02:00|
| governingOverview      | `../overview.md`                              |

## Purpose

`test_harnesses.py` covers the harness launch registry (`serving/harnesses.py`, slice 6e-2b): the
curated supported set, `find_harness`, detection (`is_detected` / `detect_harnesses`) driven by
an injected `which` so the suite is deterministic regardless of what is installed on the test box,
and — since 260703-L16 — the per-harness knob→flag mapping (`KnobMappingTests`).

## Code Commentary

### 260713-PHA-L1 Codex and settings-menu coverage

The final tests distinguish builtin Codex's stripped-non-empty model-advertised effort policy from
settings-defined `effortFlagValues`, which remain strict enumerations. They assert whitespace-only
refusal, stripped emission, loud invalid-menu refusal, and unchanged Claude/Pi behavior.

### Logic

**260707-HFX2-L15 coverage.** Codex model/effort are asserted as explicit argv with the
`model_reasoning_effort=` template; the builtin accepts stripped non-empty advertised values while
settings-declared menus remain enumerated. Pi.dev remains the env-only builtin. Invalid values refuse
before spawn according to the effective policy.

A `_which(*installed)` factory returns a `shutil.which` fake that resolves only the named commands.
`HarnessRegistryTests` assert the supported ids are exactly `["claude", "codex", "pi"]`, each harness
has a name + an `argv` equal to `(command,)`, and `find_harness` returns the known harness / `None`
for an unknown id. `DetectionTests` assert `is_detected` reflects the injected `which`, and
`detect_harnesses(which=_which("claude","codex"))` marks claude+codex detected and pi not, in
registry order (a full `DetectedHarness` list equality). `KnobMappingTests` (L16) pin the knob
surface: claude's `knob_argv` emits `--model`/`--effort` (empty with no knobs), its effort
vocabulary is the two-vehicle union `low|medium|high|xhigh|max` + `ultracode`,
`effort_session_commands` routes `ultracode` to `/effort ultracode` while flag values never leak
into the session vehicle, `invalid_effort_detail` names the harness and BOTH value sets (and passes
in-vocabulary values from either vehicle), and mapping-less codex/pi are env-only and unvalidated
(empty argv/vocabulary, `None` detail for anything).

### Conventions

Inserts `mcp/src` on `sys.path` (suite idiom). The `assert x is not None` narrowing keeps pyright
happy on the `find_harness` `Harness | None` returns. Detection is exercised purely through injected
fakes here; the *endpoint* detection path (`GET /api/harnesses`, monkeypatching `shutil.which`) lives
in `test_terminal_ws.py`.

## Repo-Internal References

| Finding | Source Path |
| --- | --- |
| The registry under test. | [serving/harnesses.py](agents-remember/mcp/src/agents_remember/serving/harnesses.py) |
| The endpoint-level harness tests (GET detection + the harness opener). | [test_terminal_ws.py](agents-remember/mcp/tests/test_terminal_ws.py) |

## Update History
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
